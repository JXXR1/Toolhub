TOOL = {
    "slug": "jwt-decoder",
    "category": "developer",
    "icon": "🔓",
    "tags": ["jwt", "json web token", "decode", "auth", "oauth", "openid"],
    "i18n": {
        "en": {
            "name": "JWT Decoder",
            "tagline": "Paste a JWT to decode its header and payload. All decoding runs in your browser — tokens never leave the page.",
            "description": "Free online JSON Web Token decoder. Decode header and payload, verify expiry timestamps, inspect signature. Works fully offline in your browser.",
        },
        "de": {
            "name": "JWT-Decoder",
            "tagline": "JWT einfügen, um Header und Payload zu dekodieren. Alles läuft im Browser — Tokens verlassen die Seite nicht.",
            "description": "Kostenloser JSON Web Token Decoder. Header und Payload dekodieren, Ablaufzeit prüfen, Signatur ansehen. Vollständig offline im Browser.",
        },
        "es": {
            "name": "Decodificador JWT",
            "tagline": "Pega un JWT para decodificar su header y payload. Todo se ejecuta en tu navegador — los tokens nunca se envían.",
            "description": "Decodificador JSON Web Token gratuito. Decodifica header y payload, verifica caducidad, inspecciona la firma. Funciona offline en tu navegador.",
        },
        "fr": {
            "name": "Décodeur JWT",
            "tagline": "Collez un JWT pour décoder son en-tête et son payload. Tout est traité localement — les tokens ne quittent pas la page.",
            "description": "Décodeur JSON Web Token gratuit. Décode en-tête et payload, vérifie l'expiration, inspecte la signature. Fonctionne hors-ligne dans votre navigateur.",
        },
        "it": {
            "name": "Decoder JWT",
            "tagline": "Incolla un JWT per decodificare header e payload. Tutto viene eseguito nel browser — i token non lasciano la pagina.",
            "description": "Decoder JSON Web Token gratuito. Decodifica header e payload, verifica scadenza, ispeziona la firma. Funziona offline nel browser.",
        },
    },
    "body": """
<div class="tool-card">
  <label>JWT</label>
  <textarea id="jwt-in" placeholder="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." spellcheck="false" oninput="jwtDecode()"></textarea>
  <div class="meta" id="jwt-summary"></div>
</div>
<div class="tool-card">
  <label>Header</label>
  <pre class="output" id="jwt-header">{LBL_NO_INPUT}</pre>
</div>
<div class="tool-card">
  <label>Payload</label>
  <pre class="output" id="jwt-payload">{LBL_NO_INPUT}</pre>
</div>
<div class="tool-card">
  <label>Signature (base64url, not verified)</label>
  <pre class="output" id="jwt-sig">{LBL_NO_INPUT}</pre>
  <div class="meta">This tool decodes only — it does not verify the signature against a key. Treat decoded payload as untrusted until verified.</div>
</div>
""",
    "script": """
<script>
function b64urlDecode(s){
  s = s.replace(/-/g,'+').replace(/_/g,'/');
  while (s.length % 4) s += '=';
  try {
    const bin = atob(s);
    // utf-8 decode
    const bytes = new Uint8Array(bin.length);
    for (let i=0;i<bin.length;i++) bytes[i] = bin.charCodeAt(i);
    return new TextDecoder('utf-8').decode(bytes);
  } catch(e){ return null; }
}
function jwtPretty(s){
  try { return JSON.stringify(JSON.parse(s), null, 2); }
  catch(e){ return s; }
}
function jwtDecode(){
  const tok = document.getElementById('jwt-in').value.trim();
  const hdr = document.getElementById('jwt-header');
  const pld = document.getElementById('jwt-payload');
  const sig = document.getElementById('jwt-sig');
  const sum = document.getElementById('jwt-summary');
  hdr.classList.remove('error'); pld.classList.remove('error'); sig.classList.remove('error');
  if (!tok){ hdr.textContent='{LBL_NO_INPUT}'; pld.textContent='{LBL_NO_INPUT}'; sig.textContent='{LBL_NO_INPUT}'; sum.textContent=''; return; }
  const parts = tok.split('.');
  if (parts.length !== 3){
    hdr.classList.add('error');
    hdr.textContent = '✗ Invalid JWT — expected 3 dot-separated parts (header.payload.signature)';
    pld.textContent = ''; sig.textContent = ''; sum.textContent = parts.length + ' parts found';
    return;
  }
  const h = b64urlDecode(parts[0]);
  const p = b64urlDecode(parts[1]);
  if (h === null){ hdr.classList.add('error'); hdr.textContent = '✗ Header is not valid base64url'; }
  else hdr.textContent = jwtPretty(h);
  if (p === null){ pld.classList.add('error'); pld.textContent = '✗ Payload is not valid base64url'; }
  else pld.textContent = jwtPretty(p);
  sig.textContent = parts[2] || '(empty signature)';
  // Summary: alg + exp/iat status
  let parts2 = [];
  try {
    const hj = JSON.parse(h);
    if (hj.alg) parts2.push('alg: ' + hj.alg);
  } catch(e){}
  try {
    const pj = JSON.parse(p);
    const now = Math.floor(Date.now()/1000);
    if (pj.exp){
      const d = new Date(pj.exp*1000);
      parts2.push('exp: ' + d.toISOString().replace('T',' ').slice(0,19) + 'Z' + (pj.exp < now ? ' ⚠ EXPIRED' : ''));
    }
    if (pj.iat){
      const d = new Date(pj.iat*1000);
      parts2.push('iat: ' + d.toISOString().replace('T',' ').slice(0,19) + 'Z');
    }
    if (pj.iss) parts2.push('iss: ' + pj.iss);
    if (pj.sub) parts2.push('sub: ' + pj.sub);
  } catch(e){}
  sum.textContent = parts2.join(' · ');
}
document.addEventListener('DOMContentLoaded', jwtDecode);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>A JWT (JSON Web Token) is three base64url-encoded parts joined by dots: <code>header.payload.signature</code>. The header and payload are JSON objects you can inspect; the signature proves the token wasn't tampered with after issuance. This tool decodes the first two parts so you can see what's inside without the noise of base64 — useful when debugging auth flows, expired sessions, or "which user is this token for, exactly?".</p>

<h3>When to use it</h3>
<ul>
  <li>Debugging an OAuth / OpenID Connect login that's failing — paste the access or ID token, see what the IdP actually issued.</li>
  <li>Confirming token expiry: the tool decodes <code>exp</code> as a real date and flags it if it's in the past.</li>
  <li>Sanity-checking custom claims a backend is asserting (roles, permissions, tenant IDs).</li>
  <li>Reading a token your library "rejected as invalid" to see whether the issue is structural, expiry, or signature.</li>
</ul>

<h3>Common claims</h3>
<ul>
  <li><code>iss</code> — issuer (who created the token)</li>
  <li><code>sub</code> — subject (the user/account it represents)</li>
  <li><code>aud</code> — audience (who should accept it)</li>
  <li><code>exp</code> — expiry (Unix timestamp)</li>
  <li><code>iat</code> — issued-at (Unix timestamp)</li>
  <li><code>nbf</code> — not-valid-before (Unix timestamp)</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>A decoded JWT is NOT a verified JWT.</strong> The signature isn't checked here — that requires the issuer's public key (RSA/EC) or shared secret (HMAC). Decoded contents tell you what the token <em>says</em>, not whether you should trust it. Always verify on the server before honouring claims.</li>
  <li><strong>Don't paste production tokens into anywhere.</strong> Anyone with a live JWT can impersonate the user until <code>exp</code>. The browser doesn't transmit it from this tool, but extensions, screen-recordings, and dev tools can. Use a fresh token from a test environment if you need to share.</li>
  <li><strong><code>alg: none</code> tokens are a known attack class.</strong> If a header has <code>alg: none</code> and your library accepts it, attackers can forge tokens. Reject this on the server.</li>
  <li><strong>Time skew matters.</strong> A token's <code>exp</code> is checked against the verifier's clock. Servers with drift fail tokens that look valid here.</li>
</ul>
""",
    },
    "related": ["base64-encoder", "json-formatter", "hash-generator"],
}
