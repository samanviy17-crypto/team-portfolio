---
layout: post
title: "Alcatraz"
description: 
permalink: /west-coast/travel/sf/alca
date: 2025-10-21
---
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Alcatraz Island — UI Hierarchy</title>
<style>
{{ '@import "beasts/inline/pages/hacks-west-coast-travel-sanfrancisco-alcatraz-1";' | scssify }}
</style>
</head>
<body>

<!-- Centered Scene -->
<div class="scene" id="scene" aria-label="Alcatraz Island scene">
  <div class="sky"></div>
  <div class="orb" aria-hidden="true"></div>

  <div class="fog" aria-hidden="true">
    <span class="f1"></span>
    <span class="f2"></span>
    <span class="f3"></span>
  </div>

  <div class="water"><div class="ripples"></div></div>

  <div class="island" aria-label="Alcatraz Island">
    <svg viewBox="0 0 1600 500" preserveAspectRatio="none" role="img">
      <defs>
        <linearGradient id="rockGrad" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="var(--rock1)"/>
          <stop offset="100%" stop-color="var(--rock2)"/>
        </linearGradient>
        <filter id="softBlur"><feGaussianBlur stdDeviation="1.2"/></filter>
      </defs>

      <path d="M0,300 C200,270 320,280 520,260 C700,245 880,240 1080,255 C1280,270 1400,290 1600,280 L1600,360 L0,360 Z" fill="url(#rockGrad)" stroke="var(--rock-edge)" stroke-width="3"/>
      <path d="M0,300 C200,270 320,280 520,260 C700,245 880,240 1080,255 C1280,270 1400,290 1600,280" fill="none" stroke="rgba(255,255,255,.55)" stroke-width="2" style="filter:url(#softBlur)"/>

      <g fill="var(--vegetation)">
        <ellipse cx="260" cy="250" rx="40" ry="24"/>
        <ellipse cx="330" cy="240" rx="26" ry="18"/>
        <ellipse cx="1240" cy="250" rx="34" ry="20"/>
        <ellipse cx="1160" cy="238" rx="24" ry="16"/>
      </g>

      <g transform="translate(520,150)">
        <rect x="0" y="0" width="520" height="90" rx="6" fill="var(--building)" stroke="var(--trim)" stroke-width="4"/>
        <rect x="20" y="-22" width="160" height="22" rx="4" fill="var(--roof)"/>
        <rect x="200" y="-22" width="160" height="22" rx="4" fill="var(--roof)"/>
        <rect x="380" y="-22" width="120" height="22" rx="4" fill="var(--roof)"/>
        <g fill="#8f8777">
          <rect x="36" y="24" width="28" height="28" rx="4"/>
          <rect x="84" y="24" width="28" height="28" rx="4"/>
          <rect x="132" y="24" width="28" height="28" rx="4"/>
          <rect x="230" y="24" width="28" height="28" rx="4"/>
          <rect x="278" y="24" width="28" height="28" rx="4"/>
          <rect x="326" y="24" width="28" height="28" rx="4"/>
          <rect x="418" y="24" width="28" height="28" rx="4"/>
          <rect x="466" y="24" width="28" height="28" rx="4"/>
        </g>
      </g>

      <g transform="translate(1080,110)">
        <rect x="-60" y="70" width="120" height="50" rx="6" fill="var(--building)" stroke="var(--trim)" stroke-width="4"/>
        <polygon points="-70,70 0,40 70,70" fill="var(--roof)"/>
        <rect x="0" y="-5" width="28" height="130" rx="8" fill="var(--lighthouse)" stroke="#cfcfcf" stroke-width="4"/>
        <circle cx="14" cy="-6" r="16" fill="var(--lamp)" stroke="#e1d48f" stroke-width="4"/>
      </g>

      <g class="beam" transform="translate(1094,104)">
        <path d="M0,0 L360,-40 L360,40 Z" fill="var(--beam)" style="transform-origin:0px 0px;animation: sweep 7.5s linear infinite"/>
      </g>

      <rect x="420" y="260" width="140" height="10" rx="4" fill="#8e8065"/>
      <rect x="410" y="270" width="160" height="8" rx="4" fill="#7a6b52"/>
    </svg>
  </div>

  <div class="boats" id="boats"></div>
  <div class="birds" id="birds"></div>
  <div class="overlay" id="overlay" aria-hidden="true"></div>
  <div class="hint">Move mouse: parallax effect</div>
</div>

<!-- Lesson Content -->
<div class="lesson-wrapper">
  <div class="lesson-content">
    <h1>UI Hierarchy Lesson: Alcatraz Island</h1>
    
    <p>UI hierarchy organizes elements by importance—just like Alcatraz Island, where the main cellhouse dominates while guard towers and smaller structures support the overall design.</p>

    <h2>The 3 Levels of Hierarchy</h2>
    
    <div class="hierarchy-grid">
      <div class="hierarchy-card">
        <h4>Primary (Main Cellhouse)</h4>
        <p>Most important content—as dominant as the main prison building.</p>
        <ul>
          <li>Main headlines</li>
          <li>Key call-to-action buttons</li>
          <li>Hero images</li>
        </ul>
      </div>

      <div class="hierarchy-card">
        <h4>Secondary (Guard Towers)</h4>
        <p>Supporting information—like D-Block and the watchtowers.</p>
        <ul>
          <li>Subheadings</li>
          <li>Section titles</li>
          <li>Secondary buttons</li>
        </ul>
      </div>

      <div class="hierarchy-card">
        <h4>Tertiary (Cell Details)</h4>
        <p>Additional details—individual stories and daily life.</p>
        <ul>
          <li>Body text</li>
          <li>Captions</li>
          <li>Metadata</li>
        </ul>
      </div>
    </div>

    <h2>5 Tools to Create Hierarchy</h2>

    <div class="tip-box">
      <strong>1. Size</strong>
      <p>Like the cellhouse towering over smaller buildings. Primary: 32-48px, Secondary: 24-32px, Tertiary: 14-16px</p>
    </div>

    <div class="tip-box">
      <strong>2. Weight</strong>
      <p>Thick steel bars vs. thinner mesh. Primary: Bold (700), Secondary: Semi-bold (600), Tertiary: Regular (400)</p>
    </div>

    <div class="tip-box">
      <strong>3. Color</strong>
      <p>Stark gray concrete against blue San Francisco Bay. Use high contrast for primary, medium for secondary, low for tertiary.</p>
    </div>

    <div class="tip-box">
      <strong>4. Spacing</strong>
      <p>Isolation cells created maximum separation—use white space the same way to emphasize importance.</p>
    </div>

    <div class="tip-box">
      <strong>5. Position</strong>
      <p>Visitors look up at the main building first—top and center naturally draw attention.</p>
    </div>

    <h2>Common Mistakes to Avoid</h2>
    <p>❌ Making everything important—nothing stands out<br>
    ❌ Too many font sizes—stick to 3-4 maximum<br>
    ❌ Ignoring spacing—use isolation for impact<br>
    ❌ Inconsistent styling—maintain order<br>
    ❌ Poor contrast—you need clarity</p>
  </div>
</div>

<script>
(function(){
  const rnd=(a=1,b=0)=>Math.random()*(a-b)+b;

  // Birds
  const birdsEl = document.getElementById('birds');
  const gullSVG = `
    <svg viewBox="0 0 24 12" xmlns="http://www.w3.org/2000/svg">
      <path d="M1 6 Q6 1 12 6 Q18 1 23 6" fill="none" stroke="#fff" stroke-width="2" stroke-linecap="round">
        <animate attributeName="d" dur="1.2s" repeatCount="indefinite"
          values="M1 6 Q6 1 12 6 Q18 1 23 6; M1 6 Q6 11 12 6 Q18 11 23 6; M1 6 Q6 1 12 6 Q18 1 23 6" />
      </path>
    </svg>`;
  function spawnGull(){
    const g=document.createElement('div'); g.className='gull'; g.innerHTML=gullSVG;
    g.style.left=rnd(2,10)+'vw'; g.style.top=rnd(2,10)+'vh';
    g.style.setProperty('--t', rnd(28,16)+'s');
    g.style.animationDelay = (-Math.random()*6)+'s';
    birdsEl.appendChild(g);
    setTimeout(()=>{ if(g.isConnected) g.remove(); }, 30000);
  }
  setInterval(spawnGull, 5000);
  for(let i=0;i<5;i++) spawnGull();

  // Boats
  const boatsEl = document.getElementById('boats');
  function spawnBoat(){
    const dir = Math.random()<0.5?1:-1;
    const el = document.createElement('div');
    const isFerry = Math.random()<0.45;
    el.className = isFerry ? 'ferry' : 'boat';
    const dur = rnd(70,40)*1000;
    el.style.left = (dir>0? -20 : 110)+'vw';
    el.animate([
      { transform:`translateX(0)` },
      { transform:`translateX(${dir>0? '140vw' : '-140vw'})` }
    ], { duration: dur, iterations: 1, easing:'linear' });
    boatsEl.appendChild(el);
    setTimeout(()=>{ if(el.isConnected) el.remove(); }, dur+1000);
  }
  setInterval(spawnBoat, 8000); 
  for(let i=0;i<3;i++) spawnBoat();

  // Lighthouse sweep
  const styleSweep = document.createElement('style');
  styleSweep.textContent = `@keyframes sweep{0%{transform:rotate(-10deg)}50%{transform:rotate(12deg)}100%{transform:rotate(-10deg)}}`;
  document.head.appendChild(styleSweep);

  // Parallax
const scene = document.getElementById('scene');
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
})();
</script>
</body>
</html>
<!-- Quiz Section -->
<div class="quiz-section">
  <h1>🏛️ Build Your Own Hierarchy</h1>
  <p class="subtitle">Answer the questions to create a custom design component!</p>
  
  <div class="question" id="q1">
    <div class="question-number">Question 1 - Choose Your Primary Size</div>
    <div class="question-text">
      What font size (in pixels) do you want for your PRIMARY heading? Choose a size that will dominate the design.
      <input type="text" class="fill-blank" id="answer1" placeholder="e.g., 40">
    </div>
    <div class="feedback" id="feedback1"></div>
  </div>
  
  <div class="question" id="q2">
    <div class="question-number">Question 2 - Choose Your Secondary Size</div>
    <div class="question-text">
      What font size (in pixels) do you want for your SECONDARY subheading? It should be smaller than primary but still noticeable.
      <input type="text" class="fill-blank" id="answer2" placeholder="e.g., 24">
    </div>
    <div class="feedback" id="feedback2"></div>
  </div>
  
  <div class="check-button-container">
    <button class="check-answers-btn" id="checkBtn">Build My Component</button>
  </div>
  
  <div class="completion-message" id="completion">
    <h2>🏆 Component Built Successfully!</h2>
    <div class="hierarchy-demo">
      <h2 class="demo-secondary" id="demoSecondary">Primary Level</h2>
      <p class="demo-tertiary" id="demoTertiary">Secondary Level</p>
    </div>
    <p style="margin-top: 25px;">You've created a custom design with proper visual hierarchy!</p>
    <p style="margin-top: 10px; font-size: 1.1em;">Your sizes work together to guide users naturally! 🎯</p>
  </div>
</div>

<style>
{{ '@import "beasts/inline/pages/hacks-west-coast-travel-sanfrancisco-alcatraz-2";' | scssify }}
</style>

<script>
document.getElementById('checkBtn').addEventListener('click', function() {
  const input1 = document.getElementById('answer1');
  const input2 = document.getElementById('answer2');
  const feedback1 = document.getElementById('feedback1');
  const feedback2 = document.getElementById('feedback2');
  const question1 = document.getElementById('q1');
  const question2 = document.getElementById('q2');
  
  const answer1 = input1.value.trim();
  const answer2 = input2.value.trim();
  
  // Extract numbers from inputs
  const primarySize = parseInt(answer1);
  const secondarySize = parseInt(answer2);
  
  let allCorrect = true;
  
  // Check answer 1 - Primary size (32-48px)
  if (primarySize >= 32 && primarySize <= 48) {
    feedback1.textContent = `✓ Great choice! ${primarySize}px is a strong primary size!`;
    feedback1.className = 'feedback correct show';
    input1.className = 'fill-blank correct';
    question1.className = 'question correct';
    input1.disabled = true;
  } else {
    feedback1.textContent = '✗ Primary size should be between 32-48px for best hierarchy!';
    feedback1.className = 'feedback incorrect show';
    allCorrect = false;
  }
  
  // Check answer 2 - Secondary size (24-32px and must be smaller than primary)
  if (secondarySize >= 24 && secondarySize <= 32 && secondarySize < primarySize) {
    feedback2.textContent = `✓ Perfect! ${secondarySize}px creates great contrast with your primary!`;
    feedback2.className = 'feedback correct show';
    input2.className = 'fill-blank correct';
    question2.className = 'question correct';
    input2.disabled = true;
  } else if (secondarySize >= primarySize) {
    feedback2.textContent = '✗ Secondary must be smaller than your primary size to create hierarchy!';
    feedback2.className = 'feedback incorrect show';
    allCorrect = false;
  } else {
    feedback2.textContent = '✗ Secondary size should be between 24-32px for best results!';
    feedback2.className = 'feedback incorrect show';
    allCorrect = false;
  }
  
  // Show reward if both correct
  if (allCorrect) {
    setTimeout(() => {
      // Show completion with user's chosen sizes
      const completion = document.getElementById('completion');
      completion.className = 'completion-message show';
      
      // Apply user's chosen sizes to the demo
      document.getElementById('demoSecondary').style.fontSize = primarySize + 'px';
      document.getElementById('demoSecondary').textContent = `Primary Level (${primarySize}px)`;
      
      document.getElementById('demoTertiary').style.fontSize = secondarySize + 'px';
      document.getElementById('demoTertiary').textContent = `Secondary Level (${secondarySize}px)`;
      
      // Disable the button
      this.disabled = true;
      this.textContent = '✓ Component Built!';
      this.style.background = 'linear-gradient(135deg, #4caf50, #66bb6a)';
    }, 500);
  }
});
</script>
