TOOL = {
    "slug": "cron-parser",
    "category": "developer",
    "icon": "🕒",
    "tags": ["cron", "schedule", "crontab", "next run", "expression"],
    "i18n": {
        "en": {
            "name": "Cron Expression Parser",
            "tagline": "Parse cron expressions and see the next 10 fire times. Standard 5-field crontab.",
            "description": "Free online cron expression parser. Validates 5-field crontab syntax and lists the next 10 scheduled fire times in your local timezone.",
        },
        "de": {
            "name": "Cron-Ausdruck-Parser",
            "tagline": "Cron-Ausdrücke parsen und die nächsten 10 Auslösezeiten anzeigen. Standard 5-Felder-Crontab.",
            "description": "Kostenloser Cron-Ausdruck-Parser. Validiert die 5-Felder-Crontab-Syntax und listet die nächsten 10 Ausführungszeitpunkte in deiner Zeitzone.",
        },
        "es": {
            "name": "Analizador de Cron",
            "tagline": "Analiza expresiones cron y ve las próximas 10 ejecuciones. Crontab estándar de 5 campos.",
            "description": "Analizador de expresiones cron gratuito. Valida la sintaxis crontab de 5 campos y muestra las próximas 10 ejecuciones en tu zona horaria.",
        },
        "fr": {
            "name": "Analyseur Cron",
            "tagline": "Analysez les expressions cron et voyez les 10 prochaines exécutions. Crontab standard à 5 champs.",
            "description": "Analyseur d'expressions cron gratuit. Valide la syntaxe crontab à 5 champs et affiche les 10 prochaines exécutions dans votre fuseau horaire.",
        },
        "it": {
            "name": "Analizzatore Cron",
            "tagline": "Analizza espressioni cron e vedi le prossime 10 esecuzioni. Crontab standard a 5 campi.",
            "description": "Analizzatore di espressioni cron gratuito. Valida la sintassi crontab a 5 campi e mostra le prossime 10 esecuzioni nel tuo fuso orario.",
        },
    },
    "body": """
<div class="tool-card">
  <label>Cron expression (5 fields: minute hour day-of-month month day-of-week)</label>
  <input type="text" id="cron-in" oninput="cronRun()" placeholder="*/5 * * * *" value="0 9 * * 1-5" style="font-family:ui-monospace,monospace">
  <div class="button-row">
    <button class="secondary" onclick="cronSet('*/5 * * * *')">every 5 min</button>
    <button class="secondary" onclick="cronSet('0 * * * *')">hourly</button>
    <button class="secondary" onclick="cronSet('0 9 * * 1-5')">weekdays 9am</button>
    <button class="secondary" onclick="cronSet('0 0 1 * *')">1st of month</button>
    <button class="secondary" onclick="cronSet('0 2 * * 0')">Sunday 2am</button>
  </div>
  <div class="meta" id="cron-explain"></div>
</div>
<div class="tool-card">
  <label>Next 10 fire times (local timezone)</label>
  <pre class="output" id="cron-out">{LBL_NO_INPUT}</pre>
</div>
""",
    "script": """
<script>
const FIELD_RANGES = [[0,59],[0,23],[1,31],[1,12],[0,7]]; // last 0 and 7 = Sunday
const FIELD_NAMES = ['minute','hour','day-of-month','month','day-of-week'];

function cronExpand(field, idx){
  const [lo,hi] = FIELD_RANGES[idx];
  const out = new Set();
  field.split(',').forEach(part => {
    let step = 1;
    if (part.includes('/')){ const [a,b] = part.split('/'); step = parseInt(b,10); part = a; }
    let from = lo, to = hi;
    if (part === '*'){ /* keep range */ }
    else if (part.includes('-')){ const [a,b] = part.split('-'); from = parseInt(a,10); to = parseInt(b,10); }
    else { from = to = parseInt(part,10); }
    if (isNaN(from) || isNaN(to) || from < lo || to > hi || from > to) throw new Error('Invalid value: ' + part + ' (expected ' + lo + '-' + hi + ')');
    if (isNaN(step) || step < 1) throw new Error('Invalid step: ' + step);
    for (let v = from; v <= to; v += step) out.add(idx === 4 && v === 7 ? 0 : v);
  });
  return out;
}

function cronMatches(date, sets){
  return sets[0].has(date.getMinutes())
      && sets[1].has(date.getHours())
      && sets[2].has(date.getDate())
      && sets[3].has(date.getMonth() + 1)
      && sets[4].has(date.getDay());
}

function cronNext(expr, count){
  const fields = expr.trim().split(/\\s+/);
  if (fields.length !== 5) throw new Error('Expected 5 space-separated fields, got ' + fields.length);
  const sets = fields.map((f, i) => cronExpand(f, i));
  const now = new Date();
  const start = new Date(now.getFullYear(), now.getMonth(), now.getDate(), now.getHours(), now.getMinutes() + 1, 0, 0);
  const out = [];
  let d = new Date(start);
  let safety = 0;
  while (out.length < count && safety < 600000){
    if (cronMatches(d, sets)) out.push(new Date(d));
    d.setMinutes(d.getMinutes() + 1);
    safety++;
  }
  if (safety >= 600000) throw new Error('Search exhausted (no matches in next ~1 year)');
  return out;
}

function cronExplain(expr){
  // Very brief human-readable summary
  const parts = expr.trim().split(/\\s+/);
  if (parts.length !== 5) return '';
  const m = parts[0], h = parts[1], dom = parts[2], mon = parts[3], dow = parts[4];
  let s = 'At ';
  if (m === '*') s += 'every minute';
  else if (m.startsWith('*/')) s += 'every ' + m.slice(2) + ' minutes';
  else s += 'minute ' + m;
  s += ', ';
  if (h === '*') s += 'every hour';
  else if (h.startsWith('*/')) s += 'every ' + h.slice(2) + ' hours';
  else s += 'hour ' + h;
  if (dow !== '*'){
    const names = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'];
    if (dow.includes('-')){
      const [a,b] = dow.split('-').map(x => parseInt(x,10));
      s += ', on ' + names[a] + '-' + names[b];
    } else if (!isNaN(parseInt(dow,10))){
      s += ', on ' + names[parseInt(dow,10) % 7];
    }
  }
  if (dom !== '*'){
    s += ', on day ' + dom + ' of the month';
  }
  if (mon !== '*'){
    s += ', in month ' + mon;
  }
  return s + '.';
}

function cronRun(){
  const expr = document.getElementById('cron-in').value;
  const out = document.getElementById('cron-out');
  const exp = document.getElementById('cron-explain');
  out.classList.remove('error');
  if (!expr.trim()){ out.textContent = '{LBL_NO_INPUT}'; exp.textContent = ''; return; }
  try {
    const dates = cronNext(expr, 10);
    out.textContent = dates.map((d,i) => (i+1).toString().padStart(2,' ') + '.  ' + d.toLocaleString(undefined,{weekday:'short', year:'numeric', month:'short', day:'2-digit', hour:'2-digit', minute:'2-digit'})).join('\\n');
    exp.textContent = cronExplain(expr);
  } catch(e){
    out.classList.add('error');
    out.textContent = '✗ ' + e.message;
    exp.textContent = '';
  }
}
function cronSet(s){ document.getElementById('cron-in').value = s; cronRun(); }
document.addEventListener('DOMContentLoaded', cronRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Cron expressions are powerful and easy to mis-write. <code>0 0 * * 1-5</code> looks like a weekday-at-midnight schedule and is. <code>*/15 0-9 * * *</code> looks like every fifteen minutes during business hours and is. <code>0 0 1 */3 *</code> looks like quarterly... if you remembered <code>*/3</code> means "every third month". This tool lets you paste an expression, see what it actually means in plain English, and preview the next 10 fire times so you can confirm before deploying.</p>

<h3>When to use it</h3>
<ul>
  <li>Sanity-checking a cron line in <code>crontab -e</code> before saving.</li>
  <li>Translating a Kubernetes <code>CronJob</code> schedule string into "what time will this actually run?".</li>
  <li>Designing a new schedule — start with English ("every weekday morning") and iterate the expression until the preview matches.</li>
  <li>Debugging a job that "didn't run when I expected" — paste the schedule, look at the next 10 times, see whether reality is the surprise or the expression is.</li>
</ul>

<h3>Cron field reference</h3>
<table>
  <tr><th>Field</th><th>Range</th><th>Wildcards</th></tr>
  <tr><td>Minute</td><td>0-59</td><td><code>*</code> · <code>*/5</code> · <code>0,30</code> · <code>0-29</code></td></tr>
  <tr><td>Hour</td><td>0-23</td><td>same</td></tr>
  <tr><td>Day of month</td><td>1-31</td><td>same</td></tr>
  <tr><td>Month</td><td>1-12</td><td>same</td></tr>
  <tr><td>Day of week</td><td>0-6 (0 = Sunday, 7 also = Sunday)</td><td>same</td></tr>
</table>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Day-of-month + day-of-week interact.</strong> If both are restricted (e.g. <code>15 * * * 1</code> meaning "the 15th OR a Monday"), most cron implementations OR them. This tool follows that convention.</li>
  <li><strong><code>*/N</code> isn't quite "every N".</strong> It's "every N starting from the lower bound", so <code>*/15</code> in minute = 0,15,30,45 (not 12,27,42,57). To start later, use a list: <code>5,20,35,50</code>.</li>
  <li><strong>Step + range combos.</strong> <code>0-30/5</code> = 0,5,10,15,20,25,30. The step applies inside the range only.</li>
  <li><strong>Timezone is browser-local here.</strong> Real cron daemons run in server time (often UTC). A schedule that looks fine in your browser may fire at a different wall-clock time on the server. Confirm timezone before pasting.</li>
  <li><strong>Some cron flavours add fields.</strong> Quartz cron has 6 or 7 fields (with seconds and year). systemd timers use a different format entirely. This tool parses standard 5-field crontab.</li>
</ul>
""",
    },
    "related": ["timestamp-converter", "timezone-converter", "date-calculator"],
}
