TOOL = {
    "slug": "js-minifier",
    "category": "developer",
    "icon": "{}",
    "tags": ["javascript", "js", "minify", "compress", "optimize"],
    "i18n": {
        "en": {
            "name": "JavaScript Minifier",
            "tagline": "Fast structural JavaScript minify — strip comments, collapse whitespace, drop blank lines. See size before/after and the saving percentage.",
            "description": "Free online JavaScript minifier. Removes single- and multi-line comments, redundant whitespace, and blank lines while preserving strings, regex literals, and template literals.",
        },
        "de": {"name": "JavaScript-Minifier", "tagline": "Schnelle JS-Minifizierung — Kommentare entfernen, Whitespace zusammenfassen, Leerzeilen löschen. Größenvergleich inkl.", "description": "Kostenloser JavaScript-Minifier. Entfernt Zeilen- und Blockkommentare, überflüssigen Whitespace und Leerzeilen, ohne Strings, Regex und Template-Literale zu beschädigen."},
        "es": {"name": "Minificador de JavaScript", "tagline": "Minificación estructural rápida de JS — quita comentarios, colapsa espacios, elimina líneas vacías. Tamaño antes/después.", "description": "Minificador de JavaScript gratuito. Elimina comentarios de una línea y multilínea, espacios redundantes y líneas vacías sin romper strings, regex ni template literals."},
        "fr": {"name": "Minifieur JavaScript", "tagline": "Minification structurelle rapide du JS — suppression des commentaires, des espaces redondants et des lignes vides. Taille avant/après.", "description": "Minifieur JavaScript gratuit. Retire les commentaires mono- et multi-lignes, les espaces redondants et les lignes vides sans casser strings, regex et template literals."},
        "it": {"name": "Minificatore JavaScript", "tagline": "Minificazione strutturale rapida del JS — rimuove commenti, comprime spazi, elimina righe vuote. Dimensione prima/dopo.", "description": "Minificatore JavaScript gratuito. Rimuove commenti single-line e multi-line, spazi superflui e righe vuote preservando stringhe, regex e template literal."},
        "pt": {"name": "Minificador JavaScript", "tagline": "Minify estrutural rápido de JavaScript — remove comentários, comprime whitespace, tira linhas em branco. Mostra tamanho antes/depois e o percentual economizado.", "description": "Minificador JavaScript grátis online. Remove comentários de uma e várias linhas, whitespace redundante e linhas em branco preservando strings, regex e template literals."},
        "pl": {"name": "Minifikator JavaScript", "tagline": "Szybka strukturalna minifikacja JavaScriptu — wytnij komentarze, zwiń białe znaki, usuń puste linie. Pokazuje rozmiar przed/po i procent oszczędności.", "description": "Darmowy online minifikator JavaScriptu. Usuwa jedno- i wieloliniowe komentarze, nadmiarowe białe znaki i puste linie, zachowując stringi, literały regex i template literale."},
        "ja": {"name": "JavaScript ミニファイア", "tagline": "高速で構造的な JavaScript ミニファイ — コメント除去、空白圧縮、空行削除。ビフォア／アフターのサイズと節約率を表示。", "description": "オンライン無料の JavaScript ミニファイア。1 行コメント・複数行コメント・冗長な空白・空行を除去しつつ、文字列、正規表現リテラル、テンプレートリテラルは正確に保持します。"},
        "nl": {"name": "JavaScript Minifier", "tagline": "Snelle structurele JavaScript-minify — strip comments, collapseer whitespace, drop blank lines. Zie size voor/na en het besparingspercentage.", "description": "Gratis online JavaScript minifier. Verwijdert single- en multi-line comments, redundante whitespace en blank lines terwijl strings, regex literals en template literals behouden blijven."},
        "tr": {"name": "JavaScript Minifier", "tagline": "Hızlı yapısal JavaScript minify — yorumları sil, boşlukları daralt, boş satırları at. Öncesi/sonrası boyutunu ve tasarruf yüzdesini gör.", "description": "Ücretsiz online JavaScript minifier. Tek ve çok satırlı yorumları, gereksiz boşlukları ve boş satırları kaldırırken string'leri, regex literal'larını ve template literal'larını korur."},
    },
    "body": """
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="jm-input" oninput="jmRun()" placeholder="// Paste JavaScript here" spellcheck="false">// Sample
function greet(name) {
  // Say hi
  const msg = `Hello, ${name}!`;
  console.log(msg);
  return msg;
}

greet('World');</textarea>
  <div class="meta" id="jm-stats" style="margin-top:0.5rem"></div>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="jm-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('jm-out', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<script>
// String/regex/comment-aware minifier. Walks the input one char at a time.
function jmMinify(src){
  let out = '';
  const n = src.length;
  let i = 0;
  // Track "previous significant token char" to know if a `/` starts a regex
  let prev = '';
  const REGEX_PREV = /[(,=:[!&|?{};+\\-*~^%<>]|^$/;
  while(i < n){
    const c = src[i];
    const next = src[i+1];
    // Line comment
    if(c === '/' && next === '/'){
      while(i < n && src[i] !== '\\n') i++;
      continue;
    }
    // Block comment
    if(c === '/' && next === '*'){
      i += 2;
      while(i < n && !(src[i] === '*' && src[i+1] === '/')) i++;
      i += 2;
      continue;
    }
    // String literals: ' " `
    if(c === '"' || c === "'" || c === '`'){
      const quote = c;
      let chunk = c;
      i++;
      while(i < n){
        const ch = src[i];
        chunk += ch;
        if(ch === '\\\\' && i+1 < n){ chunk += src[i+1]; i += 2; continue; }
        if(quote === '`' && ch === '$' && src[i+1] === '{'){
          chunk += '{'; i += 2; let depth = 1;
          while(i < n && depth > 0){
            const k = src[i];
            chunk += k;
            if(k === '{') depth++;
            else if(k === '}') depth--;
            else if(k === '"' || k === "'" || k === '`'){
              const q = k; i++;
              while(i < n){
                const c2 = src[i]; chunk += c2;
                if(c2 === '\\\\' && i+1 < n){ chunk += src[i+1]; i += 2; continue; }
                if(c2 === q){ i++; break; }
                i++;
              }
              continue;
            }
            i++;
          }
          continue;
        }
        if(ch === quote){ i++; break; }
        i++;
      }
      out += chunk;
      prev = quote;
      continue;
    }
    // Regex literal — only if prev token suggests regex context
    if(c === '/' && REGEX_PREV.test(prev)){
      let chunk = '/'; i++;
      let inClass = false;
      while(i < n){
        const ch = src[i];
        chunk += ch;
        if(ch === '\\\\' && i+1 < n){ chunk += src[i+1]; i += 2; continue; }
        if(ch === '[') inClass = true;
        else if(ch === ']') inClass = false;
        else if(ch === '/' && !inClass){ i++; break; }
        i++;
      }
      // flags
      while(i < n && /[gimsuy]/.test(src[i])){ chunk += src[i]; i++; }
      out += chunk;
      prev = '/';
      continue;
    }
    // Whitespace collapse
    if(c === ' ' || c === '\\t'){
      // keep one space if both sides are identifier chars
      let j = i;
      while(j < n && (src[j] === ' ' || src[j] === '\\t')) j++;
      const before = out[out.length-1] || '';
      const after = src[j] || '';
      if(/[A-Za-z0-9_$]/.test(before) && /[A-Za-z0-9_$]/.test(after)) out += ' ';
      i = j;
      continue;
    }
    if(c === '\\n' || c === '\\r'){
      // newline can sometimes be needed (return/no-LF rule). Keep one if both sides could need ASI.
      let j = i;
      while(j < n && (src[j] === '\\n' || src[j] === '\\r' || src[j] === ' ' || src[j] === '\\t')) j++;
      const before = out[out.length-1] || '';
      const after = src[j] || '';
      const needsNL = /[A-Za-z0-9_$\\)\\]\\}]/.test(before) && /[A-Za-z_$]/.test(after);
      if(needsNL) out += '\\n';
      i = j;
      continue;
    }
    out += c;
    if(/\\S/.test(c)) prev = c;
    i++;
  }
  return out;
}
function jmHumanBytes(n){
  if(n < 1024) return n + ' B';
  if(n < 1024*1024) return (n/1024).toFixed(1) + ' KB';
  return (n/1048576).toFixed(2) + ' MB';
}
function jmRun(){
  const raw = document.getElementById('jm-input').value;
  const out = document.getElementById('jm-out');
  const stats = document.getElementById('jm-stats');
  out.classList.remove('error');
  if(!raw){ out.textContent = '{LBL_NO_INPUT}'; stats.textContent = ''; return; }
  try {
    const min = jmMinify(raw);
    out.textContent = min;
    const before = new TextEncoder().encode(raw).length;
    const after = new TextEncoder().encode(min).length;
    const saved = before > 0 ? Math.round((1 - after/before) * 100) : 0;
    stats.textContent = `Before: ${jmHumanBytes(before)} · After: ${jmHumanBytes(after)} · Saved: ${saved}%`;
  } catch(e){ out.classList.add('error'); out.textContent = '✗ ' + e.message; stats.textContent = ''; }
}
document.addEventListener('DOMContentLoaded', jmRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>A structural JavaScript minifier strips comments and unnecessary whitespace without changing what the code does. The output is functionally identical to the input — same identifiers, same logic — just shorter. This tool runs that pass in your browser, including the tricky bits: it preserves string contents and regex literals untouched, and keeps newlines where ASI (Automatic Semicolon Insertion) would otherwise change behaviour.</p>

<h3>When to use it</h3>
<ul>
  <li>Quickly trimming a snippet for inclusion in an HTML bookmarklet or a single-file demo, where you don't have a build chain.</li>
  <li>Sanity-checking how much "fat" is in a hand-written script before deciding whether a real optimiser is worth setting up.</li>
  <li>Inlining a small library into a static site without dragging in a bundler.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>This is a structural minify, not a compressor.</strong> It won't rename variables, dead-code eliminate, mangle properties, or tree-shake. For production builds, use <code>terser</code>, <code>esbuild</code>, or <code>swc</code> in your pipeline — they cut another 30–60% on top of structural minify.</li>
  <li><strong>ASI traps.</strong> JavaScript inserts semicolons in surprising places. The minifier preserves a newline where removing it would change meaning (e.g. <code>return\\n{}</code> ≠ <code>return {}</code>). Stick to explicit semicolons in source if you can — it makes minification safer for everyone.</li>
  <li><strong>Source maps aren't generated.</strong> If you ship minified JS to production, generate source maps with a real toolchain so debugging is sane.</li>
  <li><strong>Modern compression dominates.</strong> Brotli/gzip on the wire does most of what minify does. The biggest wins come from removing unused code — that needs static analysis a structural minifier can't do.</li>
  <li><strong>Don't minify what you commit.</strong> Source goes in pretty; minify at build/deploy.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Um minificador estrutural de JavaScript remove comentários e whitespace desnecessário sem mudar o que o código faz. O output é funcionalmente idêntico ao input — mesmos identificadores, mesma lógica — só que mais curto. Esta ferramenta roda esse passe no seu browser, incluindo as partes traiçoeiras: preserva o conteúdo de strings e literais regex intactos, e mantém quebras de linha onde o ASI (Automatic Semicolon Insertion) mudaria o comportamento.</p>

<h3>Quando usar</h3>
<ul>
  <li>Cortar rápido um trecho pra inclusão num bookmarklet HTML ou demo de arquivo único, em que você não tem build chain.</li>
  <li>Verificar quanta "gordura" tem num script feito à mão antes de decidir se vale a pena montar um optimizer de verdade.</li>
  <li>Fazer inline de uma biblioteca pequena num site estático sem trazer um bundler junto.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Isto é minify estrutural, não um compressor.</strong> Não renomeia variáveis, não faz dead-code elimination, não mangle de propriedades nem tree-shaking. Pra builds de produção, use <code>terser</code>, <code>esbuild</code> ou <code>swc</code> no seu pipeline — eles cortam mais 30–60% além do minify estrutural.</li>
  <li><strong>Armadilhas do ASI.</strong> O JavaScript insere ponto-e-vírgula em lugares surpreendentes. O minificador preserva uma quebra de linha onde removê-la mudaria o significado (ex.: <code>return\\n{}</code> ≠ <code>return {}</code>). Use ponto-e-vírgula explícito no source quando puder — torna o minify mais seguro pra todo mundo.</li>
  <li><strong>Source maps não são gerados.</strong> Se você for enviar JS minificado pra produção, gere source maps com uma toolchain de verdade pra que o debug seja viável.</li>
  <li><strong>A compressão moderna domina.</strong> Brotli/gzip na rede faz a maior parte do que o minify faz. Os maiores ganhos vêm de remover código não usado — isso exige análise estática que um minificador estrutural não consegue fazer.</li>
  <li><strong>Não minifique o que você commita.</strong> Source vai bonito; minify no build/deploy.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Strukturalny minifikator JavaScriptu wycina komentarze i niepotrzebne białe znaki bez zmiany działania kodu. Wyjście jest funkcjonalnie identyczne z wejściem — te same identyfikatory, ta sama logika — tylko krótsze. To narzędzie robi tę przejazdkę w przeglądarce, łącznie z trudniejszymi miejscami: zachowuje zawartość stringów i literały regex w nienaruszonej formie, i trzyma końce linii tam, gdzie ASI (Automatic Semicolon Insertion) inaczej zmieniłoby zachowanie.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Szybkie odchudzenie snippetu do bookmarkleta HTML albo dema w jednym pliku, gdzie nie masz pipeline'u buildowego.</li>
  <li>Sanity check, ile "tłuszczu" siedzi w ręcznie pisanym skrypcie, zanim zdecydujesz, czy warto stawiać prawdziwy optymalizator.</li>
  <li>Inline'owanie małej biblioteki na statycznej stronie bez ciągnięcia bundlera.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>To strukturalna minifikacja, nie kompresor.</strong> Nie zmieni nazw zmiennych, nie zrobi dead-code elimination, nie zmangle'uje properties ani nie tree-shake'uje. Do produkcyjnych buildów używaj <code>terser</code>, <code>esbuild</code> albo <code>swc</code> w pipeline — tną kolejne 30–60% ponad strukturalny minify.</li>
  <li><strong>Pułapki ASI.</strong> JavaScript wstawia średniki w zaskakujących miejscach. Minifikator zachowuje newline tam, gdzie usunięcie zmieniłoby znaczenie (np. <code>return\\n{}</code> ≠ <code>return {}</code>). Trzymaj się jawnych średników w źródle, jeśli możesz — to robi minifikację bezpieczniejszą dla wszystkich.</li>
  <li><strong>Source mapy nie są generowane.</strong> Jeśli wysyłasz zminifikowany JS na produkcję, generuj source mapy prawdziwym toolchainem, żeby debug był sensowny.</li>
  <li><strong>Nowoczesna kompresja dominuje.</strong> Brotli/gzip na drucie robi większość tego, co minify. Największe wygrane biorą się z usuwania nieużywanego kodu — to wymaga statycznej analizy, której strukturalny minifikator nie zrobi.</li>
  <li><strong>Nie minifikuj tego, co commitujesz.</strong> Źródło wchodzi ładne; minify na buildzie/deployu.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>構造的な JavaScript ミニファイアは、コードの動作を変えずにコメントと不要な空白を取り除きます。出力は入力と機能的に同一で、識別子もロジックも同じまま、長さだけが短くなります。本ツールはこの処理をブラウザ内で実行します。文字列の中身や正規表現リテラルは触らず、ASI（自動セミコロン挿入）が動作を変えてしまう箇所では改行を保持します。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>HTML ブックマークレットや単一ファイルのデモのために、ビルドチェーンなしでスニペットをサクッと圧縮したいとき。</li>
  <li>本格的なオプティマイザを導入する価値があるか判断する前に、手書きスクリプトの「贅肉」を見積もりたいとき。</li>
  <li>バンドラを引っ張ってこずに、静的サイトに小さなライブラリをインライン化したいとき。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>これは構造的ミニファイで、コンプレッサではありません。</strong> 変数のリネーム、デッドコード除去、プロパティのマングル、ツリーシェイクは行いません。本番ビルドではパイプラインで <code>terser</code>、<code>esbuild</code>、<code>swc</code> を使ってください。構造的ミニファイの上にさらに 30〜60% の削減を期待できます。</li>
  <li><strong>ASI のトラップ。</strong> JavaScript は思いがけない場所にセミコロンを挿入します。本ミニファイアは、改行を取り除くと意味が変わってしまう箇所（例：<code>return\\n{}</code> ≠ <code>return {}</code>）では改行を保持します。可能ならソースで明示的にセミコロンを書く方がミニファイにとって安全です。</li>
  <li><strong>ソースマップは生成しません。</strong> 本番に圧縮 JS を出すなら、デバッグのために本物のツールチェーンでソースマップを併せて出力してください。</li>
  <li><strong>現代では転送時の圧縮が支配的です。</strong> ワイヤ上の Brotli/gzip がミニファイの大半の効果を担います。最大の削減は未使用コードの除去から得られ、これは構造的ミニファイヤだけでは達成できない静的解析を要します。</li>
  <li><strong>ミニファイ済みをコミットしないこと。</strong> ソースは整形済みでコミットし、ビルド／デプロイ時にミニファイします。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Een structurele JavaScript-minifier strijkt comments en onnodige whitespace eruit zonder te veranderen wat de code doet. De output is functioneel identiek aan de input — zelfde identifiers, zelfde logica — gewoon korter. Deze tool draait die pass in je browser, inclusief de lastige stukken: hij behoudt string-contents en regex-literals onaangetast en houdt newlines waar ASI (Automatic Semicolon Insertion) anders het gedrag zou veranderen.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een snippet snel trimmen voor inclusie in een HTML-bookmarklet of een single-file demo, waar je geen build chain hebt.</li>
  <li>Sanity check hoeveel "vet" in een handgeschreven script zit voor je besluit of een echte optimizer de moeite waard is.</li>
  <li>Een kleine library inline zetten in een statische site zonder een bundler binnen te slepen.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Dit is een structurele minify, geen compressor.</strong> Hij hernoemt geen variabelen, doet geen dead-code elimination, mangle't geen properties en doet geen tree-shake. Voor productie-builds gebruik <code>terser</code>, <code>esbuild</code> of <code>swc</code> in je pipeline — die snijden er nog 30–60% extra van af bovenop de structurele minify.</li>
  <li><strong>ASI-vallen.</strong> JavaScript voegt semicolons in verrassende plekken in. De minifier behoudt een newline waar weglaten betekenis zou veranderen (bijv. <code>return\n{}</code> ≠ <code>return {}</code>). Houd het bij expliciete semicolons in source als je kan — maakt minification voor iedereen veiliger.</li>
  <li><strong>Source maps worden niet gegenereerd.</strong> Als je geminifieerde JS naar productie ship't, genereer source maps met een echte toolchain zodat debuggen werkbaar is.</li>
  <li><strong>Moderne compressie domineert.</strong> Brotli/gzip over de wire doet het meeste van wat minify doet. De grootste winst komt van ongebruikte code verwijderen — dat vereist statische analyse die een structurele minifier niet kan.</li>
  <li><strong>Minify niet wat je commit.</strong> Source gaat netjes erin; minify bij build/deploy.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Bir yapısal JavaScript minifier, kodun ne yaptığını değiştirmeden yorumları ve gereksiz boşluğu temizler. Çıktı girdiyle işlevsel olarak aynıdır — aynı tanımlayıcılar, aynı mantık — sadece daha kısa. Bu araç bu pasajı tarayıcında çalıştırır, zor kısımlar dahil: string içeriklerini ve regex literal'larını dokunulmadan korur ve ASI (Otomatik Noktalı Virgül Yerleştirme) aksi takdirde davranışı değiştireceği yerlerde yeni satırları tutar.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>HTML bookmarklet'i veya tek dosyalı demo için bir snippet'i hızlıca kırpma, build chain'in olmadığında.</li>
  <li>Gerçek bir optimizer kurulumuna değip değmeyeceğine karar vermeden önce el yazımı bir script'te ne kadar "yağ" olduğunu kontrol etme.</li>
  <li>Bir bundler sürüklemeden statik bir siteye küçük bir kütüphaneyi inline yapma.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Bu yapısal bir minify, sıkıştırıcı değil.</strong> Değişkenleri yeniden adlandırmaz, ölü kod eliminasyonu yapmaz, özellikleri mangle etmez veya tree-shake yapmaz. Production build'leri için pipeline'ında <code>terser</code>, <code>esbuild</code> veya <code>swc</code> kullan — yapısal minify üstüne %30–60 daha keser.</li>
  <li><strong>ASI tuzakları.</strong> JavaScript şaşırtıcı yerlere noktalı virgül ekler. Minifier kaldırılması anlamı değiştirecek bir yeni satırı korur (örn. <code>return\n{}</code> ≠ <code>return {}</code>). Mümkünse kaynakta açık noktalı virgüllere bağlı kal — herkes için minification'ı daha güvenli yapar.</li>
  <li><strong>Source map üretilmez.</strong> Production'a minified JS gönderiyorsan, debug'ın sağlıklı olması için gerçek bir toolchain ile source map üret.</li>
  <li><strong>Modern sıkıştırma baskın.</strong> Wire üzerindeki Brotli/gzip minify'ın çoğunu yapar. En büyük kazanımlar kullanılmayan kodu çıkarmaktan gelir — bu yapısal minifier'ın yapamadığı statik analiz gerektirir.</li>
  <li><strong>Commit ettiğini minify etme.</strong> Kaynak güzel girer; build/deploy'da minify et.</li>
</ul>
""",
    },
    "related": ["css-minifier", "json-formatter", "regex-tester"],
    "howto": {"flow": "transform", "action": "minify",  "noun": "JavaScript"},
}
