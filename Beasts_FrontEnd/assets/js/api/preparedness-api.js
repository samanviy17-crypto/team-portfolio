// Shared fetch worker: use the existing API host and account token.
window.pnecCommunityRequest = async function(path, method = 'GET', data) {
  const response = await fetch(`${API_BASE}/api${path}`, {
    method, credentials: 'include', headers: _getAuthHeaders(),
    ...(data === undefined ? {} : {body: JSON.stringify(data)})
  });
  const result = await response.json();
  if (!response.ok) throw new Error(response.status === 401 ? 'Please sign in to continue.' : (result.message || result.detail || result.error || 'Request failed.'));
  return result;
};
