---
layout: cs-portfolio-lesson
title: "Submodule 4"
description: "Submodule 4 of Backend Development Mini-Quest"
permalink: /cs-portfolio-quest/backend/submodule_4/
parent: "Backend Development"
team: "Encrypters"
submodule: 4
tags: [backend, submodule, encrypters]
author: "Encrypters Team"
date: 2025-10-21

---

#  Final Project: API and Postman Validation

This final submodule requires you to demonstrate your skills by building a **functional RESTful API** and validating its  operation using a **Postman Collection**.

### Repository template:
**https://github.com/Open-Coding-Society/flask.git**

---

## 1. Capstone Implementation Steps

Follow these steps to build the **Blog Platform API**, focusing on the simplified requirements.

### **Step 1: Project Setup & Database Design**
1.  **Clone the Template:** Clone the repository template and set up your local development environment
2.  **Database Schema:** Define the database model for your blog posts.
    * **Create the `Post` Model:** Define fields like `title`, `content`, and, crucially, the foreign key relationship to the `User` model (`author_id`).
3.  **Run Migrations:** Apply your model changes to the database to create the necessary **Users** and **Posts** tables.

### **Step 2: Authentication (Security Foundation)**
1.  **Enable Register & Login:** Utilize the template's authentication logic for **Registration** (`POST /api/auth/register`) and **Login** (`POST /api/auth/login`).
    * **Security Check:** Confirm that **passwords are hashed** before storage.
2.  **Verify Protected Routes:** Test that the built-in authentication dependency (middleware) is protecting routes.
    * **Test:** An unauthenticated request to a protected endpoint must return a **`401 Unauthorized`**.

### **Step 3: Implement Posts CRUD Endpoints**

| Feature | Description | Example Endpoints |
| :--- | :--- | :--- |
| **Read (Public)** | Retrieve all posts and a single post by ID. | `GET /api/posts`, `GET /api/posts/:id` |
| **Create (Protected)** | Create a new post. **Must require authentication.** | `POST /api/posts` |
| **Update/Delete (Authorized)** | Modify or remove a post. **Must require authentication and authorization.** | `PUT /api/posts/:id`, `DELETE /api/posts/:id` |

**Authorization Logic:**
For `PUT` and `DELETE` requests, add logic to check that the ID of the currently authenticated user matches the `author_id` of the post. If they do not match, return a **`403 Forbidden`**.

### **Step 4: Error Handling and Validation**
* **Input Validation:** Implement checks for required fields (`title`, `content`) and return a **`400 Bad Request`** if validation fails.
* **Resource Not Found:** Ensure requests for non-existent IDs return a **`404 Not Found`** status code.

---

## 2. Postman Validation Steps

Create a complete Postman Collection that serves as the official test suite for your API.

### **Step 1: Set Up Postman Environment**
1.  **Create an Environment:** Create a new Postman Environment (e.g., `Capstone Blog API`).
2.  **Set Variables:** Add two variables:
    * `baseURL`: Your local server address (e.g., `http://localhost:8000`).
    * `authToken`: Initial value should be empty.

### **Step 2: Build the Authentication Workflow**
1.  **Login & Capture Token:** Create the request for **`POST {{baseURL}}/api/auth/login`**.
2.  **Add Test Script:** In the **Tests** tab of the Login request, add a script to save the returned token:

    ```javascript
    // Verify success status
    pm.test("Status code is 200", function () {
        pm.response.to.have.status(200);
    });

    // Save the token to the environment
    var jsonData = pm.response.json();
    // Use the correct key based on your template (e.g., 'access_token' or 'token')
    pm.environment.set("authToken", jsonData.access_token); 
    ```

### **Step 3: Validate CRUD with Full Test Sequence**
1.  **Set Bearer Token:** For the **`POST`, `PUT`, and `DELETE`** requests, set the **Authorization** type to **Bearer Token** and use the value `{{authToken}}`.
2.  **Full Test Sequence:** Execute the collection in a logical order to prove the full workflow:
    * **Register** a new user.
    * **Login** the user (token is saved).
    * **Create Post** (using the token).
    * **Get All Posts** (verify new post exists).
    * **Update Post** (using the token).
    * **Delete Post** (using the token).

---

### **Postman Simulator**
Take a look at what your Postman could potentially look like with various endpoints.

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>API Tester</title>
    <style>
{{ '@import "beasts/inline/pages/hacks-cs-portfolio-quest-backend-submodule-4-1";' | scssify }}
</style>
</head>
<body>
    <div class="container">
        <h1>API Tester</h1>

        <div class="presets">
            <button class="preset-btn" onclick="loadPreset('/api/users', 'GET')">GET /api/users</button>
            <button class="preset-btn" onclick="loadPreset('/api/users/1', 'GET')">GET /api/users/1</button>
            <button class="preset-btn" onclick="loadPreset('/api/users', 'POST')">POST /api/users</button>
            <button class="preset-btn" onclick="loadPreset('/api/users/1', 'PUT')">PUT /api/users/1</button>
            <button class="preset-btn" onclick="loadPreset('/api/users/1', 'DELETE')">DELETE /api/users/1</button>
            <button class="preset-btn" onclick="loadPreset('/api/products', 'GET')">GET /api/products</button>
            <button class="preset-btn" onclick="loadPreset('/api/posts', 'POST')">POST /api/posts</button>
            <button class="preset-btn" onclick="loadPreset('/api/invalid', 'GET')">GET /api/invalid (404)</button>
        </div>

        <div class="tester-section">
            <div class="input-group">
                <label>Method</label>
                <select id="method" disabled>
                    <option value="GET">GET</option>
                    <option value="POST">POST</option>
                    <option value="PUT">PUT</option>
                    <option value="DELETE">DELETE</option>
                    <option value="PATCH">PATCH</option>
                </select>

                <label>Endpoint</label>
                <input type="text" id="url" placeholder="/api/users" disabled>

                <button class="btn" onclick="sendRequest()" style="margin-top: 20px;">Send Request</button>
            </div>
        </div>

        <div id="response-container" class="response-section">
            <div class="response-header">
                <h2>Response</h2>
                <span id="status-code" class="status-badge"></span>
            </div>
            <div id="response-time" class="response-info"></div>
            <label style="color: #ffffff; font-weight: 600;">Response Body:</label>
            <div id="response-body" class="response-body"></div>
        </div>
    </div>

    <script>
        const mockEndpoints = {
            'GET:/api/users': {
                status: 200,
                body: [
                    { id: 1, name: 'Alice', email: 'alice@example.com', role: 'admin' },
                    { id: 2, name: 'Bob', email: 'bob@example.com', role: 'user' },
                    { id: 3, name: 'Charlie', email: 'charlie@example.com', role: 'user' }
                ]
            },
            'GET:/api/users/1': {
                status: 200,
                body: { id: 1, name: 'Alice', email: 'alice@example.com', role: 'admin', createdAt: '2024-01-15' }
            },
            'GET:/api/products': {
                status: 200,
                body: [
                    { id: 1, name: 'Laptop', price: 999.99, stock: 5 },
                    { id: 2, name: 'Mouse', price: 29.99, stock: 50 },
                    { id: 3, name: 'Keyboard', price: 79.99, stock: 20 }
                ]
            },
            'POST:/api/users': {
                status: 201,
                body: { id: 4, name: 'New User', email: 'newuser@example.com', role: 'user', createdAt: '2024-01-20', message: 'User created successfully' }
            },
            'POST:/api/posts': {
                status: 201,
                body: { id: 101, title: 'New Post', content: 'Post content here', author: 'User', likes: 0, createdAt: '2024-01-20', message: 'Post created' }
            },
            'PUT:/api/users/1': {
                status: 200,
                body: { id: 1, name: 'Alice Updated', email: 'alice.new@example.com', role: 'admin', updatedAt: '2024-01-20', message: 'User updated' }
            },
            'DELETE:/api/users/1': {
                status: 200,
                body: { message: 'User deleted successfully', id: 1 }
            },
            'GET:/api/invalid': {
                status: 404,
                body: { error: 'Endpoint not found', message: 'The requested resource does not exist' }
            }
        };

        function loadPreset(endpoint, method) {
            document.getElementById('url').value = endpoint;
            document.getElementById('method').value = method;
        }

        function sendRequest() {
            const method = document.getElementById('method').value;
            const endpoint = document.getElementById('url').value;

            if (!endpoint) {
                alert('Please enter an endpoint');
                return;
            }

            const key = `${method}:${endpoint}`;
            const mockResponse = mockEndpoints[key];

            const btn = event.target;
            btn.disabled = true;
            btn.textContent = 'Sending...';

            setTimeout(() => {
                document.getElementById('response-container').classList.add('active');

                if (mockResponse) {
                    const statusBadge = document.getElementById('status-code');
                    statusBadge.textContent = `${mockResponse.status}`;
                    statusBadge.className = 'status-badge';

                    if (mockResponse.status >= 200 && mockResponse.status < 300) {
                        statusBadge.classList.add('status-2xx');
                    } else if (mockResponse.status >= 400 && mockResponse.status < 500) {
                        statusBadge.classList.add('status-4xx');
                    } else {
                        statusBadge.classList.add('status-5xx');
                    }

                    document.getElementById('response-time').textContent = `Response time: ${Math.random() * 100 + 50 | 0}ms`;
                    document.getElementById('response-body').textContent = JSON.stringify(mockResponse.body, null, 2);
                } else {
                    const statusBadge = document.getElementById('status-code');
                    statusBadge.textContent = '404';
                    statusBadge.className = 'status-badge status-4xx';
                    document.getElementById('response-time').textContent = `Response time: ${Math.random() * 50 + 30 | 0}ms`;
                    document.getElementById('response-body').textContent = JSON.stringify({ error: 'Endpoint not found', availableEndpoints: Object.keys(mockEndpoints).map(k => k.split(':')[1]) }, null, 2);
                }

                btn.disabled = false;
                btn.textContent = 'Send Request';
            }, 500);
        }
    </script>
</body>

