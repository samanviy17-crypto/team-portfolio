---
microblog: true
layout: post
title: Poway Neighborhood Emergency Corps
description: Our project is continuing and expanding the Poway Neighborhood Emergency Corps (PNEC) platform, a preparedness site built for a real community organization in Poway.
permalink: /capstone/pnec
---

<style>
  /* Base Layout matched to PNEC Live Site Styling */
  .pnec-body-wrapper {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif !important;
    background-color: #0d1117 !important; /* Authentic Dark Theme Background */
    color: #c9d1d9 !important; /* Soft high-contrast text */
    max-width: 1100px;
    margin: 2rem auto;
    padding: 1.5rem;
    border-radius: 8px;
    border: 1px solid #30363d !important;
    line-height: 1.6;
  }

  .pnec-body-wrapper p, 
  .pnec-body-wrapper td, 
  .pnec-body-wrapper li, 
  .pnec-body-wrapper span {
    color: #c9d1d9 !important;
  }

  /* Headings */
  .pnec-body-wrapper h1, 
  .pnec-body-wrapper h2, 
  .pnec-body-wrapper h3 {
    color: #f0f6fc !important;
    font-weight: 700 !important;
  }

  /* Navigation & Action Links */
  .pnec-link {
    color: #58a6ff !important;
    text-decoration: underline !important;
    font-weight: 600;
  }

  .pnec-link:hover {
    color: #79c0ff !important;
  }

  .pnec-btn-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background-color: #238636;
    color: #ffffff !important;
    padding: 10px 18px;
    border-radius: 6px;
    text-decoration: none !important;
    font-weight: 600;
    margin-top: 1rem;
    border: 1px solid rgba(240,246,252,0.1);
    transition: background-color 0.2s ease;
  }

  .pnec-btn-link:hover {
    background-color: #2ea043;
    color: #ffffff !important;
  }

  /* Hero Banner */
  .pnec-hero {
    background-color: #161b22 !important;
    border: 1px solid #30363d !important;
    border-left: 6px solid #58a6ff !important;
    border-radius: 6px;
    padding: 2rem;
    margin-bottom: 2rem;
  }

  .pnec-hero h1 {
    margin-top: 0;
    font-size: 2rem;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .pnec-authors {
    font-size: 1.05rem;
    font-weight: 600;
    margin-bottom: 1rem;
  }

  .pnec-section-title {
    border-bottom: 2px solid #30363d !important;
    padding-bottom: 0.5rem;
    margin-top: 2.5rem;
    font-size: 1.5rem;
    color: #58a6ff !important;
  }

  /* Tables Matching Live Site Data */
  .pnec-table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 1rem;
    background-color: #0d1117 !important;
  }

  .pnec-table th {
    background-color: #161b22 !important;
    color: #f0f6fc !important;
    font-weight: 700;
    padding: 12px;
    border: 1px solid #30363d !important;
    text-align: left;
  }

  .pnec-table td {
    border: 1px solid #30363d !important;
    padding: 12px;
    text-align: left;
    background-color: #0d1117 !important;
  }

  /* Cards Grid */
  .pnec-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin-top: 1rem;
  }

  .pnec-card {
    border: 1px solid #30363d !important;
    border-top: 4px solid #58a6ff !important;
    border-radius: 6px;
    padding: 1.25rem;
    background-color: #161b22 !important;
    box-shadow: 0 2px 4px rgba(0,0,0,0.3);
  }

  .pnec-card h3 {
    margin-top: 0;
    font-size: 1.2rem;
    color: #58a6ff !important;
  }

  /* Rollout Section */
  .pnec-rollout {
    background-color: #161b22 !important;
    border-left: 4px solid #58a6ff !important;
    border: 1px solid #30363d;
    padding: 1rem 1.5rem 1rem 2.5rem;
    border-radius: 4px;
  }

  .pnec-rollout li {
    margin-bottom: 0.5rem;
  }
</style>

<div class="pnec-body-wrapper">

  <!-- Hero / Header Section -->
  <div class="pnec-hero">
    <h1>
      <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#58a6ff" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
        <g id="shield-icon">
          <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"></path>
        </g>
      </svg>
      Poway Neighborhood Emergency Corps (PNEC)
    </h1>
    <p class="pnec-authors">
      <strong>Project Contributors:</strong> 
      <a class="pnec-link" href="#">Joan Kim</a>, 
      <a class="pnec-link" href="#">Samanvi Yachareni</a>, 
      <a class="pnec-link" href="#">Ainsley Albert</a>
    </p>
    <p>A modern preparedness platform continuing and expanding critical safety tools built for a real community organization in Poway, California.</p>
    
    <div>
      <a class="pnec-btn-link" href="https://pnec.opencodingsociety.com/" target="_blank" rel="noopener noreferrer">
        🌐 Visit Original Live Platform (PNEC)
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6"></path><polyline points="15 3 21 3 21 9"></polyline><line x1="10" y1="14" x2="21" y2="3"></line></svg>
      </a>
    </div>
  </div>

  <!-- Background Section -->
  <div>
    <h2 class="pnec-section-title">📖 Background</h2>
    <p>PNEC is a preparedness platform built for the Poway Neighborhood Emergency Corps, a real community organization — not a hypothetical client. The previous team rebuilt the group’s site from a static page into an actual working platform available on <a class="pnec-link" href="https://pnec.opencodingsociety.com/" target="_blank" rel="noopener noreferrer">pnec.opencodingsociety.com</a>. The last team presented at the CTE Expo and Night at the Museum, gathered direct feedback from real users, and left a documented handoff for whoever picks the project up next — which is exactly the position we are stepping into.</p>

    <h3 style="margin-top: 1.5rem;">Live Features (Inherited from <a class="pnec-link" href="https://pnec.opencodingsociety.com/" target="_blank" rel="noopener noreferrer">Original Site</a>)</h3>
    <table class="pnec-table">
      <thead>
        <tr>
          <th>Feature</th>
          <th>What it does</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong>Risk Watch</strong></td>
          <td>Homepage panel showing live wildfire, flood, and extreme-heat risk for Poway, pulled from weather and air-quality data.</td>
        </tr>
        <tr>
          <td><strong>Helper Bot</strong></td>
          <td>A chatbot that answers preparedness questions (e.g. what belongs in a 72-hour kit), grounded in PNEC’s own FAQ content.</td>
        </tr>
        <tr>
          <td><strong>Find Your Neighborhood</strong></td>
          <td>Interactive map covering 60+ Poway neighborhoods, each linked to a block coordinator, nearest fire station, and evacuation route.</td>
        </tr>
        <tr>
          <td><strong>Member accounts & roles</strong></td>
          <td>Separate logins and dashboards for residents, coordinators, staff, and admins.</td>
        </tr>
        <tr>
          <td><strong>Live theme editor</strong></td>
          <td>Lets non-technical volunteers request a content change in plain English and have it committed to the site automatically — no code required.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Why We Chose PNEC -->
  <div>
    <h2 class="pnec-section-title">🎯 Why We Chose Poway Neighborhood Emergency Corps</h2>
    <p>We chose PNEC because it’s a way to help the community be prepared in cases of emergency. Living in San Diego, our community faces many risks such as wildfires, high temperatures, and earthquakes. Being prepared and ready with a plan in case of emergency is extremely important for safety. Additionally, we think there are several aspects we want to add and teach to help the community. That mix of community impact and technical depth made it the right project for us.</p>
  </div>

  <!-- Project Additions & Planned Changes -->
  <div>
    <h2 class="pnec-section-title">🛠️ What We Want to Add / Change</h2>
    <div class="pnec-grid">
      
      <div class="pnec-card">
        <h3>Family/Household Checklist</h3>
        <p>A saved, personalized checklist (72-hour kit, evacuation plan, meeting point) tied to each resident’s account, with progress tracking, so households can see what they still need to do — not just read static advice from the Helper Bot.</p>
      </div>

      <div class="pnec-card">
        <h3>Interactive Quiz</h3>
        <p>Ask residents 8–10 questions like “Do you have an emergency kit?” or “Do you know your evacuation route?”, and at the end give a preparedness score along with the top things they need to do to be more prepared.</p>
      </div>

      <div class="pnec-card">
        <h3>Volunteer Shift/Task Board</h3>
        <p>A simple sign-up board where coordinators post needs (door-to-door check-ins, supply drives, CERT training sessions) and residents/volunteers claim slots, turning the site into a coordination tool, not just an info source.</p>
      </div>

      <div class="pnec-card">
        <h3>Post-Disaster Check-In Board</h3>
        <p>During an actual emergency, let residents mark themselves “safe” or “need help” by neighborhood, visible to their coordinator — similar to Red Cross Safe and Well but scoped to Poway’s blocks.</p>
      </div>

      <div class="pnec-card">
        <h3>Multilingual Support</h3>
        <p>Auto-translate or offer key pages (Risk Watch, evacuation info, Helper Bot) in Spanish and other locally common languages, since emergency info needs to reach non-English speakers too.</p>
      </div>

      <div class="pnec-card">
        <h3>Donation Drive & Goal Tracker</h3>
        <p>A page where PNEC can list current needs (flashlights, water, first-aid kits) and show progress toward a goal, so donors and local businesses have somewhere to give.</p>
      </div>

      <div class="pnec-card">
        <h3>"Report a Hazard" Form</h3>
        <p>Let residents flag things like a downed tree, blocked evacuation route, or broken fire hydrant, with the report routed to the relevant coordinator or admin dashboard.</p>
      </div>

      <div class="pnec-card">
        <h3>Community FAQ Feedback</h3>
        <p>A “was this helpful?” prompt, or a way for residents to submit questions that stump the chatbot, so PNEC volunteers can see gaps in the Helper Bot’s knowledge base and fill them in.</p>
      </div>

      <div class="pnec-card">
        <h3>Weekly Tips & Events</h3>
        <p>Every week, new tips and volunteer/learning events are posted for residents to stay prepared, updated based on current threats — for example, flood-prep tips during an active flood risk period.</p>
      </div>

    </div>
  </div>

  <!-- Rollout Section -->
  <div>
    <h2 class="pnec-section-title">🚀 Rollout Strategy</h2>
    <ul class="pnec-rollout">
      <li>Implement and test all planned features listed above directly on top of the original codebase.</li>
      <li>Meet with the actual PNEC team to walk through the updated features on <a class="pnec-link" href="https://pnec.opencodingsociety.com/" target="_blank" rel="noopener noreferrer">pnec.opencodingsociety.com</a>.</li>
      <li>Work with the nonprofit to get this updated version adopted as their official live site.</li>
    </ul>
  </div>

</div>