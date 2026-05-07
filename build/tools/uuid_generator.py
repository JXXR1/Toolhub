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
<h2>v4 vs v7 — which should I use?</h2>
<ul>
  <li><strong>v4 (random)</strong> — 122 bits of randomness, no information about creation time. Use for IDs you don't want to leak ordering or timing.</li>
  <li><strong>v7 (time-ordered)</strong> — 48-bit Unix-ms timestamp prefix + random tail. Sorts in roughly chronological order, plays well with database indexes (B-tree locality), supersedes ULID/v6/v1 for most modern needs. Specified in RFC 9562.</li>
</ul>
<h3>How it's generated</h3>
<p>Both versions are RFC-compliant. Random bytes come from your browser's <code>crypto.getRandomValues</code> — never from <code>Math.random</code> or a server.</p>
""",
    },
    "related": ["password-generator", "hash-generator", "timestamp-converter"],
}
