---
layout: post
title: "The Painted Ladies"
description: 
permalink: /west-coast/travel/sf/paintedladies/
date: 2025-10-21
---
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Painted Ladies — UI Hierarchy Lesson</title>
<style>
{{ '@import "beasts/inline/pages/hacks-west-coast-travel-sanfrancisco-thepaintedladies-1";' | scssify }}
</style>
</head>
<body>

<div class="scene-wrapper">
<div class="scene" id="scene" aria-label="Painted Ladies scene">
  <div class="sky"></div>
  <div class="orb" aria-hidden="true"></div>

  <div class="fog" aria-hidden="true">
    <span class="f1"></span>
    <span class="f2"></span>
    <span class="f3"></span>
  </div>

  <div class="skyline" aria-label="San Francisco skyline">
    <svg viewBox="0 0 1600 400" preserveAspectRatio="none" role="img">
      <g fill="#2b4766">
        <rect x="100" y="180" width="80" height="220"/>
        <rect x="210" y="140" width="60" height="260"/>
        <rect x="300" y="120" width="90" height="280"/>
        <polygon points="430,90 460,50 490,90 490,330 430,330"/>
        <rect x="520" y="160" width="70" height="240"/>
        <rect x="620" y="130" width="60" height="270"/>
        <rect x="700" y="170" width="72" height="230"/>
        <rect x="790" y="110" width="60" height="290"/>
        <rect x="870" y="150" width="84" height="250"/>
        <polygon points="990,80 1008,40 1026,80 1026,330 990,330"/>
        <rect x="1080" y="170" width="70" height="230"/>
        <rect x="1170" y="130" width="66" height="270"/>
        <rect x="1250" y="160" width="86" height="240"/>
        <rect x="1360" y="140" width="70" height="260"/>
      </g>
      <g class="twinkle" fill="#fff98a" opacity=".8">
        <circle cx="315" cy="220" r="2"/>
        <circle cx="340" cy="260" r="2"/>
        <circle cx="905" cy="230" r="2"/>
        <circle cx="1115" cy="240" r="2"/>
        <circle cx="1285" cy="210" r="2"/>
      </g>
    </svg>
  </div>

  <div class="lawn"></div>
  <div class="walk"></div>
  <div class="tree" style="left:12vw"></div>
  <div class="tree" style="left:22vw"></div>
  <div class="tree" style="left:72vw"></div>
  <div class="tree" style="left:82vw"></div>

  <div class="ladies" aria-label="Painted Ladies row">
    <svg viewBox="0 0 1600 600" preserveAspectRatio="none" role="img">
      <defs>
        <linearGradient id="shadow" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0" stop-color="#000" stop-opacity=".18"/>
          <stop offset="1" stop-color="#000" stop-opacity="0"/>
        </linearGradient>
      </defs>

      <g transform="translate(140,120)">
        <g transform="translate(0,50)" style="filter:drop-shadow(0 6px 10px rgba(0,0,0,.35))">
          <polygon points="0,80 80,0 160,80" fill="var(--roof1)"/>
          <rect x="10" y="80" width="140" height="150" fill="var(--house1)" stroke="var(--trim1)" stroke-width="4"/>
          <rect x="55" y="100" width="50" height="70" fill="var(--house1)" stroke="var(--trim1)" stroke-width="4"/>
          <g fill="var(--window)">
            <rect x="25" y="110" width="20" height="28" rx="3"/>
            <rect x="115" y="110" width="20" height="28" rx="3"/>
            <rect x="65" y="110" width="30" height="38" rx="3"/>
            <rect x="65" y="160" width="30" height="38" rx="3"/>
          </g>
          <g class="glow1" opacity=".0">
            <rect x="25" y="110" width="20" height="28" rx="3" fill="var(--light)"/>
            <rect x="115" y="110" width="20" height="28" rx="3" fill="var(--light)"/>
            <rect x="65" y="120" width="30" height="18" rx="3" fill="var(--light)"/>
          </g>
          <rect x="10" y="230" width="140" height="10" fill="url(#shadow)"/>
          <rect x="120" y="230" width="30" height="20" fill="#c9c0b5"/>
          <rect x="120" y="246" width="30" height="6" fill="#b2a79c"/>
        </g>

        <g transform="translate(190,30)" style="filter:drop-shadow(0 6px 10px rgba(0,0,0,.35))">
          <polygon points="0,80 90,0 180,80" fill="var(--roof2)"/>
          <rect x="10" y="80" width="160" height="160" fill="var(--house2)" stroke="var(--trim2)" stroke-width="4"/>
          <rect x="65" y="105" width="50" height="70" fill="var(--house2)" stroke="var(--trim2)" stroke-width="4"/>
          <g fill="var(--window)">
            <rect x="28" y="115" width="22" height="30" rx="3"/>
            <rect x="138" y="115" width="22" height="30" rx="3"/>
            <rect x="75" y="115" width="30" height="40" rx="3"/>
            <rect x="75" y="165" width="30" height="40" rx="3"/>
          </g>
          <g class="glow2" opacity=".0">
            <rect x="28" y="115" width="22" height="30" rx="3" fill="var(--light)"/>
            <rect x="138" y="115" width="22" height="30" rx="3" fill="var(--light)"/>
          </g>
          <rect x="10" y="240" width="160" height="10" fill="url(#shadow)"/>
          <rect x="135" y="240" width="35" height="22" fill="#c9c0b5"/>
          <rect x="135" y="260" width="35" height="6" fill="#b2a79c"/>
        </g>

        <g transform="translate(400,40)" style="filter:drop-shadow(0 6px 10px rgba(0,0,0,.35))">
          <polygon points="0,80 90,0 180,80" fill="var(--roof3)"/>
          <rect x="10" y="80" width="160" height="155" fill="var(--house3)" stroke="var(--trim3)" stroke-width="4"/>
          <rect x="65" y="105" width="50" height="70" fill="var(--house3)" stroke="var(--trim3)" stroke-width="4"/>
          <g fill="var(--window)">
            <rect x="28" y="115" width="22" height="30" rx="3"/>
            <rect x="138" y="115" width="22" height="30" rx="3"/>
            <rect x="75" y="115" width="30" height="40" rx="3"/>
            <rect x="75" y="165" width="30" height="40" rx="3"/>
          </g>
          <g class="glow3" opacity=".0">
            <rect x="75" y="165" width="30" height="40" rx="3" fill="var(--light)"/>
          </g>
          <rect x="10" y="235" width="160" height="10" fill="url(#shadow)"/>
          <rect x="130" y="235" width="35" height="20" fill="#c9c0b5"/>
          <rect x="130" y="253" width="35" height="6" fill="#b2a79c"/>
        </g>

        <g transform="translate(610,20)" style="filter:drop-shadow(0 6px 10px rgba(0,0,0,.35))">
          <polygon points="0,80 90,0 180,80" fill="var(--roof4)"/>
          <rect x="10" y="80" width="160" height="165" fill="var(--house4)" stroke="var(--trim4)" stroke-width="4"/>
          <rect x="65" y="105" width="50" height="70" fill="var(--house4)" stroke="var(--trim4)" stroke-width="4"/>
          <g fill="var(--window)">
            <rect x="28" y="115" width="22" height="30" rx="3"/>
            <rect x="138" y="115" width="22" height="30" rx="3"/>
            <rect x="75" y="115" width="30" height="40" rx="3"/>
            <rect x="75" y="165" width="30" height="40" rx="3"/>
          </g>
          <g class="glow4" opacity=".0">
            <rect x="28" y="115" width="22" height="30" rx="3" fill="var(--light)"/>
            <rect x="75" y="125" width="30" height="20" rx="3" fill="var(--light)"/>
          </g>
          <rect x="10" y="245" width="160" height="10" fill="url(#shadow)"/>
          <rect x="132" y="245" width="35" height="22" fill="#c9c0b5"/>
          <rect x="132" y="265" width="35" height="6" fill="#b2a79c"/>
        </g>

        <g transform="translate(820,35)" style="filter:drop-shadow(0 6px 10px rgba(0,0,0,.35))">
          <polygon points="0,80 90,0 180,80" fill="var(--roof5)"/>
          <rect x="10" y="80" width="160" height="158" fill="var(--house5)" stroke="var(--trim5)" stroke-width="4"/>
          <rect x="65" y="105" width="50" height="70" fill="var(--house5)" stroke="var(--trim5)" stroke-width="4"/>
          <g fill="var(--window)">
            <rect x="28" y="115" width="22" height="30" rx="3"/>
            <rect x="138" y="115" width="22" height="30" rx="3"/>
            <rect x="75" y="115" width="30" height="40" rx="3"/>
            <rect x="75" y="165" width="30" height="40" rx="3"/>
          </g>
          <g class="glow5" opacity=".0">
            <rect x="138" y="115" width="22" height="30" rx="3" fill="var(--light)"/>
          </g>
          <rect x="10" y="238" width="160" height="10" fill="url(#shadow)"/>
          <rect x="128" y="238" width="35" height="22" fill="#c9c0b5"/>
          <rect x="128" y="258" width="35" height="6" fill="#b2a79c"/>
        </g>

        <g transform="translate(1030,55)" style="filter:drop-shadow(0 6px 10px rgba(0,0,0,.35))">
          <polygon points="0,80 90,0 180,80" fill="var(--roof6)"/>
          <rect x="10" y="80" width="160" height="150" fill="var(--house6)" stroke="var(--trim6)" stroke-width="4"/>
          <rect x="65" y="105" width="50" height="70" fill="var(--house6)" stroke="var(--trim6)" stroke-width="4"/>
          <g fill="var(--window)">
            <rect x="28" y="115" width="22" height="30" rx="3"/>
            <rect x="138" y="115" width="22" height="30" rx="3"/>
            <rect x="75" y="115" width="30" height="40" rx="3"/>
            <rect x="75" y="165" width="30" height="40" rx="3"/>
          </g>
          <g class="glow6" opacity=".0">
            <rect x="28" y="115" width="22" height="30" rx="3" fill="var(--light)"/>
            <rect x="75" y="170" width="30" height="18" rx="3" fill="var(--light)"/>
          </g>
          <rect x="10" y="230" width="160" height="10" fill="url(#shadow)"/>
          <rect x="124" y="230" width="35" height="22" fill="#c9c0b5"/>
          <rect x="124" y="250" width="35" height="6" fill="#b2a79c"/>
        </g>
      </g>
    </svg>
  </div>

  <div class="street"><div class="lane"></div></div>
  <div class="cruiser"><div class="head"></div></div>

  <div class="birds" id="birds"></div>

  <div class="overlay" id="overlay" aria-hidden="true"></div>
  <div class="hint">Move mouse / tap: parallax. Scene loops continuously.</div>
</div>
</div>

<main class="page">
  <div class="content-wrapper">
    <h1>🏛️ UI Hierarchy: Painted Ladies Edition</h1>
    
    <p>UI hierarchy organizes elements by importance—just like the Painted Ladies dominate Alamo Square with their colorful Victorian facades, your design should guide users' eyes naturally through content.</p>
    
    <h2>The 3 Levels of Hierarchy</h2>
    
    <div class="hierarchy-level">
      <h3>🏛️ Primary: The Victorian Facades</h3>
      <p>Your most important content—as striking as those colorful Queen Anne mansions.</p>
      <p><strong>Examples:</strong> Main headlines, hero images, primary CTAs</p>
    </div>
    
    <div class="hierarchy-level">
      <h3>🏛️ Secondary: Architectural Details</h3>
      <p>Supporting information—like ornate bay windows and decorative trim.</p>
      <p><strong>Examples:</strong> Subheadings, section titles, secondary buttons</p>
    </div>
    
    <div class="hierarchy-level">
      <h3>🏛️ Tertiary: Paint & Accents</h3>
      <p>Additional details—individual colors, spindles, flourishes.</p>
      <p><strong>Examples:</strong> Body text, captions, metadata</p>
    </div>
    
    <h2>5 Tools to Create Hierarchy</h2>
    
    <div class="tools-grid">
      <div class="tool-item">
        <h3>1️⃣ Size</h3>
        <p>Like Victorian homes rising above the park—bigger = more important</p>
      </div>
      <div class="tool-item">
        <h3>2️⃣ Weight</h3>
        <p>Bold structural elements vs. delicate gingerbread trim</p>
      </div>
      <div class="tool-item">
        <h3>3️⃣ Color</h3>
        <p>Vibrant pastels against muted backgrounds create contrast</p>
      </div>
      <div class="tool-item">
        <h3>4️⃣ Spacing</h3>
        <p>The open park creates perfect viewing distance—use whitespace</p>
      </div>
      <div class="tool-item">
        <h3>5️⃣ Position</h3>
        <p>Center and elevate to draw attention first</p>
      </div>
    </div>
    
    <h2>💡 Quick Tips</h2>
    <ul>
      <li>✓ Limit to 1-2 fonts maximum</li>
      <li>✓ Create dramatic contrast like pastel homes against city skyline</li>
      <li>✓ Test by squinting—hierarchy should still be clear</li>
      <li>✓ Use consistent patterns throughout your design</li>
    </ul>
  </div>
</main>
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
{{ '@import "beasts/inline/pages/hacks-west-coast-travel-sanfrancisco-thepaintedladies-2";' | scssify }}
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