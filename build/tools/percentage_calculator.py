TOOL = {
    "slug": "percentage-calculator",
    "category": "math",
    "icon": "%",
    "tags": ["percentage", "percent", "calculate", "discount", "increase", "decrease", "tip", "tax"],
    "i18n": {
        "en": {
            "name": "Percentage Calculator",
            "tagline": "Five percentage calculators in one: of, what %, increase/decrease, change, and tip/tax.",
            "description": "Free online percentage calculator. Compute X% of Y, what % is X of Y, percentage change, percentage increase/decrease, and tip or tax amounts.",
        },
        "de": {"name": "Prozentrechner", "tagline": "Fünf Prozent-Rechner in einem: von, wie viel %, Zunahme/Abnahme, Änderung und Trinkgeld/Steuer.", "description": "Kostenloser Prozentrechner. X % von Y, wie viel % ist X von Y, Prozentänderung, Zunahme/Abnahme sowie Trinkgeld- oder Steuerberechnung."},
        "es": {"name": "Calculadora de Porcentajes", "tagline": "Cinco calculadoras de porcentaje en una: de, qué %, aumento/descuento, variación y propina/impuesto.", "description": "Calculadora de porcentajes gratuita en línea. X% de Y, qué % es X de Y, variación porcentual, aumento/descuento y propina o impuesto."},
        "fr": {"name": "Calculateur de Pourcentage", "tagline": "Cinq calculateurs de pourcentage en un : de, quel %, hausse/baisse, variation et pourboire/taxe.", "description": "Calculateur de pourcentage gratuit en ligne. X% de Y, quel % est X de Y, variation, hausse/baisse et pourboire ou taxe."},
        "it": {"name": "Calcolatore di Percentuale", "tagline": "Cinque calcolatori di percentuale in uno: di, quale %, aumento/sconto, variazione e mancia/IVA.", "description": "Calcolatore di percentuale gratuito online. X% di Y, quale % è X di Y, variazione, aumento/sconto e mancia o IVA."},
    },
    "body": """
<div class="tool-card">
  <label>Calculation</label>
  <select id="pc-mode" onchange="pcSwitch()">
    <option value="of">What is X% of Y</option>
    <option value="is">X is what % of Y</option>
    <option value="change">% change from X to Y</option>
    <option value="inc">Increase X by Y%</option>
    <option value="dec">Decrease X by Y%</option>
    <option value="tip">Tip / Tax: X plus Y%</option>
  </select>
</div>
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label id="pc-l1">X</label>
      <input type="number" id="pc-a" step="any" oninput="pcRun()" value="20">
    </div>
    <div>
      <label id="pc-l2">Y</label>
      <input type="number" id="pc-b" step="any" oninput="pcRun()" value="150">
    </div>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="pc-out" class="output" style="font-size:1.1rem">{LBL_NO_INPUT}</div>
  <div id="pc-formula" class="meta" style="margin-top:0.6rem;font-family:ui-monospace,monospace"></div>
</div>
""",
    "script": """
<script>
function pcFmt(n){if(!isFinite(n))return '∞';const r=Math.round(n*1e6)/1e6;return Number.isInteger(r)?r.toString():r.toString().replace(/(\\.\\d*?)0+$/,'$1').replace(/\\.$/,'')}
function pcSwitch(){
  const m = document.getElementById('pc-mode').value;
  const l1 = document.getElementById('pc-l1'), l2 = document.getElementById('pc-l2');
  const labels = {
    of:    ['Percentage (X%)', 'Of (Y)'],
    is:    ['Part (X)',         'Of total (Y)'],
    change:['From (X)',         'To (Y)'],
    inc:   ['Starting value (X)', 'Increase by (Y%)'],
    dec:   ['Starting value (X)', 'Decrease by (Y%)'],
    tip:   ['Bill amount (X)',    'Tip / tax (Y%)'],
  }[m];
  l1.textContent = labels[0];
  l2.textContent = labels[1];
  pcRun();
}
function pcRun(){
  const m = document.getElementById('pc-mode').value;
  const a = parseFloat(document.getElementById('pc-a').value);
  const b = parseFloat(document.getElementById('pc-b').value);
  const out = document.getElementById('pc-out');
  const fml = document.getElementById('pc-formula');
  if(isNaN(a) || isNaN(b)){ out.textContent = '{LBL_NO_INPUT}'; fml.textContent = ''; return; }
  let res = '', formula = '';
  switch(m){
    case 'of':     { const v = (a/100)*b; res = `${pcFmt(a)}% of ${pcFmt(b)} = ${pcFmt(v)}`; formula = `(${pcFmt(a)} ÷ 100) × ${pcFmt(b)} = ${pcFmt(v)}`; break; }
    case 'is':     { const v = b===0 ? Infinity : (a/b)*100; res = `${pcFmt(a)} is ${pcFmt(v)}% of ${pcFmt(b)}`; formula = `(${pcFmt(a)} ÷ ${pcFmt(b)}) × 100 = ${pcFmt(v)}%`; break; }
    case 'change': { const v = a===0 ? Infinity : ((b-a)/Math.abs(a))*100; res = `Change: ${pcFmt(v)}% (${v>=0?'increase':'decrease'})`; formula = `((${pcFmt(b)} − ${pcFmt(a)}) ÷ |${pcFmt(a)}|) × 100 = ${pcFmt(v)}%`; break; }
    case 'inc':    { const v = a + (a*b/100); res = `${pcFmt(a)} increased by ${pcFmt(b)}% = ${pcFmt(v)}`; formula = `${pcFmt(a)} × (1 + ${pcFmt(b)}/100) = ${pcFmt(v)}`; break; }
    case 'dec':    { const v = a - (a*b/100); res = `${pcFmt(a)} decreased by ${pcFmt(b)}% = ${pcFmt(v)}`; formula = `${pcFmt(a)} × (1 − ${pcFmt(b)}/100) = ${pcFmt(v)}`; break; }
    case 'tip':    { const tip = a*b/100; const total = a+tip; res = `Tip/Tax: ${pcFmt(tip)} · Total: ${pcFmt(total)}`; formula = `${pcFmt(a)} × ${pcFmt(b)}/100 = ${pcFmt(tip)} · ${pcFmt(a)} + ${pcFmt(tip)} = ${pcFmt(total)}`; break; }
  }
  out.textContent = res;
  fml.textContent = formula;
}
document.addEventListener('DOMContentLoaded', pcSwitch);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Six different "percentage" calculations come up daily and are easy to mix up: how much is X% of Y? What percent is X out of Y? What's the change between two values? Apply a markup or discount? Tip or tax? Each is a slightly different formula, and getting them confused leads to wrong invoices, wrong discounts, and embarrassing reviews. This tool runs all six side by side with the formula spelled out, so you can pick the right one and double-check the maths.</p>

<h3>What each mode does</h3>
<ul>
  <li><strong>What is X% of Y</strong> — for discounts, commissions, percentage of a total. <em>20% of 150 → 30</em>.</li>
  <li><strong>X is what % of Y</strong> — for "score / max" style ratios. <em>30 of 150 → 20%</em>.</li>
  <li><strong>% change</strong> — signed: positive is an increase, negative is a decrease. <em>100 → 125 = +25%</em>.</li>
  <li><strong>Increase / Decrease</strong> — applies a percentage adjustment to a starting value.</li>
  <li><strong>Tip / Tax</strong> — convenience for adding a percentage on top of a bill.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Percentage change isn't symmetric.</strong> Going 100 → 125 is +25%; going 125 → 100 is −20%, not −25%. The denominator is the starting value, which differs in each direction.</li>
  <li><strong>Stacking percentages compounds.</strong> A 20% increase followed by a 20% decrease doesn't return you to the start (1.20 × 0.80 = 0.96, a net 4% loss). For sequential markups/discounts, calculate each step.</li>
  <li><strong>Tip on pre-tax vs post-tax.</strong> Convention varies by country and venue. The tool computes the percentage of the value you enter — pick which value you actually want as the base.</li>
  <li><strong>Rounding.</strong> Output is rounded to 6 decimals then trimmed; if you need legal/accounting precision (banker's rounding, currency-specific rules), do that step in your domain layer, not here.</li>
</ul>
""",
    },
    "related": ["number-base-converter", "timestamp-converter", "json-formatter"],
}
