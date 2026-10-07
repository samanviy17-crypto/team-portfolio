---
layout: post
title: "Golden Gate Bridge"
description: 
permalink: /west-coast/travel/sf/golden/
date: 2025-10-21
---

<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Golden Gate Bridge — Continuous Scene</title>
<style>
{{ '@import "beasts/inline/pages/hacks-west-coast-travel-sanfrancisco-goldengatebridge-1";' | scssify }}
</style>
</head>
<body>

<div class="scene" id="scene">
  <div class="sky"></div>
  <div class="orb" aria-hidden="true"></div>
  <div class="hills"></div>

  <div class="bridge" aria-label="Golden Gate Bridge">
    <svg viewBox="0 0 1600 600" preserveAspectRatio="none" role="img" aria-label="Golden Gate Bridge silhouette">
      <defs>
        <linearGradient id="fade" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="#fff" stop-opacity="1"/>
          <stop offset="100%" stop-color="#fff" stop-opacity="0"/>
        </linearGradient>
        <mask id="fadeMask"><rect x="0" y="300" width="1600" height="300" fill="url(#fade)"/></mask>
      </defs>

      <rect x="0" y="320" width="1600" height="6" fill="#222" opacity=".8"/>

      <g fill="var(--bridge)">
        <rect x="300" y="160" width="44" height="200" rx="6" />
        <rect x="1100" y="140" width="44" height="220" rx="6" />
        <rect x="290" y="190" width="64" height="10" opacity=".9"/>
        <rect x="290" y="230" width="64" height="10" opacity=".9"/>
        <rect x="1090" y="170" width="64" height="10" opacity=".9"/>
        <rect x="1090" y="210" width="64" height="10" opacity=".9"/>
      </g>

      <path id="cable1" d="M0,320 L300,160 C 500,300 900,300 1100,140 L1600,320" stroke="var(--cable)" stroke-width="6" fill="none"/>
      <path id="cable2" d="M0,320 L300,160 C 500,315 900,315 1100,140 L1600,320" stroke="var(--cable)" stroke-width="4" fill="none"/>

      <g id="hangers" stroke="var(--cable)" stroke-width="2"></g>

      <g mask="url(#fadeMask)" opacity=".25" transform="scale(1,-1) translate(0,-640)">
        <rect x="0" y="320" width="1600" height="6" fill="#000"/>
        <g fill="#000">
          <rect x="300" y="160" width="44" height="200" rx="6" />
          <rect x="1100" y="140" width="44" height="220" rx="6" />
          <rect x="290" y="190" width="64" height="10"/>
          <rect x="290" y="230" width="64" height="10"/>
          <rect x="1090" y="170" width="64" height="10"/>
          <rect x="1090" y="210" width="64" height="10"/>
        </g>
        <path d="M0,320 L300,160 C 500,300 900,300 1100,140 L1600,320" stroke="#000" stroke-width="6" fill="none"/>
        <path d="M0,320 L300,160 C 500,315 900,315 1100,140 L1600,320" stroke="#000" stroke-width="4" fill="none"/>
      </g>
    <script type="application/ecmascript"><![CDATA[
      (function(){
        const svg = document.currentScript.ownerSVGElement;
        const hangers = svg.getElementById('hangers');
        const path = svg.getElementById('cable1');
        if(!hangers || !path || !path.getTotalLength) return;
        const length = path.getTotalLength();
        function yAtX(targetX){
          let a=0, b=length, pt;
          for(let i=0;i<18;i++){
            const m=(a+b)/2; pt = path.getPointAtLength(m);
            if(pt.x < targetX) a = m; else b = m;
          }
          return pt.y;
        }
        for(let x=60;x<1540;x+=20){
          const y = yAtX(x);
          const line = document.createElementNS('http://www.w3.org/2000/svg','line');
          line.setAttribute('x1',x); line.setAttribute('x2',x);
          line.setAttribute('y1',y); line.setAttribute('y2',320);
          hangers.appendChild(line);
        }
      })();
    ]]></script>
    </svg>
  </div>

  <div class="deck"></div>
  <div class="rail" style="z-index:6"></div>

  <div class="cars" id="cars"></div>
  <div class="boats" id="boats"></div>
  <div class="buoy" style="left:22vw"></div>
  <div class="buoy" style="left:68vw;animation-duration:5.6s"></div>

  <div class="water">
    <div class="ripples"></div>
  </div>

  <div class="fog" aria-hidden="true">
    <span class="f1"></span>
    <span class="f2"></span>
    <span class="f3"></span>
  </div>

  <div class="overlay" id="overlay" aria-hidden="true"></div>
  <div class="hint">Move mouse for parallax effect</div>
</div>

<main class="lesson">
  <div class="container">
    <h1>UI Hierarchy: Golden Gate Bridge</h1>

    <h2>What is UI Hierarchy?</h2>
    <p>UI hierarchy guides users' eyes to what matters most—just like the Golden Gate Bridge's iconic towers instantly grab your attention against the San Francisco skyline. Think of it as organizing information from most important (the towers) to supporting details (the roadway).</p>

    <h2>The 3 Levels of Hierarchy</h2>

    <h3># H1: Primary (The Towers)</h3>
    <p>Most important—commanding like the 746-foot Art Deco towers. In Markdown, use # for your main page title. This is the biggest heading.</p>
    <ul>
      <li>Markdown: # Main Page Title</li>
      <li>HTML: &lt;h1&gt;Main Page Title&lt;/h1&gt;</li>
      <li>Use only once per page</li>
    </ul>

    <h3>## H2: Secondary (The Cables)</h3>
    <p>Supporting sections—like the suspension cables connecting everything. In Markdown, use ## for major sections.</p>
    <ul>
      <li>Markdown: ## Section Title</li>
      <li>HTML: &lt;h2&gt;Section Title&lt;/h2&gt;</li>
      <li>Use for main sections of your page</li>
    </ul>

    <h3>### H3: Tertiary (The Roadway)</h3>
    <p>Subsections and details—individual lanes and railings. In Markdown, use ### for subsections.</p>
    <ul>
      <li>Markdown: ### Subsection Title</li>
      <li>HTML: &lt;h3&gt;Subsection Title&lt;/h3&gt;</li>
      <li>Use for subsections within H2 areas</li>
    </ul>

    <h2>Why Heading Hierarchy Matters</h2>
    <p>The number of hashtags (#) determines importance and size. One hashtag (#) is biggest and most important. Two hashtags (##) is smaller and less important. Three hashtags (###) is smallest. This creates structure for screen readers and search engines.</p>
    <p>Always start with # and nest logically: # → ## → ###. Never skip levels (don't jump from # to ###).</p>

    <h2>Real Example: Bridge Website</h2>
    <div class="example-box">
      <p><strong># Cross the Golden Gate Bridge</strong></p>
      <p><strong>## San Francisco's Icon Since 1937</strong></p>
      <p><strong>### Visitor Information</strong></p>
      <p><strong>### History and Construction</strong></p>
      <p><strong>## Plan Your Visit</strong></p>
      <p><strong>### Parking and Transit</strong></p>
      <p><strong>### Best Photo Spots</strong></p>
    </div>

    <h2>Common Mistakes</h2>
    <ul>
      <li>Using multiple # headings on one page—use only one</li>
      <li>Skipping levels—going from # to ### without ##</li>
      <li>Using headings just to make text bigger—use them for structure</li>
      <li>Not organizing content logically—plan your hierarchy like the bridge's design</li>
    </ul>

    <h2>Quick Tips</h2>
    <ul>
      <li>One # per page (your main title)</li>
      <li>Use ## for major sections</li>
      <li>Use ### for subsections within those sections</li>
      <li>The fewer hashtags, the more important (and bigger) the heading</li>
      <li>Think of it like an outline—main point, sub-points, details</li>
    </ul>

    <h2>Test Your Knowledge Quiz!</h2>
    <p>Practice creating a heading hierarchy for a Golden Gate Bridge website. Type your headings below:</p>
    <div class="example-box">
      <label for="practice1" style="display:block;margin-bottom:10px;font-weight:600;color:#fff">Main page title (use #):</label>
      <input type="text" id="practice1" placeholder="# Your title here" style="width:100%;margin-bottom:20px;">
      
      <label for="practice2" style="display:block;margin-bottom:10px;font-weight:600;color:#fff">First major section (use ##):</label>
      <input type="text" id="practice2" placeholder="## Your section here" style="width:100%;margin-bottom:20px;">
      
      <label for="practice3" style="display:block;margin-bottom:10px;font-weight:600;color:#fff">A subsection (use ###):</label>
      <input type="text" id="practice3" placeholder="### Your subsection here" style="width:100%;margin-bottom:20px;">
      
      <button onclick="checkHierarchy()">Check My Hierarchy</button>
      <div id="feedback" style="margin-top:20px;padding:15px;border-radius:5px;display:none;"></div>
    </div>
  </div>
</main>
<script>
function checkHierarchy() {
  const input1 = document.getElementById('practice1').value.trim();
  const input2 = document.getElementById('practice2').value.trim();
  const input3 = document.getElementById('practice3').value.trim();
  const feedback = document.getElementById('feedback');
  
  let messages = [];
  let correct = 0;
  
  if(input1.startsWith('# ') && !input1.startsWith('## ')) {
    messages.push('✅ Perfect! Your main title uses one #');
    correct++;
  } else {
    messages.push('❌ Main title should start with one # (not ## or ###)');
  }
  
  if(input2.startsWith('## ') && !input2.startsWith('### ')) {
    messages.push('✅ Great! Your section uses ##');
    correct++;
  } else {
    messages.push('❌ Section should start with ## (two hashtags)');
  }
  
  if(input3.startsWith('### ')) {
    messages.push('✅ Excellent! Your subsection uses ###');
    correct++;
  } else {
    messages.push('❌ Subsection should start with ### (three hashtags)');
  }
  
  feedback.style.display = 'block';
  if(correct === 3) {
    feedback.style.background = 'rgba(76,175,80,.3)';
    feedback.style.border = '2px solid #4CAF50';
    feedback.style.color = '#a5d6a7';
    feedback.innerHTML = '<strong>🎉 Perfect hierarchy!</strong><br>' + messages.join('<br>') + '<br><br>You understand heading structure!';
  } else {
    feedback.style.background = 'rgba(255,193,7,.3)';
    feedback.style.border = '2px solid #FFC107';
    feedback.style.color = '#ffd54f';
    feedback.innerHTML = '<strong>Keep trying!</strong><br>' + messages.join('<br>');
  }
}
</script>

<script>
(function(){
  const carsEl = document.getElementById('cars');
  const boatsEl = document.getElementById('boats');
  const scene = document.getElementById('scene');

  const rnd=(a=1,b=0)=>Math.random()*(a-b)+b;
  const pick=a=>a[Math.floor(Math.random()*a.length)];

  const carColors=['var(--car1)','var(--car2)','var(--car3)','var(--car4)'];
  function spawnCar(){
    const car=document.createElement('div'); car.className='car';
    car.style.background=pick(carColors);
    const dir = Math.random()<0.5?1:-1;
    const dur = rnd(12,6);
    car.style.animationDuration = dur+'s';
    if(dir<0){
      car.style.transform='scaleX(-1)';
      car.animate([
        {transform:'translateX(115vw) scaleX(-1)'},
        {transform:'translateX(-15vw) scaleX(-1)'}
      ], {duration: dur*1000, iterations: Infinity, easing:'linear'});
    }
    carsEl.appendChild(car);
    const glow=document.createElement('div');
    glow.style.cssText='position:absolute;right:-4px;top:3px;width:4px;height:3px;border-radius:2px;background:rgba(255,255,200,.9);box-shadow:0 0 8px 3px rgba(255,255,200,.9)';
    if(Math.random()<.6) car.appendChild(glow);
    setTimeout(()=>{ if(car.isConnected) car.remove(); }, dur*1000*1.2);
  }
  setInterval(spawnCar, 1300);
  for(let i=0;i<6;i++) spawnCar();

  function spawnBoat(){
    const boat=document.createElement('div'); boat.className='boat';
    boat.style.left=rnd(0,100)+'vw';
    boat.style.animationDuration=rnd(65,35)+'s';
    boat.style.animationDelay = (-Math.random()*10)+'s';
    boatsEl.appendChild(boat);
    setTimeout(()=>{ if(boat.isConnected) boat.remove();}, 70000);
  }
  setInterval(spawnBoat, 8000);
  for(let i=0;i<3;i++) spawnBoat();

  let targetRX=0,targetRY=0,rx=0,ry=0;
  function onMove(x,y){
    const cx=window.innerWidth/2, cy=window.innerHeight/2;
    targetRY = (x-cx)/cx * 4;
    targetRX = -(y-cy)/cy * 3;
  }
  window.addEventListener('mousemove', e=> onMove(e.clientX,e.clientY));
  window.addEventListener('touchmove', e=>{ if(e.touches[0]) onMove(e.touches[0].clientX,e.touches[0].clientY); }, {passive:true});

  function raf(){
    rx += (targetRX - rx)*0.05; ry += (targetRY - ry)*0.05;
    scene.style.transform = `rotateX(${rx}deg) rotateY(${ry}deg)`;
    requestAnimationFrame(raf);
  }
  requestAnimationFrame(raf);

  const water=document.querySelector('.water');
  let t=0; setInterval(()=>{ t+=0.04; water.style.transform=`translateY(${Math.sin(t)*1.5}px)`; }, 50);
})();
</script>
</body>
</html>