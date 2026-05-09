TOOL = {
    "slug": "placeholder-image",
    "category": "design",
    "icon": "🖼",
    "tags": ["placeholder", "image", "svg", "mockup", "wireframe", "data uri"],
    "i18n": {
        "en": {
            "name": "Placeholder Image Generator",
            "tagline": "Generate inline-SVG placeholder images at any size with custom text and colours. Output as data URI or downloadable SVG.",
            "description": "Free placeholder image generator. Specify width × height, label text, and colours; get an inline SVG you can paste anywhere — data URI, raw markup, or download. Runs entirely in your browser.",
        },
        "de": {"name": "Platzhalter-Bild-Generator", "tagline": "Inline-SVG-Platzhalterbilder in beliebiger Größe mit eigenem Text und Farben. Als Data-URI oder SVG-Download.", "description": "Kostenloser Platzhalterbild-Generator. Breite × Höhe, Beschriftung und Farben angeben; bekomme inline-SVG zum Einfügen — Data-URI, Rohcode oder Download. Komplett im Browser."},
        "es": {"name": "Generador de Imagen Placeholder", "tagline": "Genera imágenes SVG placeholder de cualquier tamaño con texto y colores personalizados. Salida como data URI o SVG descargable.", "description": "Generador de imágenes placeholder gratuito. Especifica ancho × alto, texto y colores; obtén un SVG inline que pegas donde quieras — data URI, marcado o descarga. 100% en el navegador."},
        "fr": {"name": "Générateur d'Image Placeholder", "tagline": "Générez des images SVG placeholder de toute taille avec texte et couleurs personnalisés. Sortie en data URI ou SVG téléchargeable.", "description": "Générateur d'images placeholder gratuit. Spécifiez largeur × hauteur, texte et couleurs ; obtenez un SVG inline à coller — data URI, balisage ou téléchargement. 100% dans le navigateur."},
        "it": {"name": "Generatore Immagine Placeholder", "tagline": "Genera immagini SVG placeholder di qualsiasi dimensione con testo e colori personalizzati. Output come data URI o SVG scaricabile.", "description": "Generatore di immagini placeholder gratuito. Specifica larghezza × altezza, testo e colori; ottieni un SVG inline da incollare — data URI, markup o download. 100% nel browser."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Width (px)</label>
      <input type="number" id="ph-w" min="1" max="4096" value="600" oninput="phRun()">
    </div>
    <div>
      <label>Height (px)</label>
      <input type="number" id="ph-h" min="1" max="4096" value="400" oninput="phRun()">
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Background colour</label>
      <input type="color" id="ph-bg" value="#cccccc" oninput="phRun()" style="height:42px;padding:2px">
    </div>
    <div>
      <label>Text colour</label>
      <input type="color" id="ph-fg" value="#444444" oninput="phRun()" style="height:42px;padding:2px">
    </div>
  </div>
  <div style="margin-top:0.7rem">
    <label>Label text (leave blank for "WxH")</label>
    <input type="text" id="ph-text" oninput="phRun()" placeholder="600 × 400" maxlength="80">
  </div>
</div>
<div class="tool-card">
  <label>Preview</label>
  <div id="ph-preview" style="background:repeating-conic-gradient(#0001 0 25%, transparent 0 50%) 0 0/16px 16px;padding:1rem;display:flex;align-items:center;justify-content:center;border:1px solid var(--border);border-radius:6px;min-height:160px;overflow:auto"></div>
</div>
<div class="tool-card">
  <label>SVG markup</label>
  <div class="output-row">
    <pre class="output" id="ph-svg" style="margin:0;flex:1;max-height:160px;overflow:auto"></pre>
    <button class="copy-btn secondary" onclick="copyOutput('ph-svg', this)">{LBL_COPY}</button>
  </div>
</div>
<div class="tool-card">
  <label>Data URI</label>
  <div class="output-row">
    <pre class="output" id="ph-uri" style="margin:0;flex:1;max-height:140px;overflow:auto"></pre>
    <button class="copy-btn secondary" onclick="copyOutput('ph-uri', this)">{LBL_COPY}</button>
  </div>
</div>
<div class="tool-card">
  <label>Download</label>
  <div class="button-row">
    <button onclick="phDownload()">{LBL_DOWNLOAD} SVG</button>
  </div>
</div>
""",
    "script": """
<script>
function phEsc(s){ return String(s).replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c])); }

function phBuildSvg(){
  const w = Math.max(1, Math.min(4096, parseInt(document.getElementById('ph-w').value, 10) || 1));
  const h = Math.max(1, Math.min(4096, parseInt(document.getElementById('ph-h').value, 10) || 1));
  const bg = document.getElementById('ph-bg').value;
  const fg = document.getElementById('ph-fg').value;
  let label = document.getElementById('ph-text').value || (w + ' \\u00d7 ' + h);
  // Pick a sensible font size
  const minDim = Math.min(w, h);
  const fontSize = Math.max(10, Math.round(minDim * 0.18));
  return `<svg xmlns="http://www.w3.org/2000/svg" width="${w}" height="${h}" viewBox="0 0 ${w} ${h}" preserveAspectRatio="none"><rect width="${w}" height="${h}" fill="${bg}"/><text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="-apple-system,BlinkMacSystemFont,Segoe UI,sans-serif" font-size="${fontSize}" fill="${fg}">${phEsc(label)}</text></svg>`;
}

function phRun(){
  const svg = phBuildSvg();
  document.getElementById('ph-svg').textContent = svg;
  const uri = 'data:image/svg+xml;utf8,' + encodeURIComponent(svg);
  document.getElementById('ph-uri').textContent = uri;
  const preview = document.getElementById('ph-preview');
  preview.innerHTML = '';
  const img = document.createElement('img');
  img.src = uri;
  img.alt = 'Preview';
  img.style.maxWidth = '100%';
  img.style.height = 'auto';
  preview.appendChild(img);
}

function phDownload(){
  const svg = phBuildSvg();
  const w = document.getElementById('ph-w').value;
  const h = document.getElementById('ph-h').value;
  const blob = new Blob([svg], {type: 'image/svg+xml'});
  const a = document.createElement('a');
  a.href = URL.createObjectURL(blob);
  a.download = `placeholder-${w}x${h}.svg`;
  document.body.appendChild(a);
  a.click();
  setTimeout(() => { URL.revokeObjectURL(a.href); a.remove(); }, 100);
}

document.addEventListener('DOMContentLoaded', phRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>While designing a page, you often need an image of a specific size before the real image is ready — a hero banner, a card thumbnail, an avatar, an OG card. Loading <code>via.placeholder.com</code> or <code>placehold.co</code> works but adds an external request and a third-party dependency. This tool produces a self-contained inline SVG with the size and label you want, ready to drop into your HTML, CSS <code>background-image</code>, or React component as a data URI. Nothing leaves your browser.</p>

<h3>When to use it</h3>
<ul>
  <li>Wire-framing a layout where you need shaped placeholders before the real assets are ready.</li>
  <li>Building a Storybook or Figma export and needing per-component placeholder graphics.</li>
  <li>Testing image-loading code, lazy-loading thresholds, or aspect-ratio CSS.</li>
  <li>Replacing a third-party placeholder service in a project that needs to work offline or under strict CSP.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>SVG ≠ raster.</strong> The data URI is an SVG string; it scales infinitely without blur but a designer expecting a PNG may not. For a raster image, screenshot the preview or run the SVG through an SVG-to-PNG converter.</li>
  <li><strong>Long data URIs are awkward in <code>img src</code>.</strong> Browsers handle them, but tools (linters, search-and-replace, diff tools) often choke on multi-KB attribute values. For large mockups, prefer the SVG file download.</li>
  <li><strong>Label text is not localised.</strong> The auto-label is "WxH" with the multiplication sign; if you need a translation, type a custom label.</li>
  <li><strong>Colours are HTML hex only.</strong> The colour pickers produce <code>#rrggbb</code>. If you need <code>rgba()</code>, edit the SVG markup directly after copying.</li>
  <li><strong>Width/height are intrinsic, not display.</strong> Setting CSS to a different size will scale the SVG — visually fine, but the embedded text may look stretched if the aspect ratio changes; we use <code>preserveAspectRatio="none"</code> for predictable scaling.</li>
  <li><strong>Don't ship the placeholder.</strong> Easy to forget — replace with the real asset before going live.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>Beim Layouten braucht man oft Bilder einer bestimmten Größe, bevor das echte Asset fertig ist. Externe Dienste wie <code>via.placeholder.com</code> funktionieren, fügen aber einen externen Request hinzu. Dieses Tool liefert ein eigenständiges Inline-SVG mit Größe und Label deiner Wahl — als Data-URI oder Download. Nichts verlässt den Browser.</p>
<h3>Wann verwenden</h3>
<ul>
<li>Wireframe-Layouts vor Asset-Lieferung.</li>
<li>Storybook-/Figma-Exporte mit Platzhaltern.</li>
<li>Lazy-Loading oder Aspect-Ratio-CSS testen.</li>
<li>Externen Placeholder-Service in CSP-strikten Projekten ersetzen.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>SVG ist kein Raster.</strong> Für PNG: Screenshot oder Konverter.</li>
<li><strong>Lange Data-URIs sind unhandlich</strong> in Tools/Diffs — bei großen Mockups SVG-Download bevorzugen.</li>
<li><strong>Auto-Label ist nicht übersetzt.</strong> Bei Bedarf eigenen Text eingeben.</li>
<li><strong>Farben nur als HTML-Hex.</strong> Für rgba() SVG nachträglich bearbeiten.</li>
<li><strong>Größe ist intrinsisch.</strong> CSS-Skalierung mit <code>preserveAspectRatio="none"</code>.</li>
<li><strong>Nicht in Produktion vergessen.</strong></li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>Al diseñar una página, a menudo necesitas una imagen de tamaño específico antes de tener el asset real. Servicios como <code>via.placeholder.com</code> añaden una petición externa. Esta herramienta produce un SVG inline autocontenido con el tamaño y etiqueta que quieras — data URI o descarga. Nada sale de tu navegador.</p>
<h3>Cuándo usarlo</h3>
<ul>
<li>Wireframes antes de los assets reales.</li>
<li>Storybook/Figma con placeholders por componente.</li>
<li>Probar lazy-loading o CSS de aspect-ratio.</li>
<li>Reemplazar servicio externo en proyectos con CSP estricta.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>SVG no es raster.</strong> Para PNG: captura o conversor.</li>
<li><strong>Data URIs largas son incómodas</strong> en herramientas/diffs — prefiere descarga para mockups grandes.</li>
<li><strong>La etiqueta auto no se localiza.</strong> Escribe texto custom si lo necesitas.</li>
<li><strong>Colores solo en hex HTML.</strong> Para rgba() edita el SVG.</li>
<li><strong>El tamaño es intrínseco.</strong> Escalado CSS con <code>preserveAspectRatio="none"</code>.</li>
<li><strong>No lo dejes en producción.</strong></li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>En conception de page, on a souvent besoin d'une image d'une taille précise avant l'asset final. Les services comme <code>via.placeholder.com</code> ajoutent une requête externe. Cet outil produit un SVG inline autonome avec la taille et l'étiquette voulues — data URI ou téléchargement. Rien ne quitte le navigateur.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>Wireframes avant assets réels.</li>
<li>Exports Storybook/Figma avec placeholders.</li>
<li>Tester lazy-loading ou CSS d'aspect-ratio.</li>
<li>Remplacer un service externe dans des projets à CSP strict.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>SVG n'est pas raster.</strong> Pour PNG : capture ou convertisseur.</li>
<li><strong>Les longues data URIs sont gênantes</strong> dans les outils/diffs — préférer le téléchargement pour de gros mockups.</li>
<li><strong>L'étiquette auto n'est pas localisée.</strong> Saisir un texte custom si besoin.</li>
<li><strong>Couleurs en hex HTML uniquement.</strong> Pour rgba() éditer le SVG.</li>
<li><strong>La taille est intrinsèque.</strong> Mise à l'échelle CSS avec <code>preserveAspectRatio="none"</code>.</li>
<li><strong>Ne pas laisser en production.</strong></li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>Nel progettare una pagina serve spesso un'immagine di una certa dimensione prima dell'asset reale. Servizi come <code>via.placeholder.com</code> aggiungono una richiesta esterna. Questo strumento produce un SVG inline autonomo con dimensione ed etichetta a piacere — data URI o download. Nulla lascia il browser.</p>
<h3>Quando usarlo</h3>
<ul>
<li>Wireframe prima degli asset reali.</li>
<li>Export Storybook/Figma con placeholder.</li>
<li>Testare lazy-loading o CSS aspect-ratio.</li>
<li>Sostituire servizi esterni in progetti con CSP rigido.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>SVG non è raster.</strong> Per PNG: screenshot o convertitore.</li>
<li><strong>Data URI lunghe sono scomode</strong> in tool/diff — meglio il download per mockup grandi.</li>
<li><strong>L'etichetta auto non è localizzata.</strong> Inserisci testo custom.</li>
<li><strong>Colori solo hex HTML.</strong> Per rgba() modifica l'SVG.</li>
<li><strong>La dimensione è intrinseca.</strong> Scalatura CSS con <code>preserveAspectRatio="none"</code>.</li>
<li><strong>Non lasciare in produzione.</strong></li>
</ul>
""",
    },
    "related": ["color-picker", "color-converter", "image-to-base64", "qr-code-generator"],
}
