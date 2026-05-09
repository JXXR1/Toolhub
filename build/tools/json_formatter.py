TOOL = {
    "slug": "json-formatter",
    "category": "developer",
    "icon": "{ }",
    "tags": ["json", "format", "beautify", "validate", "minify"],
    "i18n": {
        "en": {
            "name": "JSON Formatter",
            "tagline": "Format, validate, and minify JSON instantly. Errors highlighted with line and column.",
            "description": "Free online JSON formatter and validator. Pretty-print, minify, and check JSON syntax with precise error messages.",
        },
        "de": {
            "name": "JSON-Formatter",
            "tagline": "JSON sofort formatieren, validieren und minimieren. Fehler werden mit Zeile und Spalte hervorgehoben.",
            "description": "Kostenloser Online-JSON-Formatter und Validator. JSON formatieren, minimieren und auf Syntax prüfen.",
        },
        "es": {
            "name": "Formateador JSON",
            "tagline": "Formatea, valida y minifica JSON al instante. Los errores se resaltan con línea y columna.",
            "description": "Formateador y validador JSON gratuito en línea. Formatea, minifica y verifica la sintaxis JSON.",
        },
        "fr": {
            "name": "Formateur JSON",
            "tagline": "Formatez, validez et minifiez du JSON instantanément. Les erreurs sont signalées avec ligne et colonne.",
            "description": "Formateur et validateur JSON gratuit en ligne. Embellissez, minifiez et vérifiez la syntaxe JSON.",
        },
        "it": {
            "name": "Formattatore JSON",
            "tagline": "Formatta, valida e minifica JSON all'istante. Gli errori sono evidenziati con riga e colonna.",
            "description": "Formattatore e validatore JSON gratuito online. Abbellisci, minifica e controlla la sintassi JSON.",
        },
        "pt": {
            "name": "Formatador JSON",
            "tagline": "Formata, valida e minifica JSON na hora. Erros destacados com linha e coluna.",
            "description": "Formatador e validador JSON grátis online. Pretty-print, minify e checagem da sintaxe JSON com mensagens de erro precisas.",
        },
        "pl": {
            "name": "Formatter JSON",
            "tagline": "Formatuj, waliduj i minifikuj JSON od ręki. Błędy podświetlone z numerem linii i kolumny.",
            "description": "Darmowy online formatter i walidator JSON. Pretty-print, minify i sprawdzanie składni JSON z precyzyjnymi komunikatami błędów.",
        },
    },
    "body": """
<div class="tool-card">
  <label for="json-input">{LBL_INPUT}</label>
  <textarea id="json-input" placeholder='{{"hello": "world", "n": 42}}' spellcheck="false"></textarea>
  <div class="button-row">
    <button onclick="jfFormat(2)">{LBL_FORMAT}</button>
    <button class="secondary" onclick="jfFormat(4)">Format (4-space)</button>
    <button class="secondary" onclick="jfMinify()">{LBL_MINIFY}</button>
    <button class="secondary" onclick="jfValidate()">{LBL_VALIDATE}</button>
    <button class="secondary" onclick="document.getElementById('json-input').value=''">{LBL_CLEAR}</button>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="json-output">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('json-output', this)">{LBL_COPY}</button>
  </div>
  <div class="meta" id="json-meta"></div>
</div>
""",
    "script": """
<script>
function jfShowError(e, raw){
  const out = document.getElementById('json-output');
  out.classList.add('error');
  out.classList.remove('success');
  let msg = e.message || String(e);
  // Try to extract position
  const m = msg.match(/position (\\d+)/i);
  if (m){
    const pos = parseInt(m[1], 10);
    const before = raw.slice(0, pos);
    const line = (before.match(/\\n/g) || []).length + 1;
    const col = pos - (before.lastIndexOf('\\n') + 1) + 1;
    msg = msg.replace(/position \\d+/i, 'line ' + line + ', col ' + col);
  }
  out.textContent = '✗ ' + msg;
  document.getElementById('json-meta').textContent = '';
}
function jfShowOk(text, label){
  const out = document.getElementById('json-output');
  out.classList.remove('error');
  out.classList.add('success');
  out.textContent = text;
  document.getElementById('json-meta').textContent = label || '';
}
function jfFormat(indent){
  const raw = document.getElementById('json-input').value.trim();
  if (!raw){ document.getElementById('json-output').textContent = '{LBL_NO_INPUT}'; return; }
  try {
    const obj = JSON.parse(raw);
    const out = JSON.stringify(obj, null, indent);
    jfShowOk(out, out.length + ' chars · ' + (out.match(/\\n/g)||[]).length + ' lines');
  } catch(e){ jfShowError(e, raw); }
}
function jfMinify(){
  const raw = document.getElementById('json-input').value.trim();
  if (!raw){ document.getElementById('json-output').textContent = '{LBL_NO_INPUT}'; return; }
  try {
    const obj = JSON.parse(raw);
    const out = JSON.stringify(obj);
    jfShowOk(out, out.length + ' chars (minified)');
  } catch(e){ jfShowError(e, raw); }
}
function jfValidate(){
  const raw = document.getElementById('json-input').value.trim();
  if (!raw){ document.getElementById('json-output').textContent = '{LBL_NO_INPUT}'; return; }
  try {
    const obj = JSON.parse(raw);
    const t = Array.isArray(obj) ? 'array' : typeof obj;
    const sz = JSON.stringify(obj).length;
    jfShowOk('✓ Valid JSON', 'top-level: ' + t + ' · ' + sz + ' chars minified');
  } catch(e){ jfShowError(e, raw); }
}
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>JSON travels minified — every byte counts when an API response is being shipped. But minified JSON is unreadable. This tool round-trips through the browser's native <code>JSON.parse</code> / <code>JSON.stringify</code> to produce indented, copy-able output, validate the structure, or strip whitespace back out. Nothing is uploaded; everything happens in the page.</p>

<h3>When to use it</h3>
<ul>
  <li>Pasting a minified API response and getting back something a human can scan.</li>
  <li>Catching syntax errors — trailing commas, unquoted keys, smart quotes — with the exact line/column the parser tripped on.</li>
  <li>Stripping whitespace before pasting JSON into a context where size matters (URL params, env vars, config files).</li>
  <li>Confirming your hand-written JSON is valid before piping it into another tool.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>JSON ≠ JavaScript object literal.</strong> Keys must be in double quotes. Single quotes, unquoted keys, and trailing commas all fail. If you've got JS object literals, run them through a converter first.</li>
  <li><strong>Smart quotes from copy-paste.</strong> Word processors and chat apps love to "helpfully" replace <code>"</code> with <code>"</code> / <code>"</code>. Those aren't valid JSON delimiters.</li>
  <li><strong>JSON has no comments.</strong> If your "JSON" has <code>//</code> or <code>/* */</code>, it's actually JSONC (used by VS Code config) — strip those before parsing.</li>
  <li><strong>Numbers larger than 2⁵³.</strong> JavaScript can't represent integers above <code>9007199254740992</code> exactly. Twitter snowflake IDs and similar should be quoted as strings.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>O JSON viaja minificado — cada byte conta quando uma resposta de API está sendo enviada. Mas JSON minificado é ilegível. Esta ferramenta faz round-trip pelo <code>JSON.parse</code> / <code>JSON.stringify</code> nativo do browser pra produzir output indentado e copiável, validar a estrutura ou tirar o whitespace de novo. Nada é enviado; tudo acontece na página.</p>

<h3>Quando usar</h3>
<ul>
  <li>Colar uma resposta de API minificada e receber algo que um humano consegue ler.</li>
  <li>Pegar erros de sintaxe — vírgulas no final, chaves sem aspas, smart quotes — com linha/coluna exata onde o parser tropeçou.</li>
  <li>Tirar whitespace antes de colar JSON num contexto onde tamanho importa (params de URL, env vars, arquivos de config).</li>
  <li>Confirmar que seu JSON feito à mão é válido antes de mandar pra outra ferramenta.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>JSON ≠ object literal de JavaScript.</strong> Chaves precisam estar entre aspas duplas. Aspas simples, chaves sem aspas e vírgulas no final, tudo falha. Se você tem object literals de JS, passe por um conversor antes.</li>
  <li><strong>Smart quotes vindas de copy-paste.</strong> Editores de texto e apps de chat adoram "ajudar" trocando <code>"</code> por <code>"</code> / <code>"</code>. Esses não são delimitadores JSON válidos.</li>
  <li><strong>JSON não tem comentários.</strong> Se seu "JSON" tem <code>//</code> ou <code>/* */</code>, na verdade é JSONC (usado em config do VS Code) — remova antes de fazer parse.</li>
  <li><strong>Números maiores que 2⁵³.</strong> O JavaScript não consegue representar inteiros acima de <code>9007199254740992</code> com exatidão. IDs snowflake do Twitter e similares devem vir entre aspas como strings.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>JSON podróżuje zminifikowany — każdy bajt się liczy, gdy odpowiedź API leci po sieci. Ale zminifikowany JSON jest nieczytelny. To narzędzie robi round-trip przez natywny <code>JSON.parse</code> / <code>JSON.stringify</code> przeglądarki, żeby wyprodukować wcięte, kopiowalne wyjście, zwalidować strukturę albo wyciąć białe znaki z powrotem. Nic nie jest wysyłane; wszystko dzieje się na stronie.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Wklejenie zminifikowanej odpowiedzi API i dostanie czegoś, co da się przeczytać po ludzku.</li>
  <li>Łapanie błędów składniowych — końcowych przecinków, kluczy bez cudzysłowu, smart quotes — z dokładnym numerem linii/kolumny, gdzie parser się wywalił.</li>
  <li>Wycinanie białych znaków przed wklejeniem JSON-a w kontekst, gdzie rozmiar ma znaczenie (parametry URL, zmienne środowiskowe, pliki configa).</li>
  <li>Potwierdzenie, że ręcznie pisany JSON jest poprawny, zanim wpuścisz go w inne narzędzie.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>JSON ≠ object literal w JavaScripcie.</strong> Klucze muszą być w podwójnych cudzysłowach. Pojedyncze cudzysłowy, klucze bez cudzysłowu i końcowe przecinki — wszystko padnie. Jeśli masz JS-owe object literale, najpierw przepuść je przez konwerter.</li>
  <li><strong>Smart quotes z copy-paste.</strong> Edytory tekstu i czaty uwielbiają "pomocnie" zamieniać <code>"</code> na <code>"</code> / <code>"</code>. To nie są poprawne delimitery JSON.</li>
  <li><strong>JSON nie ma komentarzy.</strong> Jeśli twój "JSON" ma <code>//</code> albo <code>/* */</code>, to faktycznie JSONC (używany w configu VS Code) — wytnij je przed parsem.</li>
  <li><strong>Liczby większe niż 2⁵³.</strong> JavaScript nie potrafi dokładnie reprezentować integerów powyżej <code>9007199254740992</code>. Snowflake'i z Twittera i podobne powinny być cytowane jako stringi.</li>
</ul>
""",
    },
    "related": ["regex-tester", "yaml-json", "json-diff"],
}
