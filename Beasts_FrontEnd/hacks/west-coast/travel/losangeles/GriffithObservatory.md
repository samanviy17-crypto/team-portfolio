---
layout: post
title: "Los Angeles"
description: "Roadtrip through LA and learn UI while you're there!"
permalink: /west-coast/analytics/losangeles/GriffithO
parent: "Analytics/Admin"
team: "Cool Collaborators"
submodule: 1
author: "Cool Collaborators"
date: 2025-10-21
---

<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Griffith Observatory — Roadtrip</title>
  <style>
{{ '@import "beasts/inline/pages/hacks-west-coast-travel-losangeles-griffithobservatory-1";' | scssify }}
</style>
</head>
<body>
  <!-- Truck intro -->
  <div class="intro" id="intro" role="region" aria-label="Introduction animation">
    <div class="loop-wrapper" role="img" aria-label="Driving up to Griffith Observatory at dusk">
      <div class="mountain" aria-hidden="true"></div>
      <div class="hill" aria-hidden="true"></div>
      <div class="tree" aria-hidden="true"></div>
      <div class="tree" aria-hidden="true"></div>
      <div class="tree" aria-hidden="true"></div>
      <div class="rock" aria-hidden="true"></div>
      <div class="truck" aria-hidden="true"></div>
      <div class="wheels" aria-hidden="true"></div>
    </div>
    <p>Winding up to Griffith Observatory…</p>
  </div>

  <!-- Scene -->
  <main class="scene hidden" id="scene" role="region" aria-label="Griffith Observatory night sky scene">
    <!-- Ambient sky objects -->
    <div class="twinkle" style="top:12%;left:12%" aria-hidden="true"></div>
    <div class="twinkle t2" style="left:48%" aria-hidden="true"></div>
    <div class="tw
    inkle t3" style="left:72%" aria-hidden="true"></div>
    <div class="twinkle t4" style="left:22%" aria-hidden="true"></div>
    <div class="comet" aria-hidden="true"></div>
    <div class="comet c2" aria-hidden="true"></div>
    <div class="comet c3" aria-hidden="true"></div>
    <div class="planet mars" aria-hidden="true"></div>
    <div class="planet jupiter" aria-hidden="true"></div>
    <div class="moon" aria-hidden="true"></div>

    <!-- LA skyline layers and haze -->
    <div class="layer skyline" aria-hidden="true"></div>
    <div class="layer haze" aria-hidden="true"></div>

    <!-- Griffith Observatory complex -->
    <div class="observatory" aria-label="Griffith Observatory">
      <!-- Left wing with small dome -->
      <div class="wing" aria-hidden="true">
        <div class="dome small" aria-hidden="true">
          <div class="shutter" aria-hidden="true"></div>
          <div class="beam small" aria-hidden="true"></div>
        </div>
      </div>

      <!-- Central colonnade with main dome and beam -->
      <div class="colonnade" aria-label="Central building with colonnade">
        <div class="pillar" aria-hidden="true"></div>
        <div class="pillar" aria-hidden="true"></div>
        <div class="pillar" aria-hidden="true"></div>
        <div class="pillar" aria-hidden="true"></div>
        <div class="pillar" aria-hidden="true"></div>
        <div class="pillar" aria-hidden="true"></div>
        <div class="pillar" aria-hidden="true"></div>
        <div class="dome" aria-label="Main dome">
          <div class="shutter" aria-hidden="true"></div>
          <div class="beam" aria-hidden="true"></div>
        </div>
        <div class="roof-light" aria-hidden="true"></div>
      </div>

      <!-- Right wing with small dome -->
      <div class="wing" aria-hidden="true">
        <div class="dome small" aria-hidden="true">
          <div class="shutter" aria-hidden="true"></div>
          <div class="beam small" aria-hidden="true"></div>
        </div>
      </div>
    </div>

    <!-- Foreground palms -->
    <div class="palms" aria-hidden="true">
      <div class="palm"></div>
      <div class="palm"></div>
      <div class="palm"></div>
      <div class="palm"></div>
    </div>

    <div class="caption">🔭 Griffith Observatory — comets, planets & moonlit LA</div>
  </main>

  <!-- Lesson Content -->
  <div class="lesson-content hidden" id="lessonContent">
    <div class="container">
        <h1>Los Angeles</h1>
        <h2>Griffith Observatory Button Lesson</h2>

        <h3>Step 1: Set Up Your HTML File</h3>
        <p>First, create a new file and save it as button.html. Every HTML file needs this basic structure:</p>
        <pre><code>&lt;!DOCTYPE html&gt;
&lt;html&gt;
&lt;head&gt;
    &lt;title&gt;My Button&lt;/title&gt;
&lt;/head&gt;
&lt;body&gt;

&lt;/body&gt;
&lt;/html&gt;</code></pre>

        <p>What this means:</p>
        <p>&lt;!DOCTYPE html&gt; tells the browser this is an HTML file</p>
        <p>&lt;html&gt; wraps everything</p>
        <p>&lt;head&gt; contains information about the page</p>
        <p>&lt;body&gt; is where your visible content goes</p>

        <h3>Step 2: Create Your First Button</h3>
        <p>Inside the &lt;body&gt; tags, add a button:</p>
        <pre><code>&lt;body&gt;
    &lt;button&gt;Click Me!&lt;/button&gt;
&lt;/body&gt;</code></pre>

        <h3>Step 3: Make the Button Do Something</h3>
        <p>Add an onclick attribute to make something happen when clicked:</p>
        <pre><code>&lt;button onclick="alert('Hello!')"&gt;Click Me!&lt;/button&gt;</code></pre>

        <div class="example-section">
            <h3>Here's an example button!</h3>
            <div class="demo-container">
                <div class="stars">
                    <div class="star star1"></div>
                    <div class="star star2"></div>
                    <div class="star star3"></div>
                    <div class="star star4"></div>
                    <div class="star star5"></div>
                    <div class="star star6"></div>
                </div>

                <div class="button-container">
                    <button onclick="generateObservatory()">Click for Griffith Observatory</button>
                </div>

                <div id="observatoryContainer">
                    <div class="observatory-demo">
                        <div class="building-demo">
                            <div class="window window1"></div>
                            <div class="window window2"></div>
                            <div class="window window3"></div>
                            <div class="window window4"></div>
                        </div>
                        <div class="dome-demo">
                            <div class="telescope"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <h2>Button Design Tips</h2>

        <h3>What is a Button?</h3>
        <p>A button triggers an action when clicked. Think of Griffith Observatory's telescope controls—clear, responsive, and purposeful. Good buttons work the same way.</p>

        <h3>The 3 Button States</h3>
        <p><strong>Default (Observatory at Rest)</strong> - How it looks normally—waiting to be clicked.</p>
        <p><strong>Hover (Dome Opening)</strong> - When you move your mouse over it—shows it's interactive.</p>
        <p><strong>Clicked (Telescope Activates)</strong> - The moment you click—confirms the action.</p>

        <h3>5 Design Tips</h3>
        
        <p><strong>1. Make it Bold</strong></p>
        <p>Like the iconic dome on Mount Hollywood—easy to see. Use size and contrast.</p>

        <p><strong>2. Use Clear Labels</strong></p>
        <p>"View Stars" is obvious—your button should be too. "Buy Now" not "Click Here". "Sign Up" not "Submit".</p>

        <p><strong>3. Show it's Clickable</strong></p>
        <p>The dome looks different from the building. Add rounded corners or shadows. Use hover effects.</p>

        <p><strong>4. Create Contrast</strong></p>
        <p>White dome against dark sky—maximum visibility. Button color should pop from the background.</p>

        <p><strong>5. Size Matters</strong></p>
        <p>Big enough to see and click easily. At least 44x44px on mobile.</p>

        <h3>Button Types</h3>
        <p><strong>Primary:</strong> Most important action (the main telescope)</p>
        <p><strong>Secondary:</strong> Supporting actions (smaller domes)</p>
        <p><strong>Tertiary:</strong> Minor actions (information plaques)</p>

        <h3>Common Mistakes</h3>
        <p>1. Vague labels like "Click" or "Submit"</p>
        <p>2. No hover effect</p>
        <p>3. Too many bold buttons</p>
        <p>4. Too small to tap</p>
        <p>5. Unclear what happens when clicked</p>

        <h3>Quick Tips</h3>
        <p>- Use action verbs: "Explore," "Discover," "View"</p>
        <p>- One primary button per section</p>
        <p>- Make it look clickable</p>
        <p>- Test on mobile</p>
    </div>
  </div>
  
<section class="quiz-section">
  <h2>🧠 Quick Quiz: Build Your Own Button!</h2>
  <p>Fill in the blanks to complete your HTML file. If you get both right, your button will appear!</p>

  <form id="button-quiz">
    <!-- Question 1 -->
    <label for="q1">
      1️⃣ Every HTML file starts with this declaration: <br>
      <code>&lt;!________ html&gt;</code>
    </label><br>
    <input type="text" id="q1" placeholder="Type your answer here"><br><br>

    <!-- Question 2 -->
    <label for="q2">
      2️⃣ Add the missing part to make your button show an alert when clicked: <br>
      <code>&lt;button ________="alert('Hello!')"&gt;Click Me!&lt;/button&gt;</code>
    </label><br>
    <input type="text" id="q2" placeholder="Type your answer here"><br><br>

    <button type="button" onclick="checkAnswers()">Check Answers</button>
  </form>

  <div id="quiz-result"></div>
  <div id="button-demo"></div>

  <script>
    function checkAnswers() {
      const a1 = document.getElementById("q1").value.trim().toLowerCase();
      const a2 = document.getElementById("q2").value.trim().toLowerCase();
      const result = document.getElementById("quiz-result");
      const demo = document.getElementById("button-demo");
      demo.innerHTML = "";
      let score = 0;

      if (a1 === "doctype") score++;
      if (a2 === "onclick") score++;

      result.textContent = "✅ You got " + score + "/2 correct!";

      if (score === 2) {
        demo.innerHTML = `
          <p>🎉 Great job! Here's your working button:</p>
          <button onclick="alert('Hello!')">Click Me!</button>
        `;
      }
    }
  </script>
</section>

  <script>
    // Constants
    const INTRO_DURATION = 4000;
    const INTRO_FAILSAFE = 6000;

    // Transition from intro to main scene
    const transitionToScene = () => {
      const introEl = document.getElementById('intro');
      const sceneEl = document.getElementById('scene');
      const lessonEl = document.getElementById('lessonContent');
      if (!introEl || !sceneEl) return;

      introEl.classList.add('hidden');
      sceneEl.classList.remove('hidden');
      document.body.style.background = 'linear-gradient(var(--night-gradient-start), var(--night-gradient-end))';

      if (introEl.parentNode) {
        introEl.parentNode.removeChild(introEl);
      }

      // Show lesson content after scene loads
      setTimeout(() => {
        if (lessonEl) {
          lessonEl.classList.remove('hidden');
        }
      }, 2000);
    };

    const scheduleTransition = () => {
      setTimeout(transitionToScene, INTRO_DURATION);
      setTimeout(transitionToScene, INTRO_FAILSAFE);
    };

    if (document.readyState === 'complete' || document.readyState === 'interactive') {
      scheduleTransition();
    } else {
      document.addEventListener('DOMContentLoaded', scheduleTransition, { once: true });
    }

    window.addEventListener('load', () => {
      scheduleTransition();
      document.body.style.overflowY = 'auto';
    }, { once: true });

    // Button demo function
    function generateObservatory() {
        var observatoryContainer = document.getElementById('observatoryContainer');
        observatoryContainer.classList.remove('show');
        setTimeout(function() {
            observatoryContainer.classList.add('show');
        }, 50);
    }
  </script>
</body>
</html>