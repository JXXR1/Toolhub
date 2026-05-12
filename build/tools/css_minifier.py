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
        "ja": {"name": "CSS ミニファイア", "tagline": "CSS からコメント・空白・冗長な記述を除去。ビフォア／アフターのサイズと圧縮率を表示。", "description": "オンライン無料の CSS ミニファイア。コメント除去、空白の圧縮、末尾セミコロンとゼロ単位のトリミングを実施し、圧縮率を表示します。"},
        "nl": {"name": "CSS Minifier", "tagline": "Strip comments, whitespace en redundantie uit CSS. Zie size voor/na en het besparingspercentage.", "description": "Gratis online CSS minifier. Verwijdert comments, collapseert whitespace, trimt trailing semicolons en zero-units. Toont compressieratio."},
        "tr": {"name": "CSS Minifier", "tagline": "CSS'ten yorumları, boşlukları ve gereksizliği temizle. Öncesi/sonrası boyutunu ve tasarruf yüzdesini gör.", "description": "Ücretsiz online CSS minifier. Yorumları kaldırır, boşlukları daraltır, sondaki noktalı virgülleri ve sıfır birimlerini keser. Sıkıştırma oranını gösterir."},
        "id": {"name": "CSS Minifier", "tagline": "Strip komentar, whitespace, dan redundansi dari CSS. Lihat ukuran sebelum/sesudah dan persen penghematan.", "description": "CSS minifier gratis. Strip komentar, whitespace, dan stylesheet kosong dari CSS-mu. Lihat ukuran sebelum/sesudah dan persen byte yang dihemat — semuanya di browser-mu."},
        "vi": {"name": "CSS Minifier", "tagline": "Bỏ comment, whitespace và phần dư thừa khỏi CSS. Xem kích thước trước/sau và phần trăm tiết kiệm.", "description": "CSS minifier miễn phí trực tuyến. Bỏ comment và whitespace, hợp nhất các quy tắc và hiển thị tiết kiệm byte. Chạy hoàn toàn trong trình duyệt."},
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
        "ja": """
<h2>用途</h2>
<p>ソース上で読みやすい CSS（コメント、インデント、意味のある空白を伴うもの）は、ユーザーがダウンロードするファイルを肥大化させます。構造的なミニファイアは、ルールの意味を変えずに見た目用のバイト（コメント、空白の連続、冗長なゼロ、より短い等価な hex コード）をすべて取り除きます。本ツールはその処理をブラウザ内で実行し、ビフォア／アフターのサイズを表示して節約量を確認できます。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>HTML メールやブログテンプレートにインラインで CSS スニペットを単発で送りたいときに、ビルドチェーンなしでバイトを削減したい。</li>
  <li>本格的なオプティマイザを導入する価値があるか判断する前に、スタイルシートの「贅肉」がどの程度かを素早く確認したい。</li>
  <li>サードパーティのウィジェット用に、配布されている整形済み CSS を圧縮して組み込みたい。</li>
</ul>

<h3>処理内容</h3>
<ul>
  <li>ブロックコメント（<code>/* … */</code>）を削除します。<code>//</code> はそもそも素の CSS としては有効ではありません。</li>
  <li><code>{ } : ; ,</code> や結合子（<code>&gt; ~ +</code>）まわりの空白を圧縮します。</li>
  <li><code>}</code> の前の末尾セミコロンを削除します。</li>
  <li>先頭の 0 を削除（<code>0.5</code> → <code>.5</code>）し、ゼロからは単位を削除（<code>0px</code> → <code>0</code>）します。</li>
  <li>等価で短く書ける場合は hex 色を短縮（<code>#aabbcc</code> → <code>#abc</code>）します。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>これは構造的なミニファイで、フルオプティマイザではありません。</strong> 重複セレクタの統合、ルールの並び替え、shorthand への書き換えは行いません。それらは <code>cssnano</code> や <code>esbuild</code> をビルドパイプラインで使ってください。</li>
  <li><strong>ソースマップは生成しません。</strong> 本番でミニファイ後の CSS をデバッグする場合は別途配布してください。</li>
  <li><strong>ミニファイ済み CSS をコミットしないこと。</strong> ソースは整形済みでコミットし、ビルド／デプロイ時にミニファイします。両者を混ぜると差分レビューが地獄になります。</li>
  <li><strong>現代では転送時の圧縮が支配的です。</strong> ワイヤ上の Brotli/gzip がミニファイの大部分の効果を担います。最大の削減は未使用ルールの除去から得られ、これはミニファイではなく tree-shaking の仕事です。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>CSS die leesbaar is in de source — met comments, indentatie en betekenisvolle whitespace — bloated het bestand dat je gebruikers downloaden. Een structurele minifier strijkt alle cosmetische bytes (comments, runs van whitespace, redundante nullen, equivalente kortere hex-codes) eruit zonder de betekenis van de rules te veranderen. Deze tool draait die pass in je browser en toont de size voor/na zodat je de besparing kunt zien.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Eenmalig een CSS-snippet inline shippen in een HTML-email of blog-post template, waar je de bytes wil verkleinen maar geen build chain hebt.</li>
  <li>Snel checken hoeveel "vet" in een stylesheet zit voor je besluit of een echte optimizer de moeite waard is.</li>
  <li>Een vendor's pretty-printed CSS plakken om af te slanken voor inclusie in een third-party widget.</li>
</ul>

<h3>Wat het doet</h3>
<ul>
  <li>Strijkt block comments eruit (<code>/* … */</code>) — single-line <code>//</code> is sowieso geen geldige plain CSS.</li>
  <li>Collapseert whitespace rond <code>{ } : ; ,</code> en combinators (<code>&gt; ~ +</code>).</li>
  <li>Laat trailing semicolons voor <code>}</code> vallen.</li>
  <li>Trimt leading zeros (<code>0.5</code> → <code>.5</code>) en verwijdert units van nul (<code>0px</code> → <code>0</code>).</li>
  <li>Verkort hex-kleuren waar exact (<code>#aabbcc</code> → <code>#abc</code>).</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Dit is een structurele minify, geen volledige optimizer.</strong> Hij merget geen duplicate selectors, herordent geen rules en herschrijft geen shorthand. Daarvoor draai je <code>cssnano</code> of <code>esbuild</code> in je build pipeline.</li>
  <li><strong>Source maps worden niet gegenereerd.</strong> Als je geminifieerde CSS in productie debugt, ship ze apart.</li>
  <li><strong>Minify niet de CSS die je commit.</strong> Commit pretty source; minify bij build/deploy. De twee mengen maakt diff review ellendig.</li>
  <li><strong>Moderne compressie domineert.</strong> Brotli/gzip over de wire doet veel van wat minification doet. De grootste besparingen komen van ongebruikte rules verwijderen — werk voor tree-shaking, niet voor minification.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Kaynakta okunabilir olan CSS — yorumlar, indent ve anlamlı boşluklarla — kullanıcılarının indirdiği dosyayı şişirir. Yapısal bir minifier tüm kozmetik byte'ları (yorumlar, boşluk grupları, gereksiz sıfırlar, eşdeğer kısa hex kodları) kuralların anlamını değiştirmeden temizler. Bu araç bu pasajı tarayıcında çalıştırır ve öncesi/sonrası boyutunu gösterir, böylece tasarrufu görebilirsin.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Bir HTML e-postaya veya blog gönderisi şablonuna bir CSS snippet'i tek seferlik inline gönderme, byte'ları küçültmek istediğinde ama build chain yokken.</li>
  <li>Gerçek bir optimizer'ı kurmaya değip değmeyeceğine karar vermeden önce bir stylesheet'te ne kadar "yağ" olduğunu hızlıca kontrol etme.</li>
  <li>Üçüncü taraf widget'ında dahil etmek için ince hale getirmek üzere bir vendor'ın güzel basılı CSS'ini yapıştırma.</li>
</ul>

<h3>Ne yapar</h3>
<ul>
  <li>Blok yorumlarını temizler (<code>/* … */</code>) — tek satırlık <code>//</code> zaten geçerli sade CSS değildir.</li>
  <li><code>{ } : ; ,</code> ve birleştiriciler (<code>&gt; ~ +</code>) etrafındaki boşluğu daraltır.</li>
  <li><code>}</code> öncesi sondaki noktalı virgülleri düşürür.</li>
  <li>Önde gelen sıfırları (<code>0.5</code> → <code>.5</code>) keser ve sıfırdan birimleri kaldırır (<code>0px</code> → <code>0</code>).</li>
  <li>Hex renklerini kısaltır kesinse (<code>#aabbcc</code> → <code>#abc</code>).</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Bu yapısal bir minify, tam optimizer değil.</strong> Yinelenen selector'ları birleştirmez, kuralları yeniden sıralamaz veya kısaltmayı yeniden yazmaz. Onun için build pipeline'ında <code>cssnano</code> veya <code>esbuild</code> çalıştır.</li>
  <li><strong>Source map üretilmez.</strong> Production'da minified CSS'i debug ediyorsan, onları ayrıca gönder.</li>
  <li><strong>Commit ettiğin CSS'i minify etme.</strong> Güzel kaynak commit et; build/deploy'da minify et. İkisini karıştırmak diff incelemesini sefil yapar.</li>
  <li><strong>Modern sıkıştırma baskın.</strong> Wire üzerindeki Brotli/gzip minification'ın çoğunu yapar. En büyük tasarruflar kullanılmayan kuralları çıkarmaktan gelir — bir tree-shaking işidir, minification değil.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>CSS yang readable di source — dengan comment, indentasi, dan whitespace yang bermakna — membengkakkan file yang diunduh user kamu. Structural minifier menghilangkan semua byte kosmetik (comment, deretan whitespace, nol redundan, hex code yang setara tapi lebih pendek) tanpa mengubah arti rule-nya. Tool ini menjalankan pass tersebut di browser kamu dan menampilkan ukuran sebelum/sesudah supaya kamu bisa melihat penghematannya.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Mengirim snippet CSS inline secara one-off di email HTML atau template blog post, di mana kamu ingin byte-nya mengecil tapi tidak punya build chain.</li>
  <li>Cek cepat berapa banyak "lemak" di sebuah stylesheet sebelum memutuskan apakah optimizer sungguhan layak dipasang.</li>
  <li>Menempelkan CSS pretty-printed dari vendor untuk diramping demi dimasukkan ke third-party widget.</li>
</ul>

<h3>Apa yang dilakukan</h3>
<ul>
  <li>Menghapus block comment (<code>/* … */</code>) — single-line <code>//</code> toh bukan plain CSS yang valid.</li>
  <li>Mengciutkan whitespace di sekitar <code>{ } : ; ,</code> dan combinator (<code>&gt; ~ +</code>).</li>
  <li>Membuang trailing semicolon sebelum <code>}</code>.</li>
  <li>Memotong leading zero (<code>0.5</code> → <code>.5</code>) dan menghapus unit dari nol (<code>0px</code> → <code>0</code>).</li>
  <li>Memendekkan hex color jika persis sama (<code>#aabbcc</code> → <code>#abc</code>).</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Ini structural minify, bukan optimizer penuh.</strong> Tool ini tidak menggabungkan selector duplikat, mengubah urutan rule, atau menulis ulang shorthand. Untuk itu, jalankan <code>cssnano</code> atau <code>esbuild</code> di build pipeline kamu.</li>
  <li><strong>Source map tidak dihasilkan.</strong> Jika kamu mendebug CSS minified di production, kirim mereka secara terpisah.</li>
  <li><strong>Jangan minify CSS yang kamu commit.</strong> Commit source yang pretty; minify saat build/deploy. Mencampur keduanya membuat review diff jadi menderita.</li>
  <li><strong>Kompresi modern dominan.</strong> Brotli/gzip di wire melakukan sebagian besar pekerjaan minification. Penghematan terbesar datang dari menghapus rule yang tidak terpakai — itu pekerjaan tree-shaking, bukan minification.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>CSS sản xuất thường được minified — bỏ comment, whitespace và đôi khi quy tắc dư thừa để file nhỏ hơn và nhanh hơn để tải xuống. Tool này thực hiện minify nhanh, structural: bỏ comment, gộp khoảng trắng và drop dòng trống. Nó không trộn quy tắc hay tối ưu hóa selector — chỉ làm cho file nhỏ hơn mà không thay đổi cách trình duyệt diễn giải nó.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Chuẩn bị CSS hand-written để deploy mà không cần pipeline build.</li>
  <li>So sánh kích thước trước/sau để chứng minh cho tiết kiệm.</li>
  <li>Minify nhanh một snippet để inline vào <code>&lt;style&gt;</code> tag.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Minify ≠ tối ưu hóa.</strong> Bộ tối ưu thực thụ (cssnano, csso) sẽ gộp các quy tắc, drop selector chết và xếp lại giá trị shorthand. Tool này chỉ làm việc dễ nhất: whitespace và comment.</li>
  <li><strong>Comment có thể là cấp phép quan trọng.</strong> Đừng tự động bỏ tất cả comment khỏi CSS chứa header license — kiểm tra trước.</li>
  <li><strong>Một số whitespace là quan trọng.</strong> Trong selector phức tạp (như <code>div > p</code>), tool này giữ lại khoảng trắng có ý nghĩa và chỉ bỏ phần trang trí.</li>
</ul>
""",
    },
    "related": ["js-minifier", "html-encoder", "color-picker"],
    "howto": {"flow": "transform", "action": "minify",  "noun": "CSS"},
}
