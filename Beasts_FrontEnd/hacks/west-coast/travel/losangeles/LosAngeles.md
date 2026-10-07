---
layout: post
title: "Los Angeles"
description: "Roadtrip through LA and learn UI while you're there!"
permalink: /west-coast/analytics/losangeles/
parent: "Analytics/Admin"
team: "Cool Collaborators"
submodule: 1
author: "Cool Collaborators"
date: 2025-10-21
microblog: true
footer: 
    home: /west-coast/travel/
    next: /west-coast/analytics/sandiego/
---
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"/>
<title>Los Angeles Roadtrip — Complete Journey</title>
<style>
{{ '@import "beasts/inline/pages/hacks-west-coast-travel-los-angeles-losangeles-1";' | scssify }}
</style>
</head>
<body>
<!-- Truck intro -->
<div class="intro-section" id="intro">
  <div class="loop-wrapper" role="img" aria-label="Driving through LA">
    <div class="mountain"></div>
    <div class="hill"></div>
    <div class="tree"></div>
    <div class="tree"></div>
    <div class="tree"></div>
    <div class="rock"></div>
    <div class="truck"></div>
    <div class="wheels"></div>
  </div>
  <p>Starting our LA roadtrip adventure…</p>
</div>

<!-- Personalization Banner -->
<div id="personalizationBanner" class="personalization-banner" style="display: none;">
  <h3>🎯 Your Personalized LA Experience</h3>
  <p>Based on your itinerary preferences, here are your selected destinations:</p>
  <div class="destinations-list" id="destinationsList"></div>
</div>

<!-- SECTION 1: GRIFFITH OBSERVATORY -->
<section class="griffith-scene scene-section" id="griffith" data-destination="Griffith Observatory" style="display: none;">
  <div class="twinkle" style="top:12%;left:12%"></div>
  <div class="twinkle t2" style="left:48%"></div>
  <div class="twinkle t3" style="left:72%"></div>
  <div class="twinkle t4" style="left:22%"></div>
  <div class="comet"></div>
  <div class="comet c2"></div>
  <div class="comet c3"></div>
  <div class="planet mars"></div>
  <div class="planet jupiter"></div>
  <div class="moon"></div>

  <div class="layer skyline"></div>
  <div class="layer haze"></div>

  <div class="observatory">
    <div class="wing">
      <div class="dome small">
        <div class="shutter"></div>
        <div class="beam small"></div>
      </div>
    </div>

    <div class="colonnade">
      <div class="pillar"></div>
      <div class="pillar"></div>
      <div class="pillar"></div>
      <div class="pillar"></div>
      <div class="pillar"></div>
      <div class="pillar"></div>
      <div class="pillar"></div>
      <div class="dome">
        <div class="shutter"></div>
        <div class="beam"></div>
      </div>
      <div class="roof-light"></div>
    </div>

    <div class="wing">
      <div class="dome small">
        <div class="shutter"></div>
        <div class="beam small"></div>
      </div>
    </div>
  </div>

  <div class="palms">
    <div class="palm"></div>
    <div class="palm"></div>
    <div class="palm"></div>
    <div class="palm"></div>
  </div>

  <div class="caption">🔭 Griffith Observatory — comets, planets & moonlit LA</div>
</section>

<!-- GRIFFITH LESSON -->
<div class="lesson-content lesson-section" data-destination="Griffith Observatory" style="display: none;">
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
          <div class="star-demo star1"></div>
          <div class="star-demo star2"></div>
          <div class="star-demo star3"></div>
          <div class="star-demo star4"></div>
          <div class="star-demo star5"></div>
          <div class="star-demo star6"></div>
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


<!-- GRIFFITH QUIZ -->
<section class="quiz-section quiz-section-item" data-destination="Griffith Observatory" style="display: none;">
  <h2>🧠 Quick Quiz: Build Your Own Button!</h2>
  <p>Fill in the blanks to complete your HTML file. If you get both right, your button will appear!</p>

  <form id="button-quiz-1">
    <label for="q1-1">
      1️⃣ Complete this code structure to add a button inside the body: <br>
      <code>&lt;body&gt;<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&lt;________&gt;Click Me!&lt;/________&gt;<br>
      &lt;/body&gt;</code>
    </label><br>
    <input type="text" id="q1-1" placeholder="Type your answer here"><br><br>

    <label for="q1-2">
      2️⃣ Add the missing part to make your button show an alert when clicked: <br>
      <code>&lt;button ________="alert('Hello!')"&gt;Click Me!&lt;/button&gt;</code>
    </label><br>
    <input type="text" id="q1-2" placeholder="Type your answer here"><br><br>

    <button type="button" onclick="checkAnswers1()">Check Answers</button>
  </form>

  <div id="quiz-result-1" class="quiz-result"></div>
  <div id="button-demo-1" class="button-demo"></div>
</section>

<!-- SECTION 2: HOLLYWOOD SIGN -->
<section class="hollywood-scene scene-section" id="hollywood" data-destination="Hollywood Sign" style="display: none;">
  <div class="hill-shape" style="--x:-10%"></div>
  <div class="hill-shape" style="--x:20%"></div>
  <div class="hill-shape" style="--x:55%"></div>
  <div class="sign">
    <div class="ltr">H</div>
    <div class="ltr">O</div>
    <div class="ltr">L</div>
    <div class="ltr">L</div>
    <div class="ltr">Y</div>
    <div class="ltr">W</div>
    <div class="ltr">O</div>
    <div class="ltr">O</div>
    <div class="ltr">D</div>
  </div>
  <div class="caption">⛰️ Hollywood Sign — Sunlit hills overlooking LA</div>
</section>

<!-- HOLLYWOOD LESSON -->
<div class="lesson-content lesson-section" data-destination="Hollywood Sign" style="display: none;">
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
      <div class="demo-container-hollywood">
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

<!-- HOLLYWOOD QUIZ -->
<section class="quiz-section quiz-section-item" data-destination="Hollywood Sign" style="display: none;">
  <h2>🧠 Quick Quiz: Build Your Own Button!</h2>
  <p>Fill in the blanks to complete your HTML file. If you get both right, your button will appear!</p>

  <form id="button-quiz-2">
    <label for="q2-1">
      1️⃣ Complete this code structure to add a button inside the body: <br>
      <code>&lt;body&gt;<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&lt;________&gt;Click Me!&lt;/________&gt;<br>
      &lt;/body&gt;</code>
    </label><br>
    <input type="text" id="q2-1" placeholder="Type your answer here"><br><br>

    <label for="q2-2">
      2️⃣ Add the missing part to make your button show an alert when clicked: <br>
      <code>&lt;button ________="alert('Hello!')"&gt;Click Me!&lt;/button&gt;</code>
    </label><br>
    <input type="text" id="q2-2" placeholder="Type your answer here"><br><br>

    <button type="button" onclick="checkAnswers2()">Check Answers</button>
  </form>

  <div id="quiz-result-2" class="quiz-result"></div>
  <div id="button-demo-2" class="button-demo"></div>
</section>


<!-- SECTION 3: UNIVERSAL STUDIOS -->
<section class="universal-scene scene-section" id="universal" data-destination="Universal Studios" style="display: none;">
  <div class="sun"></div>
  <div class="cloud cloud1"></div>
  <div class="cloud cloud2"></div>
  <div class="cloud cloud3"></div>

  <div class="title">
    <h1>UNIVERSAL STUDIOS</h1>
    <p>HOLLYWOOD</p>
  </div>

  <div class="mountains"></div>
  <div class="ground"></div>
  <div class="plaza"></div>

  <div class="globe-container">
    <div class="globe">
      <div class="latitude lat1"></div>
      <div class="latitude lat2"></div>
      <div class="latitude lat3"></div>
      <div class="longitude lon1"></div>
      <div class="longitude lon2"></div>
      <div class="longitude lon3"></div>
      <div class="universal-text">UNIVERSAL</div>
    </div>
    <div class="globe-ring"></div>
  </div>

  <div class="drop-tower">
    <div class="dt-base"></div>
    <div class="dt-rail left"></div>
    <div class="dt-rail right"></div>
    <div class="dt-shaft">
      <div class="dt-light l1"></div>
      <div class="dt-light l2"></div>
      <div class="dt-light l3"></div>
      <div class="dt-light l4"></div>
      <div class="dt-light l5"></div>
      <div class="dt-cable c1"></div>
      <div class="dt-cable c2"></div>
      <div class="dt-cable c3"></div>
      <div class="dt-car">
        <div class="harness"></div>
        <div class="car-window"></div>
        <div class="seat"></div>
        <div class="seat"></div>
        <div class="seat"></div>
        <div class="seat"></div>
      </div>
    </div>
  </div>

  <div class="coaster-area">
    <div class="track-support support-1"></div>
    <div class="track-support support-2"></div>
    <div class="track-support support-3"></div>
    <div class="track-support support-4"></div>
    <div class="track-support support-5"></div>
    <div class="track-support support-6"></div>
    <div class="track-support support-7"></div>
    <div class="track-curve curve-1"></div>
    <div class="track-curve curve-2"></div>
    <div class="track-curve curve-3"></div>
    <div class="track-curve curve-4"></div>
    <div class="coaster-train">
      <div class="train-windows"></div>
      <div class="train-wheels"></div>
    </div>
  </div>

  <div class="stand popcorn"><div class="stand-canopy"></div><div class="stand-counter">🍿</div></div>
  <div class="stand hotdog"><div class="stand-canopy"></div><div class="stand-counter">🌭</div></div>
  <div class="stand icecream"><div class="stand-canopy"></div><div class="stand-counter">🍦</div></div>
  <div class="stand pretzel"><div class="stand-canopy"></div><div class="stand-counter">🥨</div></div>
  <div class="stand soda"><div class="stand-canopy"></div><div class="stand-counter">🥤</div></div>

  <div class="visitor v1"><div class="visitor-head"></div><div class="visitor-body"></div><div class="visitor-legs"><div class="visitor-leg leg-l"></div><div class="visitor-leg leg-r"></div></div></div>
  <div class="visitor v2"><div class="visitor-head"></div><div class="visitor-body"></div><div class="visitor-legs"><div class="visitor-leg leg-l"></div><div class="visitor-leg leg-r"></div></div></div>
  <div class="visitor v3"><div class="visitor-head"></div><div class="visitor-body"></div><div class="visitor-legs"><div class="visitor-leg leg-l"></div><div class="visitor-leg leg-r"></div></div></div>
  <div class="visitor v4"><div class="visitor-head"></div><div class="visitor-body"></div><div class="visitor-legs"><div class="visitor-leg leg-l"></div><div class="visitor-leg leg-r"></div></div></div>
  <div class="visitor v5"><div class="visitor-head"></div><div class="visitor-body"></div><div class="visitor-legs"><div class="visitor-leg leg-l"></div><div class="visitor-leg leg-r"></div></div></div>
  <div class="visitor v6"><div class="visitor-head"></div><div class="visitor-body"></div><div class="visitor-legs"><div class="visitor-leg leg-l"></div><div class="visitor-leg leg-r"></div></div></div>
  <div class="visitor v7"><div class="visitor-head"></div><div class="visitor-body"></div><div class="visitor-legs"><div class="visitor-leg leg-l"></div><div class="visitor-leg leg-r"></div></div></div>

  <div class="marquee">
    <div class="marquee-text">
      🎬 WELCOME TO UNIVERSAL STUDIOS HOLLYWOOD • FEATURING: WIZARDING WORLD OF HARRY POTTER • JURASSIC WORLD • TRANSFORMERS • THE MUMMY • SUPER NINTENDO WORLD
    </div>
  </div>
</section>

<!-- UNIVERSAL LESSON -->
<div class="lesson-content lesson-section" data-destination="Universal Studios" style="display: none;">
  <div class="container">
    <h1>Los Angeles</h1>
    <h2>Universal Studios Button Lesson</h2>

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
      <div class="demo-container-universal">
        <div class="button-container">
          <button onclick="generateUniversal()">Click for Universal Studios</button>
        </div>

        <div id="universalContainer">
          <div class="globe-container-demo">
            <div class="globe-demo">
              <div class="universal-text-demo">UNIVERSAL</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <h2>Button Design Tips</h2>

    <h3>What is a Button?</h3>
    <p>A button triggers an action when clicked. Think of the Universal globe—bold, recognizable, and inviting. Great buttons work the same way!</p>

    <h3>The 3 Button States</h3>
    <p><strong>Default (Globe at Rest)</strong> - How it looks normally—waiting to be clicked.</p>
    <p><strong>Hover (Globe Glowing)</strong> - When you move your mouse over it—shows it's interactive.</p>
    <p><strong>Clicked (Globe Spinning)</strong> - The moment you click—confirms the action.</p>

    <h3>5 Design Tips</h3>
    
    <p><strong>1. Make it Bold</strong></p>
    <p>Like the Universal globe—easy to spot from anywhere. Use size and contrast to make your button stand out.</p>

    <p><strong>2. Use Clear Labels</strong></p>
    <p>Say "Buy Tickets" not "Click Here". Say "Enter Park" not "Submit". Be specific about what happens when clicked!</p>

    <p><strong>3. Show it's Clickable</strong></p>
    <p>Add rounded corners, shadows, and hover effects. Your button should look inviting and interactive.</p>

    <p><strong>4. Create Contrast</strong></p>
    <p>Blue globe against bright sky = maximum visibility. Make your button color pop from the background.</p>

    <p><strong>5. Size Matters</strong></p>
    <p>Big enough to tap easily on mobile. Aim for at least 44×44 pixels.</p>

    <h3>Button Types</h3>
    <p><strong>Primary:</strong> Most important action (the main entrance)</p>
    <p><strong>Secondary:</strong> Supporting actions (ride entrances)</p>
    <p><strong>Tertiary:</strong> Minor actions (information booths)</p>

    <h3>Common Mistakes</h3>
    <p>1. Vague labels like "Click" or "Submit"</p>
    <p>2. No hover effect</p>
    <p>3. Too many bold buttons competing</p>
    <p>4. Too small to tap on mobile</p>
    <p>5. Unclear what happens when clicked</p>

    <h3>Quick Tips</h3>
    <p>- Use action verbs like "Explore", "Buy", or "Enter"</p>
    <p>- Keep one primary button per section</p>
    <p>- And most importantly—make it look clickable!</p>
  </div>
</div>

<!-- UNIVERSAL QUIZ -->
<section class="quiz-section quiz-section-item" data-destination="Universal Studios" style="display: none;">
  <h2>🧠 Quick Quiz: Build Your Own Button!</h2>
  <p>Fill in the blanks to complete your HTML file. If you get both right, your button will appear!</p>

  <form id="button-quiz-3">
    <label for="q3-1">
      1️⃣ Complete this code structure to add a button inside the body: <br>
      <code>&lt;body&gt;<br>
      &nbsp;&nbsp;&nbsp;&nbsp;&lt;________&gt;Click Me!&lt;/________&gt;<br>
      &lt;/body&gt;</code>
    </label><br>
    <input type="text" id="q3-1" placeholder="Type your answer here"><br><br>

    <label for="q3-2">
      2️⃣ Add the missing part to make your button show an alert when clicked: <br>
      <code>&lt;button ________="alert('Hello!')"&gt;Click Me!&lt;/button&gt;</code>
    </label><br>
    <input type="text" id="q3-2" placeholder="Type your answer here"><br><br>

    <button type="button" onclick="checkAnswers3()">Check Answers</button>
  </form>

  <div id="quiz-result-3" class="quiz-result"></div>
  <div id="button-demo-3" class="button-demo"></div>
</section>

<!-- SECTION 4: WALK OF FAME -->
<section class="walkoffame-scene scene-section" id="walkoffame" data-destination="Hollywood Walk of Fame" style="display: none;">
  <div class="chinese-theatre">
    <div class="theatre-roof"></div>
    <div class="theatre-body">
      <div class="theatre-pillars">
        <div class="pillar-wof"></div>
        <div class="pillar-wof"></div>
        <div class="pillar-wof"></div>
      </div>
    </div>
  </div>
  <div class="capitol-records">
    <div class="capitol-top"></div>
    <div class="capitol-base">
      <div class="capitol-ring"></div>
      <div class="capitol-ring"></div>
      <div class="capitol-ring"></div>
      <div class="capitol-ring"></div>
    </div>
  </div>
  <div class="dolby-theatre">
    <div class="dolby-marquee">
      <div class="marquee-lights"></div>
    </div>
    <div class="dolby-body"></div>
  </div>
  <div class="sidewalk"></div>
  <div class="star s1"></div>
  <div class="star s2"></div>
  <div class="star s3"></div>
  <div class="star s4"></div>
  <div class="caption">⭐ Hollywood Walk of Fame — stars & landmarks</div>
</section>

<!-- WALK OF FAME LESSON -->
<div class="lesson-content lesson-section" data-destination="Hollywood Walk of Fame" style="display: none;">
  <div class="container">
    <h1>Los Angeles</h1>
    <h2>Hollywood Walk of Fame Button Lesson</h2>

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
      <div class="demo-container-walk">
        <div class="button-container">
          <button onclick="generateWalk()">Click for Walk of Fame</button>
        </div>
        <div id="walkContainer">
          <div class="buildings">
            <div class="building building1"></div>
            <div class="building building2"></div>
            <div class="building building3"></div>
            <div class="building building4"></div>
          </div>
          <div class="person person1">
            <div class="person-head"></div>
            <div class="person-body"></div>
            <div class="person-legs">
              <div class="leg"></div>
              <div class="leg"></div>
            </div>
          </div>
          <div class="person person2">
            <div class="person-head"></div>
            <div class="person-body"></div>
            <div class="person-legs">
              <div class="leg"></div>
              <div class="leg"></div>
            </div>
          </div>
          <div class="person person3">
            <div class="person-head"></div>
            <div class="person-body"></div>
            <div class="person-legs">
              <div class="leg"></div>
              <div class="leg"></div>
            </div>
          </div>
          <div class="sidewalk-demo">
            <div class="star-tile">
              <div class="star-shape">★</div>
              <div class="star-name">MARILYN<br>MONROE</div>
            </div>
            <div class="star-tile">
              <div class="star-shape">★</div>
              <div class="star-name">CHARLIE<br>CHAPLIN</div>
            </div>
            <div class="star-tile">
              <div class="star-shape">★</div>
              <div class="star-name">ELVIS<br>PRESLEY</div>
            </div>
            <div class="star-tile">
              <div class="star-shape">★</div>
              <div class="star-name">MICHAEL<br>JACKSON</div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <h2>Button Design Tips</h2>

    <h3>What is a Button?</h3>
    <p>A button triggers an action when clicked. Think of the Hollywood Walk of Fame stars—each one catches your attention and invites interaction. Good buttons work the same way.</p>

    <h3>The 3 Button States</h3>
    <p><strong>Default (Star on Sidewalk)</strong> - How it looks normally—waiting to be clicked.</p>
    <p><strong>Hover (Star Shining)</strong> - When you move your mouse over it—shows it's interactive.</p>
    <p><strong>Clicked (Camera Flash)</strong> - The moment you click—confirms the action.</p>

    <h3>5 Design Tips</h3>

    <p><strong>1. Make it Bold</strong></p>
    <p>Like the gold stars on gray concrete—easy to see. Use size and contrast.</p>

    <p><strong>2. Use Clear Labels</strong></p>
    <p>Each star has a name—your button should be clear too. "Get Tickets" not "Click Here". "See Stars" not "Submit".</p>

    <p><strong>3. Show it's Clickable</strong></p>
    <p>Stars stand out from the sidewalk. Add rounded corners or shadows. Use hover effects.</p>

    <p><strong>4. Create Contrast</strong></p>
    <p>Gold against gray—maximum visibility. Button color should pop from the background.</p>

    <p><strong>5. Size Matters</strong></p>
    <p>Big enough to see and click easily. At least 44x44px on mobile.</p>

    <h3>Button Types</h3>
    <p><strong>Primary:</strong> Most important action (the famous stars)</p>
    <p><strong>Secondary:</strong> Supporting actions (building entrances)</p>
    <p><strong>Tertiary:</strong> Minor actions (street signs)</p>

    <h3>Common Mistakes</h3>
    <p>1. Vague labels like "Click" or "Submit"</p>
    <p>2. No hover effect</p>
    <p>3. Too many bold buttons</p>
    <p>4. Too small to tap</p>
    <p>5. Unclear what happens when clicked</p>

    <h3>Quick Tips</h3>
    <p>- Use action verbs: "Explore," "Find," "Visit"</p>
    <p>- One primary button per section</p>
    <p>- Make it look clickable</p>
    <p>- Test on mobile</p>
  </div>
</div>

<!-- WALK OF FAME QUIZ -->


<script>
// Load itinerary from localStorage and show only selected destinations
(function() {
  try {
    const itineraryData = localStorage.getItem('westCoastItinerary');
    
    if (itineraryData) {
      const itinerary = JSON.parse(itineraryData);
      
      // Check if Los Angeles data exists
      if (itinerary.cities && itinerary.cities['Los Angeles']) {
        const laDestinations = itinerary.cities['Los Angeles'].destinations;
        
        // Show personalization banner
        const banner = document.getElementById('personalizationBanner');
        const destinationsList = document.getElementById('destinationsList');
        
        if (laDestinations && laDestinations.length > 0) {
          banner.style.display = 'block';
          
          // Display selected destinations in banner
          destinationsList.innerHTML = laDestinations.map(dest => 
            `<div class="destination-badge">${dest}</div>`
          ).join('');
          
          // Show only the sections for selected destinations
          const allScenes = document.querySelectorAll('.scene-section');
          const allLessons = document.querySelectorAll('.lesson-section');
          const allQuizzes = document.querySelectorAll('.quiz-section-item');
          
          // Hide all sections first
          allScenes.forEach(scene => scene.style.display = 'none');
          allLessons.forEach(lesson => lesson.style.display = 'none');
          allQuizzes.forEach(quiz => quiz.style.display = 'none');
          
          // Show only selected destinations
          laDestinations.forEach(destination => {
            // Show scene
            const scene = document.querySelector(`.scene-section[data-destination="${destination}"]`);
            if (scene) scene.style.display = 'block';
            
            // Show lesson
            const lesson = document.querySelector(`.lesson-section[data-destination="${destination}"]`);
            if (lesson) lesson.style.display = 'block';
            
            // Show quiz
            const quiz = document.querySelector(`.quiz-section-item[data-destination="${destination}"]`);
            if (quiz) quiz.style.display = 'block';
          });
        } else {
          // No destinations selected, show all
          showAllDestinations();
        }
      } else {
        // No LA data, show all
        showAllDestinations();
      }
    } else {
      // No itinerary data, show all
      showAllDestinations();
    }
  } catch (error) {
    console.error('Error loading itinerary:', error);
    // On error, show all
    showAllDestinations();
  }
})();

function showAllDestinations() {
  const allScenes = document.querySelectorAll('.scene-section');
  const allLessons = document.querySelectorAll('.lesson-section');
  const allQuizzes = document.querySelectorAll('.quiz-section-item');
  
  allScenes.forEach(scene => scene.style.display = 'block');
  allLessons.forEach(lesson => lesson.style.display = 'block');
  allQuizzes.forEach(quiz => quiz.style.display = 'block');
}

// Hide intro after 4 seconds
setTimeout(() => {
  const intro = document.getElementById('intro');
  if (intro) {
    intro.classList.add('hidden');
  }
}, 4000);

// Demo button functions
function generateObservatory() {
  const container = document.getElementById('observatoryContainer');
  container.classList.remove('show');
  setTimeout(() => {
    container.classList.add('show');
  }, 50);
}

function generateHollywoodSign() {
  const container = document.getElementById('signContainer');
  container.classList.remove('show');
  setTimeout(() => {
    container.classList.add('show');
  }, 50);
}

function generateUniversal() {
  const container = document.getElementById('universalContainer');
  container.classList.remove('show');
  setTimeout(() => {
    container.classList.add('show');
  }, 50);
}

function generateWalk() {
  const container = document.getElementById('walkContainer');
  container.classList.remove('show');
  setTimeout(() => {
    container.classList.add('show');
  }, 50);
}

// Quiz functions
function checkAnswers1() {
  const a1 = document.getElementById("q1-1").value.trim().toLowerCase();
  const a2 = document.getElementById("q1-2").value.trim().toLowerCase();
  const result = document.getElementById("quiz-result-1");
  const demo = document.getElementById("button-demo-1");
  demo.innerHTML = "";
  let score = 0;

  if (a1 === "button") score++;
  if (a2 === "onclick") score++;

  result.textContent = "✅ You got " + score + "/2 correct!";

  if (score === 2) {
    demo.innerHTML = `
      <p>🎉 Great job! Here's your working button:</p>
      <button onclick="alert('Hello!')">Click Me!</button>
    `;
  }
}

function checkAnswers2() {
  const a1 = document.getElementById("q2-1").value.trim().toLowerCase();
  const a2 = document.getElementById("q2-2").value.trim().toLowerCase();
  const result = document.getElementById("quiz-result-2");
  const demo = document.getElementById("button-demo-2");
  demo.innerHTML = "";
  let score = 0;

  if (a1 === "button") score++;
  if (a2 === "onclick") score++;

  result.textContent = "✅ You got " + score + "/2 correct!";

  if (score === 2) {
    demo.innerHTML = `
      <p>🎉 Great job! Here's your working button:</p>
      <button onclick="alert('Hello!')">Click Me!</button>
    `;
  }
}

function checkAnswers3() {
  const a1 = document.getElementById("q3-1").value.trim().toLowerCase();
  const a2 = document.getElementById("q3-2").value.trim().toLowerCase();
  const result = document.getElementById("quiz-result-3");
  const demo = document.getElementById("button-demo-3");
  demo.innerHTML = "";
  let score = 0;

  if (a1 === "button") score++;
  if (a2 === "onclick") score++;

  result.textContent = "✅ You got " + score + "/2 correct!";

  if (score === 2) {
    demo.innerHTML = `
      <p>🎉 Great job! Here's your working button:</p>
      <button onclick="alert('Hello!')">Click Me!</button>
    `;
  }
}

function checkAnswers4() {
  const a1 = document.getElementById("q4-1").value.trim().toLowerCase();
  const a2 = document.getElementById("q4-2").value.trim().toLowerCase();
  const result = document.getElementById("quiz-result-4");
  const demo = document.getElementById("button-demo-4");
  demo.innerHTML = "";
  let score = 0;

  if (a1 === "button") score++;
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