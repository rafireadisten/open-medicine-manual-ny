/* Rebuild from the same evidence card; install pptxgenjs in an isolated workspace. */
const fs = require('fs');
const path = require('path');
const pptxgen = require('pptxgenjs');
const root = path.resolve(process.argv[2] || '.');
const card = JSON.parse(fs.readFileSync(path.join(root, 'research/drafts/OMM-W01-S01.json')));
if (card.clinical_approval_status !== 'not_approved') throw Error('Draft-only production gate');
const helperPath = process.env.OMM_SLIDE_HELPERS;
const helpers = helperPath ? require(helperPath) : null;
const pptx = new pptxgen();
pptx.layout = 'LAYOUT_WIDE';
pptx.author = 'Open Medicine Manual NY';
pptx.subject = 'Hypertension pilot evidence draft - requires clinical review';
pptx.title = card.title;
pptx.lang = 'en-US';
pptx.theme = {headFontFace:'Aptos Display',bodyFontFace:'Aptos',lang:'en-US'};
const pages = [
  {title:'Hypertension',sub:'FIRST EXECUTION / OMM-W01-S01',body:'Targets, evidence and applicability\n\nResearch and production pilot\n26 weeks / 78 queued subtopics / 1 draft / 0 approvals',sources:[]},
  {title:'A bounded execution',sub:'ORCHESTRATION',body:'Orchestrator: preserve all 78 curriculum subtopics.\nSkills: validate available tools and input formats.\nResearch + synthesis: source-check one hypertension draft.\nProduction: generate a page and slides from one JSON card.\nPublisher: preserve an auditable GitHub record.',sources:[]},
  {title:'Current US guidance',sub:'ONE GUIDANCE HIGHLIGHT',body:card.documents[0].highlight+'\n\nThe source checked here is the official AHA summary. Exact full-guideline bibliography linkage remains open.',sources:['AHA2025']},
  {title:'Use the review as context',sub:'R1 / PUBLISHED 2024',body:card.documents[1].highlight+'\n\nThe review predates the 2025 US guideline. Its older guideline comparisons must not silently become current recommendations.',sources:['R1','AHA2025']},
  {title:'SPRINT: who and what?',sub:'CANDIDATE X1 / PICOT',body:'P  '+card.x1.picot.P+'\n\nI  '+card.x1.picot.I+'\n\nC  '+card.x1.picot.C,sources:['SPRINT2015']},
  {title:'SPRINT: outcomes and time',sub:'2015 PRIMARY REPORT',body:'O  '+card.x1.picot.O+'\n\nT  '+card.x1.picot.T,sources:['SPRINT2015']},
  {title:'Do not overgeneralize',sub:'APPLICABILITY',body:card.x1.linkage_note+'\n\n'+card.x1.limitations,sources:['SPRINT2015']},
  {title:'What blocks completion?',sub:'HUMAN REVIEW GATE',body:card.blockers.map((x,i)=>(i+1)+'. '+x).join('\n\n'),sources:['SPRINT2021','VADOD2026']},
  {title:'Source register',sub:'LINKS + PROVENANCE',body:card.sources.map(s=>s.id+'  |  '+s.title).join('\n\n'),sources:card.sources.map(s=>s.id)}
];
for (const [i,p] of pages.entries()) {
  const slide=pptx.addSlide();slide.background={color:'F5F7FA'};
  slide.addText('OPEN MEDICINE MANUAL NY',{x:.65,y:.3,w:10.5,h:.3,fontSize:12,bold:true,color:'1D566A',margin:0});
  slide.addText(p.sub,{x:.65,y:.85,w:12,h:.4,fontSize:13,bold:true,color:'5C6C79',margin:0});
  slide.addText(p.title,{x:.65,y:1.35,w:12,h:.65,fontSize:34,bold:true,color:'14354A',margin:0});
  const box={x:.65,y:2.25,w:12,h:4.15,fontSize:i===8?16:21,minFontSize:15,maxFontSize:21,mode:'shrink'};
  const layout=helpers ? helpers.autoFontSize(p.body,'Aptos',box) : {...box,fontSize:i===8?16:20};
  slide.addText(p.body,{...layout,fontFace:'Aptos',color:'244354',breakLine:false,margin:0,valign:'top',paraSpaceAfterPt:10});
  slide.addText('DRAFT - NOT CLINICALLY APPROVED',{x:.65,y:6.85,w:10.4,h:.3,fontSize:11,bold:true,color:'945D13',margin:0});
  slide.addText(String(i+1).padStart(2,'0'),{x:11.85,y:6.85,w:.75,h:.3,fontSize:11,color:'566B77',align:'right',margin:0});
  const refs=p.sources.map(id=>card.sources.find(s=>s.id===id));
  slide.addNotes('Draft pilot. No human clinical approval.\n[Sources]\n'+refs.map(s=>s.title+'\n'+s.url+'\n'+s.verification).join('\n\n')+'\n[/Sources]');
  if(helpers){helpers.warnIfSlideHasOverlaps(slide,pptx);helpers.warnIfSlideElementsOutOfBounds(slide,pptx);}
}
const out=path.join(root,'docs/drafts/batch-01/OMM_NY_Hypertension_Pilot.pptx');
fs.mkdirSync(path.dirname(out),{recursive:true});
pptx.writeFile({fileName:out,compression:true}).then(()=>console.log(out));
