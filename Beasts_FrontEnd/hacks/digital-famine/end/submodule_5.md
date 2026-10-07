---
layout: post
title: "Knowledge Restoration Protocol"
description: "Final End Quest game: Restore Earth's digital knowledge across multiple domains"
permalink: /digital-famine/end/submodule_5/
parent: "End Quest"
team: "CodeMaxxers"
submodule: 5
microblog: True
categories: [CSP, Submodule, End]
tags: [end, submodule, codemaxxers]
author: "Evan Svetina"
microblog: true
date: 2025-10-29
---

# Knowledge Restoration Protocol

## Restore Earth's Digital Wisdom

<style>
{{ '@import "beasts/inline/pages/hacks-digital-famine-end-submodule-5-1";' | scssify }}
</style>

<div class="knowledge-game">
    <div class="game-header">
        <h2>🌍 Knowledge Restoration Protocol 🌍</h2>
        <p style="font-size: 18px;">Help restore Earth's lost digital knowledge by answering questions about essential 21st century skills!</p>
        <div class="knowledge-meter">
            <div class="knowledge-fill" id="progressBar" style="width: 0%">0%</div>
        </div>
        <div class="score-display">
            Knowledge Restored: <span id="score">0</span> / <span id="total">12</span>
        </div>
    </div>

    <div id="startScreen" class="question-card">
        <h3>Mission Briefing</h3>
        <p>Welcome back to Earth, brave explorer! The digital knowledge of our civilization has been fragmented. You must answer questions across four critical domains to restore humanity's wisdom:</p>
        <div style="margin: 20px 0;">
            <span class="category-badge cybersecurity">Cybersecurity</span>
            <span class="category-badge media-literacy">Media Literacy</span>
            <span class="category-badge ai-skills">AI Skills</span>
            <span class="category-badge microblogging">Microblogging</span>
        </div>
        <p>Each correct answer restores a piece of lost knowledge. Can you achieve 100% restoration?</p>
        <button class="start-btn" onclick="startGame()">Begin Restoration</button>
    </div>

    <div id="questionScreen" class="question-card" style="display: none;">
        <div id="categoryDisplay" style="margin-bottom: 15px;"></div>
        <h3 id="questionNumber" style="color: #667eea;">Question 1 of 12</h3>
        <p id="questionText" style="font-size: 18px; margin: 20px 0;"></p>
        <div id="answersContainer"></div>
        <div id="explanation" class="explanation"></div>
        <button id="nextBtn" class="next-btn" style="display: none;" onclick="nextQuestion()">Next Question</button>
    </div>

    <div id="completionScreen" class="completion-screen" style="display: none;">
        <div class="trophy">🏆</div>
        <h2 id="finalMessage"></h2>
        <p id="finalScore" style="font-size: 20px; margin: 20px 0;"></p>
        <div id="knowledgeReport" style="text-align: left; background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;"></div>
        <button class="certificate-btn" onclick="showCertificate()">View Your Certificate</button>
    </div>

    <div id="certificateScreen" class="certificate-container" style="display: none;">
        <div class="certificate">
            <div class="certificate-border">
                <div class="certificate-content">
                    <div class="certificate-seal">🌍</div>
                    <h1 class="certificate-title">Certificate of Digital Excellence</h1>
                    <div class="certificate-subtitle">This certifies that</div>
                    <div class="certificate-recipient">YOU</div>
                    <div class="certificate-text">
                        has successfully<br>
                        <strong>Saved the Earth</strong><br>
                        and restored its knowledge, while become more educated along the way!
                    </div>
                    <div class="certificate-skills">
                        <div class="skill-badge">✓ Cybersecurity Expert</div>
                        <div class="skill-badge">✓ Media Literacy Master</div>
                        <div class="skill-badge">✓ AI Skills Specialist</div>
                        <div class="skill-badge">✓ Microblogging Professional</div>
                    </div>
                    <div class="certificate-achievement" id="certificateAchievement"></div>
                    <div class="certificate-date" id="certificateDate"></div>
                    <div class="certificate-footer">
                        <div class="signature">
                            <div class="signature-line"></div>
                            <div>CodeMaxxers Team</div>
                        </div>
                        <div class="signature">
                            <div class="signature-line"></div>
                            <div>Earth Digital Council</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <button class="back-btn" onclick="backToCompletion()">← Back to Results</button>
    </div>
</div>

<script>
const questions = [
    // Cybersecurity Questions
    {
        id: 'cyber1',
        category: "cybersecurity",
        question: "What is the MOST secure type of password?",
        answers: [
            "Your birthday and name",
            "A long passphrase with random words",
            "Password123!",
            "The same password for all accounts"
        ],
        correct: 1,
        explanation: "Passphrases like 'correct-horse-battery-staple' are both secure and memorable. They're long, random, and hard to crack!"
    },
    {
        id: 'cyber2',
        category: "cybersecurity",
        question: "You receive an email from 'your bank' asking you to click a link and verify your account. What should you do?",
        answers: [
            "Click the link immediately",
            "Reply with your account information",
            "Delete it and contact your bank directly",
            "Forward it to all your contacts"
        ],
        correct: 2,
        explanation: "This is likely a phishing attempt. Never click suspicious links. Always verify by contacting your bank through official channels."
    },
    {
        id: 'cyber3',
        category: "cybersecurity",
        question: "What does 'two-factor authentication' (2FA) require?",
        answers: [
            "Two different passwords",
            "Something you know + something you have",
            "Two email addresses",
            "Two security questions"
        ],
        correct: 1,
        explanation: "2FA combines something you know (password) with something you have (phone, authenticator app, etc.) for extra security."
    },
    
    // Media Literacy Questions
    {
        id: 'media1',
        category: "media-literacy",
        question: "What is the BEST way to verify if a news story is true?",
        answers: [
            "Check if it has lots of shares",
            "See if your friends believe it",
            "Cross-reference multiple reputable sources",
            "Trust it if it confirms your beliefs"
        ],
        correct: 2,
        explanation: "Always verify information by checking multiple reliable sources. Popularity doesn't equal truth!"
    },
    {
        id: 'media2',
        category: "media-literacy",
        question: "What is 'confirmation bias' in media consumption?",
        answers: [
            "Confirming your email subscription",
            "Only believing information that supports your existing views",
            "Fact-checking everything you read",
            "Confirming the author's credentials"
        ],
        correct: 1,
        explanation: "Confirmation bias makes us favor information that confirms what we already believe, leading to echo chambers."
    },
    {
        id: 'media3',
        category: "media-literacy",
        question: "Which is a red flag that an image might be digitally manipulated?",
        answers: [
            "High resolution quality",
            "Inconsistent lighting or shadows",
            "Professional photography",
            "Presence of watermarks"
        ],
        correct: 1,
        explanation: "Inconsistent lighting, shadows, or perspectives often reveal digital manipulation or AI-generated images."
    },
    
    // AI Skills Questions
    {
        id: 'ai1',
        category: "ai-skills",
        question: "What is a 'prompt' in the context of AI tools?",
        answers: [
            "An error message",
            "The instructions you give to an AI",
            "The AI's response time",
            "A type of AI model"
        ],
        correct: 1,
        explanation: "A prompt is your input or instructions to an AI system. Better prompts lead to better AI outputs!"
    },
    {
        id: 'ai2',
        category: "ai-skills",
        question: "What should you always remember about AI-generated content?",
        answers: [
            "It's always 100% accurate",
            "It should be verified and may contain errors",
            "It's illegal to use",
            "It can replace all human work"
        ],
        correct: 1,
        explanation: "AI can make mistakes or 'hallucinate' information. Always verify important AI-generated content!"
    },
    {
        id: 'ai3',
        category: "ai-skills",
        question: "Which is an ethical consideration when using AI image generators?",
        answers: [
            "Using them is always unethical",
            "They use no computational resources",
            "Respecting artists' rights and attribution",
            "They can only create abstract art"
        ],
        correct: 2,
        explanation: "AI art raises questions about copyright, artist attribution, and the use of training data. Use responsibly!"
    },
    
    // Microblogging Questions
    {
        id: 'micro1',
        category: "microblogging",
        question: "What is the PRIMARY purpose of hashtags in microblogging?",
        answers: [
            "To make posts look professional",
            "To categorize and discover content",
            "To increase word count",
            "To replace punctuation"
        ],
        correct: 1,
        explanation: "Hashtags help categorize content and make it discoverable by people interested in specific topics."
    },
    {
        id: 'micro2',
        category: "microblogging",
        question: "What is 'engagement' in social media context?",
        answers: [
            "Getting married online",
            "Likes, comments, shares, and interactions",
            "The time you spend online",
            "Number of followers only"
        ],
        correct: 1,
        explanation: "Engagement measures how people interact with content through likes, comments, shares, and other actions."
    },
    {
        id: 'micro3',
        category: "microblogging",
        question: "Why is it important to fact-check before sharing content on social media?",
        answers: [
            "To get more followers",
            "To prevent spread of misinformation",
            "To make posts longer",
            "It's not important"
        ],
        correct: 1,
        explanation: "Sharing false information can harm others and damage your credibility. Always verify before you amplify!"
    }
];

let remainingQuestions = [];
let correctlyAnswered = new Set();
let currentQuestion = null;
let answered = false;
let totalQuestionsAsked = 0;
let incorrectAttempts = 0;

function startGame() {
    // Reset game state
    remainingQuestions = [...questions];
    correctlyAnswered = new Set();
    totalQuestionsAsked = 0;
    incorrectAttempts = 0;
    answered = false;
    
    // Update UI
    document.getElementById('startScreen').style.display = 'none';
    document.getElementById('completionScreen').style.display = 'none';
    document.getElementById('questionScreen').style.display = 'block';
    
    // Update score display
    updateScoreDisplay();
    
    // Load first question
    loadQuestion();
}

function updateScoreDisplay() {
    document.getElementById('score').textContent = correctlyAnswered.size;
    document.getElementById('total').textContent = questions.length;
    updateProgress();
}

function loadQuestion() {
    answered = false;
    
    // Check if all questions are answered correctly
    if (correctlyAnswered.size === questions.length) {
        showCompletion();
        return;
    }
    
    // Get next question from remaining questions
    if (remainingQuestions.length === 0) {
        // All questions have been asked, but some were wrong
        // Reset remaining questions to only include the ones answered incorrectly
        remainingQuestions = questions.filter(q => !correctlyAnswered.has(q.id));
        
        // Show feedback that we're retrying missed questions
        const retryMessage = document.createElement('div');
        retryMessage.style.cssText = 'background: rgba(124, 58, 237, 0.2); padding: 15px; border-radius: 8px; margin-bottom: 20px; color: #a78bfa; text-align: center;';
        retryMessage.innerHTML = `📝 Retrying ${remainingQuestions.length} missed question${remainingQuestions.length > 1 ? 's' : ''}...`;
        
        const questionCard = document.getElementById('questionScreen');
        const existingRetry = questionCard.querySelector('.retry-message');
        if (existingRetry) existingRetry.remove();
        
        retryMessage.className = 'retry-message';
        questionCard.insertBefore(retryMessage, questionCard.firstChild);
    }
    
    // Pick a random question from remaining
    const randomIndex = Math.floor(Math.random() * remainingQuestions.length);
    currentQuestion = remainingQuestions[randomIndex];
    remainingQuestions.splice(randomIndex, 1);
    
    totalQuestionsAsked++;
    
    // Update question number - show progress through all questions
    document.getElementById('questionNumber').textContent = 
        `Progress: ${correctlyAnswered.size} / ${questions.length} Mastered`;
    
    // Show category
    const categoryColors = {
        'cybersecurity': 'cybersecurity',
        'media-literacy': 'media-literacy',
        'ai-skills': 'ai-skills',
        'microblogging': 'microblogging'
    };
    
    document.getElementById('categoryDisplay').innerHTML = 
        `<span class="category-badge ${categoryColors[currentQuestion.category]}">${currentQuestion.category.replace('-', ' ')}</span>`;
    
    // Show question
    document.getElementById('questionText').textContent = currentQuestion.question;
    
    // Show answers (shuffle them for variety)
    const answersContainer = document.getElementById('answersContainer');
    answersContainer.innerHTML = '';
    
    // Create array of answer indices and shuffle
    const indices = [0, 1, 2, 3];
    const shuffled = indices.sort(() => Math.random() - 0.5);
    
    shuffled.forEach((originalIndex) => {
        const button = document.createElement('button');
        button.className = 'answer-btn';
        button.textContent = currentQuestion.answers[originalIndex];
        button.dataset.originalIndex = originalIndex;
        button.onclick = () => selectAnswer(originalIndex);
        answersContainer.appendChild(button);
    });
    
    // Hide explanation and next button
    document.getElementById('explanation').classList.remove('show');
    document.getElementById('nextBtn').style.display = 'none';
}

function selectAnswer(selectedIndex) {
    if (answered) return;
    answered = true;
    
    const buttons = document.querySelectorAll('.answer-btn');
    
    // Disable all buttons
    buttons.forEach(btn => btn.style.cursor = 'not-allowed');
    
    // Find the button that was clicked and the correct button
    let clickedButton, correctButton;
    buttons.forEach(btn => {
        const idx = parseInt(btn.dataset.originalIndex);
        if (idx === selectedIndex) clickedButton = btn;
        if (idx === currentQuestion.correct) correctButton = btn;
    });
    
    // Show correct/incorrect
    if (selectedIndex === currentQuestion.correct) {
        clickedButton.classList.add('correct');
        correctlyAnswered.add(currentQuestion.id);
        updateScoreDisplay();
        
        // Show success message
        const explanationDiv = document.getElementById('explanation');
        explanationDiv.innerHTML = `<strong>✅ Correct!</strong> ${currentQuestion.explanation}`;
        explanationDiv.classList.add('show');
    } else {
        clickedButton.classList.add('incorrect');
        correctButton.classList.add('correct');
        incorrectAttempts++;
        
        // Show explanation with retry notice
        const explanationDiv = document.getElementById('explanation');
        explanationDiv.innerHTML = `<strong>❌ Not quite!</strong> ${currentQuestion.explanation}<br><br><em>This question will appear again later.</em>`;
        explanationDiv.classList.add('show');
        
        // Add question back to the pool if not already there
        if (!remainingQuestions.some(q => q.id === currentQuestion.id)) {
            remainingQuestions.push(currentQuestion);
        }
    }
    
    // Show next button
    document.getElementById('nextBtn').style.display = 'block';
    document.getElementById('nextBtn').textContent = 
        correctlyAnswered.size === questions.length ? 'Complete Mission!' : 'Next Question';
}

function nextQuestion() {
    if (correctlyAnswered.size === questions.length) {
        showCompletion();
    } else {
        loadQuestion();
    }
}

function updateProgress() {
    const progress = Math.round((correctlyAnswered.size / questions.length) * 100);
    const progressBar = document.getElementById('progressBar');
    progressBar.style.width = progress + '%';
    progressBar.textContent = progress + '%';
}

function showCompletion() {
    document.getElementById('questionScreen').style.display = 'none';
    document.getElementById('completionScreen').style.display = 'block';
    
    // Calculate efficiency
    const efficiency = Math.round((questions.length / totalQuestionsAsked) * 100);
    
    let message, emoji;
    if (incorrectAttempts === 0) {
        message = "PERFECT! Flawless Knowledge Restoration!";
        emoji = "🌟";
    } else if (incorrectAttempts <= 3) {
        message = "EXCELLENT! Complete Knowledge Restored!";
        emoji = "✨";
    } else {
        message = "SUCCESS! All Knowledge Restored!";
        emoji = "🎯";
    }
    
    document.getElementById('finalMessage').innerHTML = `${emoji} ${message} ${emoji}`;
    document.getElementById('finalScore').innerHTML = 
        `You mastered all ${questions.length} knowledge fragments!<br>
        Total attempts: ${totalQuestionsAsked} (${efficiency}% efficiency)`;
    
    // Store achievement for certificate
    window.gameAchievement = {
        efficiency: efficiency,
        incorrectAttempts: incorrectAttempts,
        achievement: incorrectAttempts === 0 ? 'Perfect Scholar - No mistakes!' :
                    efficiency >= 75 ? 'Quick Learner - High efficiency!' :
                    'Persistent Guardian - Never gave up!'
    };
    
    // Generate detailed report
    const report = `
        <h4>Knowledge Recovery Report:</h4>
        <p>✅ <strong>Mission Complete!</strong> 100% of Earth's digital knowledge restored!</p>
        <p>📊 <strong>Performance Stats:</strong></p>
        <ul style="text-align: left; line-height: 1.8;">
            <li>Questions Mastered: ${questions.length} / ${questions.length}</li>
            <li>Total Attempts: ${totalQuestionsAsked}</li>
            <li>Incorrect Attempts: ${incorrectAttempts}</li>
            <li>Efficiency Rating: ${efficiency}%</li>
        </ul>
        <p style="margin-top: 20px;">🏆 <strong>Achievement Unlocked:</strong> ${window.gameAchievement.achievement}</p>
        <p><strong>Remember:</strong> These skills are essential for navigating our digital world safely and effectively!</p>
    `;
    
    document.getElementById('knowledgeReport').innerHTML = report;
}

function showCertificate() {
    document.getElementById('completionScreen').style.display = 'none';
    document.getElementById('certificateScreen').style.display = 'block';
    
    // Set certificate achievement text
    const achievementText = window.gameAchievement.achievement;
    document.getElementById('certificateAchievement').innerHTML = 
        `🏆 ${achievementText}`;
    
    // Set current date
    const today = new Date();
    const dateStr = today.toLocaleDateString('en-US', { 
        year: 'numeric', 
        month: 'long', 
        day: 'numeric' 
    });
    document.getElementById('certificateDate').innerHTML = 
        `Awarded on ${dateStr}`;
    
    // Scroll to top of certificate
    document.getElementById('certificateScreen').scrollIntoView({ behavior: 'smooth' });
}

function backToCompletion() {
    document.getElementById('certificateScreen').style.display = 'none';
    document.getElementById('completionScreen').style.display = 'block';
}

function restartGame() {
    document.getElementById('certificateScreen').style.display = 'none';
    startGame();
}

// Initialize
document.getElementById('score').textContent = '0';
document.getElementById('total').textContent = questions.length;
</script>

<script type="module">
  import { initEndModuleProgression } from '{{site.baseurl}}/assets/js/digitalFamine/endModuleProgression.js';
  
  // Initialize progression system for this module
  initEndModuleProgression();
</script>

*This educational game was created as part of the End Quest series by the CodeMaxxers team.*