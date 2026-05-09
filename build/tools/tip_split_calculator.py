TOOL = {
    "slug": "tip-split-calculator",
    "category": "math",
    "icon": "💵",
    "tags": ["tip", "split", "bill", "restaurant", "calculator", "people", "share"],
    "i18n": {
        "en": {
            "name": "Tip & Split Calculator",
            "tagline": "Bill total + tip % + people = per-person amount. Round-up option, tip and grand total shown.",
            "description": "Free tip and bill split calculator. Enter the bill, tip percentage, and number of people. See the tip amount, the grand total, and the per-person share. Optional round-up.",
        },
        "de": {"name": "Trinkgeld- & Aufteilen-Rechner", "tagline": "Rechnung + Trinkgeld-% + Personen = Betrag pro Person. Aufrunden möglich, Trinkgeld und Gesamtsumme angezeigt.", "description": "Kostenloser Trinkgeld- und Rechnungs-Splitter. Gib Rechnung, Trinkgeld-% und Personenzahl ein. Trinkgeld, Gesamtbetrag und pro-Person-Anteil werden berechnet. Aufrunden optional."},
        "es": {"name": "Calculadora de Propina y División", "tagline": "Cuenta + propina % + personas = importe por persona. Opción de redondeo. Propina y total mostrados.", "description": "Calculadora gratuita de propina y división de cuenta. Introduce el total, el % de propina y el número de personas. Verás propina, total y reparto por persona. Redondeo opcional."},
        "fr": {"name": "Calculateur de Pourboire et Partage", "tagline": "Addition + pourboire % + personnes = montant par personne. Arrondi en option. Pourboire et total affichés.", "description": "Calculateur gratuit de pourboire et partage. Entrez l'addition, le pourcentage et le nombre de personnes. Pourboire, total et part par personne calculés. Arrondi en option."},
        "it": {"name": "Calcolatore Mancia e Conto Diviso", "tagline": "Conto + mancia % + persone = importo per persona. Arrotondamento opzionale. Mancia e totale mostrati.", "description": "Calcolatore gratuito mancia e divisione conto. Inserisci conto, percentuale di mancia e numero di persone. Mancia, totale e quota per persona calcolati. Arrotondamento opzionale."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Bill total</label>
      <input type="number" id="ts-bill" step="0.01" min="0" value="100" oninput="tsRun()">
    </div>
    <div>
      <label>Tip percentage</label>
      <input type="number" id="ts-tip" step="0.5" min="0" value="15" oninput="tsRun()">
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Number of people</label>
      <input type="number" id="ts-people" step="1" min="1" value="4" oninput="tsRun()">
    </div>
    <div>
      <label>Currency symbol</label>
      <input type="text" id="ts-cur" maxlength="4" value="$" oninput="tsRun()">
    </div>
  </div>
  <div class="meta" style="margin-top:0.7rem">
    <label style="display:inline-flex;gap:0.4rem;align-items:center;color:var(--text-muted);font-size:0.85rem"><input type="checkbox" id="ts-round" onchange="tsRun()" style="width:auto"> Round per-person up to nearest whole unit (be generous)</label>
  </div>
  <div class="button-row" style="margin-top:0.7rem;flex-wrap:wrap">
    <button type="button" class="secondary" onclick="tsPreset(0)" style="padding:0.4rem 0.8rem;font-size:0.85rem">No tip</button>
    <button type="button" class="secondary" onclick="tsPreset(10)" style="padding:0.4rem 0.8rem;font-size:0.85rem">10%</button>
    <button type="button" class="secondary" onclick="tsPreset(15)" style="padding:0.4rem 0.8rem;font-size:0.85rem">15%</button>
    <button type="button" class="secondary" onclick="tsPreset(18)" style="padding:0.4rem 0.8rem;font-size:0.85rem">18%</button>
    <button type="button" class="secondary" onclick="tsPreset(20)" style="padding:0.4rem 0.8rem;font-size:0.85rem">20%</button>
    <button type="button" class="secondary" onclick="tsPreset(25)" style="padding:0.4rem 0.8rem;font-size:0.85rem">25%</button>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="ts-out" class="output"></div>
</div>
""",
    "script": """
<style>
.ts-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:0.6rem;margin-bottom:0.5rem}
.ts-stat{background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;padding:0.7rem 0.85rem}
.ts-stat .ts-num{font-family:ui-monospace,monospace;font-size:1.3rem;font-weight:600;color:var(--accent)}
.ts-stat .ts-lbl{font-size:0.78rem;color:var(--text-muted);margin-top:0.15rem}
.ts-pp{margin-top:0.5rem;background:var(--accent);color:#fff;padding:0.85rem 1rem;border-radius:8px;text-align:center;font-family:ui-monospace,monospace;font-size:1.2rem;font-weight:600}
.ts-rounding{color:var(--text-muted);font-size:0.78rem;margin-top:0.4rem;text-align:center}
</style>
<script>
function tsFmt(n, cur){
  return cur + n.toFixed(2);
}
function tsPreset(p){
  document.getElementById('ts-tip').value = p;
  tsRun();
}
function tsRun(){
  const bill = parseFloat(document.getElementById('ts-bill').value) || 0;
  const tipPct = parseFloat(document.getElementById('ts-tip').value);
  const people = Math.max(1, Math.floor(parseFloat(document.getElementById('ts-people').value) || 1));
  const cur = document.getElementById('ts-cur').value || '';
  const round = document.getElementById('ts-round').checked;
  const out = document.getElementById('ts-out');
  if(!isFinite(bill) || bill < 0 || !isFinite(tipPct) || tipPct < 0){ out.textContent = '{LBL_NO_INPUT}'; return; }
  const tip = bill * tipPct / 100;
  const total = bill + tip;
  let pp = total / people;
  let bumpedTotal = total;
  let rounded = false;
  if(round){
    const ppCeil = Math.ceil(pp);
    if(ppCeil > pp){
      pp = ppCeil;
      bumpedTotal = ppCeil * people;
      rounded = true;
    }
  }
  out.innerHTML = `
    <div class="ts-grid">
      <div class="ts-stat"><div class="ts-num">${tsFmt(bill, cur)}</div><div class="ts-lbl">Bill</div></div>
      <div class="ts-stat"><div class="ts-num">${tsFmt(tip, cur)}</div><div class="ts-lbl">Tip (${tipPct}%)</div></div>
      <div class="ts-stat"><div class="ts-num">${tsFmt(bumpedTotal, cur)}</div><div class="ts-lbl">Grand total</div></div>
      <div class="ts-stat"><div class="ts-num">${people}</div><div class="ts-lbl">People</div></div>
    </div>
    <div class="ts-pp">${tsFmt(pp, cur)} per person</div>
    ${rounded ? `<div class="ts-rounding">Rounded up — total paid is ${tsFmt(bumpedTotal-total, cur)} above the bill+tip.</div>` : ''}
  `;
}
document.addEventListener('DOMContentLoaded', tsRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Splitting a restaurant bill at the end of dinner is the classic case of "easy maths, but the wine has been flowing". Three numbers go in (bill, tip percentage, number of people) and three come out (tip amount, grand total, per-person share). This tool does that without sending anything to a server, plus an optional round-up so the per-person figure lands on a whole unit and you tip a little more rather than juggling small change.</p>

<h3>When to use it</h3>
<ul>
  <li>End of a group meal — even split.</li>
  <li>Adding a known tip percentage to a service bill.</li>
  <li>Quickly testing different tip levels (10/15/18/20/25) before deciding.</li>
  <li>Settling a coffee round, a taxi, or any per-head share.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Tipping convention varies wildly.</strong> United States: 18–22% is normal; under 15% is a complaint. Most of Europe: round up or 5–10%; service often included. Japan: don't tip — it can be considered rude. Always check local custom rather than blindly applying a percentage.</li>
  <li><strong>Tip on pre-tax or post-tax?</strong> In the US tipping on the pre-tax subtotal is common etiquette but most card terminals offer post-tax percentages. The tool computes the percentage of whatever bill total you enter — pick the base intentionally.</li>
  <li><strong>Service charge ≠ tip.</strong> If a "service charge" is already on the bill (common in UK groups of 6+ and most of continental Europe), additional tipping is optional. Some venues split service charges with the kitchen; tip cash directly if you want it to reach the server.</li>
  <li><strong>Per-person rounding can hide unequal eating.</strong> An even split is fastest but unfair if one person had wine and another had water — switch to itemised splitting in that case.</li>
  <li><strong>Cash vs card.</strong> Some staff prefer cash tips because card tips are pooled, taxed-immediately, or skimmed by the venue. If the per-person figure on this calculator includes the tip, decide whether you want to settle the tip in cash on top.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>Eine Restaurantrechnung am Ende des Abends aufteilen ist einfache Mathematik — aber der Wein ist geflossen. Rechnung, Trinkgeld-% und Personenanzahl rein, Trinkgeld, Gesamtbetrag und Anteil pro Person raus. Optional Aufrunden, damit der Pro-Person-Betrag glatt wird.</p>
<h3>Wann verwenden</h3>
<ul>
<li>Nach einem gemeinsamen Essen — gleich aufgeteilt.</li>
<li>Trinkgeld-Prozentsatz auf eine Rechnung anwenden.</li>
<li>Verschiedene Trinkgeld-Stufen schnell vergleichen.</li>
<li>Kaffeerunde, Taxi oder andere Pro-Kopf-Beträge.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>Trinkgeldgepflogenheiten variieren.</strong> USA: 18–22%. Europa: aufrunden oder 5–10%. Japan: kein Trinkgeld — kann unhöflich wirken.</li>
<li><strong>Vor- oder nach Steuer?</strong> In den USA üblicherweise auf den Nettobetrag, Kartenleser bieten oft den Bruttobetrag.</li>
<li><strong>Servicecharge ≠ Trinkgeld.</strong> Bei bereits aufgeführtem Service ist zusätzliches Trinkgeld optional. Bargeld erreicht das Personal eher direkt.</li>
<li><strong>Gleicher Anteil ist unfair</strong>, wenn einer Wein hatte und der andere Wasser — dann posten-genau aufteilen.</li>
<li><strong>Bar oder Karte.</strong> Bargeld-Trinkgeld umgeht oft Pool und sofortige Versteuerung.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>Repartir la cuenta al final de una cena es matemática fácil, pero el vino ha corrido. Importe, % de propina y número de personas entran; propina, total y parte por persona salen. Redondeo opcional para que el por persona quede entero.</p>
<h3>Cuándo usarlo</h3>
<ul>
<li>Al final de una comida en grupo — partes iguales.</li>
<li>Aplicar un porcentaje de propina conocido.</li>
<li>Comparar rápidamente distintos porcentajes (10/15/18/20).</li>
<li>Café, taxi u otros gastos compartidos.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>La costumbre varía.</strong> EE.UU.: 18–22%. Mayor parte de Europa: redondear o 5–10%. Japón: no se da propina.</li>
<li><strong>¿Antes o después de impuestos?</strong> En EE.UU. suele ser sobre el subtotal pre-tax; los TPV ofrecen post-tax.</li>
<li><strong>Servicio ≠ propina.</strong> Si ya hay un cargo de servicio, una propina extra es opcional.</li>
<li><strong>Repartir igual es injusto</strong> si uno tomó vino y otro agua — usa reparto por consumición.</li>
<li><strong>Efectivo vs tarjeta.</strong> En efectivo suele ir más directo al personal.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Partager l'addition à la fin du dîner relève d'un calcul simple, mais le vin a coulé. Addition, % de pourboire et nombre de convives → pourboire, total et part par personne. Arrondi en option pour tomber sur un nombre rond.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>Fin d'un repas en groupe — partage égal.</li>
<li>Appliquer un pourcentage connu de pourboire.</li>
<li>Comparer rapidement plusieurs taux (10/15/18/20).</li>
<li>Café, taxi ou autre dépense partagée.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>L'usage varie fortement.</strong> USA : 18–22 %. Europe : arrondir ou 5–10 %. Japon : pas de pourboire.</li>
<li><strong>Avant ou après taxes ?</strong> Aux USA souvent sur le HT ; les TPE proposent souvent le TTC.</li>
<li><strong>Service ≠ pourboire.</strong> Si le service est déjà compté, le pourboire est optionnel.</li>
<li><strong>Partage égal injuste</strong> si l'un a pris du vin et l'autre de l'eau — partage à l'item alors.</li>
<li><strong>Espèces vs carte.</strong> Le pourboire en liquide va plus directement au personnel.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>Dividere il conto a fine cena è matematica facile — ma il vino è andato giù. Conto, % di mancia e numero di persone → mancia, totale e quota per persona. Arrotondamento opzionale per ottenere una cifra tonda.</p>
<h3>Quando usarlo</h3>
<ul>
<li>Fine di un pasto in gruppo — divisione paritaria.</li>
<li>Applicare una percentuale di mancia.</li>
<li>Confrontare rapidamente diverse percentuali (10/15/18/20).</li>
<li>Caffè, taxi o altre spese condivise.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>La consuetudine varia.</strong> USA: 18–22%. Europa: arrotondare o 5–10%. Giappone: non si lascia mancia.</li>
<li><strong>Prima o dopo le tasse?</strong> Negli USA in genere sul subtotale; i POS offrono il post-IVA.</li>
<li><strong>Coperto/servizio ≠ mancia.</strong> Se è già in conto, la mancia è opzionale.</li>
<li><strong>Divisione paritaria iniqua</strong> se uno ha preso vino e l'altro acqua — meglio dividere per voce.</li>
<li><strong>Contanti vs carta.</strong> La mancia in contanti spesso arriva più direttamente al personale.</li>
</ul>
""",
    },
    "related": ["percentage-calculator", "bmi-calculator", "unit-converter"],
}
