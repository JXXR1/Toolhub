TOOL = {
    "slug": "timezone-converter",
    "category": "data",
    "icon": "🌍",
    "tags": ["timezone", "tz", "convert", "utc", "date", "time", "iana"],
    "i18n": {
        "en": {
            "name": "Time Zone Converter",
            "tagline": "Convert a date and time between IANA time zones. See offsets, DST status, and weekday for both ends.",
            "description": "Free online time zone converter. Convert between any IANA time zones with DST awareness. Pick from common zones or any of the ~400+ supported by your browser.",
        },
        "de": {
            "name": "Zeitzonen-Konverter",
            "tagline": "Konvertiere Datum und Uhrzeit zwischen IANA-Zeitzonen. Mit Offsets, Sommerzeit und Wochentag.",
            "description": "Kostenloser Zeitzonen-Konverter. Konvertiert zwischen IANA-Zeitzonen inklusive Sommerzeit. Wähle aus gängigen oder den über 400 vom Browser unterstützten Zonen.",
        },
        "es": {
            "name": "Conversor de Zonas Horarias",
            "tagline": "Convierte fecha y hora entre zonas horarias IANA. Muestra offsets, horario de verano y día de la semana.",
            "description": "Conversor gratuito de zonas horarias. Convierte entre zonas IANA con conciencia del horario de verano. Selecciona de zonas comunes o de las 400+ del navegador.",
        },
        "fr": {
            "name": "Convertisseur de Fuseaux",
            "tagline": "Convertissez date et heure entre fuseaux horaires IANA. Affiche décalages, heure d'été et jour de la semaine.",
            "description": "Convertisseur de fuseaux horaires gratuit. Conversion entre fuseaux IANA avec gestion de l'heure d'été. Choisissez parmi les zones communes ou les 400+ supportées par votre navigateur.",
        },
        "it": {
            "name": "Convertitore Fusi Orari",
            "tagline": "Converti data e ora tra fusi orari IANA. Mostra offset, ora legale e giorno della settimana.",
            "description": "Convertitore di fusi orari gratuito. Conversione tra fusi IANA con consapevolezza dell'ora legale. Seleziona tra i fusi comuni o gli oltre 400 supportati dal browser.",
        },
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Date &amp; time (in source zone)</label>
      <input type="datetime-local" id="tz-when" oninput="tzRun()" step="1">
    </div>
    <div>
      <label>{LBL_FROM} (source zone)</label>
      <select id="tz-from" onchange="tzRun()"></select>
    </div>
  </div>
  <div class="row-2col" style="margin-top:1rem">
    <div>
      <label>{LBL_TO} (target zone)</label>
      <select id="tz-to" onchange="tzRun()"></select>
    </div>
    <div>
      <label>&nbsp;</label>
      <button class="secondary" onclick="tzNow()" style="width:100%">Now</button>
    </div>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <pre class="output" id="tz-out">{LBL_NO_INPUT}</pre>
</div>
""",
    "script": """
<script>
const TZ_COMMON = [
  'UTC','Europe/London','Europe/Paris','Europe/Berlin','Europe/Bratislava','Europe/Madrid','Europe/Rome','Europe/Athens','Europe/Moscow',
  'Africa/Cairo','Africa/Lagos','Africa/Johannesburg',
  'Asia/Dubai','Asia/Karachi','Asia/Kolkata','Asia/Bangkok','Asia/Singapore','Asia/Shanghai','Asia/Tokyo','Asia/Seoul',
  'Australia/Perth','Australia/Sydney','Pacific/Auckland',
  'America/New_York','America/Toronto','America/Chicago','America/Denver','America/Los_Angeles','America/Anchorage','America/Sao_Paulo','America/Mexico_City'
];

function tzPopulate(){
  const local = Intl.DateTimeFormat().resolvedOptions().timeZone;
  let all = TZ_COMMON.slice();
  if (Intl.supportedValuesOf){
    try { all = Intl.supportedValuesOf('timeZone'); } catch(e){}
  }
  if (!all.includes(local)) all = [local, ...all];
  for (const sel of [document.getElementById('tz-from'), document.getElementById('tz-to')]){
    sel.innerHTML = all.map(z => `<option value="${z}">${z}</option>`).join('');
  }
  document.getElementById('tz-from').value = local;
  document.getElementById('tz-to').value = 'UTC';
}

function tzNow(){
  const d = new Date();
  const local = Intl.DateTimeFormat().resolvedOptions().timeZone;
  document.getElementById('tz-from').value = local;
  // Format current local date for datetime-local input
  const pad = n => String(n).padStart(2,'0');
  document.getElementById('tz-when').value = d.getFullYear()+'-'+pad(d.getMonth()+1)+'-'+pad(d.getDate())+'T'+pad(d.getHours())+':'+pad(d.getMinutes())+':'+pad(d.getSeconds());
  tzRun();
}

function tzGetOffsetMinutes(date, tz){
  // Get the minutes offset of `date` (an instant) in `tz`, vs UTC
  const dtf = new Intl.DateTimeFormat('en-US', {
    timeZone: tz, hour12: false,
    year:'numeric', month:'2-digit', day:'2-digit',
    hour:'2-digit', minute:'2-digit', second:'2-digit'
  });
  const parts = Object.fromEntries(dtf.formatToParts(date).filter(p=>p.type!=='literal').map(p=>[p.type,p.value]));
  const asLocal = Date.UTC(parts.year, parts.month-1, parts.day, parts.hour==='24'?0:parts.hour, parts.minute, parts.second);
  return Math.round((asLocal - date.getTime()) / 60000);
}

function tzFormatOffset(min){
  const sign = min < 0 ? '-' : '+';
  const a = Math.abs(min);
  return sign + String(Math.floor(a/60)).padStart(2,'0') + ':' + String(a%60).padStart(2,'0');
}

function tzRun(){
  const whenStr = document.getElementById('tz-when').value;
  const from = document.getElementById('tz-from').value;
  const to = document.getElementById('tz-to').value;
  const out = document.getElementById('tz-out');
  out.classList.remove('error');
  if (!whenStr || !from || !to){ out.textContent = '{LBL_NO_INPUT}'; return; }
  // Parse the wall-clock time as if it's in the source zone.
  // Strategy: build a Date from the wall-clock as if UTC, then shift by the source-zone offset.
  const m = whenStr.match(/^(\\d{4})-(\\d{2})-(\\d{2})T(\\d{2}):(\\d{2})(?::(\\d{2}))?/);
  if (!m){ out.classList.add('error'); out.textContent = 'Invalid date'; return; }
  const utcMs = Date.UTC(+m[1], +m[2]-1, +m[3], +m[4], +m[5], +(m[6]||0));
  const probe = new Date(utcMs);
  const fromOff = tzGetOffsetMinutes(probe, from);
  // The actual instant: utcMs minus the source zone offset gives the true UTC instant for the wall-clock time
  const instant = new Date(utcMs - fromOff * 60000);
  const toFmt = new Intl.DateTimeFormat(undefined, {
    timeZone: to, weekday:'short', year:'numeric', month:'short', day:'2-digit',
    hour:'2-digit', minute:'2-digit', second:'2-digit', timeZoneName:'short', hour12: false
  });
  const fromFmt = new Intl.DateTimeFormat(undefined, {
    timeZone: from, weekday:'short', year:'numeric', month:'short', day:'2-digit',
    hour:'2-digit', minute:'2-digit', second:'2-digit', timeZoneName:'short', hour12: false
  });
  const toOff = tzGetOffsetMinutes(instant, to);
  out.textContent =
    'Source:  ' + fromFmt.format(instant) + '\\n' +
    '         (' + from + ', UTC' + tzFormatOffset(fromOff) + ')\\n\\n' +
    'Target:  ' + toFmt.format(instant) + '\\n' +
    '         (' + to + ', UTC' + tzFormatOffset(toOff) + ')\\n\\n' +
    'Diff:    ' + Math.abs(toOff - fromOff) + ' min (' + ((toOff-fromOff)/60).toFixed(2) + ' h)\\n' +
    'UTC:     ' + instant.toISOString().replace('T',' ').slice(0,19) + 'Z\\n' +
    'Unix:    ' + Math.floor(instant.getTime()/1000);
}
document.addEventListener('DOMContentLoaded', () => { tzPopulate(); tzNow(); });
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Time zones are deceptively annoying. A meeting at "9am" means different absolute moments in London, Bratislava, and New York — and the offset between any two of them changes twice a year because of daylight saving, on different dates. This tool takes a wall-clock time in one IANA zone and tells you the exact equivalent in another, with current offsets, the UTC instant, and the day-of-week for both ends.</p>

<h3>When to use it</h3>
<ul>
  <li>Scheduling a call across continents — confirming what "3pm CET" is in your colleague's zone.</li>
  <li>Reading a log timestamp recorded in UTC and translating it to local time for a user-facing report.</li>
  <li>Checking whether a deploy window or maintenance slot crosses a DST boundary.</li>
  <li>Sanity-checking that a cron expression in <code>America/New_York</code> fires at the moment you expect from your own zone.</li>
  <li>Working out the day-of-week change when crossing the international date line.</li>
</ul>

<h3>Why IANA zones (not "GMT+2")</h3>
<p>An IANA zone like <code>Europe/Bratislava</code> or <code>America/New_York</code> encodes the historical and ongoing rules for that location — DST start and end dates, time-zone changes (Russia abolished DST in 2014; Türkiye dropped DST in 2016), even Samoa skipping a whole day in 2011. A bare offset like "GMT+2" tells you nothing about whether DST applies, what the rule was last year, or what it'll be next year. Browsers ship the IANA database (via ICU/CLDR) and update it automatically, so the conversion stays correct over time.</p>

<h3>Common gotchas</h3>
<ul>
  <li><strong>DST transitions create ambiguous and missing times.</strong> When a clock falls back, 02:30 happens twice; when it springs forward, 02:30 doesn't exist at all. The tool picks the standard-time interpretation by default; if you need the other side, shift by an hour either way.</li>
  <li><strong>Offsets aren't constants.</strong> "CET" is UTC+1 in winter and UTC+2 in summer (CEST). The output always shows the actual offset for the date you entered, so trust the displayed offset over the abbreviation.</li>
  <li><strong>Country abbreviations are not zones.</strong> "EST" is ambiguous (US vs Australian); "IST" can mean Indian, Irish, or Israeli. Always pick the IANA zone, not the abbreviation.</li>
  <li><strong>Historical accuracy</strong> is good for the modern era but breaks down for very old dates. Pre-1970 timestamps may use approximated offsets in some browsers.</li>
  <li><strong>Storing dates: always use UTC.</strong> Convert at display time. The UTC line in the output gives you the canonical value to write to your database.</li>
</ul>
""",
    },
    "related": ["timestamp-converter", "date-calculator", "cron-parser"],
}
