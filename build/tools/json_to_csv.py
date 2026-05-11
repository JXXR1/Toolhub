TOOL = {
    "slug": "json-to-csv",
    "category": "data",
    "icon": "📋",
    "tags": ["json", "csv", "convert", "data", "export", "excel"],
    "i18n": {
        "en": {
            "name": "JSON to CSV",
            "tagline": "Convert JSON arrays of objects to CSV. Auto-detects fields, supports custom delimiters, escapes properly for Excel and Google Sheets.",
            "description": "Free online JSON to CSV converter. Flattens arrays of objects to rows, escapes quotes per RFC 4180, supports comma/semicolon/tab delimiters.",
        },
        "de": {"name": "JSON zu CSV", "tagline": "Konvertiere JSON-Arrays von Objekten zu CSV. Auto-Felderkennung, eigene Trennzeichen, Excel- und Google-Sheets-kompatibel.", "description": "Kostenloser JSON-zu-CSV-Konverter. Wandelt Objekt-Arrays in Zeilen um, escapet nach RFC 4180, unterstützt Komma/Semikolon/Tab."},
        "es": {"name": "JSON a CSV", "tagline": "Convierte arrays JSON de objetos en CSV. Detecta campos, soporta separadores personalizados, escapado para Excel y Google Sheets.", "description": "Conversor JSON a CSV gratuito. Aplana arrays de objetos en filas, escape conforme a RFC 4180, separadores coma/punto y coma/tab."},
        "fr": {"name": "JSON vers CSV", "tagline": "Convertissez des tableaux JSON d'objets en CSV. Détection des champs, séparateurs personnalisés, échappement compatible Excel et Google Sheets.", "description": "Convertisseur JSON vers CSV gratuit. Aplatit les tableaux d'objets en lignes, échappement RFC 4180, séparateurs virgule/point-virgule/tab."},
        "it": {"name": "JSON a CSV", "tagline": "Converti array JSON di oggetti in CSV. Rilevamento campi, separatori personalizzati, escape compatibile con Excel e Google Sheets.", "description": "Convertitore JSON-CSV gratuito. Appiattisce array di oggetti in righe, escape RFC 4180, separatori virgola/punto e virgola/tab."},
        "pt": {"name": "JSON para CSV", "tagline": "Converte arrays JSON de objetos em CSV. Detecta os campos automaticamente, suporta delimitadores customizados e faz escape correto pra Excel e Google Sheets.", "description": "Conversor JSON para CSV grátis online. Achata arrays de objetos em linhas, faz escape de aspas conforme a RFC 4180, suporta delimitadores vírgula/ponto e vírgula/tab."},
        "pl": {"name": "JSON do CSV", "tagline": "Konwertuj tablice obiektów JSON na CSV. Auto-wykrywanie pól, własne delimitery, poprawny escape pod Excela i Google Sheets.", "description": "Darmowy online konwerter JSON do CSV. Spłaszcza tablice obiektów w wiersze, escape'uje cudzysłowy wg RFC 4180, wspiera delimitery przecinek/średnik/tab."},
        "ja": {"name": "JSON から CSV", "tagline": "JSON のオブジェクト配列を CSV に変換。フィールド自動検出、カスタム区切り、Excel・Google Sheets 向けに正しくエスケープ。", "description": "オンライン無料の JSON → CSV コンバーター。オブジェクト配列を行に展開し、RFC 4180 に従って引用符をエスケープ。カンマ／セミコロン／タブの区切り文字に対応します。"},
        "nl": {"name": "JSON naar CSV", "tagline": "Converteer JSON-arrays van objects naar CSV. Detecteert velden automatisch, ondersteunt custom delimiters, escapet correct voor Excel en Google Sheets.", "description": "Gratis online JSON-naar-CSV converter. Flat arrays van objects naar rows, escapet quotes volgens RFC 4180, ondersteunt komma/puntkomma/tab delimiters."},
        "tr": {"name": "JSON'dan CSV'ye", "tagline": "Nesne JSON dizilerini CSV'ye dönüştür. Alanları otomatik tespit eder, özel sınırlayıcıları destekler, Excel ve Google Sheets için doğru escape yapar.", "description": "Ücretsiz online JSON'dan CSV'ye dönüştürücü. Nesne dizilerini satırlara düzleştirir, tırnakları RFC 4180'e göre escape eder, virgül/noktalı virgül/sekme sınırlayıcılarını destekler."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Delimiter</label>
      <select id="jc-delim" onchange="jcRun()">
        <option value=",">, comma</option>
        <option value=";">; semicolon</option>
        <option value="\\t">tab</option>
        <option value="|">| pipe</option>
      </select>
    </div>
    <div>
      <label>Output</label>
      <select id="jc-mode" onchange="jcRun()">
        <option value="header">With header row</option>
        <option value="noheader">No header row</option>
      </select>
    </div>
  </div>
  <label style="margin-top:1rem">JSON input (array of objects, or array of arrays)</label>
  <textarea id="jc-in" oninput="jcRun()" spellcheck="false" placeholder='[{"name":"Alice","age":30},{"name":"Bob","age":25}]'></textarea>
</div>
<div class="tool-card">
  <label>CSV output</label>
  <div class="output-row">
    <pre class="output" id="jc-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('jc-out', this)">{LBL_COPY}</button>
  </div>
  <button class="secondary" onclick="jcDownload()" style="margin-top:0.5rem">{LBL_DOWNLOAD} .csv</button>
</div>
""",
    "script": """
<script>
function jcEsc(v, delim){
  if (v === null || v === undefined) return '';
  let s = typeof v === 'object' ? JSON.stringify(v) : String(v);
  if (s.includes('"') || s.includes(delim) || s.includes('\\n') || s.includes('\\r')){
    s = '"' + s.replace(/"/g,'""') + '"';
  }
  return s;
}
function jcRun(){
  const raw = document.getElementById('jc-in').value.trim();
  const delim = document.getElementById('jc-delim').value === '\\\\t' ? '\\t' : document.getElementById('jc-delim').value;
  const withHeader = document.getElementById('jc-mode').value === 'header';
  const out = document.getElementById('jc-out');
  out.classList.remove('error');
  if (!raw){ out.textContent = '{LBL_NO_INPUT}'; return; }
  let data;
  try { data = JSON.parse(raw); }
  catch(e){ out.classList.add('error'); out.textContent = '✗ Invalid JSON: ' + e.message; return; }
  if (!Array.isArray(data)){ out.classList.add('error'); out.textContent = '✗ Expected a JSON array at the top level'; return; }
  if (data.length === 0){ out.textContent = ''; return; }
  let csv = '';
  if (data.every(r => Array.isArray(r))){
    csv = data.map(r => r.map(v => jcEsc(v, delim)).join(delim)).join('\\n');
  } else if (data.every(r => r && typeof r === 'object')){
    const keys = [...new Set(data.flatMap(r => Object.keys(r)))];
    if (withHeader) csv += keys.map(k => jcEsc(k, delim)).join(delim) + '\\n';
    csv += data.map(r => keys.map(k => jcEsc(r[k], delim)).join(delim)).join('\\n');
  } else {
    out.classList.add('error'); out.textContent = '✗ Mixed array — expected uniform objects or arrays'; return;
  }
  out.textContent = csv;
}
function jcDownload(){
  const csv = document.getElementById('jc-out').textContent;
  if (!csv || csv === '{LBL_NO_INPUT}') return;
  const blob = new Blob([csv], {type: 'text/csv'});
  const a = document.createElement('a');
  a.download = 'data.csv';
  a.href = URL.createObjectURL(blob);
  a.click();
}
document.addEventListener('DOMContentLoaded', jcRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>The reverse trip: feed in a JSON array and get out a CSV ready for Excel, Google Sheets, or any data tool that prefers tabular formats. Headers are auto-detected from object keys; nested values get JSON-stringified into single cells so nothing silently disappears.</p>

<h3>When to use it</h3>
<ul>
  <li>Turning an API response into a CSV for a stakeholder who only opens spreadsheets.</li>
  <li>Exporting a pile of records from a JSON dump into something you can pivot/filter in Sheets.</li>
  <li>Generating fixture rows for database imports that take CSV.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Header inference uses the union of all object keys.</strong> A row missing a key becomes an empty cell; the column doesn't disappear.</li>
  <li><strong>Nested objects/arrays are stringified.</strong> If you need a flattened CSV (one column per nested key), pre-flatten the JSON before feeding it in.</li>
  <li><strong>Excel + delimiters.</strong> European locales default to semicolons; switch the delimiter so the file opens with columns instead of one giant line. RFC 4180 escaping is applied either way.</li>
  <li><strong>UTF-8 BOM.</strong> Excel on macOS sometimes garbles non-ASCII without a BOM. This tool does NOT prepend one — paste the output through a BOM-adding step if you see mojibake.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>O caminho inverso: você joga um array JSON e recebe um CSV pronto pra Excel, Google Sheets ou qualquer ferramenta de dados que prefira formato tabular. Os headers são detectados automaticamente das chaves dos objetos; valores aninhados são serializados como JSON em células únicas, pra que nada suma silenciosamente.</p>

<h3>Quando usar</h3>
<ul>
  <li>Transformar uma resposta de API em CSV pra um stakeholder que só abre planilhas.</li>
  <li>Exportar um monte de registros de um dump JSON pra algo que dê pra pivotar/filtrar no Sheets.</li>
  <li>Gerar fixtures de linhas pra imports de banco de dados que aceitam CSV.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>A inferência de header usa a união de todas as chaves dos objetos.</strong> Uma linha sem uma chave vira célula vazia; a coluna não some.</li>
  <li><strong>Objetos/arrays aninhados são serializados como string.</strong> Se você precisa de um CSV achatado (uma coluna por chave aninhada), achate o JSON antes de jogar aqui.</li>
  <li><strong>Excel + delimitadores.</strong> Locales europeus usam ponto e vírgula por padrão; troque o delimitador pra que o arquivo abra com colunas em vez de uma linha gigantesca. O escape da RFC 4180 é aplicado de qualquer jeito.</li>
  <li><strong>BOM UTF-8.</strong> O Excel no macOS às vezes embaralha não-ASCII sem BOM. Esta ferramenta NÃO adiciona um — passe o output por um passo que adiciona BOM se aparecer mojibake.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Droga w drugą stronę: wrzucasz tablicę JSON i dostajesz CSV gotowy do Excela, Google Sheets albo dowolnego narzędzia, które woli format tabularny. Nagłówki są wykrywane automatycznie z kluczy obiektów; zagnieżdżone wartości są stringifikowane do JSON-a w pojedyncze komórki, żeby nic nie zniknęło po cichu.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Zamiana odpowiedzi API w CSV dla stakeholdera, który otwiera tylko arkusze.</li>
  <li>Eksport masy rekordów z dumpa JSON do czegoś, co da się pivotować/filtrować w Sheets.</li>
  <li>Generowanie fixture'owych wierszy dla importów do bazy, które przyjmują CSV.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Wnioskowanie nagłówków używa unii wszystkich kluczy obiektów.</strong> Wiersz bez klucza staje się pustą komórką; kolumna nie znika.</li>
  <li><strong>Zagnieżdżone obiekty/tablice są stringifikowane.</strong> Jeśli potrzebujesz spłaszczonego CSV (jedna kolumna na zagnieżdżony klucz), spłaszcz JSON-a, zanim go tu wrzucisz.</li>
  <li><strong>Excel + delimitery.</strong> Lokalizacje europejskie domyślnie używają średnika; przełącz delimiter, żeby plik otworzył się w kolumnach zamiast jednej olbrzymiej linii. Escape wg RFC 4180 jest aplikowany tak czy siak.</li>
  <li><strong>BOM UTF-8.</strong> Excel na macOS czasem psuje znaki spoza ASCII bez BOM. To narzędzie NIE dodaje go — przepuść wyjście przez krok dodający BOM, jeśli widzisz mojibake.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>逆方向の変換です。JSON 配列を入力すると、Excel、Google Sheets、その他の表形式を好むデータツール向けの CSV を出力します。ヘッダーはオブジェクトのキーから自動検出され、ネストされた値は単一セルに JSON 文字列化されるため、データが静かに失われることはありません。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>API レスポンスを、スプレッドシートしか開かないステークホルダーに渡す CSV に変換するとき。</li>
  <li>JSON ダンプの大量レコードを Sheets でピボット／フィルタできる形に変換したいとき。</li>
  <li>CSV を受け付けるデータベースインポート用のフィクスチャ行を生成したいとき。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>ヘッダーは全オブジェクトのキー和集合から推論します。</strong> あるキーを持たない行は空セルになり、列自体は消えません。</li>
  <li><strong>ネストされたオブジェクトや配列は文字列化されます。</strong> フラットな CSV（ネストキーごとに 1 列）が必要な場合は、入力前に JSON を平坦化してください。</li>
  <li><strong>Excel と区切り文字。</strong> ヨーロッパロケールはセミコロン区切りがデフォルトです。区切りを切り替えて、1 行になってしまうのを避けてください。RFC 4180 のエスケープはどちらの場合も適用されます。</li>
  <li><strong>UTF-8 BOM。</strong> macOS の Excel は BOM がないと非 ASCII を化けさせることがあります。本ツールは BOM を付与しません。文字化けが見えたら BOM を付ける処理を別途挟んでください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>De omgekeerde reis: voer een JSON-array in en krijg een CSV terug klaar voor Excel, Google Sheets of elke data-tool die tabellaire formaten prefereert. Headers worden auto-gedetecteerd uit object-keys; geneste waarden worden JSON-gestringified in losse cellen zodat niets stilletjes verdwijnt.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een API-response omzetten naar een CSV voor een stakeholder die alleen spreadsheets opent.</li>
  <li>Een berg records uit een JSON-dump exporteren naar iets dat je kunt pivoteren/filteren in Sheets.</li>
  <li>Fixture-rows genereren voor database-imports die CSV nemen.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Header-inferentie gebruikt de union van alle object-keys.</strong> Een row die een key mist wordt een lege cel; de kolom verdwijnt niet.</li>
  <li><strong>Geneste objects/arrays worden gestringified.</strong> Als je een flattened CSV nodig hebt (één kolom per geneste key), pre-flatten je het JSON voor je het invoert.</li>
  <li><strong>Excel + delimiters.</strong> Europese locales defaulten op puntkomma's; switch de delimiter zodat het bestand met kolommen opent in plaats van één grote regel. RFC 4180-escaping wordt sowieso toegepast.</li>
  <li><strong>UTF-8 BOM.</strong> Excel op macOS verprutst non-ASCII soms zonder een BOM. Deze tool zet er GEEN voor — pak de output door een BOM-toevoegende stap als je mojibake ziet.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Ters yolculuk: bir JSON array besle ve Excel, Google Sheets veya tablosal biçimleri tercih eden herhangi bir veri aracı için hazır bir CSV çıkar. Başlıklar nesne anahtarlarından otomatik tespit edilir; iç içe değerler tek hücrelere JSON-stringify edilir, böylece hiçbir şey sessizce kaybolmaz.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Sadece spreadsheet açan bir paydaş için bir API yanıtını CSV'ye dönüştürme.</li>
  <li>Sheets'te pivot/filter yapabileceğin bir şeye JSON dump'tan bir yığın kayıt dışa aktarma.</li>
  <li>CSV alan veritabanı import'ları için fixture satırları üretme.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Başlık çıkarımı tüm nesne anahtarlarının birleşimini kullanır.</strong> Anahtar eksik bir satır boş hücre olur; sütun kaybolmaz.</li>
  <li><strong>İç içe nesneler/array'ler stringify edilir.</strong> Düzleştirilmiş bir CSV gerekiyorsa (iç içe anahtar başına bir sütun), beslemeden önce JSON'u önceden düzleştir.</li>
  <li><strong>Excel + sınırlayıcılar.</strong> Avrupa locale'leri varsayılan olarak noktalı virgül kullanır; dosya tek dev satır yerine sütunlarla açılsın diye sınırlayıcıyı değiştir. Her durumda RFC 4180 escape uygulanır.</li>
  <li><strong>UTF-8 BOM.</strong> macOS'ta Excel BOM olmadan bazen ASCII olmayanı bozar. Bu araç birini önüne EKLEMEZ — mojibake görürsen çıktıyı BOM-ekleme adımından geçir.</li>
</ul>
""",
    },
    "related": ["csv-to-json", "json-formatter", "yaml-json"],
    "howto": {"flow": "transform", "action": "convert", "noun": "JSON"},
}
