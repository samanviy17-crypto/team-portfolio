---
layout: post
title: "Space Needle"
description: 
permalink: /west-coast/travel/seattle/needle/
date: 2025-10-21
---
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Space Needle - Seattle</title>
<style>
{{ '@import "beasts/inline/pages/hacks-west-coast-travel-seattle-spaceneedle-1";' | scssify }}
</style>
</head>
<body>
<div class="container">
<div class="needle-scene">
<div class="label">🗼 Space Needle</div>
      <div class="seattle-sky">
        <div class="rain-drop" style="left: 15%; animation-delay: 0s;"></div>
        <div class="rain-drop" style="left: 25%; animation-delay: 0.3s;"></div>
        <div class="rain-drop" style="left: 35%; animation-delay: 0.6s;"></div>
        <div class="rain-drop" style="left: 45%; animation-delay: 0.2s;"></div>
        <div class="rain-drop" style="left: 55%; animation-delay: 0.8s;"></div>
        <div class="rain-drop" style="left: 65%; animation-delay: 0.4s;"></div>
        <div class="rain-drop" style="left: 75%; animation-delay: 0.1s;"></div>
        <div class="rain-drop" style="left: 85%; animation-delay: 0.7s;"></div>
      </div>
      <div class="city-building b1">
        <div class="window-grid">
          <div class="window"></div><div class="window"></div><div class="window"></div>
          <div class="window"></div><div class="window"></div><div class="window"></div>
          <div class="window"></div><div class="window"></div><div class="window"></div>
        </div>
      </div>
      <div class="city-building b2">
        <div class="window-grid">
          <div class="window"></div><div class="window"></div><div class="window"></div>
          <div class="window"></div><div class="window"></div><div class="window"></div>
          <div class="window"></div><div class="window"></div><div class="window"></div>
        </div>
      </div>
      <div class="city-building b3">
        <div class="window-grid">
          <div class="window"></div><div class="window"></div><div class="window"></div>
          <div class="window"></div><div class="window"></div><div class="window"></div>
        </div>
      </div>
      <div class="city-building b4">
        <div class="window-grid">
          <div class="window"></div><div class="window"></div><div class="window"></div>
          <div class="window"></div><div class="window"></div><div class="window"></div>
          <div class="window"></div><div class="window"></div><div class="window"></div>
        </div>
      </div>
      <div class="space-needle">
        <div class="needle-top">
          <div class="antenna">
            <div class="antenna-light"></div>
          </div>
          <div class="top-cap"></div>
        </div>
        <div class="roof-ring"></div>
        <div class="observation-deck">
          <div class="deck-windows">
            <div class="deck-window"></div>
            <div class="deck-window"></div>
            <div class="deck-window"></div>
            <div class="deck-window"></div>
            <div class="deck-window"></div>
            <div class="deck-window"></div>
            <div class="deck-window"></div>
            <div class="deck-window"></div>
            <div class="deck-window"></div>
            <div class="deck-window"></div>
          </div>
        </div>
        <div class="saucer-bottom"></div>
        <div class="needle-shaft"></div>
        <div class="needle-legs">
          <div class="leg l1"></div>
          <div class="leg l2"></div>
          <div class="leg l3"></div>
          <div class="leg l4"></div>
        </div>
        <div class="needle-base"></div>
      </div>
      <div class="ground"></div>
    </div>
    
    <div class="content">
      <h1>Progress Bar Lesson: Space Needle Theme</h1>

      <h2>What is a Progress Bar?</h2>
      <p>A progress bar shows how much of a task is complete. Think of the Space Needle—visitors riding the elevator up 520 feet to the observation deck, watching floor numbers light up as you ascend. It shows where you are and how much is left.</p>

      <h2>The 3 Parts of a Progress Bar</h2>

      <h3>The Track (The Full Tower)</h3>
      <p>From ground level to the top deck—represents the total task.</p>
      <ul>
        <li>Background bar showing the complete distance</li>
      </ul>

      <h3>The Fill (Floors Climbed)</h3>
      <p>Progress up the tower—shows how far you've come.</p>
      <ul>
        <li>Colored bar that grows as you complete the task</li>
      </ul>

      <h3>The Label (Floor Display)</h3>
      <p>Digital floor counter in the elevator—tells you exactly where you are.</p>
      <ul>
        <li>Text showing percentage or "Level 3 of 5"</li>
      </ul>

      <h2>5 Design Tips</h2>

      <h3>1. Make it Visible</h3>
      <p>Like the bright floor display in the elevator—easy to see in any light.</p>
      <ul>
        <li>Use clear colors with good contrast</li>
        <li>Make it big enough to notice</li>
      </ul>

      <h3>2. Show Real Progress</h3>
      <p>Like the smooth elevator ride—accurate and honest.</p>
      <ul>
        <li>Update smoothly as tasks complete</li>
        <li>Never fake progress or go backwards</li>
      </ul>

      <h3>3. Use Iconic Colors</h3>
      <p>Space Needle white and orange create recognizable style.</p>
      <ul>
        <li>Match your brand colors</li>
        <li>Use color to show status (green = good, red = error)</li>
      </ul>

      <h3>4. Add Context</h3>
      <p>Like the elevator operator's announcements—tell users what's happening.</p>
      <ul>
        <li>"Loading... 60%"</li>
        <li>"Step 3 of 5 complete"</li>
      </ul>

      <h3>5. Keep it Simple</h3>
      <p>Don't overcomplicate like confusing observation levels.</p>
      <ul>
        <li>One bar, clear message</li>
        <li>Avoid fancy animations that distract</li>
      </ul>

      <h2>Common Mistakes</h2>
      <ul>
        <li>No feedback—users don't know if anything is happening</li>
        <li>Jumping progress—going from 10% to 90% instantly feels fake</li>
        <li>Stuck at 99%—like an elevator frozen between floors</li>
        <li>Too small—like trying to read the floor display from outside</li>
        <li>No message—progress without context confuses users</li>
      </ul>

      <h2>Quick Example</h2>
      <div class="example-box">
        <p><strong>Good:</strong> "Uploading to cloud... [████████░░] 80% - Floor 4 of 5"</p>
        <p><strong>Bad:</strong> [░░░░░░░░░░] (no message, unclear progress)</p>
      </div>

      <h2>Quick Tips</h2>
      <ul>
        <li>Always show feedback when users wait</li>
        <li>Smooth animations feel more professional (like the elevator)</li>
        <li>Add estimated time if possible: "About 40 seconds to top"</li>
        <li>Use motion to show it's working, not frozen</li>
        <li>Celebrate completion—like reaching the stunning 360° view!</li>
      </ul>
    </div>
</div>
</body>

<!-- Quiz Section -->
<div class="quiz-section">
  <h1>🎯 Progress Bar Quiz</h1>
  <p class="subtitle">Test your knowledge of progress bar design principles!</p>
  
  <div class="question" id="q1">
    <div class="question-number">Question 1</div>
    <div class="question-text">
      When designing a progress bar, you should use 
      <input type="text" class="fill-blank" id="answer1" placeholder="Your answer..."> 
      animations to make the bar feel professional and show that the task is actively running.
    </div>
    <p class="hint">💡 Hint: The opposite of jerky or jumpy</p>
    <div class="feedback" id="feedback1"></div>
    <div class="progress-reward" id="reward1">
      <h3>✅ Correct! Watch the difference:</h3>
      <p><strong>Smooth Animation:</strong></p>
      <div class="progress-bar-demo">
        <div class="progress-fill" id="progress1" style="width: 0%">0%</div>
      </div>
      <p style="font-size: 0.95em; margin-top: 12px; color: #69be28;">Smooth progress feels natural and professional!</p>
    </div>
  </div>
  
  <div class="question" id="q2">
    <div class="question-number">Question 2</div>
    <div class="question-text">
      A common mistake is making the progress bar too 
      <input type="text" class="fill-blank" id="answer2" placeholder="Your answer..."> 
      which makes it hard for users to see and track their progress.
    </div>
    <p class="hint">💡 Hint: Not big enough</p>
    <div class="feedback" id="feedback2"></div>
    <div class="progress-reward" id="reward2">
      <h3>🌟 Excellent! Size matters:</h3>
      <p><strong>Processing files...</strong></p>
      <div class="progress-bar-demo">
        <div class="progress-fill" id="progress2" style="width: 0%">0%</div>
      </div>
      <p style="font-size: 0.95em; margin-top: 12px; color: #69be28;">A visible progress bar keeps users informed and engaged!</p>
    </div>
  </div>
  
  <div class="completion-message" id="completion">
    <h2>🏆 Quiz Complete!</h2>
    <p>You've mastered the key principles of progress bar design!</p>
    <p style="margin-top: 15px; font-size: 1.1em;">Ready to build better user experiences! 🎉</p>
  </div>
</div>

<style>
{{ '@import "beasts/inline/pages/hacks-west-coast-travel-seattle-lumenfield-2";' | scssify }}
</style>

<script>
const answers = {
  q1: ['smooth', 'fluid', 'seamless'],
  q2: ['small', 'tiny', 'little']
};

let correctCount = 0;

function animateProgress(elementId, targetWidth) {
  const progressBar = document.getElementById(elementId);
  let width = 0;
  const interval = setInterval(() => {
    if (width >= targetWidth) {
      clearInterval(interval);
    } else {
      width += 2;
      progressBar.style.width = width + '%';
      progressBar.textContent = width + '%';
    }
  }, 30);
}

function checkAnswer(questionNum) {
  const input = document.getElementById(`answer${questionNum}`);
  const feedback = document.getElementById(`feedback${questionNum}`);
  const reward = document.getElementById(`reward${questionNum}`);
  const question = document.getElementById(`q${questionNum}`);
  
  const userAnswer = input.value.trim().toLowerCase();
  const correctAnswers = answers[`q${questionNum}`];
  
  if (correctAnswers.includes(userAnswer)) {
    feedback.textContent = questionNum === 1 ? '✓ Perfect! Smooth animations are key!' : '✓ Exactly! Visibility is crucial!';
    feedback.className = 'feedback correct show';
    input.className = 'fill-blank correct';
    question.className = 'question correct';
    reward.className = 'progress-reward show';
    input.disabled = true;
    
    setTimeout(() => {
      const targetWidth = questionNum === 1 ? 65 : 100;
      animateProgress(`progress${questionNum}`, targetWidth);
    }, 300);
    
    correctCount++;
    
    if (correctCount === 2) {
      setTimeout(() => {
        document.getElementById('completion').className = 'completion-message show';
      }, 2500);
    }
  } else if (userAnswer !== '') {
    feedback.textContent = '✗ Not quite! Check the lesson and try again!';
    feedback.className = 'feedback incorrect show';
    setTimeout(() => {
      feedback.className = 'feedback incorrect';
    }, 2000);
  }
}

document.getElementById('answer1').addEventListener('input', () => checkAnswer(1));
document.getElementById('answer2').addEventListener('input', () => checkAnswer(2));

document.getElementById('answer1').addEventListener('keypress', (e) => {
  if (e.key === 'Enter') checkAnswer(1);
});
document.getElementById('answer2').addEventListener('keypress', (e) => {
  if (e.key === 'Enter') checkAnswer(2);
});
</script>