---
layout: opencs
title: Solitaire Game
permalink: /solitaire/
---

<!-- Here is the styling -->
<style>
{{ '@import "beasts/inline/pages/hacks-solitaire-1";' | scssify }}
</style>

<!-- Here is the HTML body -->

<h2 class="game-title">Solitaire</h2>
<div class="container">
    <div class="container bg-secondary" style="text-align:center; border-radius: 12px; padding: 20px; box-shadow: 0 4px 12px rgba(0,0,0,0.3);">
        <!-- Main Menu -->
        <div id="menu" class="py-4 text-light fade-in">
            <p class="intro-text">Welcome to <strong>Klondike Solitaire</strong></p>
            <p class="sub-text">Move all cards to the foundation piles, organized by suit from Ace to King</p>
            <a id="new_game" class="menu-link">➕ New Game</a>
            <a id="instructions" class="menu-link">📖 How to Play</a>
        </div>
        <!-- Game Over -->
        <div id="gameover" class="py-4 text-light fade-in">
            <p class="gameover-title">💀 Game Over!</p>
            <p id="final_score" class="result-text">Final Score: 0</p>
            <p id="final_time" class="result-text">Time: 00:00</p>
            <a id="new_game1" class="menu-link">🔄 New Game</a>
            <a id="menu_return" class="menu-link">🏠 Main Menu</a>
        </div>
        <!-- Game Screen -->
        <div id="game_screen" class="game-container wrap" tabindex="1">
            <div class="game-controls">
                <div class="score-display">⭐ Score: <span id="score_value">0</span></div>
                <div class="timer-display">⏱ Time: <span id="timer_value">00:00</span></div>
                <div class="game-buttons">
                    <button id="hint_btn" class="btn-control">💡 Hint</button>
                    <button id="undo_btn" class="btn-control">↩ Undo</button>
                    <button id="restart_btn" class="btn-control">🔄 Restart</button>
                </div>
            </div>
            <div class="foundation-row">
                <div id="stock" class="card-pile stock-pile" data-pile="stock"></div>
                <div id="waste" class="card-pile waste-pile empty" data-pile="waste"></div>
                <div class="card-pile empty"></div>
                <div id="foundation_0" class="card-pile foundation" data-pile="foundation" data-index="0"></div>
                <div id="foundation_1" class="card-pile foundation" data-pile="foundation" data-index="1"></div>
                <div id="foundation_2" class="card-pile foundation" data-pile="foundation" data-index="2"></div>
                <div id="foundation_3" class="card-pile foundation" data-pile="foundation" data-index="3"></div>
            </div>
            <div class="game-board">
                <div id="tableau_0" class="card-pile tableau-pile" data-pile="tableau" data-index="0"></div>
                <div id="tableau_1" class="card-pile tableau-pile" data-pile="tableau" data-index="1"></div>
                <div id="tableau_2" class="card-pile tableau-pile" data-pile="tableau" data-index="2"></div>
                <div id="tableau_3" class="card-pile tableau-pile" data-pile="tableau" data-index="3"></div>
                <div id="tableau_4" class="card-pile tableau-pile" data-pile="tableau" data-index="4"></div>
                <div id="tableau_5" class="card-pile tableau-pile" data-pile="tableau" data-index="5"></div>
                <div id="tableau_6" class="card-pile tableau-pile" data-pile="tableau" data-index="6"></div>
            </div>
            <div id="win_message" class="win-message bounce-in">
                <h3>🎉 Congratulations!</h3>
                <p>You Won!</p>
                <p id="win_score"></p>
                <p id="win_time"></p>
                <button id="play_again_btn" class="btn-control">Play Again</button>
            </div>
        </div>
    </div>
    <div id="instructions_modal" class="modal" style="display: none;">
        <div class="modal-content slide-down">
            <span class="close">&times;</span>
            <h3>📖 How to Play Klondike Solitaire</h3>
            <div class="instructions-container">
                <h4>Objective</h4>
                <p class="highlight-box">
                    Move all cards to the four foundation piles, building each suit in ascending order from Ace to King.
                </p>
                <h4>Game Layout</h4>
                <ul>
                    <li><strong>Tableau:</strong> Seven piles where you build descending sequences of alternating colors</li>
                    <li><strong>Foundations:</strong> Four piles where you build ascending sequences by suit (Ace to King)</li>
                    <li><strong>Stock:</strong> The deck of remaining cards (click to draw)</li>
                    <li><strong>Waste:</strong> Where drawn cards from the stock are placed</li>
                </ul>
                <h4>Rules</h4>
                <ul>
                    <li>Only Kings can be placed on empty tableau piles</li>
                    <li>Build tableau piles in descending order (King to Ace) with alternating colors</li>
                    <li>Build foundation piles in ascending order (Ace to King) by suit</li>
                    <li>You can move face-up cards from one tableau pile to another</li>
                    <li>You can move cards from the waste pile to tableau or foundation piles</li>
                    <li>Click the stock pile to draw new cards</li>
                    <li>When the stock is empty, you can reset it from the waste pile</li>
                </ul>
                <h4>Scoring</h4>
                <ul>
                    <li>+5 points for each card moved to tableau</li>
                    <li>+10 points for each card moved to foundation</li>
                    <li>+5 points for turning over a face-down card in tableau</li>
                </ul>
                <h4>Controls</h4>
                <ul>
                    <li><strong>Click:</strong> Select and move cards (or draw from stock)</li>
                    <li><strong>Drag & Drop:</strong> Move cards between piles</li>
                    <li><strong>Hint Button:</strong> Get a suggestion for a move</li>
                    <li><strong>Undo Button:</strong> Reverse your last move</li>
                    <li><strong>Restart Button:</strong> Start a new game</li>
                </ul>
            </div>
        </div>
    </div>
</div>

<!-- Single module entry point -->
<script type="module" src="/assets/js/solitaire/main.js"></script>

<style>
{{ '@import "beasts/inline/pages/hacks-solitaire-2";' | scssify }}
</style>

