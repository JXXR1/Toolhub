TOOL = {
    "slug": "base64-encoder",
    "category": "encoding",
    "icon": "🔄",
    "tags": ["base64", "encode", "decode", "data-uri"],
    "i18n": {
        "en": {
            "name": "Base64 Encoder / Decoder",
            "tagline": "Encode text to Base64 or decode Base64 back to text. UTF-8 safe and base64url variant supported.",
            "description": "Free online Base64 encoder and decoder. UTF-8 safe with optional base64url variant for URLs and JWTs. Runs in your browser.",
        },
        "de": {"name": "Base64 Encoder / Decoder", "tagline": "Text in Base64 codieren oder Base64 in Text decodieren. UTF-8-sicher und base64url-Variante.", "description": "Kostenloser Base64 Encoder und Decoder. UTF-8-sicher mit optionaler base64url-Variante für URLs und JWTs."},
        "es": {"name": "Codificador / Decodificador Base64", "tagline": "Codifica texto a Base64 o decodifica Base64 a texto. Compatible con UTF-8 y variante base64url.", "description": "Codificador y decodificador Base64 gratuito. Compatible con UTF-8 y variante base64url para URLs y JWTs."},
        "fr": {"name": "Encodeur / Décodeur Base64", "tagline": "Encodez du texte en Base64 ou décodez du Base64 en texte. UTF-8 et variante base64url supportées.", "description": "Encodeur et décodeur Base64 gratuit. Compatible UTF-8 avec variante base64url pour URLs et JWTs."},
        "it": {"name": "Encoder / Decoder Base64", "tagline": "Codifica testo in Base64 o decodifica Base64 in testo. UTF-8 sicuro con variante base64url.", "description": "Encoder e decoder Base64 gratuito. UTF-8 sicuro con variante base64url per URL e JWT."},
        "pt": {"name": "Codificador / Decodificador Base64", "tagline": "Codifique texto em Base64 ou decodifique Base64 de volta em texto. Seguro em UTF-8 e suporta a variante base64url.", "description": "Codificador e decodificador Base64 online gratuito. Seguro em UTF-8 com variante base64url opcional para URLs e JWTs. Roda no seu navegador."},
        "pl": {"name": "Encoder / Decoder Base64", "tagline": "Koduj tekst do Base64 albo dekoduj Base64 z powrotem na tekst. Bezpieczny dla UTF-8, wariant base64url.", "description": "Darmowy encoder i decoder Base64 online. Bezpieczny dla UTF-8 z opcjonalnym wariantem base64url dla URL-i i JWT. Działa w przeglądarce."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Mode</label>
      <select id="b64-mode" onchange="b64Run()">
        <option value="enc">{LBL_ENCODE} (text → base64)</option>
        <option value="dec">{LBL_DECODE} (base64 → text)</option>
      </select>
    </div>
    <div>
      <label>Variant</label>
      <select id="b64-variant" onchange="b64Run()">
        <option value="std">Standard</option>
        <option value="url">base64url (URL/JWT-safe)</option>
      </select>
    </div>
  </div>
  <label style="margin-top:1rem">{LBL_INPUT}</label>
  <textarea id="b64-in" oninput="b64Run()" spellcheck="false"></textarea>
</div>
<div class="tool-card">
  <label>{LBL_OUTPUT}</label>
  <div class="output-row">
    <pre class="output" id="b64-out">{LBL_NO_INPUT}</pre>
    <button class="copy-btn secondary" onclick="copyOutput('b64-out', this)">{LBL_COPY}</button>
  </div>
  <div class="meta" id="b64-meta"></div>
</div>
""",
    "script": """
<script>
function b64Encode(s, urlSafe){
  const bytes = new TextEncoder().encode(s);
  let bin = '';
  for (const b of bytes) bin += String.fromCharCode(b);
  let out = btoa(bin);
  if (urlSafe) out = out.replace(/\\+/g,'-').replace(/\\//g,'_').replace(/=+$/,'');
  return out;
}
function b64Decode(s, urlSafe){
  let t = s.replace(/\\s+/g,'');
  if (urlSafe) t = t.replace(/-/g,'+').replace(/_/g,'/');
  while (t.length % 4) t += '=';
  const bin = atob(t);
  const bytes = new Uint8Array(bin.length);
  for (let i=0; i<bin.length; i++) bytes[i] = bin.charCodeAt(i);
  return new TextDecoder('utf-8', {fatal: true}).decode(bytes);
}
function b64Run(){
  const mode = document.getElementById('b64-mode').value;
  const variant = document.getElementById('b64-variant').value;
  const raw = document.getElementById('b64-in').value;
  const out = document.getElementById('b64-out');
  const meta = document.getElementById('b64-meta');
  out.classList.remove('error');
  if (!raw){ out.textContent = '{LBL_NO_INPUT}'; meta.textContent = ''; return; }
  try {
    const result = (mode === 'enc') ? b64Encode(raw, variant === 'url') : b64Decode(raw, variant === 'url');
    out.textContent = result;
    meta.textContent = result.length + ' chars';
  } catch(e){ out.classList.add('error'); out.textContent = '✗ ' + (e.message || e); meta.textContent = ''; }
}
document.addEventListener('DOMContentLoaded', b64Run);
</script>
""",
    "help": {
        "en": """
<h2>What Base64 actually does</h2>
<p>Base64 turns arbitrary bytes into 64 ASCII characters (A–Z, a–z, 0–9 plus two extras). Three input bytes become four output characters, so the result is roughly 33% larger than the input. It's an <em>encoding</em>, not encryption — anyone can decode it.</p>

<h3>When to use Base64</h3>
<ul>
  <li>Embedding small binary data inside text-only formats: data URIs, JSON values, environment variables, YAML strings.</li>
  <li>Encoding binary tokens (signatures, keys, hashes) for inclusion in URLs, headers, or cookies.</li>
  <li>Email attachments and SMIME — historic but still alive.</li>
</ul>

<h3>Standard vs base64url</h3>
<ul>
  <li><strong>Standard</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-4" target="_blank" rel="noopener noreferrer">RFC 4648 §4</a>) uses <code>+</code>, <code>/</code>, <code>=</code>. Fine in email, JSON values, most XML.</li>
  <li><strong>base64url</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-5" target="_blank" rel="noopener noreferrer">RFC 4648 §5</a>) uses <code>-</code>, <code>_</code>, and typically drops trailing <code>=</code> padding. Used in JWTs, OAuth tokens, and anywhere the value lives in a URL where <code>+</code>/<code>/</code>/<code>=</code> would need extra escaping.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Don't confuse it with encryption.</strong> Base64 is reversible by anyone. If the data is sensitive, encrypt it first.</li>
  <li><strong>UTF-8 round-trips correctly here</strong> — non-ASCII (é, 你好, 🚀) goes through <code>TextEncoder</code>/<code>TextDecoder</code>, not <code>btoa</code>/<code>atob</code> directly. Naive <code>btoa(str)</code> in JavaScript breaks on non-Latin characters.</li>
  <li><strong>Padding</strong> — standard Base64 always ends with 0/1/2 <code>=</code> characters depending on input length. base64url often omits them. Decoders that require padding will reject unpadded input; this tool re-adds it on decode if missing.</li>
  <li><strong>Whitespace inside encoded strings</strong> — the decoder here strips spaces and line breaks (common from copy-paste), but some libraries don't, so re-encode if you're piping to one of those.</li>
</ul>
""",
        "pt": """
<h2>O que o Base64 faz de verdade</h2>
<p>Base64 transforma bytes arbitrários em 64 caracteres ASCII (A–Z, a–z, 0–9 mais dois extras). Três bytes de entrada viram quatro caracteres de saída, então o resultado fica cerca de 33% maior que a entrada. É um <em>encoding</em>, não criptografia — qualquer um consegue decodificar.</p>

<h3>Quando usar Base64</h3>
<ul>
  <li>Embutir pequenos dados binários dentro de formatos só-texto: data URIs, valores JSON, variáveis de ambiente, strings YAML.</li>
  <li>Codificar tokens binários (assinaturas, chaves, hashes) para incluir em URLs, headers ou cookies.</li>
  <li>Anexos de e-mail e SMIME — histórico mas ainda em uso.</li>
</ul>

<h3>Standard vs base64url</h3>
<ul>
  <li><strong>Standard</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-4" target="_blank" rel="noopener noreferrer">RFC 4648 §4</a>) usa <code>+</code>, <code>/</code>, <code>=</code>. Funciona bem em e-mail, valores JSON, na maioria dos XML.</li>
  <li><strong>base64url</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-5" target="_blank" rel="noopener noreferrer">RFC 4648 §5</a>) usa <code>-</code>, <code>_</code> e tipicamente descarta o padding <code>=</code> no final. Usado em JWTs, tokens OAuth e em qualquer lugar onde o valor mora numa URL e <code>+</code>/<code>/</code>/<code>=</code> precisariam de escape extra.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Não confunda com criptografia.</strong> Base64 é reversível por qualquer um. Se o dado é sensível, criptografe primeiro.</li>
  <li><strong>UTF-8 faz round-trip corretamente aqui</strong> — caracteres não-ASCII (é, 你好, 🚀) passam por <code>TextEncoder</code>/<code>TextDecoder</code>, e não direto por <code>btoa</code>/<code>atob</code>. <code>btoa(str)</code> ingênuo em JavaScript quebra com caracteres não-latinos.</li>
  <li><strong>Padding</strong> — Base64 standard sempre termina com 0/1/2 caracteres <code>=</code> dependendo do tamanho da entrada. base64url frequentemente os omite. Decoders que exigem padding rejeitam entrada sem padding; esta ferramenta readiciona o padding no decode se estiver faltando.</li>
  <li><strong>Whitespace dentro de strings codificadas</strong> — o decoder aqui remove espaços e quebras de linha (comuns em copiar/colar), mas algumas bibliotecas não fazem isso, então recodifique se você for jogar o resultado numa delas.</li>
</ul>
""",
        "pl": """
<h2>Co Base64 właściwie robi</h2>
<p>Base64 zamienia dowolne bajty w 64 znaki ASCII (A–Z, a–z, 0–9 plus dwa dodatkowe). Trzy bajty wejścia stają się czterema znakami wyjścia, więc wynik jest mniej więcej 33% większy od wejścia. To <em>kodowanie</em>, nie szyfrowanie — każdy może to zdekodować.</p>

<h3>Kiedy używać Base64</h3>
<ul>
  <li>Wstawianie małych binarnych danych w formaty tekstowe: data URI, wartości JSON, zmienne środowiskowe, stringi YAML.</li>
  <li>Kodowanie binarnych tokenów (sygnatury, klucze, hashe) do umieszczenia w URL-ach, headerach albo cookies.</li>
  <li>Załączniki maili i SMIME — historyczne, ale wciąż żywe.</li>
</ul>

<h3>Standard vs base64url</h3>
<ul>
  <li><strong>Standard</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-4" target="_blank" rel="noopener noreferrer">RFC 4648 §4</a>) używa <code>+</code>, <code>/</code>, <code>=</code>. OK w mailu, wartościach JSON, większości XML.</li>
  <li><strong>base64url</strong> (<a href="https://datatracker.ietf.org/doc/html/rfc4648#section-5" target="_blank" rel="noopener noreferrer">RFC 4648 §5</a>) używa <code>-</code>, <code>_</code> i zwykle pomija końcowy padding <code>=</code>. Używany w JWT, tokenach OAuth i wszędzie tam, gdzie wartość siedzi w URL-u, gdzie <code>+</code>/<code>/</code>/<code>=</code> wymagałyby dodatkowego escape'owania.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Nie myl tego z szyfrowaniem.</strong> Base64 jest odwracalny przez każdego. Jeśli dane są wrażliwe — najpierw je zaszyfruj.</li>
  <li><strong>UTF-8 robi tu poprawny round-trip</strong> — znaki spoza ASCII (é, 你好, 🚀) idą przez <code>TextEncoder</code>/<code>TextDecoder</code>, nie bezpośrednio przez <code>btoa</code>/<code>atob</code>. Naiwne <code>btoa(str)</code> w JavaScripcie wywala się na znakach niełacińskich.</li>
  <li><strong>Padding</strong> — standardowy Base64 zawsze kończy się 0/1/2 znakami <code>=</code> w zależności od długości wejścia. base64url często go pomija. Dekodery wymagające paddingu odrzucają dane bez paddingu; to narzędzie sam dokleja go przy dekodowaniu, jeśli go brakuje.</li>
  <li><strong>Białe znaki w środku zakodowanego stringa</strong> — ten dekoder usuwa spacje i końce linii (typowe po copy-paste), ale niektóre biblioteki tego nie robią, więc przekoduj zanim wrzucisz to do takiej.</li>
</ul>
""",
    },
    "related": ["url-encoder", "html-encoder", "jwt-decoder", "image-to-base64"],
}
