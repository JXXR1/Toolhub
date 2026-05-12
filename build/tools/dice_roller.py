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
        "ja": {"name": "ダイスローラー", "tagline": "標準 D&D 記法でダイスをロール — 2d6+3、1d20、4d6 keep highest 3 など。暗号論的に安全な RNG。", "description": "オンライン無料のダイスローラー。標準的な TRPG 記法（1d20、2d6+3、4d6kh3、3d8-1）に対応し、各ダイスの目と合計を表示します。crypto.getRandomValues を使用し、公平で予測不能なロールを行います。"},
        "nl": {"name": "Dobbelsteen-roller", "tagline": "Gooi dobbelstenen met standaard D&D-notatie — 2d6+3, 1d20, 4d6 keep highest 3. Crypto-secure RNG.", "description": "Gratis online dobbelsteen-roller met standaard tabletop-notatie: 1d20, 2d6+3, 4d6kh3, 3d8-1. Zie elke individuele worp plus het totaal. Gebruikt crypto.getRandomValues voor eerlijke, onvoorspelbare worpen."},
        "tr": {"name": "Zar Atıcı", "tagline": "Standart D&D notasyonuyla zar at — 2d6+3, 1d20, 4d6 en yüksek 3'ü tut. Kripto-güvenli RNG.", "description": "Standart masaüstü notasyonuyla ücretsiz online zar atıcı: 1d20, 2d6+3, 4d6kh3, 3d8-1. Her tek atışı ve toplamı gör. Adil, öngörülemez atışlar için crypto.getRandomValues kullanır."},
        "id": {"name": "Pelempar Dadu", "tagline": "Lempar dadu dengan notasi D&D standar — 2d6+3, 1d20, 4d6 ambil 3 tertinggi. RNG kripto-aman.", "description": "Pelempar dadu online gratis. Mendukung notasi D&D standar (2d6+3, 1d20, 4d6kh3, 3d6!), advantage/disadvantage, eksplosi, dan keep-highest/lowest. Menggunakan crypto.getRandomValues — RNG kripto-aman."},
        "vi": {"name": "Tung Xúc xắc", "tagline": "Tung xúc xắc với notation D&D chuẩn — 2d6+3, 1d20, 4d6 lấy 3 cao nhất. RNG an toàn về mật mã.", "description": "Trình tung xúc xắc trực tuyến miễn phí. Hỗ trợ notation D&D chuẩn (1d20, 2d6+3, 4d6kh3, v.v.) bằng cách dùng crypto.getRandomValues của trình duyệt để các lần tung là công bằng và không thể đoán trước."},
    },
    "body": """
<div class="tool-card">
  <label>Dice notation</label>
  <input type="text" id="dr-notation" value="2d6+3" oninput="drValidate()" placeholder="e.g. 1d20, 2d6+3, 4d6kh3, 3d8-1" autocomplete="off" spellcheck="false" style="font-family:ui-monospace,monospace">
  <div class="meta" style="margin-top:0.4rem">Examples: <code>1d20</code> · <code>2d6+3</code> · <code>4d6kh3</code> (drop lowest) · <code>3d8-1</code> · <code>d100</code> · <code>2d20kl1</code> (disadvantage)</div>
  <div class="button-row" style="margin-top:0.7rem;flex-wrap:wrap">
    <button type="button" onclick="drRoll()">🎲 {LBL_ROLL}</button>
    <button type="button" class="secondary" onclick="drPreset('1d20')" style="padding:0.4rem 0.8rem;font-size:0.85rem">1d20</button>
    <button type="button" class="secondary" onclick="drPreset('2d6')" style="padding:0.4rem 0.8rem;font-size:0.85rem">2d6</button>
    <button type="button" class="secondary" onclick="drPreset('4d6kh3')" style="padding:0.4rem 0.8rem;font-size:0.85rem">4d6kh3</button>
    <button type="button" class="secondary" onclick="drPreset('1d100')" style="padding:0.4rem 0.8rem;font-size:0.85rem">d100</button>
    <button type="button" class="secondary" onclick="drPreset('2d20kh1')" style="padding:0.4rem 0.8rem;font-size:0.85rem">Adv (2d20kh1)</button>
    <button type="button" class="secondary" onclick="drPreset('2d20kl1')" style="padding:0.4rem 0.8rem;font-size:0.85rem">Dis (2d20kl1)</button>
    <button type="button" class="secondary" onclick="drClear()" style="padding:0.4rem 0.8rem;font-size:0.85rem">{LBL_CLEAR}</button>
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
        "ja": """
<h2>用途</h2>
<p>テーブルトップ RPG（Dungeons & Dragons、Pathfinder、OSR、その他多数）では、ダイスロールにコンパクトな記法を使います。<code>NdS</code> は「S 面ダイスを N 個振る」、<code>2d6+3</code> は「6 面ダイス 2 個を振って 3 を足す」という意味です。本ツールはこの記法をパースし、ブラウザの暗号論的 RNG でロールします。<code>Math.random()</code> よりも予測不能でバイアスがなく、重要なロールに適しています。</p>

<h3>サポートする記法</h3>
<ul>
  <li><code>1d20</code> — 20 面ダイス 1 個。</li>
  <li><code>2d6+3</code> — d6 を 2 個、合計 +3。</li>
  <li><code>3d8-1</code> — d8 を 3 個、合計 -1。</li>
  <li><code>4d6kh3</code> — d6 を 4 個、上位 3 個を <strong>k</strong>eep <strong>h</strong>ighest（D&D 5e の能力値ロールの定番）。</li>
  <li><code>2d20kl1</code> — d20 を 2 個、最低 1 個を残す（不利）。</li>
  <li><code>2d20kh1</code> — 有利。</li>
  <li><code>1d100</code> または <code>1d%</code> — パーセンタイルダイス。</li>
  <li><code>d20</code> — N は省略時 1。</li>
</ul>

<h3>使うべきタイミング</h3>
<ul>
  <li>オンラインで遊んでいて、物理ダイスが手元にない、またはリモートで GM をしているとき。</li>
  <li>ダイスアプリのサブスクなしで、再現可能な感覚のロールが欲しいとき。</li>
  <li>コインがなくても「コイントス」を決めたいとき（1d2）。</li>
  <li>ゲームデザインで確率をプロトタイピングしたいとき（100 万回振って統計が必要なら、コードでロジックを変更してください）。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>ブラウザのタブが信頼の境界です。</strong> ロールは JavaScript でタブ内で実行されるため、DevTools を開いている人は値を改ざんできます。見ず知らずの相手との競技プレイにはサーバーで仲裁するロールツールを使ってください。</li>
  <li><strong>暗号論的 RNG は「より乱数」なのではなく、予測不能なのです。</strong> 良質な PRNG と暗号論的 RNG はダイスでは区別できない分布を生成します。crypto の利点は、過去の値から次の値を予測できないことにあります。</li>
  <li><strong>修正値は keep の後に 1 度だけ適用されます。</strong> <code>4d6kh3+2</code> は 4d6 を振って上位 3 個を残し、最後に 2 を足します。「各ダイスに 2 を足す」のではありません。</li>
  <li><strong>exploding dice には対応しません。</strong> <code>!</code> 系の爆発、リロール（<code>r1</code>）、成功カウント（<code>3d10>=7</code>）はありません。ここでの記法はよくあるロールの 95% をカバーする「合計と修正」のサブセットです。</li>
  <li><strong>クリティカルは d20 でのみ表示されます。</strong> 20 は緑、1 は赤でハイライトされます。他のダイスサイズには色付けされません。</li>
  <li><strong>1 ロールあたり 1000 個まで。</strong> ページがレスポンシブで動くための上限です。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Tabletop role-playing games (Dungeons & Dragons, Pathfinder, de OSR, talloze andere) gebruiken een compacte notatie voor dobbelsteenworpen: <code>NdS</code> betekent "gooi N dobbelstenen met S zijden elk". <code>2d6+3</code> betekent "gooi twee zeszijdige dobbelstenen en tel 3 op". Deze tool parset die notatie en gooit de dobbelstenen met de cryptografische RNG van de browser, die onvoorspelbaar en onbevooroordeeld is — veel beter dan <code>Math.random()</code> voor worpen met inzet.</p>

<h3>Ondersteunde notatie</h3>
<ul>
  <li><code>1d20</code> — één twintigzijdige dobbelsteen.</li>
  <li><code>2d6+3</code> — twee d6, optellen, plus 3 modifier.</li>
  <li><code>3d8-1</code> — drie d8, optellen, min 1.</li>
  <li><code>4d6kh3</code> — vier d6, <strong>k</strong>eep <strong>h</strong>ighest 3 (klassieke D&D 5e ability score).</li>
  <li><code>2d20kl1</code> — twee d20, keep lowest 1 (disadvantage).</li>
  <li><code>2d20kh1</code> — advantage.</li>
  <li><code>1d100</code> of <code>1d%</code> — percentile dobbelsteen.</li>
  <li><code>d20</code> — N defaulted op 1.</li>
</ul>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Je speelt online, je fysieke dobbelstenen liggen buiten bereik, of je DM't op afstand.</li>
  <li>Je hebt een reproducible-feel worp nodig zonder dobbelsteen-app abonnement.</li>
  <li>Je wil "kruis of munt" beslechten zonder een muntje te vinden (1d2).</li>
  <li>Je prototypet een kans voor een game design (probeer een miljoen worpen — verander de formule in code als je stats wil).</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Browser-tab is de trust boundary.</strong> De worp gebeurt in je tab, in JavaScript — iemand met devtools open kan rommelen. Voor competitief spel met vreemden gebruik je een server-arbitrated roller.</li>
  <li><strong>Crypto-RNG is onvoorspelbaar, niet "meer random".</strong> Een goede PRNG en crypto-RNG produceren ononderscheidbare verdelingen voor dobbelstenen. Het voordeel van crypto is dat niemand het volgende getal kan voorspellen uit eerdere.</li>
  <li><strong>Modifiers worden eenmaal toegepast, na keep.</strong> <code>4d6kh3+2</code> gooit 4d6, houdt de top 3, telt dan 2 op — niet "telt 2 op bij elke dobbelsteen".</li>
  <li><strong>Dit is geen exploding dice.</strong> Geen <code>!</code>-style explosions, geen rerolls (<code>r1</code>), geen successes-counting (<code>3d10>=7</code>). De notatie hier is de simpele "sum and modify"-subset die ~95% van gewone worpen dekt.</li>
  <li><strong>Crits worden alleen gevlagd voor d20.</strong> Een 20 highlight groen, een 1 highlight rood. Andere dice-sizes krijgen geen kleuring.</li>
  <li><strong>Cap van 1000 dobbelstenen per worp.</strong> Verstandige bovengrens om de pagina responsive te houden.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Masaüstü rol yapma oyunları (Dungeons & Dragons, Pathfinder, OSR, sayısız diğeri) zar atışları için kompakt bir notasyon kullanır: <code>NdS</code> "her biri S yüzlü N zar at" anlamına gelir. <code>2d6+3</code> "iki altı yüzlü zar at ve 3 ekle" demektir. Bu araç bu notasyonu parse eder ve zarları tarayıcının kriptografik RNG'siyle atar; bu öngörülemez ve önyargısızdır — yüksek riskli atışlar için <code>Math.random()</code>'dan çok daha iyidir.</p>

<h3>Desteklenen notasyon</h3>
<ul>
  <li><code>1d20</code> — bir yirmi yüzlü zar.</li>
  <li><code>2d6+3</code> — iki d6, topla, artı 3 modifier.</li>
  <li><code>3d8-1</code> — üç d8, topla, eksi 1.</li>
  <li><code>4d6kh3</code> — dört d6, <strong>k</strong>eep en y<strong>h</strong>üksek 3 (klasik D&D 5e ability score).</li>
  <li><code>2d20kl1</code> — iki d20, en düşük 1'i tut (disadvantage).</li>
  <li><code>2d20kh1</code> — advantage.</li>
  <li><code>1d100</code> veya <code>1d%</code> — yüzdelik zar.</li>
  <li><code>d20</code> — N varsayılan 1.</li>
</ul>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Online oynuyorsun, fiziksel zarların ulaşılmaz veya uzaktan DM yapıyorsun.</li>
  <li>Zar uygulaması aboneliği olmadan tekrarlanabilir-hissi bir atışa ihtiyacın var.</li>
  <li>Madeni para bulmadan "haydi yazı tura atalım" (1d2) çözmek istiyorsun.</li>
  <li>Bir oyun tasarımı için olasılığı prototipliyorsun (bir milyon atış dene — istatistik istiyorsan kodda formülü değiştir).</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Tarayıcı sekmesi güven sınırıdır.</strong> Atış sekmende, JavaScript'te olur — devtools açık olan herkes hile yapabilir. Yabancılarla rekabetçi oyun için sunucu hakemli atıcı kullan.</li>
  <li><strong>Kripto RNG öngörülemez, "daha rastgele" değil.</strong> İyi bir PRNG ve kripto RNG zarlar için ayırt edilemez dağılımlar üretir. Kripto'nun avantajı kimsenin geçmişten sonraki sayıyı tahmin edememesidir.</li>
  <li><strong>Modifier'lar tutmadan sonra bir kez uygulanır.</strong> <code>4d6kh3+2</code> 4d6 atar, en yüksek 3'ü tutar, sonra 2 ekler — "her zara 2 ekle" değil.</li>
  <li><strong>Bu patlayan zar değildir.</strong> <code>!</code>-stili patlamalar yok, reroll'lar yok (<code>r1</code>), başarı sayımı yok (<code>3d10>=7</code>). Buradaki notasyon yaygın atışların ~%95'ini kapsayan basit "topla ve değiştir" alt kümesidir.</li>
  <li><strong>Kritikler sadece d20 için işaretlenir.</strong> 20 yeşil, 1 kırmızı vurgulanır. Diğer zar boyutları renklendirme almaz.</li>
  <li><strong>Atış başına 1000 zar sınırı.</strong> Sayfayı yanıt verir tutmak için makul üst sınır.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Tabletop role-playing game (Dungeons & Dragons, Pathfinder, OSR, dan banyak lainnya) menggunakan notasi ringkas untuk roll dice: <code>NdS</code> berarti "roll N dice dengan S sisi masing-masing". <code>2d6+3</code> berarti "roll dua dice enam sisi dan tambahkan 3". Tool ini mem-parse notasi itu dan me-roll dice menggunakan RNG kriptografi browser, yang unpredictable dan unbiased — jauh lebih baik daripada <code>Math.random()</code> untuk roll yang taruhannya tinggi.</p>

<h3>Notasi yang didukung</h3>
<ul>
  <li><code>1d20</code> — satu dice dua puluh sisi.</li>
  <li><code>2d6+3</code> — dua d6, jumlahkan, plus modifier 3.</li>
  <li><code>3d8-1</code> — tiga d8, jumlahkan, minus 1.</li>
  <li><code>4d6kh3</code> — empat d6, <strong>k</strong>eep <strong>h</strong>ighest 3 (ability score klasik D&D 5e).</li>
  <li><code>2d20kl1</code> — dua d20, keep lowest 1 (disadvantage).</li>
  <li><code>2d20kh1</code> — advantage.</li>
  <li><code>1d100</code> atau <code>1d%</code> — dice percentile.</li>
  <li><code>d20</code> — N default ke 1.</li>
</ul>

<h3>Kapan digunakan</h3>
<ul>
  <li>Kamu main online, dice fisik kamu di luar jangkauan, atau kamu jadi DM secara remote.</li>
  <li>Kamu butuh roll yang terasa reproducible tanpa langganan app dice.</li>
  <li>Kamu ingin menyelesaikan "ayo flip aja" tanpa cari koin (1d2).</li>
  <li>Kamu memprototipekan probabilitas untuk game design (coba sejuta roll — ubah formula di kode kalau kamu ingin stats).</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Tab browser adalah trust boundary.</strong> Roll terjadi di tab kamu, di JavaScript — siapa pun dengan devtools terbuka bisa memalsukannya. Untuk permainan kompetitif dengan orang asing, pakai roller yang di-arbitrasi server.</li>
  <li><strong>Crypto RNG itu unpredictable, bukan "lebih random".</strong> PRNG yang bagus dan crypto RNG menghasilkan distribusi yang tidak bisa dibedakan untuk dice. Keunggulan crypto adalah tidak ada yang bisa memprediksi angka berikutnya dari yang sebelumnya.</li>
  <li><strong>Modifier diterapkan sekali, setelah keep.</strong> <code>4d6kh3+2</code> me-roll 4d6, menyimpan 3 teratas, lalu menambah 2 — bukan "menambah 2 ke setiap dice".</li>
  <li><strong>Ini bukan exploding dice.</strong> Tidak ada explosion gaya <code>!</code>, tidak ada reroll (<code>r1</code>), tidak ada penghitungan sukses (<code>3d10>=7</code>). Notasi di sini adalah subset sederhana "sum and modify" yang menutupi ~95% roll umum.</li>
  <li><strong>Crit ditandai hanya untuk d20.</strong> Angka 20 di-highlight hijau, angka 1 di-highlight merah. Ukuran dice lain tidak mendapat pewarnaan.</li>
  <li><strong>Cap 1000 dice per roll.</strong> Batas atas yang masuk akal untuk menjaga halaman tetap responsif.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Notation xúc xắc D&D đóng gói "tung X xúc xắc Y mặt và làm Z với chúng" thành một chuỗi nhỏ: <code>2d6+3</code> là tung hai d6 và cộng 3, <code>4d6kh3</code> là tung bốn d6 và giữ ba cao nhất. Tool này phân tích notation, sử dụng <code>crypto.getRandomValues</code> để có ngẫu nhiên thực sự không thể đoán trước, và hiển thị từng kết quả tung cộng với tổng.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Chơi RPG bàn hoặc PBP và cần tung công bằng mà GM của bạn không thể chỉnh.</li>
  <li>Test xác suất — chạy 1000 lần tung <code>2d6</code> và kiểm tra phân phối.</li>
  <li>Chọn ngẫu nhiên — <code>1d20</code> để chọn một mục từ 20 lựa chọn.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>RNG mã hóa không phải là "chống gian lận".</strong> Trừ khi bạn ngồi bên cạnh người tung, không có RNG nào có thể chứng minh được không bị giả mạo. Đối với chơi nghiêm túc, dùng tool tung được ký bằng mã hóa hoặc tung trực tiếp.</li>
  <li><strong>"Drop the lowest" và "keep the highest" không giống nhau với tổng số xúc xắc khác nhau.</strong> 4d6 keep highest 3 ≠ 4d6 drop lowest 1 chỉ khi notation rõ ràng về việc khớp.</li>
  <li><strong>Notation D&D không phổ thông.</strong> Một số hệ thống chơi (Storyteller, World of Darkness, dicepool games) dùng cú pháp khác. Tool này tập trung vào notation D&D / Pathfinder.</li>
</ul>
""",
    },
    "related": ["password-generator", "uuid-generator", "percentage-calculator"],
    "howto": {"flow": "generate",  "action": "roll",    "noun": "roll"},
}
