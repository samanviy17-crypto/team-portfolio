---
layout: cs-bigsix-lesson
title: "Backend Development — All-in-One Advanced Lesson"
description: "A multi-step lesson on backend development, from fundamentals to advanced topics like serverless, IaC, and AI integration."
permalink: /bigsix/backend_lesson
parent: "bigsix"
lesson_number: 2
team: "Encrypters"
categories: [CSP, Backend, Interactive, Advanced]
tags: [backend, flask, spring, serverless, ai, interactive]
author: "Encrypters Team"
date: 2025-12-02
---

<style>
{{ '@import "beasts/inline/pages/hacks-thebig6-backend-backend-lesson-1";' | scssify }}
</style>

<div class="container page-content">
  <div class="lesson-header">
    <div class="badge">Module 2 · Encrypters Team</div>
    <h1>Backend Development</h1>
    <p>Servers, databases, frameworks, APIs — everything that runs behind what users see.</p>
    <a href="../" class="back-btn">← Back to Big Six</a>
  </div>

  <!-- Progress tracker -->
  <div class="progress-track">
    <div class="progress-steps" id="progressSteps"></div>
  </div>

  <!-- ═══════════════════════════════════════════
       STEP 1: Backend Fundamentals
  ═══════════════════════════════════════════ -->
  <div class="section active" id="step1">
    <div class="card">
      <h2><span class="step-num">1</span> Backend Fundamentals</h2>
      <div class="block-desc">The backend is everything users <em>don't</em> see — authentication, business logic, data processing, and API endpoints. Before saving anything or returning a response, a well-built backend always <strong>validates first</strong>.</div>

      <!-- Architecture diagram -->
      <div class="arch-diagram">
        <div class="arch-box"><div class="arch-icon">🌐</div><div class="arch-label">Client</div><div class="arch-sub">Browser / App</div></div>
        <div class="arch-arrow">→</div>
        <div class="arch-box" style="border-color:rgba(88,166,255,0.4);"><div class="arch-icon">🛡️</div><div class="arch-label">Auth</div><div class="arch-sub">Validate &amp; Guard</div></div>
        <div class="arch-arrow">→</div>
        <div class="arch-box"><div class="arch-icon">⚙️</div><div class="arch-label">Controller</div><div class="arch-sub">Route Handler</div></div>
        <div class="arch-arrow">→</div>
        <div class="arch-box"><div class="arch-icon">🧠</div><div class="arch-label">Service</div><div class="arch-sub">Business Logic</div></div>
        <div class="arch-arrow">→</div>
        <div class="arch-box"><div class="arch-icon">🗃️</div><div class="arch-label">Database</div><div class="arch-sub">Persist Data</div></div>
      </div>

      <!-- Concept tiles -->
      <div class="concept-grid">
        <div class="concept-tile">
          <div class="tile-icon">🔒</div>
          <div class="tile-title">Authentication</div>
          <div class="tile-body">Verify who the user is (login, JWT, sessions). Happens before any data is accessed.</div>
        </div>
        <div class="concept-tile">
          <div class="tile-icon">✅</div>
          <div class="tile-title">Validation</div>
          <div class="tile-body">Check that incoming data has the right format and required fields before processing.</div>
        </div>
        <div class="concept-tile">
          <div class="tile-icon">🧠</div>
          <div class="tile-title">Business Logic</div>
          <div class="tile-body">Rules specific to your app — pricing, permissions, workflows. Lives in the Service layer.</div>
        </div>
        <div class="concept-tile">
          <div class="tile-icon">📡</div>
          <div class="tile-title">API Endpoints</div>
          <div class="tile-body">URLs the frontend calls. Each maps to a controller method that handles a specific action.</div>
        </div>
      </div>

      <!-- MCQ -->
      <div id="quiz1" class="quiz-wrap"></div>
      <div class="btn-row">
        <button onclick="gradeQuiz('quiz1')">Grade</button>
        <button onclick="resetQuiz('quiz1')" class="secondary">Reset</button>
        <span id="quiz1-score" class="score-badge" style="display:none;"></span>
      </div>
      <div class="tip">Validation and authentication always happen before database writes. A backend that saves first and asks questions later is a security risk.</div>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════
       STEP 2: Databases & APIs
  ═══════════════════════════════════════════ -->
  <div class="section" id="step2">
    <div class="card">
      <h2><span class="step-num">2</span> Databases &amp; APIs</h2>
      <div class="block-desc">Databases persist your data. APIs expose it. Understanding SQL vs NoSQL and REST principles is foundational to every backend project.</div>

      <!-- SQL vs NoSQL comparison -->
      <table class="compare-table">
        <thead>
          <tr><th>Feature</th><th>SQL (Relational)</th><th>NoSQL (Non-Relational)</th></tr>
        </thead>
        <tbody>
          <tr><td>Structure</td><td>Fixed schema — tables, rows, columns</td><td>Flexible — documents, key-value, graphs</td></tr>
          <tr><td>Query language</td><td><code>SELECT * FROM users WHERE id = 1</code></td><td><code>db.users.find({id: 1})</code></td></tr>
          <tr><td>Relationships</td><td>JOINs between tables</td><td>Embedded documents or references</td></tr>
          <tr><td>Best for</td><td>Complex queries, strict consistency</td><td>Scale, flexible data, rapid iteration</td></tr>
          <tr><td>Examples</td><td>PostgreSQL, MySQL, SQLite</td><td>MongoDB, Redis, DynamoDB</td></tr>
        </tbody>
      </table>

      <!-- REST CRUD code snippet -->
      <div class="code-block">
        <div class="code-header">
          <div class="dots"><span class="d-r"></span><span class="d-y"></span><span class="d-g"></span></div>
          <span class="lang">REST API — CRUD Endpoints</span>
        </div>
        <pre><span class="cm"># Spring Boot Controller</span>
<span class="an">@RestController</span>
<span class="an">@RequestMapping</span>(<span class="st">"/api/users"</span>)
<span class="kw">public class</span> <span class="fn">UserController</span> {

    <span class="an">@GetMapping</span>           <span class="cm">// GET  /api/users       → Read all</span>
    <span class="kw">public</span> List&lt;User&gt; <span class="fn">getAll</span>() { ... }

    <span class="an">@GetMapping</span>(<span class="st">"/{id}"</span>)  <span class="cm">// GET  /api/users/1     → Read one</span>
    <span class="kw">public</span> User <span class="fn">getById</span>(<span class="an">@PathVariable</span> Long id) { ... }

    <span class="an">@PostMapping</span>          <span class="cm">// POST /api/users       → Create</span>
    <span class="kw">public</span> User <span class="fn">create</span>(<span class="an">@RequestBody</span> UserDTO dto) { ... }

    <span class="an">@PutMapping</span>(<span class="st">"/{id}"</span>)   <span class="cm">// PUT  /api/users/1     → Update</span>
    <span class="kw">public</span> User <span class="fn">update</span>(<span class="an">@PathVariable</span> Long id, <span class="an">@RequestBody</span> UserDTO dto) { ... }

    <span class="an">@DeleteMapping</span>(<span class="st">"/{id}"</span>) <span class="cm">// DELETE /api/users/1   → Delete</span>
    <span class="kw">public void</span> <span class="fn">delete</span>(<span class="an">@PathVariable</span> Long id) { ... }
}</pre>
      </div>

      <!-- Fill-in-the-blank vocab -->
      <h3 style="color:var(--accent);font-size:15px;margin:20px 0 12px;">Vocabulary Check — Fill in the Blanks</h3>
      <div id="vocab2" class="quiz-wrap"></div>
      <div class="btn-row">
        <button onclick="gradeVocab('vocab2')">Check Answers</button>
        <button onclick="resetVocab('vocab2')" class="secondary">Reset</button>
        <span id="vocab2-score" class="score-badge" style="display:none;"></span>
      </div>
      <div class="tip">In REST, every endpoint maps to one of four CRUD operations: Create (POST), Read (GET), Update (PUT/PATCH), Delete (DELETE).</div>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════
       STEP 3: Backend Frameworks
  ═══════════════════════════════════════════ -->
  <div class="section" id="step3">
    <div class="card">
      <h2><span class="step-num">3</span> Backend Frameworks</h2>
      <div class="block-desc">Frameworks give structure. <strong>Flask</strong> (Python) is minimal and flexible — great for microservices and ML backends. <strong>Spring Boot</strong> (Java) is opinionated and full-featured — great for enterprise APIs with strict layers.</div>

      <!-- Framework comparison -->
      <table class="compare-table">
        <thead>
          <tr><th>Feature</th><th>Flask (Python)</th><th>Spring Boot (Java)</th></tr>
        </thead>
        <tbody>
          <tr><td>Philosophy</td><td>Micro — bring what you need</td><td>Opinionated — batteries included</td></tr>
          <tr><td>Routing</td><td><code>@app.route('/path')</code></td><td><code>@GetMapping('/path')</code></td></tr>
          <tr><td>DB layer</td><td>SQLAlchemy / raw SQL</td><td>Spring Data JPA / Hibernate</td></tr>
          <tr><td>Auth built-in</td><td>Flask-Login / JWT manual</td><td>Spring Security (powerful)</td></tr>
          <tr><td>Best for</td><td>Quick APIs, ML serving, scripts</td><td>Large enterprise backends, strict architecture</td></tr>
        </tbody>
      </table>

      <!-- Side-by-side code -->
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:16px 0;">
        <div>
          <div class="field-label" style="margin-bottom:6px;">Flask (Python)</div>
          <div class="code-block">
            <div class="code-header"><div class="dots"><span class="d-r"></span><span class="d-y"></span><span class="d-g"></span></div><span class="lang">python</span></div>
            <pre><span class="kw">from</span> flask <span class="kw">import</span> Flask, jsonify

app = <span class="fn">Flask</span>(__name__)

<span class="an">@app.route</span>(<span class="st">'/api/hello'</span>)
<span class="kw">def</span> <span class="fn">hello</span>():
    <span class="kw">return</span> <span class="fn">jsonify</span>({
        <span class="st">'message'</span>: <span class="st">'Hello!'</span>
    })

<span class="kw">if</span> __name__ == <span class="st">'__main__'</span>:
    app.<span class="fn">run</span>(debug=<span class="nb">True</span>)</pre>
          </div>
        </div>
        <div>
          <div class="field-label" style="margin-bottom:6px;">Spring Boot (Java)</div>
          <div class="code-block">
            <div class="code-header"><div class="dots"><span class="d-r"></span><span class="d-y"></span><span class="d-g"></span></div><span class="lang">java</span></div>
            <pre><span class="an">@RestController</span>
<span class="an">@RequestMapping</span>(<span class="st">"/api"</span>)
<span class="kw">public class</span> <span class="fn">HelloController</span> {

    <span class="an">@GetMapping</span>(<span class="st">"/hello"</span>)
    <span class="kw">public</span> Map&lt;String, String&gt; <span class="fn">hello</span>() {
        <span class="kw">return</span> Map.<span class="fn">of</span>(
            <span class="st">"message"</span>, <span class="st">"Hello!"</span>
        );
    }
}</pre>
          </div>
        </div>
      </div>

      <!-- MCQ -->
      <div id="quiz3" class="quiz-wrap"></div>
      <div class="btn-row">
        <button onclick="gradeQuiz('quiz3')">Grade</button>
        <button onclick="resetQuiz('quiz3')" class="secondary">Reset</button>
        <span id="quiz3-score" class="score-badge" style="display:none;"></span>
      </div>
      <div class="tip">Spring Boot's layered architecture: Controller (routes) → Service (logic) → Repository (database). Never put database calls in a Controller.</div>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════
       STEP 4: API Tester
  ═══════════════════════════════════════════ -->
  <div class="section" id="step4">
    <div class="card">
      <h2><span class="step-num">4</span> API Project &amp; Testing</h2>
      <div class="block-desc">Testing your API before the frontend is built is essential. Tools like <strong>Postman</strong> let you send requests, inspect responses, and verify your endpoints behave correctly — all without writing a single line of frontend code.</div>

      <div class="api-tester">
        <div class="api-left">
          <span class="field-label">Method + Endpoint</span>
          <select id="endpoint-select">
            <option value="GET:/api/users">GET /api/users</option>
            <option value="GET:/api/users/1">GET /api/users/1</option>
            <option value="POST:/api/users">POST /api/users</option>
            <option value="PUT:/api/users/1">PUT /api/users/1</option>
            <option value="DELETE:/api/users/1">DELETE /api/users/1</option>
            <option value="GET:/api/invalid">GET /api/invalid (404)</option>
            <option value="POST:/api/users/bad">POST /api/users (invalid body → 400)</option>
          </select>

          <span class="field-label" style="margin-top:12px;">Request Preview</span>
          <div class="code-block">
            <div class="code-header"><div class="dots"><span class="d-r"></span><span class="d-y"></span><span class="d-g"></span></div><span class="lang" id="reqLang">http</span></div>
            <pre id="reqPreview" style="font-size:11px;">GET /api/users HTTP/1.1
Host: localhost:8080
Accept: application/json</pre>
          </div>

          <button onclick="sendRequest()" style="margin-top:8px;">▶ Send Request</button>
          <div id="sendStatus" style="font-size:12px;color:var(--muted);margin-top:6px;"></div>
        </div>

        <div class="api-right">
          <span class="field-label">Response</span>
          <div class="response-box" style="flex:1;">
            <div class="response-box-header">
              <span>Body</span>
              <span id="status-badge-wrap"></span>
            </div>
            <div class="response-box-body" id="response-body">Select an endpoint and click Send.</div>
            <div class="response-meta" id="response-meta" style="display:none;">
              <span id="resp-time"></span>
              <span id="resp-size"></span>
            </div>
          </div>

          <span class="field-label" style="margin-top:12px;">What to look for</span>
          <div id="apiHint" style="background:var(--panel-3);border:1px solid var(--border);border-radius:8px;padding:12px;font-size:12px;color:var(--muted);line-height:1.6;">
            Pick an endpoint and send a request to see what a real API response looks like.
          </div>
        </div>
      </div>

      <div class="tip">HTTP status codes tell you what happened: 2xx = success, 4xx = client error (bad request, not found), 5xx = server error.</div>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════
       STEP 5: Advanced Backend
  ═══════════════════════════════════════════ -->
  <div class="section" id="step5">
    <div class="card">
      <h2><span class="step-num">5</span> Advanced Backend Concepts</h2>
      <div class="block-desc">Once you know the basics, these are the patterns that separate junior from senior backend engineers — security, scalability, observability, and AI integration.</div>

      <div class="concept-grid">
        <div class="concept-tile">
          <div class="tile-icon">☁️</div>
          <div class="tile-title">Serverless</div>
          <div class="tile-body">Deploy individual functions (AWS Lambda, Vercel Functions) without managing a server. Scale to zero when idle.</div>
        </div>
        <div class="concept-tile">
          <div class="tile-icon">🔑</div>
          <div class="tile-title">JWT Auth</div>
          <div class="tile-body">JSON Web Tokens encode user identity. The backend signs them; every subsequent request carries the token so no session needed.</div>
        </div>
        <div class="concept-tile">
          <div class="tile-icon">📊</div>
          <div class="tile-title">Observability</div>
          <div class="tile-body">Logging, metrics, and tracing. You can't fix what you can't see — structured logs are as important as the code itself.</div>
        </div>
        <div class="concept-tile">
          <div class="tile-icon">🤖</div>
          <div class="tile-title">AI Integration</div>
          <div class="tile-body">Backend calls to LLM APIs (OpenAI, Gemini) for summarization, classification, generation — AI is just another service call.</div>
        </div>
        <div class="concept-tile">
          <div class="tile-icon">⚡</div>
          <div class="tile-title">Caching</div>
          <div class="tile-body">Redis stores frequent queries in memory so the database isn't hit every time. Can cut response times 100x.</div>
        </div>
        <div class="concept-tile">
          <div class="tile-icon">🏗️</div>
          <div class="tile-title">IaC</div>
          <div class="tile-body">Infrastructure as Code (Terraform, Pulumi) — define servers, databases, and networks in version-controlled config files.</div>
        </div>
      </div>

      <!-- JWT code -->
      <div class="code-block">
        <div class="code-header"><div class="dots"><span class="d-r"></span><span class="d-y"></span><span class="d-g"></span></div><span class="lang">python — JWT token flow</span></div>
        <pre><span class="kw">import</span> jwt, datetime

SECRET = <span class="st">"your-secret-key"</span>

<span class="kw">def</span> <span class="fn">create_token</span>(user_id):
    payload = {
        <span class="st">"sub"</span>: user_id,
        <span class="st">"iat"</span>: datetime.<span class="fn">utcnow</span>(),
        <span class="st">"exp"</span>: datetime.<span class="fn">utcnow</span>() + datetime.timedelta(hours=<span class="nb">24</span>)
    }
    <span class="kw">return</span> jwt.<span class="fn">encode</span>(payload, SECRET, algorithm=<span class="st">"HS256"</span>)

<span class="kw">def</span> <span class="fn">verify_token</span>(token):
    <span class="kw">try</span>:
        <span class="kw">return</span> jwt.<span class="fn">decode</span>(token, SECRET, algorithms=[<span class="st">"HS256"</span>])
    <span class="kw">except</span> jwt.ExpiredSignatureError:
        <span class="kw">raise</span> <span class="fn">Exception</span>(<span class="st">"Token expired"</span>)
    <span class="kw">except</span> jwt.InvalidTokenError:
        <span class="kw">raise</span> <span class="fn">Exception</span>(<span class="st">"Invalid token"</span>)</pre>
      </div>

      <!-- Advanced MCQ -->
      <div id="quiz5" class="quiz-wrap"></div>
      <div class="btn-row">
        <button onclick="gradeQuiz('quiz5')">Grade</button>
        <button onclick="resetQuiz('quiz5')" class="secondary">Reset</button>
        <span id="quiz5-score" class="score-badge" style="display:none;"></span>
      </div>
    </div>
  </div>

  <!-- ═══════════════════════════════════════════
       STEP 6: FRQ & Reflection
  ═══════════════════════════════════════════ -->
  <div class="section" id="step6">
    <div class="card">
      <h2><span class="step-num">6</span> Free Response &amp; Reflection</h2>
      <div class="block-desc">Apply everything you've learned. Answer each question thoughtfully — responses are graded against a rubric of key backend concepts.</div>

      <div id="frqContainer"></div>

      <div style="margin-top:24px;background:var(--panel-2);border:1px solid var(--border);border-radius:10px;padding:16px;">
        <div style="font-size:14px;font-weight:700;color:#a6c9ff;margin-bottom:10px;">✅ What You Covered</div>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:8px;">
          <div style="background:var(--panel-3);border-radius:8px;padding:10px 12px;font-size:12px;color:var(--muted);">
            <span style="color:var(--accent-2);font-weight:700;">Step 1</span> — Backend flow: validate → authenticate → process → persist
          </div>
          <div style="background:var(--panel-3);border-radius:8px;padding:10px 12px;font-size:12px;color:var(--muted);">
            <span style="color:var(--accent-2);font-weight:700;">Step 2</span> — SQL vs NoSQL, REST CRUD, HTTP methods &amp; status codes
          </div>
          <div style="background:var(--panel-3);border-radius:8px;padding:10px 12px;font-size:12px;color:var(--muted);">
            <span style="color:var(--accent-2);font-weight:700;">Step 3</span> — Flask vs Spring Boot architecture and layering
          </div>
          <div style="background:var(--panel-3);border-radius:8px;padding:10px 12px;font-size:12px;color:var(--muted);">
            <span style="color:var(--accent-2);font-weight:700;">Step 4</span> — API testing: status codes, request/response shape
          </div>
          <div style="background:var(--panel-3);border-radius:8px;padding:10px 12px;font-size:12px;color:var(--muted);">
            <span style="color:var(--accent-2);font-weight:700;">Step 5</span> — Serverless, JWT, caching, observability, AI integration
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Navigation -->
  <div class="nav-buttons">
    <button id="prevBtn" onclick="prevStep()" class="secondary" disabled>← Previous</button>
    <span id="stepIndicator">Step 1 / 6</span>
    <button id="nextBtn" onclick="nextStep()">Next →</button>
  </div>
</div>

<script>
// ============================================================
// CONFIG — all lesson data lives here
// ============================================================
const STEPS = ['step1','step2','step3','step4','step5','step6'];
const STEP_LABELS = ['Fundamentals','Databases','Frameworks','API Testing','Advanced','FRQ'];
const STORAGE_KEY = 'backend_combined_v2';

// ── MCQ DATA ──────────────────────────────────────────────
const QUIZZES = {
  quiz1: [
    {
      q: 'You see this frontend call:',
      code: 'fetch(`${javaURI}/api/responses`, {\n  method: "POST",\n  headers: { "Content-Type": "application/json" },\n  body: JSON.stringify({ name: "Ana", response: "Here is my answer" })\n});',
      opts: [
        'Immediately save the data to the database',
        'Return a success message to the frontend',
        'Validate the request format and required fields, then authenticate the user if needed',
        'Start a background processing job'
      ],
      a: 2,
      explanation: 'Correct — validation and authentication always happen first. Saving unvalidated data is a major security risk that can corrupt the database or allow malicious input.'
    },
    {
      q: 'Which HTTP status code indicates a request succeeded and a new resource was created?',
      opts: ['200 OK', '201 Created', '204 No Content', '301 Moved Permanently'],
      a: 1,
      explanation: '201 Created is the correct response for a successful POST that creates a new resource. 200 OK is for successful reads or updates that return a body.'
    },
    {
      q: 'What does a 401 Unauthorized response mean?',
      opts: [
        'The resource does not exist',
        'The server crashed',
        'The client is not authenticated — no valid credentials were provided',
        'The client does not have permission for this specific resource (that is 403)'
      ],
      a: 2,
      explanation: '401 = not authenticated (no login / bad token). 403 = authenticated but not authorized (you are logged in but do not have permission). These are different!'
    }
  ],

  quiz3: [
    {
      q: 'In Spring Boot\'s layered architecture, which layer should contain business logic?',
      opts: ['Controller — it handles the HTTP request', 'Service — it holds all business rules and logic', 'Repository — it talks to the database', 'Entity — it defines the data model'],
      a: 1,
      explanation: 'The Service layer holds business logic. Controllers only route requests and call services. Repositories only talk to the database. This separation makes code testable and maintainable.'
    },
    {
      q: 'What is the primary advantage of Flask over Spring Boot for a small ML serving endpoint?',
      opts: [
        'Flask has built-in Spring Security',
        'Flask uses JPA for database access',
        'Flask is minimal and Python-native, making it easy to integrate with PyTorch/TensorFlow models',
        'Flask requires less RAM than Spring at runtime'
      ],
      a: 2,
      explanation: 'Flask is written in Python, which is the native language of ML libraries like PyTorch and TensorFlow. You can import your model directly and serve predictions with very few lines of code.'
    },
    {
      q: 'Which annotation in Spring Boot maps a POST request to a controller method?',
      opts: ['@GetMapping', '@PostMapping', '@RequestBody', '@Service'],
      a: 1,
      explanation: '@PostMapping maps HTTP POST requests to the annotated method. @RequestBody is used to bind the request body to a parameter, not to map the route.'
    }
  ],

  quiz5: [
    {
      q: 'What is the main advantage of serverless functions (e.g., AWS Lambda) over traditional servers?',
      opts: [
        'They run faster than regular servers',
        'They scale automatically to zero when idle — no idle compute cost',
        'They support more programming languages',
        'They do not need authentication'
      ],
      a: 1,
      explanation: 'Serverless functions spin up on demand and scale down to zero — you only pay when they run. Traditional servers run 24/7 even when idle.'
    },
    {
      q: 'In a JWT (JSON Web Token), where is user data stored?',
      opts: [
        'In a server-side session database',
        'In a cookie only',
        'Encoded directly in the token payload — readable by anyone, signed by the server',
        'Encrypted inside the token — unreadable without the private key'
      ],
      a: 2,
      explanation: 'JWT payloads are Base64-encoded, not encrypted — anyone can read the claims. The server\'s signature (using a secret key) is what makes them tamper-proof. Never put sensitive data like passwords in a JWT payload.'
    },
    {
      q: 'What does Redis primarily improve in a backend architecture?',
      opts: [
        'Code compilation speed',
        'Database schema migrations',
        'Response time for frequently accessed data by caching it in memory',
        'Serverless cold start latency'
      ],
      a: 2,
      explanation: 'Redis is an in-memory data store used as a cache. Frequently queried data is stored in RAM so the backend skips the database entirely on cache hits, reducing response times dramatically.'
    }
  ]
};

// ── VOCAB DATA ────────────────────────────────────────────
const VOCAB_DATA = {
  vocab2: [
    { clue: 'A structured set of rows and columns in a relational database', hint: '5 letters', answer: 'TABLE' },
    { clue: 'A single record in a database table', hint: '3 letters', answer: 'ROW' },
    { clue: 'A lightweight data format used in REST API responses (two abbreviations)', hint: '4 letters', answer: 'JSON' },
    { clue: 'The HTTP method used to CREATE a new resource', hint: '4 letters', answer: 'POST' },
    { clue: 'SQL keyword used to combine rows from two or more tables', hint: '4 letters', answer: 'JOIN' }
  ]
};

// ── FRQ DATA ──────────────────────────────────────────────
const FRQ_DATA = [
  {
    id: 'frq1',
    q: 'Describe the full lifecycle of a POST request in a Spring Boot backend — from the moment the frontend sends the request to the moment a response is returned. Mention at least three layers.',
    rubric: [
      { key: 'controller', label: 'Controller mentioned', test: a => /controller/i.test(a) },
      { key: 'service', label: 'Service layer mentioned', test: a => /service/i.test(a) },
      { key: 'repository', label: 'Repository / database layer mentioned', test: a => /repositor|database|db|persist/i.test(a) },
      { key: 'validation', label: 'Validation or auth discussed', test: a => /valid|auth/i.test(a) },
      { key: 'response', label: 'HTTP response / status code discussed', test: a => /response|status|201|200|return/i.test(a) }
    ]
  },
  {
    id: 'frq2',
    q: 'Compare SQL and NoSQL databases. Give a real-world scenario where you would choose each, and explain why.',
    rubric: [
      { key: 'sql_def', label: 'SQL defined (relational, schema, tables)', test: a => /relational|schema|table|column|row/i.test(a) },
      { key: 'nosql_def', label: 'NoSQL defined (flexible, document, key-value)', test: a => /nosql|document|flexible|mongo|key.value/i.test(a) },
      { key: 'sql_use', label: 'SQL use case given', test: a => /bank|financial|transaction|commerce|consistent/i.test(a) },
      { key: 'nosql_use', label: 'NoSQL use case given', test: a => /social|real.time|cache|scale|json|rapid/i.test(a) },
      { key: 'reasoning', label: 'Reasoning explained (not just listed)', test: a => a.length > 120 }
    ]
  }
];

// ── API MOCK ──────────────────────────────────────────────
const MOCK_API = {
  'GET:/api/users': {
    status: 200,
    body: [{ id: 1, name: 'Alice', role: 'admin' }, { id: 2, name: 'Bob', role: 'user' }],
    hint: '200 OK — the server found the resource and returned it. This is the expected response for a successful GET.'
  },
  'GET:/api/users/1': {
    status: 200,
    body: { id: 1, name: 'Alice', role: 'admin', createdAt: '2024-01-15' },
    hint: '200 OK — fetching a single record by ID. If the ID did not exist you would get 404.'
  },
  'POST:/api/users': {
    status: 201,
    body: { id: 3, name: 'Carol', role: 'user', createdAt: '2025-12-02' },
    hint: '201 Created — a new resource was successfully created. The response body contains the created record with its new ID.'
  },
  'PUT:/api/users/1': {
    status: 200,
    body: { id: 1, name: 'Alice Updated', role: 'admin', updatedAt: '2025-12-02' },
    hint: '200 OK — the resource was updated. Some APIs return 204 No Content instead (no body).'
  },
  'DELETE:/api/users/1': {
    status: 204,
    body: null,
    hint: '204 No Content — the resource was deleted. No body is returned because there is nothing left to send.'
  },
  'GET:/api/invalid': {
    status: 404,
    body: { error: 'Not Found', message: 'No route matches GET /api/invalid', timestamp: '2025-12-02T10:30:00Z' },
    hint: '404 Not Found — the route or resource does not exist. Check your URL path and spelling.'
  },
  'POST:/api/users/bad': {
    status: 400,
    body: { error: 'Bad Request', message: 'Validation failed: "name" is required, "email" must be a valid email', timestamp: '2025-12-02T10:30:00Z' },
    hint: '400 Bad Request — the client sent invalid data. The server caught this during validation before touching the database.'
  }
};

const REQUEST_PREVIEWS = {
  'GET:/api/users':       `GET /api/users HTTP/1.1\nHost: localhost:8080\nAccept: application/json`,
  'GET:/api/users/1':     `GET /api/users/1 HTTP/1.1\nHost: localhost:8080\nAccept: application/json`,
  'POST:/api/users':      `POST /api/users HTTP/1.1\nHost: localhost:8080\nContent-Type: application/json\n\n{\n  "name": "Carol",\n  "role": "user"\n}`,
  'PUT:/api/users/1':     `PUT /api/users/1 HTTP/1.1\nHost: localhost:8080\nContent-Type: application/json\n\n{\n  "name": "Alice Updated"\n}`,
  'DELETE:/api/users/1':  `DELETE /api/users/1 HTTP/1.1\nHost: localhost:8080`,
  'GET:/api/invalid':     `GET /api/invalid HTTP/1.1\nHost: localhost:8080`,
  'POST:/api/users/bad':  `POST /api/users HTTP/1.1\nHost: localhost:8080\nContent-Type: application/json\n\n{\n  "name": "",\n  "email": "not-an-email"\n}`
};

// ============================================================
// State
// ============================================================
let currentStep = 0;
const quizPicks = {}; // quizId → { qIndex → optIndex }

const $ = id => document.getElementById(id);

// ============================================================
// Navigation
// ============================================================
function showStep(n) {
  currentStep = Math.max(0, Math.min(STEPS.length - 1, n));
  STEPS.forEach((s, i) => $(s).classList.toggle('active', i === currentStep));

  // Update progress dots
  const stepsEl = $('progressSteps');
  stepsEl.innerHTML = STEPS.map((_, i) => {
    const state = i < currentStep ? 'done' : i === currentStep ? 'active' : '';
    const icon = i < currentStep ? '✓' : i + 1;
    return `<div class="progress-step ${state}" onclick="showStep(${i})">
      <div class="step-dot">${icon}</div>
      <div class="step-label">${STEP_LABELS[i]}</div>
    </div>`;
  }).join('');

  $('stepIndicator').textContent = `Step ${currentStep + 1} / ${STEPS.length}`;
  $('prevBtn').disabled = currentStep === 0;
  $('nextBtn').disabled = currentStep === STEPS.length - 1;

  persist();

  if (currentStep === STEPS.length - 1) {
    if (typeof completeBigSixLesson === 'function') completeBigSixLesson();
  }
  saveBigSixProgress(currentStep + 1);
}

function prevStep() { showStep(currentStep - 1); }
function nextStep() { showStep(currentStep + 1); }

// ============================================================
// MCQ Engine
// ============================================================
function renderQuiz(quizId) {
  const data = QUIZZES[quizId];
  if (!data) return;
  const box = $(quizId);
  if (!box) return;
  if (!quizPicks[quizId]) quizPicks[quizId] = {};
  box.innerHTML = '';

  data.forEach((item, qi) => {
    const wrap = document.createElement('div');
    wrap.className = 'question-block';

    const qText = document.createElement('div');
    qText.className = 'question-text';
    qText.textContent = `Q${qi + 1}. ${item.q}`;
    wrap.appendChild(qText);

    if (item.code) {
      const codeEl = document.createElement('pre');
      codeEl.className = 'question-code';
      codeEl.textContent = item.code;
      wrap.appendChild(codeEl);
    }

    item.opts.forEach((optText, oi) => {
      const el = document.createElement('div');
      el.className = 'opt';
      el.dataset.qi = qi;
      el.dataset.oi = oi;
      el.dataset.quiz = quizId;

      const dot = document.createElement('span');
      dot.className = 'radio-dot';

      const lbl = document.createElement('span');
      lbl.className = 'opt-label';
      lbl.textContent = `${String.fromCharCode(65 + oi)}. ${optText}`;

      el.appendChild(dot);
      el.appendChild(lbl);

      el.addEventListener('click', () => {
        quizPicks[quizId][qi] = oi;
        box.querySelectorAll(`.opt[data-qi="${qi}"][data-quiz="${quizId}"]`).forEach(x => x.classList.remove('sel'));
        el.classList.add('sel');
      });

      wrap.appendChild(el);
    });

    // Explanation placeholder (hidden until graded)
    const exp = document.createElement('div');
    exp.className = 'explanation';
    exp.id = `${quizId}-exp-${qi}`;
    wrap.appendChild(exp);

    box.appendChild(wrap);
  });
}

function gradeQuiz(quizId) {
  const data = QUIZZES[quizId];
  if (!data) return;
  const picks = quizPicks[quizId] || {};
  let correct = 0;

  data.forEach((item, qi) => {
    const chosen = picks[qi];
    // Clear previous
    document.querySelectorAll(`.opt[data-qi="${qi}"][data-quiz="${quizId}"]`).forEach(el => el.classList.remove('good', 'bad'));
    const expEl = $(`${quizId}-exp-${qi}`);

    if (chosen === undefined) {
      // Not answered
      if (expEl) { expEl.textContent = '⚠ Not answered. The correct answer is ' + String.fromCharCode(65 + item.a) + '.'; expEl.classList.add('show'); }
      return;
    }

    const isCorrect = chosen === item.a;
    if (isCorrect) correct++;

    const chosenEl = document.querySelector(`.opt[data-qi="${qi}"][data-oi="${chosen}"][data-quiz="${quizId}"]`);
    if (chosenEl) chosenEl.classList.add(isCorrect ? 'good' : 'bad');

    if (!isCorrect) {
      const correctEl = document.querySelector(`.opt[data-qi="${qi}"][data-oi="${item.a}"][data-quiz="${quizId}"]`);
      if (correctEl) correctEl.classList.add('good');
    }

    if (expEl) {
      expEl.textContent = (isCorrect ? '✅ ' : '❌ ') + item.explanation;
      expEl.classList.add('show');
    }
  });

  const scoreEl = $(`${quizId}-score`);
  if (scoreEl) {
    scoreEl.textContent = `${correct} / ${data.length}`;
    scoreEl.style.display = 'inline-block';
    scoreEl.className = 'score-badge' + (correct === data.length ? ' perfect' : '');
  }
}

function resetQuiz(quizId) {
  quizPicks[quizId] = {};
  const scoreEl = $(`${quizId}-score`);
  if (scoreEl) { scoreEl.style.display = 'none'; scoreEl.textContent = ''; }
  renderQuiz(quizId);
}

// ============================================================
// Vocab / Fill-in-Blank Engine
// ============================================================
function renderVocab(vocabId) {
  const data = VOCAB_DATA[vocabId];
  if (!data) return;
  const box = $(vocabId);
  if (!box) return;
  box.innerHTML = '';
  data.forEach((item, i) => {
    const row = document.createElement('div');
    row.className = 'vocab-item';
    row.innerHTML = `
      <div class="vocab-clue">
        <strong>${i + 1}.</strong> ${item.clue}
        <span class="hint">(${item.hint})</span>
      </div>
      <input class="vocab-input" id="${vocabId}-inp-${i}" maxlength="${item.answer.length}"
             placeholder="${'_'.repeat(item.answer.length)}" autocomplete="off" spellcheck="false" />
    `;
    box.appendChild(row);
  });
}

function gradeVocab(vocabId) {
  const data = VOCAB_DATA[vocabId];
  if (!data) return;
  let correct = 0;
  data.forEach((item, i) => {
    const inp = $(`${vocabId}-inp-${i}`);
    if (!inp) return;
    const val = inp.value.trim().toUpperCase();
    const isCorrect = val === item.answer;
    if (isCorrect) correct++;
    inp.classList.remove('correct', 'wrong');
    inp.classList.add(isCorrect ? 'correct' : 'wrong');
    if (!isCorrect) inp.placeholder = item.answer; // Reveal answer
  });
  const scoreEl = $(`${vocabId}-score`);
  if (scoreEl) {
    scoreEl.textContent = `${correct} / ${data.length}`;
    scoreEl.style.display = 'inline-block';
    scoreEl.className = 'score-badge' + (correct === data.length ? ' perfect' : '');
  }
}

function resetVocab(vocabId) {
  const data = VOCAB_DATA[vocabId];
  if (!data) return;
  data.forEach((_, i) => {
    const inp = $(`${vocabId}-inp-${i}`);
    if (inp) { inp.value = ''; inp.className = 'vocab-input'; inp.placeholder = '_'.repeat(data[i].answer.length); }
  });
  const scoreEl = $(`${vocabId}-score`);
  if (scoreEl) { scoreEl.style.display = 'none'; scoreEl.textContent = ''; }
}

// ============================================================
// API Tester
// ============================================================
function updateRequestPreview() {
  const key = $('endpoint-select').value;
  const preview = REQUEST_PREVIEWS[key] || '';
  $('reqPreview').textContent = preview;
  const method = key.split(':')[0];
  $('reqLang').textContent = method + ' · http';
}

function sendRequest() {
  const key = $('endpoint-select').value;
  const mock = MOCK_API[key];
  if (!mock) return;

  const bodyEl = $('response-body');
  const metaEl = $('response-meta');
  const hintEl = $('apiHint');
  const statusWrap = $('status-badge-wrap');
  const sendStatus = $('sendStatus');

  bodyEl.textContent = 'Sending…';
  statusWrap.innerHTML = '';
  metaEl.style.display = 'none';
  sendStatus.textContent = 'Request sent…';

  const start = Date.now();
  const delay = 300 + Math.floor(Math.random() * 300);

  setTimeout(() => {
    const elapsed = Date.now() - start;
    const body = mock.body ? JSON.stringify(mock.body, null, 2) : '(no body — 204 No Content)';
    const size = body.length;

    bodyEl.textContent = body;

    const s = mock.status;
    const cls = s >= 500 ? 'status-5xx' : s >= 400 ? 'status-4xx' : 'status-2xx';
    statusWrap.innerHTML = `<span class="status-badge ${cls}">${s}</span>`;

    metaEl.style.display = 'flex';
    $('resp-time').textContent = `⏱ ${elapsed}ms`;
    $('resp-size').textContent = `📦 ${size} bytes`;

    hintEl.innerHTML = `<strong style="color:var(--text);">${s}</strong> — ${mock.hint}`;
    sendStatus.textContent = 'Done';
  }, delay);
}

// ============================================================
// FRQ Engine
// ============================================================
function renderFrqs() {
  const container = $('frqContainer');
  if (!container) return;
  container.innerHTML = '';

  FRQ_DATA.forEach((frq, fi) => {
    const wrap = document.createElement('div');
    wrap.className = 'frq-box';
    wrap.innerHTML = `
      <div class="frq-question">FRQ ${fi + 1}: ${frq.q}</div>
      <textarea class="frq-textarea" id="${frq.id}-ans" rows="5" placeholder="Write your response here — use complete sentences and be specific..."></textarea>
      <div class="btn-row">
        <button onclick="gradeFrq('${frq.id}')">Grade Response</button>
        <button class="secondary" onclick="resetFrq('${frq.id}')">Clear</button>
      </div>
      <div class="frq-feedback" id="${frq.id}-fb"></div>
    `;
    container.appendChild(wrap);
  });
}

function gradeFrq(frqId) {
  const frq = FRQ_DATA.find(f => f.id === frqId);
  if (!frq) return;
  const answer = ($(`${frqId}-ans`).value || '').trim();
  const fb = $(`${frqId}-fb`);

  if (!answer) { fb.innerHTML = '<span style="color:var(--error);">Please write a response before grading.</span>'; fb.classList.add('show'); return; }

  let hits = 0;
  const tagsHtml = frq.rubric.map(r => {
    const passed = r.test(answer);
    if (passed) hits++;
    return `<span class="rubric-tag ${passed ? 'hit' : ''}">${passed ? '✓' : '○'} ${r.label}</span>`;
  }).join('');

  const total = frq.rubric.length;
  const score = Math.round((hits / total) * 100);
  let verdict = '';
  if (score >= 80) verdict = `<strong style="color:var(--success);">Strong response (${hits}/${total} criteria met)</strong>`;
  else if (score >= 50) verdict = `<strong style="color:var(--warn);">Partial response (${hits}/${total} criteria met) — expand your answer</strong>`;
  else verdict = `<strong style="color:var(--error);">Needs more depth (${hits}/${total} criteria met)</strong>`;

  fb.innerHTML = `${verdict}<div class="frq-rubric" style="margin-top:10px;">${tagsHtml}</div>`;
  fb.classList.add('show');
}

function resetFrq(frqId) {
  const ans = $(`${frqId}-ans`);
  const fb = $(`${frqId}-fb`);
  if (ans) ans.value = '';
  if (fb) { fb.innerHTML = ''; fb.classList.remove('show'); }
}

// ============================================================
// Persistence
// ============================================================
function persist() {
  try { localStorage.setItem(STORAGE_KEY, JSON.stringify({ step: currentStep })); } catch(e) {}
}

function restore() {
  try {
    const data = JSON.parse(localStorage.getItem(STORAGE_KEY));
    if (data) showStep(data.step || 0);
    else showStep(0);
  } catch(e) { showStep(0); }
}

function saveBigSixProgress(stepNumber) {
  try {
    const key = 'bigsix:backend_lesson:lesson:' + stepNumber;
    if (localStorage.getItem(key) !== 'done') localStorage.setItem(key, 'done');
  } catch(e) {}
}

// ============================================================
// Boot
// ============================================================
document.addEventListener('DOMContentLoaded', () => {
  renderQuiz('quiz1');
  renderVocab('vocab2');
  renderQuiz('quiz3');
  renderQuiz('quiz5');
  renderFrqs();

  const epSelect = $('endpoint-select');
  if (epSelect) epSelect.addEventListener('change', updateRequestPreview);
  updateRequestPreview();

  restore();
});
</script>

<script>
(function(){
  document.addEventListener('DOMContentLoaded',function(){
    document.querySelectorAll('a.back-btn').forEach(function(a){
      a.addEventListener('click',function(e){
        if(e.metaKey||e.ctrlKey||e.shiftKey||e.button===1)return;
        e.preventDefault();
        try{if(document.referrer&&new URL(document.referrer).origin===location.origin){history.back();return;}}catch(err){}
        var p=location.pathname.replace(/\/$/,'').split('/');
        if(p.length>1){p.pop();window.location.href=p.join('/')+'/';}else{window.location.href='/';}
      });
    });
  });
})();
</script>

<script src="/assets/js/lesson-completion-bigsix.js"></script>