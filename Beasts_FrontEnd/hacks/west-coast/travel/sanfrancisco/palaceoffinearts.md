---
layout: post
title: "Palace of Fine Arts"
description: 
permalink: /west-coast/travel/sf/palaceoffinearts/
date: 2025-10-21
---
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Palace of Fine Arts — Continuous Scene (with Ground)</title>
<style>
{{ '@import "beasts/inline/pages/hacks-west-coast-travel-sanfrancisco-palaceoffinearts-1";' | scssify }}
</style>
</head>
<body>
<div class="scene-wrapper">
<!-- Scene -->
<div class="scene" id="scene" aria-label="Palace of Fine Arts scene">
  <div class="sky"></div>
  <div class="orb" aria-hidden="true"></div>

  <!-- Fog layers -->
  <div class="fog" aria-hidden="true">
    <span class="f1"></span>
    <span class="f2"></span>
    <span class="f3"></span>
  </div>

  <!-- WATER -->
  <div class="water"><div class="ripples"></div></div>

  <!-- GROUND strip & promenade -->
  <div class="bank"></div>
  <div class="curb"></div>
  <div class="prom"></div>
  <div class="reeds" id="reeds"></div>

  <!-- TREES behind the promenade for depth -->
  <div class="trees" aria-hidden="true">
    <div class="tree" style="left:6vw"></div>
    <div class="tree" style="left:14vw"></div>
    <div class="tree" style="left:78vw"></div>
    <div class="tree" style="left:86vw"></div>
  </div>

  <!-- PALACE silhouette with rotunda & colonnade -->
  <div class="palace" aria-label="Palace rotunda and colonnade">
    <svg viewBox="0 0 1600 700" preserveAspectRatio="none" role="img">
      <defs>
        <linearGradient id="stoneGrad" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="var(--stone)"/>
          <stop offset="100%" stop-color="var(--stone-deep)"/>
        </linearGradient>
        <linearGradient id="capGrad" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="var(--cap)"/>
          <stop offset="100%" stop-color="var(--shadow)"/>
        </linearGradient>
        <linearGradient id="fade" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="#fff" stop-opacity="1"/>
          <stop offset="100%" stop-color="#fff" stop-opacity="0"/>
        </linearGradient>
        <mask id="fadeMask"><rect x="0" y="360" width="1600" height="340" fill="url(#fade)"/></mask>
      </defs>

      <!-- Colonnade left -->
      <g transform="translate(140,320)" fill="url(#stoneGrad)" stroke="var(--shadow)" stroke-width="4">
        <g>
          <rect x="0" y="0" width="36" height="170" rx="8"/>
          <rect x="90" y="0" width="36" height="170" rx="8"/>
          <rect x="180" y="0" width="36" height="170" rx="8"/>
          <rect x="-16" y="-26" width="248" height="28" rx="8" fill="url(#capGrad)"/>
          <rect x="-10" y="170" width="236" height="18" rx="8" fill="url(#capGrad)"/>
        </g>
      </g>

      <!-- Rotunda center -->
      <g transform="translate(520,180)" stroke="var(--shadow)" stroke-width="4">
        <rect x="-10" y="300" width="580" height="26" rx="10" fill="url(#capGrad)"/>
        <g fill="url(#stoneGrad)">
          <rect x="0" y="120" width="40" height="190" rx="10"/>
          <rect x="90" y="120" width="40" height="190" rx="10"/>
          <rect x="180" y="120" width="40" height="190" rx="10"/>
          <rect x="270" y="120" width="40" height="190" rx="10"/>
          <rect x="360" y="120" width="40" height="190" rx="10"/>
          <rect x="450" y="120" width="40" height="190" rx="10"/>
        </g>
        <rect x="-20" y="80" width="560" height="48" rx="16" fill="url(#capGrad)"/>
        <ellipse cx="260" cy="60" rx="290" ry="60" fill="url(#capGrad)"/>
        <ellipse cx="260" cy="20" rx="220" ry="48" fill="url(#capGrad)"/>
      </g>

      <!-- Colonnade right -->
      <g transform="translate(1200,320)" fill="url(#stoneGrad)" stroke="var(--shadow)" stroke-width="4">
        <g>
          <rect x="0" y="0" width="36" height="170" rx="8"/>
          <rect x="90" y="0" width="36" height="170" rx="8"/>
          <rect x="180" y="0" width="36" height="170" rx="8"/>
          <rect x="-16" y="-26" width="248" height="28" rx="8" fill="url(#capGrad)"/>
          <rect x="-10" y="170" width="236" height="18" rx="8" fill="url(#capGrad)"/>
        </g>
      </g>

      <!-- Ground contact shadows -->
      <g class="groundShadows" opacity=".5">
        <ellipse cx="800" cy="510" rx="310" ry="10" fill="rgba(0,0,0,.28)" style="filter:blur(1.5px)"/>
        <ellipse cx="250" cy="510" rx="130" ry="9" fill="rgba(0,0,0,.28)" style="filter:blur(1.2px)"/>
        <ellipse cx="1310" cy="510" rx="130" ry="9" fill="rgba(0,0,0,.28)" style="filter:blur(1.2px)"/>
      </g>

      <!-- Reflection of palace -->
      <g mask="url(#fadeMask)" opacity=".25" transform="scale(1,-1) translate(0,-720)">
        <g transform="translate(140,320)" fill="#000">
          <rect x="0" y="0" width="36" height="170" rx="8"/>
          <rect x="90" y="0" width="36" height="170" rx="8"/>
          <rect x="180" y="0" width="36" height="170" rx="8"/>
          <rect x="-16" y="-26" width="248" height="28" rx="8"/>
          <rect x="-10" y="170" width="236" height="18" rx="8"/>
        </g>
        <g transform="translate(520,180)" fill="#000">
          <rect x="-10" y="300" width="580" height="26" rx="10"/>
          <rect x="0" y="120" width="40" height="190" rx="10"/>
          <rect x="90" y="120" width="40" height="190" rx="10"/>
          <rect x="180" y="120" width="40" height="190" rx="10"/>
          <rect x="270" y="120" width="40" height="190" rx="10"/>
          <rect x="360" y="120" width="40" height="190" rx="10"/>
          <rect x="450" y="120" width="40" height="190" rx="10"/>
          <rect x="-20" y="80" width="560" height="48" rx="16"/>
          <ellipse cx="260" cy="60" rx="290" ry="60"/>
          <ellipse cx="260" cy="20" rx="220" ry="48"/>
        </g>
        <g transform="translate(1200,320)" fill="#000">
          <rect x="0" y="0" width="36" height="170" rx="8"/>
          <rect x="90" y="0" width="36" height="170" rx="8"/>
          <rect x="180" y="0" width="36" height="170" rx="8"/>
          <rect x="-16" y="-26" width="248" height="28" rx="8"/>
          <rect x="-10" y="170" width="236" height="18" rx="8"/>
        </g>
      </g>
    </svg>
  </div>

  <!-- SWANS / BOAT -->
  <div class="swans" id="swans"></div>

  <!-- BIRDS -->
  <div class="birds" id="birds"></div>

  <!-- Interaction layer -->
  <div class="overlay" id="overlay" aria-hidden="true"></div>
</div>
</div>

<!-- Scrollable content below the scene -->
<main class="page">
  <section class="lesson-content">
    <h1 style="text-align:center;font-size:3em;color:#fff;margin-bottom:40px;text-shadow:none">🏛️ UI Hierarchy Lesson: Palace of Fine Arts</h1>
    
   <div style="padding:50px;max-width:900px;margin:0 auto 60px;">
      <h2 style="color:#fff;font-size:2.2em;margin-bottom:20px">What is UI Hierarchy?</h2>
      <p style="color:#fff;font-size:1.2em;line-height:1.8;margin-bottom:30px">
      UI hierarchy organizes elements by importance. Think of the Palace of Fine Arts—the grand rotunda dominates the landscape, with colonnades and lagoon arranged to guide visitors naturally through the architectural wonder.
      </p>
      
      <h2 style="color:#fff;font-size:2.2em;margin:40px 0 20px">The 3 Levels of Hierarchy</h2>
      
  <div style="padding:30px;margin:20px 0;">
        <h3 style="color:#fff;font-size:1.8em;margin-bottom:15px">🏛️ Primary (The Rotunda)</h3>
        <p style="color:#fff;font-size:1.15em;line-height:1.7">
          Most important content—as majestic as the 162-foot central dome.<br>
          <strong>Examples:</strong> Main headlines, key buttons, hero images
        </p>
      </div>
      
  <div style="padding:30px;margin:20px 0;">
        <h3 style="color:#fff;font-size:1.5em;margin-bottom:15px">🏛️ Secondary (The Colonnades)</h3>
        <p style="color:#fff;font-size:1.1em;line-height:1.7">
          Supporting information—like the sweeping curved colonnades that frame the space.<br>
          <strong>Examples:</strong> Subheadings, section titles, secondary buttons
        </p>
      </div>
      
  <div style="padding:30px;margin:20px 0;">
        <h3 style="color:#fff;font-size:1.2em;margin-bottom:15px">🏛️ Tertiary (Decorative Details)</h3>
        <p style="color:#fff;font-size:1em;line-height:1.7">
          Additional details—ornate sculptures, weeping maidens, and reflecting pool.<br>
          <strong>Examples:</strong> Body text, captions, metadata
        </p>
      </div>
      
  <h2 style="color:#fff;font-size:2.2em;margin:50px 0 20px">5 Tools to Create Hierarchy</h2>
      
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:25px;margin:30px 0">
        <div style="padding:25px;">
          <h4 style="color:#fff;font-size:1.4em;margin-bottom:10px">1️⃣ Size</h4>
          <p style="color:#fff;line-height:1.6">Like the rotunda rising above the colonnades</p>
        </div>
        <div style="padding:25px;">
          <h4 style="color:#fff;font-size:1.4em;margin-bottom:10px">2️⃣ Weight</h4>
          <p style="color:#fff;line-height:1.6">Massive Roman columns vs. delicate sculptural details</p>
        </div>
        <div style="padding:25px;">
          <h4 style="color:#fff;font-size:1.4em;margin-bottom:10px">3️⃣ Color</h4>
          <p style="color:#fff;line-height:1.6">Warm terracotta against lush greenery</p>
        </div>
        <div style="padding:25px;">
          <h4 style="color:#fff;font-size:1.4em;margin-bottom:10px">4️⃣ Spacing</h4>
          <p style="color:#fff;line-height:1.6">Open lagoon creates breathing room</p>
        </div>
        <div style="padding:25px;">
          <h4 style="color:#fff;font-size:1.4em;margin-bottom:10px">5️⃣ Position</h4>
          <p style="color:#fff;line-height:1.6">Eyes travel to the rotunda first</p>
        </div>
      </div>
      
  <div style="padding:30px;margin:50px 0 30px;">
        <h3 style="color:#fff;font-size:1.8em;margin-bottom:15px">💡 Quick Tips</h3>
        <ul style="color:#fff;font-size:1.15em;line-height:2;list-style:none;padding-left:0">
          <li>✓ Limit to 1-2 fonts</li>
          <li>✓ Create dramatic contrast (terracotta columns against sky)</li>
          <li>✓ Test by squinting—structure should still be clear</li>
          <li>✓ Use familiar patterns (entrance → colonnade → rotunda → lagoon)</li>
        </ul>
      </div>
    </div>
  </section>
</main>

<script>
(function(){
  const scene = document.getElementById('scene');

  const rnd=(a=1,b=0)=>Math.random()*(a-b)+b;

  // Add reeds at shoreline
  const reeds = document.getElementById('reeds');
  for(let i=0;i<40;i++){
    const r=document.createElement('div'); r.className='reed';
    r.style.left = `${rnd(2,98)}vw`;
    r.style.height = `calc(2vh + ${rnd(1.5,4)}vmin)`;
    r.style.opacity = rnd(.9,.4);
    reeds.appendChild(r);
  }

  // Birds
  const birdsEl = document.getElementById('birds');
  const gullSVG = `
    <svg viewBox="0 0 24 12" xmlns="http://www.w3.org/2000/svg" aria-hidden="true">
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

  // Swans & sailboat
  const swansEl = document.getElementById('swans');
  function spawnSwan(){
    const s=document.createElement('div'); s.className='swan';
    s.innerHTML = '<div class="body"></div><div class="neck"></div><div class="head"></div><div class="bill"></div>';
    s.style.left = rnd(0,100)+'vw';
    s.animate([
      { transform:`translateX(-140vw)` },
      { transform:`translateX(120vw)` }
    ], { duration: rnd(70000,40000), iterations: 1, easing:'linear' });
    swansEl.appendChild(s);
    setTimeout(()=>{ if(s.isConnected) s.remove(); }, 72000);
  }
  function spawnBoat(){
    const b=document.createElement('div'); b.className='sail';
    b.style.left = rnd(0,100)+'vw';
    b.animate([
      { transform:`translateX(-140vw)` },
      { transform:`translateX(120vw)` }
    ], { duration: rnd(80000,50000), iterations: 1, easing:'linear' });
    swansEl.appendChild(b);
    setTimeout(()=>{ if(b.isConnected) b.remove(); }, 82000);
  }
  setInterval(spawnSwan, 9000); 
  for(let i=0;i<3;i++) spawnSwan();
  setInterval(spawnBoat, 12000); 
  spawnBoat();
})();
</script>

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
{{ '@import "beasts/inline/pages/hacks-west-coast-travel-sanfrancisco-palaceoffinearts-2";' | scssify }}
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
