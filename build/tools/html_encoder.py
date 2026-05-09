TOOL = {
    "slug": "html-encoder",
    "category": "encoding",
    "icon": "&lt;&gt;",
    "tags": ["html", "encode", "entities", "escape", "xss"],
    "i18n": {
        "en": {
            "name": "HTML Encoder / Decoder",
            "tagline": "Escape HTML special characters or decode entities back. Useful for safely embedding user input or debugging encoded markup.",
            "description": "Free online HTML entity encoder and decoder. Escapes &amp; &lt; &gt; &quot; ' and named entities. Decodes named, numeric, and hex entity references.",
        },
        "de": {"name": "HTML Encoder / Decoder", "tagline": "HTML-Sonderzeichen escapen oder Entities zurück in Klartext.", "description": "Kostenloser HTML-Entity Encoder und Decoder. Escapet &amp; &lt; &gt; &quot; ' und benannte Entities."},
        "es": {"name": "Codificador / Decodificador HTML", "tagline": "Escapa caracteres especiales HTML o decodifica entidades.", "description": "Codificador y decodificador de entidades HTML gratuito. Escapa &amp; &lt; &gt; &quot; ' y entidades con nombre."},
        "fr": {"name": "Encodeur / Décodeur HTML", "tagline": "Échappez les caractères spéciaux HTML ou décodez les entités.", "description": "Encodeur et décodeur d'entités HTML gratuit. Échappe &amp; &lt; &gt; &quot; ' et entités nommées."},
        "it": {"name": "Encoder / Decoder HTML", "tagline": "Escape di caratteri speciali HTML o decodifica delle entità.", "description": "Encoder e decoder di entità HTML gratuito. Escape di &amp; &lt; &gt; &quot; ' e entità con nome."},
        "pt": {"name": "Encoder / Decoder HTML", "tagline": "Faz escape de caracteres especiais HTML ou decodifica entidades de volta. Útil para embutir input do usuário com segurança ou debugar markup escapado.", "description": "Encoder e decoder de entidades HTML grátis online. Faz escape de &amp; &lt; &gt; &quot; ' e entidades nomeadas. Decodifica entidades nomeadas, decimais e em hex."},
        "pl": {"name": "Encoder / Decoder HTML", "tagline": "Escape'uj znaki specjalne HTML albo dekoduj encje z powrotem. Przydatne do bezpiecznego osadzania inputu użytkownika albo debugowania zescape'owanego markupu.", "description": "Darmowy online encoder i decoder encji HTML. Escape'uje &amp; &lt; &gt; &quot; ' oraz nazwane encje. Dekoduje nazwane, dziesiętne i szesnastkowe odwołania do encji."},
    },
    "body": """
<div class="tool-card">
  <label>Mode</label>
  <select id="he-mode" onchange="heRun()">
    <option value="enc">{LBL_ENCODE} (text → entities)</option>
    <option value="dec">{LBL_DECODE} (entities → text)</option>
  </select>
  <label style="margin-top:1rem">{LBL_INPUT}</label>
  <textarea id="he-in" oninput="heRun()" spellcheck="false"></textarea>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="he-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('he-out', this)">{LBL_COPY}</button>
  </div>
</div>
""",
    "script": """
<script>
function heEnc(s){ return s.replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c])); }
function heDec(s){
  const t = document.createElement('textarea');
  t.innerHTML = s;
  return t.value;
}
function heRun(){
  const mode = document.getElementById('he-mode').value;
  const raw = document.getElementById('he-in').value;
  const out = document.getElementById('he-out');
  if (!raw){ out.textContent = '{LBL_NO_INPUT}'; return; }
  out.textContent = mode === 'enc' ? heEnc(raw) : heDec(raw);
}
document.addEventListener('DOMContentLoaded', heRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>HTML reserves five characters with structural meaning — <code>&amp;</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&quot;</code>, <code>'</code>. Putting any of those into a page as <em>content</em> requires escaping them as HTML entities so the browser doesn't interpret them as markup. This tool flips both directions: encode raw text into safe entities, or decode scraped HTML back to plain text.</p>

<h3>When to use it</h3>
<ul>
  <li>Embedding untrusted user content in HTML — encode first to prevent XSS.</li>
  <li>Decoding scraped or copy-pasted markup that arrived with entities (<code>&amp;amp;</code>, <code>&amp;#x27;</code>, <code>&amp;ldquo;</code>).</li>
  <li>Un-mangling templates that have been double-escaped accidentally.</li>
  <li>Preparing snippets for JSDoc, CDATA-free XML, or markdown code fences that need literal angle brackets.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Encoding is not sanitisation.</strong> Encoding makes text safe to display; if you also want to <em>strip</em> tags, you need an HTML sanitiser instead.</li>
  <li><strong>Attributes vs body.</strong> Both contexts need the same five characters escaped, but JavaScript event handlers like <code>onclick</code> need additional escaping (which this tool doesn't do — keep untrusted data out of attributes).</li>
  <li><strong>Decoder is permissive.</strong> Named entities (<code>&amp;ldquo;</code>), decimal (<code>&amp;#34;</code>) and hex (<code>&amp;#x22;</code>) all decode via the browser's parser, so it accepts anything a real browser would.</li>
  <li><strong>Don't double-encode.</strong> Encoding an already-encoded value gives you <code>&amp;amp;amp;</code>. Decode first if you see entities in your input.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>O HTML reserva cinco caracteres com significado estrutural — <code>&amp;</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&quot;</code>, <code>'</code>. Colocar qualquer um deles na página como <em>conteúdo</em> exige escapá-los como entidades HTML para que o browser não os interprete como markup. Esta ferramenta vai nas duas direções: codifica texto puro em entidades seguras, ou decodifica HTML capturado de volta para texto plano.</p>

<h3>Quando usar</h3>
<ul>
  <li>Embutir conteúdo de usuário não confiável em HTML — codifique antes para evitar XSS.</li>
  <li>Decodificar markup capturado ou colado que veio com entidades (<code>&amp;amp;</code>, <code>&amp;#x27;</code>, <code>&amp;ldquo;</code>).</li>
  <li>Desfazer templates que foram escapados em dobro por acidente.</li>
  <li>Preparar trechos para JSDoc, XML sem CDATA ou code fences de Markdown que precisam de sinais de menor/maior literais.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Encoding não é sanitização.</strong> Codificar deixa o texto seguro para exibir; se você também quer <em>remover</em> tags, precisa de um sanitizer HTML.</li>
  <li><strong>Atributos vs corpo.</strong> Os dois contextos precisam dos mesmos cinco caracteres escapados, mas event handlers JavaScript como <code>onclick</code> precisam de escape adicional (que esta ferramenta não faz — mantenha dados não confiáveis fora de atributos).</li>
  <li><strong>O decoder é permissivo.</strong> Entidades nomeadas (<code>&amp;ldquo;</code>), decimais (<code>&amp;#34;</code>) e hex (<code>&amp;#x22;</code>) são todas decodificadas pelo parser do browser, então aceita qualquer coisa que um browser real aceitaria.</li>
  <li><strong>Não codifique em dobro.</strong> Codificar um valor já codificado dá <code>&amp;amp;amp;</code>. Decodifique antes se vir entidades no input.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>HTML rezerwuje pięć znaków o znaczeniu strukturalnym — <code>&amp;</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&quot;</code>, <code>'</code>. Wstawienie któregokolwiek z nich na stronę jako <em>treści</em> wymaga zescape'owania ich jako encji HTML, żeby przeglądarka nie potraktowała ich jako markupu. To narzędzie idzie w obie strony: koduje surowy tekst na bezpieczne encje, albo dekoduje zeskrobany HTML z powrotem na zwykły tekst.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Osadzanie nieufanej treści użytkownika w HTML — zakoduj najpierw, żeby zapobiec XSS.</li>
  <li>Dekodowanie zeskrobanego albo skopiowanego markupu, który przyszedł z encjami (<code>&amp;amp;</code>, <code>&amp;#x27;</code>, <code>&amp;ldquo;</code>).</li>
  <li>Odplątywanie szablonów, które zostały przypadkowo zescape'owane podwójnie.</li>
  <li>Przygotowanie snippetów do JSDoc, XML bez CDATA albo code fence'ów Markdowna, które potrzebują dosłownych ostrych nawiasów.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Encoding to nie sanityzacja.</strong> Encoding sprawia, że tekst można bezpiecznie wyświetlić; jeśli chcesz też <em>wyciąć</em> tagi, potrzebujesz sanitizera HTML.</li>
  <li><strong>Atrybuty vs treść.</strong> Oba konteksty wymagają tych samych pięciu znaków escape'owanych, ale handlery JS typu <code>onclick</code> potrzebują dodatkowego escape'owania (czego to narzędzie nie robi — trzymaj nieufne dane z dala od atrybutów).</li>
  <li><strong>Decoder jest permisywny.</strong> Encje nazwane (<code>&amp;ldquo;</code>), dziesiętne (<code>&amp;#34;</code>) i hex (<code>&amp;#x22;</code>) — wszystko dekoduje przez parser przeglądarki, więc akceptuje wszystko, co przyjąłby prawdziwy browser.</li>
  <li><strong>Nie koduj podwójnie.</strong> Zakodowanie już zakodowanej wartości daje <code>&amp;amp;amp;</code>. Najpierw zdekoduj, jeśli widzisz encje w inpucie.</li>
</ul>
""",
    },
    "related": ["url-encoder", "base64-encoder", "markdown-to-html"],
}
