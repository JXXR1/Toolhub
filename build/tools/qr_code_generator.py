TOOL = {
    "slug": "qr-code-generator",
    "category": "media",
    "icon": "📱",
    "tags": ["qr", "code", "generate", "url", "wifi", "vcard", "svg", "png"],
    "i18n": {
        "en": {
            "name": "QR Code Generator",
            "tagline": "Generate QR codes for any text, URL, Wi-Fi, or vCard. Custom size, colors, and error correction. Export PNG or SVG.",
            "description": "Free online QR code generator. Custom size, foreground/background colors, error correction levels. Download as PNG or SVG. No watermarks.",
        },
        "de": {
            "name": "QR-Code-Generator",
            "tagline": "Erzeuge QR-Codes für Text, URLs, WLAN oder vCards. Größe, Farben und Fehlerkorrektur einstellbar. Export als PNG oder SVG.",
            "description": "Kostenloser QR-Code-Generator. Größe, Vorder-/Hintergrundfarbe und Fehlerkorrekturstufen. PNG oder SVG ohne Wasserzeichen.",
        },
        "es": {
            "name": "Generador de Códigos QR",
            "tagline": "Genera códigos QR para texto, URLs, Wi-Fi o vCards. Tamaño, colores y corrección de errores personalizables. Exporta PNG o SVG.",
            "description": "Generador de códigos QR gratuito en línea. Tamaño, colores y niveles de corrección de errores personalizables. PNG o SVG sin marcas de agua.",
        },
        "fr": {
            "name": "Générateur de Codes QR",
            "tagline": "Générez des codes QR pour du texte, URL, Wi-Fi ou vCard. Taille, couleurs et correction d'erreurs personnalisables. Export PNG ou SVG.",
            "description": "Générateur de codes QR gratuit en ligne. Taille, couleurs avant/arrière, niveaux de correction. PNG ou SVG sans filigrane.",
        },
        "it": {
            "name": "Generatore di Codici QR",
            "tagline": "Genera codici QR per testo, URL, Wi-Fi o vCard. Dimensione, colori e correzione errori personalizzabili. Esporta PNG o SVG.",
            "description": "Generatore di codici QR gratuito online. Dimensione, colori e livelli di correzione errori personalizzabili. PNG o SVG senza filigrane.",
        },
        "pt": {
            "name": "Gerador de QR Code",
            "tagline": "Gere QR codes para qualquer texto, URL, Wi-Fi ou vCard. Tamanho, cores e correção de erro personalizáveis. Exporte como PNG ou SVG.",
            "description": "Gerador de QR code gratuito online. Tamanho, cores de foreground/background e níveis de correção de erro personalizáveis. Baixe como PNG ou SVG. Sem marca d'água.",
        },
        "pl": {
            "name": "Generator Kodów QR",
            "tagline": "Generuj kody QR dla dowolnego tekstu, URL-a, Wi-Fi albo vCard. Konfigurowalny rozmiar, kolory i korekcja błędów. Eksportuj PNG albo SVG.",
            "description": "Darmowy online generator kodów QR. Konfigurowalny rozmiar, kolory foreground/background i poziomy korekcji błędów. Pobierz jako PNG albo SVG. Bez znaków wodnych.",
        },
    },
    "body": """
<div class="tool-card">
  <label>{LBL_INPUT}</label>
  <textarea id="qr-input" placeholder="https://example.com" oninput="qrRender()">https://toolhub.software</textarea>
  <div class="row-2col" style="margin-top:1rem">
    <div>
      <label>Size (px)</label>
      <input type="number" id="qr-size" value="320" min="64" max="1024" step="32" oninput="qrRender()">
    </div>
    <div>
      <label>Error correction</label>
      <select id="qr-ec" onchange="qrRender()">
        <option value="L">L — 7%</option>
        <option value="M" selected>M — 15%</option>
        <option value="Q">Q — 25%</option>
        <option value="H">H — 30%</option>
      </select>
    </div>
  </div>
  <div class="row-2col" style="margin-top:1rem">
    <div>
      <label>Foreground</label>
      <input type="color" id="qr-fg" value="#000000" oninput="qrRender()" style="height:42px;padding:4px">
    </div>
    <div>
      <label>Background</label>
      <input type="color" id="qr-bg" value="#ffffff" oninput="qrRender()" style="height:42px;padding:4px">
    </div>
  </div>
  <div class="button-row">
    <button onclick="qrDownloadPng()">PNG</button>
    <button onclick="qrDownloadSvg()">SVG</button>
    <button class="secondary" onclick="qrPreset('wifi')">Wi-Fi preset</button>
    <button class="secondary" onclick="qrPreset('mailto')">Email preset</button>
    <button class="secondary" onclick="qrPreset('tel')">Phone preset</button>
  </div>
</div>
<div class="tool-card" style="text-align:center">
  <div id="qr-canvas" style="display:inline-block"></div>
  <div class="meta" id="qr-meta"></div>
</div>
""",
    "script": """
<script src="https://cdn.jsdelivr.net/npm/qrcode@1.5.4/build/qrcode.min.js"></script>
<script>
function qrRender(){
  const text = document.getElementById('qr-input').value || ' ';
  const size = parseInt(document.getElementById('qr-size').value, 10) || 320;
  const ec = document.getElementById('qr-ec').value;
  const fg = document.getElementById('qr-fg').value;
  const bg = document.getElementById('qr-bg').value;
  const wrap = document.getElementById('qr-canvas');
  wrap.innerHTML = '<canvas></canvas>';
  const canvas = wrap.querySelector('canvas');
  QRCode.toCanvas(canvas, text, {
    width: size,
    errorCorrectionLevel: ec,
    color: { dark: fg, light: bg },
    margin: 2,
  }, function(err){
    if (err){ document.getElementById('qr-meta').textContent = 'Error: ' + err.message; return; }
    document.getElementById('qr-meta').textContent = size + '×' + size + 'px · EC ' + ec + ' · ' + text.length + ' chars';
  });
}
function qrDownloadPng(){
  const canvas = document.querySelector('#qr-canvas canvas');
  if (!canvas) return;
  const a = document.createElement('a');
  a.download = 'qrcode.png';
  a.href = canvas.toDataURL('image/png');
  a.click();
}
function qrDownloadSvg(){
  const text = document.getElementById('qr-input').value || ' ';
  const ec = document.getElementById('qr-ec').value;
  const fg = document.getElementById('qr-fg').value;
  const bg = document.getElementById('qr-bg').value;
  QRCode.toString(text, { type: 'svg', errorCorrectionLevel: ec, color: { dark: fg, light: bg }, margin: 2 }, function(err, svg){
    if (err) return;
    const blob = new Blob([svg], {type: 'image/svg+xml'});
    const a = document.createElement('a');
    a.download = 'qrcode.svg';
    a.href = URL.createObjectURL(blob);
    a.click();
  });
}
function qrPreset(kind){
  const inp = document.getElementById('qr-input');
  if (kind === 'wifi') inp.value = 'WIFI:T:WPA;S:NetworkName;P:password;;';
  if (kind === 'mailto') inp.value = 'mailto:hello@example.com?subject=Hello';
  if (kind === 'tel') inp.value = 'tel:+421900000000';
  qrRender();
}
document.addEventListener('DOMContentLoaded', () => { setTimeout(qrRender, 100); });
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>QR codes are tiny URLs that a phone camera can read in a fraction of a second. Encode a URL, a Wi-Fi network, an email draft, a phone number, or any short text — print it on a poster, a business card, or a menu, and anyone with a phone can act on it without typing. This generator runs entirely in your browser using the open-source <a href="https://github.com/soldair/node-qrcode" rel="noopener">qrcode</a> library. Your input text never leaves the page.</p>

<h3>When to use it</h3>
<ul>
  <li>Sharing a URL on a slide, a poster, a business card, or a packaging insert.</li>
  <li>Letting guests join your Wi-Fi without typing the password (use the Wi-Fi preset).</li>
  <li>Putting "scan to pay / book / order" on signage in physical spaces.</li>
  <li>Encoding a vCard for instant contact-card import on the receiver's phone.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Error correction trades off with density.</strong> Higher levels (Q, H) survive scratches and overlaid logos; lower levels (L, M) keep the code small and faster to scan. Use <strong>H</strong> if you plan to overlay a logo, otherwise <strong>M</strong> is the sane default.</li>
  <li><strong>Contrast matters.</strong> Stylised QR codes with low foreground/background contrast often look pretty but scan poorly under bad light. Test by scanning from the printed/screen output before shipping.</li>
  <li><strong>Long content forces a denser code.</strong> If you must encode a 200-character URL, the resulting code is dense and harder to scan from far away. Shorten via a redirect first if size matters.</li>
  <li><strong>SVG vs PNG.</strong> SVG scales without quality loss — best for print or large displays. PNG is universally accepted but pixelates if scaled up; export at the size you'll use.</li>
  <li><strong>Wi-Fi preset format.</strong> <code>WIFI:T:WPA;S:&lt;SSID&gt;;P:&lt;password&gt;;;</code> — modern iOS/Android scan and join automatically; very old phones may not support it.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>QR codes são URLs minúsculos que a câmera de um celular consegue ler em uma fração de segundo. Codifique uma URL, uma rede Wi-Fi, um rascunho de e-mail, um número de telefone ou qualquer texto curto — imprima num pôster, num cartão de visita ou num cardápio, e qualquer pessoa com um celular pode agir sem digitar. Este gerador roda inteiramente no seu navegador usando a biblioteca open-source <a href="https://github.com/soldair/node-qrcode" rel="noopener">qrcode</a>. Seu texto de entrada nunca sai da página.</p>

<h3>Quando usar</h3>
<ul>
  <li>Compartilhar uma URL num slide, num pôster, num cartão de visita ou num inserto de embalagem.</li>
  <li>Deixar convidados entrarem no seu Wi-Fi sem digitar a senha (use o preset Wi-Fi).</li>
  <li>Colocar "scan to pay / book / order" em sinalização em espaços físicos.</li>
  <li>Codificar um vCard para importação instantânea de cartão de contato no celular do receptor.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Correção de erro tem trade-off com densidade.</strong> Níveis mais altos (Q, H) sobrevivem a arranhões e logos sobrepostos; níveis mais baixos (L, M) deixam o código menor e mais rápido de escanear. Use <strong>H</strong> se planeja sobrepor um logo, caso contrário <strong>M</strong> é o default sensato.</li>
  <li><strong>Contraste importa.</strong> QR codes estilizados com pouco contraste entre foreground e background ficam bonitos mas escaneiam mal sob luz ruim. Teste escaneando do output impresso/da tela antes de publicar.</li>
  <li><strong>Conteúdo longo força um código mais denso.</strong> Se você precisa codificar uma URL de 200 caracteres, o código resultante é denso e mais difícil de escanear de longe. Encurte com um redirect antes se o tamanho importar.</li>
  <li><strong>SVG vs PNG.</strong> SVG escala sem perda de qualidade — melhor para impressão ou displays grandes. PNG é universalmente aceito mas pixela se aumentar de escala; exporte no tamanho que vai usar.</li>
  <li><strong>Formato do preset Wi-Fi.</strong> <code>WIFI:T:WPA;S:&lt;SSID&gt;;P:&lt;senha&gt;;;</code> — iOS/Android modernos escaneiam e conectam automaticamente; celulares muito antigos podem não suportar.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Kody QR to maleńkie URL-e, które kamera telefonu czyta w ułamku sekundy. Zakoduj URL, sieć Wi-Fi, wersję roboczą maila, numer telefonu albo dowolny krótki tekst — wydrukuj na plakacie, wizytówce albo karcie menu i każdy z telefonem może coś z tym zrobić bez wpisywania. Ten generator działa w całości w przeglądarce, używając open-source'owej biblioteki <a href="https://github.com/soldair/node-qrcode" rel="noopener">qrcode</a>. Twój tekst nie opuszcza strony.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Udostępnianie URL-a na slajdzie, plakacie, wizytówce albo wkładce do opakowania.</li>
  <li>Łatwe dołączenie gości do twojego Wi-Fi bez wpisywania hasła (preset Wi-Fi).</li>
  <li>"Skanuj, żeby zapłacić / zarezerwować / zamówić" na oznakowaniu w przestrzeniach fizycznych.</li>
  <li>Kodowanie vCarda do natychmiastowego importu kontaktu na telefonie odbiorcy.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Korekcja błędów ma trade-off z gęstością.</strong> Wyższe poziomy (Q, H) przeżyją zarysowania i nałożone logo; niższe (L, M) trzymają kod mały i szybszy do skanowania. Używaj <strong>H</strong>, jeśli planujesz nakładać logo, w przeciwnym razie <strong>M</strong> to sensowny default.</li>
  <li><strong>Kontrast ma znaczenie.</strong> Stylizowane kody QR z niskim kontrastem foreground/background często ładnie wyglądają, ale słabo skanują w gorszym świetle. Przetestuj skanując z wydruku/ekranu, zanim ruszy.</li>
  <li><strong>Długa zawartość wymusza gęstszy kod.</strong> Jeśli musisz zakodować 200-znakowy URL, wynikowy kod jest gęsty i trudniej go zeskanować z daleka. Skróć przez redirect, jeśli rozmiar ma znaczenie.</li>
  <li><strong>SVG vs PNG.</strong> SVG skaluje się bez utraty jakości — najlepsze do druku albo dużych ekranów. PNG jest powszechnie akceptowany, ale piksel się rozbiega przy powiększaniu; eksportuj w docelowym rozmiarze.</li>
  <li><strong>Format presetu Wi-Fi.</strong> <code>WIFI:T:WPA;S:&lt;SSID&gt;;P:&lt;hasło&gt;;;</code> — nowoczesne iOS/Android skanują i łączą się automatycznie; bardzo stare telefony mogą nie wspierać.</li>
</ul>
""",
    },
    "related": ["url-encoder", "image-to-base64", "youtube-thumbnail"],
}
