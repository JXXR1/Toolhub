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
    },
    "related": ["json-to-csv", "json-formatter", "yaml-json"],
}
