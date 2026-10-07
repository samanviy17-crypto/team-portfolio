---
layout: opencs
title: "Los Angeles"
description: "Submodule 2 of Backend Development Mini-Quest"
permalink: /west-coast/backend/submodule_2/
parent: "Backend Development"
team: "Zombies"
submodule: 2
categories: [CSP, Submodule, Backend]
tags: [backend, submodule, zombies]
author: "Zombies Team"
date: 2025-10-21
microblog: True
footer:
  previous: /west-coast/backend/submodule_1/
  home: /west-coast/sports/
  next: /west-coast/backend/submodule_3/
---

<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>LA Sports API - Step 2: Backend Setup</title>
    <style>
{{ '@import "beasts/inline/pages/hacks-west-coast-sports-submodule-2-1";' | scssify }}
</style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🌟 Los Angeles Sports API</h1>
            <p>Learn to Build API URLs Like a Pro!</p>
            <div class="step-badge">📊 Step 2: Understanding API URLs</div>
        </div>

        <div class="concept-section">
            <h2>📚 Understanding API URLs</h2>
            <p>Just like finding seats at Dodger Stadium, API URLs have specific parts that tell you exactly where to go. Let's break down how to build the perfect API URL to get LA sports team data!</p>
            
            <h3>🏠 Base URL</h3>
            <p>The foundation - like the stadium address</p>
            <div class="code-box">https://www.thesportsdb.com/api/v1/json/</div>

            <h3>🔑 API Key</h3>
            <p>Your ticket to access the data</p>
            <div class="code-box">3</div>

            <h3>📍 Endpoint</h3>
            <p>What section you're looking for</p>
            <div class="code-box">searchteams.php</div>

            <h3>🎯 Parameters</h3>
            <p>Your specific seat number</p>
            <div class="code-box">?t=Dodgers</div>

            <h3 style="margin-top: 30px;">Complete URL Example:</h3>
            <div class="code-box" style="font-size: 1.1em;">https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t=Dodgers</div>
        </div>

        <div class="la-teams-showcase">
            <h2>🏟️ Your LA Sports Teams & Their API URLs</h2>
            <div class="teams-grid" id="teams-grid"></div>
        </div>

        <div class="practice-section">
            <h2>✏️ Practice: Build Your Own URL</h2>
            <button class="check-button" style="margin-bottom: 30px;" onclick="autofillAll()">⚙️ Autofill All Fields</button>
            <div id="practice-container"></div>
        </div>

        <div class="challenge-section">
            <h2>🎯 Challenge Time!</h2>
            
            <div class="challenge-card">
                <h3>Challenge 1: Build a URL for the LA Rams</h3>
                <input type="text" class="challenge-input" id="challenge1" placeholder="Type your URL here...">
                <button class="challenge-button" onclick="checkChallenge(1)">Check Answer</button>
                <div class="feedback" id="feedback1"></div>
                <div class="hint">💡 Hint: Replace "Dodgers" with "Rams" in the example URL</div>
            </div>

            <div class="challenge-card">
                <h3>Challenge 2: Get ALL NBA Teams</h3>
                <input type="text" class="challenge-input" id="challenge2" placeholder="Type your URL here...">
                <button class="challenge-button" onclick="checkChallenge(2)">Check Answer</button>
                <div class="feedback" id="feedback2"></div>
                <div class="hint">💡 Hint: Use endpoint "search_all_teams.php" with parameter "?l=NBA"</div>
            </div>

            <div class="challenge-card">
                <h3>Challenge 3: Search for USC Trojans Players</h3>
                <input type="text" class="challenge-input" id="challenge3" placeholder="Type your URL here...">
                <button class="challenge-button" onclick="checkChallenge(3)">Check Answer</button>
                <div class="feedback" id="feedback3"></div>
                <div class="hint">💡 Hint: Use endpoint "searchplayers.php" with parameter "?t=USC_Trojans" (use underscore for spaces)</div>
            </div>
        </div>

        <div class="key-takeaways">
            <h2>💡 Key Takeaways</h2>
            <ul>
                <li><strong>API URLs have four main parts:</strong> Base URL, API Key, Endpoint, and Parameters — each serves a specific purpose</li>
                <li><strong>Base URL is the foundation</strong> — it's like the street address of the API server</li>
                <li><strong>API Keys authenticate requests</strong> — they're your ticket to access the data</li>
                <li><strong>Endpoints specify what data you want</strong> — different endpoints return different types of information</li>
                <li><strong>Parameters filter and customize results</strong> — use them to get exactly the data you need</li>
                <li><strong>Practice building URLs</strong> — understanding URL structure is essential for working with any API</li>
            </ul>
        </div>
    </div>

    <script>
        // COMPLETE LA TEAMS DATABASE
        const COMPLETE_LA_TEAMS = {
            "Basketball - Clippers": {
                id: 1,
                name: "Los Angeles Clippers",
                sport: "Basketball - Clippers",
                stadium: "Intuit Dome",
                capacity: 18000,
                founded: 1970,
                championships: 0,
                icon: "🏀",
                searchName: "Los%20Angeles%20Clippers"
            },
            "Football - Chargers": {
                id: 2,
                name: "Los Angeles Chargers",
                sport: "Football - Chargers",
                stadium: "SoFi Stadium",
                capacity: 70240,
                founded: 1960,
                championships: 0,
                icon: "🏈",
                searchName: "Chargers"
            },
            "Football - USC": {
                id: 3,
                name: "USC Trojans",
                sport: "Football - USC",
                stadium: "LA Memorial Coliseum",
                capacity: 77500,
                founded: 1888,
                championships: 11,
                icon: "🏈",
                searchName: "USC"
            },
            "Baseball - Dodgers": {
                id: 4,
                name: "Los Angeles Dodgers",
                sport: "Baseball - Dodgers",
                stadium: "Dodger Stadium",
                capacity: 56000,
                founded: 1883,
                championships: 7,
                icon: "⚾",
                searchName: "Dodgers"
            },
            "Soccer - LA Galaxy": {
                id: 5,
                name: "LA Galaxy",
                sport: "Soccer - LA Galaxy",
                stadium: "Dignity Health Sports Park",
                capacity: 27000,
                founded: 1995,
                championships: 5,
                icon: "⚽",
                searchName: "LA%20Galaxy"
            }
        };

        let userTeams = [];

        // Load user's itinerary from localStorage
        function loadUserItinerary() {
            try {
                const itinerary = JSON.parse(localStorage.getItem('westCoastItinerary'));
                if (itinerary && itinerary.cities && itinerary.cities['Los Angeles'] && 
                    itinerary.cities['Los Angeles'].sports) {
                    const userSports = itinerary.cities['Los Angeles'].sports;
                    
                    // Map user sports to team data
                    userTeams = userSports.map(sport => COMPLETE_LA_TEAMS[sport.name]).filter(t => t);
                    
                    if (userTeams.length === 2) {
                        displayUserTeams();
                        createPracticeAreas();
                    }
                }
            } catch (error) {
                console.error('Error loading itinerary:', error);
            }
        }

        // Display user's selected teams
        function displayUserTeams() {
            const grid = document.getElementById('teams-grid');
            let html = '';

            userTeams.forEach(team => {
                const teamUrl = `https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t=${team.searchName}`;
                const elementId = team.sport.toLowerCase().replace(/\s+/g, '-').replace(/-+/g, '-') + '-url';
                html += `
                    <div class="team-card">
                        <div class="team-icon">${team.icon}</div>
                        <div class="team-name">${team.name}</div>
                        <div class="stadium-name">${team.stadium}</div>
                        <div class="team-url" id="${elementId}">${teamUrl}</div>
                        <button class="copy-button" onclick="copyURL('${elementId}')">📋 Copy URL</button>
                    </div>
                `;
            });

            grid.innerHTML = html;
        }

        // Create practice areas dynamically based on user teams
        function createPracticeAreas() {
            const container = document.getElementById('practice-container');
            let html = '';

            userTeams.forEach((team, index) => {
                const num = index + 1;
                html += `
                    <div class="build-area">
                        <p>Now it's your turn! Fill in the blanks to create an API URL for the ${team.name}.</p>
                        
                        <div class="build-step">
                            <div class="step-label">Step 1: Base URL</div>
                            <input type="text" class="step-input" id="base-url-${num}" placeholder="Enter the base URL...">
                        </div>

                        <div class="build-step">
                            <div class="step-label">Step 2: API Key</div>
                            <input type="text" class="step-input" id="api-key-${num}" placeholder="Enter your API key...">
                        </div>

                        <div class="build-step">
                            <div class="step-label">Step 3: Endpoint</div>
                            <input type="text" class="step-input" id="endpoint-${num}" placeholder="Enter the endpoint...">
                        </div>

                        <div class="build-step">
                            <div class="step-label">Step 4: Team Parameter</div>
                            <input type="text" class="step-input" id="parameter-${num}" placeholder="Enter ?t=TeamName...">
                        </div>

                        <div class="build-step">
                            <div class="step-label">Your Complete URL:</div>
                            <div class="url-output" id="built-url-${num}">Fill in the fields above to build your URL...</div>
                        </div>

                        <button class="check-button" onclick="checkBuiltURL(${num})">✅ Check My URL</button>
                        <div class="feedback" id="build-feedback-${num}"></div>
                    </div>
                `;
            });

            container.innerHTML = html;

            // Add event listeners for dynamic inputs
            userTeams.forEach((team, index) => {
                const num = index + 1;
                document.getElementById(`base-url-${num}`)?.addEventListener('input', () => updateBuiltURL(num));
                document.getElementById(`api-key-${num}`)?.addEventListener('input', () => updateBuiltURL(num));
                document.getElementById(`endpoint-${num}`)?.addEventListener('input', () => updateBuiltURL(num));
                document.getElementById(`parameter-${num}`)?.addEventListener('input', () => updateBuiltURL(num));
            });
        }

        function copyURL(elementId) {
            const urlElement = document.getElementById(elementId);
            const url = urlElement.textContent;
            
            navigator.clipboard.writeText(url).then(() => {
                alert('✅ URL copied to clipboard!\n\nNow paste it in your browser address bar to test it!');
            }).catch(err => {
                alert('Please select and copy the URL manually: ' + url);
            });
        }

        function updateBuiltURL(num) {
            const base = document.getElementById(`base-url-${num}`)?.value || '';
            const key = document.getElementById(`api-key-${num}`)?.value || '';
            const endpoint = document.getElementById(`endpoint-${num}`)?.value || '';
            const param = document.getElementById(`parameter-${num}`)?.value || '';
            
            let url = '';
            if (base) url += base;
            if (key) url += key + '/';
            if (endpoint) url += endpoint;
            if (param) url += param;
            
            const outputElement = document.getElementById(`built-url-${num}`);
            if (outputElement) {
                outputElement.textContent = url || 'Fill in the fields above to build your URL...';
            }
        }

        function checkBuiltURL(num) {
            const builtURL = document.getElementById(`built-url-${num}`).textContent.trim();
            const feedback = document.getElementById(`build-feedback-${num}`);
            
            if (num <= userTeams.length) {
                const team = userTeams[num - 1];
                const correctURL = `https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t=${team.searchName}`;
                const teamName = team.name;
                
                const alt1 = correctURL.replace(/%20/g, '+');
                const alt2 = correctURL.replace(/%20/g, ' ');
                
                if (builtURL.toLowerCase() === correctURL.toLowerCase() || 
                    builtURL.toLowerCase() === alt1.toLowerCase() || 
                    builtURL.toLowerCase() === alt2.toLowerCase()) {
                    feedback.className = 'feedback correct';
                    feedback.textContent = `🎉 Perfect! You built the ${teamName} API URL correctly! Try copying and testing it in your browser.`;
                } else {
                    feedback.className = 'feedback incorrect';
                    feedback.textContent = `❌ Not quite right. The correct answer is: ${correctURL}`;
                }
            }
        }

        function checkChallenge(challengeNum) {
            const input = document.getElementById(`challenge${challengeNum}`).value.trim();
            const feedback = document.getElementById(`feedback${challengeNum}`);
            
            let correct = false;
            let correctAnswer = '';

            switch(challengeNum) {
                case 1:
                    correctAnswer = 'https://www.thesportsdb.com/api/v1/json/3/searchteams.php?t=Rams';
                    correct = input.toLowerCase() === correctAnswer.toLowerCase();
                    break;
                case 2:
                    correctAnswer = 'https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?l=NBA';
                    correct = input.toLowerCase() === correctAnswer.toLowerCase();
                    break;
                case 3:
                    correctAnswer = 'https://www.thesportsdb.com/api/v1/json/3/searchplayers.php?t=USC_Trojans';
                    correct = input.toLowerCase() === correctAnswer.toLowerCase();
                    break;
            }

            if (correct) {
                feedback.className = 'feedback correct';
                feedback.textContent = '🎉 Correct! Great job! Copy this URL and test it in your browser to see the data.';
            } else {
                feedback.className = 'feedback incorrect';
                feedback.textContent = `❌ Not quite right. The correct answer is: ${correctAnswer}`;
            }
        }

        // Load user's itinerary on page load
        document.addEventListener('DOMContentLoaded', loadUserItinerary);
        function autofillAll() {
            userTeams.forEach((team, index) => {
                const num = index + 1;

        // Autofill correct values
                document.getElementById(`base-url-${num}`).value = 'https://www.thesportsdb.com/api/v1/json/';
                document.getElementById(`api-key-${num}`).value = '3';
                document.getElementById(`endpoint-${num}`).value = 'searchteams.php';
                document.getElementById(`parameter-${num}`).value = `?t=${team.searchName.replace(/%20/g, ' ')}`;

        // Update display and feedback
                updateBuiltURL(num);
                const feedback = document.getElementById(`build-feedback-${num}`);
                feedback.className = 'feedback correct';
                feedback.textContent = `✅ Autofilled successfully for ${team.name}!`;
    });
}

    </script>
</body>
</html>