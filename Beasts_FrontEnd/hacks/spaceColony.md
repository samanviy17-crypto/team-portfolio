---
layout: opencs
title: Space Colony
permalink: /spaceColony
---

<style>
{{ '@import "beasts/inline/pages/hacks-spacecolony-1";' | scssify }}
</style>

<div id="gameContainer">
    <div id="promptDropDown" class="promptDropDown" style="z-index: 9999"></div>
    <canvas id='gameCanvas'></canvas>
</div>

<script src="{{site.baseurl}}/assets/js/spaceColony/Game.js"></script>