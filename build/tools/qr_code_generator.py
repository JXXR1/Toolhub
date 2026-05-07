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
<h2>How it works</h2>
<p>Generated entirely in your browser using the open-source <a href="https://github.com/soldair/node-qrcode" rel="noopener">qrcode</a> library. Your input text never leaves the page.</p>
<h3>Tips</h3>
<ul>
  <li><strong>Error correction</strong>: higher levels survive more damage but make the code denser. Use <strong>H</strong> if you plan to overlay a logo.</li>
  <li><strong>Wi-Fi preset</strong>: format is <code>WIFI:T:WPA;S:&lt;SSID&gt;;P:&lt;password&gt;;;</code> — most modern phones scan and join automatically.</li>
  <li><strong>Contrast matters</strong>: if scanners struggle, increase contrast between foreground and background.</li>
  <li><strong>SVG</strong> scales to any size without quality loss — best for print or large displays.</li>
</ul>
""",
    },
    "related": ["url-encoder", "image-to-base64", "youtube-thumbnail"],
}
