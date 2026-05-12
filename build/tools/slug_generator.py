TOOL = {
    "slug": "slug-generator",
    "category": "text",
    "icon": "/-",
    "tags": ["slug", "url", "seo", "kebab", "permalink", "transliterate"],
    "i18n": {
        "en": {
            "name": "Slug Generator",
            "tagline": "Turn any title into a clean URL slug — transliterates accents, strips punctuation, joins with hyphens.",
            "description": "Free online URL slug generator. Lowercases, transliterates accented characters (à → a, ñ → n), strips punctuation, and joins words with a chosen separator. Stop-word removal optional.",
        },
        "de": {"name": "Slug-Generator", "tagline": "Wandle jeden Titel in einen sauberen URL-Slug um — transliteriert Akzente, entfernt Satzzeichen, verbindet mit Bindestrichen.", "description": "Kostenloser URL-Slug-Generator. Kleinbuchstaben, Transliteration von Akzentzeichen (à → a, ñ → n), Satzzeichen entfernen, Wörter mit Trennzeichen verbinden."},
        "es": {"name": "Generador de Slug", "tagline": "Convierte cualquier título en un slug URL limpio — translitera acentos, elimina puntuación, une con guiones.", "description": "Generador de slugs URL gratuito. Minúsculas, transliteración de acentos (à → a, ñ → n), eliminación de puntuación y unión de palabras con separador."},
        "fr": {"name": "Générateur de Slug", "tagline": "Transformez tout titre en slug URL propre — translittère les accents, supprime la ponctuation, joint avec tirets.", "description": "Générateur de slug URL gratuit. Minuscules, translittération des accents (à → a, ñ → n), suppression de la ponctuation et jonction des mots."},
        "it": {"name": "Generatore di Slug", "tagline": "Trasforma qualsiasi titolo in uno slug URL pulito — translittera accenti, rimuove punteggiatura, unisce con trattini.", "description": "Generatore di slug URL gratuito. Minuscole, traslitterazione di accenti (à → a, ñ → n), rimozione punteggiatura e unione parole con separatore."},
        "pt": {"name": "Gerador de Slug", "tagline": "Transforme qualquer título em um slug de URL limpo — translitera acentos, remove pontuação, une com hifens.", "description": "Gerador de slug de URL gratuito. Coloca em minúsculas, translitera caracteres acentuados (à → a, ñ → n), remove pontuação e une as palavras com o separador escolhido. Remoção opcional de stop words."},
        "pl": {"name": "Generator Slugów", "tagline": "Zamień dowolny tytuł w czysty slug URL — translikuje znaki diakrytyczne, wycina interpunkcję, łączy myślnikami.", "description": "Darmowy online generator slugów URL. Zamienia na małe litery, translikuje znaki diakrytyczne (à → a, ń → n, ż → z), wycina interpunkcję i łączy słowa wybranym separatorem. Opcjonalne usuwanie stop words."},
        "ja": {"name": "スラグ生成ツール", "tagline": "任意のタイトルからクリーンな URL スラグを生成。アクセントを翻字し、句読点を取り除き、ハイフンで連結。", "description": "オンライン無料の URL スラグ生成ツール。小文字化、アクセント文字の翻字（à → a、ñ → n）、句読点除去、選択した区切り文字での連結を実行します。ストップワードの除去もオプションで利用可能です。"},
        "nl": {"name": "Slug Generator", "tagline": "Maak van elke titel een schone URL-slug — translitereert accenten, strijkt punctuation, voegt met hyphens samen.", "description": "Gratis online URL slug generator. Maakt lowercase, translitereert accenten (à → a, ñ → n), strijkt punctuation en voegt woorden samen met een gekozen separator. Stop-word removal optioneel."},
        "tr": {"name": "Slug Üretici", "tagline": "Herhangi bir başlığı temiz URL slug'a dönüştür — aksanları transliter eder, noktalama temizler, tirelerle birleştirir.", "description": "Ücretsiz online URL slug üretici. Küçük harfe çevirir, aksanlı karakterleri transliter eder (à → a, ñ → n), noktalama işaretlerini temizler ve kelimeleri seçilen ayraçla birleştirir. Stop-word kaldırma opsiyoneldir."},
        "id": {"name": "Slug Generator", "tagline": "Ubah judul apa pun menjadi URL slug bersih — transliterate aksen, strip tanda baca, satukan dengan tanda hubung.", "description": "Slug generator gratis. Ubah judul apa pun menjadi slug URL ramah-SEO: lowercase, transliterate aksen (café → cafe), strip tanda baca, dan gabungkan kata dengan tanda hubung. Sempurna untuk permalink dan path konten."},
        "vi": {"name": "Tạo Slug", "tagline": "Biến bất kỳ tiêu đề nào thành URL slug sạch — chuyển tự chữ có dấu, bỏ dấu câu, nối bằng dấu gạch ngang.", "description": "Trình tạo slug miễn phí trực tuyến. Biến tiêu đề thành URL slug thân thiện với SEO — chuyển tự chữ có dấu sang ASCII, bỏ dấu câu, viết thường tất cả và nối các từ bằng dấu gạch ngang."},
    },
    "body": """
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="sg-input" oninput="sgRun()" placeholder="The Quick Brown Fox: A Café Story (1956)" spellcheck="false">The Quick Brown Fox: A Café Story (1956)</textarea>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Separator</label>
      <select id="sg-sep" onchange="sgRun()">
        <option value="-">- (hyphen, default)</option>
        <option value="_">_ (underscore)</option>
        <option value=".">. (dot)</option>
        <option value="">none</option>
      </select>
    </div>
    <div>
      <label>Case</label>
      <select id="sg-case" onchange="sgRun()">
        <option value="lower">lowercase</option>
        <option value="upper">UPPERCASE</option>
        <option value="preserve">preserve</option>
      </select>
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.5rem">
    <div>
      <label><input type="checkbox" id="sg-stop" onchange="sgRun()"> Strip English stop words</label>
    </div>
    <div>
      <label>Max length <input type="number" id="sg-max" value="80" min="1" max="500" oninput="sgRun()" style="width:80px;display:inline-block"></label>
    </div>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="sg-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('sg-out', this)">{LBL_COPY}</button>
  </div>
  <div id="sg-meta" class="meta" style="margin-top:0.5rem"></div>
</div>
""",
    "script": """
<script>
const SG_STOP = new Set(['a','an','and','the','of','to','in','on','at','for','by','with','from','is','are','was','were','be','been','as','it','this','that','these','those']);
function sgTransliterate(s){
  // NFD normalize then strip combining diacritics
  s = s.normalize('NFD').replace(/[\\u0300-\\u036f]/g, '');
  // common European ligatures + special letters
  const map = {
    'ß':'ss','æ':'ae','Æ':'AE','œ':'oe','Œ':'OE',
    'ø':'o','Ø':'O','å':'a','Å':'A','ł':'l','Ł':'L',
    'ð':'d','Ð':'D','þ':'th','Þ':'Th',
    '€':'eur','£':'gbp','$':'usd','¥':'jpy','%':'pct','&':'and','@':'at','+':'plus','=':'eq'
  };
  return s.replace(/[ßæÆœŒøØåÅłŁðÐþÞ€£$¥%&@+=]/g, c => map[c] || c);
}
function sgRun(){
  const raw = document.getElementById('sg-input').value;
  const sep = document.getElementById('sg-sep').value;
  const cas = document.getElementById('sg-case').value;
  const strip = document.getElementById('sg-stop').checked;
  const maxLen = Math.max(1, parseInt(document.getElementById('sg-max').value) || 80);
  const out = document.getElementById('sg-out');
  const meta = document.getElementById('sg-meta');
  if(!raw.trim()){ out.textContent = '{LBL_NO_INPUT}'; meta.textContent=''; return; }
  let s = sgTransliterate(raw);
  // collapse anything not letter/digit to a space
  s = s.replace(/[^A-Za-z0-9]+/g, ' ').trim();
  let words = s.split(/\\s+/);
  if(strip) words = words.filter(w => !SG_STOP.has(w.toLowerCase()));
  if(words.length === 0) words = [s.replace(/\\s+/g,'')];
  if(cas === 'lower') words = words.map(w => w.toLowerCase());
  else if(cas === 'upper') words = words.map(w => w.toUpperCase());
  let slug = words.join(sep);
  if(slug.length > maxLen){
    slug = slug.slice(0, maxLen);
    if(sep) slug = slug.replace(new RegExp('\\\\' + sep + '+$'), '');
  }
  out.textContent = slug || '—';
  meta.textContent = `${slug.length} characters · ${words.length} words${strip?' (after stop-word removal)':''}`;
}
document.addEventListener('DOMContentLoaded', sgRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>A URL slug is the human-readable last segment of a URL — <code>/blog/the-quick-brown-fox</code> rather than <code>/blog/post-4827</code>. Good slugs are lowercase, hyphenated, ASCII-only, and short enough to read at a glance, but generating them from real titles full of accents, punctuation, and emoji is fiddly to get right. This tool transliterates accents, strips junk, joins with your chosen separator, and truncates at a clean boundary so the output is safe to drop straight into a route or filename.</p>

<h3>When to use it</h3>
<ul>
  <li>Generating <code>/blog/&lt;slug&gt;</code> URLs from article titles — especially when titles contain accented characters (à, ñ, ø) or punctuation (colons, parentheses, em dashes).</li>
  <li>Producing safe filenames from user-supplied names — uploads, exports, generated reports.</li>
  <li>Building stable identifiers for tags, categories, or anchors (<code>#getting-started</code>) from human labels.</li>
  <li>Bulk-converting a list of headings to kebab-case for a static-site build step.</li>
</ul>

<h3>How the conversion works</h3>
<ol>
  <li>NFD-normalizes Unicode and strips combining diacritics (<code>café → cafe</code>).</li>
  <li>Maps common European ligatures and special letters: <code>ß → ss</code>, <code>æ → ae</code>, <code>ø → o</code>, <code>Ł → L</code>, plus a few currency/math symbols (<code>€ → eur</code>, <code>& → and</code>).</li>
  <li>Replaces every non-alphanumeric run with a single space.</li>
  <li>Optionally drops common English stop words (<em>a, an, and, the, of, to, …</em>).</li>
  <li>Lowercases (or preserves case), joins with your separator, and truncates at the limit without leaving a dangling separator.</li>
</ol>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Non-Latin scripts get dropped.</strong> Diacritic stripping handles à/ñ/ø, but it can't romanize Chinese, Japanese, Cyrillic, Arabic, or Hebrew character-by-character — those need language-specific tables (Hanyu Pinyin, ICU transliteration) which are deliberately out of scope here. Such characters disappear after the strip step.</li>
  <li><strong>Stop-word removal is English-only.</strong> "El gato negro" doesn't lose <em>el</em>; "Le chat noir" doesn't lose <em>le</em>. Leave the toggle off for non-English titles.</li>
  <li><strong>Truncation can change meaning.</strong> "introduction-to-rust-programming" cut to 20 chars becomes "introduction-to-rust" — fine; cut to 16 becomes "introduction-to" — clearly worse. Set the limit by hand for content where the tail matters.</li>
  <li><strong>Slugs aren't unique.</strong> Two different titles can collapse to the same slug ("Café" and "Cafe" both → <code>cafe</code>). If you're using slugs as URL keys, append a short ID or a suffix on collision.</li>
  <li><strong>Don't change shipped slugs.</strong> Once a URL is live and indexed, regenerating its slug breaks links and SEO. If a title changes, keep the old slug or set up a 301 redirect.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Um slug de URL é o último segmento legível por humanos da URL — <code>/blog/the-quick-brown-fox</code> em vez de <code>/blog/post-4827</code>. Bons slugs são em minúsculas, separados por hifens, só ASCII e curtos o bastante para ler de relance, mas gerá-los a partir de títulos reais cheios de acentos, pontuação e emoji é chato de acertar. Esta ferramenta translitera acentos, remove lixo, une com o separador escolhido e trunca em um limite limpo, então a saída é segura para colar direto numa rota ou nome de arquivo.</p>

<h3>Quando usar</h3>
<ul>
  <li>Gerar URLs <code>/blog/&lt;slug&gt;</code> a partir de títulos de artigos — especialmente quando os títulos têm caracteres acentuados (à, ñ, ø) ou pontuação (dois-pontos, parênteses, travessões).</li>
  <li>Produzir nomes de arquivo seguros a partir de nomes fornecidos pelo usuário — uploads, exports, relatórios gerados.</li>
  <li>Criar identificadores estáveis para tags, categorias ou âncoras (<code>#getting-started</code>) a partir de rótulos humanos.</li>
  <li>Converter em massa uma lista de títulos para kebab-case num build step de site estático.</li>
</ul>

<h3>Como funciona a conversão</h3>
<ol>
  <li>Normaliza Unicode para NFD e remove diacríticos combinantes (<code>café → cafe</code>).</li>
  <li>Mapeia ligaturas europeias e letras especiais comuns: <code>ß → ss</code>, <code>æ → ae</code>, <code>ø → o</code>, <code>Ł → L</code>, mais alguns símbolos de moeda/matemática (<code>€ → eur</code>, <code>& → and</code>).</li>
  <li>Substitui qualquer sequência não-alfanumérica por um único espaço.</li>
  <li>Opcionalmente remove stop words comuns do inglês (<em>a, an, and, the, of, to, …</em>).</li>
  <li>Coloca em minúsculas (ou preserva o case), une com seu separador e trunca no limite sem deixar separador solto.</li>
</ol>

<h3>Pegadinhas comuns</h3>
<ul>
  <li><strong>Scripts não-latinos somem.</strong> A remoção de diacríticos lida com à/ñ/ø, mas não consegue romanizar chinês, japonês, cirílico, árabe ou hebraico caractere a caractere — esses precisam de tabelas específicas por idioma (Hanyu Pinyin, transliteração ICU) que estão deliberadamente fora do escopo aqui. Esses caracteres desaparecem após a etapa de remoção.</li>
  <li><strong>Remoção de stop words é só em inglês.</strong> "El gato negro" não perde <em>el</em>; "Le chat noir" não perde <em>le</em>. Deixe a opção desligada para títulos não-ingleses.</li>
  <li><strong>Truncamento pode mudar o sentido.</strong> "introduction-to-rust-programming" cortado em 20 caracteres vira "introduction-to-rust" — ok; cortado em 16 vira "introduction-to" — claramente pior. Defina o limite à mão para conteúdo onde a parte final importa.</li>
  <li><strong>Slugs não são únicos.</strong> Dois títulos diferentes podem virar o mesmo slug ("Café" e "Cafe" ambos → <code>cafe</code>). Se você usa slugs como chave de URL, anexe um ID curto ou um sufixo em caso de colisão.</li>
  <li><strong>Não mude slugs que já estão no ar.</strong> Uma vez que a URL está publicada e indexada, regerar o slug quebra links e SEO. Se o título muda, mantenha o slug antigo ou configure um redirect 301.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>URL slug to czytelny dla człowieka ostatni segment URL-a — <code>/blog/the-quick-brown-fox</code> zamiast <code>/blog/post-4827</code>. Dobre slugi są małymi literami, łączone myślnikami, tylko ASCII i wystarczająco krótkie, by przeczytać na pierwszy rzut oka, ale generowanie ich z prawdziwych tytułów pełnych diakrytyków, interpunkcji i emoji jest upierdliwe. To narzędzie translikuje diakrytyki, wycina śmieci, łączy wybranym separatorem i ucina na czystej granicy, więc wyjście jest bezpieczne, by wkleić wprost do route'a albo nazwy pliku.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Generowanie URL-i <code>/blog/&lt;slug&gt;</code> z tytułów artykułów — szczególnie gdy tytuły zawierają znaki diakrytyczne (à, ń, ø) albo interpunkcję (dwukropki, nawiasy, pauzy).</li>
  <li>Tworzenie bezpiecznych nazw plików z nazw podanych przez użytkownika — uploady, eksporty, generowane raporty.</li>
  <li>Budowa stabilnych identyfikatorów dla tagów, kategorii albo anchorów (<code>#getting-started</code>) z czytelnych etykiet.</li>
  <li>Hurtowa konwersja listy nagłówków na kebab-case w buildzie statycznej strony.</li>
</ul>

<h3>Jak działa konwersja</h3>
<ol>
  <li>NFD-normalizuje Unicode i wycina łączące diakrytyki (<code>café → cafe</code>, <code>żółć → zolc</code>).</li>
  <li>Mapuje typowe europejskie ligatury i znaki specjalne: <code>ß → ss</code>, <code>æ → ae</code>, <code>ø → o</code>, <code>Ł → L</code>, plus kilka symboli walutowych/matematycznych (<code>€ → eur</code>, <code>& → and</code>).</li>
  <li>Zamienia każdy ciąg nie-alfanumeryczny na pojedynczą spację.</li>
  <li>Opcjonalnie wycina typowe angielskie stop words (<em>a, an, and, the, of, to, …</em>).</li>
  <li>Zamienia na małe litery (albo zachowuje wielkość), łączy twoim separatorem i ucina na limicie bez zostawiania wiszącego separatora.</li>
</ol>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Skrypty nielatyńskie wypadają.</strong> Wycinanie diakrytyków radzi sobie z à/ń/ø, ale nie zromanizuje chińskiego, japońskiego, cyrylicy, arabskiego ani hebrajskiego znak po znaku — te wymagają tabel zależnych od języka (Hanyu Pinyin, ICU transliteration), które są celowo poza zakresem. Te znaki znikają po kroku wycinania.</li>
  <li><strong>Usuwanie stop words działa tylko po angielsku.</strong> "El gato negro" nie traci <em>el</em>; "Le chat noir" nie traci <em>le</em>. Wyłącz toggle dla tytułów nieangielskich.</li>
  <li><strong>Ucinanie może zmienić znaczenie.</strong> "introduction-to-rust-programming" obcięte do 20 znaków staje się "introduction-to-rust" — OK; obcięte do 16 to "introduction-to" — wyraźnie gorzej. Ustaw limit ręcznie dla treści, gdzie ogon ma znaczenie.</li>
  <li><strong>Slugi nie są unikalne.</strong> Dwa różne tytuły mogą zwinąć się do tego samego slugu ("Café" i "Cafe" oba → <code>cafe</code>). Jeśli używasz slugów jako kluczy URL, dokleej krótkie ID albo suffix przy kolizji.</li>
  <li><strong>Nie zmieniaj slugów już opublikowanych.</strong> Gdy URL jest live i zindeksowany, regenerowanie slugu psuje linki i SEO. Jeśli tytuł się zmienia, zachowaj stary slug albo ustaw redirect 301.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>URL スラグは、<code>/blog/post-4827</code> ではなく <code>/blog/the-quick-brown-fox</code> のような、人が読める URL の最後のセグメントです。良いスラグは小文字、ハイフンつなぎ、ASCII のみ、ぱっと見て分かる短さですが、アクセント、句読点、絵文字を含む実際のタイトルから作るのは結構面倒です。本ツールはアクセントを翻字し、不要な記号を取り除き、選んだ区切り文字でつなぎ、上限文字数で末尾区切りが残らないように切り詰めるため、出力をそのままルートやファイル名に使えます。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>記事タイトルから <code>/blog/&lt;slug&gt;</code> URL を生成するとき。特にアクセント（à、ñ、ø）や句読点（コロン、括弧、ダッシュ）を含む場合。</li>
  <li>ユーザー入力名から安全なファイル名（アップロード、エクスポート、生成レポート）を作るとき。</li>
  <li>人間が読めるラベルから、タグ／カテゴリ／アンカー（<code>#getting-started</code>）の安定した識別子を作るとき。</li>
  <li>静的サイトのビルドステップで、見出しのリストを kebab-case に一括変換するとき。</li>
</ul>

<h3>変換の流れ</h3>
<ol>
  <li>NFD で正規化し、結合用ダイアクリティカル記号を除去（<code>café → cafe</code>）。</li>
  <li>典型的なヨーロッパのリガチャや特殊文字をマッピング：<code>ß → ss</code>、<code>æ → ae</code>、<code>ø → o</code>、<code>Ł → L</code>、加えて通貨／数学記号の一部（<code>€ → eur</code>、<code>& → and</code>）。</li>
  <li>非英数字の連続を 1 個のスペースに置換。</li>
  <li>オプションで一般的な英語のストップワード（<em>a, an, and, the, of, to, …</em>）を除去。</li>
  <li>小文字化（または大文字保持）し、選んだ区切り文字で連結し、上限で切り詰めます。末尾に区切り文字は残しません。</li>
</ol>

<h3>よくある注意点</h3>
<ul>
  <li><strong>非ラテン文字は落ちます。</strong> ダイアクリティカル除去は à/ñ/ø は扱えますが、中国語・日本語・キリル・アラビア・ヘブライなどを 1 文字ずつローマ字化することはできません。これらは Hanyu Pinyin や ICU 翻字のような言語別テーブルが必要で、本ツールの対象外です。除去ステップで消えます。</li>
  <li><strong>ストップワード除去は英語のみです。</strong> "El gato negro" の <em>el</em>、"Le chat noir" の <em>le</em> は落ちません。英語以外のタイトルではトグルをオフにしてください。</li>
  <li><strong>切り詰めで意味が変わることがあります。</strong> "introduction-to-rust-programming" を 20 文字で切ると "introduction-to-rust"（OK）。16 文字だと "introduction-to"（明らかに悪い）。末尾の語が重要な場合は手で長さを設定してください。</li>
  <li><strong>スラグは一意ではありません。</strong> 「Café」と「Cafe」はどちらも <code>cafe</code> になります。URL キーとして使うなら、衝突時には短い ID やサフィックスを付けてください。</li>
  <li><strong>公開済みのスラグは変えないこと。</strong> URL がインデックスされた後にスラグを再生成するとリンクと SEO が壊れます。タイトル変更時は旧スラグを残すか、301 リダイレクトを設定してください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Een URL-slug is het menselijk leesbare laatste segment van een URL — <code>/blog/the-quick-brown-fox</code> in plaats van <code>/blog/post-4827</code>. Goede slugs zijn lowercase, ge-hyphend, alleen ASCII en kort genoeg om in één oogopslag te lezen, maar ze genereren uit echte titels vol accenten, punctuation en emoji is gepriegel om goed te krijgen. Deze tool translitereert accenten, strijkt rotzooi, voegt samen met je gekozen separator en kapt op een schone grens af zodat de output veilig direct in een route of bestandsnaam te droppen is.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li><code>/blog/&lt;slug&gt;</code>-URLs genereren uit artikeltitels — vooral als titels accenten (à, ñ, ø) of punctuation (colons, parentheses, em-dashes) bevatten.</li>
  <li>Veilige filenames produceren uit user-supplied names — uploads, exports, generated reports.</li>
  <li>Stabiele identifiers bouwen voor tags, categorieën of anchors (<code>#getting-started</code>) uit menselijke labels.</li>
  <li>In bulk een lijst koppen converteren naar kebab-case voor een static-site build step.</li>
</ul>

<h3>Hoe de conversie werkt</h3>
<ol>
  <li>NFD-normaliseert Unicode en strijkt combining diacritics (<code>café → cafe</code>).</li>
  <li>Mapt gebruikelijke Europese ligatures en speciale letters: <code>ß → ss</code>, <code>æ → ae</code>, <code>ø → o</code>, <code>Ł → L</code>, plus een paar currency/math-symbolen (<code>€ → eur</code>, <code>& → and</code>).</li>
  <li>Vervangt elke non-alphanumeric run met een enkele spatie.</li>
  <li>Laat optioneel veelvoorkomende Engelse stop words vallen (<em>a, an, and, the, of, to, …</em>).</li>
  <li>Maakt lowercase (of behoudt case), voegt samen met je separator en kapt af op de limit zonder een loszittende separator achter te laten.</li>
</ol>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Non-Latin scripts verdwijnen.</strong> Diacritic-strippen handelt à/ñ/ø af, maar het kan Chinees, Japans, Cyrillisch, Arabisch of Hebreeuws niet karakter-voor-karakter romaniseren — die hebben taalspecifieke tabellen nodig (Hanyu Pinyin, ICU transliteration) die hier bewust buiten scope vallen. Zulke karakters verdwijnen na de strip step.</li>
  <li><strong>Stop-word removal is Engels-only.</strong> "El gato negro" verliest geen <em>el</em>; "Le chat noir" verliest geen <em>le</em>. Laat de toggle uit voor niet-Engelse titels.</li>
  <li><strong>Truncation kan betekenis veranderen.</strong> "introduction-to-rust-programming" gekapt op 20 tekens wordt "introduction-to-rust" — prima; gekapt op 16 wordt "introduction-to" — duidelijk slechter. Stel de limit met de hand in voor content waar de staart ertoe doet.</li>
  <li><strong>Slugs zijn niet uniek.</strong> Twee verschillende titels kunnen tot dezelfde slug instorten ("Café" en "Cafe" worden beide → <code>cafe</code>). Als je slugs als URL-keys gebruikt, voeg een korte ID of suffix toe bij collision.</li>
  <li><strong>Verander geen geshipte slugs.</strong> Zodra een URL live en geïndexeerd is, breekt zijn slug regenereren links en SEO. Als een titel verandert, behoud de oude slug of zet een 301-redirect op.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Bir URL slug, bir URL'nin insan tarafından okunabilir son segmentidir — <code>/blog/the-quick-brown-fox</code>, <code>/blog/post-4827</code> yerine. İyi slug'lar küçük harfli, tirelidir, sadece ASCII'dir ve bir bakışta okunacak kadar kısadır, ama aksan, noktalama ve emoji dolu gerçek başlıklardan üretmek zahmetlidir. Bu araç aksanları transliter eder, çöpü temizler, seçtiğin ayraçla birleştirir ve çıktının doğrudan bir route veya dosya adına bırakmaya güvenli olması için temiz bir sınırda keser.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Makale başlıklarından <code>/blog/&lt;slug&gt;</code> URL'leri üretme — özellikle başlıklar aksanlı karakterler (à, ñ, ø) veya noktalama (iki nokta üst üste, parantez, em dash) içerdiğinde.</li>
  <li>Kullanıcı tarafından sağlanan adlardan güvenli dosya adları üretme — upload'lar, export'lar, üretilen raporlar.</li>
  <li>İnsan etiketlerinden tag'ler, kategoriler veya çapalar için (<code>#getting-started</code>) kararlı tanımlayıcılar kurma.</li>
  <li>Statik site build adımı için bir başlık listesini toplu olarak kebab-case'e dönüştürme.</li>
</ul>

<h3>Dönüşüm nasıl çalışır</h3>
<ol>
  <li>Unicode'u NFD-normalize eder ve birleştirici diakritikleri temizler (<code>café → cafe</code>).</li>
  <li>Yaygın Avrupa bağlaçlarını ve özel harfleri eşler: <code>ß → ss</code>, <code>æ → ae</code>, <code>ø → o</code>, <code>Ł → L</code>, artı birkaç para birimi/matematik sembolü (<code>€ → eur</code>, <code>& → and</code>).</li>
  <li>Her alfanümerik olmayan grubu tek boşlukla değiştirir.</li>
  <li>İsteğe bağlı olarak yaygın İngilizce stop word'leri düşürür (<em>a, an, and, the, of, to, …</em>).</li>
  <li>Küçük harfe çevirir (veya case'i korur), ayraçınla birleştirir ve sondaki ayraç bırakmadan sınırda keser.</li>
</ol>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Latin olmayan yazılar düşer.</strong> Diakritik temizleme à/ñ/ø'yi ele alır, ama Çince, Japonca, Kiril, Arapça veya İbranice'yi karakter karakter romanize edemez — bunlar dile özgü tablolar gerektirir.</li>
  <li><strong>Stop-word kaldırma sadece İngilizce'dir.</strong> "El gato negro" <em>el</em>'i kaybetmez; "Le chat noir" <em>le</em>'yi kaybetmez. İngilizce olmayan başlıklar için toggle'ı kapat.</li>
  <li><strong>Kesme anlamı değiştirebilir.</strong> "introduction-to-rust-programming" 20 karaktere kesilirse "introduction-to-rust" olur — iyi; 16'ya kesilirse "introduction-to" olur — açıkça daha kötü.</li>
  <li><strong>Slug'lar benzersiz değildir.</strong> İki farklı başlık aynı slug'a çökebilir ("Café" ve "Cafe" ikisi de → <code>cafe</code>). Slug'ları URL anahtarları olarak kullanıyorsan, çakışmada kısa bir ID veya sonek ekle.</li>
  <li><strong>Gönderilmiş slug'ları değiştirme.</strong> Bir URL canlı ve indekslendikten sonra, slug'unu yeniden üretmek linkleri ve SEO'yu bozar. Bir başlık değişirse, eski slug'u koru veya 301 yönlendirmesi kur.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>URL slug adalah segmen terakhir URL yang bisa dibaca manusia — <code>/blog/the-quick-brown-fox</code> bukan <code>/blog/post-4827</code>. Slug yang baik adalah lowercase, ber-hyphen, hanya ASCII, dan cukup pendek untuk dibaca sekilas, tapi menghasilkannya dari judul nyata yang penuh aksen, tanda baca, dan emoji itu ribet untuk dibenarkan. Tool ini men-transliterate aksen, membuang sampah, menggabungkan dengan separator pilihan kamu, dan memotong di batas yang bersih sehingga output aman untuk langsung di-drop ke route atau filename.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Menghasilkan URL <code>/blog/&lt;slug&gt;</code> dari judul artikel — terutama saat judul mengandung karakter beraksen (à, ñ, ø) atau tanda baca (titik dua, kurung, em dash).</li>
  <li>Memproduksi filename aman dari nama yang disediakan user — upload, export, generated report.</li>
  <li>Membangun identifier stabil untuk tag, kategori, atau anchor (<code>#getting-started</code>) dari label manusia.</li>
  <li>Mengkonversi batch daftar heading ke kebab-case untuk langkah build static-site.</li>
</ul>

<h3>Cara konversi bekerja</h3>
<ol>
  <li>NFD-normalize Unicode dan strip combining diacritic (<code>café → cafe</code>).</li>
  <li>Memetakan ligature Eropa umum dan huruf khusus: <code>ß → ss</code>, <code>æ → ae</code>, <code>ø → o</code>, <code>Ł → L</code>, plus beberapa simbol mata uang/matematika (<code>€ → eur</code>, <code>& → and</code>).</li>
  <li>Mengganti setiap run non-alfanumerik dengan satu spasi.</li>
  <li>Opsional membuang stop word umum bahasa Inggris (<em>a, an, and, the, of, to, …</em>).</li>
  <li>Lowercase (atau pertahankan case), gabungkan dengan separator kamu, dan potong di limit tanpa meninggalkan separator menggantung.</li>
</ol>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Aksara non-Latin terbuang.</strong> Stripping diakritik menangani à/ñ/ø, tapi tidak bisa romanize Mandarin, Jepang, Sirilik, Arab, atau Ibrani karakter-per-karakter — itu butuh tabel spesifik bahasa (Hanyu Pinyin, transliterasi ICU) yang sengaja di luar scope di sini. Karakter seperti itu hilang setelah langkah strip.</li>
  <li><strong>Penghapusan stop-word hanya bahasa Inggris.</strong> "El gato negro" tidak kehilangan <em>el</em>; "Le chat noir" tidak kehilangan <em>le</em>. Matikan toggle untuk judul non-Inggris.</li>
  <li><strong>Truncation bisa mengubah makna.</strong> "introduction-to-rust-programming" dipotong ke 20 karakter jadi "introduction-to-rust" — oke; dipotong ke 16 jadi "introduction-to" — jelas lebih buruk. Atur limit manual untuk konten di mana ekor penting.</li>
  <li><strong>Slug tidak unik.</strong> Dua judul berbeda bisa collapse ke slug yang sama ("Café" dan "Cafe" keduanya → <code>cafe</code>). Jika kamu memakai slug sebagai URL key, append ID pendek atau suffix saat tabrakan.</li>
  <li><strong>Jangan ubah slug yang sudah di-ship.</strong> Setelah URL live dan terindeks, regenerasi slug-nya merusak link dan SEO. Jika judul berubah, pertahankan slug lama atau setup 301 redirect.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>URL slug là phần URL chứa keyword: <code>/blog/my-great-post</code>. Slug nên là chữ thường, không có space, không có dấu câu, và không có dấu (accent). Tool này biến bất kỳ tiêu đề nào thành slug đẹp — chuyển tự chữ có dấu sang ASCII, bỏ dấu câu, viết thường tất cả và nối các từ bằng dấu gạch ngang.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Bài blog mới — biến tiêu đề thành URL slug.</li>
  <li>Trang sản phẩm — tạo slug từ tên sản phẩm.</li>
  <li>Anchor heading trong tài liệu — slug heading tạo anchor ID.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Slug nên là duy nhất.</strong> Hai bài "My Day" sẽ tạo cùng slug — backend nên thêm hậu tố hoặc append ID.</li>
  <li><strong>Đừng đổi slug đã ship.</strong> Slug là phần permalink — đổi nó vỡ link. Nếu bạn phải, set up redirect.</li>
  <li><strong>Chữ tiếng Việt và châu Á.</strong> Chuyển tự (transliteration) loại bỏ dấu thì OK cho Việt nhưng tiếng Trung và tiếng Nhật cần pinyin/romaji — không có quy tắc chung. Tool này keep ASCII chữ cái thông qua các quy tắc tiêu chuẩn.</li>
</ul>
""",
    },
    "related": ["case-converter", "url-encoder", "lorem-ipsum"],
    "howto": {"flow": "transform", "action": "convert", "noun": "slug"},
}
