// Build a Toolhub URL for a detected tool + payload.
// When `slug` is empty we fall back to the homepage with a search query.
// Data always travels in the URL fragment (`#data=`) — fragments are
// client-only and never sent in Referer or request bodies.

const BASE = 'https://toolhub.software';

export function buildUrl(slug, data) {
  const payload = (data || '').toString();
  if (!slug) {
    return `${BASE}/?q=${encodeURIComponent(payload.slice(0, 100))}`;
  }
  return `${BASE}/${slug}/#data=${encodeURIComponent(payload)}`;
}
