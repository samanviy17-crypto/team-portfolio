---
layout: post
author: Nikhil, Rohan, Pranav, Aditya, Shriya, Samhita
permalink: /breakout
---


<style>
{{ '@import "beasts/inline/pages/hacks-breakout-breakout-1";' | scssify }}
</style>


<div class="lesson-hub">
    <h1 class="hub-title">🎮 Breakout Game Learning Hub</h1>
    <p class="hub-subtitle">
        Master game development through two comprehensive learning paths. Start with functional programming fundamentals, then advance to object-oriented design patterns.
    </p>

    <div class="cards-container">
        <!-- Card 1: Functional Breakout -->
        <div class="lesson-card">
            <div class="difficulty-badge difficulty-beginner">Beginner</div>
            <div class="card-header">
                <h2 class="card-title">🛠️ Functional Breakout</h2>
                <p class="card-description">
                    Learn the fundamentals of game development using functional programming. Build your breakout game step-by-step with interactive demos and hands-on coding.
                </p>
            </div>
           
            <ul class="card-features">
                <li>Paddle movement and controls</li>
                <li>Ball physics and bouncing</li>
                <li>Power-ups and special effects</li>
                <li>Interactive quizzes and whiteboard</li>
            </ul>


            <div class="card-buttons">
                <a href="{{site.baseurl}}/functionalbreakoutlesson" class="btn btn-lesson">📚 Start Lessons</a>
                <a href="{{site.baseurl}}/functionalbreakoutgame" class="btn btn-game">🎮 Play Game</a>
            </div>
        </div>


        <!-- Card 2: OOP Breakout -->
        <div class="lesson-card">
            <div class="difficulty-badge difficulty-intermediate">Intermediate</div>
            <div class="card-header">
                <h2 class="card-title">🏗️ OOP Breakout</h2>
                <p class="card-description">
                    Advance to object-oriented programming principles. Learn inheritance, composition, and encapsulation while building a sophisticated breakout game.
                </p>
            </div>
           
            <ul class="card-features">
                <li>Classes and inheritance patterns</li>
                <li>GameObject composition</li>
                <li>Advanced game mechanics</li>
                <li>Code architecture and design</li>
            </ul>


            <div class="card-buttons">
                <a href="{{site.baseurl}}/oopbreakoutlesson" class="btn btn-lesson">📚 Start Lessons</a>
                <a href="{{site.baseurl}}/oopbreakoutgame" class="btn btn-game">🎮 Play Game</a>
            </div>
        </div>
    </div>


    <div style="text-align: center; margin-top: 50px; padding: 30px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); border-radius: 15px; color: white;">
        <h3 style="margin-bottom: 15px;">🎯 Learning Path Recommendation</h3>
        <p style="margin: 0; opacity: 0.9;">
            New to programming? Start with <strong>Functional Breakout</strong> to learn the basics.
            Ready for advanced concepts? Jump into <strong>OOP Breakout</strong> for sophisticated design patterns.
        </p>
    </div>
</div>

