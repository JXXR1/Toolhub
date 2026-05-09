TOOL = {
    "slug": "timestamp-converter",
    "category": "developer",
    "icon": "🕐",
    "tags": ["timestamp", "unix", "epoch", "date", "convert", "iso8601"],
    "i18n": {
        "en": {
            "name": "Unix Timestamp Converter",
            "tagline": "Convert between Unix timestamps and human-readable dates. Seconds and milliseconds, UTC and local.",
            "description": "Free online Unix timestamp converter. Convert between epoch seconds, milliseconds, ISO 8601, and human-readable dates in UTC or local time.",
        },
        "de": {"name": "Unix-Zeitstempel-Konverter", "tagline": "Konvertiere zwischen Unix-Zeitstempeln und lesbarem Datum. Sekunden und Millisekunden, UTC und lokal.", "description": "Kostenloser Unix-Zeitstempel-Konverter. Konvertiere zwischen Epoch-Sekunden, Millisekunden, ISO 8601 und lesbarem Datum."},
        "es": {"name": "Conversor de Timestamp Unix", "tagline": "Convierte entre timestamps Unix y fechas legibles. Segundos y milisegundos, UTC y local.", "description": "Conversor gratuito de timestamps Unix. Convierte entre segundos epoch, milisegundos, ISO 8601 y fechas legibles."},
        "fr": {"name": "Convertisseur Timestamp Unix", "tagline": "Convertissez entre timestamps Unix et dates lisibles. Secondes et millisecondes, UTC et local.", "description": "Convertisseur de timestamp Unix gratuit. Conversion entre secondes epoch, millisecondes, ISO 8601 et dates lisibles."},
        "it": {"name": "Convertitore Timestamp Unix", "tagline": "Converti tra timestamp Unix e date leggibili. Secondi e millisecondi, UTC e locale.", "description": "Convertitore gratuito di timestamp Unix. Conversione tra secondi epoch, millisecondi, ISO 8601 e date leggibili."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Unix timestamp</label>
      <input type="text" id="ts-num" oninput="tsFromNum()" placeholder="1704067200 or 1704067200000" style="font-family:ui-monospace,monospace">
      <div class="meta">Auto-detects seconds vs milliseconds</div>
    </div>
    <div>
      <label>Date &amp; time</label>
      <input type="datetime-local" id="ts-date" step="1" oninput="tsFromDate()">
      <div class="meta">Local timezone</div>
    </div>
  </div>
  <div class="button-row">
    <button onclick="tsNow()">Now</button>
    <button class="secondary" onclick="document.getElementById('ts-num').value=''; tsRender(null)">{LBL_CLEAR}</button>
  </div>
</div>
<div class="tool-card">
  <label>Result</label>
  <pre class="output" id="ts-out">{LBL_NO_INPUT}</pre>
</div>
""",
    "script": """
<script>
function tsRender(d){
  const out = document.getElementById('ts-out');
  if (!d){ out.textContent = '{LBL_NO_INPUT}'; return; }
  const ms = d.getTime();
  const sec = Math.floor(ms / 1000);
  const iso = d.toISOString();
  const local = d.toLocaleString(undefined, { weekday:'long', year:'numeric', month:'short', day:'2-digit', hour:'2-digit', minute:'2-digit', second:'2-digit' });
  const utc = d.toUTCString();
  // Relative
  const now = Date.now();
  const diffMs = ms - now;
  const abs = Math.abs(diffMs);
  let rel;
  const sec_ = Math.floor(abs/1000), min = Math.floor(sec_/60), hr = Math.floor(min/60), day = Math.floor(hr/24), yr = Math.floor(day/365);
  if (yr) rel = yr + 'y ' + (day - yr*365) + 'd';
  else if (day) rel = day + 'd ' + (hr - day*24) + 'h';
  else if (hr) rel = hr + 'h ' + (min - hr*60) + 'm';
  else if (min) rel = min + 'm ' + (sec_ - min*60) + 's';
  else rel = sec_ + 's';
  rel += diffMs >= 0 ? ' from now' : ' ago';
  out.textContent =
    'Unix seconds:       ' + sec + '\\n' +
    'Unix milliseconds:  ' + ms + '\\n' +
    'ISO 8601 (UTC):     ' + iso + '\\n' +
    'UTC:                ' + utc + '\\n' +
    'Local:              ' + local + '\\n' +
    'Relative:           ' + rel;
}
function tsFromNum(){
  const v = document.getElementById('ts-num').value.trim();
  if (!v){ tsRender(null); return; }
  const n = Number(v);
  if (!isFinite(n)){ tsRender(null); return; }
  // Heuristic: <= 10 digits = seconds, else ms
  const ms = (Math.abs(n) >= 1e12) ? n : (Math.abs(n) >= 1e10 ? n : n * 1000);
  const d = new Date(ms);
  // Update date input
  const pad = x => String(x).padStart(2,'0');
  document.getElementById('ts-date').value = d.getFullYear()+'-'+pad(d.getMonth()+1)+'-'+pad(d.getDate())+'T'+pad(d.getHours())+':'+pad(d.getMinutes())+':'+pad(d.getSeconds());
  tsRender(d);
}
function tsFromDate(){
  const v = document.getElementById('ts-date').value;
  if (!v){ tsRender(null); return; }
  const d = new Date(v);
  if (isNaN(d.getTime())){ tsRender(null); return; }
  document.getElementById('ts-num').value = Math.floor(d.getTime()/1000);
  tsRender(d);
}
function tsNow(){
  const d = new Date();
  document.getElementById('ts-num').value = Math.floor(d.getTime()/1000);
  const pad = x => String(x).padStart(2,'0');
  document.getElementById('ts-date').value = d.getFullYear()+'-'+pad(d.getMonth()+1)+'-'+pad(d.getDate())+'T'+pad(d.getHours())+':'+pad(d.getMinutes())+':'+pad(d.getSeconds());
  tsRender(d);
}
document.addEventListener('DOMContentLoaded', tsNow);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>A Unix timestamp is a single integer — the number of seconds (or milliseconds) since 1970-01-01 00:00:00 UTC. They're everywhere: log files, API responses, JWT <code>iat</code>/<code>exp</code> claims, database <code>created_at</code> columns, cache headers. They're unambiguous and timezone-free, but not human-readable, so when something breaks at <code>1735689600</code>, you need to know whether that's 2pm or 4am, today or last year. This tool flips between the integer form and the readable form in both directions, with seconds/ms auto-detection and a relative-time hint.</p>

<h3>When to use it</h3>
<ul>
  <li>Decoding a <code>"timestamp": 1735689600</code> field from a log entry or API response.</li>
  <li>Checking when a JWT was issued or when it expires (<code>iat</code> / <code>exp</code> claims are seconds-since-epoch).</li>
  <li>Calculating a future timestamp for a <code>retry-after</code> header, scheduled job, or cache TTL.</li>
  <li>Sanity-checking whether a date stored in a database is in seconds, milliseconds, or microseconds.</li>
  <li>Converting "now" into the format your tool of the moment wants.</li>
</ul>

<h3>Seconds, milliseconds, microseconds</h3>
<ul>
  <li><strong>Seconds</strong> — the original Unix convention; ~10 digits today (e.g. <code>1735689600</code>). Used in C, Linux, JWT, most APIs, most database <code>integer</code> columns.</li>
  <li><strong>Milliseconds</strong> — JavaScript's <code>Date.now()</code>, Java <code>System.currentTimeMillis()</code>, Kafka, many JSON APIs. ~13 digits.</li>
  <li><strong>Microseconds (16 digits) / nanoseconds (19 digits)</strong> — Python <code>time.time_ns()</code>, Go <code>time.Now().UnixNano()</code>, some metrics systems. This tool doesn't auto-handle them — divide by 1,000 or 1,000,000 first.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>The Year 2038 problem.</strong> Signed 32-bit timestamps overflow at <code>2147483647</code> = <strong>03:14:07 UTC, 19 January 2038</strong>. Old C code, MySQL <code>TIMESTAMP</code> columns, and embedded systems can wrap to 1901. Modern systems use 64-bit and are fine until ~year 292,277,026,596.</li>
  <li><strong>Unix time skips leap seconds.</strong> A Unix day is exactly 86,400 seconds, even when UTC has 86,401. This is by design (it keeps arithmetic simple) but means you can't use Unix timestamps for sub-second-accurate astronomy or GPS.</li>
  <li><strong>Negative timestamps</strong> are valid and represent dates before 1970. Some libraries reject them — test before relying on it.</li>
  <li><strong>Auto-detection isn't foolproof.</strong> A 10-digit value <em>could</em> be a millisecond timestamp from 1970 — vanishingly unlikely in practice, but if you know which unit you have, don't rely on the heuristic.</li>
  <li><strong>Always store UTC.</strong> Timestamps are timezone-free; "local time" is for display only. The "Local" line in the output uses your browser's zone, but the underlying integer is always UTC.</li>
</ul>
""",
    },
    "related": ["timezone-converter", "cron-parser", "date-calculator"],
}
