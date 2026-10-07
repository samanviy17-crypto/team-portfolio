---
layout: cs-bigsix-lesson
title: "AI Development — All-in-One Interactive Lesson"
description: "A multi-step interactive lesson on using AI for prompt engineering, coding, and professional development."
permalink: /bigsix/ai_lesson
parent: "bigsix"
lesson_number: 5
team: "Thinkers"
categories: [CSP, AI, Interactive]
tags: [ai, prompt-engineering, interactive]
author: "Thinkers Team"
date: 2025-12-02
---

<style>
{{ '@import "beasts/inline/pages/hacks-thebig6-ai-ai-lesson-1";' | scssify }}
</style>

<div class="container page-content">
  <div class="header">
    <h1>AI Development — All-in-One</h1>
    <p>A multi-step interactive lesson on using AI for prompt engineering, coding, and professional development.</p>
    <a href="../" class="back-btn">← Back</a>
  </div>

  <div class="progress-bar" id="progressBar"></div>

  <!-- Step 1: Prompt Engineering -->
  <div class="section active" id="step1">
    <div class="card">
      <h2>1 — Prompt Engineering</h2>
      <p>Mastering the art of communication with AI is the first step. A great prompt includes four key ingredients: Context, Problem, What You've Tried, and What You Need.</p>
      <ul>
        <li><strong>The Prompt Formula</strong>: A great prompt includes four key ingredients:
          <ol>
            <li><strong>Context</strong>: What are you working with? (e.g., Python, Flask, a specific library)</li>
            <li><strong>Problem</strong>: What is the specific issue? (e.g., "I'm getting a 404 error")</li>
            <li><strong>What You've Tried</strong>: Show your work. (e.g., "I've checked the routes and tested with Postman")</li>
            <li><strong>What You Need</strong>: What is your desired outcome? (e.g., "I need a checklist of likely causes")</li>
          </ol>
        </li>
        <li><strong>Iterate, Don't Quit</strong>: The first response from an AI is rarely perfect. The key to success is to refine your prompt based on the AI's output. Add more specifics, clarify your needs, and guide the AI to the correct solution. Winners iterate 3–5 times.</li>
      </ul>
    </div>
  </div>

  <!-- Step 2: Coding with AI -->
  <div class="section" id="step2">
    <div class="card">
      <h2>2 — Coding with AI</h2>
      <p>When it comes to generating code, specificity is everything. Use frameworks and checklists to ensure your AI-generated code is safe and effective.</p>
      <ul>
        <li><strong>The SPEC Framework</strong>: To get useful code, your prompt must be a detailed specification: Specific, Platform, Examples, and Constraints.</li>
        <li><strong>4-Step Debugging Template</strong>: When you're stuck, give the AI the information it needs: Problem, Expected vs. Actual, Minimal Code, and What You Tried.</li>
        <li><strong>The 5 Security Non-Negotiables</strong>: Always check for SQL Injection, Hardcoded Secrets, Input Validation, XSS, and improper Authentication/Authorization.</li>
      </ul>
    </div>
  </div>

  <!-- Step 3: Professional Applications -->
  <div class="section" id="step3">
    <div class="card">
      <h2>3 — Professional Applications</h2>
      <p>Leverage AI to accelerate your career, but know its limits. Use it for resume building, interview prep, and more.</p>
      <ul>
        <li><strong>Resume Transformation with STAR</strong>: Turn weak resume points into compelling, quantified achievements (Situation, Task, Action, Result).</li>
        <li><strong>Interview Preparation</strong>: Practice answering crucial questions about failure, project architecture, and your interest in the company.</li>
        <li><strong>Know When to Use AI</strong>: It's great for summarizing and brainstorming, but bad for highly specialized or sensitive topics where accuracy is critical.</li>
      </ul>
    </div>
  </div>

  <!-- Step 4: Resume Transformer -->
  <div class="section" id="step4">
    <div class="card">
      <h2>4 — Interactive: Resume Transformer</h2>
      <div class="tool-panel">
        <h3>Resume Bullet Transformer</h3>
        <p>Paste your weak bullet point and we'll generate 3 STAR versions!</p>
        <label>Your Current Bullet:</label>
        <textarea id="weak-bullet" placeholder="e.g., 'Worked on website development'" rows="3"></textarea>
        <button class="action-button" onclick="generateVersions()">✦ Transform to STAR Format</button>
        <div id="versions-container" style="display:none; margin-top:16px;">
          <div class="version-card"><h4>Version 1 — Conservative</h4><p id="version-conservative"></p></div>
          <div class="version-card"><h4>Version 2 — Balanced</h4><p id="version-balanced"></p></div>
          <div class="version-card"><h4>Version 3 — Bold</h4><p id="version-bold"></p></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Step 5: Interview Analyzer -->
  <div class="section" id="step5">
    <div class="card">
      <h2>5 — Interactive: Interview Analyzer</h2>
      <div class="tool-panel">
        <h3>Mock Interview Analyzer</h3>
        <p>Type your answer to one of the questions below (250 words max).</p>
        <label>Which question are you answering?</label>
        <select id="question-choice">
          <option value="1">Question 1: Tell me about a time you failed</option>
          <option value="2">Question 2: Walk me through your architecture</option>
          <option value="3">Question 3: Why this company?</option>
        </select>
        <label>Your Answer:</label>
        <textarea id="interview-answer" placeholder="Type your answer here..." rows="6"></textarea>
        <button class="action-button" onclick="analyzeInterview()">🔍 Analyze My Answer</button>
        <div class="analysis-result" id="analysis-result">
          <h4>Analysis Results</h4>
          <div id="analysis-content"></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Step 6: AI Use Case Sorter -->
  <div class="section" id="step6">
    <div class="card">
      <h2>6 — Interactive: AI Use Case Sorter</h2>
      <div class="tool-panel">
        <h3>Use Case Sorter Game</h3>
        <p>Click each scenario card to sort it — confirm if it's a <strong style="color:#4ade80;">good</strong> or <strong style="color:#f87171;">bad</strong> use of AI.</p>
        <p>Score: <span id="game-score">0/6</span> correct</p>
        <div id="scenarios-container"></div>
        <button class="action-button" onclick="resetGame()" style="margin-top:16px;">↺ Reset Game</button>
      </div>
    </div>
  </div>

  <!-- Navigation -->
  <div class="nav-buttons">
    <button id="prevBtn" onclick="prevStep()" class="secondary">← Previous</button>
    <div class="flex-row">
      <span id="stepIndicator">Step 1 / 6</span>
      <button id="nextBtn" onclick="nextStep()" class="primary">Next →</button>
    </div>
  </div>
</div>

<script>
// ── Config ────────────────────────────────────────────────────────────────────
// Primary: Flask /api/gemini (requires login cookie).
// Fallback: Spring /api/chatbot/chat (no auth required).
const FLASK_URL  = 'https://flask.opencodingsociety.com';
const SPRING_URL = 'https://spring.opencodingsociety.com';
const GEMINI_ENDPOINT        = `${FLASK_URL}/api/gemini`;
const SPRING_CHAT_ENDPOINT   = `${SPRING_URL}/api/chatbot/chat`;

// ── Shared AI helper — tries Flask first, falls back to Spring ────────────────
// Returns { text: <string> } on success, throws on total failure.
async function callGemini(promptText, fullPrompt) {
  // 1️⃣ Try Flask (works when user is logged in via cookie)
  try {
    const res = await fetch(GEMINI_ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'include',
      body: JSON.stringify({ text: promptText, prompt: fullPrompt })
    });
    if (res.ok) {
      const data = await res.json();
      if (data.success && data.text) return { text: data.text };
    }
    // Non-ok or success:false → fall through to Spring
  } catch (_) { /* network error → fall through */ }

  // 2️⃣ Fallback: Spring /api/chatbot/chat (no auth required)
  const springRes = await fetch(SPRING_CHAT_ENDPOINT, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      userId: 'lesson-guest',
      message: `${fullPrompt}: ${promptText}`
    })
  });
  if (!springRes.ok) throw new Error(`AI service error ${springRes.status}. Please try again.`);
  const springData = await springRes.json();
  const text = springData.response || springData.text || '';
  if (!text) throw new Error('No response from AI service.');
  return { text };
}

// ── State & Navigation ────────────────────────────────────────────────────────
let currentStep = 0;
const steps = ['step1','step2','step3','step4','step5','step6'];
const STORAGE_KEY = 'ai_combined_v1';

const BIG_SIX_META = { module: 'ai_lesson', lesson: 5 };

function completeBigSixLesson() {
  const key = `bigsix:${BIG_SIX_META.module}:lesson:${BIG_SIX_META.lesson}`;
  if (localStorage.getItem(key) !== 'done') {
    localStorage.setItem(key, 'done');
    console.log(`✅ Big Six completed: ${key}`);
  }
}

function showStep(n) {
  currentStep = Math.max(0, Math.min(steps.length - 1, n));

  steps.forEach((s, i) => {
    const el = document.getElementById(s);
    if (el) el.classList.toggle('active', i === currentStep);
  });

  const bar = document.getElementById('progressBar');
  if (bar) bar.innerHTML = steps.map((_, i) =>
    `<div class="step ${i <= currentStep ? 'active' : ''}" onclick="showStep(${i})"></div>`
  ).join('');

  const indicator = document.getElementById('stepIndicator');
  if (indicator) indicator.textContent = `Step ${currentStep + 1} / ${steps.length}`;

  const prevBtn = document.getElementById('prevBtn');
  if (prevBtn) prevBtn.disabled = currentStep === 0;

  const nextBtn = document.getElementById('nextBtn');
  if (nextBtn) nextBtn.disabled = currentStep === steps.length - 1;

  persist();

  if (currentStep === steps.length - 1) completeBigSixLesson();
}

function prevStep() { showStep(currentStep - 1); }
function nextStep() { showStep(currentStep + 1); }
window.prevStep = prevStep;
window.nextStep = nextStep;
window.showStep = showStep;

// ── Resume Transformer (AI-powered — Flask first, Spring fallback) ───────────
async function generateVersions() {
  const weakBullet = document.getElementById('weak-bullet').value.trim();
  if (!weakBullet) { alert('Please enter a resume bullet point first!'); return; }

  const btn = document.querySelector('[onclick="generateVersions()"]');
  const container = document.getElementById('versions-container');
  const ids = ['version-conservative', 'version-balanced', 'version-bold'];

  btn.disabled = true;
  btn.textContent = 'Generating…';
  container.style.display = 'block';
  ids.forEach(id => {
    document.getElementById(id).innerHTML = '<div class="ai-loading"><div class="ai-spinner"></div>Thinking…</div>';
  });

  const prev = document.getElementById('transformer-error');
  if (prev) prev.remove();

  const resumePrompt = `You are a professional resume coach. Transform this weak resume bullet point into 3 STAR-format versions.

Respond ONLY with valid JSON — no markdown, no backticks, no extra text. Use this exact structure:
{
  "conservative": "one sentence, modest tone, no invented metrics",
  "balanced": "one sentence, moderate achievements, 1 realistic metric",
  "bold": "one sentence, strong action verb, 1-2 impactful metrics"
}

Rules:
- Each version must be a single polished resume bullet (one sentence)
- Start with a strong past-tense action verb
- Use STAR structure: imply Situation/Task, show Action, hint at Result
- Do NOT invent specific company names or technologies not mentioned
- Conservative: stay close to the original, just strengthen the language
- Balanced: add one plausible metric (e.g. 20%, 5 features, 3-person team)
- Bold: make it sound impressive with 1-2 quantified results
- The bullet to transform is`;

  try {
    const { text } = await callGemini(weakBullet, resumePrompt);

    let parsed;
    try {
      parsed = JSON.parse(text.replace(/```json|```/g, '').trim());
    } catch {
      // Gemini sometimes returns plain text — show it in all three cards
      const fallback = text.trim() || '—';
      ids.forEach(id => { document.getElementById(id).textContent = fallback; });
      return;
    }

    document.getElementById('version-conservative').textContent = parsed.conservative || '—';
    document.getElementById('version-balanced').textContent     = parsed.balanced     || '—';
    document.getElementById('version-bold').textContent         = parsed.bold         || '—';

  } catch (err) {
    ids.forEach(id => { document.getElementById(id).textContent = ''; });
    container.insertAdjacentHTML('beforebegin',
      `<div class="ai-error" id="transformer-error">⚠ ${err.message}</div>`);
  } finally {
    btn.disabled = false;
    btn.textContent = '✦ Transform to STAR Format';
  }
}
window.generateVersions = generateVersions;

// ── Interview Analyzer (AI-powered — Flask first, Spring fallback) ───────────
async function analyzeInterview() {
  const answer   = document.getElementById('interview-answer').value.trim();
  const qChoice  = document.getElementById('question-choice').value;
  if (!answer) { alert('Please write your interview answer first!'); return; }

  const questionMap = {
    '1': 'Tell me about a time you failed.',
    '2': 'Walk me through your project architecture.',
    '3': 'Why do you want to work at this company?'
  };
  const question = questionMap[qChoice];

  const btn        = document.querySelector('[onclick="analyzeInterview()"]');
  const resultBox  = document.getElementById('analysis-result');
  const contentEl  = document.getElementById('analysis-content');

  btn.disabled = true;
  btn.textContent = 'Analyzing…';
  resultBox.style.display = 'block';
  contentEl.innerHTML = '<div class="ai-loading"><div class="ai-spinner"></div>Analyzing your answer…</div>';

  const prev = document.getElementById('interview-error');
  if (prev) prev.remove();

  const interviewPrompt = `You are an experienced technical interviewer and career coach. The candidate was asked: "${question}". Analyze their answer below.

Respond ONLY with valid JSON — no markdown, no backticks, no preamble. Use exactly this structure:
{
  "wordCount": <number>,
  "scores": {
    "structure": { "rating": "good|ok|poor", "feedback": "one sentence" },
    "specificity": { "rating": "good|ok|poor", "feedback": "one sentence" },
    "metrics": { "rating": "good|ok|poor", "feedback": "one sentence" },
    "relevance": { "rating": "good|ok|poor", "feedback": "one sentence" }
  },
  "overallFeedback": "2-3 sentences of actionable coaching advice",
  "improvedOpener": "Rewrite just the first sentence of their answer to be stronger"
}

The candidate's answer is`;

  try {
    const { text } = await callGemini(answer, interviewPrompt);

    let parsed;
    try {
      parsed = JSON.parse(text.replace(/```json|```/g, '').trim());
    } catch {
      throw new Error('Could not parse AI response. Try again.');
    }

    const ratingColor = r => r === 'good' ? 'good' : r === 'ok' ? '' : 'bad';
    const ratingLabel = r => r === 'good' ? '✓ Good' : r === 'ok' ? '~ OK' : '✗ Needs work';

    const badgeStyle = r => {
      if (r === 'good') return 'background:var(--good);border:1px solid var(--good-border);color:#4ade80;';
      if (r === 'ok')   return 'background:rgba(234,179,8,0.1);border:1px solid rgba(234,179,8,0.4);color:#fbbf24;';
      return 'background:var(--bad);border:1px solid var(--bad-border);color:#f87171;';
    };

    const scores = parsed.scores || {};
    const labels = { structure: 'STAR Structure', specificity: 'Specificity', metrics: 'Metrics/Numbers', relevance: 'Relevance to Question' };

    let html = `<div style="font-size:12px;color:var(--muted);margin-bottom:12px;">${parsed.wordCount || '?'} words</div>`;

    html += '<div style="display:grid;gap:8px;margin-bottom:16px;">';
    for (const [key, label] of Object.entries(labels)) {
      const s = scores[key] || {};
      html += `<div style="display:flex;gap:10px;align-items:flex-start;">
        <span style="flex-shrink:0;padding:3px 10px;border-radius:20px;font-size:11px;font-weight:600;${badgeStyle(s.rating)}">${ratingLabel(s.rating)}</span>
        <span style="font-size:13px;"><strong style="color:#a6c9ff;">${label}:</strong> ${s.feedback || ''}</span>
      </div>`;
    }
    html += '</div>';

    if (parsed.overallFeedback) {
      html += `<div style="background:var(--blue-bg);border:1px solid var(--blue-border);border-radius:8px;padding:12px;margin-bottom:12px;font-size:13px;line-height:1.7;">
        <strong style="color:var(--blue);display:block;margin-bottom:4px;">Coach Feedback</strong>
        ${parsed.overallFeedback}
      </div>`;
    }
    if (parsed.improvedOpener) {
      html += `<div style="background:var(--accent-soft);border:1px solid var(--accent-border);border-radius:8px;padding:12px;font-size:13px;line-height:1.7;">
        <strong style="color:#c4b5fd;display:block;margin-bottom:4px;">Stronger Opening</strong>
        "${parsed.improvedOpener}"
      </div>`;
    }

    contentEl.innerHTML = html;

  } catch (err) {
    contentEl.innerHTML = '';
    resultBox.insertAdjacentHTML('beforebegin',
      `<div class="ai-error" id="interview-error">⚠ ${err.message}</div>`);
  } finally {
    btn.disabled = false;
    btn.textContent = '🔍 Analyze My Answer';
  }
}
window.analyzeInterview = analyzeInterview;

// ── Use Case Sorter ───────────────────────────────────────────────────────────
let gameScore = 0;
const scenarios = [
  { text: 'Summarize a 50-page research paper',     correct: 'good' },
  { text: 'Generate a legal contract for a startup', correct: 'bad'  },
  { text: 'Write a SQL query for a database',        correct: 'good' },
  { text: 'Diagnose chest pain symptoms',            correct: 'bad'  },
  { text: 'Brainstorm app feature ideas',            correct: 'good' },
  { text: 'Calculate structural load for a bridge',  correct: 'bad'  },
];

function initializeGame() {
  const container = document.getElementById('scenarios-container');
  if (!container) return;
  container.innerHTML = '';
  gameScore = 0;
  scenarios.forEach(scenario => {
    const card = document.createElement('div');
    card.className = 'scenario-card';
    card.textContent = scenario.text;
    card.onclick = () => handleScenarioClick(card, scenario.correct);
    container.appendChild(card);
  });
  updateScore();
}

function handleScenarioClick(card, correctAnswer) {
  if (card.classList.contains('correct') || card.classList.contains('incorrect')) return;
  const userChoice = confirm(`Is "${card.textContent}" a GOOD use of AI?\n\nOK = Yes (good use)\nCancel = No (bad use)`);
  const choice = userChoice ? 'good' : 'bad';
  if (choice === correctAnswer) { card.classList.add('correct'); gameScore++; }
  else { card.classList.add('incorrect'); }
  updateScore();
}

function updateScore() {
  const el = document.getElementById('game-score');
  if (el) el.textContent = `${gameScore}/${scenarios.length}`;
}

function resetGame() { initializeGame(); }
window.resetGame = resetGame;

// ── Persistence ───────────────────────────────────────────────────────────────
function persist() {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify({
      step: currentStep,
      weakBullet: document.getElementById('weak-bullet')?.value || '',
      interviewAnswer: document.getElementById('interview-answer')?.value || '',
    }));
  } catch(e) {}
}

function restore() {
  try {
    const data = JSON.parse(localStorage.getItem(STORAGE_KEY));
    if (!data) return;
    const wb = document.getElementById('weak-bullet');
    if (wb && data.weakBullet) wb.value = data.weakBullet;
    const ia = document.getElementById('interview-answer');
    if (ia && data.interviewAnswer) ia.value = data.interviewAnswer;
    showStep(data.step || 0);
  } catch(e) { showStep(0); }
}

// ── Boot ──────────────────────────────────────────────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
  restore();
  initializeGame();
  // Ensure progress bar renders even if restore() skips showStep
  if (!document.querySelector('#progressBar .step')) showStep(0);
});
</script>

<script>
// Back button handler
(function(){
  document.addEventListener('DOMContentLoaded', function(){
    document.querySelectorAll('a.back-btn').forEach(function(a){
      a.addEventListener('click', function(e){
        if (e.metaKey || e.ctrlKey || e.shiftKey || e.button === 1) return;
        e.preventDefault();
        try {
          if (document.referrer && new URL(document.referrer).origin === location.origin) {
            history.back(); return;
          }
        } catch(err) {}
        var p = location.pathname.replace(/\/$/, '').split('/');
        if (p.length > 1) { p.pop(); window.location.href = p.join('/') + '/'; }
        else { window.location.href = '/'; }
      });
    });
  });
})();
</script>

<script src="/assets/js/lesson-completion-bigsix.js"></script>