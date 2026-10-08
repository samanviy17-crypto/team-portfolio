// assets/js/api/auth-api.js
// Responsibility: Auth fetch workers — backend auth plus local user cache in page layer.

function _getAuthHeaders() {
  var token = localStorage.getItem('pnec_token') || sessionStorage.getItem('pnec_token');
  var headers = { 'Content-Type': 'application/json' };
  if (token) headers['Authorization'] = 'Bearer ' + token;
  return headers;
}

function _storeAuthResult(data, remember = true) {
  const storage = remember ? localStorage : sessionStorage;
  const other = remember ? sessionStorage : localStorage;
  other.removeItem('pnec_token'); other.removeItem('pnec_user');
  if (data && data.token) storage.setItem('pnec_token', data.token);
  if (data && data.user) storage.setItem('pnec_user', JSON.stringify(data.user));
}
async function validateAuthResponse(response) {
  if (response.ok) return response;
  const data = await response.json().catch(() => ({}));
  const error = new Error(data.detail || data.message || getErrorMessage(classifyHttpError(response.status)));
  error.type = classifyHttpError(response.status); error.status = response.status;
  throw error;
}

function loginUser(email, password, remember) {
  return fetch(`${API_BASE}/api/auth/login`, {
    method: 'POST',
    credentials: 'include',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password, remember }),
  })
    .then(validateAuthResponse)
    .then(r => r.json())
    .then(data => { _storeAuthResult(data, remember); return data; });
}

function registerUser(userData) {
  const payload = {
    name: userData.display_name,
    display_name: userData.display_name,
    email: userData.email,
    password: userData.password,
    neighborhood_id: userData.neighborhood_id,
  };
  return fetch(`${API_BASE}/api/auth/register`, {
    method: 'POST',
    credentials: 'include',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  })
    .then(validateAuthResponse)
    .then(r => r.json())
    .then(data => { _storeAuthResult(data); return data; });
}

function logoutUser() {
  const headers = _getAuthHeaders();
  localStorage.removeItem('pnec_token');
  sessionStorage.removeItem('pnec_token');
  localStorage.removeItem('pnec_user');
  localStorage.removeItem('pnec_new_user');
  sessionStorage.removeItem('pnec_user');
  return fetch(`${API_BASE}/api/auth/logout`, {
    method: 'POST',
    credentials: 'include',
    headers,
  }).then(validateAuthResponse);
}

function fetchCurrentUser() {
  return fetch(`${API_BASE}/api/auth/me`, {
    method: 'GET',
    credentials: 'include',
    headers: _getAuthHeaders(),
  })
    .then(function(response) {
      if (response.status === 401) return null;
      return response.json().then(function(data) { return data.user || null; });
    })
    .catch(function() { return null; });
}

function fetchNeighborhoodsForSelect() {
  return fetch(`${API_BASE}/api/neighborhoods`, {
    method: 'GET',
    credentials: 'include',
  })
    .then(validateAuthResponse)
    .then(r => r.json())
    .then(data => data.neighborhoods || []);
}


async function requestPasswordReset(email) {
  return accountRecoveryRequest('/forgot-password', {email});
}
async function resetPassword(token, password) {
  return accountRecoveryRequest('/reset-password', {token, password});
}
async function accountRecoveryRequest(path, payload) {
  const response = await fetch(`${API_BASE}/api/auth${path}`, {
    method: 'POST', credentials: 'include', headers: {'Content-Type':'application/json'},
    body: JSON.stringify(payload)
  });
  const result = await response.json();
  if (!response.ok) throw new Error(result.detail || result.message || 'Please try again.');
  return result;
}
function safeAccountRedirect() {
  const fallback = (window.siteBase || (typeof SITE_BASE === 'undefined' ? '' : SITE_BASE)) + '/pages/profile.html';
  const next = new URLSearchParams(location.search).get('next');
  if (!next) return fallback;
  const target = new URL(next, location.origin);
  return target.origin === location.origin ? target.pathname + target.search + target.hash : fallback;
}


function updateProfile(payload) {
  return fetch(`${API_BASE}/api/auth/profile`, {
    method: 'PATCH', credentials: 'include', headers: _getAuthHeaders(),
    body: JSON.stringify(payload),
  }).then(validateAuthResponse).then(response => response.json()).then(data => {
    const remember = localStorage.getItem('pnec_token') !== null;
    _storeAuthResult(data, remember);
    return data.user;
  });
}
