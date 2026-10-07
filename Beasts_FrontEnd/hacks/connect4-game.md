---
layout: opencs
title: Connect 4
permalink: /connect4/play/
---

<div id="app" class="wrap">
  <!-- Start Screen -->
  <section id="start" class="card center">
    <h1 class="title">Connect 4</h1>
    <p class="muted">Choose a timer per player</p>
    <div class="row">
      <button class="btn" data-time="180">3 Minutes</button>
      <button class="btn" data-time="300">5 Minutes</button>
      <button class="btn" data-time="600">10 Minutes</button>
    </div>
    <p class="press">…or press <kbd>Enter</kbd> to start with 5:00</p>
  </section>

  <!-- Game Screen - Board Overlay -->
  <section id="game" class="hidden game-overlay">
    <div class="hud">
      <!-- Red panel -->
      <div class="panel red-side">
        <h2>Red</h2>
        <div class="timer" id="tRed">05:00</div>
        <div class="stash">
          <div class="dot red"></div>
          <span>Coins: <b id="cRed">21</b></span>
        </div>
      </div>
      <!-- Board -->
      <div id="boardWrap">
        <div id="board"></div>
        <!-- falling coin overlay -->
        <div id="fall" class="coin hidden"></div>
      </div>
      <!-- Yellow panel -->
      <div class="panel yellow-side">
        <h2>Yellow</h2>
        <div class="timer" id="tYellow">05:00</div>
        <div class="stash">
          <div class="dot yellow"></div>
          <span>Coins: <b id="cYellow">21</b></span>
        </div>
      </div>
    </div>
    <br>
    <br>
    <br>
    <div class="row center">
      <button id="restart" class="btn danger">Restart</button>
    </div>
  </section>
</div>

<!-- ========= Styles ========= -->
<style>
{{ '@import "beasts/inline/pages/hacks-connect4-game-1";' | scssify }}
</style>

<!-- ========= OOP Logic ========= -->
<script>
// ========= PLAYER CLASS =========
class Player {
  constructor(name, color) {
    this.name = name;
    this.color = color;
    this.time = 300; // default 5 minutes
    this.coins = 21;
  }

  setTime(seconds) {
    this.time = seconds;
  }

  usesCoin() {
    if (this.coins > 0) {
      this.coins--;
      return true;
    }
    return false;
  }

  hasTimeLeft() {
    return this.time > 0;
  }

  decrementTime() {
    if (this.time > 0) {
      this.time--;
    }
  }

  reset(timeInSeconds) {
    this.time = timeInSeconds;
    this.coins = 21;
  }
}

// ========= GAME BOARD CLASS =========
class GameBoard {
  constructor(rows = 6, cols = 7) {
    this.rows = rows;
    this.cols = cols;
    this.grid = [];
    this.initialize();
  }

  initialize() {
    this.grid = Array.from({length: this.rows}, () => Array(this.cols).fill(null));
  }

  isValidColumn(col) {
    return col >= 0 && col < this.cols && this.grid[0][col] === null;
  }

  getDropRow(col) {
    if (!this.isValidColumn(col)) return -1;
    
    for (let row = this.rows - 1; row >= 0; row--) {
      if (this.grid[row][col] === null) {
        return row;
      }
    }
    return -1;
  }

  placePiece(row, col, color) {
    if (row >= 0 && row < this.rows && col >= 0 && col < this.cols) {
      this.grid[row][col] = color;
      return true;
    }
    return false;
  }

  checkWin(row, col) {
    const color = this.grid[row][col];
    if (!color) return false;

    const directions = [
      [1, 0],   // vertical
      [0, 1],   // horizontal
      [1, 1],   // diagonal \
      [1, -1]   // diagonal /
    ];

    for (const [deltaRow, deltaCol] of directions) {
      let count = 1; // count the current piece

      // Check in both directions
      for (const direction of [-1, 1]) {
        let r = row + deltaRow * direction;
        let c = col + deltaCol * direction;

        while (
          r >= 0 && r < this.rows &&
          c >= 0 && c < this.cols &&
          this.grid[r][c] === color
        ) {
          count++;
          r += deltaRow * direction;
          c += deltaCol * direction;
        }
      }

      if (count >= 4) return true;
    }

    return false;
  }

  isFull() {
    return this.grid.every(row => row.every(cell => cell !== null));
  }

  reset() {
    this.initialize();
  }
}

// ========= TIMER CLASS =========
class GameTimer {
  constructor() {
    this.intervalId = null;
    this.onTick = null;
    this.onTimeUp = null;
  }

  start(tickCallback, timeUpCallback) {
    this.onTick = tickCallback;
    this.onTimeUp = timeUpCallback;
    
    this.intervalId = setInterval(() => {
      if (this.onTick) {
        this.onTick();
      }
    }, 1000);
  }

  stop() {
    if (this.intervalId) {
      clearInterval(this.intervalId);
      this.intervalId = null;
    }
  }

  reset() {
    this.stop();
  }
}

// ========= GAME UI CLASS =========
class GameUI {
  constructor() {
    this.elements = {
      start: document.getElementById('start'),
      game: document.getElementById('game'),
      boardWrap: document.getElementById('boardWrap'),
      board: document.getElementById('board'),
      fallCoin: document.getElementById('fall'),
      redTimer: document.getElementById('tRed'),
      yellowTimer: document.getElementById('tYellow'),
      redCoins: document.getElementById('cRed'),
      yellowCoins: document.getElementById('cYellow'),
      restartBtn: document.getElementById('restart')
    };
  }

  showStartScreen() {
    this.elements.start.classList.remove('hidden');
    this.elements.game.classList.add('hidden');
  }

  showGameScreen() {
    this.elements.start.classList.add('hidden');
    this.elements.game.classList.remove('hidden');
  }

  createBoard(rows, cols) {
    this.elements.board.innerHTML = '';
    for (let r = 0; r < rows; r++) {
      for (let c = 0; c < cols; c++) {
        const hole = document.createElement('div');
        hole.className = 'hole';
        hole.dataset.col = c;
        this.elements.board.appendChild(hole);
      }
    }
  }

  updateBoard(board) {
    const holes = [...this.elements.board.children];
    holes.forEach((hole, index) => {
      const row = Math.floor(index / board.cols);
      const col = index % board.cols;
      const piece = board.grid[row][col];
      
      hole.classList.remove('filled', 'red', 'yellow');
      if (piece) {
        hole.classList.add('filled', piece);
      }
    });
  }

  updatePlayerInfo(redPlayer, yellowPlayer) {
    this.elements.redTimer.textContent = this.formatTime(redPlayer.time);
    this.elements.yellowTimer.textContent = this.formatTime(yellowPlayer.time);
    this.elements.redCoins.textContent = redPlayer.coins;
    this.elements.yellowCoins.textContent = yellowPlayer.coins;
  }

  formatTime(seconds) {
    const minutes = Math.floor(Math.max(0, seconds) / 60);
    const secs = Math.max(0, seconds) % 60;
    return `${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
  }

  async animateFallingCoin(col, row, color) {
    const cellSize = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--cell'));
    const gap = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--gap'));
    const padding = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--boardPad'));
    
    const x = padding + col * (cellSize + gap);
    const y = padding + row * (cellSize + gap);
    
    this.elements.fallCoin.className = `coin ${color}`;
    this.elements.fallCoin.style.left = x + 'px';
    this.elements.fallCoin.style.transform = 'translate(0, -100%)';
    this.elements.fallCoin.classList.remove('hidden');
    
    // Force reflow
    void this.elements.fallCoin.offsetWidth;
    
    const duration = Math.min(120 + row * 120, 520);
    this.elements.fallCoin.style.transitionDuration = `${duration}ms`;
    this.elements.fallCoin.style.transform = `translate(0, ${y}px)`;
    
    return new Promise(resolve => {
      const onTransitionEnd = () => {
        this.elements.fallCoin.removeEventListener('transitionend', onTransitionEnd);
        this.elements.fallCoin.classList.add('hidden');
        resolve();
      };
      this.elements.fallCoin.addEventListener('transitionend', onTransitionEnd, {once: true});
    });
  }

  showWinMessage(message) {
    const winOverlay = document.createElement('div');
    winOverlay.className = 'win-overlay';
    winOverlay.innerHTML = `
      <div class="win-card">
        <h2 class="win-title">${message}</h2>
        <button class="btn win-btn" onclick="this.parentElement.parentElement.remove()">Continue</button>
      </div>
    `;
    document.body.appendChild(winOverlay);
  }
}

// ========= MAIN GAME CLASS =========
class Connect4Game {
  constructor() {
    this.board = new GameBoard(6, 7);
    this.redPlayer = new Player('Red', 'red');
    this.yellowPlayer = new Player('Yellow', 'yellow');
    this.currentPlayer = this.redPlayer;
    this.timer = new GameTimer();
    this.ui = new GameUI();
    this.isRunning = false;
    this.isAnimating = false;
    
    this.initializeEventListeners();
  }

  initializeEventListeners() {
    // Start screen buttons
    this.ui.elements.start.querySelectorAll('.btn').forEach(button => {
      button.addEventListener('click', () => {
        const timeInSeconds = parseInt(button.dataset.time);
        this.startGame(timeInSeconds);
      });
    });

    // Enter key for default time
    window.addEventListener('keydown', (e) => {
      if (!this.ui.elements.game.classList.contains('hidden') || e.key !== 'Enter') return;
      this.startGame(300);
    });

    // Board clicks
    this.ui.elements.board.addEventListener('click', (e) => {
      this.handleBoardClick(e);
    });

    // Restart button
    this.ui.elements.restartBtn.addEventListener('click', () => {
      this.restart();
    });
  }

  startGame(timeInSeconds) {
    // Reset game state
    this.board.reset();
    this.redPlayer.reset(timeInSeconds);
    this.yellowPlayer.reset(timeInSeconds);
    this.currentPlayer = this.redPlayer;
    this.isRunning = true;
    this.isAnimating = false;

    // Setup UI
    this.ui.showGameScreen();
    this.ui.createBoard(this.board.rows, this.board.cols);
    this.ui.updateBoard(this.board);
    this.ui.updatePlayerInfo(this.redPlayer, this.yellowPlayer);

    // Start timer
    this.timer.start(
      () => this.handleTimerTick(),
      (player) => this.handleTimeUp(player)
    );
  }

  async handleBoardClick(event) {
    const hole = event.target.closest('.hole');
    if (!hole || !this.isRunning || this.isAnimating) return;

    const col = parseInt(hole.dataset.col);
    const row = this.board.getDropRow(col);
    
    if (row < 0) return; // Column is full
    if (!this.currentPlayer.usesCoin()) return; // No coins left

    this.isAnimating = true;

    // Animate the falling coin
    await this.ui.animateFallingCoin(col, row, this.currentPlayer.color);

    // Place the piece on the board
    this.board.placePiece(row, col, this.currentPlayer.color);
    
    // Update UI
    this.ui.updateBoard(this.board);
    this.ui.updatePlayerInfo(this.redPlayer, this.yellowPlayer);

    this.isAnimating = false;

    // Check for win or draw
    if (this.board.checkWin(row, col)) {
      this.endGame(`${this.currentPlayer.name} wins!`);
      return;
    }

    if (this.board.isFull()) {
      this.endGame('Draw!');
      return;
    }

    // Switch players
    this.switchPlayer();
  }

  handleTimerTick() {
    if (!this.isRunning) return;
    
    this.currentPlayer.decrementTime();
    
    if (!this.currentPlayer.hasTimeLeft()) {
      const winner = this.currentPlayer === this.redPlayer ? this.yellowPlayer : this.redPlayer;
      this.endGame(`${winner.name} wins on time!`);
      return;
    }

    this.ui.updatePlayerInfo(this.redPlayer, this.yellowPlayer);
  }

  switchPlayer() {
    this.currentPlayer = this.currentPlayer === this.redPlayer ? this.yellowPlayer : this.redPlayer;
  }

  endGame(message) {
    this.isRunning = false;
    this.timer.stop();
    this.ui.showWinMessage(message);
  }

  restart() {
    this.timer.stop();
    this.ui.showStartScreen();
    this.isRunning = false;
  }
}

// ========= INITIALIZE GAME =========
(() => {
  const game = new Connect4Game();
})();
</script>