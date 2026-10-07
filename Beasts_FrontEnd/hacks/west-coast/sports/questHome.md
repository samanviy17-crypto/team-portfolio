---
layout: post 
tailwind: True
title: Backend Development Quest
description: >
  Learn about database structures, types, and integration with frontend for real-world full-stack development
author: CSP 2025-26
permalink: /west-coast/sports/
lxdData:
  Title: "Backend Development Modules"
  Description: "Master backend development and database integration skills!"
  Topics:
    - Title: "San Diego"
      Genre: "Project Creation"
      Level: 1
      Description: "Stop 1: San Diego — Connecting to the Data Field"
      Categories: ["Backend", "Flask", "Spring", "Databases"]
      Video: "/west-coast/backend/submodule_1-video"
      Lessons: "/west-coast/backend/submodule_1/"
      Image1: "/images/west-coast/petcopark.webp"
    - Title: "Los Angeles"
      Genre: "Project Creation"
      Level: 2
      Description: "Stop 2: Los Angeles — Filtering the Playbook"
      Categories: ["Backend", "Flask", "Spring", "Databases"]
      Video: "/west-coast/backend/submodule_2-video"
      Lessons: "/west-coast/backend/submodule_2/"
      Image2: "/images/west-coast/sofistadium.jpg"
    - Title: "San Francisco"
      Genre: "Project Creation"
      Level: 3
      Description: "Stop 3: San Francisco — Analyzing Performance Data"
      Categories: ["Backend", "Flask", "Spring", "Databases"]
      Video: "/west-coast/backend/submodule_3-video"
      Lessons: "/west-coast/backend/submodule_3/"
      Image3: "/images/west-coast/chasecenter.jpg"
    - Title: "Seattle"
      Genre: "Project Creation"
      Level: 4
      Description: "Stop 4: Seattle — Updating the Leaderboard"
      Categories: ["Backend", "Flask", "Spring", "Databases"]
      Video: "/west-coast/backend/submodule_4-video"
      Lessons: "/west-coast/backend/submodule_4/"
      Image4: "/images/west-coast/seattlestadiums.webp"
footer:
  home: /west-coast/sports/
  next: /west-coast/backend/submodule_1/
---

<style>
{{ '@import "beasts/inline/pages/hacks-west-coast-sports-questhome-1";' | scssify }}
</style>

<div class="quest-container">
  <div class="quest-header">
    <h1>🚀 Backend Development Quest</h1>
    <p>Master backend development and database integration skills!</p>
  </div>
  
  <div class="modules-grid">
    {% for topic in page.lxdData.Topics %}
      <div class="module-card">
        <div class="module-header {% if topic.Title == 'San Diego' %}san-diego{% elsif topic.Title == 'Los Angeles' %}los-angeles{% elsif topic.Title == 'San Francisco' %}san-francisco{% else %}seattle{% endif %}">
          <span class="module-level">Level {{ topic.Level }}</span>
          <h2>{{ topic.Title }}</h2>
          <p>{{ topic.Genre }}</p>
        </div>
        
        <div class="module-body">


          <h3>{{ topic.Description }}</h3>
          <img src="{{topic.Image1}}">
          <img src="{{topic.Image2}}">
          <img src="{{topic.Image3}}">
          <img src="{{topic.Image4}}">
          <div class="module-tags" alt="Petco Park">
            {% for category in topic.Categories %}
            <span class="tag">{{ category }}</span>
            {% endfor %}
          </div>
          
          <div class="module-actions">
            <a href="{{ topic.Lessons }}" class="btn btn-primary">Start Learning</a>
            <a href="{{ topic.Video }}" class="btn btn-secondary">Watch Video</a>
          </div>
        </div>
      </div>
    {% endfor %}
  </div>
</div>
