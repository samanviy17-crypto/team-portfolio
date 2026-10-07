---
layout: cs-portfolio-lesson
title: "JavaScript Guide"
description: Guide on and how to code in JavaScript
permalink: /cs-portfolio-quest/frontend/submodule_5/
parent: "Frontend Development"
team: "Creators"
submodule: 5
microblog: True
breadcrumb: True
tags: [javascript]
author: "Creators Team"
date: 2025-10-21
---

<style>
{{ '@import "beasts/inline/pages/hacks-cs-portfolio-quest-frontend-submodule-5-1";' | scssify }}
</style>

# JavaScript Section

## Purpose

Considering you're on this section, you likely have learned that HTML is what structures website and CSS is what styles and adds design to websites. JavaScript add to this list: **It makes the website interactive.**

<br>

This guide will go over some of the most fundamental concepts relating to JavaScript.

## Variables

Variables are essentially how data is stored in usable containers in code.

There are 4 ways this can be done, but only two are recommended.

The first of these methods is **let**. It allows the variable to be changed after it is defined:

```
let x = 5;
x = 6; // Successfully changes value
```

The second of these methods is **const**. After the variable is defined, it cannot be changed:

```
const x = 5;
x = 6; // WILL NOT WORK
```

<div class="exercise-section">
  <h4>Checkpoint: Practice Variables</h4>
  <p>
    Define at least three variables using either let or const and initialize each variable with a different data type.
  </p>

  <textarea id="codeInput" class="code-input" placeholder="// Write your JavaScript code here..."></textarea>

  <div class="button-row">
    <button onclick="saveCode()">Save Code</button>
    <button onclick="loadCode()">Load Saved</button>
    <button onclick="clearCode()">Clear</button>
  </div>
</div>

## Operators

Mathematical operators are often used in JavaScript and other programming languages. Below is a handful of operators:

**Addition operator:**

```
let x = 5;
let y = 3;

let z = x + y

// z will output 8
console.log(z);
```

**Subtraction operator:**

```
let x = 5;
let y = 3;

let z = x - y;

// z will output 3
console.log(z);
```

**Multiplication operator:**

```
let x = 5;
let y = 2;

let z = x * y;

// z will output 10
console.log(z);

```

**Division operator:**

```
let x = 10;
let y = 2;

let z = x / y;

// z will output 20
console.log(z);
```

**Modulus operator:**

```
let x = 10;
let y = 2;

let z = x % y;

// z will output 0
console.log(z);
```

**Exponential operator:**

```
let x = 2;
let y = 4;

let z = 2**4;

// z will output 16
console.log(z);

```


<div class="exercise-section">
  <h4>Checkpoint: Practice JavaScript Operators</h4>
  <p>
    Define two variables and use JavaScript operators such as <code>+</code>, <code>-</code>, <code>*</code>, and <code>%</code> 
    to perform calculations. Use the buttons below to save your code locally or reload it later.
  </p>

  <textarea id="codeInput" class="code-input" placeholder="// Write your JavaScript code here..."></textarea>

  <div class="button-row">
    <button onclick="saveCode()">Save Code</button>
    <button onclick="loadCode()">Load Saved</button>
    <button onclick="clearCode()">Clear</button>
  </div>
</div>

## Function
Functions are reusable blocks of code that code to be more efficiently and concisely managed. In JavaScript, they are formatted like the following:

```
function name(p1, p2) {
    // Code here
}
```

These are each of the individual components of a function:

<ol>
    <li>Each function must be initialized with the keyword 'function'</li>
    <br>
    <li>Next comes the name of the function followed by a pair of parentheses ()</li>
    <br>
    <li>Inside the parentheses are optional parameters that can be used in the function</li>
    <br>
    <li>After the function name and possible parameters have been established, curly brackets { } are used to hold the code</li>
    <br>
    <li>At this point, you write the code you want to reuse!</li>
    <br>
</ol>

<div class="exercise-section">
  <h4>Checkpoint: Practice Functions</h4>
  <p>
    Make a function that takes two parameters, n1 & n2, and returns the multiplied value of those parameters.
  </p>

  <textarea id="codeInput" class="code-input" placeholder="// Write your JavaScript code here..."></textarea>

  <div class="button-row">
    <button onclick="saveCode()">Save Code</button>
    <button onclick="loadCode()">Load Saved</button>
    <button onclick="clearCode()">Clear</button>
  </div>
</div>

## DOM Basics
JavaScript can be used to edit dynamically edit HTML content as well!

Here is an example of how that can be done:

```
<p id="change-content"></p>

<script>
    const element = document.getElementById("change-content");
    element.innerHTML = "Hello, World!"
</script>
```

Essentially, in order to change the content of an HTML tag, you must first apply an identifier to the certain tag. This allows us to identify and access that tag in JavaScript via the ID.

<br>

Once an ID is in place, in JavaScript, a variable is defined that retrieves the element via its id with the code `document.getElementById("id-here");`

<br>

Now, at this point, the variable can be used to access the HTML by using `.innerHTML = " ";` allowing for the text of the HTML tag to be directly modified.

## Console and console.log()
A very useful part of JavaScript is the tools it provides to help developers debug their code.

<br>

The most prominent of these 'tools' is console.log(), while allow developers to output and record how their code works and reacts in a special place on a web page called the console.

<br>

The console can be accessed by the shortcut Control+Shift+J for Windows and Linux or Command+Option+J for Mac.

<br>

Using console.log() outputs stuff straight here to the console. You can only use console.log() in the console itself! Try it out by typing the following code in the console: `console.log("Hello, World!");`.

<br>

It should output Hello World.

<br>

console.log() is used in many applications beyond this, and is helpful for debugging certain parts of your code. So, when trying to identify why certain parts of the codes are acting in an unintended manner, consider using console.log() to help out.

<div class="exercise-section">
  <h4>Checkpoint: Practice console.log()</h4>
  <p>
    Define two variables and add their values to together. Use console.log() to output the value of the variables individually as well as their combined value.
  </p>

  <textarea id="codeInput" class="code-input" placeholder="// Write your JavaScript code here..."></textarea>

  <div class="button-row">
    <button onclick="saveCode()">Save Code</button>
    <button onclick="loadCode()">Load Saved</button>
    <button onclick="clearCode()">Clear</button>
  </div>
</div>
    
<script>
    function showAnswer() {
        const exampleAnswer = document.getElementById("example-answer");
        exampleAnswer.innerHTML = "x=5<br>y=2<br>z=x*2<br>console.log(z)";
    }

    const codeKey = "jsCheckpointCode";

    function saveCode() {
    const code = document.getElementById("codeInput").value;
    localStorage.setItem(codeKey, code);
    alert("Code saved.");
    }

    function loadCode() {
    const saved = localStorage.getItem(codeKey);
    if (saved) {
        document.getElementById("codeInput").value = saved;
        alert("Code loaded from local storage.");
    } else {
        alert("No saved code found.");
    }
    }

    function clearCode() {
    document.getElementById("codeInput").value = "";
    localStorage.removeItem(codeKey);
    alert("Code cleared.");
    }
</script>