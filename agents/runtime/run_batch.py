#!/usr/bin/env python3
"""Bounded OMM-NY draft pipeline. No model calls, approvals, deployments or git writes."""
import argparse
import csv
import hashlib
import html
import io
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

NOTICE = 'DRAFT - NOT CLINICALLY APPROVED'
ROLES = ['orchestrator', 'skills', 'research', 'synthesis', 'production', 'publisher']


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def load_records(path, keys=('items', 'records')):
    """Read genuine JSON/CSV; remove only a recognized legacy CSV extraction wrapper."""
    text = Path(path).read_text(encoding='utf-8-sig')
    if Path(path).suffix == '.json':
        obj = json.loads(text)
        records = obj if isinstance(obj, list) else next((obj[k] for k in keys if k in obj), None)
    else:
        lines = text.splitlines()
        if lines and lines[0].startswith('<PARSED TEXT FOR SHEET:'):
            end = next((i for i, line in enumerate(lines) if line.startswith('TAB NAME:') and line.endswith('>')), None)
            if end is None:
                raise ValueError('Malformed CSV wrapper; refusing to guess')
            text = '\n'.join(lines[end + 1:])
        records = list(csv.DictReader(io.StringIO(text)))
        for record in records:
            record.pop('index', None)
    if not isinstance(records, list) or not records or not all(isinstance(r, dict) for r in records):
        raise ValueError('Missing or empty inventory is NOT completion')
    return records


def build_queue(rows):
    seen, queue = set(), []
    for row in rows:
        uid = row['id']
        week = int(row['week'])
        if uid in seen or not re.fullmatch(r'OMM-W\d{2}-S\d{2}', uid) or not 1 <= week <= 26:
            raise ValueError('Invalid or duplicate curriculum unit')
        if int(uid[5:7]) != week or not str(row.get('subtopic', '')).strip():
            raise ValueError('ID/week mismatch or missing subtopic')
        seen.add(uid)
        queue.append({'id': uid, 'week': week, 'topic': row['subtopic'],
                      'status': 'not_started', 'complete': False,
                      'legacy_proposal_url': row.get('reference_url'),
                      'legacy_track': row.get('reference_track'),
                      'source_verification': 'not_reverified', 'human_approval': None})
    if {q['week'] for q in queue} != set(range(1, 27)):
        raise ValueError('Inventory must represent all 26 weeks')
    return queue


def validate_card(card):
    if card.get('clinical_approval_status') != 'not_approved' or card.get('clinical_reviewer') is not None:
        raise ValueError('This draft-only runner cannot accept or create clinical approval')
    if not card.get('blockers') or not card.get('sources') or not card.get('documents'):
        raise ValueError('Explicit evidence provenance and review blockers are required')
    source_ids = {s['id'] for s in card['sources']}
    for source in card['sources']:
        if not source['url'].startswith('https://'):
            raise ValueError('Source URL must use HTTPS')
    for doc in card['documents']:
        if doc['source_id'] not in source_ids or not doc.get('highlight'):
            raise ValueError('Each selected document needs one sourced highlight')
        if not doc.get('locator') or not doc.get('x1_linkage_status'):
            raise ValueError('Source locator and honest X1 linkage status required')
    picot = card['x1']['picot']
    if card['x1']['source_id'] not in source_ids or not all(picot.get(k) for k in 'PICOT'):
        raise ValueError('A primary study source and all PICOT fields are required')
    if card['x1'].get('design') != 'randomized_controlled_trial':
        raise ValueError('This pilot card expects an original randomized trial, not a review')
    return True


def produce(card, queue, out):
    out.mkdir(parents=True, exist_ok=True)
    esc = html.escape
    source_map = {s['id']: s for s in card['sources']}
    md = [f'# {card["title"]}', '', NOTICE, '', card['scope'], '']
    for doc in card['documents']:
        source = source_map[doc['source_id']]
        md += [f'## {source["title"]}', doc['highlight'],
               f'Locator: {doc["locator"]}', f'X1 linkage: {doc["x1_linkage_status"]}',
               f'Source: {source["url"]}', '']
    md += ['## X1 - SPRINT (2015)', card['x1']['linkage_note']]
    for key, value in card['x1']['picot'].items():
        md += [f'{key}: {value}']
    md += ['Limitations: ' + card['x1']['limitations'], '', '## Blockers']
    md += ['- ' + value for value in card['blockers']]
    md += ['', '## Source register']
    md += [f'{s["id"]}: {s["title"]}\n{s["url"]}\nCheck: {s["verification"]}' for s in card['sources']]
    (out / 'hypertension.md').write_text('\n\n'.join(md), encoding='utf-8')
    cards = ''.join(f'<article><h2>{esc(source_map[d["source_id"]]["title"])}</h2>'
                    f'<p>{esc(d["highlight"])}</p><small>{esc(d["locator"])}</small></article>'
                    for d in card['documents'])
    picot = ''.join(f'<dt>{k}</dt><dd>{esc(v)}</dd>' for k, v in card['x1']['picot'].items())
    sources = ''.join(f'<li><a href="{esc(s["url"], quote=True)}" rel="noopener noreferrer">'
                      f'{esc(s["title"])}</a> - {esc(s["verification"])}</li>' for s in card['sources'])
    page = ('<!doctype html><html lang="en"><meta charset="utf-8">'
            '<meta name="viewport" content="width=device-width,initial-scale=1">'
            '<title>OMM-NY | Hypertension draft</title><style>'
            'body{font:17px/1.6 system-ui;max-width:1000px;margin:36px auto;padding:0 24px;color:#18354d}'
            'article{background:#f2f6fa;border-left:4px solid #21677d;padding:20px;margin:20px 0}'
            '.notice{background:#fff1d4;padding:15px}dt{font-weight:700}dd{margin-bottom:15px}'
            'a{color:#075a83}small{color:#526575}</style>'
            f'<header><p>OPEN MEDICINE MANUAL NY / WEEK 01</p><h1>{esc(card["title"])}</h1></header>'
            f'<p class="notice">{NOTICE}. Source linkage and clinician review remain open.</p>'
            f'<p>{esc(card["scope"])}</p>{cards}<h2>X1: SPRINT (2015)</h2>'
            f'<p>{esc(card["x1"]["linkage_note"])}</p><dl>{picot}</dl>'
            f'<p>{esc(card["x1"]["limitations"])}</p><h2>Unresolved work</h2><ul>'
            + ''.join(f'<li>{esc(b)}</li>' for b in card['blockers'])
            + f'</ul><h2>References</h2><ol>{sources}</ol></html>')
    (out / 'hypertension.html').write_text(page, encoding='utf-8')
    (out / 'draft_index.json').write_text(json.dumps({'notice': NOTICE, 'drafts': [card['unit_id']],
        'indexed_complete': [], 'total_units': len(queue)}, indent=2) + '\n', encoding='utf-8')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path('.'))
    args = parser.parse_args(argv)
    root = args.root.resolve()
    proposal = root / 'research/normalized/curriculum_subtopics.json'
    card_path = root / 'research/drafts/OMM-W01-S01.json'
    queue = build_queue(load_records(proposal))
    card = json.loads(card_path.read_text())
    validate_card(card)
    unit = next((u for u in queue if u['id'] == card['unit_id']), None)
    if unit is None:
        raise ValueError('Evidence card has no matching curriculum unit')
    unit.update(status='draft_produced_evidence_linkage_pending', blockers=card['blockers'])
    out = root / 'docs/drafts/batch-01'
    produce(card, queue, out)
    queue_path = root / 'research/agent_queue.json'
    queue_path.write_text(json.dumps({'schema_version': '1.1.0',
        'execution_status': 'local_batch_executed_remote_not_started',
        'source_inventory': 'research/normalized/curriculum_subtopics.json',
        'source_inventory_status': 'provisional_78_slots_not_exhaustive',
        'units': [{'id': u['id'], 'status': u['status'], 'complete': False} for u in queue]}, indent=2) + '\n')
    report = {'run_at_utc': datetime.now(timezone.utc).isoformat(), 'execution': 'local',
        'roles': ROLES, 'implementation': 'deterministic draft pipeline with ChatGPT-authored evidence card',
        'remote_agent': 'not_started_safety_blocked', 'weeks': 26, 'units': len(queue),
        'draft_units': 1, 'clinical_approvals': 0, 'indexed_complete': 0,
        'input_sha256': {str(p.relative_to(root)): sha(p) for p in (proposal, card_path)},
        'approval_registry_modified': False, 'network_requests': 0, 'autonomous_synthesis': False,
        'outputs': ['research/agent_queue.json', 'docs/drafts/batch-01/hypertension.html',
                    'docs/drafts/batch-01/hypertension.md', 'docs/drafts/batch-01/draft_index.json']}
    (root / 'research/batch_01_report.json').write_text(json.dumps(report, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ('execution', 'units', 'draft_units', 'clinical_approvals', 'remote_agent')}))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except (ValueError, KeyError, OSError, StopIteration) as exc:
        print(f'Blocked: {exc}', file=sys.stderr)
        raise SystemExit(1)
