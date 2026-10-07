---
layout: certchatbot
title: "Submodule 2: Certificates and Badges"
description: "Submodule 2 of Analytics/Admin Mini-Quest"
permalink: /cs-portfolio-quest/analytics/submodule_2/
parent: "Analytics/Admin"
team: "Curators"
submodule: 2
tags: [analytics, submodule, curators]
author: "Curators Team"
date: 2025-10-21
microblog: true
---

# Submodule 2: Certfication

<style>
{{ '@import "beasts/inline/pages/hacks-cs-portfolio-quest-analytics-submodule-2-1";' | scssify }}
</style>

<div class="container">
  
  <h2 class="section-title">Individual Module Certificates</h2>
  <div class="certificates-grid">
    <div class="cert-card cert-orange">
      <span class="cert-badge">Verified</span>
      <h3 class="cert-title">Frontend Development</h3>
      <div class="cert-org">Open Coding Society</div>
      <div class="cert-date">November 2025</div>
      <div class="cert-actions">
        <button class="btn btn-download" onclick="downloadCert('Frontend Development', 'Open Coding Society', 'November 2025')">⬇ Download</button>
      </div>
    </div>

    <div class="cert-card cert-red">
      <span class="cert-badge">Verified</span>
      <h3 class="cert-title">Backend Development</h3>
      <div class="cert-org">Open Coding Society</div>
      <div class="cert-date">November 2025</div>
      <div class="cert-actions">
        <button class="btn btn-download" onclick="downloadCert('Backend Development', 'Open Coding Society', 'November 2025')">⬇ Download</button>
      </div>
    </div>

    <div class="cert-card cert-purple">
      <span class="cert-badge">Verified</span>
      <h3 class="cert-title">Data Visualization</h3>
      <div class="cert-org">Open Coding Society</div>
      <div class="cert-date">November 2025</div>
      <div class="cert-actions">
        <button class="btn btn-download" onclick="downloadCert('Data Visualization', 'Open Coding Society', 'November 2025')">⬇ Download</button>
      </div>
    </div>

    <div class="cert-card cert-teal">
      <span class="cert-badge">Verified</span>
      <h3 class="cert-title">Resume Building</h3>
      <div class="cert-org">Open Coding Society</div>
      <div class="cert-date">November 2025</div>
      <div class="cert-actions">
        <button class="btn btn-download" onclick="downloadCert('Resume Building', 'Open Coding Society', 'November 2025')">⬇ Download</button>
      </div>
    </div>

    <div class="cert-card cert-yellow">
      <span class="cert-badge">Verified</span>
      <h3 class="cert-title">AI Usage</h3>
      <div class="cert-org">Open Coding Society</div>
      <div class="cert-date">November 2025</div>
      <div class="cert-actions">
        <button class="btn btn-download" onclick="downloadCert('AI Usage', 'Open Coding Society', 'November 2025')">⬇ Download</button>
      </div>
    </div>
  </div>
  <h2 class="section-title">Overall Certificate</h2>
  <div class="certificates-grid">
    <div class="cert-card cert-green" >
      <span class="cert-badge">Verified</span>
      <h3 class="cert-title">Overall CS Portfolio Certificate</h3>
      <div class="cert-org">Open Coding Society</div>
      <div class="cert-date">November 2025</div>
      <div class="cert-actions">
        <button class="btn btn-download" onclick="downloadCert('Computer Science Portfolio - Full Stack Development', 'Open Coding Society', 'November 2025')">⬇ Download</button>
        <button class="btn btn-share" onclick="addToLinkedIn('Computer Science Portfolio - Full Stack Development Java Usage')">Add to LinkedIn</button>
      </div>
    </div>
  </div>

  
<!-- Instructional Card -->
<div style="
  width: 100%;
  background-color: #121212;
  border: 1px solid #d1d9e0;
  border-radius: 16px;
  padding: 24px;
  margin-top: 40px;
  box-shadow: 0 2px 8px rgba(117, 47, 47, 0.08);
  font-family: 'Segoe UI', Tahoma, sans-serif;
  line-height: 1.6;
">

  <h2 style="text-align: center; color: #004182;">How to Fill Out Your Certification</h2>

  <!-- Screenshot image -->
  <center><img src="{{site.baseurl}}/images/cs-portfolio-quest/analytics/LinkdenReqs.png" height="625"></center>


  <p style="text-align: center; max-width: 800px; margin: 0 auto 20px auto;">
    Use the example above as a reference when adding your certification on LinkedIn. Below is a guide explaining what to fill out in each section.
  </p>

  <ul style="list-style-type: none; padding-left: 0; max-width: 800px; margin: 0 auto;">
    <li><strong>Name:</strong> Enter the official title of your certificate (e.g., “Python Data Analysis Certificate” or “AWS Certified Developer”).</li>
    <li><strong>Issuing Organization:</strong> Type the name of the organization that granted the certificate (e.g., “Coursera,” “Google,” “Microsoft”).</li>
    <li><strong>Issue Date:</strong> Select the month and year when you received your certification.</li>
    <li><strong>Expiration Date:</strong> Leave this blank if the certification never expires, or fill in the date when it becomes invalid.</li>
    <li><strong>Credential ID:</strong> If your certificate includes a unique ID number, enter it here. Otherwise, you can leave it empty.</li>
    <li><strong>Credential URL:</strong> Paste the link where your certificate can be verified or viewed online (for example, the public certificate link from your organization).</li>
  </ul>

  <h3 style="color: #004182; margin-top: 30px; text-align: center;">Optional Sections</h3>
  <ul style="list-style-type: none; padding-left: 0; max-width: 800px; margin: 0 auto;">
    <li><strong>Skills:</strong> Add relevant skills that this certification demonstrates, such as “Cybersecurity,” “Cloud Computing,” or “Data Analysis.”</li>
    <li><strong>Media:</strong> Upload a copy of your certificate (PDF or image) or link to a project or document that showcases your achievement.</li>
  </ul>

  <p style="text-align: center; color: #333; margin-top: 20px;">
    Once everything is complete, click <strong>Save</strong> to publish your certification to your LinkedIn profile.
  </p>
</div>


<canvas id="certCanvas"></canvas>

<script type="module">
// Provide a safe global stub immediately so inline onclick handlers won't fail
window.downloadCert = async function () {
  // temporary stub while module initializes
  alert('Preparing certificate... If this message persists, the certificate system failed to initialize.');
};

(async () => {
  try {
    const cfg = await import('{{ site.baseurl }}/assets/js/api/config.js');
    const { pythonURI, fetchOptions } = cfg;

    async function getCredentials() {
      try {
        const res = await fetch(`${pythonURI}/api/id`, fetchOptions );

        if (res.ok) {
          const data = await res.json();
          return data.name || 'Student Name';
        } else {
          console.log(`Request failed with status ${res.status}`);
        }
      } catch (err) {
        console.log(`Error fetching credentials: ${err}`);
      }
      return 'Student Name';
    }

    async function downloadCert(course, org, date) {
      const name = await getCredentials();

      const canvas = document.getElementById('certCanvas');
      const ctx = canvas.getContext('2d');

      canvas.width = 1400;
      canvas.height = 1000;

      // Background - elegant cream
      ctx.fillStyle = '#f8f6f0';
      ctx.fillRect(0, 0, canvas.width, canvas.height);

      // Outer border - navy
      ctx.strokeStyle = '#2c3e50';
      ctx.lineWidth = 25;
      ctx.strokeRect(50, 50, canvas.width - 100, canvas.height - 100);

      // Inner border - gold accent
      ctx.strokeStyle = '#c9b037';
      ctx.lineWidth = 3;
      ctx.strokeRect(80, 80, canvas.width - 160, canvas.height - 160);

      // Decorative corners
      ctx.fillStyle = '#c9b037';
      ctx.beginPath();
      ctx.arc(80, 80, 15, 0, Math.PI * 2);
      ctx.arc(canvas.width - 80, 80, 15, 0, Math.PI * 2);
      ctx.arc(80, canvas.height - 80, 15, 0, Math.PI * 2);
      ctx.arc(canvas.width - 80, canvas.height - 80, 15, 0, Math.PI * 2);
      ctx.fill();

      // Title
      ctx.fillStyle = '#2c3e50';
      ctx.font = 'bold 60px Georgia';
      ctx.textAlign = 'center';
      ctx.fillText('CERTIFICATE', canvas.width / 2, 200);

      ctx.font = 'bold 48px Georgia';
      ctx.fillText('OF COMPLETION', canvas.width / 2, 260);

      // Decorative line under title
      ctx.strokeStyle = '#c9b037';
      ctx.lineWidth = 4;
      ctx.beginPath();
      ctx.moveTo(400, 290);
      ctx.lineTo(1000, 290);
      ctx.stroke();

      // "This is to certify that"
      ctx.fillStyle = '#2c3e50';
      ctx.font = '28px Arial';
      ctx.fillText('This is to certify that', canvas.width / 2, 380);

      // Student name (from API)
      ctx.fillStyle = '#ea8c33';
      ctx.font = 'italic bold 52px Georgia';
      ctx.fillText(name, canvas.width / 2, 470);

      // Underline
      ctx.strokeStyle = '#ea8c33';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(400, 490);
      ctx.lineTo(1000, 490);
      ctx.stroke();

      // "has successfully completed"
      ctx.fillStyle = '#2c3e50';
      ctx.font = '28px Arial';
      ctx.fillText('has successfully completed the course', canvas.width / 2, 560);

      // Course name
      ctx.fillStyle = '#2c3e50';
      ctx.font = 'bold 44px Arial';
      ctx.fillText(course, canvas.width / 2, 650);

      // Organization
      ctx.fillStyle = '#555';
      ctx.font = '26px Arial';
      ctx.fillText('Issued by ' + org, canvas.width / 2, 710);

  // Date — use current date to ensure certificate is issued today
  const issuanceDate = new Date();
  const formattedDate = issuanceDate.toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric' });
  // match the Advanced Python Programming accent (red) for the date
  ctx.fillStyle = '#2c3e50';
  ctx.font = 'bold 24px Arial';
  ctx.fillText('Date: ' + formattedDate, canvas.width / 2, 800);

      // Signature line
      ctx.strokeStyle = '#2c3e50';
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.moveTo(500, 880);
      ctx.lineTo(900, 880);
      ctx.stroke();

      // signature name: larger and lifted above the line to match 'OF COMPLETION'
      ctx.fillStyle = '#555';
      ctx.font = 'bold 48px Georgia';
      // place slightly above the signature line
      ctx.fillText('John Mortenson', canvas.width / 2, 860);

      // Trigger download
      const link = document.createElement('a');
      link.download = `${course.replace(/\s+/g, '_')}_Certificate.png`;
      link.href = canvas.toDataURL('image/png');
      link.click();
    }

    function addToLinkedIn(courseName) {
      const certId = 'CSPORTFOLIO-' + Date.now() + '-' + Math.random().toString(36).substring(2, 8).toUpperCase();
      
      const url = new URL('https://www.linkedin.com/profile/add');
      url.searchParams.append('startTask', 'CERTIFICATION_NAME');
      url.searchParams.append('name', courseName);
      url.searchParams.append('organizationName', 'Open Coding Society');
      url.searchParams.append('issueYear', new Date().getFullYear());
      url.searchParams.append('issueMonth', new Date().getMonth() + 1);
      url.searchParams.append('certId', certId);
      url.searchParams.append('certUrl', window.location.origin + '/cs-portfolio-verify/' + certId);
      
      window.open(url.toString(), '_blank');
    }


    // replace the stub with the real implementation
    window.downloadCert = downloadCert;
    window.addToLinkedIn = addToLinkedIn;

  } catch (err) {
    console.error('Failed to initialize certificate downloader:', err);
    // keep the user-friendly stub already assigned above
  }
})();

</script>