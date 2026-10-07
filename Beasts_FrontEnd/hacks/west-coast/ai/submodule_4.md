--- 
layout: post
title: "Submodule 4"
description: "Submodule 4 of AI Usage Mini-Quest of Generating the Itinerary"
permalink: /west-coast/ai/submodule_4/
parent: "AI Usage"
team: "TheSprinters"
microblog: True
submodule: 4
categories: [CSP, Submodule, AIUsage]
tags: [ai, submodule, Generation]
author: "TheSprinters"
date: 2025-10-21
footer:
  previous: /west-coast/ai/submodule_3/
  home: /west-coast/ai/
---
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>West Coast Trip Planner</title>
  <style>
{{ '@import "beasts/inline/pages/hacks-west-coast-ai-submodule-4-1";' | scssify }}
</style>
</head>
<body>
  <div class="container">
    <h1>🌴 West Coast Trip Planner</h1>
    <p class="subtitle">Plan your dream vacation step by step!</p>

    <div class="progress-container">
      <div class="progress-bar" id="progressBar"></div>
    </div>

    <div class="steps">
      <div class="step-dot" id="dot1" aria-current="step">1</div>
      <div class="step-dot" id="dot2">2</div>
      <div class="step-dot" id="dot3">3</div>
      <div class="step-dot" id="dot4">4</div>
    </div>

    <!-- Step 1: Transportation -->
    <section class="card step active" id="step1">
      <h2>Step 1: Choose Your Transportation</h2>
      <p class="step-description">How do you want to travel between destinations?</p>

      <div class="grid">
        <button class="selectable" data-transport="Drive">
          <div class="icon">🚗</div>
          <div class="title">Drive</div>
          <div class="hint">Flexible, scenic routes</div>
        </button>
        <button class="selectable" data-transport="Fly">
          <div class="icon">✈️</div>
          <div class="title">Fly</div>
          <div class="hint">Fast, convenient</div>
        </button>
        <button class="selectable" data-transport="Train">
          <div class="icon">🚂</div>
          <div class="title">Take the Train</div>
          <div class="hint">Relaxing, scenic</div>
        </button>
        <button class="selectable" data-transport="Bus">
          <div class="icon">🚌</div>
          <div class="title">Take the Bus</div>
          <div class="hint">Budget-friendly</div>
        </button>
      </div>

      <div class="buttons">
        <button class="btn primary" id="nextFromTransport" disabled>Next Step</button>
      </div>
    </section>

    <!-- Step 2: Accommodations -->
    <section class="card step" id="step2">
      <h2>Step 2: Choose Your Accommodations</h2>
      <p class="step-description">Where will you stay during your trip?</p>

      <div class="grid">
        <button class="selectable" data-accommodation="Hotel">
          <div class="icon">🏨</div>
          <div class="title">Hotel</div>
          <div class="hint">Comfortable, amenities</div>
        </button>
        <button class="selectable" data-accommodation="Hostel">
          <div class="icon">🛏️</div>
          <div class="title">Hostel</div>
          <div class="hint">Budget-friendly, social</div>
        </button>
        <button class="selectable" data-accommodation="Airbnb">
          <div class="icon">🏠</div>
          <div class="title">Airbnb</div>
          <div class="hint">Home away from home</div>
        </button>
        <button class="selectable" data-accommodation="Camping">
          <div class="icon">⛺</div>
          <div class="title">Camping</div>
          <div class="hint">Adventure, nature</div>
        </button>
      </div>

      <div class="buttons">
        <button class="btn secondary" id="backFromAccommodation">Back</button>
        <button class="btn primary" id="nextFromAccommodation" disabled>Generate Itinerary</button>
      </div>
    </section>

    <!-- Step 3: Generated Itinerary -->
    <section class="card step" id="step3">
      <h2>Step 3: Your Custom Itinerary</h2>
      <p class="step-description">Here's your AI-generated West Coast trip plan!</p>

      <div id="itineraryPreview" class="itinerary"></div>

      <div class="card quiz-section">
        <h3>🎯 Test Your Knowledge!</h3>
        <div id="quizContainer"></div>
      </div>

      <div class="card" style="margin-top:16px">
        <h3>💡 Trip Planning Notes</h3>
        <textarea id="tripNotes" placeholder="Jot down ideas for your trip..."></textarea>
        <div class="buttons">
          <button class="btn secondary" id="exportBtn">⬇️ Export</button>
          <button class="btn secondary" id="shareBtn">🔗 Share</button>
        </div>
      </div>

      <div class="buttons">
        <button class="btn secondary" id="backFromItinerary">Back</button>
        <button class="btn primary" id="nextFromItinerary">Continue</button>
      </div>
    </section>

    <!-- Step 4: Share & Reflect -->
    <section class="card step" id="step4">
      <h2>Step 4: Share Your Itinerary</h2>
      <p class="step-description">Reflect on your trip plan!</p>

      <div class="card">
        <h3>🌟 Your Trip Summary</h3>
        <div id="finalSummary"></div>
      </div>

      <div class="card">
        <h3>✍️ Reflection</h3>
        <textarea id="reflection" placeholder="What are you most excited about?"></textarea>
      </div>

      <div class="buttons">
        <button class="btn secondary" id="backFromShare">Back</button>
        <button class="btn primary" id="restartBtn">Plan Another Trip 🎉</button>
      </div>
    </section>
  </div>

  <script>
    // Data structures
    const CITY_DATA = {
      'San Diego': {
        destinations: ['Petco Park', 'San Diego Zoo', 'Balboa Park', 'La Jolla'],
        foods: ['Fish Tacos (Baja-style)', 'California Burrito', 'Carne Asada Fries', 'Acai Bowls', 'Baja Bowl', 'Baja Seafood'],
        sports: [
          { name: 'Baseball - Padres', venue: 'Petco Park' },
          { name: 'Soccer - SDFC', venue: 'Snapdragon Stadium' },
          { name: 'AHL Hockey - Gulls', venue: 'Pechanga Arena' },
          { name: 'Basketball - Aztecs', venue: 'Viejas Arena' },
          { name: 'Football - USD', venue: 'Torero Stadium' }
        ]
      },
      'Los Angeles': {
        destinations: ['Hollywood Sign', 'Hollywood Walk of Fame', 'Griffith Observatory', 'Universal Studios'],
        foods: ['Korean BBQ', 'Street Tacos (al pastor)', 'In-N-Out Burger', 'Avocado Toast', 'Ramen & Fusion Dishes', 'Erewhon'],
        sports: [
          { name: 'Basketball - Clippers', venue: 'Intuit Dome' },
          { name: 'Football - Chargers', venue: 'SoFi Stadium' },
          { name: 'Football - USC', venue: 'LA Memorial Coliseum' },
          { name: 'Baseball - Dodgers', venue: 'Dodger Stadium' },
          { name: 'Soccer - LA Galaxy', venue: 'Dignity Health Sports Park' }
        ]
      },
      'San Francisco': {
        destinations: ['Golden Gate Bridge', 'Alcatraz', 'Palace of Fine Arts', 'The Painted Ladies'],
        foods: ['Clam Chowder in Sourdough Bread Bowl', 'Mission Burrito', 'Dungeness Crab', 'Ghirardelli Chocolate', 'Cioppino', 'Gourmet Dishes'],
        sports: [
          { name: 'Football - 49ers', venue: "Levi's Stadium" },
          { name: 'Basketball - Warriors', venue: 'Chase Center' },
          { name: 'Baseball - Giants', venue: 'Oracle Park' },
          { name: 'Ice Hockey - Sharks', venue: 'SAP Center' },
          { name: "Baseball - A's", venue: 'Oakland Coliseum' }
        ]
      },
      'Seattle': {
        destinations: ['Space Needle', 'Pike Place Market', 'Lumen Field', 'Mount Rainier National Park'],
        foods: ['Fresh Salmon', 'Pike Place Market Chowder', 'Dungeness Crab', 'Coffee Culture', 'Oysters & Shellfish', 'Clam Chowder in Sourdough Bread Bowl'],
        sports: [
          { name: 'Football - Seahawks', venue: 'Lumen Field' },
          { name: 'Baseball - Mariners', venue: 'T-Mobile Park' },
          { name: 'Ice Hockey - Kraken', venue: 'Climate Pledge Arena' },
          { name: 'College Football - Huskies', venue: 'Husky Stadium' },
          { name: 'Cricket - Orcas', venue: 'Marymoor Park' }
        ]
      }
    };

    const QUIZ_QUESTIONS = [
      {
        question: "Which city is home to the Golden Gate Bridge?",
        options: ["San Diego", "Los Angeles", "San Francisco", "Seattle"],
        correct: 2,
        explanation: "The iconic Golden Gate Bridge is located in San Francisco!"
      },
      {
        question: "What stadium do the Seattle Seahawks play at?",
        options: ["Lumen Field", "SoFi Stadium", "Petco Park", "Chase Center"],
        correct: 0,
        explanation: "The Seahawks play at Lumen Field, also known for its loud fans!"
      },
      {
        question: "Which food is San Diego most famous for?",
        options: ["Clam Chowder", "Korean BBQ", "Fish Tacos", "Fresh Salmon"],
        correct: 2,
        explanation: "San Diego is renowned for its Baja-style Fish Tacos!"
      },
      {
        question: "Where would you find the Hollywood Sign?",
        options: ["San Francisco", "Seattle", "San Diego", "Los Angeles"],
        correct: 3,
        explanation: "The Hollywood Sign overlooks Los Angeles from the Hollywood Hills!"
      },
      {
        question: "Which city has Pike Place Market?",
        options: ["Seattle", "Portland", "San Francisco", "Los Angeles"],
        correct: 0,
        explanation: "Pike Place Market is Seattle's famous public market!"
      }
    ];

    // State
    const STEPS = 4;
    let currentStep = 1;
    const selectedDestinations = ['San Francisco', 'Los Angeles', 'San Diego', 'Seattle'];
    let selectedTransport = '';
    let selectedAccommodation = '';
    let generatedItinerary = null;

    // DOM helpers
    const $ = (sel) => document.querySelector(sel);
    const $$ = (sel) => Array.from(document.querySelectorAll(sel));

    function updateProgress() {
      const progress = ((currentStep - 1) / (STEPS - 1)) * 100;
      $('#progressBar').style.width = progress + '%';
      for (let i = 1; i <= STEPS; i++) {
        const dot = $('#dot' + i);
        dot.removeAttribute('aria-current');
        dot.classList.toggle('completed', i < currentStep);
      }
      $('#dot' + currentStep).setAttribute('aria-current', 'step');
    }

    function stepTo(next) {
      $('#step' + currentStep).classList.remove('active');
      currentStep = next;
      $('#step' + currentStep).classList.add('active');
      updateProgress();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Step 1: Transport
    const transportButtons = $$('[data-transport]');
    transportButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        transportButtons.forEach(b => b.setAttribute('aria-checked', 'false'));
        btn.setAttribute('aria-checked', 'true');
        selectedTransport = btn.dataset.transport;
        $('#nextFromTransport').disabled = false;
      });
    });
    $('#nextFromTransport').addEventListener('click', () => stepTo(2));

    // Step 2: Accommodation
    const accommodationButtons = $$('[data-accommodation]');
    accommodationButtons.forEach(btn => {
      btn.addEventListener('click', () => {
        accommodationButtons.forEach(b => b.setAttribute('aria-checked', 'false'));
        btn.setAttribute('aria-checked', 'true');
        selectedAccommodation = btn.dataset.accommodation;
        $('#nextFromAccommodation').disabled = false;
      });
    });
    $('#backFromAccommodation').addEventListener('click', () => stepTo(1));
    $('#nextFromAccommodation').addEventListener('click', () => {
      generateItinerary();
      stepTo(3);
    });

    // AI Generation - Random selection of 2 items per category
    function getRandomItems(arr, count) {
      const shuffled = [...arr].sort(() => Math.random() - 0.5);
      return shuffled.slice(0, count);
    }

    function generateItinerary() {
      generatedItinerary = {
        transport: selectedTransport,
        accommodation: selectedAccommodation,
        cities: {}
      };

      selectedDestinations.forEach(city => {
        const data = CITY_DATA[city];
        generatedItinerary.cities[city] = {
          destinations: getRandomItems(data.destinations, 2),
          foods: getRandomItems(data.foods, 2),
          sports: getRandomItems(data.sports, 2)
        };
      });

      // Store in localStorage
      localStorage.setItem('westCoastItinerary', JSON.stringify(generatedItinerary));
      localStorage.setItem('westCoastItineraryTimestamp', new Date().toISOString());

      displayItinerary();
      generateQuiz();
    }

    function displayItinerary() {
      const wrap = $('#itineraryPreview');
      let html = '<h3>✨ Your West Coast Adventure</h3>';

      Object.keys(generatedItinerary.cities).forEach((city, idx) => {
        const cityData = generatedItinerary.cities[city];
        html += `
          <div class="stop">
            <h4>Stop ${idx + 1}: ${city}</h4>
            
            <div class="category">
              <div class="category-title">🏛️ Destinations to Visit:</div>
              <ul class="item-list">
                ${cityData.destinations.map(d => `<li>${d}</li>`).join('')}
              </ul>
            </div>

            <div class="category">
              <div class="category-title">🍽️ Foods to Try:</div>
              <ul class="item-list">
                ${cityData.foods.map(f => `<li>${f}</li>`).join('')}
              </ul>
            </div>

            <div class="category">
              <div class="category-title">🏟️ Sports & Venues:</div>
              <ul class="item-list">
                ${cityData.sports.map(s => `<li>${s.name} at ${s.venue}</li>`).join('')}
              </ul>
            </div>
          </div>
        `;
      });

      wrap.innerHTML = html;
    }

    function generateQuiz() {
      const container = $('#quizContainer');
      let html = '';

      QUIZ_QUESTIONS.forEach((q, idx) => {
        html += `
          <div class="quiz-question" data-question="${idx}">
            <h4>Question ${idx + 1}: ${q.question}</h4>
            <div class="quiz-options">
              ${q.options.map((opt, optIdx) => `
                <div class="quiz-option" data-option="${optIdx}">
                  ${opt}
                </div>
              `).join('')}
            </div>
            <div class="quiz-result" hidden></div>
          </div>
        `;
      });

      container.innerHTML = html;

      // Add click handlers
      $$('.quiz-option').forEach(opt => {
        opt.addEventListener('click', function() {
          const questionDiv = this.closest('.quiz-question');
          const questionIdx = parseInt(questionDiv.dataset.question);
          const optionIdx = parseInt(this.dataset.option);
          const question = QUIZ_QUESTIONS[questionIdx];
          
          // Clear previous selection
          questionDiv.querySelectorAll('.quiz-option').forEach(o => o.classList.remove('selected'));
          this.classList.add('selected');
          
          // Show result
          const resultDiv = questionDiv.querySelector('.quiz-result');
          const isCorrect = optionIdx === question.correct;
          resultDiv.className = 'quiz-result ' + (isCorrect ? 'correct' : 'incorrect');
          resultDiv.textContent = isCorrect ? `✓ Correct! ${question.explanation}` : `✗ ${question.explanation}`;
          resultDiv.hidden = false;
        });
      });
    }

    // Step 3: Utilities
    $('#backFromItinerary').addEventListener('click', () => stepTo(2));
    $('#nextFromItinerary').addEventListener('click', () => {
      generateFinalSummary();
      stepTo(4);
    });

    $('#exportBtn').addEventListener('click', () => {
      const data = {
        ...generatedItinerary,
        notes: $('#tripNotes').value,
        generatedAt: new Date().toISOString()
      };
      const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' });
      const url = URL.createObjectURL(blob);
      const a = document.createElement('a');
      a.href = url;
      a.download = 'west-coast-itinerary.json';
      a.click();
      URL.revokeObjectURL(url);
    });

    $('#shareBtn').addEventListener('click', async () => {
      const summary = `My West Coast Trip: ${Object.keys(generatedItinerary.cities).join(' → ')}`;
      try {
        if (navigator.share) {
          await navigator.share({ title: 'West Coast Trip', text: summary });
        } else {
          await navigator.clipboard.writeText(summary);
          alert('Summary copied to clipboard!');
        }
      } catch (e) {
        console.error('Share failed:', e);
      }
    });

    // Step 4: Final summary
    function generateFinalSummary() {
      const cities = Object.keys(generatedItinerary.cities);
      let html = `
        <p style="line-height:1.9">
          <strong>🌍 Destinations:</strong> ${cities.join(' → ')}<br />
          <strong>🚗 Transportation:</strong> ${selectedTransport}<br />
          <strong>🏨 Accommodations:</strong> ${selectedAccommodation}<br />
          <strong>⏱️ Duration:</strong> ${cities.length * 2.5} days (approx)
        </p>
      `;
      $('#finalSummary').innerHTML = html;
    }

    $('#backFromShare').addEventListener('click', () => stepTo(3));
    $('#restartBtn').addEventListener('click', () => {
      selectedTransport = '';
      selectedAccommodation = '';
      generatedItinerary = null;
      transportButtons.forEach(b => b.setAttribute('aria-checked', 'false'));
      accommodationButtons.forEach(b => b.setAttribute('aria-checked', 'false'));
      $('#nextFromTransport').disabled = true;
      $('#nextFromAccommodation').disabled = true;
      $('#tripNotes').value = '';
      $('#reflection').value = '';
      stepTo(1);
    });

    updateProgress();
  </script>
</body>
</html>

<!-- 🌴 San Diego Journey Button -->
<a href="https://pages.opencodingsociety.com/west-coast/analytics/sandiego/" target="_blank" style="
  display: inline-block;
  background: linear-gradient(135deg, #007bff, #00bcd4);
  color: white;
  font-size: 18px;
  font-weight: bold;
  text-decoration: none;
  padding: 14px 24px;
  border-radius: 10px;
  box-shadow: 0 4px 10px rgba(0,0,0,0.2);
  transition: all 0.3s ease;
">
  🌴: Click to start your journey in San Diego
</a>

<script>
  // Optional hover effect for interaction
  const link = document.querySelector('a[href*="sandiego"]');
  link.addEventListener('mouseover', () => link.style.transform = 'scale(1.05)');
  link.addEventListener('mouseout', () => link.style.transform = 'scale(1)');
</script>
