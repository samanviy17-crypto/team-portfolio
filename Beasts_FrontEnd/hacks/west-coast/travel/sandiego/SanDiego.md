---
layout: post
title: "San Diego"
description: "Roadtrip through SD and learn UI while you're there!"
permalink: /west-coast/analytics/sandiego/
parent: "Analytics/Admin"
team: "Cool Collaborators"
submodule: 3
author: "Cool Collaborators"
date: 2025-10-21
microblog: true 
footer: 
    previous: /west-coast/analytics/losangeles/
    home: /west-coast/travel/
    next: /west-coast/analytics/sanfrancisco/
---
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>San Diego Roadtrip - Learn HTML Audio</title>
<style>
{{ '@import "beasts/inline/pages/hacks-west-coast-travel-sandiego-sandiego-1";' | scssify }}
</style>
</head>
<body>

<!-- Intro Screen -->
<div class="intro" id="intro">
  <h1>🌴 San Diego Roadtrip 🌊</h1>
  <p>Learn HTML Audio Through San Diego's Iconic Locations!</p>
</div>

<!-- Main Header -->
<div class="main-header">
  <h1>🎵 San Diego Audio Tour</h1>
  <p id="headerSubtitle">A Journey Through Four Iconic Locations</p>
</div>

<!-- Personalization Notice -->
<div class="personalization-notice" id="personalizationNotice" style="display: none;">
  <h3>✨ Your Personalized Experience</h3>
  <p id="personalizationText"></p>
</div>

<!-- Balboa Park -->
<div class="location" id="location-balboa">
  <div class="location-header">
    <h2>🏛️ Balboa Park</h2>
    <p>Learn about HTML audio with the majestic Spreckels Organ!</p>
  </div>
  
  <div class="scene-container">
    <div class="balboa-scene">
      <div class="sun"></div>
      <div class="botanical">
        <div class="tower left">
          <div class="tower-top"></div>
        </div>
        <div class="dome-building">
          <div class="dome"></div>
          <div class="arch"></div>
        </div>
        <div class="tower right">
          <div class="tower-top"></div>
        </div>
      </div>
      <div class="flower f1">
        <div class="petal p1"></div>
        <div class="petal p2"></div>
        <div class="petal p3"></div>
        <div class="petal p4"></div>
        <div class="flower-center"></div>
      </div>
      <div class="flower f2">
        <div class="petal p1"></div>
        <div class="petal p2"></div>
        <div class="petal p3"></div>
        <div class="petal p4"></div>
        <div class="flower-center"></div>
      </div>
      <div class="balboa-garden"></div>
    </div>
  </div>
  
  <div class="lesson-content">
    <h3>Balboa Park Organ Audio Lesson</h3>
    <p>Learn how to add and control audio using HTML with sounds from Balboa Park's historic Spreckels Organ Pavilion.</p>
    
    <h4>1. What It Does</h4>
    <p>Use the &lt;audio&gt; tag to play clips (music, nature, narration) directly in the browser.</p>
    
    <h4>2. Basic Structure</h4>
    <p>Each audio player includes a heading, description, and the audio element:</p>
    <pre><code>&lt;audio controls&gt;
  &lt;source src="path/to/audio.mp3" type="audio/mpeg"&gt;
&lt;/audio&gt;</code></pre>
    
   <div class="example-section">
      <h3>🎵 Example Audio Player</h3>
      <p>This is a sample audio player showing the controls attribute in action:</p>
      <audio controls>
        <source src= "/hacks/west-coast/travel/sandiego/funny-organ-intro-outro-5008.mp3" type="audio/mpeg">
      </audio>
      <p class="source-text">Sample audio for demonstration</p>
    </div>
  </div>
  
  <div class="quiz-section">
    <h3>🎵 Build Your Audio Player</h3>
    <p class="subtitle">Fill in the blanks to create a working audio player!</p>
    
    <div class="question" id="balboa-q1">
      <div class="question-number">Question 1 - Audio Tag Opening</div>
      <div class="question-text">
        What attribute do you add to the &lt;audio&gt; tag to show playback controls?
        <div class="code-block">
&lt;<span class="code-tag">audio</span> <input type="text" class="fill-blank" id="balboa-a1" placeholder="Your answer">&gt;
&lt;/<span class="code-tag">audio</span>&gt;
        </div>
      </div>
      <div class="feedback" id="balboa-f1"></div>
    </div>
    
    <div class="question" id="balboa-q2">
      <div class="question-number">Question 2 - Source Tag</div>
      <div class="question-text">
        What tag do you use inside &lt;audio&gt; to specify the audio file?
        <div class="code-block">
&lt;<span class="code-tag">audio</span> <span class="code-attr">controls</span>&gt;
  &lt;<input type="text" class="fill-blank" id="balboa-a2" placeholder="Your answer"> <span class="code-attr">src</span>=<span class="code-value">"organ.mp3"</span>
     <span class="code-attr">type</span>=<span class="code-value">"audio/mpeg"</span>&gt;
&lt;/<span class="code-tag">audio</span>&gt;
        </div>
      </div>
      <div class="feedback" id="balboa-f2"></div>
    </div>
    
    <div class="question" id="balboa-q3">
      <div class="question-number">Question 3 - File Type</div>
      <div class="question-text">
        What type value should you use for .mp3 files?
        <div class="code-block">
&lt;<span class="code-tag">source</span> <span class="code-attr">src</span>=<span class="code-value">"balboa.mp3"</span>
   <span class="code-attr">type</span>=<span class="code-value">"audio/<input type="text" class="fill-blank" id="balboa-a3" placeholder="Your answer">"</span>&gt;
        </div>
      </div>
      <div class="feedback" id="balboa-f3"></div>
    </div>
    
    <div class="check-button-container">
      <button class="check-answers-btn" id="balboa-check">Build My Audio Player</button>
    </div>
    
   <div class="completion-message" id="balboa-complete">
      <h3>🏆 Audio Player Built Successfully!</h3>
      <div class="audio-player">
        <p>🎵 Your Working Audio Player:</p>
        <audio controls>
          <source src="/hacks/west-coast/travel/sandiego/funny-organ-intro-outro-5008.mp3" type="audio/mpeg">
        </audio>
      </div>
      <p>You've successfully created an audio player!</p>
      <p>Now you can add audio to any webpage! 🎯</p>
    </div>
  </div>
</div>

<div class="divider"></div>

<!-- La Jolla Beach -->
<div class="location" id="location-lajolla">
  <div class="location-header">
    <h2>🌊 La Jolla Beach</h2>
    <p>Learn HTML audio with the soothing sounds of the Pacific Ocean!</p>
  </div>
  
  <div class="scene-container">
    <div class="lajolla-scene">
      <div class="beach-sun"></div>
      <div class="ocean-water">
        <div class="wave-line"></div>
        <div class="wave-line w2"></div>
        <div class="wave-line w3"></div>
      </div>
      <div class="seal">
        <div class="seal-body">
          <div class="seal-head">
            <div class="seal-nose"></div>
          </div>
        </div>
      </div>
      <div class="sand"></div>
    </div>
  </div>
  
  <div class="lesson-content">
    <h3>La Jolla Beach Audio Lesson</h3>
    <p>Learn how to add and control audio using sounds from La Jolla's beautiful coastline.</p>
    
    <h4>1. What It Does</h4>
    <p>Use the &lt;audio&gt; tag to play clips (ocean waves, seagulls, beach ambience) directly in the browser.</p>
    
    <h4>2. Basic Structure</h4>
    <pre><code>&lt;audio controls&gt;
  &lt;source src="path/to/audio.mp3" type="audio/mpeg"&gt;
&lt;/audio&gt;</code></pre>
    
   <div class="example-section">
      <h3>🌊 Beach Sounds Example</h3>
      <p>Listen to the soothing sounds of waves crashing on the shores of La Jolla Beach:</p>
      <audio controls>
        <source src="/hacks/west-coast/travel/sandiego/gentle-ocean-waves-3-300839.mp3" type="audio/mpeg">
      </audio>
      <p class="source-text">Sample ocean waves audio</p>
    </div>
  </div>
  
  <div class="quiz-section">
    <h3>🌊 Build Your Audio Player</h3>
    <p class="subtitle">Fill in the blanks to create a working audio player with La Jolla Beach sounds!</p>
    
    <div class="question" id="lajolla-q1">
      <div class="question-number">Question 1 - Audio Tag Opening</div>
      <div class="question-text">
        What attribute do you add to the &lt;audio&gt; tag to show playback controls?
        <div class="code-block">
&lt;<span class="code-tag">audio</span> <input type="text" class="fill-blank" id="lajolla-a1" placeholder="Your answer">&gt;
&lt;/<span class="code-tag">audio</span>&gt;
        </div>
      </div>
      <div class="feedback" id="lajolla-f1"></div>
    </div>
    
    <div class="question" id="lajolla-q2">
      <div class="question-number">Question 2 - Source Tag</div>
      <div class="question-text">
        What tag do you use inside &lt;audio&gt; to specify the audio file?
        <div class="code-block">
&lt;<span class="code-tag">audio</span> <span class="code-attr">controls</span>&gt;
  &lt;<input type="text" class="fill-blank" id="lajolla-a2" placeholder="Your answer"> <span class="code-attr">src</span>=<span class="code-value">"waves.mp3"</span>
     <span class="code-attr">type</span>=<span class="code-value">"audio/mpeg"</span>&gt;
&lt;/<span class="code-tag">audio</span>&gt;
        </div>
      </div>
      <div class="feedback" id="lajolla-f2"></div>
    </div>
    
    <div class="question" id="lajolla-q3">
      <div class="question-number">Question 3 - File Type</div>
      <div class="question-text">
        What type value should you use for .mp3 files?
        <div class="code-block">
&lt;<span class="code-tag">source</span> <span class="code-attr">src</span>=<span class="code-value">"beach.mp3"</span>
   <span class="code-attr">type</span>=<span class="code-value">"audio/<input type="text" class="fill-blank" id="lajolla-a3" placeholder="Your answer">"</span>&gt;
        </div>
      </div>
      <div class="feedback" id="lajolla-f3"></div>
    </div>
    
    <div class="check-button-container">
      <button class="check-answers-btn" id="lajolla-check">Build My Audio Player</button>
    </div>
    
  <div class="completion-message" id="lajolla-complete">
      <h3>🏆 Audio Player Built Successfully!</h3>
      <div class="audio-player">
        <p>🌊 La Jolla Beach Ocean Waves</p>
        <audio controls>
          <source src= "/hacks/west-coast/travel/sandiego/gentle-ocean-waves-3-300839.mp3" type="audio/mpeg">
        </audio>
      </div>
      <p>You've successfully created an audio player using HTML!</p>
      <p>Now you can add audio to any webpage! 🎯</p>
    </div>
  </div>
</div>

<div class="divider"></div>

<!-- Petco Park -->
<div class="location" id="location-petco">
  <div class="location-header">
    <h2>⚾ Petco Park</h2>
    <p>Learn HTML audio with the exciting sounds of baseball!</p>
  </div>
  
  <div class="scene-container">
    <div class="petco-scene">
      <div class="sun"></div>
      <div class="scoreboard">
        <div class="team">
          <div class="team-name">PADRES</div>
          <div class="score">3</div>
        </div>
        <div class="team">
          <div class="team-name">AWAY</div>
          <div class="score">2</div>
        </div>
      </div>
      <div class="field">
        <div class="infield">
          <div class="base first"></div>
          <div class="base second"></div>
          <div class="base third"></div>
          <div class="base home"></div>
        </div>
        <div class="baseball"></div>
      </div>
    </div>
  </div>
  
  <div class="lesson-content">
    <h3>Petco Park Audio Lesson</h3>
    <p>Learn how to add and control audio with sounds from San Diego's Petco Park.</p>
    
    <h4>1. What It Does</h4>
    <p>Use the &lt;audio&gt; tag to play clips (crowd cheers, announcers, game sounds) directly in the browser.</p>
    
    <h4>2. Basic Structure</h4>
    <pre><code>&lt;audio controls&gt;
  &lt;source src="path/to/audio.mp3" type="audio/mpeg"&gt;
&lt;/audio&gt;</code></pre>
    
   <div class="example-section">
      <h3>⚾ Petco Park Atmosphere</h3>
      <p>Listen to authentic game-day sounds from the Padres' home stadium:</p>
      <audio controls>
        <source src="/hacks/west-coast/travel/sandiego/applause-cheer-236786.mp3" type="audio/mpeg">
      </audio>
      <p class="source-text">Baseball crowd cheer sound effect</p>
    </div>
  </div>
  
  <div class="quiz-section">
    <h3>⚾ Build Your Audio Player</h3>
    <p class="subtitle">Fill in the blanks to create a working audio player with Petco Park sounds!</p>
    
    <div class="question" id="petco-q1">
      <div class="question-number">Question 1 - Audio Tag Opening</div>
      <div class="question-text">
        What attribute do you add to the &lt;audio&gt; tag to show playback controls?
        <div class="code-block">
&lt;<span class="code-tag">audio</span> <input type="text" class="fill-blank" id="petco-a1" placeholder="Your answer">&gt;
&lt;/<span class="code-tag">audio</span>&gt;
        </div>
      </div>
      <div class="feedback" id="petco-f1"></div>
    </div>
    
    <div class="question" id="petco-q2">
      <div class="question-number">Question 2 - Source Tag</div>
      <div class="question-text">
        What tag do you use inside &lt;audio&gt; to specify the audio file?
        <div class="code-block">
&lt;<span class="code-tag">audio</span> <span class="code-attr">controls</span>&gt;
  &lt;<input type="text" class="fill-blank" id="petco-a2" placeholder="Your answer"> <span class="code-attr">src</span>=<span class="code-value">"cheer.mp3"</span>
     <span class="code-attr">type</span>=<span class="code-value">"audio/mpeg"</span>&gt;
&lt;/<span class="code-tag">audio</span>&gt;
        </div>
      </div>
      <div class="feedback" id="petco-f2"></div>
    </div>
    
    <div class="question" id="petco-q3">
      <div class="question-number">Question 3 - File Type</div>
      <div class="question-text">
        What type value should you use for .mp3 files?
        <div class="code-block">
&lt;<span class="code-tag">source</span> <span class="code-attr">src</span>=<span class="code-value">"petco.mp3"</span>
   <span class="code-attr">type</span>=<span class="code-value">"audio/<input type="text" class="fill-blank" id="petco-a3" placeholder="Your answer">"</span>&gt;
        </div>
      </div>
      <div class="feedback" id="petco-f3"></div>
    </div>
    
    <div class="check-button-container">
      <button class="check-answers-btn" id="petco-check">Play Ball! 🏟️</button>
    </div>
    
   <div class="completion-message" id="petco-complete">
      <h3>⚾ Home Run!</h3>
      <div class="audio-player">
        <p>⚾ Petco Park Game Day Atmosphere</p>
        <audio controls>
          <source src="/hacks/west-coast/travel/sandiego/applause-cheer-236786.mp3" type="audio/mpeg">
        </audio>
      </div>
      <p>The Padres faithful are cheering you on! 🎊</p>
    </div>
  </div>
</div>

<div class="divider"></div>

<!-- San Diego Zoo -->
<div class="location" id="location-zoo">
  <div class="location-header">
    <h2>🦁 San Diego Zoo</h2>
    <p>Learn HTML audio with the wild sounds of the famous San Diego Zoo!</p>
  </div>
  
  <div class="scene-container">
    <div class="zoo-scene">
      <div class="sun"></div>
      <div class="zoo-sign">
        <div class="zoo-sign-text">SAN DIEGO ZOO</div>
      </div>
      <div class="animal panda">
        <div class="panda-body">
          <div class="panda-head">
            <div class="panda-ear left"></div>
            <div class="panda-ear right"></div>
            <div class="panda-eye left"></div>
            <div class="panda-eye right"></div>
          </div>
        </div>
      </div>
      <div class="animal lion">
        <div class="lion-mane">
          <div class="lion-head">
            <div class="lion-eye left"></div>
            <div class="lion-eye right"></div>
          </div>
        </div>
      </div>
      <div class="zoo-path"></div>
    </div>
  </div>
  
  <div class="lesson-content">
    <h3>San Diego Zoo Audio Lesson</h3>
    <p>Learn how to add and control audio using HTML with sounds from the world-famous San Diego Zoo.</p>
    
    <h4>1. What It Does</h4>
    <p>Use the &lt;audio&gt; tag to play clips (lion roars, bird calls, wildlife sounds) directly in the browser.</p>
    
    <h4>2. Basic Structure</h4>
    <pre><code>&lt;audio controls&gt;
  &lt;source src="path/to/audio.mp3" type="audio/mpeg"&gt;
&lt;/audio&gt;</code></pre>
    
   <div class="example-section">
      <h3>🦁 San Diego Zoo Lion Roar</h3>
      <p>Listen to the powerful roar of the king of the jungle:</p>
      <audio controls>
        <source src="/hacks/west-coast/travel/sandiego/tiger-roar-wildlife-sfx-376158.mp3" type="audio/mpeg">
      </audio>
      <p class="source-text">Lion roar and wildlife sounds</p>
    </div>
  </div>
  
  <div class="quiz-section">
    <h3>🦁 Build Your Audio Player</h3>
    <p class="subtitle">Fill in the blanks to create a working audio player with San Diego Zoo sounds!</p>
    
    <div class="question" id="zoo-q1">
      <div class="question-number">Question 1 - Audio Tag Opening</div>
      <div class="question-text">
        What attribute do you add to the &lt;audio&gt; tag to show playback controls?
        <div class="code-block">
&lt;<span class="code-tag">audio</span> <input type="text" class="fill-blank" id="zoo-a1" placeholder="Your answer">&gt;
&lt;/<span class="code-tag">audio</span>&gt;
        </div>
      </div>
      <div class="feedback" id="zoo-f1"></div>
    </div>
    
    <div class="question" id="zoo-q2">
      <div class="question-number">Question 2 - Source Tag</div>
      <div class="question-text">
        What tag do you use inside &lt;audio&gt; to specify the audio file?
        <div class="code-block">
&lt;<span class="code-tag">audio</span> <span class="code-attr">controls</span>&gt;
  &lt;<input type="text" class="fill-blank" id="zoo-a2" placeholder="Your answer"> <span class="code-attr">src</span>=<span class="code-value">"lion.mp3"</span>
     <span class="code-attr">type</span>=<span class="code-value">"audio/mpeg"</span>&gt;
&lt;/<span class="code-tag">audio</span>&gt;
        </div>
      </div>
      <div class="feedback" id="zoo-f2"></div>
    </div>
    
    <div class="question" id="zoo-q3">
      <div class="question-number">Question 3 - File Type</div>
      <div class="question-text">
        What type value should you use for .mp3 files?
        <div class="code-block">
&lt;<span class="code-tag">source</span> <span class="code-attr">src</span>=<span class="code-value">"zoo.mp3"</span>
   <span class="code-attr">type</span>=<span class="code-value">"audio/<input type="text" class="fill-blank" id="zoo-a3" placeholder="Your answer">"</span>&gt;
        </div>
      </div>
      <div class="feedback" id="zoo-f3"></div>
    </div>
    
    <div class="check-button-container">
      <button class="check-answers-btn" id="zoo-check">Hear the Roar! 🦁</button>
    </div>
    
   <div class="completion-message" id="zoo-complete">
      <h3>🦁 Wild Success!</h3>
      <div class="audio-player">
        <p>🦁 King of the Jungle - Lion Roar</p>
        <audio controls>
          <source src= "/hacks/west-coast/travel/sandiego/tiger-roar-wildlife-sfx-376158.mp3" type="audio/mpeg">
        </audio>
      </div>
      <p>The animals are roaring with pride! 🐾</p>
    </div>
  </div>
</div>

<script>
// PERSONALIZATION FEATURE - Load user's selected destinations from localStorage
(function() {
  const DESTINATION_MAP = {
    'Petco Park': 'location-petco',
    'San Diego Zoo': 'location-zoo',
    'Balboa Park': 'location-balboa',
    'La Jolla': 'location-lajolla'
  };

  function loadPersonalization() {
    try {
      const itineraryData = localStorage.getItem('westCoastItinerary');
      
      if (itineraryData) {
        const itinerary = JSON.parse(itineraryData);
        
        // Check if San Diego data exists in the itinerary
        if (itinerary.cities && itinerary.cities['San Diego']) {
          const sanDiegoDestinations = itinerary.cities['San Diego'].destinations;
          
          if (sanDiegoDestinations && sanDiegoDestinations.length > 0) {
            // Show personalization notice
            const notice = document.getElementById('personalizationNotice');
            const noticeText = document.getElementById('personalizationText');
            notice.style.display = 'block';
            noticeText.textContent = `Based on your itinerary, we're showing you: ${sanDiegoDestinations.join(' and ')}! These were your selected destinations from the trip planner.`;
            
            // Update header subtitle
            const headerSubtitle = document.getElementById('headerSubtitle');
            headerSubtitle.textContent = `Your Personalized Journey: ${sanDiegoDestinations.join(' & ')}`;
            
            // Hide all locations first
            Object.values(DESTINATION_MAP).forEach(locationId => {
              const locationElement = document.getElementById(locationId);
              if (locationElement) {
                locationElement.style.display = 'none';
              }
            });
            
            // Show only the selected destinations
            sanDiegoDestinations.forEach(destination => {
              const locationId = DESTINATION_MAP[destination];
              if (locationId) {
                const locationElement = document.getElementById(locationId);
                if (locationElement) {
                  locationElement.style.display = 'block';
                }
              }
            });
            
            return true; // Personalization applied
          }
        }
      }
    } catch (error) {
      console.log('No personalization data found or error loading:', error);
    }
    
    return false; // No personalization applied, show all locations
  }

  // Apply personalization on page load
  const personalized = loadPersonalization();
  
  if (!personalized) {
    // If no personalization, ensure all locations are visible
    Object.values(DESTINATION_MAP).forEach(locationId => {
      const locationElement = document.getElementById(locationId);
      if (locationElement) {
        locationElement.style.display = 'block';
      }
    });
  }
})();

// Hide intro after 3 seconds
setTimeout(function() {
  document.getElementById('intro').classList.add('hidden');
}, 3000);

// Quiz functionality for each location
function setupQuiz(location) {
  const checkBtn = document.getElementById(`${location}-check`);
  
  checkBtn.addEventListener('click', function() {
    const input1 = document.getElementById(`${location}-a1`);
    const input2 = document.getElementById(`${location}-a2`);
    const input3 = document.getElementById(`${location}-a3`);
    const feedback1 = document.getElementById(`${location}-f1`);
    const feedback2 = document.getElementById(`${location}-f2`);
    const feedback3 = document.getElementById(`${location}-f3`);
    const question1 = document.getElementById(`${location}-q1`);
    const question2 = document.getElementById(`${location}-q2`);
    const question3 = document.getElementById(`${location}-q3`);
    
    const answer1 = input1.value.trim().toLowerCase();
    const answer2 = input2.value.trim().toLowerCase();
    const answer3 = input3.value.trim().toLowerCase();
    
    let allCorrect = true;
    
    // Check answer 1 - controls
    if (answer1 === 'controls') {
      feedback1.textContent = '✓ Perfect! The controls attribute shows play, pause, and volume buttons!';
      feedback1.className = 'feedback correct show';
      input1.className = 'fill-blank correct';
      question1.className = 'question correct';
      input1.disabled = true;
    } else {
      feedback1.textContent = '✗ Not quite! You need to add the "controls" attribute to show playback controls.';
      feedback1.className = 'feedback incorrect show';
      allCorrect = false;
    }
    
    // Check answer 2 - source
    if (answer2 === 'source') {
      feedback2.textContent = '✓ Great job! The <source> tag specifies the audio file location!';
      feedback2.className = 'feedback correct show';
      input2.className = 'fill-blank correct';
      question2.className = 'question correct';
      input2.disabled = true;
    } else {
      feedback2.textContent = '✗ Try again! The tag that specifies the audio file is called "source".';
      feedback2.className = 'feedback incorrect show';
      allCorrect = false;
    }
    
    // Check answer 3 - mpeg
    if (answer3 === 'mpeg') {
      feedback3.textContent = '✓ Excellent! audio/mpeg is the correct MIME type for MP3 files!';
      feedback3.className = 'feedback correct show';
      input3.className = 'fill-blank correct';
      question3.className = 'question correct';
      input3.disabled = true;
    } else {
      feedback3.textContent = '✗ Not quite! For .mp3 files, use "mpeg" as the type (audio/mpeg).';
      feedback3.className = 'feedback incorrect show';
      allCorrect = false;
    }
    
    // Show completion if all correct
    if (allCorrect) {
      setTimeout(() => {
        const completion = document.getElementById(`${location}-complete`);
        completion.className = 'completion-message show';
        
        // Disable the button
        checkBtn.disabled = true;
        checkBtn.textContent = '✓ Complete!';
        checkBtn.style.background = 'linear-gradient(135deg, #4caf50, #66bb6a)';
        checkBtn.style.color = 'white';
        
        // Scroll to completion message
        completion.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }, 500);
    }
  });
}

// Setup quizzes for all locations
setupQuiz('balboa');
setupQuiz('lajolla');
setupQuiz('petco');
setupQuiz('zoo');
</script>
 Share your experiences on the microblog!
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