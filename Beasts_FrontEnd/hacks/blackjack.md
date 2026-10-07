---
layout: opencs
title: Blackjack Card Game
permalink: /javascript/project/blackjack
---

<style>
{{ '@import "beasts/inline/pages/hacks-blackjack-1";' | scssify }}
</style>

<h2>Blackjack</h2>
<p>Dealer hits on 16</p>

<div id="game-container">
    <div id="dealer-area" class="player-area">
        <h2>Dealer's Hand: <span id="dealer-score">0</span></h2>
        <div class="hand-container">
            <div id="dealer-cards" class="cards-container"></div>
            <div id="dealer-points" class="points-list"></div>
        </div>
    </div>
    <div id="player-area" class="player-area">
        <h2>Your Hand: <span id="player-score">0</span></h2>
        <div class="hand-container">
            <div id="player-cards" class="cards-container"></div>
            <div id="player-points" class="points-list"></div>
        </div>
    </div>
    <div id="game-controls">
        <button id="new-game-btn">New Game</button>
        <button id="hit-btn">Hit</button>
        <button id="stand-btn">Stand</button>
    </div>
    <p id="message"></p>
</div>

<script>
const dealerCardsEl = document.getElementById("dealer-cards");
const playerCardsEl = document.getElementById("player-cards");
const dealerScoreEl = document.getElementById("dealer-score");
const playerScoreEl = document.getElementById("player-score");
const messageEl = document.getElementById("message");

const newGameBtn = document.getElementById("new-game-btn");
const hitBtn = document.getElementById("hit-btn");
const standBtn = document.getElementById("stand-btn");

let deck = [];
let playerHand = [];
let dealerHand = [];
let gameOver = false;

function createDeck() {
    const suits = ["♠", "♥", "♦", "♣"];
    const values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"];
    let newDeck = [];
    for (let suit of suits) {
        for (let value of values) newDeck.push({value, suit});
    }
    return shuffle(newDeck);
}

function shuffle(deck) {
    for (let i = deck.length -1; i > 0; i--) {
        const j = Math.floor(Math.random()*(i+1));
        [deck[i], deck[j]] = [deck[j], deck[i]];
    }
    return deck;
}

function getCardValue(card) {
    if (["J","Q","K"].includes(card.value)) return 10;
    if (card.value === "A") return 11;
    return parseInt(card.value);
}

function calculateHand(hand) {
    let value = 0, aceCount = 0;
    for (let card of hand) {
        value += getCardValue(card);
        if (card.value === "A") aceCount++;
    }
    while (value > 21 && aceCount > 0) { value -= 10; aceCount--; }
    return value;
}

function renderHand(hand, container, pointsContainer) {
    container.innerHTML = "";
    pointsContainer.innerHTML = "";
    for (let card of hand) {
        const cardEl = document.createElement("div");
        cardEl.classList.add("card");
        cardEl.textContent = `${card.value}${card.suit}`;
        cardEl.style.color = (card.suit==="♥"||card.suit==="♦")?"red":"black";
        container.appendChild(cardEl);
    }
    pointsContainer.textContent = calculateHand(hand);
}

function renderDealerInitial() {
    dealerCardsEl.innerHTML = "";
    const firstCard = dealerHand[0];
    const secondCard = dealerHand[1];

    // First card
    const cardEl1 = document.createElement("div");
    cardEl1.classList.add("card");
    cardEl1.textContent = `${firstCard.value}${firstCard.suit}`;
    cardEl1.style.color = (firstCard.suit==="♥"||firstCard.suit==="♦")?"red":"black";
    dealerCardsEl.appendChild(cardEl1);

    // Hidden second card
    const cardEl2 = document.createElement("div");
    cardEl2.classList.add("card");
    cardEl2.textContent = "🂠";
    dealerCardsEl.appendChild(cardEl2);

    document.getElementById("dealer-points").textContent = getCardValue(firstCard);
}

function updateScores() {
    dealerScoreEl.textContent = calculateHand(dealerHand);
    playerScoreEl.textContent = calculateHand(playerHand);
}

function checkGameOver() {
    const playerValue = calculateHand(playerHand);
    const dealerValue = calculateHand(dealerHand);

    if (playerValue > 21) {
        messageEl.textContent = "You busted! Dealer wins.";
        gameOver = true;
    } else if (dealerValue > 21) {
        messageEl.textContent = "Dealer busted! You win!";
        gameOver = true;
    } else if (gameOver) {
        if (playerValue > dealerValue) messageEl.textContent = "You win!";
        else if (dealerValue > playerValue) messageEl.textContent = "Dealer wins!";
        else messageEl.textContent = "It's a tie!";
    }
}

function newGame() {
    deck = createDeck();
    playerHand = [deck.pop(), deck.pop()];
    dealerHand = [deck.pop(), deck.pop()];
    gameOver = false;

    renderHand(playerHand, playerCardsEl, document.getElementById("player-points"));
    renderDealerInitial();
    messageEl.textContent = "Game started. Your move!";
}

function hit() {
    if (gameOver) return;
    playerHand.push(deck.pop());
    renderHand(playerHand, playerCardsEl, document.getElementById("player-points"));
    if (calculateHand(playerHand) > 21) checkGameOver();
}

function stand() {
    if (gameOver) return;

    // Reveal dealer hidden card
    dealerCardsEl.children[1].textContent = `${dealerHand[1].value}${dealerHand[1].suit}`;
    dealerCardsEl.children[1].style.color = (dealerHand[1].suit==="♥"||dealerHand[1].suit==="♦") ? "red" : "black";

    // Recalculate dealer total after hidden card
    document.getElementById("dealer-points").textContent = calculateHand(dealerHand);

    // Dealer draws until 17 or more
    while (calculateHand(dealerHand) < 17) {
        const card = deck.pop();
        dealerHand.push(card);
        const cardEl = document.createElement("div");
        cardEl.classList.add("card");
        cardEl.textContent = `${card.value}${card.suit}`;
        cardEl.style.color = (card.suit==="♥"||card.suit==="♦")?"red":"black";
        dealerCardsEl.appendChild(cardEl);
        document.getElementById("dealer-points").textContent = calculateHand(dealerHand);
    }

    // Update final score
    updateScores();
    gameOver = true;
    checkGameOver();
}

newGameBtn.addEventListener("click", newGame);
hitBtn.addEventListener("click", hit);
standBtn.addEventListener("click", stand);
</script>
