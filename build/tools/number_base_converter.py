TOOL = {
    "slug": "number-base-converter",
    "category": "developer",
    "icon": "0b",
    "tags": ["binary", "hex", "octal", "decimal", "base", "convert", "number"],
    "i18n": {
        "en": {
            "name": "Number Base Converter",
            "tagline": "Convert between binary, octal, decimal, hexadecimal, and any base from 2 to 36.",
            "description": "Free online number base converter. Convert between binary, octal, decimal, hex, and arbitrary bases 2-36. Handles negative numbers and large integers via BigInt.",
        },
        "de": {
            "name": "Zahlensystem-Konverter",
            "tagline": "Konvertiere zwischen binär, oktal, dezimal, hexadezimal und beliebigen Basen von 2 bis 36.",
            "description": "Kostenloser Zahlensystem-Konverter. Konvertiere zwischen binär, oktal, dezimal, hexadezimal und beliebiger Basis 2-36. Auch negative und große Zahlen via BigInt.",
        },
        "es": {
            "name": "Conversor de Bases Numéricas",
            "tagline": "Convierte entre binario, octal, decimal, hexadecimal y cualquier base de 2 a 36.",
            "description": "Conversor gratuito de bases numéricas. Convierte entre binario, octal, decimal, hexadecimal y cualquier base 2-36. Soporta negativos y enteros grandes con BigInt.",
        },
        "fr": {
            "name": "Convertisseur de Bases",
            "tagline": "Convertissez entre binaire, octal, décimal, hexadécimal et toute base de 2 à 36.",
            "description": "Convertisseur de bases numériques gratuit. Convertissez entre binaire, octal, décimal, hex et bases arbitraires 2-36. Gère les nombres négatifs et grands entiers via BigInt.",
        },
        "it": {
            "name": "Convertitore Basi Numeriche",
            "tagline": "Converti tra binario, ottale, decimale, esadecimale e qualsiasi base da 2 a 36.",
            "description": "Convertitore gratuito di basi numeriche. Converti tra binario, ottale, decimale, esadecimale e basi arbitrarie 2-36. Supporta negativi e interi grandi con BigInt.",
        },
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>{LBL_INPUT}</label>
      <input type="text" id="nb-in" oninput="nbRun()" placeholder="42" value="42" style="font-family:ui-monospace,monospace">
    </div>
    <div>
      <label>{LBL_FROM} (base)</label>
      <select id="nb-from" onchange="nbRun()">
        <option value="2">2 — binary</option>
        <option value="8">8 — octal</option>
        <option value="10" selected>10 — decimal</option>
        <option value="16">16 — hexadecimal</option>
        <option value="36">36</option>
        <option value="other">Other (2-36)…</option>
      </select>
      <input type="number" id="nb-from-other" min="2" max="36" placeholder="custom base" oninput="nbRun()" style="display:none;margin-top:0.4rem">
    </div>
  </div>
</div>
<div class="tool-card">
  <label>All bases</label>
  <table>
    <tr><th style="width:140px">Base</th><th>Value</th></tr>
    <tr><td>2 (binary)</td><td><code id="nb-bin">…</code></td></tr>
    <tr><td>8 (octal)</td><td><code id="nb-oct">…</code></td></tr>
    <tr><td>10 (decimal)</td><td><code id="nb-dec">…</code></td></tr>
    <tr><td>16 (hex)</td><td><code id="nb-hex">…</code></td></tr>
    <tr><td>32</td><td><code id="nb-32">…</code></td></tr>
    <tr><td>36</td><td><code id="nb-36">…</code></td></tr>
  </table>
  <div class="meta" id="nb-meta"></div>
</div>
""",
    "script": """
<script>
function nbValidate(s, base){
  // Accept optional leading minus, but BigInt with arbitrary base needs custom parsing
  if (!s) return null;
  s = s.trim();
  let neg = false;
  if (s.startsWith('-')){ neg = true; s = s.slice(1); }
  if (!s.length) return null;
  // Strip leading 0x/0o/0b/# prefix lenience for base 10 input — only when base hints
  if (base === 16 && (s.startsWith('0x') || s.startsWith('0X') || s.startsWith('#'))) s = s.replace(/^0x|^0X|^#/,'');
  if (base === 2 && (s.startsWith('0b') || s.startsWith('0B'))) s = s.slice(2);
  if (base === 8 && (s.startsWith('0o') || s.startsWith('0O'))) s = s.slice(2);
  s = s.replace(/_/g, ''); // allow digit grouping with underscores
  // Validate against alphabet
  const alpha = '0123456789abcdefghijklmnopqrstuvwxyz'.slice(0, base);
  for (const ch of s.toLowerCase()){
    if (!alpha.includes(ch)) throw new Error('Invalid digit `' + ch + '` for base ' + base);
  }
  let val = 0n;
  for (const ch of s.toLowerCase()) val = val * BigInt(base) + BigInt(alpha.indexOf(ch));
  return neg ? -val : val;
}

function nbToBase(big, base){
  if (big === 0n) return '0';
  const neg = big < 0n;
  let n = neg ? -big : big;
  const alpha = '0123456789abcdefghijklmnopqrstuvwxyz';
  let out = '';
  while (n > 0n){
    out = alpha[Number(n % BigInt(base))] + out;
    n = n / BigInt(base);
  }
  return (neg ? '-' : '') + out;
}

function nbRun(){
  const sel = document.getElementById('nb-from');
  const otherInput = document.getElementById('nb-from-other');
  otherInput.style.display = sel.value === 'other' ? 'block' : 'none';
  let base = sel.value === 'other' ? parseInt(otherInput.value, 10) : parseInt(sel.value, 10);
  const inp = document.getElementById('nb-in').value;
  const meta = document.getElementById('nb-meta');
  const ids = ['nb-bin','nb-oct','nb-dec','nb-hex','nb-32','nb-36'];
  if (!base || base < 2 || base > 36){ meta.textContent = 'Pick a base between 2 and 36'; return; }
  try {
    const big = nbValidate(inp, base);
    if (big === null){ ids.forEach(id => document.getElementById(id).textContent = '—'); meta.textContent = ''; return; }
    document.getElementById('nb-bin').textContent = nbToBase(big, 2);
    document.getElementById('nb-oct').textContent = nbToBase(big, 8);
    document.getElementById('nb-dec').textContent = big.toString();
    document.getElementById('nb-hex').textContent = nbToBase(big, 16).toUpperCase();
    document.getElementById('nb-32').textContent = nbToBase(big, 32);
    document.getElementById('nb-36').textContent = nbToBase(big, 36);
    const bits = big < 0n ? (-big).toString(2).length + 1 : big.toString(2).length;
    meta.textContent = bits + ' bits';
  } catch(e){
    meta.textContent = '✗ ' + e.message;
    ids.forEach(id => document.getElementById(id).textContent = '—');
  }
}
document.addEventListener('DOMContentLoaded', nbRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Numbers are the same number regardless of base — <code>255</code>, <code>0xff</code>, <code>0b11111111</code>, and <code>0o377</code> are identical. But which base you read or write in matters when you're translating between memory layouts, parsing colour codes, decoding bit fields, or just reading hex from a debugger. This tool converts between binary, octal, decimal, hexadecimal, and any base from 2 to 36, using BigInt under the hood so you don't lose precision on large numbers.</p>

<h3>When to use it</h3>
<ul>
  <li>Reading a hex value from a stack trace and figuring out what it is in decimal.</li>
  <li>Converting CSS colour <code>0xff8800</code> into an RGB triple, or vice versa.</li>
  <li>Inspecting a bitmask or flags integer in binary to see which bits are set.</li>
  <li>Translating between base-36 short IDs and decimal counters.</li>
</ul>

<h3>Recognised prefixes</h3>
<ul>
  <li>Hex: <code>0x</code>, <code>0X</code>, <code>#</code></li>
  <li>Binary: <code>0b</code>, <code>0B</code></li>
  <li>Octal: <code>0o</code>, <code>0O</code></li>
  <li>Underscore digit grouping: <code>1_000_000</code></li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Negative numbers are sign-prefixed, not two's complement.</strong> <code>-128</code> is shown as <code>-10000000</code> in binary, not <code>10000000</code>. Most languages display the same way for arbitrary-precision integers.</li>
  <li><strong>Big numbers don't lose precision here.</strong> JavaScript <code>Number</code> caps at 2<sup>53</sup>; this tool uses <code>BigInt</code>, so 64-bit integers, large hashes, and crypto values all round-trip exactly.</li>
  <li><strong>Don't confuse base with case.</strong> Base-16 letters can be upper or lower; the tool accepts both and emits uppercase. Base-32 / base-36 outputs are lowercase by convention.</li>
  <li><strong>Leading zeros are dropped.</strong> <code>0x000F</code> becomes <code>F</code>. If you need a fixed-width hex (e.g. for byte representations), pad in your code afterward.</li>
</ul>
""",
    },
    "related": ["base64-encoder", "hash-generator", "uuid-generator"],
}
