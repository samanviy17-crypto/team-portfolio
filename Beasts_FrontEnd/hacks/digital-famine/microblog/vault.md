---
layout: post
title: "Microblogging Vault"
description: "Microblog Vault"
permalink: /digital-famine/microblog/vault/
parent: "AI Usage"
team: "Unzippers"
submodule: 1
categories: [CSP, Submodule, Microblogging]
tags: [microblogging, submodule, unzippers]
author: "Krishna Visvanath, Sloane Sommers, Lucas M"
date: 2025-10-21
breadcrumb: true
---

<html lang="en">
<head>
<meta charset="utf-8">
<title>Code Access Terminal</title>
<meta name="viewport" content="width=device-width, initial-scale=1">

<style>
{{ '@import "beasts/inline/pages/hacks-digital-famine-microblog-vault-1";' | scssify }}
</style>
</head>
<body>

<h2>Access Verification Terminal</h2>

<div class="terminal">
  <input id="code" type="text" autocomplete="off" placeholder="Enter access code">
  <div class="status-light" id="status-light"></div>
</div>

<div id="out"></div>

<div id="doors">
  <div class="door left"></div>
  <div class="door right"></div>
</div>

<div id="cake-section">
  <h2>Access Granted</h2>
  <img src="https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiyDRuMxLUUyNkbDfMOxqFjQzwOLI8hUsC5E5a5NVIqSPeDWONt6UouQyBuZuWbMqlfUy3sMJsrMMcQ8DEeNVbJYDhiew-JoN3_LbCa27ahv0W9v9LLb8kHFyoX7PvaRRsSTBRyR9dCUbs/s1600/the_cake_is_a_lie_portal.jpg" alt="Portal Cake">
  <button onclick="window.location.href='{{ base.siteurl }}/digital-famine/'">Continue</button>
</div>

<!-- CryptoJS -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/crypto-js/4.1.1/crypto-js.min.js"></script>

<script>
  const KEY_STR = "meow mroww meoww";
  const STORED_CIPHERTEXT = "6e4b7871f58d3e221921f62c7ae9371df338d24e78248e0dd4c8a480beb5014a";

  const codeEl = document.getElementById('code');
  const light = document.getElementById('status-light');
  const out = document.getElementById('out');
  const doors = document.getElementById('doors');
  const leftDoor = document.querySelector('#doors .door.left');
  const rightDoor = document.querySelector('#doors .door.right');

  function encryptAes128EcbHex(plaintext) {
    const key = CryptoJS.enc.Utf8.parse(KEY_STR);
    const cp = CryptoJS.AES.encrypt(plaintext, key, { mode: CryptoJS.mode.ECB, padding: CryptoJS.pad.Pkcs7 });
    return cp.ciphertext.toString(CryptoJS.enc.Hex);
  }

  function verify() {
    console.log('[vault] Verify clicked, input:', codeEl.value);
    const code = (codeEl.value || "").trim();
    if (!code) {
      out.textContent = "Please enter a code.";
      return;
    }

    const computed = encryptAes128EcbHex(code);
    console.log('[vault] computed:', computed, ' expected:', STORED_CIPHERTEXT);
    if (computed === STORED_CIPHERTEXT) {
      out.textContent = "Code accepted.";
      light.style.animation = "blink-green 1s infinite";
      document.body.classList.add("doors-open");
      doors.classList.add("doors-open");
      // remove any inline forced transforms if present
      if (leftDoor) leftDoor.style.transform = '';
      if (rightDoor) rightDoor.style.transform = '';
      console.log('[vault] doors-open class added to body and #doors');
    } else {
      out.textContent = "Access denied.";
      light.style.animation = "blink-red 1s infinite";
      // small visible feedback
      const terminal = document.querySelector('.terminal');
      if (terminal) {
        terminal.classList.remove('shake');
        // force reflow to restart animation
        void terminal.offsetWidth;
        terminal.classList.add('shake');
      }
    }
  }

   codeEl.addEventListener('keydown', (e) => {
     if (e.key === 'Enter') {
         e.preventDefault();
         console.log('[vault] Enter pressed');
         verify();
      }
    });
</script>
</body>
</html>

