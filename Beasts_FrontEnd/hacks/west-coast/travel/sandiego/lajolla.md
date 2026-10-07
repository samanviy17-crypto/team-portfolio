---
layout: post
title: "La Jolla Shores"
description: 
permalink: /west-coast/travel/sd/lajolla/
date: 2025-10-21
---
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>La Jolla Beach — San Diego Roadtrip</title>
<style>
{{ '@import "beasts/inline/pages/hacks-west-coast-travel-sandiego-lajolla-1";' | scssify }}
</style>
</head>
<body class="loading">
<!-- Truck intro -->
<div class="intro" id="intro">
<div class="loop-wrapper" role="img" aria-label="Driving through teal hills toward La Jolla Beach">
<div class="mountain"></div>
<div class="hill"></div>
<div class="tree"></div><div class="tree"></div><div class="tree"></div>
<div class="rock"></div>
<div class="truck"></div>
<div class="wheels"></div>
</div>
<p>Cruising to La Jolla Beach, San Diego…</p>
</div>

<!-- Scene -->
<main class="hidden" id="scene">
<div class="animation-wrapper">
  <div class="container">
    <div class="lajolla-scene">
      <div class="beach-sun"></div>
      <div class="ocean-water">
        <div class="wave-motion">
          <div class="wave-line"></div>
          <div class="wave-line w2"></div>
          <div class="wave-line w3"></div>
        </div>
      </div>
      <div class="seal">
        <div class="seal-body">
          <div class="seal-head">
            <div class="seal-nose"></div>
            <div class="seal-whisker w1"></div>
            <div class="seal-whisker w2"></div>
          </div>
          <div class="seal-flipper"></div>
        </div>
      </div>
      <div class="surfer">
        <div class="surfboard"></div>
        <div class="surfer-body">
          <div class="surfer-head"></div>
          <div class="surfer-arm left"></div>
          <div class="surfer-arm right"></div>
        </div>
      </div>
      <div class="seagull"></div>
      <div class="sand"></div>
    </div>
  </div>
</div>
</main>

<!-- Lesson Content -->
<div class="audio-lesson hidden" id="lessonContent">
<div class="audio-container">
  <h1>La Jolla Beach Audio Lesson</h1>
  <h2>Adding Audio to a Webpage</h2>
  <p>Learn how to add and control audio using sounds from La Jolla's beautiful coastline</p>

  <h3>1. What It Does</h3>
  <p>Use the &lt;audio&gt; tag to play clips (ocean waves, seagulls, narration) directly in the browser.</p>

  <h3>2. Prepare Files</h3>
  <p>Save audio files like:</p>
  <pre><code>/audio/ocean-waves.mp3
/audio/seagulls.mp3
/audio/beach-ambience.mp3
/audio/seal-sounds.mp3</code></pre>

  <h3>3. Basic Structure</h3>
  <p>Each section should include a heading, a short description, and an audio player.</p>
  <pre><code>&lt;audio controls&gt;
  &lt;source src="path/to/audio.mp3" type="audio/mpeg"&gt;
&lt;/audio&gt;</code></pre>

  <div class="example-section">
    <h2>Audio you will be working with: La Jolla Beach Sounds</h2>
    <p>
      Listen to the soothing sounds of waves crashing on the shores of La Jolla Beach, accompanied by the calls of seagulls overhead.
    </p>
    <audio controls>
      <source src= "/hacks/west-coast/travel/sandiego/gentle-ocean-waves-3-300839.mp3" type="audio/mpeg">
    </audio>
    <p class="source-text">Source: Ocean waves and beach ambience</p>
  </div>
</div>
</div>

<script>
// Hide intro after 3 seconds
setTimeout(function(){
  document.getElementById('intro').classList.add('hidden');
  document.getElementById('scene').classList.remove('hidden');
  document.getElementById('lessonContent').classList.remove('hidden');
  document.body.classList.remove('loading');
},3000);
</script>
</body>
</html>

<!-- Quiz Section -->
<div class="quiz-section">
  <h1>🌊 Build Your Audio Player</h1>
  <p class="subtitle">Fill in the blanks to create a working audio player with La Jolla Beach sounds!</p>
  
  <div class="question" id="q1">
    <div class="question-number">Question 1 - Audio Tag Opening</div>
    <div class="question-text">
      What attribute do you add to the &lt;audio&gt; tag to show playback controls?
      <div class="code-line">
        <span class="code-tag">&lt;audio</span> 
        <input type="text" class="fill-blank" id="answer1" placeholder="____">
        <span class="code-tag">&gt;</span>
      </div>
    </div>
    <div class="feedback" id="feedback1"></div>
  </div>
  
  <div class="question" id="q2">
    <div class="question-number">Question 2 - Source Tag</div>
    <div class="question-text">
      What tag do you use inside &lt;audio&gt; to specify the audio file?
      <div class="code-line">
        <span class="indent">&lt;</span>
        <input type="text" class="fill-blank" id="answer2" placeholder="____">
        <span class="code-tag"> src="audio.mp3" type="audio/mpeg"&gt;</span>
      </div>
    </div>
    <div class="feedback" id="feedback2"></div>
  </div>
  
  <div class="question" id="q3">
    <div class="question-number">Question 3 - File Type</div>
    <div class="question-text">
      What type value should you use for .mp3 files?
      <div class="code-line">
        <span class="indent code-tag">&lt;source src="audio.mp3" type="audio/</span>
        <input type="text" class="fill-blank" id="answer3" placeholder="____">
        <span class="code-tag">"&gt;</span>
      </div>
    </div>
    <div class="feedback" id="feedback3"></div>
  </div>
  
  <div class="check-button-container">
    <button class="check-answers-btn" id="checkBtn">Build My Audio Player</button>
  </div>
  
  <div class="completion-message" id="completion">
    <h2>🏆 Audio Player Built Successfully!</h2>
    <div class="audio-demo">
      <h3>Your Working Audio Player:</h3>
      <audio controls id="resultAudio">
        <source src="/hacks/west-coast/travel/sandiego/gentle-ocean-waves-3-300839.mp3" type="audio/mpeg">
      </audio>
      <p style="color: #1e3a5f; margin-top: 20px; font-size: 1.1em;">🌊 La Jolla Beach Ocean Waves</p>
    </div>
    <p style="margin-top: 25px;">You've successfully created an audio player using HTML!</p>
    <p style="margin-top: 10px; font-size: 1.1em;">Now you can add audio to any webpage! 🎯</p>
  </div>
</div>

<style>
{{ '@import "beasts/inline/pages/hacks-west-coast-travel-sandiego-balboapark-2";' | scssify }}
</style>

<script>
document.getElementById('checkBtn').addEventListener('click', function() {
  const input1 = document.getElementById('answer1');
  const input2 = document.getElementById('answer2');
  const input3 = document.getElementById('answer3');
  const feedback1 = document.getElementById('feedback1');
  const feedback2 = document.getElementById('feedback2');
  const feedback3 = document.getElementById('feedback3');
  const question1 = document.getElementById('q1');
  const question2 = document.getElementById('q2');
  const question3 = document.getElementById('q3');
  
  const answer1 = input1.value.trim().toLowerCase();
  const answer2 = input2.value.trim().toLowerCase();
  const answer3 = input3.value.trim().toLowerCase();
  
  let allCorrect = true;
  
  // Check answer 1 - controls
  if (answer1 === 'controls') {
    feedback1.textContent = '✓ Correct! "controls" shows the audio controls!';
    feedback1.className = 'feedback correct show';
    input1.className = 'fill-blank correct';
    question1.className = 'question correct';
    input1.disabled = true;
  } else {
    feedback1.textContent = '✗ Try again! Think about what shows play/pause buttons.';
    feedback1.className = 'feedback incorrect show';
    allCorrect = false;
  }
  
  // Check answer 2 - source
  if (answer2 === 'source') {
    feedback2.textContent = '✓ Perfect! The <source> tag specifies the audio file!';
    feedback2.className = 'feedback correct show';
    input2.className = 'fill-blank correct';
    question2.className = 'question correct';
    input2.disabled = true;
  } else {
    feedback2.textContent = '✗ Not quite! What tag links to the audio file?';
    feedback2.className = 'feedback incorrect show';
    allCorrect = false;
  }
  
  // Check answer 3 - mpeg
  if (answer3 === 'mpeg') {
    feedback3.textContent = '✓ Excellent! MP3 files use "mpeg" as their type!';
    feedback3.className = 'feedback correct show';
    input3.className = 'fill-blank correct';
    question3.className = 'question correct';
    input3.disabled = true;
  } else {
    feedback3.textContent = '✗ Try again! What format type is used for .mp3 files?';
    feedback3.className = 'feedback incorrect show';
    allCorrect = false;
  }
  
  // Show completion if all correct
  if (allCorrect) {
    setTimeout(() => {
      const completion = document.getElementById('completion');
      completion.className = 'completion-message show';
      
      // Disable the button
      this.disabled = true;
      this.textContent = '✓ Audio Player Built!';
      this.style.background = 'linear-gradient(135deg, #4caf50, #66bb6a)';
      
      // Scroll to result
      setTimeout(() => {
        completion.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }, 300);
    }, 500);
  }
});
</script>