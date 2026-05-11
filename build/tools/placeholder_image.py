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
        "pt": {"name": "Gerador de Imagem Placeholder", "tagline": "Gere imagens placeholder em SVG inline em qualquer tamanho com texto e cores personalizados. Saída como data URI ou SVG para download.", "description": "Gerador de imagens placeholder gratuito. Especifique width × height, texto do label e cores; receba um SVG inline para colar onde quiser — data URI, markup puro ou download. Roda inteiramente no seu navegador."},
        "pl": {"name": "Generator Placeholder Image", "tagline": "Generuj placeholderowe obrazki inline-SVG w dowolnym rozmiarze z własnym tekstem i kolorami. Wyjście jako data URI albo SVG do pobrania.", "description": "Darmowy generator placeholder imageów. Podaj width × height, tekst labela i kolory; dostaniesz inline-SVG do wklejenia gdziekolwiek — data URI, surowy markup albo download. Działa w całości w przeglądarce."},
        "ja": {"name": "プレースホルダー画像ジェネレーター", "tagline": "任意のサイズで、テキストや色をカスタムしたインライン SVG プレースホルダー画像を生成。data URI または SVG ダウンロードで出力。", "description": "無料のプレースホルダー画像ジェネレーター。横×高さ、ラベルテキスト、配色を指定し、貼り付けに使えるインライン SVG（data URI、生のマークアップ、ダウンロード）を取得できます。すべてブラウザ内で動作します。"},
        "nl": {"name": "Placeholder Image Generator", "tagline": "Genereer inline-SVG placeholder images op elke size met custom tekst en kleuren. Output als data URI of downloadbaar SVG.", "description": "Gratis placeholder image-generator. Specificeer width × height, labeltekst en kleuren; krijg een inline SVG die je overal kunt plakken — data URI, raw markup of download. Draait volledig in je browser."},
        "tr": {"name": "Placeholder Görsel Üretici", "tagline": "Özel metin ve renklerle her boyutta inline-SVG placeholder görseller üret. Data URI veya indirilebilir SVG olarak çıkar.", "description": "Ücretsiz placeholder görsel üretici. Genişlik × yükseklik, etiket metni ve renkleri belirle; her yere yapıştırabileceğin inline SVG al — data URI, ham işaretleme veya indirme. Tamamen tarayıcında çalışır."},
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
        "pt": """
<h2>Para que serve?</h2>
<p>Enquanto você desenha uma página, frequentemente precisa de uma imagem de tamanho específico antes da imagem real estar pronta — um banner hero, uma thumbnail de card, um avatar, um card OG. Carregar <code>via.placeholder.com</code> ou <code>placehold.co</code> funciona mas adiciona uma requisição externa e uma dependência de terceiro. Esta ferramenta produz um SVG inline autocontido com o tamanho e label que você quer, pronto para colar no seu HTML, no <code>background-image</code> CSS, ou num componente React como data URI. Nada sai do seu navegador.</p>

<h3>Quando usar</h3>
<ul>
  <li>Fazendo wireframe de um layout onde você precisa de placeholders com formato antes dos assets reais ficarem prontos.</li>
  <li>Montando um Storybook ou export do Figma e precisando de gráficos placeholder por componente.</li>
  <li>Testando código de carregamento de imagem, thresholds de lazy-loading ou CSS de aspect-ratio.</li>
  <li>Substituindo um serviço placeholder de terceiros num projeto que precisa funcionar offline ou sob CSP rigoroso.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>SVG não é raster.</strong> A data URI é uma string SVG; ela escala infinitamente sem blur, mas um designer esperando um PNG pode não esperar isso. Para uma imagem raster, tire um screenshot do preview ou rode o SVG num conversor SVG-to-PNG.</li>
  <li><strong>Data URIs longos são desconfortáveis em <code>img src</code>.</strong> Browsers lidam, mas ferramentas (linters, search-and-replace, diff tools) muitas vezes engasgam com valores de atributo de vários KB. Para mockups grandes, prefira o download do arquivo SVG.</li>
  <li><strong>O texto do label não é localizado.</strong> O auto-label é "WxH" com o sinal de multiplicação; se precisar de tradução, digite um label customizado.</li>
  <li><strong>Cores são apenas hex HTML.</strong> Os color pickers produzem <code>#rrggbb</code>. Se precisar de <code>rgba()</code>, edite o markup do SVG diretamente depois de copiar.</li>
  <li><strong>Width/height são intrínsecos, não de display.</strong> Definir CSS para um tamanho diferente vai escalar o SVG — visualmente ok, mas o texto embutido pode parecer esticado se o aspect ratio mudar; usamos <code>preserveAspectRatio="none"</code> para escala previsível.</li>
  <li><strong>Não publique o placeholder.</strong> Fácil de esquecer — substitua pelo asset real antes do go-live.</li>
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
        "pl": """
<h2>Do czego to służy?</h2>
<p>Projektując stronę często potrzebujesz obrazka o konkretnym rozmiarze, zanim prawdziwy obrazek będzie gotowy — hero banner, miniaturka karty, awatar, OG card. Wczytanie <code>via.placeholder.com</code> albo <code>placehold.co</code> działa, ale dodaje zewnętrzny request i zewnętrzną zależność. To narzędzie produkuje samowystarczalny inline SVG z rozmiarem i labelem, jakiego chcesz, gotowy do wrzucenia w HTML, CSS-owy <code>background-image</code> albo komponent React jako data URI. Nic nie opuszcza przeglądarki.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Wireframing layoutu, gdzie potrzebujesz placeholderów w kształcie zanim prawdziwe assety są gotowe.</li>
  <li>Budowa Storybooka albo eksportu z Figmy, potrzebujesz placeholderowej grafiki per komponent.</li>
  <li>Testowanie kodu ładowania obrazków, progów lazy-loadingu albo CSS aspect-ratio.</li>
  <li>Zastąpienie zewnętrznego placeholder service w projekcie, który musi działać offline albo pod restrykcyjnym CSP.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>SVG ≠ raster.</strong> Data URI to string SVG; skaluje się bez końca bez bluru, ale designer oczekujący PNG może oczekiwać czego innego. Po obrazek raster zrób screen z preview albo przepuść SVG przez konwerter SVG-to-PNG.</li>
  <li><strong>Długie data URI są niewygodne w <code>img src</code>.</strong> Przeglądarki je trawią, ale narzędzia (lintery, search-and-replace, diff toole) często krztuszą się wielokilobajtowymi wartościami atrybutów. Dla dużych mockupów wybieraj download SVG.</li>
  <li><strong>Tekst labela nie jest lokalizowany.</strong> Auto-label to "WxH" ze znakiem mnożenia; jeśli potrzebujesz tłumaczenia, wpisz custom label.</li>
  <li><strong>Kolory tylko HTML hex.</strong> Color pickery produkują <code>#rrggbb</code>. Jeśli chcesz <code>rgba()</code>, edytuj markup SVG po skopiowaniu.</li>
  <li><strong>Width/height są intrinsic, nie display.</strong> Ustawienie CSS na inny rozmiar przeskaluje SVG — wizualnie OK, ale osadzony tekst może wyglądać rozciągnięty, jeśli aspect ratio się zmieni; używamy <code>preserveAspectRatio="none"</code> dla przewidywalnego skalowania.</li>
  <li><strong>Nie wysyłaj placeholdera na produkcję.</strong> Łatwo zapomnieć — podmień na prawdziwy asset przed go-live.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>ページ設計中、本物の画像が用意される前に特定サイズの画像が必要になる場面はよくあります。ヒーローバナー、カードのサムネイル、アバター、OG カードなど。<code>via.placeholder.com</code> や <code>placehold.co</code> も使えますが、外部リクエストとサードパーティ依存が増えます。本ツールは指定サイズとラベルを持つ自己完結型のインライン SVG を生成し、HTML、CSS の <code>background-image</code>、React コンポーネントの data URI などにそのまま貼り付けられます。データはブラウザの外に出ません。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>本物のアセットが揃う前に、形のあるプレースホルダでワイヤーフレームを作りたいとき。</li>
  <li>Storybook や Figma エクスポートで、コンポーネントごとのプレースホルダ画像が必要なとき。</li>
  <li>画像読み込みコード、レイジーロードのしきい値、aspect-ratio CSS をテストしたいとき。</li>
  <li>厳しい CSP やオフライン要件のあるプロジェクトで、外部のプレースホルダサービスを置き換えたいとき。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>SVG はラスタではありません。</strong> data URI は SVG 文字列で、無限に拡大しても滲みませんが、デザイナーが PNG を期待しているとは限りません。ラスタが必要ならプレビューを画面キャプチャするか、SVG→PNG コンバータを使ってください。</li>
  <li><strong>長い data URI は <code>img src</code> に貼ると扱いにくいです。</strong> ブラウザは扱えますが、リンタや検索置換、diff ツールが詰まることがあります。大きなモックアップでは SVG ファイルでのダウンロードを推奨します。</li>
  <li><strong>ラベルテキストはローカライズされません。</strong> 自動ラベルは「WxH」（×は乗算記号）です。翻訳が必要ならカスタム文字列を入力してください。</li>
  <li><strong>色は HTML の hex のみ。</strong> カラーピッカーは <code>#rrggbb</code> を返します。<code>rgba()</code> が必要ならコピー後に SVG マークアップを直接編集してください。</li>
  <li><strong>幅・高さは intrinsic で、display ではありません。</strong> CSS で別サイズに指定すると SVG はスケールされます。アスペクト比が変わるとテキストが伸縮して見えるため、予測可能なスケーリングのために <code>preserveAspectRatio="none"</code> を使用しています。</li>
  <li><strong>本番にプレースホルダを残さないこと。</strong> 忘れがちなので、公開前に実アセットへ差し替えてください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Tijdens het ontwerpen van een pagina heb je vaak een afbeelding op een specifieke size nodig voordat de echte image klaar is — een hero-banner, een card-thumbnail, een avatar, een OG-card. <code>via.placeholder.com</code> of <code>placehold.co</code> laden werkt maar voegt een extern request en een third-party dependency toe. Deze tool produceert een zelfstandige inline SVG met de size en label die je wil, klaar om in je HTML, CSS <code>background-image</code> of React-component als data URI te droppen. Niets verlaat je browser.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een layout wireframen waar je shaped placeholders nodig hebt voor de echte assets klaar zijn.</li>
  <li>Een Storybook of Figma-export bouwen en per-component placeholder graphics nodig hebben.</li>
  <li>Image-loading code, lazy-loading thresholds of aspect-ratio CSS testen.</li>
  <li>Een third-party placeholder-service vervangen in een project dat offline of onder strikte CSP moet werken.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>SVG ≠ raster.</strong> De data URI is een SVG-string; hij schaalt oneindig zonder blur maar een designer die een PNG verwacht niet. Voor een raster-image screenshot je de preview of draai je de SVG door een SVG-naar-PNG converter.</li>
  <li><strong>Lange data URIs zijn omslachtig in <code>img src</code>.</strong> Browsers handelen ze af, maar tools (linters, search-and-replace, diff-tools) verslikken zich vaak in multi-KB attribute-values. Voor grote mockups prefereer de SVG-file-download.</li>
  <li><strong>Labeltekst is niet gelokaliseerd.</strong> Het auto-label is "WxH" met het maaltteken; als je een vertaling nodig hebt, type een custom label.</li>
  <li><strong>Kleuren zijn alleen HTML-hex.</strong> De kleurkiezers produceren <code>#rrggbb</code>. Als je <code>rgba()</code> nodig hebt, bewerk de SVG-markup direct na kopiëren.</li>
  <li><strong>Width/height zijn intrinsiek, niet display.</strong> CSS op een andere size zetten zal de SVG schalen — visueel prima, maar de embedded tekst kan stretched lijken als de aspect ratio verandert; we gebruiken <code>preserveAspectRatio="none"</code> voor voorspelbare scaling.</li>
  <li><strong>Ship de placeholder niet.</strong> Makkelijk te vergeten — vervang met het echte asset voor je live gaat.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Bir sayfa tasarlarken, gerçek görsel hazır olmadan önce sıklıkla belirli boyutta bir görsele ihtiyacın olur — hero banner, kart thumbnail, avatar, OG kartı. <code>via.placeholder.com</code> veya <code>placehold.co</code> yüklemek çalışır ama harici bir istek ve üçüncü taraf bağımlılığı ekler. Bu araç istediğin boyut ve etiketle kendi kendine yeten inline SVG üretir, HTML'ine, CSS <code>background-image</code>'ına veya React bileşenine data URI olarak bırakmaya hazır. Hiçbir şey tarayıcını terk etmez.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Gerçek varlıklar hazır olmadan önce şekilli placeholder'lara ihtiyaç duyduğun bir layout için wireframe yapma.</li>
  <li>Bir Storybook veya Figma export kurma ve bileşen başına placeholder grafiğine ihtiyaç duyma.</li>
  <li>Görsel yükleme kodunu, lazy-loading eşiklerini veya en-boy oranı CSS'ini test etme.</li>
  <li>Çevrimdışı çalışması veya katı CSP altında çalışması gereken bir projedeki üçüncü taraf placeholder servisini değiştirme.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>SVG ≠ raster.</strong> Data URI bir SVG string'idir; sonsuza kadar bulanıklık olmadan ölçeklenir ama PNG bekleyen bir tasarımcı beklemeyebilir. Raster görsel için önizlemenin ekran görüntüsünü al veya SVG'yi bir SVG-to-PNG dönüştürücüden geçir.</li>
  <li><strong>Uzun data URI'lar <code>img src</code>'de zahmetlidir.</strong> Tarayıcılar bunları işler, ancak araçlar (linter'lar, search-and-replace, diff araçları) sıklıkla çok-KB nitelik değerlerinde tıkanır. Büyük mockup'lar için SVG dosya indirmesini tercih et.</li>
  <li><strong>Etiket metni yerelleştirilmemiştir.</strong> Otomatik etiket çarpma işareti ile "WxH"dir; çeviri gerekiyorsa özel bir etiket yaz.</li>
  <li><strong>Renkler sadece HTML hex'tir.</strong> Renk seçiciler <code>#rrggbb</code> üretir. <code>rgba()</code> gerekiyorsa, kopyaladıktan sonra SVG markup'ını doğrudan düzenle.</li>
  <li><strong>Genişlik/yükseklik içseldir, display değildir.</strong> CSS'i farklı bir boyuta ayarlamak SVG'yi ölçeklendirir — görsel olarak iyi, ama en-boy oranı değişirse gömülü metin gerilmiş görünebilir.</li>
  <li><strong>Placeholder'ı gönderme.</strong> Unutmak kolaydır — yayına geçmeden önce gerçek varlıkla değiştir.</li>
</ul>
""",
    },
    "related": ["color-picker", "color-converter", "image-to-base64", "qr-code-generator"],
    "howto": {"flow": "generate",  "action": "generate","noun": "image"},
}
