// Pure-function content-type detection for selected text.
// Returns { slug, label, confidence } describing the best Toolhub tool match,
// or a fallback descriptor when nothing specific matches.

function tryDecodeBase64Url(seg) {
  const padded = seg.replace(/-/g, '+').replace(/_/g, '/');
  const pad = padded.length % 4 === 0 ? '' : '='.repeat(4 - (padded.length % 4));
  return atob(padded + pad);
}

export function detect(rawText) {
  const text = (rawText || '').toString();
  if (!text) return { slug: '', label: 'Toolhub', confidence: 'none' };

  // 1. JWT — three base64url segments, header decodes to JSON with `alg`
  if (/^[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+\.[A-Za-z0-9_-]+$/.test(text)) {
    try {
      const header = JSON.parse(tryDecodeBase64Url(text.split('.')[0]));
      if (header && header.alg) {
        return { slug: 'jwt-decoder', label: 'JWT Decoder', confidence: 'high' };
      }
    } catch (e) { /* fall through */ }
  }

  // 2. JSON — wrapped in {} or [] and parses cleanly
  const trimmed = text.trim();
  if ((trimmed.startsWith('{') && trimmed.endsWith('}')) ||
      (trimmed.startsWith('[') && trimmed.endsWith(']'))) {
    try {
      JSON.parse(trimmed);
      return { slug: 'json-formatter', label: 'JSON Formatter', confidence: 'high' };
    } catch (e) { /* fall through */ }
  }

  // 3. CIDR — N.N.N.N/M
  if (/^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\/\d{1,2}$/.test(trimmed)) {
    return { slug: 'cidr-calculator', label: 'CIDR Calculator', confidence: 'high' };
  }

  // 4. URL-encoded — contains %XX patterns
  if (/%[0-9A-Fa-f]{2}/.test(text)) {
    return { slug: 'url-encoder', label: 'URL Encoder/Decoder', confidence: 'medium' };
  }

  // 5. Base64 — strict charset, ≥16 chars, length divisible by 4
  if (trimmed.length >= 16 && trimmed.length % 4 === 0 && /^[A-Za-z0-9+/=]+$/.test(trimmed)) {
    return { slug: 'base64-encoder', label: 'Base64 Encoder/Decoder', confidence: 'medium' };
  }

  // 6. HTML — starts with a tag
  if (/^\s*<[a-zA-Z]+[\s>]/.test(text)) {
    return { slug: 'html-formatter', label: 'HTML Formatter', confidence: 'medium' };
  }

  // 7. Markdown — headings, bold, links, or inline code
  if (/(^#+\s)|(\*\*.+\*\*)|(\[.+\]\(.+\))|(`.+`)/m.test(text)) {
    return { slug: 'markdown-to-html', label: 'Markdown', confidence: 'low' };
  }

  // 8. Fallback — homepage search
  return { slug: '', label: 'Toolhub', confidence: 'none' };
}
