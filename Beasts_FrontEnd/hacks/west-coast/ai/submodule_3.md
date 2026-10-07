---
layout: post
title: "Submodule 3"
description: "Submodule 3 of AI Usage Mini-Quest about Prompt Engineering"
permalink: /west-coast/ai/submodule_3/
parent: "AI Usage"
team: "TheSprinters"
microblog: True
submodule: 3
categories: [CSP, Submodule, AIUsage]
tags: [ai, submodule, PromptEnginering]
author: "TheSprinters"
date: 2025-10-21
footer:
  previous: /west-coast/ai/submodule_2
  home: /west-coast/ai
  next: /west-coast/ai/submodule_4
---

<style>
{{ '@import "beasts/inline/pages/hacks-west-coast-ai-submodule-3-1";' | scssify }}
</style>

# Submodule 3: Prompt Engineering Mastery

<div class="demo-container">
  <h2>🎨 The Art of Talking to AI</h2>
  <p>Master the skill of crafting perfect AI prompts and unlock limitless possibilities! Prompt engineering is writing clear, effective instructions to get the best results from AI models.</p>
</div>

---

## Part 1: What Makes a Good Prompt?

<div class="feature-grid">
  <div class="feature-card">
    <strong>🎯 Clarity</strong>
    <span>Be specific about what you want</span>
  </div>
  
  <div class="feature-card">
    <strong>📚 Context</strong>
    <span>Give the AI background information</span>
  </div>
  
  <div class="feature-card">
    <strong>📋 Format</strong>
    <span>Specify response structure</span>
  </div>
  
  <div class="feature-card">
    <strong>🔒 Constraints</strong>
    <span>Set boundaries or requirements</span>
  </div>
  
  <div class="feature-card">
    <strong>💡 Examples</strong>
    <span>Show what you're looking for</span>
  </div>
</div>

---

## Part 2: Interactive Challenges

<div class="demo-container">
  <h2>🎮 Challenge 1: The Travel Planner</h2>
  <p>Compare how different levels of detail affect AI responses.</p>
  
  <div class="comparison-table">
    <div class="bad-prompt">
      <strong>❌ Bad Prompt</strong>
      <div class="prompt-example">
        Tell me about Paris
      </div>
    </div>
    
    <div class="good-prompt">
      <strong>✅ Good Prompt</strong>
      <div class="prompt-example">
        Create a 3-day itinerary for Paris in summer for a family with two teenagers. Include:<br/>
        • 2 famous landmarks per day<br/>
        • 1 unique local experience<br/>
        • Budget-friendly lunch options<br/>
        • Evening activities suitable for teens<br/>
        • Format as a daily schedule with times
      </div>
    </div>
  </div>
  
  <div class="info-box">
    <strong>🤔 Your Turn:</strong> Try both prompts with an AI and compare the results. What differences do you notice?
  </div>
  
  <div>
    <label style="display: block; font-weight: bold; color: #4ecca3 !important; margin-bottom: 10px;">📝 Share your findings:</label>
    <textarea id="travel-notes" placeholder="What differences did you notice between the bad and good prompts?"></textarea>
    <button onclick="saveChallenge('travel', document.getElementById('travel-notes').value)">Save My Notes ✅</button>
    <span id="travel-saved" class="saved-indicator">Saved! ✨</span>
  </div>
</div>

---

<div class="demo-container">
  <h2>✍️ Challenge 2: The Creative Writer</h2>
  <p>Discover how specificity improves creative output.</p>
  
  <div class="comparison-table">
    <div class="bad-prompt">
      <strong>❌ Bad Prompt</strong>
      <div class="prompt-example">
        Write a story
      </div>
    </div>
    
    <div class="good-prompt">
      <strong>✅ Good Prompt</strong>
      <div class="prompt-example">
        Write a 200-word mystery story set in a futuristic school where:<br/>
        • The protagonist is a student detective<br/>
        • Something valuable has gone missing<br/>
        • Include a surprising twist at the end<br/>
        • Use descriptive language and dialogue<br/>
        • Target audience: middle school readers
      </div>
    </div>
  </div>
  
  <div class="info-box">
    <strong>🤔 Your Turn:</strong> Which prompt gives you a more useful and interesting story?
  </div>
  
  <div>
    <label style="display: block; font-weight: bold; color: #4ecca3 !important; margin-bottom: 10px;">📝 Share your findings:</label>
    <textarea id="story-notes" placeholder="What made the good prompt's story better?"></textarea>
    <button onclick="saveChallenge('story', document.getElementById('story-notes').value)">Save My Notes ✅</button>
    <span id="story-saved" class="saved-indicator">Saved! ✨</span>
  </div>
</div>

---

<div class="demo-container">
  <h2>💻 Challenge 3: The Code Helper</h2>
  <p>See how technical requests benefit from detailed specifications.</p>
  
  <div class="comparison-table">
    <div class="bad-prompt">
      <strong>❌ Bad Prompt</strong>
      <div class="prompt-example">
        Help me with Python
      </div>
    </div>
    
    <div class="good-prompt">
      <strong>✅ Good Prompt</strong>
      <div class="prompt-example">
        I'm a beginner learning Python. Help me write a function that:<br/>
        • Takes a list of numbers as input<br/>
        • Returns only the even numbers<br/>
        • Include comments explaining each step<br/>
        • Provide an example of how to use the function<br/>
        • Explain why this approach works
      </div>
    </div>
  </div>
  
  <div class="info-box">
    <strong>🤔 Your Turn:</strong> Try asking for coding help both ways. Which gets you closer to what you actually need?
  </div>
  
  <div>
    <label style="display: block; font-weight: bold; color: #4ecca3 !important; margin-bottom: 10px;">📝 Share your findings:</label>
    <textarea id="code-notes" placeholder="How did specificity help with the coding task?"></textarea>
    <button onclick="saveChallenge('code', document.getElementById('code-notes').value)">Save My Notes ✅</button>
    <span id="code-saved" class="saved-indicator">Saved! ✨</span>
  </div>
</div>

---

## Part 3: Interactive Prompt Analyzer

<div class="demo-container">
  <h2>🎨 Prompt Quality Analyzer</h2>
  <p>Our AI-powered analyzer gives you instant feedback on your prompt quality!</p>
  
  <div>
    <label style="display: block; font-weight: bold; color: #4ecca3 !important; margin-bottom: 10px;">💭 Enter your prompt:</label>
    <textarea
      id="promptInput"
      placeholder="Type your prompt here... (e.g., 'Help me with homework' or 'Write a story')"
      oninput="analyzePrompt()"
      style="min-height: 120px;"
    ></textarea>
    <div style="text-align: right; color: #aaa; font-size: 0.9em; margin-top: 5px;">
      <span id="charCount">0</span> characters
    </div>
  </div>
  
  <div id="analysisResults" style="display: none; margin-top: 25px;">
    <div class="stats">
      <h3 style="color: #4ecca3 !important; margin-top: 0;">📊 Prompt Quality Score</h3>
      <div class="progress-bar">
        <div class="progress-fill" id="scoreIndicator" style="width: 0%;">
          <span id="scoreText">-</span>
        </div>
      </div>
    </div>
    
    <div class="analysis-box">
      <div class="stat-row">
        <span class="stat-label">🎯 Clarity:</span>
        <span class="stat-value" id="clarityScore">-</span>
      </div>
      <p id="clarityFeedback" style="color: #d1d5db !important; margin: 5px 0;"></p>
    </div>
    
    <div class="analysis-box">
      <div class="stat-row">
        <span class="stat-label">📚 Context:</span>
        <span class="stat-value" id="contextScore">-</span>
      </div>
      <p id="contextFeedback" style="color: #d1d5db !important; margin: 5px 0;"></p>
    </div>
    
    <div class="analysis-box">
      <div class="stat-row">
        <span class="stat-label">📋 Format:</span>
        <span class="stat-value" id="formatScore">-</span>
      </div>
      <p id="formatFeedback" style="color: #d1d5db !important; margin: 5px 0;"></p>
    </div>
    
    <div class="analysis-box">
      <div class="stat-row">
        <span class="stat-label">🔍 Specificity:</span>
        <span class="stat-value" id="specificityScore">-</span>
      </div>
      <p id="specificityFeedback" style="color: #d1d5db !important; margin: 5px 0;"></p>
    </div>
    
    <div id="suggestions" class="info-box">
      <h4 style="color: #4ecca3 !important; margin-top: 0;">💡 Suggestions for Improvement</h4>
      <ul id="suggestionsList" style="margin: 10px 0; padding-left: 20px;"></ul>
    </div>
    
    <div id="improvedPrompt" style="display: none;">
      <h4 style="color: #4ecca3 !important;">✨ Example Improved Version</h4>
      <div class="prompt-example">
        <p id="improvedPromptText" style="margin: 0; color: #d1d5db !important;"></p>
      </div>
    </div>
  </div>
  
  <div class="controls">
    <button onclick="document.getElementById('promptInput').value='Tell me about space'; analyzePrompt();">
      Example 1: Vague ❌
    </button>
    <button class="secondary" onclick="document.getElementById('promptInput').value='You are a science teacher. Explain black holes to a 12-year-old student using simple analogies and examples from everyday life. Keep it under 150 words and make it engaging.'; analyzePrompt();">
      Example 2: Great ✅
    </button>
  </div>
</div>

---

## Part 4: Pro Tips & Techniques

<div class="demo-container">
  <h2>💡 Interactive Tips Quiz</h2>
  <p>Click on each tip to reveal a challenge and test your skills!</p>
  
  <div class="quiz-tip" onclick="toggleQuiz(1)">
    <strong>🎭 Tip 1: Role Assignment</strong> <span style="float: right; color: #4ecca3 !important;">▼</span>
    <div id="quiz-1" style="display: none; margin-top: 10px; padding-top: 10px; border-top: 2px dashed #667eea;">
      <p style="color: #d1d5db !important; margin: 10px 0;">Try it: Write a prompt that assigns the AI the role of a "friendly chef teaching cooking to beginners"</p>
      <textarea id="quiz-1-input" placeholder="Write your prompt here..."></textarea>
      <button onclick="checkQuiz(1); event.stopPropagation();">Check My Answer ✓</button>
      <div id="quiz-1-feedback"></div>
    </div>
  </div>
  
  <div class="quiz-tip" onclick="toggleQuiz(2)">
    <strong>🎯 Tip 2: Few-Shot Learning</strong> <span style="float: right; color: #4ecca3 !important;">▼</span>
    <div id="quiz-2" style="display: none; margin-top: 10px; padding-top: 10px; border-top: 2px dashed #667eea;">
      <p style="color: #d1d5db !important; margin: 10px 0;">Try it: Provide examples to teach AI to convert sentences to hashtags</p>
      <textarea id="quiz-2-input" placeholder="Example: 'I love pizza' → #FoodLover #PizzaTime"></textarea>
      <button onclick="checkQuiz(2); event.stopPropagation();">Check My Answer ✓</button>
      <div id="quiz-2-feedback"></div>
    </div>
  </div>
  
  <div class="quiz-tip" onclick="toggleQuiz(3)">
    <strong>📋 Tip 3: Breaking Into Steps</strong> <span style="float: right; color: #4ecca3 !important;">▼</span>
    <div id="quiz-3" style="display: none; margin-top: 10px; padding-top: 10px; border-top: 2px dashed #667eea;">
      <p style="color: #d1d5db !important; margin: 10px 0;">Try it: Break down "plan my birthday party" into clear steps</p>
      <textarea id="quiz-3-input" placeholder="Step 1: ..." style="min-height: 100px;"></textarea>
      <button onclick="checkQuiz(3); event.stopPropagation();">Check My Answer ✓</button>
      <div id="quiz-3-feedback"></div>
    </div>
  </div>
</div>

---

## Part 5: Real-World Applications

<div class="feature-grid">
  <div class="feature-card">
    <strong>🎓 Students</strong>
    <span>Getting better homework help and study materials</span>
  </div>
  
  <div class="feature-card">
    <strong>💻 Developers</strong>
    <span>Writing code more efficiently</span>
  </div>
  
  <div class="feature-card">
    <strong>✍️ Writers</strong>
    <span>Brainstorming ideas and editing content</span>
  </div>
  
  <div class="feature-card">
    <strong>🔬 Researchers</strong>
    <span>Analyzing data and summarizing information</span>
  </div>
  
  <div class="feature-card">
    <strong>💼 Businesses</strong>
    <span>Creating marketing content and customer support</span>
  </div>
</div>

---

## Part 6: Reflection Questions

<div class="demo-container">
  <h2>🤔 Think About Your Learning</h2>
  
  <div style="margin: 20px 0;">
    <label style="display: block; font-weight: bold; color: #4ecca3 !important; margin-bottom: 10px;">
      1. How did adding details change the AI's responses?
    </label>
    <textarea class="reflection-input" data-reflection="1" placeholder="Type your reflection here..."></textarea>
  </div>
  
  <div style="margin: 20px 0;">
    <label style="display: block; font-weight: bold; color: #4ecca3 !important; margin-bottom: 10px;">
      2. What happened when you specified a format?
    </label>
    <textarea class="reflection-input" data-reflection="2" placeholder="Type your reflection here..."></textarea>
  </div>
  
  <div style="margin: 20px 0;">
    <label style="display: block; font-weight: bold; color: #4ecca3 !important; margin-bottom: 10px;">
      3. Did providing context make the answers more relevant?
    </label>
    <textarea class="reflection-input" data-reflection="3" placeholder="Type your reflection here..."></textarea>
  </div>
  
  <div style="margin: 20px 0;">
    <label style="display: block; font-weight: bold; color: #4ecca3 !important; margin-bottom: 10px;">
      4. Which techniques worked best for different types of tasks?
    </label>
    <textarea class="reflection-input" data-reflection="4" placeholder="Type your reflection here..."></textarea>
  </div>
  
  <div style="margin: 20px 0;">
    <label style="display: block; font-weight: bold; color: #4ecca3 !important; margin-bottom: 10px;">
      5. How can you apply prompt engineering to help with your schoolwork or projects?
    </label>
    <textarea class="reflection-input" data-reflection="5" placeholder="Type your reflection here..."></textarea>
  </div>
  
  <div style="text-align: center; margin-top: 20px;">
    <button onclick="saveReflections()">Save All Reflections 📝</button>
    <span id="reflection-saved" class="saved-indicator">All reflections saved! ✨</span>
  </div>
</div>

---

## Summary: Key Takeaways

<div class="takeaway-list">
  <div class="takeaway-item">
    ✨ <strong>Specific prompts get better results than vague ones</strong>
  </div>
  
  <div class="takeaway-item">
    🎯 <strong>Context helps AI understand what you really need</strong>
  </div>
  
  <div class="takeaway-item">
    💡 <strong>Examples guide AI to produce the format you want</strong>
  </div>
  
  <div class="takeaway-item">
    🔄 <strong>Iteration is key - refine your prompts based on results</strong>
  </div>
  
  <div class="takeaway-item">
    🚀 <strong>Prompt engineering is a valuable skill for working with AI tools</strong>
  </div>
</div>

<div style="text-align: center; padding: 30px; background: rgba(30, 41, 59, 0.8); border-radius: 15px; margin: 30px 0; border: 2px solid #4ecca3;">
  <h2 style="color: #4ecca3 !important; font-size: 2em; margin: 0;">🌟 Keep Practicing! 🌟</h2>
  <p style="color: #d1d5db !important; font-size: 1.2em; margin: 15px 0 0 0;">You're on your way to becoming a prompt engineering expert!</p>
</div>

---

<script>
// Challenge note saving
function saveChallenge(challenge, notes) {
  if (!notes.trim()) {
    alert('Please write something before saving!');
    return;
  }
  localStorage.setItem('ai-module-c3-challenge-' + challenge, notes);
  const savedIndicator = document.getElementById(challenge + '-saved');
  savedIndicator.style.display = 'inline';
  setTimeout(() => {
    savedIndicator.style.display = 'none';
  }, 3000);
}

// Load saved challenges on page load
document.addEventListener('DOMContentLoaded', function() {
  const challenges = ['travel', 'story', 'code'];
  challenges.forEach(challenge => {
    const saved = localStorage.getItem('ai-module-c3-challenge-' + challenge);
    if (saved) {
      const element = document.getElementById(challenge + '-notes');
      if (element) element.value = saved;
    }
  });

  // Load saved reflections
  document.querySelectorAll('.reflection-input').forEach(input => {
    const num = input.getAttribute('data-reflection');
    const saved = localStorage.getItem('ai-module-c3-reflection-' + num);
    if (saved) input.value = saved;
  });
  
  // Load saved quiz answers
  for (let i = 1; i <= 3; i++) {
    const saved = localStorage.getItem('ai-module-c3-quiz-' + i);
    if (saved) {
      const element = document.getElementById('quiz-' + i + '-input');
      if (element) element.value = saved;
    }
  }
});

// Save reflections
function saveReflections() {
  let count = 0;
  document.querySelectorAll('.reflection-input').forEach(input => {
    const num = input.getAttribute('data-reflection');
    if (input.value.trim()) {
      localStorage.setItem('ai-module-c3-reflection-' + num, input.value);
      count++;
    }
  });

  const savedIndicator = document.getElementById('reflection-saved');
  if (count > 0) {
    savedIndicator.textContent = `${count} reflection${count !== 1 ? 's' : ''} saved! ✨`;
    savedIndicator.style.display = 'inline';
    setTimeout(() => {
      savedIndicator.style.display = 'none';
    }, 4000);
  } else {
    alert('Please write at least one reflection before saving!');
  }
}

// Prompt analyzer
function analyzePrompt() {
  const input = document.getElementById('promptInput').value;
  const charCount = document.getElementById('charCount');
  const results = document.getElementById('analysisResults');

  charCount.textContent = input.length;

  if (input.length === 0) {
    results.style.display = 'none';
    return;
  }

  results.style.display = 'block';

  let scores = {
    clarity: 0,
    context: 0,
    format: 0,
    specificity: 0
  };

  let suggestions = [];

  // Clarity check
  const wordCount = input.trim().split(/\s+/).length;
  if (wordCount < 3) {
    scores.clarity = 2;
    document.getElementById('clarityFeedback').textContent = 'Too vague. Add more details about what you want.';
    suggestions.push('Be more specific about your goal or desired outcome');
  } else if (wordCount < 10) {
    scores.clarity = 5;
    document.getElementById('clarityFeedback').textContent = 'Basic clarity. Could use more details.';
    suggestions.push('Add more information about what specifically you need');
  } else {
    scores.clarity = 9;
    document.getElementById('clarityFeedback').textContent = 'Good length and detail!';
  }

  // Context check
  const contextWords = ['for', 'because', 'about', 'regarding', 'need', 'want', 'help', 'audience', 'purpose', 'background'];
  const hasContext = contextWords.some(word => input.toLowerCase().includes(word));
  const hasBullets = input.includes('•') || input.includes('-') || input.includes('*');

  if (!hasContext && wordCount > 5) {
    scores.context = 4;
    document.getElementById('contextFeedback').textContent = 'Missing context. Who is this for? What\'s the purpose?';
    suggestions.push('Add context: Who is your audience? What\'s the purpose?');
  } else if (hasContext) {
    scores.context = 9;
    document.getElementById('contextFeedback').textContent = 'Good context provided!';
  } else {
    scores.context = 2;
    document.getElementById('contextFeedback').textContent = 'No context detected.';
    suggestions.push('Provide background information or explain the situation');
  }

  // Format check
  const formatWords = ['format', 'table', 'list', 'points', 'paragraph', 'structure', 'include', 'columns', 'sections'];
  const hasFormat = formatWords.some(word => input.toLowerCase().includes(word)) || hasBullets;

  if (hasFormat || hasBullets) {
    scores.format = 9;
    document.getElementById('formatFeedback').textContent = 'Great! You specified the output format.';
  } else {
    scores.format = 3;
    document.getElementById('formatFeedback').textContent = 'No format specified. How should the AI respond?';
    suggestions.push('Specify the desired format (list, table, paragraph, etc.)');
  }

  // Specificity check
  const specificWords = ['specific', 'exactly', 'must', 'should', 'requirement', 'constraint', 'limit', 'between', 'maximum', 'minimum'];
  const hasNumbers = /\d/.test(input);
  const hasConstraints = specificWords.some(word => input.toLowerCase().includes(word)) || hasNumbers;

  if (hasConstraints && wordCount > 15) {
    scores.specificity = 10;
    document.getElementById('specificityFeedback').textContent = 'Excellent specificity with clear constraints!';
  } else if (hasConstraints || wordCount > 15) {
    scores.specificity = 7;
    document.getElementById('specificityFeedback').textContent = 'Good level of detail.';
  } else {
    scores.specificity = 3;
    document.getElementById('specificityFeedback').textContent = 'Too general. Add specific requirements or constraints.';
    suggestions.push('Add specific constraints (word count, style, requirements)');
  }

  // Update score displays
  document.getElementById('clarityScore').textContent = getScoreEmoji(scores.clarity) + ' ' + scores.clarity + '/10';
  document.getElementById('contextScore').textContent = getScoreEmoji(scores.context) + ' ' + scores.context + '/10';
  document.getElementById('formatScore').textContent = getScoreEmoji(scores.format) + ' ' + scores.format + '/10';
  document.getElementById('specificityScore').textContent = getScoreEmoji(scores.specificity) + ' ' + scores.specificity + '/10';

  // Calculate overall score
  const overallScore = Math.round((scores.clarity + scores.context + scores.format + scores.specificity) / 4);
  const scorePercent = overallScore * 10;

  document.getElementById('scoreIndicator').style.width = scorePercent + '%';
  document.getElementById('scoreText').textContent = overallScore + '/10 - ' + getScoreLabel(overallScore);

  // Show suggestions
  const suggestionsList = document.getElementById('suggestionsList');
  if (suggestions.length > 0) {
    suggestionsList.innerHTML = suggestions.map(s => '<li>' + s + '</li>').join('');
  } else {
    suggestionsList.innerHTML = '<li>Excellent work! Your prompt is well-structured.</li>';
  }

  // Generate improved version for low scores
  if (overallScore < 7) {
    generateImprovedPrompt(input, scores);
  } else {
    document.getElementById('improvedPrompt').style.display = 'none';
  }
}

function getScoreEmoji(score) {
  if (score >= 8) return '🌟';
  if (score >= 6) return '👍';
  if (score >= 4) return '⚠️';
  return '❌';
}

function getScoreLabel(score) {
  if (score >= 9) return 'Excellent!';
  if (score >= 7) return 'Good Job!';
  if (score >= 5) return 'Getting There';
  if (score >= 3) return 'Needs Work';
  return 'Too Vague';
}

function generateImprovedPrompt(original, scores) {
  const improved = document.getElementById('improvedPrompt');
  const improvedText = document.getElementById('improvedPromptText');

  let enhancement = original;
  let additions = [];

  if (scores.context < 6) {
    additions.push('[Add context: specify your audience, purpose, or background]');
  }
  if (scores.format < 6) {
    additions.push('[Specify format: e.g., "Format as a bulleted list" or "Provide in table format"]');
  }
  if (scores.specificity < 6) {
    additions.push('[Add constraints: e.g., "in 200 words" or "include 3 examples"]');
  }

  if (additions.length > 0) {
    enhancement = original + '\n\n' + additions.join('\n');
  }

  improvedText.textContent = enhancement;
  improved.style.display = 'block';
}

// Quiz functions
function toggleQuiz(num) {
  const quiz = document.getElementById('quiz-' + num);
  const isVisible = quiz.style.display !== 'none';

  for (let i = 1; i <= 3; i++) {
    document.getElementById('quiz-' + i).style.display = 'none';
  }

  if (!isVisible) {
    quiz.style.display = 'block';
  }
}

function checkQuiz(num) {
  const input = document.getElementById('quiz-' + num + '-input').value.trim();
  const feedback = document.getElementById('quiz-' + num + '-feedback');

  if (!input) {
    feedback.innerHTML = '<p class="feedback-negative">Please write something first!</p>';
    return;
  }

  const wordCount = input.split(/\s+/).length;
  let message = '';

  if (num === 1) {
    const hasRole = /you are|act as|as a|pretend/i.test(input);
    if (hasRole && wordCount > 5) {
      message = '<p class="feedback-positive">🌟 Excellent! You clearly assigned a role to the AI!</p>';
    } else {
      message = '<p class="feedback-warning">💡 Good start! Try using phrases like "You are a..." or "Act as a..." to make the role crystal clear.</p>';
    }
  } else if (num === 2) {
    const hasArrow = /→|->|:|=>/i.test(input);
    const hasExample = wordCount > 8;
    if (hasArrow && hasExample) {
      message = '<p class="feedback-positive">🌟 Perfect! You provided clear examples with the pattern!</p>';
    } else {
      message = '<p class="feedback-warning">💡 Try showing multiple examples with arrows (→) to demonstrate the pattern!</p>';
    }
  } else if (num === 3) {
    const hasSteps = /step|1\.|2\.|•|-/i.test(input);
    if (hasSteps && wordCount > 15) {
      message = '<p class="feedback-positive">🌟 Great job! You broke it down into clear, actionable steps!</p>';
    } else {
      message = '<p class="feedback-warning">💡 Try breaking it into numbered steps or bullet points for clarity!</p>';
    }
  }

  feedback.innerHTML = message;
  localStorage.setItem('ai-module-c3-quiz-' + num, input);
}

// Completion tracking
document.addEventListener("DOMContentLoaded", function() {
  const storageKey = 'ai-module-c3-completed';
  
  if (localStorage.getItem(storageKey) === 'true') {
    return;
  }
  
  let hasScrolledToBottom = false;
  
  function checkScrollPosition() {
    const scrollTop = window.scrollY;
    const windowHeight = window.innerHeight;
    const documentHeight = document.documentElement.scrollHeight;
    
    if (scrollTop + windowHeight >= documentHeight - 100) {
      if (!hasScrolledToBottom) {
        hasScrolledToBottom = true;
        localStorage.setItem(storageKey, 'true');
        
        const banner = document.createElement('div');
        banner.className = 'completion-banner';
        banner.innerHTML = `
          <h3 style="margin: 0; font-size: 18px; font-weight: bold;">🎉 Module 3 Completed!</h3>
          <p style="margin: 5px 0 0 0; font-size: 14px;">Module 4 unlocked!</p>
        `;
        document.body.appendChild(banner);
        
        setTimeout(() => {
          banner.style.animation = 'slideIn 0.5s ease-out reverse';
          setTimeout(() => banner.remove(), 500);
        }, 4000);
        
        window.removeEventListener('scroll', checkScrollPosition);
      }
    }
  }
  
  window.addEventListener('scroll', checkScrollPosition);
  checkScrollPosition();
});
</script>