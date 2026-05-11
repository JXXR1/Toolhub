TOOL = {
    "slug": "regex-cheatsheet",
    "category": "developer",
    "icon": "📖",
    "tags": ["regex", "cheatsheet", "reference", "pattern", "anchors", "groups", "lookaround"],
    "i18n": {
        "en": {
            "name": "Regex Cheatsheet",
            "tagline": "Quick reference: anchors, character classes, quantifiers, groups, lookarounds, flags. Click any pattern to copy.",
            "description": "Free regex (regular expression) cheatsheet. Anchors, character classes, quantifiers, groups, lookarounds and flags — with click-to-copy patterns and a live filter. PCRE / JavaScript flavour.",
        },
        "de": {"name": "Regex-Spickzettel", "tagline": "Schnellreferenz: Anker, Zeichenklassen, Quantoren, Gruppen, Lookarounds, Flags. Muster zum Kopieren anklicken.", "description": "Kostenloser Regex-Spickzettel. Anker, Zeichenklassen, Quantoren, Gruppen, Lookarounds und Flags — mit Klick-zum-Kopieren und Filter. PCRE / JavaScript."},
        "es": {"name": "Chuleta Regex", "tagline": "Referencia rápida: anclas, clases de caracteres, cuantificadores, grupos, lookarounds, flags. Haz clic en cualquier patrón para copiarlo.", "description": "Chuleta de regex (expresiones regulares) gratuita. Anclas, clases, cuantificadores, grupos, lookarounds y flags — con copiar al clic y filtro. PCRE / JavaScript."},
        "fr": {"name": "Aide-mémoire Regex", "tagline": "Référence rapide : ancres, classes de caractères, quantificateurs, groupes, lookarounds, drapeaux. Cliquez pour copier un motif.", "description": "Aide-mémoire regex (expressions régulières) gratuit. Ancres, classes, quantificateurs, groupes, lookarounds et flags — avec copie au clic et filtre. PCRE / JavaScript."},
        "it": {"name": "Cheatsheet Regex", "tagline": "Riferimento rapido: ancore, classi di caratteri, quantificatori, gruppi, lookaround, flag. Clicca un pattern per copiarlo.", "description": "Cheatsheet regex (espressioni regolari) gratuito. Ancore, classi, quantificatori, gruppi, lookaround e flag — con copia al clic e filtro. PCRE / JavaScript."},
        "pt": {"name": "Cheatsheet de Regex", "tagline": "Referência rápida: anchors, classes de caracteres, quantificadores, grupos, lookarounds, flags. Clique em qualquer pattern para copiar.", "description": "Cheatsheet de regex gratuito. Anchors, classes de caracteres, quantificadores, grupos, lookarounds e flags — com clique-para-copiar e filtro ao vivo. Sabor PCRE / JavaScript."},
        "pl": {"name": "Ściąga Regex", "tagline": "Szybka referencja: anchory, klasy znaków, kwantyfikatory, grupy, lookaroundy, flagi. Kliknij dowolny pattern, by skopiować.", "description": "Darmowa ściąga regex (wyrażenia regularne). Anchory, klasy znaków, kwantyfikatory, grupy, lookaroundy i flagi — z klikaniem do skopiowania i filtrem na żywo. Smak PCRE / JavaScript."},
        "ja": {"name": "正規表現チートシート", "tagline": "クイックリファレンス：アンカー、文字クラス、量指定子、グループ、後読み／先読み、フラグ。クリックでコピー。", "description": "無料の正規表現チートシート。アンカー、文字クラス、量指定子、グループ、ルックアラウンド、フラグを網羅し、クリックでコピー、ライブフィルタにも対応。PCRE / JavaScript 風です。"},
        "nl": {"name": "Regex Spiekbrief", "tagline": "Snelle referentie: anchors, character classes, quantifiers, groups, lookarounds, flags. Klik elk patroon om te kopiëren.", "description": "Gratis regex (regular expression)-spiekbrief. Anchors, character classes, quantifiers, groups, lookarounds en flags — met click-to-copy patronen en een live filter. PCRE / JavaScript flavour."},
        "tr": {"name": "Regex Çetel", "tagline": "Hızlı referans: çapalar, karakter sınıfları, niceleyiciler, gruplar, lookaround'lar, bayraklar. Kopyalamak için herhangi bir desene tıkla.", "description": "Ücretsiz regex (düzenli ifade) çeteli. Çapalar, karakter sınıfları, niceleyiciler, gruplar, lookaround'lar ve bayraklar — tıkla-kopyala desenler ve canlı filtre ile. PCRE / JavaScript lehçesi."},
    },
    "body": """
<div class="tool-card">
  <label>Filter</label>
  <input type="text" id="rc-filter" oninput="rcFilter()" placeholder="e.g. 'lookahead', 'digit', '?='" autocomplete="off" spellcheck="false">
  <div class="meta" style="margin-top:0.5rem">Click any pattern in the table to copy it. Examples are illustrative.</div>
</div>
<div id="rc-sections"></div>
""",
    "script": """
<style>
.rc-section { background: var(--surface); border: 1px solid var(--border); border-radius: 10px; padding: 1.1rem 1.25rem; margin-bottom: 1rem; }
.rc-section h3 { font-size: 0.95rem; margin-bottom: 0.6rem; color: var(--text); }
.rc-section table { width: 100%; }
.rc-section td { vertical-align: top; padding: 0.4rem 0.5rem; border-bottom: 1px solid var(--border); }
.rc-section td:first-child { width: 28%; }
.rc-section td:nth-child(2) { width: 38%; color: var(--text-muted); }
.rc-section td:nth-child(3) { font-family: ui-monospace, monospace; font-size: 0.82rem; color: var(--text-muted); }
.rc-pat { font-family: ui-monospace, monospace; font-size: 0.85rem; background: var(--code-bg); padding: 0.18rem 0.5rem; border-radius: 4px; cursor: pointer; user-select: all; border: 1px solid var(--border); display: inline-block; }
.rc-pat:hover { border-color: var(--accent); color: var(--accent); }
.rc-pat.copied { background: var(--green); color: #fff; border-color: var(--green); }
.rc-section.hidden { display: none; }
.rc-row.hidden { display: none; }
@media (max-width: 600px) {
  .rc-section { padding: 0.9rem 0.75rem; }
  .rc-section table, .rc-section thead, .rc-section tbody, .rc-section tr { display: block; width: 100%; }
  .rc-section td { display: block; width: 100% !important; padding: 0.2rem 0; border-bottom: none; }
  .rc-section tr { padding: 0.55rem 0; border-bottom: 1px solid var(--border); }
  .rc-section tr:last-child { border-bottom: none; }
  .rc-section td:nth-child(3) { font-size: 0.78rem; }
}
</style>
<script>
const RC_DATA = [
  {
    title: 'Anchors',
    rows: [
      ['^', 'Start of line/string', 'matches before the first char'],
      ['$', 'End of line/string', 'matches after the last char'],
      ['\\\\b', 'Word boundary', 'between \\\\w and \\\\W'],
      ['\\\\B', 'Non-word boundary', 'inside or outside a word run'],
      ['\\\\A', 'Start of string (PCRE)', 'never per-line; not in JS'],
      ['\\\\Z', 'End of string (PCRE)', 'never per-line; not in JS'],
    ]
  },
  {
    title: 'Character classes',
    rows: [
      ['.', 'Any char except newline', "with /s flag, includes \\n"],
      ['\\\\d', 'Digit', '[0-9]'],
      ['\\\\D', 'Non-digit', '[^0-9]'],
      ['\\\\w', 'Word char', '[A-Za-z0-9_]'],
      ['\\\\W', 'Non-word char', "[^A-Za-z0-9_]"],
      ['\\\\s', 'Whitespace', 'space, tab, newline, etc.'],
      ['\\\\S', 'Non-whitespace', ''],
      ['[abc]', 'Any of a, b, c', 'character set'],
      ['[^abc]', 'Anything except a, b, c', 'negated set'],
      ['[a-z]', 'Lowercase ASCII letter', 'range'],
      ['[a-zA-Z0-9_]', 'Word-char-equivalent', '== \\\\w (ASCII)'],
      ['\\\\p{L}', 'Any Unicode letter', 'requires /u flag'],
      ['\\\\p{N}', 'Any Unicode number', 'requires /u flag'],
    ]
  },
  {
    title: 'Quantifiers',
    rows: [
      ['*', '0 or more', 'greedy'],
      ['+', '1 or more', 'greedy'],
      ['?', '0 or 1', 'optional'],
      ['{n}', 'Exactly n', 'fixed count'],
      ['{n,}', 'n or more', ''],
      ['{n,m}', 'Between n and m', ''],
      ['*?', 'Lazy 0 or more', 'matches as few as possible'],
      ['+?', 'Lazy 1 or more', 'matches as few as possible'],
      ['??', 'Lazy 0 or 1', ''],
      ['*+', 'Possessive 0 or more', 'PCRE only, no backtracking'],
    ]
  },
  {
    title: 'Groups & alternation',
    rows: [
      ['(abc)', 'Capturing group', 'referenced as $1'],
      ['(?:abc)', 'Non-capturing group', 'no backref number'],
      ['(?<name>abc)', 'Named capturing group', 'referenced as $<name>'],
      ['a|b', 'Either a or b', 'alternation'],
      ['\\\\1', 'Backreference to group 1', 'matches what group 1 matched'],
      ['\\\\k<name>', 'Backreference to named group', 'JS / PCRE'],
    ]
  },
  {
    title: 'Lookarounds',
    rows: [
      ['(?=foo)', 'Positive lookahead', 'followed by foo'],
      ['(?!foo)', 'Negative lookahead', 'NOT followed by foo'],
      ['(?<=foo)', 'Positive lookbehind', 'preceded by foo'],
      ['(?<!foo)', 'Negative lookbehind', 'NOT preceded by foo'],
    ]
  },
  {
    title: 'Flags (modifiers)',
    rows: [
      ['g', 'Global', 'find all matches, not just first'],
      ['i', 'Case-insensitive', 'A == a'],
      ['m', 'Multi-line', '^ and $ per line'],
      ['s', 'Dotall', '. matches newline'],
      ['u', 'Unicode', 'enables \\\\p{...}, surrogate-aware'],
      ['y', 'Sticky (JS)', 'match only at lastIndex'],
      ['x', 'Extended (PCRE)', 'free-spacing & comments'],
    ]
  },
  {
    title: 'Common patterns',
    rows: [
      ['^\\\\s*$', 'Empty / whitespace-only line', 'with /m flag'],
      ['\\\\b\\\\w+@\\\\w+\\\\.\\\\w+\\\\b', 'Email-ish', 'not RFC-strict'],
      ['^https?://', 'Starts with http:// or https://', ''],
      ['\\\\b\\\\d{4}-\\\\d{2}-\\\\d{2}\\\\b', 'ISO date YYYY-MM-DD', ''],
      ['^\\\\+?[1-9]\\\\d{6,14}$', 'E.164-ish phone', 'rough, not strict'],
      ['([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}', 'MAC address', '6 colon-separated hex pairs'],
      ['\\\\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[1-5][0-9a-fA-F]{3}-[89ab][0-9a-fA-F]{3}-[0-9a-fA-F]{12}\\\\b', 'UUID v1-5', 'canonical form'],
      ['#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\\\\b', 'CSS hex colour', '#fff or #ffffff'],
    ]
  }
];

function rcEsc(s){ return s.replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c])); }

function rcRender(){
  const wrap = document.getElementById('rc-sections');
  wrap.innerHTML = '';
  RC_DATA.forEach(sec => {
    const div = document.createElement('div');
    div.className = 'rc-section';
    div.dataset.title = sec.title.toLowerCase();
    let rows = sec.rows.map(r =>
      `<tr class="rc-row" data-q="${rcEsc((r[0]+' '+r[1]+' '+r[2]).toLowerCase())}">` +
        `<td><span class="rc-pat" onclick="rcCopy(this)">${rcEsc(r[0])}</span></td>` +
        `<td>${rcEsc(r[1])}</td>` +
        `<td>${rcEsc(r[2])}</td>` +
      `</tr>`).join('');
    div.innerHTML = `<h3>${rcEsc(sec.title)}</h3><table>${rows}</table>`;
    wrap.appendChild(div);
  });
}

function rcCopy(el){
  const t = el.textContent;
  navigator.clipboard.writeText(t).then(()=>{
    el.classList.add('copied');
    setTimeout(()=>el.classList.remove('copied'), 700);
  });
}

function rcFilter(){
  const q = document.getElementById('rc-filter').value.trim().toLowerCase();
  document.querySelectorAll('.rc-section').forEach(sec => {
    let any = false;
    sec.querySelectorAll('.rc-row').forEach(r => {
      const match = !q || r.dataset.q.includes(q) || sec.dataset.title.includes(q);
      r.classList.toggle('hidden', !match);
      if(match) any = true;
    });
    sec.classList.toggle('hidden', !any);
  });
}

document.addEventListener('DOMContentLoaded', () => (window.requestIdleCallback || ((cb)=>setTimeout(cb,0)))(rcRender));
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>A printable, searchable summary of the bits of regex syntax you keep half-remembering. The tables here cover the major categories — anchors, character classes, quantifiers, groups, lookarounds, flags — plus a starter set of common patterns. Click any pattern to copy it; type in the filter to narrow down. Pair this with the <a href="/regex-tester/">Regex Tester</a> to actually try the patterns against text.</p>

<h3>When to use it</h3>
<ul>
  <li>You need <code>(?&lt;=foo)</code> and can't remember whether <code>?</code> goes before or after the <code>&lt;</code>.</li>
  <li>You're explaining regex to someone and need a stable reference page rather than rummaging through Stack Overflow tabs.</li>
  <li>You want a starter pattern (UUID, email, ISO date) you can copy and tweak rather than write from scratch.</li>
  <li>You need to know which flag does what — particularly <code>s</code> (dotall) vs <code>m</code> (multi-line), which people routinely mix up.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Flavour matters.</strong> Most of this is JavaScript / modern PCRE, but features differ. Lookbehind only landed in JavaScript with ES2018; <code>x</code> (extended) is PCRE/Python and not in JS; possessive quantifiers <code>++</code> are PCRE-only.</li>
  <li><strong><code>m</code> ≠ "multi-line matching".</strong> <code>m</code> changes what <code>^</code> and <code>$</code> mean (per-line instead of per-string). To match across line breaks with <code>.</code>, you want <code>s</code> (dotall).</li>
  <li><strong>Greedy matches eat too much.</strong> <code>&lt;.*&gt;</code> against <code>&lt;a&gt;b&lt;/a&gt;</code> matches the whole thing, not just <code>&lt;a&gt;</code>. Use <code>&lt;.*?&gt;</code> for the lazy version, or better yet a more specific class like <code>&lt;[^&gt;]+&gt;</code>.</li>
  <li><strong>Regex isn't an HTML or JSON parser.</strong> The "common patterns" here are good for one-off scraping or validation hints, not for treating structured input as a string.</li>
  <li><strong>Email regexes are always wrong.</strong> The example here is a rough shape-check; for production validation, send a confirmation email instead.</li>
  <li><strong>Don't trust copy-pasted "perfect" regexes.</strong> Test them against your real data with the Regex Tester before deploying.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Um resumo imprimível e pesquisável dos pedaços de sintaxe regex que você sempre lembra pela metade. As tabelas aqui cobrem as categorias principais — anchors, classes de caracteres, quantificadores, grupos, lookarounds, flags — além de um conjunto inicial de patterns comuns. Clique em qualquer pattern para copiar; digite no filtro para restringir. Combine com o <a href="/regex-tester/">Regex Tester</a> para realmente testar os patterns contra texto.</p>

<h3>Quando usar</h3>
<ul>
  <li>Você precisa de <code>(?&lt;=foo)</code> e não lembra se o <code>?</code> vai antes ou depois do <code>&lt;</code>.</li>
  <li>Você está explicando regex para alguém e precisa de uma página de referência estável em vez de vasculhar abas do Stack Overflow.</li>
  <li>Você quer um pattern inicial (UUID, e-mail, data ISO) para copiar e ajustar em vez de escrever do zero.</li>
  <li>Você precisa saber qual flag faz o quê — em particular <code>s</code> (dotall) vs <code>m</code> (multi-line), que as pessoas misturam toda hora.</li>
</ul>

<h3>Pegadinhas comuns</h3>
<ul>
  <li><strong>O sabor importa.</strong> A maior parte aqui é JavaScript / PCRE moderno, mas as features diferem. Lookbehind só chegou no JavaScript com ES2018; <code>x</code> (extended) é PCRE/Python e não existe em JS; quantificadores possessivos <code>++</code> são só PCRE.</li>
  <li><strong><code>m</code> ≠ "matching multi-linha".</strong> <code>m</code> muda o que <code>^</code> e <code>$</code> significam (por linha em vez de por string). Para que <code>.</code> bata em quebras de linha, você quer <code>s</code> (dotall).</li>
  <li><strong>Greedy come demais.</strong> <code>&lt;.*&gt;</code> contra <code>&lt;a&gt;b&lt;/a&gt;</code> casa a coisa toda, não só <code>&lt;a&gt;</code>. Use <code>&lt;.*?&gt;</code> para a versão lazy, ou melhor ainda uma classe mais específica como <code>&lt;[^&gt;]+&gt;</code>.</li>
  <li><strong>Regex não é parser de HTML ou JSON.</strong> Os "patterns comuns" aqui servem para scraping pontual ou dicas de validação, não para tratar entrada estruturada como string.</li>
  <li><strong>Regex de e-mail estão sempre erradas.</strong> O exemplo aqui é uma checagem grosseira de formato; para validação em produção, mande um e-mail de confirmação.</li>
  <li><strong>Não confie em regex "perfeitas" copiadas.</strong> Teste contra seus dados reais no Regex Tester antes de subir.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>Eine durchsuchbare Zusammenfassung der Regex-Syntax, die man immer halb vergisst. Tabellen für Anker, Zeichenklassen, Quantoren, Gruppen, Lookarounds, Flags — plus Beispielmuster. Muster anklicken zum Kopieren; Filter zum Eingrenzen. Mit dem <a href="/regex-tester/">Regex-Tester</a> kombinieren.</p>
<h3>Wann verwenden</h3>
<ul>
<li>Wenn man die exakte Lookbehind-Syntax vergessen hat.</li>
<li>Als stabile Referenz beim Erklären.</li>
<li>Startmuster (UUID/E-Mail/ISO-Datum) zum Anpassen.</li>
<li>Klärung welcher Flag was tut — besonders <code>s</code> vs <code>m</code>.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>Variante zählt.</strong> Meist JS/PCRE, aber Features unterscheiden sich. Lookbehind erst seit ES2018; <code>x</code> nicht in JS.</li>
<li><strong><code>m</code> ist nicht "mehrzeiliges Matching".</strong> Es ändert <code>^</code>/<code>$</code>; für <code>.</code> über Zeilen <code>s</code>.</li>
<li><strong>Greedy frisst zu viel.</strong> <code>&lt;.*&gt;</code> matched alles; Lazy <code>&lt;.*?&gt;</code> oder besser <code>&lt;[^&gt;]+&gt;</code>.</li>
<li><strong>Regex ist kein HTML/JSON-Parser.</strong></li>
<li><strong>E-Mail-Regexes sind immer falsch.</strong> Für Produktion eine Bestätigungsmail.</li>
<li><strong>Kopierten "perfekten" Regexes nicht trauen.</strong></li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>Un resumen filtrable de la sintaxis regex que siempre olvidas a medias. Tablas para anclas, clases, cuantificadores, grupos, lookarounds, flags — más patrones comunes. Haz clic para copiar; filtra para acotar. Combínalo con el <a href="/regex-tester/">Probador de Regex</a>.</p>
<h3>Cuándo usarlo</h3>
<ul>
<li>Cuando olvidas la sintaxis exacta de lookbehind.</li>
<li>Como referencia estable al explicar.</li>
<li>Patrón inicial (UUID/email/ISO) para ajustar.</li>
<li>Aclarar qué hace cada flag — sobre todo <code>s</code> vs <code>m</code>.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>El sabor importa.</strong> Esto es JS/PCRE moderno, pero hay diferencias. Lookbehind sólo desde ES2018.</li>
<li><strong><code>m</code> no es "matching multi-línea".</strong> Cambia <code>^</code>/<code>$</code>; para <code>.</code> con saltos usa <code>s</code>.</li>
<li><strong>Greedy come demasiado.</strong> Usa lazy o clases más específicas.</li>
<li><strong>Regex no es un parser HTML/JSON.</strong></li>
<li><strong>Las regex de email siempre están mal.</strong> En producción envía email de confirmación.</li>
<li><strong>No confíes en regex "perfectas" copiadas.</strong></li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Un résumé filtrable de la syntaxe regex qu'on oublie toujours à moitié. Tableaux pour ancres, classes, quantificateurs, groupes, lookarounds, drapeaux — plus motifs courants. Clic pour copier ; filtre pour cibler. À combiner avec le <a href="/regex-tester/">Testeur Regex</a>.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>Quand on oublie la syntaxe exacte du lookbehind.</li>
<li>Comme référence stable pour expliquer.</li>
<li>Motif de départ (UUID/email/ISO) à adapter.</li>
<li>Clarifier ce que fait chaque flag — surtout <code>s</code> vs <code>m</code>.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>La variante compte.</strong> JS/PCRE moderne ici. Lookbehind seulement depuis ES2018.</li>
<li><strong><code>m</code> n'est pas « matching multi-ligne ».</strong> Change <code>^</code>/<code>$</code> ; pour <code>.</code> sur retours utiliser <code>s</code>.</li>
<li><strong>Le greedy mange trop.</strong> Utiliser lazy ou des classes plus précises.</li>
<li><strong>Regex n'est pas un parseur HTML/JSON.</strong></li>
<li><strong>Les regex d'email sont toujours fausses.</strong> En production, email de confirmation.</li>
<li><strong>Ne pas faire confiance aux regex « parfaites » copiées.</strong></li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>Un riepilogo filtrabile della sintassi regex che dimentichi sempre a metà. Tabelle per ancore, classi, quantificatori, gruppi, lookaround, flag — più pattern comuni. Clicca per copiare; filtra per restringere. Da abbinare al <a href="/regex-tester/">Tester Regex</a>.</p>
<h3>Quando usarlo</h3>
<ul>
<li>Quando dimentichi la sintassi esatta del lookbehind.</li>
<li>Come riferimento stabile quando spieghi.</li>
<li>Pattern di partenza (UUID/email/ISO) da adattare.</li>
<li>Chiarire cosa fa ogni flag — soprattutto <code>s</code> vs <code>m</code>.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>La variante conta.</strong> JS/PCRE moderno qui. Lookbehind solo da ES2018.</li>
<li><strong><code>m</code> non è "matching multi-riga".</strong> Cambia <code>^</code>/<code>$</code>; per <code>.</code> su a-capo usa <code>s</code>.</li>
<li><strong>Il greedy mangia troppo.</strong> Usa lazy o classi più specifiche.</li>
<li><strong>Regex non è un parser HTML/JSON.</strong></li>
<li><strong>Le regex per email sono sempre sbagliate.</strong> In produzione manda email di conferma.</li>
<li><strong>Non fidarti delle regex "perfette" copiate.</strong></li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Drukowalne, przeszukiwalne podsumowanie kawałków składni regex, które ciągle pamiętasz w połowie. Tabele tu pokrywają główne kategorie — anchory, klasy znaków, kwantyfikatory, grupy, lookaroundy, flagi — plus startowy zestaw typowych patternów. Kliknij dowolny pattern, żeby go skopiować; wpisz w filtr, żeby zawęzić. Sparuj to z <a href="/regex-tester/">Regex Testerem</a>, żeby faktycznie odpalić te patterny na tekście.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Potrzebujesz <code>(?&lt;=foo)</code> i nie pamiętasz, czy <code>?</code> idzie przed czy po <code>&lt;</code>.</li>
  <li>Tłumaczysz komuś regex i potrzebujesz stabilnej strony referencyjnej zamiast grzebać po zakładkach Stack Overflow.</li>
  <li>Chcesz pattern startowy (UUID, email, ISO date) do skopiowania i podstrojenia, zamiast pisać od zera.</li>
  <li>Musisz wiedzieć, która flaga co robi — szczególnie <code>s</code> (dotall) vs <code>m</code> (multi-line), które ludzie regularnie mylą.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Wariant ma znaczenie.</strong> Większość tu to JavaScript / nowoczesny PCRE, ale ficze się różnią. Lookbehind wylądował w JS dopiero z ES2018; <code>x</code> (extended) jest w PCRE/Pythonie i nie ma go w JS; possessive quantifiery <code>++</code> są tylko w PCRE.</li>
  <li><strong><code>m</code> ≠ "multi-line matching".</strong> <code>m</code> zmienia, co znaczą <code>^</code> i <code>$</code> (per linia, nie per string). Żeby <code>.</code> łapało przez końce linii, chcesz <code>s</code> (dotall).</li>
  <li><strong>Greedy zżerają za dużo.</strong> <code>&lt;.*&gt;</code> przeciw <code>&lt;a&gt;b&lt;/a&gt;</code> matchuje całość, nie tylko <code>&lt;a&gt;</code>. Użyj <code>&lt;.*?&gt;</code> dla wersji lazy, albo lepiej bardziej specyficznej klasy w stylu <code>&lt;[^&gt;]+&gt;</code>.</li>
  <li><strong>Regex nie jest parserem HTML ani JSON.</strong> "Typowe patterny" tu są dobre do jednorazowego scrapingu albo wskazówek walidacyjnych, nie do traktowania strukturalnego inputu jak stringa.</li>
  <li><strong>Regexy do emaili są zawsze złe.</strong> Przykład tu jest grubym sprawdzeniem kształtu; do walidacji produkcyjnej lepiej wyślij maila potwierdzającego.</li>
  <li><strong>Nie ufaj skopiowanym "idealnym" regexom.</strong> Przetestuj je na swoich realnych danych w Regex Testerze przed deployem.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>正規表現でいつもなんとなくしか思い出せない構文を、検索・印刷可能な形でまとめたチートシートです。アンカー、文字クラス、量指定子、グループ、ルックアラウンド、フラグの主要カテゴリに加え、よくあるパターンの例も用意しています。任意のパターンをクリックでコピーでき、フィルタ入力で絞り込めます。実際にテキストに対して試したいときは <a href="/regex-tester/">正規表現テスター</a>と組み合わせてください。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li><code>(?&lt;=foo)</code> が必要なときに、<code>?</code> が <code>&lt;</code> の前か後ろか思い出したいとき。</li>
  <li>誰かに正規表現を説明する場面で、Stack Overflow のタブを漁るより、安定した参照ページがほしいとき。</li>
  <li>UUID、メール、ISO 日付のような出発点となるパターンをコピーして調整したいとき。</li>
  <li>各フラグの違いを確認したいとき — 特に <code>s</code>（dotall）と <code>m</code>（multi-line）の混同を解きたい場面。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>方言に注意。</strong> ここの内容はほぼ JavaScript／現代の PCRE ですが、機能差があります。lookbehind が JS に入ったのは ES2018、<code>x</code>（extended）は PCRE/Python であり JS にはなく、possessive 量指定子 <code>++</code> は PCRE 限定です。</li>
  <li><strong><code>m</code> は「複数行マッチ」ではありません。</strong> <code>m</code> は <code>^</code> と <code>$</code> の意味（行単位 or 文字列単位）を変えます。改行をまたいで <code>.</code> を当てたいなら <code>s</code>（dotall）が必要です。</li>
  <li><strong>greedy は食べすぎます。</strong> <code>&lt;.*&gt;</code> を <code>&lt;a&gt;b&lt;/a&gt;</code> に当てると全体にマッチします。lazy 版 <code>&lt;.*?&gt;</code> か、より具体的な <code>&lt;[^&gt;]+&gt;</code> を使ってください。</li>
  <li><strong>正規表現は HTML や JSON のパーサではありません。</strong> ここでの「よくあるパターン」は単発のスクレイピングや簡易検証向けで、構造化入力を文字列として扱うのには向きません。</li>
  <li><strong>メールの正規表現は常に「外れ」です。</strong> ここの例はおおまかな形チェックです。本番の検証はメールでの確認に頼ってください。</li>
  <li><strong>コピペした「完璧な」正規表現を信用しないこと。</strong> デプロイ前に Regex Tester で実データに対して試してください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Een printbare, doorzoekbare samenvatting van de stukjes regex-syntax die je je half blijft herinneren. De tabellen hier dekken de hoofdcategorieën — anchors, character classes, quantifiers, groups, lookarounds, flags — plus een starter-set veelvoorkomende patronen. Klik elk patroon om te kopiëren; typ in het filter om te versmallen. Combineer dit met de <a href="/regex-tester/">Regex Tester</a> om de patronen daadwerkelijk tegen tekst te proberen.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Je hebt <code>(?&lt;=foo)</code> nodig en kunt je niet herinneren of <code>?</code> voor of na <code>&lt;</code> staat.</li>
  <li>Je legt regex uit aan iemand en hebt een stabiele referentiepagina nodig in plaats van Stack Overflow-tabs door te wroeten.</li>
  <li>Je wil een starter-patroon (UUID, email, ISO-datum) dat je kunt kopiëren en tweaken in plaats van vanaf nul schrijven.</li>
  <li>Je wil weten welke flag wat doet — vooral <code>s</code> (dotall) vs <code>m</code> (multi-line), die mensen routinematig verwarren.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Flavour doet ertoe.</strong> Het meeste hier is JavaScript / moderne PCRE, maar features verschillen. Lookbehind landde in JavaScript pas met ES2018; <code>x</code> (extended) is PCRE/Python en niet in JS; possessive quantifiers <code>++</code> zijn alleen PCRE.</li>
  <li><strong><code>m</code> ≠ "multi-line matching".</strong> <code>m</code> verandert wat <code>^</code> en <code>$</code> betekenen (per-line in plaats van per-string). Om met <code>.</code> over line breaks heen te matchen wil je <code>s</code> (dotall).</li>
  <li><strong>Greedy matches eten te veel.</strong> <code>&lt;.*&gt;</code> tegen <code>&lt;a&gt;b&lt;/a&gt;</code> matcht het hele ding, niet alleen <code>&lt;a&gt;</code>. Gebruik <code>&lt;.*?&gt;</code> voor de lazy versie, of liever een specifiekere class als <code>&lt;[^&gt;]+&gt;</code>.</li>
  <li><strong>Regex is geen HTML- of JSON-parser.</strong> De "veelvoorkomende patronen" hier zijn goed voor eenmalig scrapen of validatie-hints, niet om structured input als string te behandelen.</li>
  <li><strong>Email-regexes zijn altijd fout.</strong> Het voorbeeld hier is een ruwe shape-check; voor production-validatie stuur je in plaats daarvan een bevestigingsmail.</li>
  <li><strong>Vertrouw geen copy-pasted "perfect" regexes.</strong> Test ze tegen je echte data met de Regex Tester voor je deployt.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Yarı hatırladığın regex sözdiziminin parçalarının yazdırılabilir, aranabilir bir özeti. Buradaki tablolar ana kategorileri kapsar — çapalar, karakter sınıfları, niceleyiciler, gruplar, lookaround'lar, bayraklar — artı yaygın desenlerin başlangıç seti. Bir deseni kopyalamak için tıkla; daraltmak için filtreye yaz. Desenleri metne karşı gerçekten denemek için bunu <a href="/regex-tester/">Regex Tester</a> ile eşle.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li><code>(?&lt;=foo)</code>'ya ihtiyacın var ve <code>?</code>'nin <code>&lt;</code>'den önce mi sonra mı geldiğini hatırlayamıyorsun.</li>
  <li>Birine regex anlatıyorsun ve Stack Overflow sekmeleri karıştırmak yerine kararlı bir referans sayfası gerekiyor.</li>
  <li>Sıfırdan yazmak yerine kopyalayıp ince ayarlayabileceğin bir başlangıç deseni (UUID, e-posta, ISO tarih) istiyorsun.</li>
  <li>Hangi bayrağın ne yaptığını bilmek istiyorsun — özellikle <code>s</code> (dotall) ve <code>m</code> (multi-line) ki insanlar rutin olarak karıştırır.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Lehçe önemlidir.</strong> Bunun çoğu JavaScript / modern PCRE'dir, ama özellikler değişir. Lookbehind JavaScript'e sadece ES2018 ile geldi; <code>x</code> (extended) PCRE/Python'dur ve JS'de yoktur; possessive niceleyiciler <code>++</code> sadece PCRE'dir.</li>
  <li><strong><code>m</code> ≠ "çok satırlı eşleştirme".</strong> <code>m</code> <code>^</code> ve <code>$</code>'ın anlamını değiştirir (string başına yerine satır başına). <code>.</code> ile satır sonları arasında eşleştirmek için <code>s</code> (dotall) istiyorsun.</li>
  <li><strong>Greedy eşleşmeler çok fazla yer.</strong> <code>&lt;a&gt;b&lt;/a&gt;</code>'a karşı <code>&lt;.*&gt;</code> tüm şeyi eşleştirir, sadece <code>&lt;a&gt;</code>'yı değil. Lazy sürüm için <code>&lt;.*?&gt;</code> kullan, veya daha iyisi <code>&lt;[^&gt;]+&gt;</code> gibi daha spesifik bir sınıf.</li>
  <li><strong>Regex bir HTML veya JSON parser değildir.</strong> Buradaki "yaygın desenler" tek seferlik kazıma veya doğrulama ipuçları için iyidir, yapılandırılmış girdiyi bir string olarak ele almak için değil.</li>
  <li><strong>E-posta regex'leri her zaman yanlıştır.</strong> Buradaki örnek kaba bir şekil kontrolüdür; production doğrulama için bunun yerine bir onay e-postası gönder.</li>
  <li><strong>Kopya-yapıştırılmış "mükemmel" regex'lere güvenme.</strong> Deploy etmeden önce gerçek verinle Regex Tester ile test et.</li>
</ul>
""",
    },
    "related": ["regex-tester", "ascii-table", "unicode-inspector", "http-status-codes"],
}
