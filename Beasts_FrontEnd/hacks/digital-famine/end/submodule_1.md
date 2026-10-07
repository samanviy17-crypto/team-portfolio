---
layout: post
title: "Task 1 for End Quest"
description: "Submodule 1 for End Quest"
permalink: /digital-famine/end/submodule_1/
parent: "End Quest"
team: "CodeMaxxers"
submodule: 1
tags: [end, submodule, codemaxxers]
author: "William Windle"
microblog: true
date: 2025-10-24
---
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Satellite Repair Mission</title>
  <style>
{{ '@import "beasts/inline/pages/hacks-digital-famine-end-submodule-1-1";' | scssify }}
</style>
</head>
<body>
  <div class="stars" id="stars"></div>
  
  <div class="container">
    <div class="mission-header">
      <h1>🛰️ SATELLITE LINK REPAIR PROTOCOL</h1>
      <p class="subtitle">Mission: Diagnose and repair corrupted communication signals between Ground Control and RSV-Phoenix</p>
    </div>

    <div id="intro-section">
      <div class="hud-container">
        <div class="hud-card">
          <h3>⚡ SYSTEMS STATUS</h3>
          <div class="hud-value" id="intro-progress">0/5</div>
          <div class="progress-bar">
            <div class="progress-fill" id="intro-progress-bar" style="width: 0%"></div>
          </div>
        </div>
        <div class="hud-card">
          <h3>🎯 DIAGNOSTIC ACCURACY</h3>
          <div class="hud-value" id="intro-accuracy">0%</div>
          <div class="progress-bar">
            <div class="progress-fill" id="intro-accuracy-bar" style="width: 0%"></div>
          </div>
        </div>
        <div class="hud-card">
          <h3>📡 SIGNAL INTEGRITY</h3>
          <div class="hud-value">DEGRADED</div>
          <p style="color: var(--warning); font-size: 0.9rem; margin-top: 0.5rem;">⚠️ Multiple transmission anomalies detected</p>
        </div>
      </div>

      <div class="console-card">
        <h2 style="margin-bottom: 1rem;">🚀 Mission Brief</h2>
        <p style="line-height: 1.8; color: var(--text-muted); margin-bottom: 1.5rem;">
          The RSV-Phoenix has lost primary satellite connection during its Mars approach sequence. 
          You are receiving 5 diagnostic transmissions through backup channels. Each transmission 
          may contain <strong style="color: var(--success)">VALID signal data</strong> or 
          <strong style="color: var(--danger)">CORRUPTED interference</strong>.
        </p>
        <p style="line-height: 1.8; color: var(--text-muted); margin-bottom: 2rem;">
          Your task: Analyze signal patterns, source authenticity, data integrity markers, and 
          protocol compliance to identify which transmissions are safe to route to the ship's 
          navigation system. One wrong diagnosis could send false coordinates to the crew.
        </p>
        <div style="text-align: center;">
          <button class="btn-primary" id="start-btn">Initialize Diagnostic Sequence</button>
          <div style="margin-top: 1rem;">
            <button class="btn-primary" id="test-btn" style="background: linear-gradient(90deg, var(--warning), #f97316); font-size: 0.9rem; padding: 0.75rem 1.5rem;">⚡ Test Mode (Auto-Complete)</button>
          </div>
        </div>
      </div>
    </div>

    <div id="mission-section" class="hidden">
      <div class="hud-container">
        <div class="hud-card">
          <h3>⚡ SIGNALS PROCESSED</h3>
          <div class="hud-value" id="mission-progress">0/5</div>
          <div class="progress-bar">
            <div class="progress-fill" id="mission-progress-bar" style="width: 0%"></div>
          </div>
        </div>
        <div class="hud-card">
          <h3>🎯 REPAIR ACCURACY</h3>
          <div class="hud-value" id="mission-accuracy">0%</div>
          <div class="progress-bar">
            <div class="progress-fill" id="mission-accuracy-bar" style="width: 0%"></div>
          </div>
        </div>
      </div>

      <div class="console-card">
        <div class="transmission-card">
          <div class="transmission-header">
            <div>
              <div style="font-size: 0.85rem; color: var(--text-muted); margin-bottom: 0.25rem;">TRANSMISSION ID</div>
              <div style="font-size: 1.3rem; font-weight: 700;" id="signal-id">#001</div>
            </div>
            <div class="signal-status">
              <div class="signal-dot" id="signal-dot" style="background: var(--signal-good)"></div>
              <span id="signal-count">Signal 1/5</span>
            </div>
          </div>

          <div class="transmission-data">
            <span class="data-label">SOURCE:</span>
            <div id="signal-source" style="margin-bottom: 1rem;"></div>
            
            <span class="data-label">SIGNAL DATA:</span>
            <div id="signal-content"></div>
          </div>

          <div class="diagnostic-prompt">⚙️ Diagnostic Assessment Required:</div>
          <div class="choices-grid">
            <button class="choice-btn" id="btn-valid">
              <span>✅</span>
              <span>VALID SIGNAL</span>
            </button>
            <button class="choice-btn" id="btn-corrupted">
              <span>⚠️</span>
              <span>CORRUPTED DATA</span>
            </button>
          </div>

          <div id="feedback" class="hidden"></div>

          <div id="next-container" class="hidden" style="text-align: center; margin-top: 1.5rem;">
            <button class="btn-primary" id="btn-next">Next Transmission →</button>
          </div>
        </div>
      </div>
    </div>

    <div id="results-section" class="hidden">
      <div class="console-card">
        <div class="results-panel">
          <h2 style="font-size: 2rem; margin-bottom: 1rem;">🛰️ REPAIR SEQUENCE COMPLETE</h2>
          <div class="results-score" id="final-score">0/5</div>
          
          <div class="hud-container" style="max-width: 500px; margin: 2rem auto;">
            <div class="hud-card">
              <h3>📊 FINAL ACCURACY RATING</h3>
              <div class="hud-value" id="final-accuracy">0%</div>
              <div class="progress-bar">
                <div class="progress-fill" id="final-accuracy-bar" style="width: 0%"></div>
              </div>
            </div>
          </div>

          <div id="verdict" class="results-verdict"></div>

          <div class="btn-container">
            <button class="btn-primary" onclick="location.reload()">🔄 Run Diagnostics Again</button>
            <button class="btn-primary hidden" id="return-mission-btn">🚀 Return to Mission</button>
          </div>
        </div>
      </div>
    </div>
  </div>

  <script>
    // Generate stars
    (function() {
      const starsContainer = document.getElementById('stars');
      for (let i = 0; i < 100; i++) {
        const star = document.createElement('div');
        star.className = 'star';
        star.style.left = Math.random() * 100 + '%';
        star.style.top = Math.random() * 100 + '%';
        star.style.animationDelay = Math.random() * 3 + 's';
        starsContainer.appendChild(star);
      }
    })();

    // Only 5 signals now
    const signals = [
      {
        id: "RSV-PHX-001",
        source: "@NASA_DeepSpace • Verified Ground Control Station • Houston, TX",
        content: "RSV-Phoenix trajectory update: Orbital insertion burn scheduled T-minus 72 hours. Delta-V requirement: 1,247 m/s. Telemetry nominal. Full burn sequence uploaded to primary nav computer. Verification code: MARS-2025-PHX-ALPHA.",
        answer: "valid",
        explanation: "VALID: Official NASA source with verification badge, specific technical parameters (Delta-V, timing), procedural language, verification code included. Standard mission update protocol followed."
      },
      {
        id: "ANON-LEAK-447",
        source: "@SpaceLeaks_Insider • Unverified Account • Location Hidden",
        content: "🚨 URGENT: Phoenix crew in DANGER! NASA hiding critical system failures. Thermal shielding compromised but they won't abort mission. SHARE before they silence this! Anonymous source inside mission control confirms coverup. Trust NO official statements!",
        answer: "corrupted",
        explanation: "CORRUPTED: Unverified source, sensational fear language, conspiracy framing, no technical specifics, urgency manipulation tactics, attacks official sources without evidence. Classic misinformation signature."
      },
      {
        id: "MIT-AERO-229",
        source: "@Dr_Rodriguez_MIT • Verified Aerospace Professor • Cambridge, MA",
        content: "Fascinating engineering challenge with Phoenix's entry corridor. New paper analyzing hypersonic thermal dynamics during Mars EDL available on arXiv:2025.10847. Peer review pending. Models suggest Phoenix's ablative shield design offers 15% safety margin improvement over Curiosity.",
        answer: "valid",
        explanation: "VALID: Credentialed academic expert, specific technical content, peer-review transparency mentioned, arXiv preprint reference (verifiable), measured claims with percentage specifics. Scholarly communication standard."
      },
      {
        id: "VIRAL-SPACE-334",
        source: "@CosmicTruths88 • Unverified Account • Anonymous",
        content: "You WON'T BELIEVE what Phoenix cameras captured near Mars!! 😱 Structures that NASA is HIDING from public! Ancient alien technology confirmed! Click for SHOCKING images they don't want you to see! Government knows but won't tell you!!! #TruthSeekers #WakeUp",
        answer: "corrupted",
        explanation: "CORRUPTED: Pure clickbait structure, multiple exclamation marks, vague sensational claims, 'they don't want you to know' conspiracy framing, no specific evidence, manipulation tactics, unverified anonymous source."
      },
      {
        id: "SPACEX-COORD-203",
        source: "@SpaceX_Tracking • Verified SpaceX Operations • Hawthorne, CA",
        content: "Starlink constellation providing comm relay support for RSV-Phoenix during trans-Mars coast phase. Network handoff to NASA DSN for Mars orbit insertion sequence. Anticipate brief signal dropout during atmospheric entry (expected ~7min blackout per mission profile).",
        answer: "valid",
        explanation: "VALID: Verified SpaceX source, explains technical coordination role, realistic details (7min blackout is standard for Mars entry), professional cooperation between private and government space entities."
      }
    ];

    let currentIndex = 0;
    let correctCount = 0;
    let hasAnswered = false;

    const updateMeters = () => {
      const progress = (currentIndex / 5) * 100;
      const accuracy = currentIndex > 0 ? Math.round((correctCount / currentIndex) * 100) : 0;
      
      ['intro', 'mission'].forEach(prefix => {
        const progressBar = document.getElementById(`${prefix}-progress-bar`);
        const progressText = document.getElementById(`${prefix}-progress`);
        const accuracyBar = document.getElementById(`${prefix}-accuracy-bar`);
        const accuracyText = document.getElementById(`${prefix}-accuracy`);
        
        if (progressBar) progressBar.style.width = `${progress}%`;
        if (progressText) progressText.textContent = `${currentIndex}/5`;
        if (accuracyBar) accuracyBar.style.width = `${accuracy}%`;
        if (accuracyText) accuracyText.textContent = `${accuracy}%`;
      });
    };

    const showSignal = () => {
      if (currentIndex >= signals.length) {
        showResults();
        return;
      }

      const signal = signals[currentIndex];
      hasAnswered = false;

      document.getElementById('signal-id').textContent = signal.id;
      document.getElementById('signal-count').textContent = `Signal ${currentIndex + 1}/5`;
      document.getElementById('signal-source').textContent = signal.source;
      document.getElementById('signal-content').textContent = signal.content;
      
      const signalDot = document.getElementById('signal-dot');
      signalDot.style.background = signal.answer === 'valid' ? 'var(--signal-good)' : 'var(--signal-bad)';
      
      document.getElementById('feedback').classList.add('hidden');
      document.getElementById('next-container').classList.add('hidden');
      
      document.getElementById('btn-valid').disabled = false;
      document.getElementById('btn-corrupted').disabled = false;
      document.getElementById('btn-valid').classList.remove('correct', 'incorrect');
      document.getElementById('btn-corrupted').classList.remove('correct', 'incorrect');
    };

    const handleAnswer = (userAnswer) => {
      if (hasAnswered) return;
      hasAnswered = true;

      const signal = signals[currentIndex];
      const correct = userAnswer === signal.answer;
      const feedback = document.getElementById('feedback');
      
      document.getElementById('btn-valid').disabled = true;
      document.getElementById('btn-corrupted').disabled = true;

      if (correct) {
        correctCount++;
        feedback.className = 'feedback-panel correct';
        feedback.innerHTML = `<div class="feedback-title">✅ CORRECT DIAGNOSIS</div><p>${signal.explanation}</p>`;
        
        if (userAnswer === 'valid') {
          document.getElementById('btn-valid').classList.add('correct');
        } else {
          document.getElementById('btn-corrupted').classList.add('correct');
        }
      } else {
        feedback.className = 'feedback-panel incorrect';
        feedback.innerHTML = `<div class="feedback-title">❌ INCORRECT DIAGNOSIS</div><p>This was ${signal.answer.toUpperCase()}. ${signal.explanation}</p>`;
        
        if (userAnswer === 'valid') {
          document.getElementById('btn-valid').classList.add('incorrect');
          document.getElementById('btn-corrupted').classList.add('correct');
        } else {
          document.getElementById('btn-corrupted').classList.add('incorrect');
          document.getElementById('btn-valid').classList.add('correct');
        }
      }
      
      feedback.classList.remove('hidden');
      document.getElementById('next-container').classList.remove('hidden');

      currentIndex++;
      updateMeters();
    };

    const showResults = () => {
      document.getElementById('intro-section').classList.add('hidden');
      document.getElementById('mission-section').classList.add('hidden');
      document.getElementById('results-section').classList.remove('hidden');

      const pct = Math.round((correctCount / 5) * 100);

      if (pct >= 70 && window.markCurrentModuleComplete) {
        window.markCurrentModuleComplete();
      }

      document.getElementById('final-score').textContent = `${correctCount} / 5 Correct`;
      document.getElementById('final-accuracy').textContent = `${pct}%`;
      document.getElementById('final-accuracy-bar').style.width = `${pct}%`;

      const verdict = document.getElementById('verdict');
      const returnBtn = document.getElementById('return-mission-btn');
      
      if (pct >= 90) {
        verdict.style.background = 'rgba(16,185,129,0.15)';
        verdict.style.borderColor = 'var(--success)';
        verdict.innerHTML = '🛡️ <strong>ELITE TECHNICIAN</strong><br>Outstanding performance! All critical systems restored. The RSV-Phoenix navigation is secure and mission-ready.';
        returnBtn.classList.remove('hidden');
      } else if (pct >= 70) {
        verdict.style.background = 'rgba(251,191,36,0.15)';
        verdict.style.borderColor = 'var(--warning)';
        verdict.innerHTML = '⚡ <strong>PROFICIENT OPERATOR</strong><br>Good diagnostic work! Most threats neutralized. Review the missed signals to achieve expert certification.';
        returnBtn.classList.remove('hidden');
      } else {
        verdict.style.background = 'rgba(239,68,68,0.15)';
        verdict.style.borderColor = 'var(--danger)';
        verdict.innerHTML = '🔧 <strong>ADDITIONAL TRAINING REQUIRED</strong><br>System vulnerability remains high. Study the signal patterns and re-attempt diagnostic sequence for mission clearance.';
        returnBtn.classList.add('hidden');
      }
    };

    // Event listeners
    document.getElementById('start-btn').addEventListener('click', () => {
      document.getElementById('intro-section').classList.add('hidden');
      document.getElementById('mission-section').classList.remove('hidden');
      showSignal();
    });

    document.getElementById('test-btn').addEventListener('click', () => {
      // Auto-complete with 100% score
      currentIndex = 5;
      correctCount = 5;
      updateMeters();
      showResults();
      
      // Mark module as complete through progression system
      if (window.markCurrentModuleComplete) {
        window.markCurrentModuleComplete();
      }
    });

    document.getElementById('btn-valid').addEventListener('click', () => handleAnswer('valid'));
    document.getElementById('btn-corrupted').addEventListener('click', () => handleAnswer('corrupted'));
    document.getElementById('btn-next').addEventListener('click', showSignal);
    
    document.getElementById('return-mission-btn').addEventListener('click', () => {
      window.location.href = '/digital-famine/end';
    });

    updateMeters();
  </script>

  <script type="module">
    import { initEndModuleProgression } from '{{site.baseurl}}/assets/js/digitalFamine/endModuleProgression.js';
    
    // Initialize progression system for this module
    initEndModuleProgression();
  </script>
</body>
</html>