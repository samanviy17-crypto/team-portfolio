---
layout: post
title: "Seattle"
description: "Roadtrip through Seattle and learn UI while you're there!"
permalink: /west-coast/analytics/seattle/
parent: "Analytics/Admin"
team: "Cool Collaborators"
submodule: 4
author: "Cool Collaborators"
date: 2025-10-21
microblog: true
footer: 
    previous: /west-coast/analytics/sanfrancisco/
    home: /west-coast/travel/
---
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Seattle Landmarks - Progress Bar Lessons</title>
<style>
{{ '@import "beasts/inline/pages/hacks-west-coast-travel-seattle-seattle-1";' | scssify }}
</style>
</head>
<body class="loading">

<!-- Personalization Banner -->
<div id="personalizationBanner" class="personalization-banner">
  <h3>🎯 Your Personalized Seattle Experience</h3>
  <p>Based on your itinerary preferences, here are your selected destinations:</p>
  <div class="destinations-list" id="destinationsList"></div>
</div>

<div class="loading-screen" id="loadingScreen">
  <div class="loading-text">Loading Seattle Landmarks...</div>
  
  <div class="truck-container">
    <div class="truck">
      <div class="truck-cab">
        <div class="truck-windshield"></div>
      </div>
      <div class="truck-cargo">
        <div class="cargo-text">PROGRESS<br>LESSONS</div>
      </div>
      <div class="truck-wheel wheel-front"></div>
      <div class="truck-wheel wheel-back1"></div>
      <div class="truck-wheel wheel-back2"></div>
    </div>
    
    <div class="road">
      <div class="road-line"></div>
      <div class="road-line"></div>
      <div class="road-line"></div>
      <div class="road-line"></div>
      <div class="road-line"></div>
    </div>
  </div>
  
  <div class="loading-bar">
    <div class="loading-progress"></div>
  </div>
</div>

<div class="main-container">

<!-- Space Needle Section -->
<div class="landmark-section" data-destination="Space Needle">
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
  
  <div class="quiz-section">
    <h1>🎯 Progress Bar Quiz</h1>
    <p class="subtitle">Test your knowledge of progress bar design principles!</p>
    
    <div class="question" id="needle-q1">
      <div class="question-number">Question 1</div>
      <div class="question-text">
        When designing a progress bar, you should use 
        <input type="text" class="fill-blank" id="needle-answer1" placeholder="Your answer..."> 
        animations to make the bar feel professional and show that the task is actively running.
      </div>
      <p class="hint">💡 Hint: The opposite of jerky or jumpy</p>
      <div class="feedback" id="needle-feedback1"></div>
      <div class="progress-reward" id="needle-reward1">
        <h3>✅ Correct! Watch the difference:</h3>
        <p><strong>Smooth Animation:</strong></p>
        <div class="progress-bar-demo">
          <div class="progress-fill" id="needle-progress1" style="width: 0%">0%</div>
        </div>
        <p style="font-size: 0.95em; margin-top: 12px; color: #69be28;">Smooth progress feels natural and professional!</p>
      </div>
    </div>
    
    <div class="question" id="needle-q2">
      <div class="question-number">Question 2</div>
      <div class="question-text">
        A common mistake is making the progress bar too 
        <input type="text" class="fill-blank" id="needle-answer2" placeholder="Your answer..."> 
        which makes it hard for users to see and track their progress.
      </div>
      <p class="hint">💡 Hint: Not big enough</p>
      <div class="feedback" id="needle-feedback2"></div>
      <div class="progress-reward" id="needle-reward2">
        <h3>🌟 Excellent! Size matters:</h3>
        <p><strong>Processing files...</strong></p>
        <div class="progress-bar-demo">
          <div class="progress-fill" id="needle-progress2" style="width: 0%">0%</div>
        </div>
        <p style="font-size: 0.95em; margin-top: 12px; color: #69be28;">A visible progress bar keeps users informed and engaged!</p>
      </div>
    </div>
    
    <div class="completion-message" id="needle-completion">
      <h2>🏆 Quiz Complete!</h2>
      <p>You've mastered the key principles of progress bar design!</p>
      <p style="margin-top: 15px; font-size: 1.1em;">Ready to build better user experiences! 🎉</p>
    </div>
  </div>
</div>

<!-- Pike Place Market Section -->
<div class="landmark-section" data-destination="Pike Place Market">
  <div class="pike-scene">
    <div class="label">🐟 Pike Place Market</div>
    <div class="clock">
      <div class="clock-hand hour-hand"></div>
      <div class="clock-hand minute-hand"></div>
    </div>
    <div class="market-sign">
      <div class="market-sign-text">PUBLIC MARKET</div>
    </div>
    <div class="market-awning"></div>
    <div class="crate c1"></div>
    <div class="crate c2"></div>
    <div class="crate c3"></div>
    <div class="fish">
      <div class="fish-eye"></div>
      <div class="fish-tail"></div>
    </div>
    <div class="vendor v1">
      <div class="vendor-head"></div>
      <div class="vendor-body"></div>
    </div>
    <div class="vendor v2">
      <div class="vendor-head"></div>
      <div class="vendor-body"></div>
    </div>
    <div class="market-stall"></div>
  </div>
  
  <div class="content">
    <h1>Progress Bar Lesson: Pike Place Market Theme</h1>

    <h2>What is a Progress Bar?</h2>
    <p>A progress bar shows how much of a task is complete. Think of Pike Place Market—shoppers moving through vendor stalls from the fish market to the flower stands, checking items off their list. It shows where you are and how much is left.</p>

    <h2>The 3 Parts of a Progress Bar</h2>

    <h3>The Track (The Full Market)</h3>
    <p>From the famous Pike Place sign to the last vendor—represents the total task.</p>
    <ul>
      <li>Background bar showing the complete distance</li>
    </ul>

    <h3>The Fill (Stalls Visited)</h3>
    <p>Progress through the market—shows how far you've come.</p>
    <ul>
      <li>Colored bar that grows as you complete the task</li>
    </ul>

    <h3>The Label (Vendor Signs)</h3>
    <p>Clear signs at each stall—tells you exactly where you are.</p>
    <ul>
      <li>Text showing percentage or "3 of 10 items checked out"</li>
    </ul>

    <h2>5 Design Tips</h2>

    <h3>1. Make it Visible</h3>
    <p>Like the bright vendor signs—easy to see in the busy market.</p>
    <ul>
      <li>Use clear colors with good contrast</li>
      <li>Make it big enough to notice</li>
    </ul>

    <h3>2. Show Real Progress</h3>
    <p>Like crossing items off your shopping list—accurate and honest.</p>
    <ul>
      <li>Update smoothly as tasks complete</li>
      <li>Never fake progress or go backwards</li>
    </ul>

    <h3>3. Use Market Colors</h3>
    <p>Bright produce colors and fresh fish tones create energy.</p>
    <ul>
      <li>Match your brand colors</li>
      <li>Use color to show status (green = good, red = error)</li>
    </ul>

    <h3>4. Add Context</h3>
    <p>Like vendor shouts calling out specials—tell users what's happening.</p>
    <ul>
      <li>"Processing payment... 60%"</li>
      <li>"2 of 5 items added to cart"</li>
    </ul>

    <h3>5. Keep it Simple</h3>
    <p>Don't overcomplicate like a crowded Saturday morning.</p>
    <ul>
      <li>One bar, clear message</li>
      <li>Avoid fancy animations that distract</li>
    </ul>

    <h2>Common Mistakes</h2>
    <ul>
      <li>No feedback—users don't know if anything is happening</li>
      <li>Jumping progress—going from 10% to 90% instantly feels fake</li>
      <li>Stuck at 99%—like waiting in the checkout line forever</li>
      <li>Too small—like trying to read price signs from across the aisle</li>
      <li>No message—progress without context confuses users</li>
    </ul>

    <h2>Quick Example</h2>
    <div class="example-box">
      <p><strong>Good:</strong> "Adding to cart... [████████░░] 80% - Almost done!"</p>
      <p><strong>Bad:</strong> [░░░░░░░░░░] (no message, unclear progress)</p>
    </div>

    <h2>Quick Tips</h2>
    <ul>
      <li>Always show feedback when users wait</li>
      <li>Smooth animations feel more professional</li>
      <li>Add estimated time if possible: "About 30 seconds remaining"</li>
      <li>Use motion to show it's working, not frozen</li>
      <li>Celebrate completion—like finding the perfect bouquet!</li>
    </ul>
  </div>
  
  <div class="quiz-section">
    <h1>🎯 Progress Bar Quiz</h1>
    <p class="subtitle">Test your knowledge of progress bar design principles!</p>
    
    <div class="question" id="pike-q1">
      <div class="question-number">Question 1</div>
      <div class="question-text">
        When designing a progress bar, you should use 
        <input type="text" class="fill-blank" id="pike-answer1" placeholder="Your answer..."> 
        animations to make the bar feel professional and show that the task is actively running.
      </div>
      <p class="hint">💡 Hint: The opposite of jerky or jumpy</p>
      <div class="feedback" id="pike-feedback1"></div>
      <div class="progress-reward" id="pike-reward1">
        <h3>✅ Correct! Watch the difference:</h3>
        <p><strong>Smooth Animation:</strong></p>
        <div class="progress-bar-demo">
          <div class="progress-fill" id="pike-progress1" style="width: 0%">0%</div>
        </div>
        <p style="font-size: 0.95em; margin-top: 12px; color: #69be28;">Smooth progress feels natural and professional!</p>
      </div>
    </div>
    
    <div class="question" id="pike-q2">
      <div class="question-number">Question 2</div>
      <div class="question-text">
        A common mistake is making the progress bar too 
        <input type="text" class="fill-blank" id="pike-answer2" placeholder="Your answer..."> 
        which makes it hard for users to see and track their progress.
      </div>
      <p class="hint">💡 Hint: Not big enough</p>
      <div class="feedback" id="pike-feedback2"></div>
      <div class="progress-reward" id="pike-reward2">
        <h3>🌟 Excellent! Size matters:</h3>
        <p><strong>Processing files...</strong></p>
        <div class="progress-bar-demo">
          <div class="progress-fill" id="pike-progress2" style="width: 0%">0%</div>
        </div>
        <p style="font-size: 0.95em; margin-top: 12px; color: #69be28;">A visible progress bar keeps users informed and engaged!</p>
      </div>
    </div>
    
    <div class="completion-message" id="pike-completion">
      <h2>🏆 Quiz Complete!</h2>
      <p>You've mastered the key principles of progress bar design!</p>
      <p style="margin-top: 15px; font-size: 1.1em;">Ready to build better user experiences! 🎉</p>
    </div>
  </div>
</div>

<!-- Mount Rainier Section -->
<div class="landmark-section" data-destination="Mount Rainier National Park">
  <div class="rainier-scene">
    <div class="label">⛰️ Mount Rainier</div>
    
    <div class="mountain-sky">
      <div class="mountain-cloud mc1"></div>
      <div class="mountain-cloud mc2"></div>
    </div>
    
    <div class="mount-rainier">
      <div class="mountain-peak">
        <div class="snow-cap"></div>
        <div class="glacier g1"></div>
        <div class="glacier g2"></div>
      </div>
    </div>
    
    <div class="tree t1">
      <div class="tree-trunk"></div>
      <div class="tree-foliage"></div>
    </div>
    <div class="tree t2">
      <div class="tree-trunk"></div>
      <div class="tree-foliage"></div>
    </div>
    <div class="tree t3">
      <div class="tree-trunk"></div>
      <div class="tree-foliage"></div>
    </div>
    <div class="tree t4">
      <div class="tree-trunk"></div>
      <div class="tree-foliage"></div>
    </div>
    <div class="tree t5">
      <div class="tree-trunk"></div>
      <div class="tree-foliage"></div>
    </div>
    <div class="tree t6">
      <div class="tree-trunk"></div>
      <div class="tree-foliage"></div>
    </div>
    
    <div class="deer">
      <div class="deer-head">
        <div class="antler left"></div>
        <div class="antler right"></div>
      </div>
      <div class="deer-body"></div>
      <div class="deer-leg dl1"></div>
      <div class="deer-leg dl2"></div>
      <div class="deer-leg dl3"></div>
      <div class="deer-leg dl4"></div>
    </div>
    
    <div class="eagle"></div>
    
    <div class="forest-base"></div>
  </div>
  
  <div class="content">
    <h1>Progress Bar Lesson: Mount Rainier National Park Theme</h1>

    <h2>What is a Progress Bar?</h2>
    <p>A progress bar shows how much of a task is complete. Think of Mount Rainier National Park—hikers watching trail markers count up to the summit, or the elevation gain on your climb. It shows where you are and how much is left.</p>

    <h2>The 3 Parts of a Progress Bar</h2>

    <h3>The Track (The Trail)</h3>
    <p>The full trail from Paradise to the summit—represents the total task.</p>
    <ul>
      <li>Background bar showing the complete distance</li>
    </ul>

    <h3>The Fill (Miles Hiked)</h3>
    <p>Progress up the mountain—shows how far you've come.</p>
    <ul>
      <li>Colored bar that grows as you complete the task</li>
    </ul>

    <h3>The Label (Trail Marker)</h3>
    <p>Elevation signs and mile markers—tells you exactly where you are.</p>
    <ul>
      <li>Text showing percentage or "3 of 10 miles complete"</li>
    </ul>

    <h2>5 Design Tips</h2>

    <h3>1. Make it Visible</h3>
    <p>Like trail markers visible through the mist—easy to see from anywhere.</p>
    <ul>
      <li>Use clear colors with good contrast</li>
      <li>Make it big enough to notice</li>
    </ul>

    <h3>2. Show Real Progress</h3>
    <p>Like elevation markers on the trail—accurate and honest.</p>
    <ul>
      <li>Update smoothly as tasks complete</li>
      <li>Never fake progress or go backwards</li>
    </ul>

    <h3>3. Use Nature Colors</h3>
    <p>Mountain blues and forest greens create calm focus.</p>
    <ul>
      <li>Match your brand colors</li>
      <li>Use color to show status (green = good, red = error)</li>
    </ul>

    <h3>4. Add Context</h3>
    <p>Like a trail map—tell users what's happening.</p>
    <ul>
      <li>"Uploading photos... 60%"</li>
      <li>"2 of 5 forms completed"</li>
    </ul>

    <h3>5. Keep it Simple</h3>
    <p>Don't overcomplicate like confusing trail junctions.</p>
    <ul>
      <li>One bar, clear message</li>
      <li>Avoid fancy animations that distract</li>
    </ul>

    <h2>Common Mistakes</h2>
    <ul>
      <li>No feedback—users don't know if anything is happening</li>
      <li>Jumping progress—going from 10% to 90% instantly feels fake</li>
      <li>Stuck at 99%—like being 100 feet from the summit forever</li>
      <li>Too small—like trying to read a trail sign from a mile away</li>
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
      <li>Celebrate completion—like reaching the summit!</li>
    </ul>
  </div>
  
    <div class="quiz-section">
    <h1>🎯 Progress Bar Quiz</h1>
    <p class="subtitle">Test your knowledge of progress bar design principles!</p>
    
    <div class="question" id="rainier-q1">
      <div class="question-number">Question 1</div>
      <div class="question-text">
        When designing a progress bar, you should use 
        <input type="text" class="fill-blank" id="rainier-answer1" placeholder="Your answer..."> 
        animations to make the bar feel professional and show that the task is actively running.
      </div>
      <p class="hint">💡 Hint: The opposite of jerky or jumpy</p>
      <div class="feedback" id="rainier-feedback1"></div>
      <div class="progress-reward" id="rainier-reward1">
        <h3>✅ Correct! Watch the difference:</h3>
        <p><strong>Smooth Animation:</strong></p>
        <div class="progress-bar-demo">
          <div class="progress-fill" id="rainier-progress1" style="width: 0%">0%</div>
        </div>
        <p style="font-size: 0.95em; margin-top: 12px; color: #69be28;">Smooth progress feels natural and professional!</p>
      </div>
    </div>
    
    <div class="question" id="rainier-q2">
      <div class="question-number">Question 2</div>
      <div class="question-text">
        A common mistake is making the progress bar too 
        <input type="text" class="fill-blank" id="rainier-answer2" placeholder="Your answer..."> 
        which makes it hard for users to see and track their progress.
      </div>
      <p class="hint">💡 Hint: Not big enough</p>
      <div class="feedback" id="rainier-feedback2"></div>
      <div class="progress-reward" id="rainier-reward2">
        <h3>🌟 Excellent! Size matters:</h3>
        <p><strong>Processing files...</strong></p>
        <div class="progress-bar-demo">
          <div class="progress-fill" id="rainier-progress2" style="width: 0%">0%</div>
        </div>
        <p style="font-size: 0.95em; margin-top: 12px; color: #69be28;">A visible progress bar keeps users informed and engaged!</p>
      </div>
    </div>
    
    <div class="completion-message" id="rainier-completion">
      <h2>🏆 Quiz Complete!</h2>
      <p>You've mastered the key principles of progress bar design!</p>
      <p style="margin-top: 15px; font-size: 1.1em;">Ready to build better user experiences! 🎉</p>
    </div>
  </div>
</div>

<!-- Lumen Field Section -->
<div class="landmark-section" data-destination="Lumen Field">
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
  
  <div class="quiz-section">
    <h1>🎯 Progress Bar Quiz</h1>
    <p class="subtitle">Test your knowledge of progress bar design principles!</p>
    
    <div class="question" id="lumen-q1">
      <div class="question-number">Question 1</div>
      <div class="question-text">
        When designing a progress bar, you should use 
        <input type="text" class="fill-blank" id="lumen-answer1" placeholder="Your answer..."> 
        animations to make the bar feel professional and show that the task is actively running.
      </div>
      <p class="hint">💡 Hint: The opposite of jerky or jumpy</p>
      <div class="feedback" id="lumen-feedback1"></div>
      <div class="progress-reward" id="lumen-reward1">
        <h3>✅ Correct! Watch the difference:</h3>
        <p><strong>Smooth Animation:</strong></p>
        <div class="progress-bar-demo">
          <div class="progress-fill" id="lumen-progress1" style="width: 0%">0%</div>
        </div>
        <p style="font-size: 0.95em; margin-top: 12px; color: #69be28;">Smooth progress feels natural and professional!</p>
      </div>
    </div>
    
    <div class="question" id="lumen-q2">
      <div class="question-number">Question 2</div>
      <div class="question-text">
        A common mistake is making the progress bar too 
        <input type="text" class="fill-blank" id="lumen-answer2" placeholder="Your answer..."> 
        which makes it hard for users to see and track their progress.
      </div>
      <p class="hint">💡 Hint: Not big enough</p>
      <div class="feedback" id="lumen-feedback2"></div>
      <div class="progress-reward" id="lumen-reward2">
        <h3>🌟 Excellent! Size matters:</h3>
        <p><strong>Processing files...</strong></p>
        <div class="progress-bar-demo">
          <div class="progress-fill" id="lumen-progress2" style="width: 0%">0%</div>
        </div>
        <p style="font-size: 0.95em; margin-top: 12px; color: #69be28;">A visible progress bar keeps users informed and engaged!</p>
      </div>
    </div>
    
    <div class="completion-message" id="lumen-completion">
      <h2>🏆 Quiz Complete!</h2>
      <p>You've mastered the key principles of progress bar design!</p>
      <p style="margin-top: 15px; font-size: 1.1em;">Ready to build better user experiences! 🎉</p>
    </div>
  </div>
</div>

</div>

<script>
// Load itinerary from localStorage and show only selected destinations
(function() {
  try {
    const itineraryData = localStorage.getItem('westCoastItinerary');
    
    if (itineraryData) {
      const itinerary = JSON.parse(itineraryData);
      
      // Check if Seattle data exists
      if (itinerary.cities && itinerary.cities['Seattle']) {
        const seattleDestinations = itinerary.cities['Seattle'].destinations;
        
        // Show personalization banner
        const banner = document.getElementById('personalizationBanner');
        const destinationsList = document.getElementById('destinationsList');
        
        if (seattleDestinations && seattleDestinations.length > 0) {
          banner.style.display = 'block';
          
          // Display selected destinations in banner
          destinationsList.innerHTML = seattleDestinations.map(dest => 
            `<div class="destination-badge">${dest}</div>`
          ).join('');
          
          // Show only the sections for selected destinations
          const allSections = document.querySelectorAll('.landmark-section');
          
          // Hide all sections first
          allSections.forEach(section => section.style.display = 'none');
          
          // Show only selected destinations
          seattleDestinations.forEach(destination => {
            const section = document.querySelector(`.landmark-section[data-destination="${destination}"]`);
            if (section) {
              section.style.display = 'block';
              
              // Also show the lesson and quiz content within this section
              const lesson = section.querySelector('.content');
              const quiz = section.querySelector('.quiz-section');
              if (lesson) lesson.style.display = 'block';
              if (quiz) quiz.style.display = 'block';
            }
          });
        } else {
          // No destinations selected, show all
          showAllDestinations();
        }
      } else {
        // No Seattle data, show all
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
  const allSections = document.querySelectorAll('.landmark-section');
  allSections.forEach(section => {
    section.style.display = 'block';
    const lesson = section.querySelector('.content');
    const quiz = section.querySelector('.quiz-section');
    if (lesson) lesson.style.display = 'block';
    if (quiz) quiz.style.display = 'block';
  });
}

// Loading screen
window.addEventListener('load', function() {
  setTimeout(() => {
    const loadingScreen = document.getElementById('loadingScreen');
    loadingScreen.classList.add('hidden');
    document.body.classList.remove('loading');
  }, 2000);
});

const answers = {
  q1: ['smooth', 'fluid', 'seamless'],
  q2: ['small', 'tiny', 'little']
};

const landmarks = ['needle', 'pike', 'rainier', 'lumen'];
const correctCounts = {};

landmarks.forEach(landmark => {
  correctCounts[landmark] = 0;
});

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

function checkAnswer(landmark, questionNum) {
  const input = document.getElementById(`${landmark}-answer${questionNum}`);
  const feedback = document.getElementById(`${landmark}-feedback${questionNum}`);
  const reward = document.getElementById(`${landmark}-reward${questionNum}`);
  const question = document.getElementById(`${landmark}-q${questionNum}`);
  
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
      animateProgress(`${landmark}-progress${questionNum}`, targetWidth);
    }, 300);
    
    correctCounts[landmark]++;
    
    if (correctCounts[landmark] === 2) {
      setTimeout(() => {
        document.getElementById(`${landmark}-completion`).className = 'completion-message show';
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

landmarks.forEach(landmark => {
  // Only add event listeners if the elements exist (for selected destinations)
  const answer1 = document.getElementById(`${landmark}-answer1`);
  const answer2 = document.getElementById(`${landmark}-answer2`);
  
  if (answer1) {
    answer1.addEventListener('input', () => checkAnswer(landmark, 1));
    answer1.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') checkAnswer(landmark, 1);
    });
  }
  
  if (answer2) {
    answer2.addEventListener('input', () => checkAnswer(landmark, 2));
    answer2.addEventListener('keypress', (e) => {
      if (e.key === 'Enter') checkAnswer(landmark, 2);
    });
  }
});
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