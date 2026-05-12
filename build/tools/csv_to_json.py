TOOL = {
    "slug": "csv-to-json",
    "category": "data",
    "icon": "📊",
    "tags": ["csv", "json", "convert", "data", "import"],
    "i18n": {
        "en": {
            "name": "CSV to JSON",
            "tagline": "Convert CSV data to JSON arrays. Header detection, custom delimiters, quoted fields, and embedded newlines handled.",
            "description": "Free online CSV to JSON converter. Auto-detects headers, supports custom delimiters and quoted multi-line fields. Runs in your browser.",
        },
        "de": {"name": "CSV zu JSON", "tagline": "CSV-Daten in JSON-Arrays konvertieren. Header-Erkennung, eigene Trennzeichen, zitierte Felder und eingebettete Zeilenumbrüche.", "description": "Kostenloser CSV-zu-JSON-Konverter. Auto-Header-Erkennung, beliebige Trennzeichen, zitierte mehrzeilige Felder. Läuft im Browser."},
        "es": {"name": "CSV a JSON", "tagline": "Convierte datos CSV en arrays JSON. Detección de cabeceras, separadores personalizados y campos entre comillas.", "description": "Conversor CSV a JSON gratuito. Detecta cabeceras automáticamente, soporta separadores personalizados y campos entre comillas multilínea."},
        "fr": {"name": "CSV vers JSON", "tagline": "Convertissez du CSV en tableaux JSON. Détection d'en-têtes, séparateurs personnalisés, champs avec guillemets et sauts de ligne.", "description": "Convertisseur CSV vers JSON gratuit. Détection automatique d'en-têtes, séparateurs personnalisés, champs entre guillemets multi-lignes."},
        "it": {"name": "CSV a JSON", "tagline": "Converti dati CSV in array JSON. Riconoscimento intestazioni, separatori personalizzati, campi tra virgolette e a capo.", "description": "Convertitore CSV-JSON gratuito. Rileva intestazioni, supporta separatori personalizzati e campi multi-riga tra virgolette."},
        "pt": {"name": "CSV para JSON", "tagline": "Converta dados CSV em arrays JSON. Detecção de cabeçalho, delimitadores customizados, campos entre aspas e quebras de linha embutidas.", "description": "Conversor CSV para JSON online gratuito. Detecta cabeçalhos automaticamente, suporta delimitadores customizados e campos multilinha entre aspas. Roda no seu browser."},
        "pl": {"name": "CSV do JSON", "tagline": "Konwertuj dane CSV na tablice JSON. Wykrywanie nagłówka, własne delimitery, pola w cudzysłowach i osadzone końce linii.", "description": "Darmowy online konwerter CSV do JSON. Auto-wykrywanie nagłówków, wsparcie dla własnych delimiterów i wielowierszowych pól w cudzysłowach. Działa w przeglądarce."},
        "ja": {"name": "CSV から JSON", "tagline": "CSV データを JSON 配列に変換。ヘッダー検出、カスタム区切り文字、引用符付きフィールド、埋め込み改行に対応。", "description": "オンライン無料の CSV → JSON コンバーター。ヘッダーの自動検出、カスタム区切り文字、引用符で囲まれた複数行フィールドに対応。すべてブラウザ内で動作します。"},
        "nl": {"name": "CSV naar JSON", "tagline": "Converteer CSV-data naar JSON-arrays. Header-detectie, custom delimiters, quoted fields en embedded newlines worden afgehandeld.", "description": "Gratis online CSV naar JSON converter. Detecteert headers automatisch, ondersteunt custom delimiters en quoted multi-line fields. Draait in je browser."},
        "tr": {"name": "CSV'den JSON'a", "tagline": "CSV verisini JSON dizilerine dönüştür. Başlık tespiti, özel sınırlayıcılar, tırnaklı alanlar ve gömülü satır sonları işlenir.", "description": "Ücretsiz online CSV'den JSON'a dönüştürücü. Başlıkları otomatik tespit eder, özel sınırlayıcıları ve tırnaklı çok satırlı alanları destekler. Tarayıcıda çalışır."},
        "id": {"name": "CSV ke JSON", "tagline": "Konversi data CSV ke array JSON. Menangani deteksi header, delimiter custom, field yang di-quote, dan newline tersisip.", "description": "Konverter CSV ke JSON gratis. Tempel CSV apa pun dan dapatkan array JSON dari objek. Menangani deteksi header, delimiter custom, field yang di-quote, dan newline tersisip. Berjalan di browser-mu."},
        "vi": {"name": "CSV sang JSON", "tagline": "Chuyển dữ liệu CSV thành mảng JSON. Xử lý phát hiện header, delimiter tùy chỉnh, trường được quote và newline lồng nhau.", "description": "Bộ chuyển CSV sang JSON miễn phí trực tuyến. Phát hiện header tự động, hỗ trợ delimiter tùy chỉnh, trường được quote và newline trong giá trị. Toàn bộ chuyển đổi chạy cục bộ."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Delimiter</label>
      <select id="cj-delim" onchange="cjRun()">
        <option value=",">, comma</option>
        <option value=";">; semicolon</option>
        <option value="\\t">tab</option>
        <option value="|">| pipe</option>
      </select>
    </div>
    <div>
      <label>Has header row?</label>
      <select id="cj-header" onchange="cjRun()">
        <option value="yes">Yes — use as keys</option>
        <option value="no">No — emit arrays</option>
      </select>
    </div>
  </div>
  <label style="margin-top:1rem">CSV input</label>
  <textarea id="cj-in" oninput="cjRun()" spellcheck="false" placeholder='name,age,city
Alice,30,Bratislava
Bob,25,"Vienna, Austria"'></textarea>
</div>
<div class="tool-card">
  <label>JSON output</label>
  <div class="output-row">
    <pre class="output" id="cj-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('cj-out', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<script>
function csvParse(text, delim){
  // RFC 4180-ish parser: handles quoted fields with embedded delim and newlines, escaped quotes via ""
  const rows = [];
  let row = [], field = '', i = 0, inQ = false;
  while (i < text.length){
    const c = text[i];
    if (inQ){
      if (c === '"'){
        if (text[i+1] === '"'){ field += '"'; i += 2; continue; }
        inQ = false; i++; continue;
      }
      field += c; i++; continue;
    }
    if (c === '"'){ inQ = true; i++; continue; }
    if (c === delim){ row.push(field); field = ''; i++; continue; }
    if (c === '\\n' || c === '\\r'){
      if (c === '\\r' && text[i+1] === '\\n') i++;
      row.push(field); rows.push(row); row = []; field = ''; i++; continue;
    }
    field += c; i++;
  }
  if (field !== '' || row.length){ row.push(field); rows.push(row); }
  return rows;
}
function cjRun(){
  const raw = document.getElementById('cj-in').value;
  const delim = document.getElementById('cj-delim').value === '\\\\t' ? '\\t' : document.getElementById('cj-delim').value;
  const useHeader = document.getElementById('cj-header').value === 'yes';
  const out = document.getElementById('cj-out');
  out.classList.remove('error');
  if (!raw.trim()){ out.textContent = '{LBL_NO_INPUT}'; return; }
  try {
    const rows = csvParse(raw, delim);
    let result;
    if (useHeader && rows.length){
      const keys = rows[0];
      result = rows.slice(1).map(r => {
        const o = {};
        for (let k = 0; k < keys.length; k++){
          let v = r[k] ?? '';
          // type-coerce numbers/bools/null
          if (v === 'true') v = true;
          else if (v === 'false') v = false;
          else if (v === 'null' || v === '') v = v === 'null' ? null : '';
          else if (/^-?\\d+(?:\\.\\d+)?(?:[eE][-+]?\\d+)?$/.test(v)) v = Number(v);
          o[keys[k]] = v;
        }
        return o;
      });
    } else {
      result = rows;
    }
    out.textContent = JSON.stringify(result, null, 2);
  } catch(e){ out.classList.add('error'); out.textContent = '✗ ' + e.message; }
}
document.addEventListener('DOMContentLoaded', cjRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>CSV is the lingua franca of spreadsheet exports; JSON is the lingua franca of APIs and config. This converter takes properly-quoted CSV (RFC 4180-compatible) and emits a JSON array — either an array of objects (when there's a header row) or an array of arrays. Useful when you've exported a sheet and need to feed it into something that talks JSON.</p>

<h3>When to use it</h3>
<ul>
  <li>Turning a one-off Google Sheets / Excel export into seed data for an API mock or test fixture.</li>
  <li>Loading reference tables (countries, currency codes, lookup data) into a frontend that consumes JSON.</li>
  <li>Inspecting a CSV with embedded commas / newlines that gets misrendered everywhere except a real RFC 4180 parser.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Delimiter detection isn't magic.</strong> If your file uses semicolons (common in EU locales) or tabs (TSV), switch the delimiter dropdown — auto-detection guesses but can be fooled by data containing the wrong character.</li>
  <li><strong>Type coercion is opinionated.</strong> Numeric strings, <code>true</code>, <code>false</code>, and literal <code>null</code> are converted to JSON types. Things that look numeric but aren't (zip codes, ISBNs with leading zeros, phone numbers) lose leading zeros — disable coercion or post-process.</li>
  <li><strong>Empty cells become empty strings, not <code>null</code>.</strong> Most APIs treat the two differently.</li>
  <li><strong>BOMs in the wild.</strong> Excel often saves UTF-8 with a byte-order mark on Windows; the parser tolerates it but other consumers may not.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>CSV é a língua franca dos exports de planilha; JSON é a língua franca de APIs e configs. Este conversor pega um CSV bem formatado com aspas (compatível com RFC 4180) e devolve um array JSON — seja um array de objects (quando há linha de cabeçalho) ou um array de arrays. Útil quando você exportou uma planilha e precisa alimentar algo que fala JSON.</p>

<h3>Quando usar</h3>
<ul>
  <li>Transformar um export pontual de Google Sheets / Excel em seed data para um mock de API ou fixture de teste.</li>
  <li>Carregar tabelas de referência (países, códigos de moeda, dados de lookup) num frontend que consome JSON.</li>
  <li>Inspecionar um CSV com vírgulas / quebras de linha embutidas que renderiza errado em todo lugar exceto num parser RFC 4180 de verdade.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Detecção de delimitador não é mágica.</strong> Se seu arquivo usa ponto e vírgula (comum em locales europeus) ou tabs (TSV), troque no dropdown — a auto-detecção chuta mas pode ser enganada por dados que contêm o caractere errado.</li>
  <li><strong>Coerção de tipos é opinada.</strong> Strings numéricas, <code>true</code>, <code>false</code> e <code>null</code> literal são convertidos para tipos JSON. Coisas que parecem numéricas mas não são (CEPs, ISBNs com zero à esquerda, telefones) perdem os zeros — desabilite a coerção ou pós-processe.</li>
  <li><strong>Células vazias viram strings vazias, não <code>null</code>.</strong> A maioria das APIs trata os dois de forma diferente.</li>
  <li><strong>BOMs no mundo real.</strong> O Excel costuma salvar UTF-8 com byte-order mark no Windows; o parser tolera mas outros consumers podem não tolerar.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>CSV to lingua franca eksportów z arkuszy; JSON to lingua franca API i configów. Ten konwerter bierze poprawnie zacudzysłowiony CSV (zgodny z RFC 4180) i wypluwa tablicę JSON — albo tablicę obiektów (gdy jest wiersz nagłówka), albo tablicę tablic. Przydaje się, gdy wyeksportowałeś arkusz i musisz nakarmić nim coś, co mówi po JSON-owemu.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Zamiana jednorazowego eksportu z Google Sheets / Excela w seed data dla mocka API albo fixture'a testowego.</li>
  <li>Wczytanie tabel referencyjnych (kraje, kody walut, dane lookupowe) do frontendu konsumującego JSON.</li>
  <li>Inspekcja CSV-a z osadzonymi przecinkami / końcami linii, który źle się renderuje wszędzie poza prawdziwym parserem RFC 4180.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Wykrywanie delimitera nie jest magią.</strong> Jeśli plik używa średników (typowe w lokalizacjach EU) albo tabów (TSV), przełącz dropdown — auto-detekcja zgaduje, ale można ją oszukać danymi zawierającymi zły znak.</li>
  <li><strong>Konwersja typów jest opiniotwórcza.</strong> Stringi liczbowe, <code>true</code>, <code>false</code> i literalny <code>null</code> są konwertowane na typy JSON. Rzeczy, które wyglądają na liczbowe, ale nie są (kody pocztowe, ISBN-y z wiodącymi zerami, numery telefonów) tracą wiodące zera — wyłącz konwersję albo dopracuj po.</li>
  <li><strong>Puste komórki stają się pustymi stringami, nie <code>null</code>.</strong> Większość API traktuje to jako dwie różne rzeczy.</li>
  <li><strong>BOM-y w plikach z dzikiej.</strong> Excel zapisuje na Windowsie UTF-8 z byte-order markiem; parser to toleruje, ale inni konsumenci mogą nie.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>CSV はスプレッドシート出力の共通語、JSON は API や設定の共通語です。このコンバーターは適切に引用された CSV（RFC 4180 準拠）を入力として受け取り、JSON 配列を返します。ヘッダー行があるならオブジェクトの配列、そうでなければ配列の配列です。シートをエクスポートして JSON を扱う何かに食わせたいときに便利です。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>Google Sheets / Excel の単発エクスポートを、API モックやテストフィクスチャの seed データに変換するとき。</li>
  <li>参照テーブル（国コード、通貨コード、ルックアップデータ）を JSON 消費型のフロントエンドに読み込ませるとき。</li>
  <li>埋め込みカンマや改行を含む CSV で、ちゃんとした RFC 4180 パーサー以外では正しく開けないファイルを確認したいとき。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>区切り文字の自動検出は魔法ではありません。</strong> ファイルがセミコロン（EU ロケールに多い）やタブ（TSV）を使うなら、ドロップダウンで切り替えてください。データに該当文字が含まれていると自動推定が騙されることがあります。</li>
  <li><strong>型推論には方針があります。</strong> 数値文字列、<code>true</code>、<code>false</code>、リテラル <code>null</code> は JSON の型に変換されます。郵便番号、ISBN、電話番号など、見た目は数値だが実は違うデータは先頭の 0 が落ちます。型変換を無効にするか、変換後に補正してください。</li>
  <li><strong>空セルは <code>null</code> ではなく空文字列になります。</strong> 多くの API はこの 2 つを区別します。</li>
  <li><strong>実際のファイルにある BOM。</strong> Excel は Windows で UTF-8 をバイトオーダーマーク付きで保存することがあります。パーサーは許容しますが、他のコンシューマは許容しない場合があります。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>CSV is de lingua franca van spreadsheet-exports; JSON is de lingua franca van API's en config. Deze converter pakt correct-quoted CSV (RFC 4180-compatible) en levert een JSON-array — ofwel een array van objects (als er een header-row is) of een array van arrays. Nuttig als je een sheet hebt geëxporteerd en het in iets moet voeren dat JSON spreekt.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een eenmalige Google Sheets / Excel-export omzetten naar seed-data voor een API-mock of test fixture.</li>
  <li>Reference-tabellen (landen, currency codes, lookup-data) laden in een frontend die JSON consumeert.</li>
  <li>Een CSV inspecteren met embedded comma's / newlines die overal verkeerd rendert behalve in een echte RFC 4180-parser.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Delimiter-detectie is geen magie.</strong> Als je file puntkomma's gebruikt (gebruikelijk in EU-locales) of tabs (TSV), schakel de delimiter-dropdown — auto-detectie raadt maar kan voor de gek gehouden worden door data met het verkeerde karakter erin.</li>
  <li><strong>Type-coercion heeft een mening.</strong> Numerieke strings, <code>true</code>, <code>false</code> en letterlijk <code>null</code> worden geconverteerd naar JSON-types. Dingen die numeriek lijken maar niet zijn (postcodes, ISBN's met leading zeros, telefoonnummers) verliezen leading zeros — schakel coercion uit of post-process.</li>
  <li><strong>Lege cellen worden lege strings, geen <code>null</code>.</strong> De meeste API's behandelen die twee verschillend.</li>
  <li><strong>BOM's in het wild.</strong> Excel slaat UTF-8 op Windows vaak op met een byte-order mark; de parser tolereert het maar andere consumers misschien niet.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>CSV spreadsheet export'larının ortak dilidir; JSON API ve config'lerin ortak dilidir. Bu dönüştürücü düzgün tırnaklı CSV (RFC 4180 uyumlu) alır ve bir JSON dizisi çıkarır — bir başlık satırı olduğunda nesnelerin dizisi veya dizilerin dizisi. Bir sheet export ettiğinde ve onu JSON konuşan bir şeye beslemen gerektiğinde kullanışlıdır.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Tek seferlik bir Google Sheets / Excel export'unu bir API mock veya test fixture için seed verisine dönüştürme.</li>
  <li>Referans tablolarını (ülkeler, para birimi kodları, lookup verileri) JSON tüketen bir frontend'e yükleme.</li>
  <li>Gerçek bir RFC 4180 parser dışında her yerde yanlış render edilen gömülü virgül / yeni satırlı bir CSV'yi inceleme.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Sınırlayıcı tespiti sihir değildir.</strong> Dosyan noktalı virgül (AB locale'lerinde yaygın) veya sekme (TSV) kullanıyorsa, sınırlayıcı dropdown'unu değiştir — otomatik tespit tahmin eder ama yanlış karakter içeren veriyle kandırılabilir.</li>
  <li><strong>Tür dönüşümü tarafsız değildir.</strong> Sayısal string'ler, <code>true</code>, <code>false</code> ve literal <code>null</code> JSON türlerine dönüştürülür. Sayısal görünen ama olmayan şeyler (zip kodları, baştaki sıfırlı ISBN'ler, telefon numaraları) baştaki sıfırları kaybeder — coercion'u kapat veya post-process.</li>
  <li><strong>Boş hücreler boş string olur, <code>null</code> değil.</strong> Çoğu API ikisini farklı ele alır.</li>
  <li><strong>Doğadaki BOM'lar.</strong> Excel sıklıkla Windows'ta UTF-8'i byte-order mark ile kaydeder; parser bunu tolere eder ama diğer tüketiciler edemeyebilir.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>CSV adalah lingua franca dari export spreadsheet; JSON adalah lingua franca dari API dan config. Converter ini mengambil CSV yang ter-quote dengan benar (kompatibel RFC 4180) dan menghasilkan array JSON — bisa array of object (kalau ada header row) atau array of array. Berguna saat kamu sudah meng-export sheet dan perlu memberinya makan ke sesuatu yang berbicara JSON.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Mengubah export one-off dari Google Sheets / Excel menjadi seed data untuk API mock atau test fixture.</li>
  <li>Memuat tabel referensi (negara, kode mata uang, data lookup) ke frontend yang mengonsumsi JSON.</li>
  <li>Memeriksa CSV dengan koma / newline yang embedded yang ter-render salah di mana-mana kecuali di parser RFC 4180 sungguhan.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Deteksi delimiter bukan sihir.</strong> Jika file kamu menggunakan semicolon (umum di locale EU) atau tab (TSV), ubah dropdown delimiter — auto-detection menebak tapi bisa tertipu oleh data yang mengandung karakter yang salah.</li>
  <li><strong>Type coercion punya opini.</strong> String numerik, <code>true</code>, <code>false</code>, dan literal <code>null</code> dikonversi ke tipe JSON. Hal-hal yang terlihat numerik tapi sebenarnya bukan (kode pos, ISBN dengan leading zero, nomor telepon) kehilangan leading zero — matikan coercion atau post-process.</li>
  <li><strong>Sel kosong jadi string kosong, bukan <code>null</code>.</strong> Sebagian besar API memperlakukan keduanya secara berbeda.</li>
  <li><strong>BOM di dunia nyata.</strong> Excel sering menyimpan UTF-8 dengan byte-order mark di Windows; parser mentoleransinya tapi consumer lain mungkin tidak.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>CSV là định dạng dữ liệu lingua franca — Excel, Google Sheets, dump cơ sở dữ liệu, file export — nhưng nó khó để chương trình xử lý so với JSON. Tool này phân tích CSV và xuất ra JSON tương ứng (mảng các object, một object trên mỗi hàng) sẵn sàng để fetch, console.log, hoặc đặt vào schema validator.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Chuyển một export CSV nhỏ thành JSON để seed cơ sở dữ liệu hoặc dùng làm test fixture.</li>
  <li>Khám phá một file CSV — JSON dễ filter và truy vấn bằng tool dòng lệnh hơn.</li>
  <li>Đưa dữ liệu CSV vào một API kỳ vọng JSON.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Delimiter không chỉ là dấu phẩy.</strong> CSV châu Âu thường dùng dấu chấm phẩy vì dấu phẩy là dấu thập phân trong các locale đó. Tool này cho phép bạn chọn delimiter.</li>
  <li><strong>Field được quote có thể chứa newline.</strong> Một CSV well-formed quote các field chứa dấu phẩy hoặc newline. Đảm bảo parser hiểu điều đó — đừng split chỉ trên newline.</li>
  <li><strong>Encoding nhập nhằng.</strong> File CSV có thể là UTF-8, Latin-1, Windows-1252, hoặc thậm chí UTF-16. Nếu ký tự đặc biệt trông xấu xí, encoding sai. Convert sang UTF-8 trước khi parse.</li>
  <li><strong>Number trông giống chuỗi.</strong> CSV không có kiểu — mọi thứ là văn bản. Tool có thể auto-detect số, nhưng kiểm tra xem ID dài (snowflake, mã sản phẩm có 0 ở đầu) có bị hỏng không.</li>
</ul>
""",
    },
    "related": ["json-to-csv", "json-formatter", "yaml-json"],
    "howto": {"flow": "transform", "action": "convert", "noun": "CSV"},
}
