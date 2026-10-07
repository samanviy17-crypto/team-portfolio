---
layout: post
title: "Los Angeles"
description: "Roadtrip through LA and learn UI while you're there!"
permalink: /west-coast/analytics/losangeles/HollywoodS
parent: "Analytics/Admin"
team: "Cool Collaborators"
submodule: 1
author: "Cool Collaborators"
date: 2025-10-21
---
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Hollywood Sign — Roadtrip</title>
<style>
{{ '@import "beasts/inline/pages/hacks-west-coast-travel-losangeles-hollywood-sign-1";' | scssify }}
</style>
</head>
<body>
<!-- Truck intro -->
<div class="intro" id="intro">
<div class="loop-wrapper" role="img" aria-label="Driving through teal hills toward Hollywood">
<div class="mountain"></div>
<div class="hill"></div>
<div class="tree"></div><div class="tree"></div><div class="tree"></div>
<div class="rock"></div>
<div class="truck"></div>
<div class="wheels"></div>
</div>
<p>Cruising up to the Hollywood Hills…</p>
</div>
<!-- Scene -->
<main class="scene hidden" id="scene">
<div class="hill-shape" style="--x:-10%"></div>
<div class="hill-shape" style="--x:20%"></div>
<div class="hill-shape" style="--x:55%"></div>
<div class="sign" aria-label="HOLLYWOOD sign">
<div class="ltr">H</div><div class="ltr">O</div><div class="ltr">L</div><div class="ltr">L</div>
<div class="ltr">Y</div><div class="ltr">W</div><div class="ltr">O</div><div class="ltr">O</div><div class="ltr">D</div>
</div>
<div class="caption">⛰️ Hollywood Sign — Sunlit hills overlooking LA</div>
</main>
<!-- Lesson Content -->
<div class="lesson-content hidden" id="lessonContent">
<div class="container">
<h1>Los Angeles</h1>
<h2>Hollywood Sign Button Lesson</h2>
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
                <div class="hillside">
                    <div class="hill-demo hill1"></div>
                    <div class="hill-demo hill2"></div>
                    <div class="hill-demo hill3"></div>
                </div>
                <div class="button-container">
                    <button onclick="generateHollywoodSign()">Click for Hollywood Sign</button>
                </div>
                <div id="signContainer">
                    <div class="hollywood-sign">
                        <div class="letter">H</div>
                        <div class="letter">O</div>
                        <div class="letter">L</div>
                        <div class="letter">L</div>
                        <div class="letter">Y</div>
                        <div class="letter">W</div>
                        <div class="letter">O</div>
                        <div class="letter">O</div>
                        <div class="letter">D</div>
                    </div>
                </div>
            </div>
        </div>
        <h2>Button Design Tips</h2>
        <h3>What is a Button?</h3>
        <p>A button triggers an action when clicked. Think of the Hollywood Sign—bold, impossible to miss, and tells you exactly what it is. Good buttons work the same way.</p>
        <h3>The 3 Button States</h3>
        <p><strong>Default (Sign at Dawn)</strong> - How it looks normally—waiting to be clicked.</p>
        <p><strong>Hover (Spotlights On)</strong> - When you move your mouse over it—shows it's interactive.</p>
        <p><strong>Clicked (Lights Flash)</strong> - The moment you click—confirms the action.</p>
        <h3>5 Design Tips</h3>
        <p><strong>1. Make it Bold</strong></p>
        <p>Like 45-foot tall letters—easy to see. Use size and contrast.</p>
        <p><strong>2. Use Clear Labels</strong></p>
        <p>"HOLLYWOOD" is obvious—your button should be too. "Buy Now" not "Click Here". "Sign Up" not "Submit".</p>
        <p><strong>3. Show it's Clickable</strong></p>
        <p>The sign looks different from the hills. Add rounded corners or shadows. Use hover effects.</p>
        <p><strong>4. Create Contrast</strong></p>
        <p>White letters on brown hillside—maximum visibility. Button color should pop from the background.</p>
        <p><strong>5. Size Matters</strong></p>
        <p>Big enough to see and click easily. At least 44x44px on mobile.</p>
        <h3>Button Types</h3>
        <p><strong>Primary:</strong> Most important action (the main sign)</p>
        <p><strong>Secondary:</strong> Supporting actions (smaller signs)</p>
        <p><strong>Tertiary:</strong> Minor actions (trail markers)</p>
        <h3>Common Mistakes</h3>
        <p>1. Vague labels like "Click" or "Submit"</p>
        <p>2. No hover effect</p>
        <p>3. Too many bold buttons</p>
        <p>4. Too small to tap</p>
        <p>5. Unclear what happens when clicked</p>
        <h3>Quick Tips</h3>
        <p>- Use action verbs: "Download," "Shop," "Join"</p>
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
</section>
<script>
setTimeout(()=>{
document.getElementById('intro').classList.add('hidden');
document.getElementById('scene').classList.remove('hidden');
document.body.style.background = 'linear-gradient(#8fd0ff,#eaf6ff)';
// Show lesson content after another delay
setTimeout(()=>{
document.getElementById('lessonContent').classList.remove('hidden');
  }, 2000);
}, 8000);
function generateHollywoodSign() {
var signContainer = document.getElementById('signContainer');
signContainer.classList.remove('show');
setTimeout(function() {
signContainer.classList.add('show');
    }, 50);
}
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
</body>
</html>