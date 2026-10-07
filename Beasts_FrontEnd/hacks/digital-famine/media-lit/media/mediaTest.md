---
layout: fortunefinders
title: Media Bias Game
permalink: /mediaTest
---

<div style="background-color:#0f1720;color:white;padding:0;margin:0;font-family:system-ui,sans-serif;min-height:100vh;">

<style>
{{ '@import "beasts/inline/pages/hacks-digital-famine-media-lit-media-mediatest-1";' | scssify }}
</style>

<div class="wrap">
  <header>
    <h1>Media Bias Game — Base</h1>
    <div class="controls">
      <button id="shuffle">Shuffle</button>
      <button id="reset">Reset</button>
    </div>
  </header>

  <main class="game">
    <section class="board" aria-label="game board">
      <p class="status">Drag headlines into the zone you think they belong to.</p>
      <div class="items" id="items" aria-live="polite"></div>
    </section>

    <aside class="side">
      <div class="zone good" id="leftZone" data-zone="good" tabindex="0" aria-label="Accurate / Balanced reporting">
        <strong>Balanced / Accurate</strong>
        <div class="zone-contents"></div>
      </div>

      <div class="zone bad" id="rightZone" data-zone="bad" tabindex="0" aria-label="Biased / Misleading reporting">
        <strong>Biased / Misleading</strong>
        <div class="zone-contents"></div>
      </div>

      <div class="footer">
        <div>Score: <span id="score">0</span> / <span id="total">0</span></div>
        <div style="margin-top:6px">Hints: <small>Use keyboard: TAB to focus, SPACE to select, arrow keys to move.</small></div>
      </div>
    </aside>
  </main>
</div>

<script>
  const HEADLINES = [
    {id:1, text:'Study finds coffee linked to lower heart disease risk', correct:'good'},
    {id:2, text:'Celebrity says x — experts warn of rising trend', correct:'bad'},
    {id:3, text:'Government releases budget with small tax relief for families', correct:'good'},
    {id:4, text:'Opinion: this frightening trend will destroy your neighborhood', correct:'bad'},
    {id:5, text:'Local school wins national science award', correct:'good'},
    {id:6, text:'Shocking footage suggests new conspiracy about vaccines', correct:'bad'}
  ];

  const itemsEl = document.getElementById('items');
  const leftZone = document.getElementById('leftZone');
  const rightZone = document.getElementById('rightZone');
  const scoreEl = document.getElementById('score');
  const totalEl = document.getElementById('total');
  const shuffleBtn = document.getElementById('shuffle');
  const resetBtn = document.getElementById('reset');
  let state = { order: [], placed: {} };

  function makeDraggable(item){
    const btn = document.createElement('button');
    btn.className = 'draggable';
    btn.type = 'button';
    btn.draggable = true;
    btn.id = 'item-'+item.id;
    btn.textContent = item.text;
    btn.setAttribute('data-id', item.id);
    btn.setAttribute('aria-pressed','false');

    btn.addEventListener('dragstart', e => {
      e.dataTransfer.setData('text/plain', item.id);
      btn.style.opacity = '0.6';
    });
    btn.addEventListener('dragend', () => btn.style.opacity = '');

    btn.addEventListener('keydown', e => {
      if(e.code === 'Space'){
        e.preventDefault();
        const pressed = btn.getAttribute('aria-pressed') === 'true';
        btn.setAttribute('aria-pressed', String(!pressed));
      }
      if(['ArrowLeft','ArrowRight'].includes(e.code)){
        e.preventDefault();
        const zone = e.code === 'ArrowLeft' ? leftZone : rightZone;
        placeIntoZone(item.id, zone.dataset.zone);
      }
    });

    return btn;
  }

  function renderList(){
    itemsEl.innerHTML = '';
    state.order.forEach(id => {
      const item = HEADLINES.find(h => h.id === id);
      if(!item) return;
      if(state.placed[id]) return;
      itemsEl.appendChild(makeDraggable(item));
    });
    updateTotals();
  }

  function updateTotals(){
    const total = HEADLINES.length;
    const score = computeScore();
    totalEl.textContent = total;
    scoreEl.textContent = score + ' (' + Object.keys(state.placed).length + ' placed)';
  }

  function computeScore(){
    let s = 0;
    for(const [id, zone] of Object.entries(state.placed)){
      const item = HEADLINES.find(h => h.id === Number(id));
      if(item && item.correct === zone) s++;
    }
    return s;
  }

  function shuffleOrder(){
    state.order = HEADLINES.map(h => h.id).sort(() => Math.random()-0.5);
  }

  function clearZones(){
    leftZone.querySelector('.zone-contents').innerHTML = '';
    rightZone.querySelector('.zone-contents').innerHTML = '';
    state.placed = {};
  }

  function placeIntoZone(id, zoneName){
    id = Number(id);
    for(const z of ['good','bad']){
      const container = (z === 'good' ? leftZone : rightZone).querySelector('.zone-contents');
      const existing = container.querySelector('[data-id="'+id+'"]');
      if(existing) existing.remove();
    }
    const item = HEADLINES.find(h => h.id === id);
    if(!item) return;
    const wrapper = document.createElement('div');
    wrapper.textContent = item.text;
    wrapper.className = 'draggable';
    wrapper.setAttribute('data-id', id);
    wrapper.tabIndex = 0;
    (zoneName === 'good' ? leftZone : rightZone).querySelector('.zone-contents').appendChild(wrapper);
    state.placed[id] = zoneName;
    renderList();
  }

  [leftZone, rightZone].forEach(zone => {
    zone.addEventListener('dragover', e => e.preventDefault());
    zone.addEventListener('drop', e => {
      e.preventDefault();
      const id = e.dataTransfer.getData('text/plain');
      placeIntoZone(id, zone.dataset.zone);
    });

    zone.addEventListener('click', e => {
      const picked = document.querySelector('.draggable[aria-pressed="true"]');
      if(picked){
        const id = picked.getAttribute('data-id');
        placeIntoZone(id, zone.dataset.zone);
        picked.setAttribute('aria-pressed','false');
      }
    });
  });

  shuffleBtn.addEventListener('click', () => { shuffleOrder(); clearZones(); renderList(); });
  resetBtn.addEventListener('click', () => { shuffleOrder(); clearZones(); renderList(); });

  (function init(){ shuffleOrder(); renderList(); })();

  const observer = new MutationObserver(() => {
    if(Object.keys(state.placed).length === HEADLINES.length){
      setTimeout(()=>{ alert('All placed! Score: ' + computeScore() + ' / ' + HEADLINES.length); }, 150);
    }
  });
  observer.observe(leftZone.querySelector('.zone-contents'), {childList:true});
  observer.observe(rightZone.querySelector('.zone-contents'), {childList:true});
</script>

</div>