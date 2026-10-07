---
layout: post
title: "Lumen Field"
description: 
permalink: /west-coast/travel/seattle/lumen/
date: 2025-10-21
---

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Lumen Field - Seattle</title>
<style>
{{ '@import "beasts/inline/pages/hacks-west-coast-travel-seattle-lumenfield-1";' | scssify }}
</style>
</head>
<body>
  <div class="container">
    <div class="lumen-scene">
      <div class="label">🏈 Lumen Field</div>
      
      <div class="stadium-lights">
        <div class="light-tower lt1">
          <div class="light-beam"></div>
        </div>
        <div class="light-tower lt2">
          <div class="light-beam"></div>
        </div>
        <div class="light-tower lt3">
          <div class="light-beam"></div>
        </div>
        <div class="light-tower lt4">
          <div class="light-beam"></div>
        </div>
      </div>
      
      <div class="stadium-structure">
        <div class="stadium-seats"></div>
      </div>
      
      <div class="football-field">
        <div class="yard-line" style="--x: 20%"></div>
        <div class="yard-line" style="--x: 40%"></div>
        <div class="yard-line" style="--x: 60%"></div>
        <div class="yard-line" style="--x: 80%"></div>
        <div class="midfield">12</div>
      </div>
      
      <div class="football-player">
        <div class="player-helmet">
          <div class="facemask"></div>
        </div>
        <div class="jersey"></div>
        <div class="player-legs">
          <div class="player-leg"></div>
          <div class="player-leg"></div>
        </div>
      </div>
      
      <div class="football">
        <div class="laces"></div>
      </div>
    </div>
    
    <div class="content">
      <h1>Progress Bar Lesson: Lumen Field Theme</h1>

      <h2>What is a Progress Bar?</h2>
      <p>A progress bar shows how much of a task is complete. Think of Lumen Field—fans watching the game clock count down, or the "12th Man" flag raising before kickoff. It shows where you are and how much is left.</p>

      <h2>The 3 Parts of a Progress Bar</h2>

      <h3>The Track (The Field)</h3>
      <p>The full 100 yards—represents the total task.</p>
      <ul>
        <li>Background bar showing the complete distance</li>
      </ul>

      <h3>The Fill (Yards Gained)</h3>
      <p>Progress down the field—shows how far you've come.</p>
      <ul>
        <li>Colored bar that grows as you complete the task</li>
      </ul>

      <h3>The Label (Scoreboard)</h3>
      <p>Game stats and time remaining—tells you exactly where you are.</p>
      <ul>
        <li>Text showing percentage or "3 of 10 steps complete"</li>
      </ul>

      <h2>5 Design Tips</h2>

      <h3>1. Make it Visible</h3>
      <p>Like the giant scoreboard—easy to see from anywhere.</p>
      <ul>
        <li>Use clear colors with good contrast</li>
        <li>Make it big enough to notice</li>
      </ul>

      <h3>2. Show Real Progress</h3>
      <p>Like yard markers on the field—accurate and honest.</p>
      <ul>
        <li>Update smoothly as tasks complete</li>
        <li>Never fake progress or go backwards</li>
      </ul>

      <h3>3. Use Team Colors</h3>
      <p>Seahawks blue and green create excitement.</p>
      <ul>
        <li>Match your brand colors</li>
        <li>Use color to show status (green = good, red = error)</li>
      </ul>

      <h3>4. Add Context</h3>
      <p>Like the play clock—tell users what's happening.</p>
      <ul>
        <li>"Uploading files... 60%"</li>
        <li>"2 of 5 questions answered"</li>
      </ul>

      <h3>5. Keep it Simple</h3>
      <p>Don't overcomplicate like a confusing penalty call.</p>
      <ul>
        <li>One bar, clear message</li>
        <li>Avoid fancy animations that distract</li>
      </ul>

      <h2>Common Mistakes</h2>
      <ul>
        <li>No feedback—users don't know if anything is happening</li>
        <li>Jumping progress—going from 10% to 90% instantly feels fake</li>
        <li>Stuck at 99%—like being at the 1-yard line forever</li>
        <li>Too small—like trying to read the scoreboard from the parking lot</li>
        <li>No message—progress without context confuses users</li>
      </ul>

      <h2>Quick Example</h2>
      <div class="example-box">
        <p><strong>Good:</strong> "Processing images... [████████░░] 80% - 2 minutes left"</p>
        <p><strong>Bad:</strong> [░░░░░░░░░░] (no message, unclear progress)</p>
      </div>

      <h2>Quick Tips</h2>
      <ul>
        <li>Always show feedback when users wait</li>
        <li>Smooth animations feel more professional</li>
        <li>Add estimated time if possible: "About 2 minutes remaining"</li>
        <li>Use motion to show it's working, not frozen</li>
        <li>Celebrate completion—like a touchdown celebration!</li>
      </ul>
    </div>
  </div>
</body>
</html>

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