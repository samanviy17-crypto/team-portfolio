---
layout: post
title: "San Francisco"
description: "Roadtrip through SF and learn UI while you're there!"
permalink: /west-coast/analytics/sanfrancisco/
parent: "Analytics/Admin"
team: "Cool Collaborators"
submodule: 2
author: "Cool Collaborators"
date: 2025-10-21
microblog: true
footer: 
    previous:  /west-coast/analytics/sandiego/
    home: /west-coast/travel/
    next: /west-coast/analytics/seattle/
---


<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>San Francisco UI Hierarchy Tour</title>
<style>
{{ '@import "beasts/inline/pages/hacks-west-coast-travel-sanfrancisco-sanfrancisco-1";' | scssify }}
</style>
</head>
<body>

<div class="hero">
  <h1>🌉 San Francisco UI Hierarchy Tour</h1>
  <p>Learn UI design principles through iconic SF landmarks</p>
</div>

<nav class="nav">
  <ul class="nav-links">
    <li><a href="#alcatraz" id="nav-alcatraz">🏛️ Alcatraz</a></li>
    <li><a href="#golden-gate" id="nav-golden-gate">🌉 Golden Gate</a></li>
    <li><a href="#palace" id="nav-palace">🏛️ Palace of Fine Arts</a></li>
    <li><a href="#painted-ladies" id="nav-painted-ladies">🏠 Painted Ladies</a></li>
  </ul>
</nav>

<div class="personalization-notice" id="personalization-notice" style="display:none;">
  <h3>✨ Personalized for You!</h3>
  <p>Based on your itinerary quiz, we're showing you your selected San Francisco destinations.</p>
</div>

<!-- ALCATRAZ -->
<div class="location" id="alcatraz">
  <div class="location-header">
    <h2>🏛️ Alcatraz Island</h2>
    <p>UI Hierarchy Lesson</p>
  </div>

  <div class="scene">
    <div class="sky"></div>
    <div class="orb"></div>
    <div class="fog">
      <span class="f1"></span>
      <span class="f2"></span>
      <span class="f3"></span>
    </div>
    <div class="water"><div class="ripples"></div></div>
    <svg viewBox="0 0 1600 500" preserveAspectRatio="none" style="position:absolute;left:8vw;right:8vw;bottom:calc(42vh - 64px);height:24vh;z-index:5">
      <defs>
        <linearGradient id="rockGrad" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="var(--rock1)"/>
          <stop offset="100%" stop-color="var(--rock2)"/>
        </linearGradient>
      </defs>
      <path d="M0,300 C200,270 320,280 520,260 C700,245 880,240 1080,255 C1280,270 1400,290 1600,280 L1600,360 L0,360 Z" fill="url(#rockGrad)" stroke="var(--rock-edge)" stroke-width="3"/>
      <g fill="var(--vegetation)">
        <ellipse cx="260" cy="250" rx="40" ry="24"/>
        <ellipse cx="1240" cy="250" rx="34" ry="20"/>
      </g>
      <g transform="translate(520,150)">
        <rect x="0" y="0" width="520" height="90" rx="6" fill="var(--building)" stroke="var(--trim)" stroke-width="4"/>
        <rect x="20" y="-22" width="160" height="22" rx="4" fill="var(--roof)"/>
        <g fill="#8f8777">
          <rect x="36" y="24" width="28" height="28" rx="4"/>
          <rect x="230" y="24" width="28" height="28" rx="4"/>
        </g>
      </g>
      <g transform="translate(1080,110)">
        <rect x="-60" y="70" width="120" height="50" rx="6" fill="var(--building)" stroke="var(--trim)" stroke-width="4"/>
        <rect x="0" y="-5" width="28" height="130" rx="8" fill="var(--lighthouse)" stroke="#cfcfcf" stroke-width="4"/>
        <circle cx="14" cy="-6" r="16" fill="var(--lamp)" stroke="#e1d48f" stroke-width="4"/>
      </g>
    </svg>
    <div class="hint">Alcatraz: Isolation creates hierarchy</div>
  </div>

  <div class="lesson-content">
    <h3>UI Hierarchy: Alcatraz Island</h3>
    <p>UI hierarchy organizes elements by importance—just like Alcatraz Island, where the main cellhouse dominates while guard towers and smaller structures support the overall design.</p>

    <h3>The 3 Levels of Hierarchy</h3>
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

    <div class="tip-box">
      <strong>Size</strong>
      <p>Like the cellhouse towering over smaller buildings. Primary: 32-48px, Secondary: 24-32px, Tertiary: 14-16px</p>
    </div>
    <div class="tip-box">
      <strong>Spacing</strong>
      <p>Isolation cells created maximum separation—use white space the same way to emphasize importance.</p>
    </div>
  </div>

  <div class="quiz-section">
    <h3>🏛️ Build Your Hierarchy</h3>
    <p class="subtitle">Create a custom design component!</p>
    
    <div class="question" id="alc-q1">
      <div class="question-number">Question 1 - Primary Size</div>
      <div class="question-text">
        What font size (in pixels) for your PRIMARY heading? Choose a size that will dominate (32-48px).
        <input type="text" class="fill-blank" id="alc-a1" placeholder="e.g., 40">
      </div>
      <div class="feedback" id="alc-f1"></div>
    </div>
    
    <div class="question" id="alc-q2">
      <div class="question-number">Question 2 - Secondary Size</div>
      <div class="question-text">
        What font size for your SECONDARY subheading? Smaller than primary but noticeable (24-32px).
        <input type="text" class="fill-blank" id="alc-a2" placeholder="e.g., 24">
      </div>
      <div class="feedback" id="alc-f2"></div>
    </div>
    
    <div class="check-button-container">
      <button class="check-answers-btn" id="alc-check">Build My Component</button>
    </div>
    
    <div class="completion-message" id="alc-complete">
      <h4>🏆 Component Built!</h4>
      <div class="hierarchy-demo">
        <h2 class="demo-secondary" id="alc-demo-p">Primary Level</h2>
        <p class="demo-tertiary" id="alc-demo-s">Secondary Level</p>
      </div>
      <p>Your sizes work together to guide users naturally! 🎯</p>
    </div>
  </div>
</div>

<!-- GOLDEN GATE BRIDGE -->
<div class="location" id="golden-gate">
  <div class="location-header">
    <h2>🌉 Golden Gate Bridge</h2>
    <p>Heading Hierarchy Lesson</p>
  </div>

  <div class="scene">
    <div class="sky"></div>
    <div class="orb"></div>
    <div class="fog">
      <span class="f1"></span>
      <span class="f2"></span>
    </div>
    <div class="water" style="height:40vh"><div class="ripples"></div></div>
    <svg viewBox="0 0 1600 600" preserveAspectRatio="none" style="position:absolute;left:0;right:0;bottom:30vh;height:40vh;z-index:4">
      <rect x="0" y="320" width="1600" height="6" fill="#222" opacity=".8"/>
      <g fill="var(--bridge)">
        <rect x="300" y="160" width="44" height="200" rx="6"/>
        <rect x="1100" y="140" width="44" height="220" rx="6"/>
      </g>
      <path d="M0,320 L300,160 C 500,300 900,300 1100,140 L1600,320" stroke="var(--cable)" stroke-width="6" fill="none"/>
    </svg>
    <div class="hint">Golden Gate: Strong structure</div>
  </div>

  <div class="lesson-content">
    <h3>Heading Hierarchy: # to ###</h3>
    <p>The Golden Gate's iconic towers command attention. In Markdown and HTML, headings work the same way—# is biggest, ## is medium, ### is smaller.</p>

    <h3># H1: Primary (The Towers)</h3>
    <p>Most important—commanding like the 746-foot Art Deco towers. Use # for your main page title.</p>
    <ul>
      <li>Markdown: # Main Page Title</li>
      <li>HTML: &lt;h1&gt;Main Page Title&lt;/h1&gt;</li>
      <li>Use only once per page</li>
    </ul>

    <h3>## H2: Secondary (The Cables)</h3>
    <p>Supporting sections—like the suspension cables. Use ## for major sections.</p>

    <h3>### H3: Tertiary (The Roadway)</h3>
    <p>Subsections and details. Use ### for subsections within H2 areas.</p>

    <div class="tip-box">
      <strong>Why It Matters</strong>
      <p>The number of hashtags determines importance. One # is biggest. Two ## is smaller. Three ### is smallest. Always start with # and nest logically: # → ## → ###. Never skip levels!</p>
    </div>
  </div>

  <div class="quiz-section">
    <h3>🌉 Build Your Hierarchy</h3>
    <p class="subtitle">Create proper heading structure!</p>
    
    <div class="question" id="gg-q1">
      <div class="question-number">Question 1 - Primary Size</div>
      <div class="question-text">
        What font size (in pixels) for your PRIMARY heading (32-48px)?
        <input type="text" class="fill-blank" id="gg-a1" placeholder="e.g., 40">
      </div>
      <div class="feedback" id="gg-f1"></div>
    </div>
    
    <div class="question" id="gg-q2">
      <div class="question-number">Question 2 - Secondary Size</div>
      <div class="question-text">
        What font size for your SECONDARY subheading (24-32px)?
        <input type="text" class="fill-blank" id="gg-a2" placeholder="e.g., 24">
      </div>
      <div class="feedback" id="gg-f2"></div>
    </div>
    
    <div class="check-button-container">
      <button class="check-answers-btn" id="gg-check">Build Component</button>
    </div>
    
    <div class="completion-message" id="gg-complete">
      <h4>🎉 Success!</h4>
      <div class="hierarchy-demo">
        <h2 class="demo-secondary" id="gg-demo-p">Primary Level</h2>
        <p class="demo-tertiary" id="gg-demo-s">Secondary Level</p>
      </div>
      <p>Your heading structure is solid! 🌉</p>
    </div>
  </div>
</div>

<!-- PALACE OF FINE ARTS -->
<div class="location" id="palace">
  <div class="location-header">
    <h2>🏛️ Palace of Fine Arts</h2>
    <p>Visual Hierarchy Lesson</p>
  </div>

  <div class="scene">
    <div class="sky"></div>
    <div class="orb"></div>
    <div class="fog">
      <span class="f1"></span>
      <span class="f2"></span>
    </div>
    <div class="water" style="height:38vh"><div class="ripples"></div></div>
    <div style="position:absolute;left:0;right:0;bottom:38vh;height:10vh;z-index:4;background:linear-gradient(to bottom,var(--bank1),var(--bank2))"></div>
    <svg viewBox="0 0 1600 700" preserveAspectRatio="none" style="position:absolute;left:0;right:0;bottom:36vh;height:44vh;z-index:6">
      <defs>
        <linearGradient id="stoneGrad" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="var(--stone)"/>
          <stop offset="100%" stop-color="var(--stone-deep)"/>
        </linearGradient>
        <linearGradient id="capGrad" x1="0" x2="0" y1="0" y2="1">
          <stop offset="0%" stop-color="var(--cap)"/>
          <stop offset="100%" stop-color="var(--shadow)"/>
        </linearGradient>
      </defs>
      <g transform="translate(140,320)" fill="url(#stoneGrad)" stroke="var(--shadow)" stroke-width="4">
        <rect x="0" y="0" width="36" height="170" rx="8"/>
        <rect x="90" y="0" width="36" height="170" rx="8"/>
        <rect x="180" y="0" width="36" height="170" rx="8"/>
        <rect x="-16" y="-26" width="248" height="28" rx="8" fill="url(#capGrad)"/>
      </g>
      <g transform="translate(520,180)" stroke="var(--shadow)" stroke-width="4">
        <rect x="-10" y="300" width="580" height="26" rx="10" fill="url(#capGrad)"/>
        <g fill="url(#stoneGrad)">
          <rect x="0" y="120" width="40" height="190" rx="10"/>
          <rect x="180" y="120" width="40" height="190" rx="10"/>
          <rect x="360" y="120" width="40" height="190" rx="10"/>
        </g>
        <rect x="-20" y="80" width="560" height="48" rx="16" fill="url(#capGrad)"/>
        <ellipse cx="260" cy="60" rx="290" ry="60" fill="url(#capGrad)"/>
      </g>
      <g transform="translate(1200,320)" fill="url(#stoneGrad)" stroke="var(--shadow)" stroke-width="4">
        <rect x="0" y="0" width="36" height="170" rx="8"/>
        <rect x="90" y="0" width="36" height="170" rx="8"/>
        <rect x="180" y="0" width="36" height="170" rx="8"/>
        <rect x="-16" y="-26" width="248" height="28" rx="8" fill="url(#capGrad)"/>
      </g>
    </svg>
    <div class="hint">Palace: Rotunda dominates</div>
  </div>

  <div class="lesson-content">
    <h3>Visual Hierarchy Principles</h3>
    <p>UI hierarchy organizes elements by importance. Think of the Palace of Fine Arts—the grand rotunda dominates the landscape, with colonnades and lagoon arranged to guide visitors naturally through the architectural wonder.</p>

    <h3>The 3 Levels of Hierarchy</h3>
    <div class="hierarchy-grid">
      <div class="hierarchy-card">
        <h4>🏛️ Primary (The Rotunda)</h4>
        <p>Most important content—as majestic as the 162-foot central dome.</p>
        <ul>
          <li>Main headlines</li>
          <li>Key buttons</li>
          <li>Hero images</li>
        </ul>
      </div>
      <div class="hierarchy-card">
        <h4>🏛️ Secondary (The Colonnades)</h4>
        <p>Supporting information—like the sweeping curved colonnades that frame the space.</p>
        <ul>
          <li>Subheadings</li>
          <li>Section titles</li>
          <li>Secondary buttons</li>
        </ul>
      </div>
      <div class="hierarchy-card">
        <h4>🏛️ Tertiary (Decorative Details)</h4>
        <p>Additional details—ornate sculptures, weeping maidens, and reflecting pool.</p>
        <ul>
          <li>Body text</li>
          <li>Captions</li>
          <li>Metadata</li>
        </ul>
      </div>
    </div>

    <div class="tip-box">
      <strong>5 Tools to Create Hierarchy</strong>
      <p>1. Size - Like the rotunda rising above the colonnades<br>
      2. Weight - Massive Roman columns vs. delicate sculptural details<br>
      3. Color - Warm terracotta against lush greenery<br>
      4. Spacing - Open lagoon creates breathing room<br>
      5. Position - Eyes travel to the rotunda first</p>
    </div>
  </div>

  <div class="quiz-section">
    <h3>🏛️ Build Your Hierarchy</h3>
    <p class="subtitle">Create a custom design component!</p>
    
    <div class="question" id="palace-q1">
      <div class="question-number">Question 1 - Primary Size</div>
      <div class="question-text">
        What font size (in pixels) for your PRIMARY heading (32-48px)?
        <input type="text" class="fill-blank" id="palace-a1" placeholder="e.g., 40">
      </div>
      <div class="feedback" id="palace-f1"></div>
    </div>
    
    <div class="question" id="palace-q2">
      <div class="question-number">Question 2 - Secondary Size</div>
      <div class="question-text">
        What font size for your SECONDARY subheading (24-32px)?
        <input type="text" class="fill-blank" id="palace-a2" placeholder="e.g., 24">
      </div>
      <div class="feedback" id="palace-f2"></div>
    </div>
    
    <div class="check-button-container">
      <button class="check-answers-btn" id="palace-check">Build Component</button>
    </div>
    
    <div class="completion-message" id="palace-complete">
      <h4>🏆 Magnificent!</h4>
      <div class="hierarchy-demo">
        <h2 class="demo-secondary" id="palace-demo-p">Primary Level</h2>
        <p class="demo-tertiary" id="palace-demo-s">Secondary Level</p>
      </div>
      <p>Your hierarchy is as beautiful as the Palace! 🎨</p>
    </div>
  </div>
</div>

<!-- PAINTED LADIES -->
<div class="location" id="painted-ladies">
  <div class="location-header">
    <h2>🏠 Painted Ladies</h2>
    <p>Color & Contrast Hierarchy</p>
  </div>

  <div class="scene">
    <div class="sky"></div>
    <div class="orb"></div>
    <div class="fog">
      <span class="f1"></span>
      <span class="f2"></span>
    </div>
    <div style="position:absolute;inset:auto 0 16vh 0;height:28vh;background:radial-gradient(120% 60% at 50% 0%, #3fa36e, var(--lawn));z-index:4"></div>
    <div style="position:absolute;left:10vw;right:10vw;bottom:26vh;height:28px;background:linear-gradient(#cdb793,#a68a63);border-radius:18px;box-shadow:0 6px 10px rgba(0,0,0,.25);z-index:5"></div>
    <svg viewBox="0 0 1600 600" preserveAspectRatio="none" style="position:absolute;left:0;right:0;bottom:20vh;height:40vh;z-index:7">
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
          <g fill="#333">
            <rect x="25" y="110" width="20" height="28" rx="3"/>
            <rect x="115" y="110" width="20" height="28" rx="3"/>
          </g>
        </g>
        <g transform="translate(190,30)" style="filter:drop-shadow(0 6px 10px rgba(0,0,0,.35))">
          <polygon points="0,80 90,0 180,80" fill="var(--roof2)"/>
          <rect x="10" y="80" width="160" height="160" fill="var(--house2)" stroke="var(--trim2)" stroke-width="4"/>
          <rect x="65" y="105" width="50" height="70" fill="var(--house2)" stroke="var(--trim2)" stroke-width="4"/>
          <g fill="#333">
            <rect x="28" y="115" width="22" height="30" rx="3"/>
            <rect x="138" y="115" width="22" height="30" rx="3"/>
          </g>
        </g>
        <g transform="translate(400,40)" style="filter:drop-shadow(0 6px 10px rgba(0,0,0,.35))">
          <polygon points="0,80 90,0 180,80" fill="var(--roof3)"/>
          <rect x="10" y="80" width="160" height="155" fill="var(--house3)" stroke="var(--trim3)" stroke-width="4"/>
          <rect x="65" y="105" width="50" height="70" fill="var(--house3)" stroke="var(--trim3)" stroke-width="4"/>
          <g fill="#333">
            <rect x="28" y="115" width="22" height="30" rx="3"/>
            <rect x="138" y="115" width="22" height="30" rx="3"/>
          </g>
        </g>
      </g>
    </svg>
    <div style="position:absolute;left:0;right:0;bottom:12vh;height:10vh;background:linear-gradient(#383838,#1f1f1f);z-index:8;box-shadow:0 -4px 14px rgba(0,0,0,.35) inset"></div>
    <div class="hint">Painted Ladies: Color creates contrast</div>
  </div>

  <div class="lesson-content">
    <h3>Color & Contrast in Hierarchy</h3>
    <p>UI hierarchy organizes elements by importance—just like the Painted Ladies dominate Alamo Square with their colorful Victorian facades, your design should guide users' eyes naturally through content.</p>

    <h3>The 3 Levels of Hierarchy</h3>
    <div class="hierarchy-grid">
      <div class="hierarchy-card">
        <h4>🏛️ Primary: The Victorian Facades</h4>
        <p>Your most important content—as striking as those colorful Queen Anne mansions.</p>
        <ul>
          <li>Main headlines</li>
          <li>Hero images</li>
          <li>Primary CTAs</li>
        </ul>
      </div>
      <div class="hierarchy-card">
        <h4>🏛️ Secondary: Architectural Details</h4>
        <p>Supporting information—like ornate bay windows and decorative trim.</p>
        <ul>
          <li>Subheadings</li>
          <li>Section titles</li>
          <li>Secondary buttons</li>
        </ul>
      </div>
      <div class="hierarchy-card">
        <h4>🏛️ Tertiary: Paint & Accents</h4>
        <p>Additional details—individual colors, spindles, flourishes.</p>
        <ul>
          <li>Body text</li>
          <li>Captions</li>
          <li>Metadata</li>
        </ul>
      </div>
    </div>

    <div class="tip-box">
      <strong>Quick Tips</strong>
      <p>✓ Limit to 1-2 fonts maximum<br>
      ✓ Create dramatic contrast like pastel homes against city skyline<br>
      ✓ Test by squinting—hierarchy should still be clear<br>
      ✓ Use consistent patterns throughout your design</p>
    </div>
  </div>

  <div class="quiz-section">
    <h3>🏠 Build Your Hierarchy</h3>
    <p class="subtitle">Create a custom design component!</p>
    
    <div class="question" id="ladies-q1">
      <div class="question-number">Question 1 - Primary Size</div>
      <div class="question-text">
        What font size (in pixels) for your PRIMARY heading (32-48px)?
        <input type="text" class="fill-blank" id="ladies-a1" placeholder="e.g., 40">
      </div>
      <div class="feedback" id="ladies-f1"></div>
    </div>
    
    <div class="question" id="ladies-q2">
      <div class="question-number">Question 2 - Secondary Size</div>
      <div class="question-text">
        What font size for your SECONDARY subheading (24-32px)?
        <input type="text" class="fill-blank" id="ladies-a2" placeholder="e.g., 24">
      </div>
      <div class="feedback" id="ladies-f2"></div>
    </div>
    
    <div class="check-button-container">
      <button class="check-answers-btn" id="ladies-check">Build Component</button>
    </div>
    
    <div class="completion-message" id="ladies-complete">
      <h4>🎨 Beautiful Work!</h4>
      <div class="hierarchy-demo">
        <h2 class="demo-secondary" id="ladies-demo-p">Primary Level</h2>
        <p class="demo-tertiary" id="ladies-demo-s">Secondary Level</p>
      </div>
      <p>Your design is as iconic as the Painted Ladies! 🏠</p>
    </div>
  </div>
</div>

<script>
// Destination mapping
const DESTINATION_MAP = {
  'Alcatraz': 'alcatraz',
  'Golden Gate Bridge': 'golden-gate',
  'Palace of Fine Arts': 'palace',
  'The Painted Ladies': 'painted-ladies'
};

// Load itinerary from localStorage and filter destinations
function loadItineraryAndFilter() {
  try {
    const itineraryData = localStorage.getItem('westCoastItinerary');
    
    if (itineraryData) {
      const itinerary = JSON.parse(itineraryData);
      
      // Check if San Francisco exists in the itinerary
      if (itinerary.cities && itinerary.cities['San Francisco']) {
        const sfData = itinerary.cities['San Francisco'];
        const selectedDestinations = sfData.destinations || [];
        
        if (selectedDestinations.length > 0) {
          // Show personalization notice
          document.getElementById('personalization-notice').style.display = 'block';
          
          // Hide all destinations first
          const allDestinations = ['alcatraz', 'golden-gate', 'palace', 'painted-ladies'];
          allDestinations.forEach(dest => {
            const section = document.getElementById(dest);
            const navLink = document.getElementById('nav-' + dest);
            if (section) section.classList.add('hidden-location');
            if (navLink) navLink.classList.add('hidden-nav');
          });
          
          // Show only selected destinations
          selectedDestinations.forEach(destName => {
            const destId = DESTINATION_MAP[destName];
            if (destId) {
              const section = document.getElementById(destId);
              const navLink = document.getElementById('nav-' + destId);
              if (section) section.classList.remove('hidden-location');
              if (navLink) navLink.classList.remove('hidden-nav');
            }
          });
          
          console.log('Filtered to show destinations:', selectedDestinations);
        }
      }
    }
  } catch (error) {
    console.error('Error loading itinerary:', error);
    // If there's an error, show all destinations (default behavior)
  }
}

// Run on page load
loadItineraryAndFilter();

function setupQuiz(location) {
  const checkBtn = document.getElementById(`${location}-check`);
  
  checkBtn.addEventListener('click', function() {
    const input1 = document.getElementById(`${location}-a1`);
    const input2 = document.getElementById(`${location}-a2`);
    const feedback1 = document.getElementById(`${location}-f1`);
    const feedback2 = document.getElementById(`${location}-f2`);
    const question1 = document.getElementById(`${location}-q1`);
    const question2 = document.getElementById(`${location}-q2`);
    
    const primarySize = parseInt(input1.value.trim());
    const secondarySize = parseInt(input2.value.trim());
    
    let allCorrect = true;
    
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
    
    if (allCorrect) {
      setTimeout(() => {
        const completion = document.getElementById(`${location}-complete`);
        completion.className = 'completion-message show';
        
        document.getElementById(`${location}-demo-p`).style.fontSize = primarySize + 'px';
        document.getElementById(`${location}-demo-p`).textContent = `Primary Level (${primarySize}px)`;
        
        document.getElementById(`${location}-demo-s`).style.fontSize = secondarySize + 'px';
        document.getElementById(`${location}-demo-s`).textContent = `Secondary Level (${secondarySize}px)`;
        
        checkBtn.disabled = true;
        checkBtn.textContent = '✓ Component Built!';
        checkBtn.style.background = 'linear-gradient(135deg, #4caf50, #66bb6a)';
      }, 500);
    }
  });
}

setupQuiz('alc');
setupQuiz('gg');
setupQuiz('palace');
setupQuiz('ladies');
</script>
<!-- 🌍 Destination Finder Tool -->
<div style="padding: 15px; border-radius: 6px; margin-bottom: 20px; border: 1px solid #dee2e6;">
  <h3 style="margin-top: 0; color: #495057;">AI-Powered Destination Finder</h3>

  <label>Search a Place or Interest:</label>
  <textarea id="user-search-input" placeholder="e.g., beaches, hiking, Paris, ancient history..." style="min-height: 80px; width: 100%; padding: 8px; resize: vertical;"></textarea>
  
  <div style="display: flex; gap: 10px; margin-top: 10px; flex-wrap: wrap;">
    <button class="iridescent flex-1 text-white text-center py-2 rounded-lg font-semibold transition" style="background-color: #007bff;" onclick="generateDestination()">
      🔍 Search Destination
    </button>
    <button class="iridescent flex-1 text-white text-center py-2 rounded-lg font-semibold transition" style="background-color: #28a745;" onclick="saveDestination()">
      💾 Save Destination
    </button>
    <button class="iridescent flex-1 text-white text-center py-2 rounded-lg font-semibold transition" style="background-color: #17a2b8;" onclick="loadDestination()">
      📂 Load Saved
    </button>
  </div>

  <div id="ai-status" style="margin-top: 10px; padding: 8px; border-radius: 4px; display: none;"></div>

  <!-- Destination Info -->
  <div id="destination-info" style="margin-top: 15px; display: none; border-left: 4px solid #007bff; padding: 12px; border-radius: 4px;">
    <h4 id="dest-name" style="margin: 0; color: #007bff;"></h4>
    <p id="dest-country" style="font-weight: bold; margin: 5px 0;"></p>
    <p id="dest-description" style="color: #495057;"></p>
    <p><strong>🗓 Best Time to Visit:</strong> <span id="dest-best-time"></span></p>
    <p><strong>🌤️ Climate:</strong> <span id="dest-climate"></span></p>
    <p><strong>📍 Suggested Activities:</strong> <span id="dest-activities"></span></p>
  </div>
</div>

<script>
// 🌍 Status message helper
function showAIStatus(message, type) {
  const statusDiv = document.getElementById("ai-status");
  statusDiv.textContent = message;
  statusDiv.style.display = "block";

  switch (type) {
    case "loading":
      statusDiv.style.backgroundColor = "#cce5ff";
      statusDiv.style.color = "#004085";
      break;
    case "success":
      statusDiv.style.backgroundColor = "#d1ecf1";
      statusDiv.style.color = "#0c5460";
      break;
    case "error":
      statusDiv.style.backgroundColor = "#f8d7da";
      statusDiv.style.color = "#721c24";
      break;
  }

  if (type !== "loading") {
    setTimeout(() => (statusDiv.style.display = "none"), 5000);
  }
}

// 🌍 Example destinations (can be replaced with AI/Gemini API later)
const DESTINATIONS = [
  {
    keywords: ["beach", "tropical", "ocean"],
    name: "Maui",
    country: "Hawaii, USA",
    description: "A lush island paradise famous for golden beaches, waterfalls, and volcanic landscapes.",
    bestTime: "April to October",
    climate: "Warm tropical",
    activities: "Snorkeling, hiking Haleakalā, surfing, scenic drives along Hana Highway"
  },
  {
    keywords: ["mountain", "hiking", "nature", "alps"],
    name: "Zermatt",
    country: "Switzerland",
    description: "A picturesque alpine village located at the base of the iconic Matterhorn mountain.",
    bestTime: "June to September (hiking), December to March (skiing)",
    climate: "Cool mountain climate",
    activities: "Hiking, skiing, cable car rides, glacier tours"
  },
  {
    keywords: ["history", "ancient", "ruins"],
    name: "Athens",
    country: "Greece",
    description: "The birthplace of democracy and home to ancient landmarks like the Parthenon.",
    bestTime: "April to June, September to October",
    climate: "Mediterranean",
    activities: "Museum visits, walking tours, exploring Acropolis, Greek cuisine"
  },
  {
    keywords: ["art", "romantic", "europe"],
    name: "Florence",
    country: "Italy",
    description: "A Renaissance treasure known for its art, architecture, and cuisine.",
    bestTime: "May to September",
    climate: "Warm Mediterranean",
    activities: "Visiting the Uffizi Gallery, Duomo climb, wine tasting in Tuscany"
  },
  {
    keywords: ["wildlife", "adventure", "africa", "safari"],
    name: "Serengeti National Park",
    country: "Tanzania",
    description: "A vast ecosystem renowned for the Great Migration and diverse African wildlife.",
    bestTime: "June to October",
    climate: "Warm dry savanna",
    activities: "Safari drives, wildlife photography, balloon safaris"
  }
];

// 🌍 Generate Destination
function generateDestination() {
  const query = document.getElementById("user-search-input").value.trim().toLowerCase();
  if (!query) {
    showAIStatus("⚠️ Please enter a place or theme to search.", "error");
    return;
  }

  showAIStatus("🔍 Searching destinations...", "loading");

  // Find matching destination
  const found = DESTINATIONS.find(dest =>
    dest.keywords.some(k => query.includes(k))
  );

  if (found) {
    displayDestination(found);
    showAIStatus("✅ Destination found!", "success");
  } else {
    // Fallback destination
    displayDestination({
      name: "Kyoto",
      country: "Japan",
      description:
        "A serene city known for its traditional temples, cherry blossoms, and tea culture.",
      bestTime: "March to May, October to November",
      climate: "Mild temperate",
      activities: "Temple visits, tea ceremonies, exploring Arashiyama bamboo forest"
    });
    showAIStatus("🌸 No exact match found, but here's a great suggestion: Kyoto!", "success");
  }
}

// 🌍 Display destination info
function displayDestination(dest) {
  document.getElementById("destination-info").style.display = "block";
  document.getElementById("dest-name").textContent = dest.name;
  document.getElementById("dest-country").textContent = dest.country;
  document.getElementById("dest-description").textContent = dest.description;
  document.getElementById("dest-best-time").textContent = dest.bestTime;
  document.getElementById("dest-climate").textContent = dest.climate;
  document.getElementById("dest-activities").textContent = dest.activities;
}

// 🌍 Save to localStorage
function saveDestination() {
  const data = {
    input: document.getElementById("user-search-input").value.trim(),
    name: document.getElementById("dest-name").textContent,
    country: document.getElementById("dest-country").textContent,
    description: document.getElementById("dest-description").textContent,
    bestTime: document.getElementById("dest-best-time").textContent,
    climate: document.getElementById("dest-climate").textContent,
    activities: document.getElementById("dest-activities").textContent,
    timestamp: new Date().toISOString()
  };

  if (!data.name) {
    showAIStatus("⚠️ Please generate a destination before saving.", "error");
    return;
  }

  localStorage.setItem("destination-finder-saved", JSON.stringify(data));
  showAIStatus("✅ Destination saved successfully!", "success");
}

// 🌍 Load saved destination
function loadDestination() {
  const saved = localStorage.getItem("destination-finder-saved");
  if (!saved) {
    showAIStatus("⚠️ No saved destination found.", "error");
    return;
  }

  const data = JSON.parse(saved);
  displayDestination(data);
  document.getElementById("user-search-input").value = data.input;
  const saveDate = new Date(data.timestamp).toLocaleString();
  showAIStatus(`📂 Loaded saved destination (Saved: ${saveDate})`, "success");
}
</script>
Share your experiences on the microblog!
</body>
</html>