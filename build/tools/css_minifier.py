TOOL = {
    "slug": "css-minifier",
    "category": "developer",
    "icon": "{}",
    "tags": ["css", "minify", "compress", "optimize", "stylesheet"],
    "i18n": {
        "en": {
            "name": "CSS Minifier",
            "tagline": "Strip comments, whitespace, and redundancy from CSS. See size before/after and the saving percentage.",
            "description": "Free online CSS minifier. Removes comments, collapses whitespace, trims trailing semicolons and zero units. Shows compression ratio.",
        },
        "de": {"name": "CSS-Minifier", "tagline": "Kommentare, Leerzeichen und Redundanz aus CSS entfernen. Vorher/Nachher-Größe und Einsparung anzeigen.", "description": "Kostenloser CSS-Minifier. Entfernt Kommentare, kürzt Leerzeichen, trimmt überflüssige Semikolons und Null-Einheiten. Mit Kompressionsanzeige."},
        "es": {"name": "Minificador CSS", "tagline": "Elimina comentarios, espacios y redundancia del CSS. Compara tamaños y porcentaje de ahorro.", "description": "Minificador CSS en línea gratuito. Elimina comentarios, comprime espacios, recorta puntos y comas y unidades cero. Muestra ratio de compresión."},
        "fr": {"name": "Minificateur CSS", "tagline": "Supprimez commentaires, espaces et redondances du CSS. Tailles avant/après et pourcentage d'économie.", "description": "Minificateur CSS gratuit. Supprime commentaires, espaces inutiles, point-virgules superflus et unités zéro. Affiche le taux de compression."},
        "it": {"name": "Minificatore CSS", "tagline": "Rimuovi commenti, spazi e ridondanza dal CSS. Vedi dimensione prima/dopo e percentuale di risparmio.", "description": "Minificatore CSS online gratuito. Rimuove commenti, comprime spazi, taglia punti e virgola e unità zero. Mostra il rapporto di compressione."},
        "pt": {"name": "Minificador CSS", "tagline": "Remova comentários, espaços e redundância do CSS. Veja o tamanho antes/depois e o percentual de economia.", "description": "Minificador CSS online gratuito. Remove comentários, colapsa espaços, corta ponto e vírgula final e unidades zero. Mostra a taxa de compressão."},
        "pl": {"name": "Minifikator CSS", "tagline": "Usuń komentarze, białe znaki i nadmiarowość z CSS. Zobacz rozmiar przed/po i procent oszczędności.", "description": "Darmowy online minifikator CSS. Usuwa komentarze, zwija białe znaki, ucina końcowe średniki i jednostki zero. Pokazuje współczynnik kompresji."},
    },
    "body": """
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="cm-input" oninput="cmRun()" placeholder="/* paste your CSS here */
.button {
  background: #3b82f6;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  color: #ffffff;
}" spellcheck="false">/* sample */
.button {
  background-color: #3b82f6;
  padding: 0.5rem 1.0rem;
  border-radius: 6px;
  color: #ffffff;
  margin: 0px 0px 0px 0px;
}

/* hover state */
.button:hover {
  background-color: #2563eb;
}</textarea>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="cm-out" style="white-space:pre-wrap;word-break:break-all"></pre>
    <button class="copy-btn secondary" onclick="copyOutput('cm-out', this)">{LBL_COPY}</button>
  </div>
  <div class="meta" id="cm-stats" style="margin-top:0.6rem"></div>
</div>
""",
    "script": """
<script>
function copyOutput(id, btn){
  const el = document.getElementById(id);
  navigator.clipboard.writeText(el.textContent || '');
  const o = btn.textContent; btn.textContent = '✓'; setTimeout(()=>btn.textContent = o, 900);
}
function cmMinify(css){
  // Strip /* … */ comments (non-greedy)
  let out = css.replace(/\\/\\*[\\s\\S]*?\\*\\//g, '');
  // Preserve string contents — quick mask
  const strings = [];
  out = out.replace(/("([^"\\\\]|\\\\.)*"|'([^'\\\\]|\\\\.)*')/g, m => { strings.push(m); return '\\u0001' + (strings.length-1) + '\\u0002'; });
  // Collapse all whitespace
  out = out.replace(/\\s+/g, ' ');
  // Tighten around punctuation
  out = out.replace(/\\s*([{}:;,>~+])\\s*/g, '$1');
  // Trim trailing ; before }
  out = out.replace(/;}/g, '}');
  // Drop leading zeros (0.5 → .5) but keep 0 alone
  out = out.replace(/(^|[\\s:,(])0+(\\.\\d+)/g, '$1$2');
  // Zero units (0px, 0em, 0% → 0) — but not in calc() and not for time/angle where 0s differs
  out = out.replace(/(^|[\\s:,(])(0)(px|em|rem|%|vh|vw|pt|pc|ex|ch)(?=[\\s,;)})]|$)/g, '$1$2');
  // Hex shortening (#aabbcc → #abc)
  out = out.replace(/#([0-9a-f])\\1([0-9a-f])\\2([0-9a-f])\\3/gi, '#$1$2$3');
  // Restore strings
  out = out.replace(/\\u0001(\\d+)\\u0002/g, (_, i) => strings[+i]);
  return out.trim();
}
function cmRun(){
  const src = document.getElementById('cm-input').value;
  const out = document.getElementById('cm-out');
  const stats = document.getElementById('cm-stats');
  if(!src.trim()){ out.textContent = '{LBL_NO_INPUT}'; stats.textContent = ''; return; }
  const min = cmMinify(src);
  out.textContent = min;
  const before = new Blob([src]).size;
  const after = new Blob([min]).size;
  const saved = before - after;
  const pct = before ? Math.round((saved/before)*100) : 0;
  stats.textContent = `Original: ${before.toLocaleString()} B · Minified: ${after.toLocaleString()} B · Saved: ${saved.toLocaleString()} B (${pct}%)`;
}
document.addEventListener('DOMContentLoaded', cmRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>CSS that's readable in source — with comments, indentation, and meaningful whitespace — bloats the file your users download. A structural minifier strips all the cosmetic bytes (comments, runs of whitespace, redundant zeros, equivalent shorter hex codes) without changing the rules' meaning. This tool runs that pass in your browser and shows the size before/after so you can see the saving.</p>

<h3>When to use it</h3>
<ul>
  <li>One-off shipping a CSS snippet inline in an HTML email or a blog post template, where you want the bytes shrunk but don't have a build chain.</li>
  <li>Quickly checking how much "fat" is in a stylesheet before deciding whether a real optimiser is worth wiring up.</li>
  <li>Pasting a vendor's pretty-printed CSS to slim it down for inclusion in a third-party widget.</li>
</ul>

<h3>What it does</h3>
<ul>
  <li>Strips block comments (<code>/* … */</code>) — single-line <code>//</code> isn't valid plain CSS anyway.</li>
  <li>Collapses whitespace around <code>{ } : ; ,</code> and combinators (<code>&gt; ~ +</code>).</li>
  <li>Drops trailing semicolons before <code>}</code>.</li>
  <li>Trims leading zeros (<code>0.5</code> → <code>.5</code>) and removes units from zero (<code>0px</code> → <code>0</code>).</li>
  <li>Shortens hex colours where exact (<code>#aabbcc</code> → <code>#abc</code>).</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>This is a structural minify, not a full optimiser.</strong> It won't merge duplicate selectors, reorder rules, or rewrite shorthand. For that, run <code>cssnano</code> or <code>esbuild</code> in your build pipeline.</li>
  <li><strong>Source maps aren't generated.</strong> If you debug minified CSS in production, ship them separately.</li>
  <li><strong>Don't minify the CSS you commit.</strong> Commit pretty source; minify at build/deploy. Mixing the two makes diff review miserable.</li>
  <li><strong>Modern compression dominates.</strong> Brotli/gzip on the wire does much of what minification does. The biggest savings come from removing unused rules — a job for tree-shaking, not minification.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>CSS legível no código-fonte — com comentários, indentação e espaços significativos — incha o arquivo que seus usuários baixam. Um minificador estrutural retira todos os bytes cosméticos (comentários, sequências de espaços, zeros redundantes, códigos hex equivalentes mais curtos) sem mudar o significado das regras. Esta ferramenta roda essa passagem no seu browser e mostra o tamanho antes/depois para você ver a economia.</p>

<h3>Quando usar</h3>
<ul>
  <li>Enviar pontualmente um snippet de CSS inline num email HTML ou template de blog, onde quer encolher os bytes mas não tem cadeia de build.</li>
  <li>Verificar rapidamente quanta "gordura" tem num stylesheet antes de decidir se vale a pena conectar um otimizador de verdade.</li>
  <li>Colar um CSS pretty-printed de algum fornecedor para enxugá-lo e incluir num widget de terceiro.</li>
</ul>

<h3>O que ele faz</h3>
<ul>
  <li>Remove comentários de bloco (<code>/* … */</code>) — single-line <code>//</code> não é CSS válido puro mesmo.</li>
  <li>Colapsa espaços ao redor de <code>{ } : ; ,</code> e combinadores (<code>&gt; ~ +</code>).</li>
  <li>Tira ponto e vírgula final antes de <code>}</code>.</li>
  <li>Remove zeros à esquerda (<code>0.5</code> → <code>.5</code>) e remove unidades de zero (<code>0px</code> → <code>0</code>).</li>
  <li>Encurta cores hex onde for exato (<code>#aabbcc</code> → <code>#abc</code>).</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Isto é uma minificação estrutural, não um otimizador completo.</strong> Não vai mesclar seletores duplicados, reordenar regras nem reescrever shorthands. Para isso, rode <code>cssnano</code> ou <code>esbuild</code> no seu pipeline de build.</li>
  <li><strong>Source maps não são gerados.</strong> Se for fazer debug de CSS minificado em produção, envie-os separadamente.</li>
  <li><strong>Não comite o CSS minificado.</strong> Comite o source bonito; minifique no build/deploy. Misturar os dois deixa o review de diff miserável.</li>
  <li><strong>Compressão moderna domina.</strong> Brotli/gzip no fio faz boa parte do que a minificação faz. As maiores economias vêm de remover regras não usadas — trabalho de tree-shaking, não de minificação.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>CSS, który jest czytelny w źródle — z komentarzami, wcięciami i znaczącymi białymi znakami — pęcznieje plik, który ściągają twoi użytkownicy. Strukturalny minifikator wycina wszystkie kosmetyczne bajty (komentarze, ciągi białych znaków, redundantne zera, krótsze równoważne kody hex) bez zmiany znaczenia reguł. To narzędzie robi tę przejazdkę w przeglądarce i pokazuje rozmiar przed/po, żebyś zobaczył oszczędność.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Jednorazowe wysłanie snippetu CSS inline w mailu HTML albo szablonie blogowym, gdzie chcesz zmniejszyć bajty, ale nie masz pipeline'u buildowego.</li>
  <li>Szybkie sprawdzenie, ile "tłuszczu" jest w stylesheecie, zanim zdecydujesz, czy warto podpiąć prawdziwy optymalizator.</li>
  <li>Wklejanie pretty-printed CSS od jakiegoś dostawcy, żeby go odchudzić do włączenia w widget zewnętrzny.</li>
</ul>

<h3>Co robi</h3>
<ul>
  <li>Wycina komentarze blokowe (<code>/* … */</code>) — single-line <code>//</code> i tak nie jest poprawnym czystym CSS-em.</li>
  <li>Zwija białe znaki wokół <code>{ } : ; ,</code> i kombinatorów (<code>&gt; ~ +</code>).</li>
  <li>Ucina końcowe średniki przed <code>}</code>.</li>
  <li>Wycina wiodące zera (<code>0.5</code> → <code>.5</code>) i usuwa jednostki z zera (<code>0px</code> → <code>0</code>).</li>
  <li>Skraca kolory hex, gdzie to bezstratne (<code>#aabbcc</code> → <code>#abc</code>).</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>To strukturalna minifikacja, nie pełny optymalizator.</strong> Nie zmerguje duplikatów selektorów, nie przegrupuje reguł ani nie przepisze shorthandów. Do tego użyj <code>cssnano</code> albo <code>esbuilda</code> w pipeline buildowym.</li>
  <li><strong>Source mapy nie są generowane.</strong> Jeśli debugujesz zminifikowany CSS na produkcji, wysyłaj je osobno.</li>
  <li><strong>Nie commituj zminifikowanego CSS-a.</strong> Commituj ładne źródło; minifikuj na buildzie/deployu. Mieszanie tych dwóch sprawia, że review diffów staje się męką.</li>
  <li><strong>Nowoczesna kompresja dominuje.</strong> Brotli/gzip na drucie robi większość tego, co minifikacja. Największe oszczędności biorą się z usuwania nieużywanych reguł — to robota dla tree-shakingu, nie minifikacji.</li>
</ul>
""",
    },
    "related": ["js-minifier", "html-encoder", "color-picker"],
}
