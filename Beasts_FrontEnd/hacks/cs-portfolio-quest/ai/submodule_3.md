---
layout: cs-portfolio-lesson
title: "Professional Applications"
description: "Use AI for resumes, interviews, and knowing when NOT to use AI"
permalink: /cs-portfolio-quest/ai/submodule_3/
parent: "AI Usage"
team: "Thinkers"
submodule: 3
is_last_submodule: true
tags: [ai, submodule, thinkers]
author: "Thinkers Team"
date: 2025-10-21
breadcrumb: true
microblog: true
---

<style>
{{ '@import "beasts/inline/pages/hacks-cs-portfolio-quest-ai-submodule-3-1";' | scssify }}
</style>

<div class="comic-container">
    <div class="comic-header">
        <h1 class="pow-effect">PROFESSIONAL APPLICATIONS!</h1>
        <p style="color: #f3f3f3 !important; font-style: italic;">Use AI for resumes, interviews, and knowing when NOT to use AI</p>
    </div>

    <!-- PAGE 1: Resume Transformation -->
    <div class="comic-page active" id="page-1">
        <img src="{{site.baseurl}}/images/docx/Quests_QuestOfCode-AIUsage-Thinkers_image1.png" height="625">
        <div class="comic-panel">
            <h2 style="color: #000; font-size: 32px; margin-bottom: 20px;">Comic Strip 1: Resume Transformation</h2>
            <p style="color: #000; font-size: 18px; line-height: 1.8;">
                Generic bullets don't get interviews. <strong>Quantified STAR-format bullets do.</strong>
            </p>
        </div>

        <div class="star-method-box">
            <h3>The STAR Method</h3>
            <div class="star-component">
                <strong>S - Situation:</strong>
                <p>Set the context - Where were you? What was happening?</p>
            </div>
            <div class="star-component">
                <strong>T - Task:</strong>
                <p>Your responsibility - What did you need to accomplish?</p>
            </div>
            <div class="star-component">
                <strong>A - Action:</strong>
                <p>What you did - Specific steps you took</p>
            </div>
            <div class="star-component">
                <strong>R - Result:</strong>
                <p>Outcome with metrics - Numbers, percentages, impact</p>
            </div>
        </div>

        <div class="comparison-grid">
            <div class="speech-bubble bad">
                <h3>❌ Before</h3>
                <p><em>"Worked on team projects"</em></p>
                <p style="margin-top: 10px;"><strong>Problems:</strong> Vague, no metrics, no impact, anyone could write this</p>
            </div>

            <div class="speech-bubble good">
                <h3>✅ After</h3>
                <p><em>"Collaborated with 4-person team to build full-stack web app, reducing page load time by 40% through database query optimization"</em></p>
                <p style="margin-top: 10px;"><strong>Why it works:</strong> Specific role, team size, technology, measurable result</p>
            </div>
        </div>

        <div class="comparison-grid">
            <div class="speech-bubble bad">
                <h3>❌ Before</h3>
                <p><em>"Helped with coding"</em></p>
            </div>

            <div class="speech-bubble good">
                <h3>✅ After</h3>
                <p><em>"Implemented JWT authentication system using Flask and React, securing 10,000+ user accounts with 99.9% uptime"</em></p>
            </div>
        </div>

        <div class="transformer-tool">
            <h3>Resume Bullet Transformer</h3>
            <p style="margin-bottom: 15px;">Paste your weak bullet point and we'll generate 3 STAR versions!</p>

            <label style="display: block; margin-top: 15px; font-weight: bold;">Your Current Bullet:</label>
            <textarea id="weak-bullet" placeholder="e.g., 'Worked on website development'"></textarea>

            <button class="action-button" onclick="generateVersions()">Transform to STAR Format</button>

            <div id="versions-container" style="display: none; margin-top: 20px;">
                <div class="version-card">
                    <h4>Version 1: Conservative</h4>
                    <p id="version-conservative"></p>
                    <p class="pros-cons"><strong>Best for:</strong> When you want to play it safe and stick close to facts</p>
                </div>

                <div class="version-card">
                    <h4>Version 2: Balanced</h4>
                    <p id="version-balanced"></p>
                    <p class="pros-cons"><strong>Best for:</strong> Most situations - good detail with reasonable metrics</p>
                </div>

                <div class="version-card">
                    <h4>Version 3: Bold</h4>
                    <p id="version-bold"></p>
                    <p class="pros-cons"><strong>Best for:</strong> When you have impressive numbers to back it up</p>
                </div>
            </div>
        </div>

        <div class="submit-area">
            <h3>Submit Your Resume Bullet</h3>
            <p style="color: #000; margin-bottom: 15px;">Paste one weak bullet from your resume, then paste the AI-improved STAR version you'll actually use. Explain why you picked that version.</p>
            <textarea id="submit-prompt-1" placeholder="Original: [your weak bullet]

Improved: [STAR version you chose]

Why I picked this: [explanation of why it's honest and strong]"></textarea>
            <button class="action-button" onclick="saveSubmission(1)">Save Submission</button>
            <button class="action-button" onclick="loadExample(1)">Load Example</button>
            <div id="status-1" class="status-box"></div>
        </div>
    </div>

    <!-- PAGE 2: Interview Prep -->
    <div class="comic-page" id="page-2">
        <div class="comic-panel">
            <h2 style="color: #000; font-size: 32px; margin-bottom: 20px;">Comic Strip 2: Interview Prep That Works</h2>
            <p style="color: #000; font-size: 18px; margin-bottom: 20px;">
                <strong>Master the 3 questions you MUST nail</strong>
            </p>
        </div>

        <div class="interview-question-box">
            <h4>1. "Tell me about a time you failed"</h4>
            <div class="tip">
                <strong>What they want:</strong> Self-awareness, learning, growth
            </div>
            <div class="tip">
                <strong>Structure:</strong> Situation → What went wrong → What you learned → How you improved
            </div>
            <div class="tip">
                <strong>❌ Don't:</strong> Blame others, pick a personal issue, say "I don't fail"
            </div>
            <div class="tip">
                <strong>✅ Do:</strong> Own it, show what you learned, prove you applied the lesson
            </div>
        </div>

        <div class="interview-question-box">
            <h4>2. "Walk me through [project name] architecture"</h4>
            <div class="tip">
                <strong>What they want:</strong> Technical depth, decision-making, trade-offs
            </div>
            <div class="tip">
                <strong>Structure:</strong> High-level overview → Dive into 2-3 key components → Explain why you chose them
            </div>
            <div class="tip">
                <strong>❌ Don't:</strong> Jump straight to tiny details, memorize a script
            </div>
            <div class="tip">
                <strong>✅ Do:</strong> Start broad, go deep when asked, explain trade-offs
            </div>
        </div>

        <div class="interview-question-box">
            <h4>3. "Why are you interested in this company?"</h4>
            <div class="tip">
                <strong>What they want:</strong> You actually researched them, fit with their needs
            </div>
            <div class="tip">
                <strong>❌ Don't:</strong> "Great culture", "learning opportunity" (everyone says this)
            </div>
            <div class="tip">
                <strong>✅ Do:</strong> Reference their tech stack, recent projects, specific problems you can solve
            </div>
        </div>

        <div class="interview-analyzer">
            <h3>Mock Interview Analyzer</h3>
            <p style="margin-bottom: 15px;">Type your answer to ONE of the 3 questions above (250 words max)</p>

            <label style="display: block; margin-top: 15px; font-weight: bold;">Which question are you answering?</label>
            <select id="question-choice" style="width: 100%; padding: 10px; border: 3px solid #000; border-radius: 10px; margin: 10px 0;">
                <option value="1">Question 1: Tell me about a time you failed</option>
                <option value="2">Question 2: Walk me through your architecture</option>
                <option value="3">Question 3: Why this company?</option>
            </select>

            <label style="display: block; margin-top: 15px; font-weight: bold;">Your Answer:</label>
            <textarea id="interview-answer" placeholder="Type your answer here..." style="width: 100%; min-height: 150px; padding: 15px; border: 3px solid #000; border-radius: 10px; margin: 10px 0;"></textarea>

            <button class="action-button" onclick="analyzeInterview()">Analyze My Answer</button>

            <div class="analysis-result" id="analysis-result">
                <h4 style="color: #4ECDC4; margin-bottom: 15px;">Analysis Results</h4>
                <div id="analysis-content"></div>
            </div>
        </div>

        <div class="submit-area">
            <h3>Submit Your Interview Answer</h3>
            <p style="color: #000; margin-bottom: 15px;">Write your answer to ONE of the 3 questions (250 words max). Use STAR format. Then list what you would improve.</p>
            <textarea id="submit-prompt-2" placeholder="Question: [which one you chose]

My Answer: [your full answer]

What I would improve: [specific things to make it better]"></textarea>
            <button class="action-button" onclick="saveSubmission(2)">Save Submission</button>
            <button class="action-button" onclick="loadExample(2)">Load Example</button>
            <div id="status-2" class="status-box"></div>
        </div>
    </div>

    <!-- PAGE 3: When AI Helps/Doesn't -->
    <div class="comic-page" id="page-3">
        <div class="comic-panel">
            <h2 style="color: #000; font-size: 32px; margin-bottom: 20px;">Comic Strip 3: When AI Helps (and When It Doesn't)</h2>
            <p style="color: #000; font-size: 18px;">
                <strong>Know when to use AI and when to stay away</strong>
            </p>
        </div>

        <div class="comparison-grid">
            <div class="speech-bubble good">
                <h3>✅ When AI Actually Helps</h3>
                <ul style="margin-top: 10px; padding-left: 20px; color: #000;">
                    <li>Summarizing long documents/emails</li>
                    <li>Generating meeting notes with action items</li>
                    <li>Quick data analysis in Sheets</li>
                    <li>Draft responses to common questions</li>
                    <li>Extracting key points from research</li>
                    <li>Brainstorming ideas/approaches</li>
                </ul>
            </div>

            <div class="speech-bubble bad">
                <h3>❌ When It Doesn't Help</h3>
                <ul style="margin-top: 10px; padding-left: 20px; color: #000;">
                    <li>Technical/specialized content (AI guesses)</li>
                    <li>Legal or medical documents</li>
                    <li>Anything requiring 100% accuracy</li>
                    <li>Math proofs or complex calculations</li>
                    <li>Real-time/current event info</li>
                    <li>Financial advice or medical diagnosis</li>
                </ul>
            </div>
        </div>

        <div class="comic-panel">
            <h3 style="color: #000; font-size: 24px; margin-bottom: 15px;">Red Flags for Unreliable AI Output</h3>
            <ul class="red-flag-list">
                <li>Gives different answers to the same question</li>
                <li>Overly detailed when you asked for summary (hallucination)</li>
                <li>No sources provided for factual claims</li>
                <li>Generic advice when you need specifics</li>
                <li>"As of my knowledge cutoff..." (info might be outdated)</li>
            </ul>
        </div>

        <div class="use-case-sorter">
            <h3>Use Case Sorter Game</h3>
            <p style="margin-bottom: 15px;">Click each scenario card to sort it into "Good AI Use" or "Bad AI Use"</p>
            <p style="margin-bottom: 20px; font-style: italic;">Score: <span id="game-score">0/12</span> correct</p>

            <div id="scenarios-container">
                <!-- Scenarios will be generated here -->
            </div>

            <button class="action-button" onclick="resetGame()" style="margin-top: 20px;">Reset Game</button>
        </div>

        <div class="submit-area">
            <h3>Submit Your AI Use Cases</h3>
            <p style="color: #000; margin-bottom: 15px;">Describe one task where AI SAVED you time. Then describe one task where you should NOT use AI. Explain why for both (2-3 sentences each).</p>
            <textarea id="submit-prompt-3" placeholder="Task where AI helped: [describe task]
Why it helped: [explanation]

Task where you shouldn't use AI: [describe task]
Why not: [explanation]" style="min-height: 200px;"></textarea>
            <button class="action-button" onclick="saveSubmission(3)">Save Submission</button>
            <button class="action-button" onclick="loadExample(3)">Load Example</button>
            <div id="status-3" class="status-box"></div>
        </div>
    </div>

    <div class="navigation" id="pageNav">
        <button class="nav-button" id="prevBtn" onclick="changePage(-1)">← Previous</button>
        <div class="page-indicator">
            Page <span id="currentPage">1</span> of <span id="totalPages">3</span>
        </div>
        <button class="nav-button" id="nextBtn" onclick="changePage(1)">Next →</button>
    </div>

    <!-- Module Navigation (only shows on page 3) -->
    <div class="navigation" id="moduleNav" style="display: none;">
        <a href="{{site.baseurl}}/cs-portfolio-quest/ai/" class="nav-button" style="text-decoration: none; display: inline-block; width: auto;">← Back to AI Module</a>
    </div>
</div>

<script>
    let currentPage = 1;
    const totalPages = 3;
    let gameScore = 0;
    let gamesPlayed = 0;

    // Scenarios for the sorting game
    const scenarios = [
        { text: "Summarize 50-page research paper", correct: "good" },
        { text: "Generate legal contract for startup", correct: "bad" },
        { text: "Write SQL query for database", correct: "good" },
        { text: "Diagnose chest pain symptoms", correct: "bad" },
        { text: "Brainstorm app feature ideas", correct: "good" },
        { text: "Calculate structural load for bridge", correct: "bad" },
        { text: "Draft email response template", correct: "good" },
        { text: "Provide financial investment advice", correct: "bad" },
        { text: "Extract meeting action items", correct: "good" },
        { text: "Prescribe medication dosage", correct: "bad" },
        { text: "Generate code documentation", correct: "good" },
        { text: "Interpret medical lab results", correct: "bad" }
    ];

    function showPage(pageNum) {
        document.querySelectorAll('.comic-page').forEach(page => {
            page.classList.remove('active');
        });
        document.getElementById(`page-${pageNum}`).classList.add('active');
        document.getElementById('currentPage').textContent = pageNum;

        document.getElementById('prevBtn').disabled = pageNum === 1;
        document.getElementById('nextBtn').disabled = pageNum === totalPages;
        
        // Show/hide module navigation on last page
        const pageNav = document.querySelector('.navigation:not(#moduleNav)');
        const moduleNav = document.getElementById('moduleNav');
        
        if (pageNum === totalPages) {
            pageNav.style.display = 'none';
            moduleNav.style.display = 'flex';
        } else {
            pageNav.style.display = 'flex';
            moduleNav.style.display = 'none';
        }

        window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    function changePage(direction) {
        currentPage += direction;
        if (currentPage < 1) currentPage = 1;
        if (currentPage > totalPages) currentPage = totalPages;
        showPage(currentPage);
    }

    document.addEventListener('keydown', function(e) {
        if (e.key === 'ArrowLeft') changePage(-1);
        if (e.key === 'ArrowRight') changePage(1);
    });

    function generateVersions() {
        const weakBullet = document.getElementById('weak-bullet').value.trim();
        
        if (!weakBullet) {
            alert('Please enter a resume bullet point first!');
            return;
        }

        // Conservative version
        document.getElementById('version-conservative').textContent = 
            `Contributed to team project using ${extractTech(weakBullet)}, implementing core features and collaborating with 3-4 team members to meet project deadlines`;

        // Balanced version
        document.getElementById('version-balanced').textContent = 
            `Developed ${extractTech(weakBullet)} application as part of 4-person team, implementing 5+ key features and improving system performance by 25% through code optimization`;

        // Bold version
        document.getElementById('version-bold').textContent = 
            `Led development of ${extractTech(weakBullet)} platform serving 5,000+ monthly users, architecting scalable backend infrastructure and reducing load times by 40% through database optimization and caching strategies`;

        document.getElementById('versions-container').style.display = 'block';
    }

    function extractTech(text) {
        const techKeywords = ['web', 'app', 'website', 'application', 'software', 'system'];
        const lowerText = text.toLowerCase();
        
        for (let tech of techKeywords) {
            if (lowerText.includes(tech)) {
                return tech;
            }
        }
        return 'web';
    }

    function analyzeInterview() {
        const answer = document.getElementById('interview-answer').value.trim();
        const question = document.getElementById('question-choice').value;

        if (!answer) {
            alert('Please write your interview answer first!');
            return;
        }

        const wordCount = answer.split(/\s+/).length;
        const fillerWords = (answer.match(/\b(um|uh|like|you know|basically|actually)\b/gi) || []).length;
        const hasMetrics = /\d+/.test(answer);
        const hasSTAR = answer.length > 100;

        let analysisHTML = '';

        // Filler words analysis
        const fillerPercentage = Math.round((fillerWords / wordCount) * 100);
        const fillerClass = fillerPercentage < 3 ? 'good' : fillerPercentage < 7 ? 'medium' : 'bad';
        analysisHTML += `<div><span class="score-badge ${fillerClass}">Filler Words: ${fillerWords} (${fillerPercentage}%)</span>`;
        if (fillerPercentage > 5) {
            analysisHTML += `<p style="color: #666; margin-top: 5px;">Remove words like: "um", "like", "you know"</p>`;
        }
        analysisHTML += `</div>`;

        // STAR structure
        const starClass = hasSTAR ? 'good' : 'bad';
        analysisHTML += `<div style="margin-top: 15px;"><span class="score-badge ${starClass}">STAR Structure: ${hasSTAR ? 'Present' : 'Missing'}</span>`;
        if (!hasSTAR) {
            analysisHTML += `<p style="color: #666; margin-top: 5px;">Add more detail - describe Situation, Task, Action, Result</p>`;
        }
        analysisHTML += `</div>`;

        // Specificity
        const specificityScore = hasMetrics ? 9 : 5;
        const specificityClass = specificityScore >= 8 ? 'good' : 'medium';
        analysisHTML += `<div style="margin-top: 15px;"><span class="score-badge ${specificityClass}">Specificity: ${specificityScore}/10</span>`;
        if (!hasMetrics) {
            analysisHTML += `<p style="color: #666; margin-top: 5px;">Add metrics: team sizes, percentages, time saved, users impacted</p>`;
        }
        analysisHTML += `</div>`;

        // Length
        const lengthClass = wordCount >= 100 && wordCount <= 300 ? 'good' : 'medium';
        analysisHTML += `<div style="margin-top: 15px;"><span class="score-badge ${lengthClass}">Length: ${wordCount} words</span>`;
        if (wordCount < 100) {
            analysisHTML += `<p style="color: #666; margin-top: 5px;">Too short - add more detail about what you did and the outcome</p>`;
        } else if (wordCount > 300) {
            analysisHTML += `<p style="color: #666; margin-top: 5px;">Too long - practice condensing to 2-3 minutes (150-250 words)</p>`;
        }
        analysisHTML += `</div>`;

        // Overall feedback
        analysisHTML += `<div style="margin-top: 20px; padding: 15px; background: #f8f9fa; border-radius: 8px;">`;
        analysisHTML += `<strong style="color: #000;">Overall Feedback:</strong><br>`;
        if (specificityScore >= 8 && fillerPercentage < 5 && hasSTAR) {
            analysisHTML += `<span style="color: #28a745;">Strong answer! Your response is specific, well-structured, and concise.</span>`;
        } else {
            analysisHTML += `<span style="color: #856404;">Good start! Focus on: `;
            const improvements = [];
            if (!hasMetrics) improvements.push('adding specific numbers');
            if (fillerPercentage > 5) improvements.push('removing filler words');
            if (!hasSTAR) improvements.push('using STAR format');
            analysisHTML += improvements.join(', ') + '.</span>';
        }
        analysisHTML += `</div>`;

        document.getElementById('analysis-content').innerHTML = analysisHTML;
        document.getElementById('analysis-result').classList.add('show');
    }

    function initializeGame() {
        const container = document.getElementById('scenarios-container');
        container.innerHTML = '';
        gameScore = 0;
        gamesPlayed++;

        scenarios.forEach((scenario, index) => {
            const card = document.createElement('div');
            card.className = 'scenario-card';
            card.textContent = scenario.text;
            card.dataset.correct = scenario.correct;
            card.dataset.index = index;
            card.onclick = () => handleScenarioClick(card);
            container.appendChild(card);
        });

        updateScore();
    }

    function handleScenarioClick(card) {
        if (card.classList.contains('correct') || card.classList.contains('incorrect')) {
            return; // Already answered
        }

        const userChoice = confirm(`Is "${card.textContent}" a GOOD use of AI?\n\nClick OK for YES (good use)\nClick Cancel for NO (bad use)`);
        const correctAnswer = card.dataset.correct;
        const isCorrect = (userChoice && correctAnswer === 'good') || (!userChoice && correctAnswer === 'bad');

        if (isCorrect) {
            card.classList.add('correct');
            card.textContent = '✓ ' + card.textContent + ' - Correct!';
            gameScore++;
        } else {
            card.classList.add('incorrect');
            card.textContent = '✗ ' + card.textContent + ` - Actually ${correctAnswer === 'good' ? 'GOOD' : 'BAD'} use`;
        }

        updateScore();
    }

    function updateScore() {
        document.getElementById('game-score').textContent = `${gameScore}/12`;
    }

    function resetGame() {
        initializeGame();
    }

    function saveSubmission(pageNum) {
        const textarea = document.getElementById('submit-prompt-' + pageNum);
        const statusDiv = document.getElementById('status-' + pageNum);
        const content = textarea.value.trim();

        if (!content) {
            statusDiv.textContent = "Please write something before saving!";
            statusDiv.style.backgroundColor = "#fff3cd";
            statusDiv.style.color = "#856404";
            statusDiv.style.borderColor = "#ffc107";
            statusDiv.style.display = "block";
            setTimeout(() => statusDiv.style.display = "none", 3000);
            return;
        }

        const data = {
            page: pageNum,
            content: content,
            timestamp: new Date().toISOString()
        };

        try {
            localStorage.setItem('ai-submodule-3-page-' + pageNum, JSON.stringify(data));
            statusDiv.textContent = "Submission saved successfully!";
            statusDiv.style.backgroundColor = "#d4edda";
            statusDiv.style.color = "#155724";
            statusDiv.style.borderColor = "#28a745";
            statusDiv.style.display = "block";
            setTimeout(() => statusDiv.style.display = "none", 3000);
        } catch (error) {
            statusDiv.textContent = "Failed to save: " + error.message;
            statusDiv.style.backgroundColor = "#f8d7da";
            statusDiv.style.color = "#721c24";
            statusDiv.style.borderColor = "#dc3545";
            statusDiv.style.display = "block";
        }
    }

    function loadExample(pageNum) {
        const examples = {
            1: `Original: "Worked on website development"

Improved: "Collaborated with 4-person team to design and develop responsive e-commerce website using React and Node.js, improving mobile user experience and increasing conversion rate by 30%"

Why I picked this: This version is honest about my role (collaborated, not led), includes specific technologies I used, and has a real metric from our analytics. The 30% increase is accurate based on our A/B testing data. It's bold enough to stand out but conservative enough that I can defend every claim in an interview.`,

            2: `Question: Tell me about a time you failed

My Answer: During my junior year, I was leading a team project to build a student portfolio platform. I got excited about adding features and didn't properly plan our sprint timelines. Two weeks before the deadline, we realized we had built too many incomplete features instead of focusing on core functionality. The site was buggy and missing key features. I called an emergency team meeting, and we honestly assessed what we could finish. We cut 40% of features, focused on making the remaining ones solid, and delivered a working product that met the original requirements. I learned to prioritize core features first and get team buy-in before adding scope. In my next project, I used agile methodology properly and we delivered early.

What I would improve: Add specific numbers (how many features exactly, team size, actual deadline date). Mention what specifically was buggy. Could strengthen the "result" by adding what grade we got or client feedback. Remove "got excited" and replace with more professional language like "prioritized feature quantity over quality."`,

            3: `Task where AI helped: Writing documentation for our Flask API endpoints. I pasted my route code and asked AI to generate OpenAPI documentation. It saved me 2+ hours of manual work and caught inconsistencies in my parameter descriptions. The AI understood the code structure and created properly formatted docs I could import directly into Swagger.

Why it helped: This is a perfect AI use case - it's pattern matching and reformatting, not creating anything requiring judgment. The code was the source of truth, so the AI couldn't hallucinate incorrect info.

Task where you shouldn't use AI: Calculating load-bearing requirements for a robotics arm in our engineering project. This requires precise physics calculations, safety margins, and real-world material properties. An AI might confidently give wrong numbers that could cause mechanical failure or safety issues.

Why not: Engineering calculations need 100% accuracy and domain expertise. AI can't account for all real-world factors, and mistakes could be dangerous. This requires a licensed engineer or professor review.`
        };

        const textarea = document.getElementById('submit-prompt-' + pageNum);
        textarea.value = examples[pageNum] || '';

        const statusDiv = document.getElementById('status-' + pageNum);
        statusDiv.textContent = "Example loaded! Edit as needed then save.";
        statusDiv.style.backgroundColor = "#d1ecf1";
        statusDiv.style.color = "#0c5460";
        statusDiv.style.borderColor = "#17a2b8";
        statusDiv.style.display = "block";
        setTimeout(() => statusDiv.style.display = "none", 3000);
    }

    function loadSubmissions() {
        for (let i = 1; i <= 3; i++) {
            try {
                const saved = localStorage.getItem('ai-submodule-3-page-' + i);
                if (saved) {
                    const data = JSON.parse(saved);
                    const textarea = document.getElementById('submit-prompt-' + i);
                    if (textarea) {
                        textarea.value = data.content;
                    }
                }
            } catch (error) {
                console.error('Error loading page ' + i, error);
            }
        }
    }

    document.addEventListener('DOMContentLoaded', function() {
        showPage(1);
        loadSubmissions();
    });

    // Save completion status
    localStorage.setItem('ai-submodule-3-completed', 'true');
</script>


