TOOL = {
    "slug": "dice-roller",
    "category": "utility",
    "icon": "🎲",
    "tags": ["dice", "roll", "d20", "rpg", "dnd", "random", "tabletop", "notation"],
    "i18n": {
        "en": {
            "name": "Dice Roller",
            "tagline": "Roll dice with standard D&D notation — 2d6+3, 1d20, 4d6 keep highest 3. Crypto-secure RNG.",
            "description": "Free online dice roller using standard tabletop notation: 1d20, 2d6+3, 4d6kh3, 3d8-1. See every individual roll plus the total. Uses crypto.getRandomValues for fair, unpredictable rolls.",
        },
        "de": {"name": "Würfelroller", "tagline": "Würfle mit Standard-D&D-Notation — 2d6+3, 1d20, 4d6 keep highest 3. Krypto-sicherer RNG.", "description": "Kostenloser Online-Würfler mit Standard-Tabletop-Notation: 1d20, 2d6+3, 4d6kh3, 3d8-1. Zeigt jeden Wurf einzeln plus Summe. Verwendet crypto.getRandomValues für faire Würfe."},
        "es": {"name": "Lanzador de Dados", "tagline": "Lanza dados con notación D&D estándar — 2d6+3, 1d20, 4d6 quedarse 3 más altos. RNG criptográfico.", "description": "Lanzador de dados gratuito con notación estándar de mesa: 1d20, 2d6+3, 4d6kh3, 3d8-1. Cada tirada y el total. Usa crypto.getRandomValues para tiradas justas."},
        "fr": {"name": "Lanceur de Dés", "tagline": "Lancez les dés avec la notation D&D standard — 2d6+3, 1d20, 4d6 garder les 3 plus hauts. RNG crypto-sûr.", "description": "Lanceur de dés gratuit avec notation standard de jeu de rôle : 1d20, 2d6+3, 4d6kh3, 3d8-1. Chaque dé et le total. Utilise crypto.getRandomValues pour des lancers équitables."},
        "it": {"name": "Lanciatore di Dadi", "tagline": "Lancia dadi con notazione D&D standard — 2d6+3, 1d20, 4d6 tieni i 3 più alti. RNG crittograficamente sicuro.", "description": "Lanciatore di dadi gratuito con notazione standard da tavolo: 1d20, 2d6+3, 4d6kh3, 3d8-1. Ogni dado e il totale. Usa crypto.getRandomValues per lanci equi."},
        "pt": {"name": "Rolador de Dados", "tagline": "Role dados com notação padrão de D&D — 2d6+3, 1d20, 4d6 mantendo os 3 maiores. RNG criptograficamente seguro.", "description": "Rolador de dados online gratuito com notação padrão de RPG de mesa: 1d20, 2d6+3, 4d6kh3, 3d8-1. Veja cada dado individualmente e o total. Usa crypto.getRandomValues para rolagens justas e imprevisíveis."},
        "pl": {"name": "Rzucacz Kości", "tagline": "Rzucaj kostkami w standardowej notacji D&D — 2d6+3, 1d20, 4d6 keep highest 3. Kryptograficznie bezpieczny RNG.", "description": "Darmowy online rzucacz kości w standardowej notacji RPG: 1d20, 2d6+3, 4d6kh3, 3d8-1. Zobacz każdy rzut z osobna plus sumę. Używa crypto.getRandomValues dla uczciwych, nieprzewidywalnych rzutów."},
    },
    "body": """
<div class="tool-card">
  <label>Dice notation</label>
  <input type="text" id="dr-notation" value="2d6+3" oninput="drValidate()" placeholder="e.g. 1d20, 2d6+3, 4d6kh3, 3d8-1" autocomplete="off" spellcheck="false" style="font-family:ui-monospace,monospace">
  <div class="meta" style="margin-top:0.4rem">Examples: <code>1d20</code> · <code>2d6+3</code> · <code>4d6kh3</code> (drop lowest) · <code>3d8-1</code> · <code>d100</code> · <code>2d20kl1</code> (disadvantage)</div>
  <div class="button-row" style="margin-top:0.7rem;flex-wrap:wrap">
    <button type="button" onclick="drRoll()">🎲 Roll</button>
    <button type="button" class="secondary" onclick="drPreset('1d20')" style="padding:0.4rem 0.8rem;font-size:0.85rem">1d20</button>
    <button type="button" class="secondary" onclick="drPreset('2d6')" style="padding:0.4rem 0.8rem;font-size:0.85rem">2d6</button>
    <button type="button" class="secondary" onclick="drPreset('4d6kh3')" style="padding:0.4rem 0.8rem;font-size:0.85rem">4d6kh3</button>
    <button type="button" class="secondary" onclick="drPreset('1d100')" style="padding:0.4rem 0.8rem;font-size:0.85rem">d100</button>
    <button type="button" class="secondary" onclick="drPreset('2d20kh1')" style="padding:0.4rem 0.8rem;font-size:0.85rem">Adv (2d20kh1)</button>
    <button type="button" class="secondary" onclick="drPreset('2d20kl1')" style="padding:0.4rem 0.8rem;font-size:0.85rem">Dis (2d20kl1)</button>
    <button type="button" class="secondary" onclick="drClear()" style="padding:0.4rem 0.8rem;font-size:0.85rem">Clear log</button>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="dr-out" class="output">Press Roll.</div>
</div>
<div class="tool-card">
  <label>Roll history</label>
  <div id="dr-log" class="output" style="font-family:ui-monospace,monospace;font-size:0.85rem;min-height:3rem">(empty)</div>
</div>
""",
    "script": """
<style>
.dr-total{font-family:ui-monospace,monospace;font-size:2rem;font-weight:700;color:var(--accent);text-align:center;margin:0.3rem 0}
.dr-rolls{display:flex;gap:0.4rem;flex-wrap:wrap;justify-content:center;margin:0.5rem 0}
.dr-die{display:inline-flex;align-items:center;justify-content:center;min-width:2.4rem;height:2.4rem;padding:0 0.5rem;background:var(--bg-elev);border:1px solid var(--border);border-radius:6px;font-family:ui-monospace,monospace;font-weight:600;color:var(--text)}
.dr-die.dropped{opacity:0.4;text-decoration:line-through;color:var(--text-muted)}
.dr-die.crit-h{background:rgba(63,185,80,0.15);color:#3fb950;border-color:#3fb950}
.dr-die.crit-l{background:rgba(248,81,73,0.15);color:#f85149;border-color:#f85149}
.dr-detail{text-align:center;color:var(--text-muted);font-family:ui-monospace,monospace;font-size:0.85rem;margin-top:0.4rem}
.dr-log-row{padding:0.25rem 0;border-bottom:1px dashed var(--border);display:grid;grid-template-columns:auto 1fr auto;gap:0.7rem}
.dr-log-row:last-child{border:none}
.dr-log-time{color:var(--text-muted);font-size:0.78rem}
.dr-log-not{color:var(--accent)}
.dr-log-tot{color:var(--text);font-weight:600;text-align:right}
</style>
<script>
function drRandInt(maxExclusive){
  const arr = new Uint32Array(1);
  // Rejection sampling for unbiased range
  const range = maxExclusive;
  const limit = Math.floor(0xFFFFFFFF / range) * range;
  let v;
  do { crypto.getRandomValues(arr); v = arr[0]; } while (v >= limit);
  return v % range;
}
function drParse(s){
  // Format: [N]d<sides>[kh<K>|kl<K>][+/-<mod>]
  // Split on +/- for mod, but only after the dice spec
  s = (s||'').trim().toLowerCase().replace(/\\s+/g,'');
  if(!s) return {ok:false, err:'Empty input'};
  const m = s.match(/^(\\d*)d(\\d+|%)(?:(kh|kl)(\\d+))?([+-]\\d+)?$/);
  if(!m) return {ok:false, err:'Expected something like 2d6, 1d20+3, 4d6kh3'};
  const n = m[1] === '' ? 1 : parseInt(m[1], 10);
  const sides = m[2] === '%' ? 100 : parseInt(m[2], 10);
  const keepKind = m[3] || null;
  const keepN = m[4] ? parseInt(m[4], 10) : null;
  const mod = m[5] ? parseInt(m[5], 10) : 0;
  if(n < 1 || n > 1000) return {ok:false, err:'Number of dice must be 1–1000'};
  if(sides < 2 || sides > 1000000) return {ok:false, err:'Sides must be 2–1,000,000'};
  if(keepN !== null && (keepN < 1 || keepN > n)) return {ok:false, err:`Keep count must be between 1 and ${n}`};
  return {ok:true, n, sides, keepKind, keepN, mod};
}
function drValidate(){
  const p = drParse(document.getElementById('dr-notation').value);
  const out = document.getElementById('dr-out');
  if(!p.ok && document.getElementById('dr-notation').value){
    out.classList.add('error');
    out.textContent = '✗ ' + p.err;
  } else {
    out.classList.remove('error');
    if(out.textContent.startsWith('✗')) out.textContent = 'Press Roll.';
  }
}
function drPreset(s){
  document.getElementById('dr-notation').value = s;
  drValidate();
}
function drRoll(){
  const out = document.getElementById('dr-out');
  const log = document.getElementById('dr-log');
  const notation = document.getElementById('dr-notation').value;
  const p = drParse(notation);
  if(!p.ok){ out.classList.add('error'); out.textContent = '✗ ' + p.err; return; }
  out.classList.remove('error');
  const rolls = [];
  for(let i=0;i<p.n;i++) rolls.push(drRandInt(p.sides) + 1);
  // Decide which rolls are kept
  let keptIdx;
  if(p.keepKind === 'kh' && p.keepN !== null){
    const sorted = rolls.map((v,i)=>[v,i]).sort((a,b)=>b[0]-a[0]);
    keptIdx = new Set(sorted.slice(0, p.keepN).map(x=>x[1]));
  } else if(p.keepKind === 'kl' && p.keepN !== null){
    const sorted = rolls.map((v,i)=>[v,i]).sort((a,b)=>a[0]-b[0]);
    keptIdx = new Set(sorted.slice(0, p.keepN).map(x=>x[1]));
  } else {
    keptIdx = new Set(rolls.map((_,i)=>i));
  }
  let sumKept = 0;
  for(const i of keptIdx) sumKept += rolls[i];
  const total = sumKept + p.mod;
  const dieHtml = rolls.map((r,i) => {
    let cls = 'dr-die';
    if(!keptIdx.has(i)) cls += ' dropped';
    if(p.sides === 20 && r === 20) cls += ' crit-h';
    if(p.sides === 20 && r === 1)  cls += ' crit-l';
    return `<div class="${cls}">${r}</div>`;
  }).join('');
  const detail = `${p.n}d${p.sides}${p.keepKind ? p.keepKind + p.keepN : ''}${p.mod ? (p.mod >= 0 ? '+' + p.mod : p.mod) : ''}`;
  out.innerHTML = `
    <div class="dr-detail">${detail}</div>
    <div class="dr-rolls">${dieHtml}</div>
    <div class="dr-total">${total}</div>
    <div class="dr-detail">kept ${sumKept}${p.mod ? (p.mod>=0?' + '+p.mod:' − '+Math.abs(p.mod)) : ''} = ${total}</div>
  `;
  // Log
  const t = new Date();
  const ts = String(t.getHours()).padStart(2,'0') + ':' + String(t.getMinutes()).padStart(2,'0') + ':' + String(t.getSeconds()).padStart(2,'0');
  const row = `<div class="dr-log-row"><span class="dr-log-time">${ts}</span><span class="dr-log-not">${detail}</span><span class="dr-log-tot">${total}</span></div>`;
  if(log.textContent === '(empty)') log.innerHTML = row;
  else log.innerHTML = row + log.innerHTML;
}
function drClear(){ document.getElementById('dr-log').textContent = '(empty)'; }
document.addEventListener('DOMContentLoaded', drValidate);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Tabletop role-playing games (Dungeons & Dragons, Pathfinder, the OSR, countless others) use a compact notation for dice rolls: <code>NdS</code> means "roll N dice with S sides each". <code>2d6+3</code> means "roll two six-sided dice and add 3". This tool parses that notation and rolls the dice using the browser's cryptographic RNG, which is unpredictable and unbiased — much better than <code>Math.random()</code> for high-stakes rolls.</p>

<h3>Notation supported</h3>
<ul>
  <li><code>1d20</code> — one twenty-sided die.</li>
  <li><code>2d6+3</code> — two d6, sum, plus 3 modifier.</li>
  <li><code>3d8-1</code> — three d8, sum, minus 1.</li>
  <li><code>4d6kh3</code> — four d6, <strong>k</strong>eep <strong>h</strong>ighest 3 (classic D&D 5e ability score).</li>
  <li><code>2d20kl1</code> — two d20, keep lowest 1 (disadvantage).</li>
  <li><code>2d20kh1</code> — advantage.</li>
  <li><code>1d100</code> or <code>1d%</code> — percentile die.</li>
  <li><code>d20</code> — N defaults to 1.</li>
</ul>

<h3>When to use it</h3>
<ul>
  <li>You're playing online, your physical dice are out of reach, or you're DMing remotely.</li>
  <li>You need a reproducible-feel roll without the dice-app subscription.</li>
  <li>You want to settle a "let's flip for it" without finding a coin (1d2).</li>
  <li>You're prototyping a probability for a game design (try a million rolls — change the formula in code if you want stats).</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Browser tab is the trust boundary.</strong> The roll happens in your tab, in JavaScript — anyone with devtools open could fudge it. For competitive play with strangers, use a server-arbitrated roller.</li>
  <li><strong>Crypto RNG is unpredictable, not "more random".</strong> A good PRNG and crypto RNG produce indistinguishable distributions for dice. The advantage of crypto is that no one can predict the next number from past ones.</li>
  <li><strong>Modifiers apply once, after keeping.</strong> <code>4d6kh3+2</code> rolls 4d6, keeps the top 3, then adds 2 — not "adds 2 to each die".</li>
  <li><strong>This is not exploding dice.</strong> No <code>!</code>-style explosions, no rerolls (<code>r1</code>), no successes-counting (<code>3d10>=7</code>). The notation here is the simple "sum and modify" subset that covers ~95% of common rolls.</li>
  <li><strong>Crits are flagged for d20 only.</strong> A 20 highlights green, a 1 highlights red. Other dice sizes don't get the colouring.</li>
  <li><strong>Cap of 1000 dice per roll.</strong> Sane upper bound to keep the page responsive.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>RPGs de mesa (Dungeons & Dragons, Pathfinder, OSR e incontáveis outros) usam uma notação compacta para rolagens de dados: <code>NdL</code> significa "role N dados de L lados cada". <code>2d6+3</code> significa "role dois dados de seis lados e some 3". Esta ferramenta interpreta essa notação e rola os dados usando o RNG criptográfico do browser, que é imprevisível e imparcial — muito melhor que <code>Math.random()</code> para rolagens importantes.</p>

<h3>Notação suportada</h3>
<ul>
  <li><code>1d20</code> — um dado de vinte lados.</li>
  <li><code>2d6+3</code> — dois d6, somados, mais modificador 3.</li>
  <li><code>3d8-1</code> — três d8, somados, menos 1.</li>
  <li><code>4d6kh3</code> — quatro d6, <strong>k</strong>eep <strong>h</strong>ighest 3 (mantenha os 3 maiores — clássico para atributos em D&D 5e).</li>
  <li><code>2d20kl1</code> — dois d20, mantenha o menor (desvantagem).</li>
  <li><code>2d20kh1</code> — vantagem.</li>
  <li><code>1d100</code> ou <code>1d%</code> — dado percentual.</li>
  <li><code>d20</code> — N assume valor 1 por padrão.</li>
</ul>

<h3>Quando usar</h3>
<ul>
  <li>Você está jogando online, seus dados físicos estão fora de alcance ou está mestrando remotamente.</li>
  <li>Precisa de uma rolagem com sensação reproduzível sem assinar app de dados.</li>
  <li>Quer resolver um "vamos tirar na sorte" sem achar uma moeda (1d2).</li>
  <li>Está prototipando uma probabilidade para design de jogo (tente um milhão de rolagens — mude a fórmula no código se quiser stats).</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>A aba do browser é o limite de confiança.</strong> A rolagem acontece na sua aba, em JavaScript — qualquer um com devtools aberto pode burlar. Para jogo competitivo com estranhos, use um rolador arbitrado pelo servidor.</li>
  <li><strong>RNG cripto é imprevisível, não "mais aleatório".</strong> Um bom PRNG e um RNG cripto produzem distribuições indistinguíveis para dados. A vantagem do cripto é que ninguém pode prever o próximo número a partir dos anteriores.</li>
  <li><strong>Modificadores se aplicam uma vez, depois do keep.</strong> <code>4d6kh3+2</code> rola 4d6, mantém os 3 maiores e então soma 2 — não "soma 2 a cada dado".</li>
  <li><strong>Não há exploding dice.</strong> Sem explosões estilo <code>!</code>, sem rerolls (<code>r1</code>), sem contagem de sucessos (<code>3d10>=7</code>). A notação aqui é o subset simples de "soma e modifica" que cobre ~95% das rolagens comuns.</li>
  <li><strong>Críticos são sinalizados só para d20.</strong> Um 20 destaca em verde, um 1 destaca em vermelho. Outros tamanhos de dado não recebem essa cor.</li>
  <li><strong>Limite de 1000 dados por rolagem.</strong> Limite razoável para manter a página responsiva.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>Pen-&-Paper-Rollenspiele (D&D, Pathfinder u.v.m.) nutzen eine kompakte Notation für Würfel: <code>NdS</code> = "rolle N Würfel mit S Seiten". <code>2d6+3</code> = "zwei W6 und +3". Dieses Tool parst die Notation und würfelt mit dem kryptographischen RNG des Browsers — unvoreingenommen und unvorhersehbar.</p>
<h3>Unterstützte Notation</h3>
<ul>
<li><code>1d20</code> — ein W20.</li>
<li><code>2d6+3</code> — zwei W6, Summe +3.</li>
<li><code>4d6kh3</code> — vier W6, <strong>k</strong>eep <strong>h</strong>öchste 3.</li>
<li><code>2d20kl1</code> — Nachteil; <code>2d20kh1</code> — Vorteil.</li>
<li><code>1d100</code> oder <code>1d%</code> — Prozentwürfel.</li>
</ul>
<h3>Wann verwenden</h3>
<ul>
<li>Online-Runde, Würfel weg, Remote-DM.</li>
<li>Schnell-Wurf ohne Abo-App.</li>
<li>Wahrscheinlichkeit prototypen.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>Vertrauensgrenze ist der Browser-Tab.</strong> Wer DevTools öffnet, kann manipulieren — für Wettbewerb Server-Roller nehmen.</li>
<li><strong>Krypto-RNG ist unvorhersehbar, nicht "zufälliger".</strong> Verteilung wie ein guter PRNG.</li>
<li><strong>Modifikator wirkt einmal, nach Keep.</strong> <code>4d6kh3+2</code> = top 3 + 2.</li>
<li><strong>Keine "exploding dice"</strong>, keine Erfolgs-Zählung — nur Summen-Subset.</li>
<li><strong>Krits nur für d20.</strong> 20 grün, 1 rot.</li>
<li><strong>Max 1000 Würfel.</strong> Performance-Limit.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>Los juegos de rol de mesa (D&D, Pathfinder y muchos más) usan una notación compacta para los dados: <code>NdC</code> = "tira N dados de C caras". <code>2d6+3</code> = "dos d6 y +3". Esta herramienta interpreta la notación y tira con el RNG criptográfico del navegador — imparcial e impredecible.</p>
<h3>Notación soportada</h3>
<ul>
<li><code>1d20</code>, <code>2d6+3</code>, <code>3d8-1</code></li>
<li><code>4d6kh3</code> — guardar los 3 mejores.</li>
<li><code>2d20kl1</code> desventaja, <code>2d20kh1</code> ventaja.</li>
<li><code>1d100</code> o <code>1d%</code> — dado porcentual.</li>
</ul>
<h3>Cuándo usarlo</h3>
<ul>
<li>Partida online, sin dados físicos, DM remoto.</li>
<li>Tirada rápida sin app de suscripción.</li>
<li>Prototipar probabilidad de un diseño.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>El navegador es el límite de confianza.</strong> Con devtools se puede manipular — para competición usa un servidor.</li>
<li><strong>Crypto RNG es impredecible, no "más aleatorio".</strong> Distribución equivalente a un buen PRNG.</li>
<li><strong>El modificador se aplica una sola vez, tras filtrar.</strong></li>
<li><strong>Sin explosiones ni conteo de éxitos.</strong> Solo suma + modificador.</li>
<li><strong>Críticos solo en d20.</strong> 20 verde, 1 rojo.</li>
<li><strong>Máximo 1000 dados.</strong> Límite de rendimiento.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Les jeux de rôle papier (D&D, Pathfinder, etc.) utilisent une notation compacte : <code>NdF</code> = "lancer N dés à F faces". <code>2d6+3</code> = "deux d6 et +3". Cet outil interprète la notation et lance avec le RNG cryptographique du navigateur — non biaisé et imprévisible.</p>
<h3>Notation prise en charge</h3>
<ul>
<li><code>1d20</code>, <code>2d6+3</code>, <code>3d8-1</code>.</li>
<li><code>4d6kh3</code> — garder les 3 plus hauts.</li>
<li><code>2d20kl1</code> désavantage, <code>2d20kh1</code> avantage.</li>
<li><code>1d100</code> ou <code>1d%</code> — dé centésimal.</li>
</ul>
<h3>Quand l'utiliser</h3>
<ul>
<li>Partie en ligne, dés physiques absents, MJ à distance.</li>
<li>Lancer rapide sans appli payante.</li>
<li>Prototyper une probabilité.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>L'onglet du navigateur est la frontière de confiance.</strong> Avec devtools on peut tricher — pour du compétitif, lanceur côté serveur.</li>
<li><strong>RNG crypto = imprévisible, pas "plus aléatoire".</strong></li>
<li><strong>Modificateur appliqué une fois, après le keep.</strong></li>
<li><strong>Pas d'explosions ni de comptage de succès.</strong></li>
<li><strong>Critiques uniquement sur d20.</strong> 20 vert, 1 rouge.</li>
<li><strong>Max 1000 dés.</strong> Limite de performance.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>I giochi di ruolo da tavolo (D&D, Pathfinder, e molti altri) usano una notazione compatta: <code>NdF</code> = "tira N dadi a F facce". <code>2d6+3</code> = "due d6 e +3". Questo strumento interpreta la notazione e tira con il RNG crittografico del browser — imparziale e imprevedibile.</p>
<h3>Notazione supportata</h3>
<ul>
<li><code>1d20</code>, <code>2d6+3</code>, <code>3d8-1</code>.</li>
<li><code>4d6kh3</code> — tieni i 3 più alti.</li>
<li><code>2d20kl1</code> svantaggio, <code>2d20kh1</code> vantaggio.</li>
<li><code>1d100</code> o <code>1d%</code> — dado percentuale.</li>
</ul>
<h3>Quando usarlo</h3>
<ul>
<li>Sessione online, dadi fisici fuori portata, DM remoto.</li>
<li>Tiro rapido senza app a abbonamento.</li>
<li>Prototipare una probabilità di design.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>Il tab del browser è il confine di fiducia.</strong> Chi ha devtools può barare — per il competitivo usa un roller server-side.</li>
<li><strong>RNG crittografico = imprevedibile, non "più casuale".</strong></li>
<li><strong>Modificatore applicato una volta, dopo il keep.</strong></li>
<li><strong>Niente esplosioni o conteggio successi.</strong></li>
<li><strong>Critici solo per d20.</strong> 20 verde, 1 rosso.</li>
<li><strong>Massimo 1000 dadi.</strong> Limite di performance.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>RPG-i papierowe (Dungeons & Dragons, Pathfinder, OSR i niezliczone inne) używają zwartej notacji rzutów: <code>NdS</code> znaczy "rzuć N kośćmi o S ścianach każda". <code>2d6+3</code> znaczy "rzuć dwiema sześciościennymi i dodaj 3". To narzędzie parsuje tę notację i rzuca kośćmi używając kryptograficznego RNG przeglądarki, który jest nieprzewidywalny i nieobciążony — znacznie lepszy niż <code>Math.random()</code> do ważnych rzutów.</p>

<h3>Obsługiwana notacja</h3>
<ul>
  <li><code>1d20</code> — jedna kostka dwudziestościenna.</li>
  <li><code>2d6+3</code> — dwie d6, suma, plus modyfikator 3.</li>
  <li><code>3d8-1</code> — trzy d8, suma, minus 1.</li>
  <li><code>4d6kh3</code> — cztery d6, <strong>k</strong>eep <strong>h</strong>ighest 3 (klasyk D&D 5e do statystyk postaci).</li>
  <li><code>2d20kl1</code> — dwie d20, zachowaj najniższą (disadvantage).</li>
  <li><code>2d20kh1</code> — advantage.</li>
  <li><code>1d100</code> albo <code>1d%</code> — kostka procentowa.</li>
  <li><code>d20</code> — N domyślnie 1.</li>
</ul>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Grasz online, fizyczne kostki są poza zasięgiem albo prowadzisz sesję zdalnie.</li>
  <li>Potrzebujesz rzutu bez subskrypcji apki do kości.</li>
  <li>Chcesz rozstrzygnąć "rzućmy o to" bez szukania monety (1d2).</li>
  <li>Prototypujesz prawdopodobieństwo do projektu gry (puść milion rzutów — zmień formułę w kodzie, jeśli chcesz statystyk).</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Tab przeglądarki to granica zaufania.</strong> Rzut dzieje się w twoim tabie, w JavaScripcie — każdy z otwartymi devtoolsami może to podkręcić. Do rozgrywki kompetytywnej z obcymi używaj rzucacza arbitrowanego po stronie serwera.</li>
  <li><strong>Crypto RNG jest nieprzewidywalny, nie "bardziej losowy".</strong> Dobry PRNG i crypto RNG dają nierozróżnialne rozkłady dla kostek. Przewaga crypto polega na tym, że nikt nie przewidzi następnej liczby z poprzednich.</li>
  <li><strong>Modyfikatory aplikują się raz, po keep.</strong> <code>4d6kh3+2</code> rzuca 4d6, zachowuje top 3, a potem dodaje 2 — nie "dodaje 2 do każdej kostki".</li>
  <li><strong>To nie są exploding dice.</strong> Brak eksplozji w stylu <code>!</code>, brak rerollów (<code>r1</code>), brak liczenia sukcesów (<code>3d10>=7</code>). Notacja tu to prosty subset "suma i modyfikuj", który pokrywa ~95% typowych rzutów.</li>
  <li><strong>Crity są oznaczane tylko dla d20.</strong> 20 podświetla się na zielono, 1 na czerwono. Inne rozmiary nie dostają koloru.</li>
  <li><strong>Limit 1000 kości na rzut.</strong> Rozsądna górna granica, żeby strona nie zamulała.</li>
</ul>
""",
    },
    "related": ["password-generator", "uuid-generator", "percentage-calculator"],
}
