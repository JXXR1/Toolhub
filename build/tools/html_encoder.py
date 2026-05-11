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
        "ja": {"name": "HTML エンコーダー / デコーダー", "tagline": "HTML 特殊文字をエスケープ、またはエンティティをデコード。ユーザー入力の安全な埋め込みや、エスケープ済みマークアップのデバッグに便利。", "description": "オンライン無料の HTML エンティティエンコーダー / デコーダー。&amp; &lt; &gt; &quot; ' と名前付きエンティティをエスケープし、名前付き・10 進・16 進のエンティティ参照をデコードします。"},
        "nl": {"name": "HTML Encoder / Decoder", "tagline": "Escape HTML-speciale tekens of decodeer entities terug. Nuttig voor veilig embedden van user input of debuggen van encoded markup.", "description": "Gratis online HTML-entity encoder en decoder. Escapet &amp; &lt; &gt; &quot; ' en named entities. Decodeert named, decimal en hex entity references."},
        "tr": {"name": "HTML Encoder / Decoder", "tagline": "HTML özel karakterlerini escape et veya entity'leri geri çöz. Kullanıcı girdisini güvenle gömmek veya kodlanmış işaretlemeyi debug etmek için kullanışlı.", "description": "Ücretsiz online HTML entity encoder ve decoder. &amp; &lt; &gt; &quot; ' ve adlandırılmış entity'leri escape eder. Adlandırılmış, sayısal ve hex entity referanslarını çözer."},
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
        "ja": """
<h2>用途</h2>
<p>HTML には構造的な意味を持つ 5 文字 — <code>&amp;</code>、<code>&lt;</code>、<code>&gt;</code>、<code>&quot;</code>、<code>'</code> — が予約されています。これらをページに<em>コンテンツ</em>として表示するには、ブラウザがマークアップとして解釈しないように HTML エンティティへエスケープする必要があります。本ツールは双方向に対応しており、生テキストを安全なエンティティへエンコード、または取得した HTML をプレーンテキストへデコードできます。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>信頼できないユーザー入力を HTML に埋め込むとき — XSS 対策のため、まずエンコードしてください。</li>
  <li>スクレイピングやコピーで取得した、エンティティ（<code>&amp;amp;</code>、<code>&amp;#x27;</code>、<code>&amp;ldquo;</code>）混じりのマークアップをデコードしたいとき。</li>
  <li>誤って二重エスケープされたテンプレートを元に戻したいとき。</li>
  <li>JSDoc、CDATA を使わない XML、Markdown のコードフェンスなど、リテラルな山括弧が必要な場面のスニペット作成。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>エンコードはサニタイズではありません。</strong> エンコードは表示用に安全化するだけです。タグを<em>除去</em>したいなら、別途 HTML サニタイザーが必要です。</li>
  <li><strong>属性とボディ。</strong> どちらも同じ 5 文字をエスケープしますが、<code>onclick</code> のような JavaScript イベントハンドラは追加のエスケープが必要です（本ツールは行いません。信頼できないデータを属性に入れないでください）。</li>
  <li><strong>デコーダは寛容です。</strong> 名前付きエンティティ（<code>&amp;ldquo;</code>）、10 進（<code>&amp;#34;</code>）、16 進（<code>&amp;#x22;</code>）はすべてブラウザのパーサーで復号されるため、本物のブラウザが受け入れるものはすべて受け入れます。</li>
  <li><strong>二重エンコードに注意。</strong> 既にエンコード済みの値を再度エンコードすると <code>&amp;amp;amp;</code> になります。入力にエンティティが見える場合はまずデコードしてください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>HTML reserveert vijf karakters met structurele betekenis — <code>&amp;</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&quot;</code>, <code>'</code>. Een van die als <em>content</em> in een pagina zetten vereist ze als HTML-entities te escapen zodat de browser ze niet als markup interpreteert. Deze tool werkt beide kanten op: encode raw tekst naar veilige entities, of decodeer scraped HTML terug naar plain text.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Onbetrouwbare user content embedden in HTML — encode eerst om XSS te voorkomen.</li>
  <li>Scraped of geplakte markup decoderen die met entities arriveerde (<code>&amp;amp;</code>, <code>&amp;#x27;</code>, <code>&amp;ldquo;</code>).</li>
  <li>Templates ontmangelen die per ongeluk dubbel zijn ge-escaped.</li>
  <li>Snippets voorbereiden voor JSDoc, CDATA-free XML of markdown code fences die letterlijke angle brackets nodig hebben.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Encoderen is geen sanitisering.</strong> Encoderen maakt tekst veilig om te tonen; als je ook tags wil <em>strippen</em> heb je een HTML-sanitizer nodig.</li>
  <li><strong>Attributen vs body.</strong> Beide contexts vereisen dezelfde vijf karakters geëscaped, maar JavaScript event handlers zoals <code>onclick</code> hebben extra escaping nodig (wat deze tool niet doet — houd untrusted data uit attributen).</li>
  <li><strong>Decoder is permissief.</strong> Named entities (<code>&amp;ldquo;</code>), decimal (<code>&amp;#34;</code>) en hex (<code>&amp;#x22;</code>) decoderen allemaal via de browser-parser, dus hij accepteert alles wat een echte browser zou accepteren.</li>
  <li><strong>Encode niet dubbel.</strong> Een al-encoded value encoderen geeft <code>&amp;amp;amp;</code>. Decodeer eerst als je entities in je input ziet.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>HTML beş karakter yapısal anlam için ayırır — <code>&amp;</code>, <code>&lt;</code>, <code>&gt;</code>, <code>&quot;</code>, <code>'</code>. Bunlardan herhangi birini bir sayfaya <em>içerik</em> olarak koymak, tarayıcının markup olarak yorumlamaması için bunları HTML entity olarak escape etmeyi gerektirir. Bu araç her iki yönü çevirir: ham metni güvenli entity'lere kodla veya kazınmış HTML'i düz metne geri çöz.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Güvenilmeyen kullanıcı içeriğini HTML'e gömerken — XSS'i önlemek için önce kodla.</li>
  <li>Entity'lerle gelen kazınmış veya kopyala-yapıştırılmış markup'ı çözme (<code>&amp;amp;</code>, <code>&amp;#x27;</code>, <code>&amp;ldquo;</code>).</li>
  <li>Yanlışlıkla çift escape edilmiş template'ları düzeltme.</li>
  <li>JSDoc, CDATA-free XML veya literal açı parantezi gereken markdown code fence'leri için snippet hazırlama.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Kodlama temizleme değildir.</strong> Kodlama metni güvenli gösterilebilir yapar; tag'leri <em>çıkarmak</em> istiyorsan, bir HTML sanitizer'a ihtiyacın var.</li>
  <li><strong>Nitelikler - gövde.</strong> Her iki bağlam da aynı beş karakteri escape etmeyi gerektirir, ancak <code>onclick</code> gibi JavaScript olay işleyicileri ek escape gerektirir (bu araç bunu yapmaz — güvenilmeyen veriyi niteliklerden uzak tut).</li>
  <li><strong>Decoder hoşgörülüdür.</strong> Adlandırılmış entity'ler (<code>&amp;ldquo;</code>), ondalık (<code>&amp;#34;</code>) ve hex (<code>&amp;#x22;</code>) hepsi tarayıcının parser'ı aracılığıyla çözülür, bu yüzden gerçek bir tarayıcının kabul edeceği her şeyi kabul eder.</li>
  <li><strong>Çift kodlama yapma.</strong> Zaten kodlanmış bir değeri kodlamak <code>&amp;amp;amp;</code> verir. Girişinde entity'ler görüyorsan önce decode et.</li>
</ul>
""",
    },
    "related": ["url-encoder", "base64-encoder", "markdown-to-html"],
    "howto": {"flow": "transform", "action": "encode",  "noun": "text"},
}
