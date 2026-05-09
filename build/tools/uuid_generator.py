TOOL = {
    "slug": "uuid-generator",
    "category": "developer",
    "icon": "🆔",
    "tags": ["uuid", "guid", "v4", "v7", "random", "unique", "identifier"],
    "i18n": {
        "en": {
            "name": "UUID Generator",
            "tagline": "Generate RFC 4122 UUIDs (v4 random or v7 time-ordered). Batch up to 100. Cryptographically secure.",
            "description": "Free online UUID generator. RFC 4122 v4 (random) and v7 (time-ordered, sortable). Generate one or many at a time, all in your browser.",
        },
        "de": {
            "name": "UUID-Generator",
            "tagline": "RFC 4122 UUIDs erzeugen (v4 zufällig oder v7 zeitgeordnet). Bis zu 100 auf einmal. Kryptographisch sicher.",
            "description": "Kostenloser UUID-Generator. RFC 4122 v4 (zufällig) und v7 (zeitgeordnet, sortierbar). Einzeln oder im Stapel erzeugen, alles im Browser.",
        },
        "es": {
            "name": "Generador UUID",
            "tagline": "Genera UUIDs RFC 4122 (v4 aleatorio o v7 ordenado por tiempo). Hasta 100 por lote. Criptográficamente seguro.",
            "description": "Generador UUID gratuito en línea. RFC 4122 v4 (aleatorio) y v7 (ordenado por tiempo). Genera uno o varios, todo en tu navegador.",
        },
        "fr": {
            "name": "Générateur UUID",
            "tagline": "Générez des UUIDs RFC 4122 (v4 aléatoire ou v7 ordonné par temps). Jusqu'à 100 à la fois. Cryptographiquement sûr.",
            "description": "Générateur UUID gratuit en ligne. RFC 4122 v4 (aléatoire) et v7 (ordonné par temps, triable). Un ou plusieurs, tout dans votre navigateur.",
        },
        "it": {
            "name": "Generatore UUID",
            "tagline": "Genera UUID RFC 4122 (v4 casuale o v7 ordinato per tempo). Fino a 100 per batch. Crittograficamente sicuro.",
            "description": "Generatore UUID gratuito online. RFC 4122 v4 (casuale) e v7 (ordinato per tempo, ordinabile). Uno o molti, tutto nel browser.",
        },
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Version</label>
      <select id="uuid-ver">
        <option value="4">v4 (random)</option>
        <option value="7">v7 (time-ordered, sortable)</option>
      </select>
    </div>
    <div>
      <label>{LBL_COUNT} (1-100)</label>
      <input type="number" id="uuid-count" value="1" min="1" max="100">
    </div>
  </div>
  <div class="button-row">
    <button onclick="uuidGen()">{LBL_GENERATE}</button>
    <button class="secondary" onclick="copyOutput('uuid-out', this)">{LBL_COPY}</button>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <pre class="output" id="uuid-out"></pre>
</div>
""",
    "script": """
<script>
function uuidV4(){
  const b = new Uint8Array(16);
  crypto.getRandomValues(b);
  b[6] = (b[6] & 0x0f) | 0x40;
  b[8] = (b[8] & 0x3f) | 0x80;
  const h = [...b].map(x => x.toString(16).padStart(2,'0'));
  return h.slice(0,4).join('') + '-' + h.slice(4,6).join('') + '-' + h.slice(6,8).join('') + '-' + h.slice(8,10).join('') + '-' + h.slice(10,16).join('');
}
function uuidV7(){
  // RFC 9562 v7: 48-bit unix-ms timestamp + 12 bits rand_a + 62 bits rand_b + version/variant bits
  const ts = BigInt(Date.now());
  const r = new Uint8Array(10);
  crypto.getRandomValues(r);
  const b = new Uint8Array(16);
  // 6 bytes of timestamp (big-endian)
  for (let i = 0; i < 6; i++) b[i] = Number((ts >> BigInt(40 - 8*i)) & 0xffn);
  for (let i = 0; i < 10; i++) b[i+6] = r[i];
  b[6] = (b[6] & 0x0f) | 0x70;     // version 7
  b[8] = (b[8] & 0x3f) | 0x80;     // variant 10
  const h = [...b].map(x => x.toString(16).padStart(2,'0'));
  return h.slice(0,4).join('') + '-' + h.slice(4,6).join('') + '-' + h.slice(6,8).join('') + '-' + h.slice(8,10).join('') + '-' + h.slice(10,16).join('');
}
function uuidGen(){
  const ver = document.getElementById('uuid-ver').value;
  const n = Math.max(1, Math.min(100, parseInt(document.getElementById('uuid-count').value, 10) || 1));
  const out = [];
  for (let i = 0; i < n; i++) out.push(ver === '7' ? uuidV7() : uuidV4());
  document.getElementById('uuid-out').textContent = out.join('\\n');
}
document.addEventListener('DOMContentLoaded', uuidGen);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>A UUID (or GUID) is a 128-bit identifier — written as 32 hex digits in 5 groups, like <code>550e8400-e29b-41d4-a716-446655440000</code>. They're collision-free across systems without coordination: any process anywhere can mint one and the chance of two ever colliding is effectively zero. Useful when you need an ID before talking to a database, when you want to avoid leaking row counts, or when an ID has to be generated client-side and synced later. This tool emits RFC 4122 / RFC 9562 compliant UUIDs in v4 (random) or v7 (time-ordered) form, generated with cryptographically-secure randomness in your browser.</p>

<h3>When to use it</h3>
<ul>
  <li>Primary keys for distributed systems where you don't want to round-trip to the database for an ID.</li>
  <li>Idempotency keys for API requests (stripe, payment providers, queue messages).</li>
  <li>File-upload identifiers, session tokens, correlation IDs in logs.</li>
  <li>Anywhere you'd otherwise expose an auto-incrementing ID and leak how many records you have.</li>
  <li>Test data — seed a hundred records with realistic identifiers in one click.</li>
</ul>

<h3>v4 vs v7 — which should I use?</h3>
<ul>
  <li><strong>v4 (random)</strong> — 122 bits of randomness, no embedded creation time. Use when you want zero correlation between IDs and creation order, or when the ID will live in a hash-map / non-clustered index where ordering doesn't matter.</li>
  <li><strong>v7 (time-ordered)</strong> — 48-bit Unix-ms timestamp prefix + random tail. <strong>Default to this for new database primary keys.</strong> The timestamp prefix gives B-tree indexes locality (recent inserts go to the same pages, much better cache behaviour than v4), and IDs sort in roughly chronological order. Defined in RFC 9562 (May 2024) — supersedes ULID and v1/v6 for most use cases.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>UUIDs are not secrets.</strong> v4 has 122 bits of entropy and is unguessable, but the format itself doesn't authorize anything. Don't use a UUID as a session token or password-reset token unless you're treating it as a secret (HTTPS-only, time-limited, single-use).</li>
  <li><strong>v7 leaks creation time.</strong> The first 48 bits encode the millisecond it was minted. Fine for internal IDs; bad if you don't want users to learn when records were created. Use v4 in that case.</li>
  <li><strong>Index size matters.</strong> A UUID is 16 bytes vs 8 for a bigint — your B-tree indexes get bigger. Worth it for distributed/no-coordination, often not worth it for single-server apps with a sequential ID.</li>
  <li><strong>v4 fragments database indexes.</strong> Random IDs scatter writes across the index, hurting page cache hit rate and write throughput. This is the original argument for v7.</li>
  <li><strong>Don't use v1.</strong> The old time-and-MAC variant leaks the generating machine's MAC address. v7 is the modern replacement.</li>
  <li><strong>Use crypto-secure randomness.</strong> This tool uses <code>crypto.getRandomValues</code>; never roll your own with <code>Math.random</code> — it's not random enough and IDs become predictable.</li>
</ul>
""",
    },
    "related": ["password-generator", "hash-generator", "timestamp-converter"],
}
