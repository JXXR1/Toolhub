TOOL = {
    "slug": "og-tag-preview",
    "category": "design",
    "icon": "🪟",
    "tags": ["og", "open graph", "twitter", "facebook", "linkedin", "discord", "preview", "social"],
    "i18n": {
        "en": {
            "name": "OG Tag Preview",
            "tagline": "Paste OG meta tags or fill title/description/image — preview share cards as they look on Twitter/X, Facebook, LinkedIn, and Discord.",
            "description": "Free Open Graph tag preview. Paste your <meta> tags or just fill in title/description/image and see how your link will render in Twitter/X, Facebook, LinkedIn, and Discord share previews. Runs entirely in your browser.",
        },
        "de": {"name": "OG-Tag-Vorschau", "tagline": "OG-Meta-Tags einfügen oder Titel/Beschreibung/Bild ausfüllen — Vorschau für Twitter/X, Facebook, LinkedIn und Discord.", "description": "Kostenlose Open-Graph-Tag-Vorschau. <meta>-Tags einfügen oder Titel/Beschreibung/Bild ausfüllen und sehen, wie der Link auf Twitter/X, Facebook, LinkedIn und Discord aussieht. Komplett im Browser."},
        "es": {"name": "Vista Previa de Etiquetas OG", "tagline": "Pega meta-tags OG o rellena título/descripción/imagen — previsualiza tarjetas de Twitter/X, Facebook, LinkedIn y Discord.", "description": "Vista previa Open Graph gratuita. Pega tus <meta> tags o rellena título/descripción/imagen y mira cómo se verá tu enlace en Twitter/X, Facebook, LinkedIn y Discord. 100% en el navegador."},
        "fr": {"name": "Aperçu des Balises OG", "tagline": "Collez des balises meta OG ou remplissez titre/description/image — aperçu des cartes Twitter/X, Facebook, LinkedIn et Discord.", "description": "Aperçu Open Graph gratuit. Collez vos balises <meta> ou remplissez titre/description/image et voyez le rendu sur Twitter/X, Facebook, LinkedIn et Discord. 100% dans le navigateur."},
        "it": {"name": "Anteprima Tag OG", "tagline": "Incolla meta tag OG o riempi titolo/descrizione/immagine — anteprima delle card Twitter/X, Facebook, LinkedIn e Discord.", "description": "Anteprima Open Graph gratuita. Incolla i tuoi <meta> tag o riempi titolo/descrizione/immagine e vedi come apparirà il link su Twitter/X, Facebook, LinkedIn e Discord. 100% nel browser."},
        "pt": {"name": "Preview de Tags OG", "tagline": "Cole meta tags OG ou preencha título/descrição/imagem — visualize os share cards como aparecem no Twitter/X, Facebook, LinkedIn e Discord.", "description": "Preview de Open Graph tags gratuito. Cole seus <meta> tags ou preencha título/descrição/imagem e veja como seu link vai renderizar nos previews de compartilhamento do Twitter/X, Facebook, LinkedIn e Discord. Roda inteiramente no seu navegador."},
        "pl": {"name": "Podgląd Tagów OG", "tagline": "Wklej meta tagi OG albo wpisz title/description/image — zobacz, jak share cardy wyglądają na Twitter/X, Facebook, LinkedIn i Discord.", "description": "Darmowy podgląd Open Graph tagów. Wklej swoje <meta> tagi albo po prostu wpisz title/description/image i zobacz, jak twój link wyrenderuje się w podglądach udostępnień na Twitter/X, Facebook, LinkedIn i Discord. Działa w całości w przeglądarce."},
        "ja": {"name": "OG タグプレビュー", "tagline": "OG メタタグを貼るか、タイトル／説明／画像を入力すると、Twitter/X、Facebook、LinkedIn、Discord のシェアカードを確認できます。", "description": "無料の Open Graph タグプレビュー。<meta> タグの貼り付けか、タイトル／説明／画像の入力で、リンクが Twitter/X、Facebook、LinkedIn、Discord でどう見えるかを確認できます。すべてブラウザ内で動作します。"},
        "nl": {"name": "OG Tag Preview", "tagline": "Plak OG meta tags of vul title/description/image — preview share cards zoals ze er op Twitter/X, Facebook, LinkedIn en Discord uitzien.", "description": "Gratis Open Graph tag preview. Plak je <meta>-tags of vul gewoon title/description/image in en zie hoe je link zal renderen in Twitter/X, Facebook, LinkedIn en Discord share-previews. Draait volledig in je browser."},
        "tr": {"name": "OG Tag Önizleme", "tagline": "OG meta tag'lerini yapıştır veya title/description/image doldur — paylaşım kartlarını Twitter/X, Facebook, LinkedIn ve Discord'da nasıl görüneceği gibi önizle.", "description": "Ücretsiz Open Graph tag önizleme. <meta> tag'lerini yapıştır veya sadece title/description/image doldur ve linkinin Twitter/X, Facebook, LinkedIn ve Discord paylaşım önizlemelerinde nasıl görüneceğini gör. Tamamen tarayıcında çalışır."},
        "id": {"name": "Pratinjau OG Tag", "tagline": "Tempel meta tag OG atau isi title/description/image — pratinjau kartu sosial seperti yang muncul di Twitter/X, Facebook, LinkedIn, dan Discord.", "description": "Pratinjau tag Open Graph gratis. Tempel meta tag dari HTML atau isi field, dan lihat seperti apa pratinjau link-mu di Twitter/X, Facebook, LinkedIn, dan Discord. Bantu pastikan kartu sosial-mu terlihat benar sebelum dipublikasikan."},
        "vi": {"name": "Xem trước OG Tag", "tagline": "Dán OG meta tag hoặc điền title/description/image — xem trước social card như chúng xuất hiện trên Twitter/X, Facebook, LinkedIn và Discord.", "description": "Trình xem trước Open Graph miễn phí trực tuyến. Dán OG meta tag hoặc điền các trường thủ công và xem chính xác cách thẻ social-share xuất hiện trên Twitter/X, Facebook, LinkedIn và Discord."},
    },
    "body": """
<div class="tool-card">
  <label>Paste meta tags (optional — fields below are filled from this if provided)</label>
  <textarea id="og-html" oninput="ogParse()" spellcheck="false" placeholder='<meta property="og:title" content="My Page">&#10;<meta property="og:description" content="A short description.">&#10;<meta property="og:image" content="https://example.com/og.png">&#10;<meta property="og:url" content="https://example.com/page">' style="min-height:120px"></textarea>
</div>
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Title</label>
      <input type="text" id="og-title" oninput="ogRender()" placeholder="Page title" value="Toolhub — 60 free privacy-first developer tools">
    </div>
    <div>
      <label>Site URL</label>
      <input type="text" id="og-url" oninput="ogRender()" placeholder="https://example.com/page" value="https://toolhub.software/">
    </div>
  </div>
  <div style="margin-top:0.7rem">
    <label>Description</label>
    <textarea id="og-desc" oninput="ogRender()" rows="3" placeholder="Short description">Format JSON, decode JWTs, build cron schedules, and dozens more — all client-side, no data leaves your browser.</textarea>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Image URL</label>
      <input type="text" id="og-image" oninput="ogRender()" placeholder="https://example.com/og-image.png" value="https://toolhub.software/og-image.png">
    </div>
    <div>
      <label>Site name</label>
      <input type="text" id="og-site" oninput="ogRender()" placeholder="example.com" value="toolhub.software">
    </div>
  </div>
</div>
<div class="tool-card">
  <label>Twitter / X (summary_large_image)</label>
  <div id="og-twitter" class="og-card og-twitter"></div>
</div>
<div class="tool-card">
  <label>Facebook</label>
  <div id="og-facebook" class="og-card og-facebook"></div>
</div>
<div class="tool-card">
  <label>LinkedIn</label>
  <div id="og-linkedin" class="og-card og-linkedin"></div>
</div>
<div class="tool-card">
  <label>Discord</label>
  <div id="og-discord" class="og-card og-discord"></div>
</div>
""",
    "script": """
<style>
.og-card { border-radius: 10px; overflow: hidden; max-width: 540px; }
.og-img { width: 100%; aspect-ratio: 1.91 / 1; background: #2228 center/cover no-repeat; display:flex;align-items:center;justify-content:center;color:#888;font-size:0.85rem; }
.og-img-empty::after { content: '(no image)'; }

.og-twitter { background: var(--surface); border: 1px solid var(--border); }
.og-twitter .og-body { padding: 0.65rem 0.85rem; }
.og-twitter .og-host { color: var(--text-muted); font-size: 0.8rem; margin-bottom: 0.15rem; }
.og-twitter .og-title { color: var(--text); font-size: 0.95rem; font-weight: 600; line-height: 1.25; }
.og-twitter .og-desc { color: var(--text-muted); font-size: 0.85rem; margin-top: 0.2rem; line-height: 1.35; max-height: 2.7em; overflow: hidden; }

.og-facebook { background: var(--surface); border: 1px solid var(--border); }
.og-facebook .og-body { padding: 0.65rem 0.85rem; background: var(--card-hover); }
.og-facebook .og-host { color: var(--text-muted); font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.04em; margin-bottom: 0.2rem; }
.og-facebook .og-title { color: var(--text); font-size: 1rem; font-weight: 700; line-height: 1.2; }
.og-facebook .og-desc { color: var(--text-muted); font-size: 0.85rem; margin-top: 0.25rem; line-height: 1.35; max-height: 2.7em; overflow: hidden; }

.og-linkedin { background: var(--surface); border: 1px solid var(--border); }
.og-linkedin .og-body { padding: 0.7rem 0.9rem; }
.og-linkedin .og-title { color: var(--text); font-size: 0.95rem; font-weight: 600; line-height: 1.3; }
.og-linkedin .og-host { color: var(--text-muted); font-size: 0.8rem; margin-top: 0.3rem; }

.og-discord { background: #36393f; color: #dcddde; border-left: 4px solid #4f545c; padding: 0.6rem 0.9rem; max-width: 480px; border-radius: 4px; }
.og-discord .og-host { color: #b9bbbe; font-size: 0.8rem; }
.og-discord .og-title { color: #00b0f4; font-size: 1rem; font-weight: 600; margin-top: 0.15rem; line-height: 1.25; cursor: pointer; }
.og-discord .og-desc { color: #dcddde; font-size: 0.88rem; margin-top: 0.25rem; line-height: 1.4; }
.og-discord .og-img { aspect-ratio: 1.91 / 1; margin-top: 0.5rem; max-width: 400px; border-radius: 4px; }
</style>
<script>
function ogEsc(s){ return String(s||'').replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c])); }

function ogHost(url){
  try { return new URL(url).host; } catch(e){ return ''; }
}

function ogParse(){
  const html = document.getElementById('og-html').value;
  if(!html.trim()){ ogRender(); return; }
  const doc = new DOMParser().parseFromString('<!doctype html><html><head>' + html + '</head><body></body></html>', 'text/html');
  const get = (sel) => {
    const el = doc.querySelector(sel);
    return el ? (el.getAttribute('content') || '') : '';
  };
  const t = get('meta[property="og:title"]') || get('meta[name="twitter:title"]') || get('title');
  const d = get('meta[property="og:description"]') || get('meta[name="twitter:description"]') || get('meta[name="description"]');
  const img = get('meta[property="og:image"]') || get('meta[name="twitter:image"]');
  const url = get('meta[property="og:url"]');
  const site = get('meta[property="og:site_name"]');
  if(t) document.getElementById('og-title').value = t;
  if(d) document.getElementById('og-desc').value = d;
  if(img) document.getElementById('og-image').value = img;
  if(url) document.getElementById('og-url').value = url;
  if(site) document.getElementById('og-site').value = site;
  ogRender();
}

function ogClampTitle(s, max){
  if(!s) return '';
  if(s.length <= max) return s;
  return s.slice(0, max-1).trim() + '…';
}

function ogRender(){
  const title = document.getElementById('og-title').value;
  const desc = document.getElementById('og-desc').value;
  const image = document.getElementById('og-image').value;
  const url = document.getElementById('og-url').value;
  const site = document.getElementById('og-site').value || ogHost(url) || 'example.com';

  const imgStyle = image ? `style="background-image:url('${ogEsc(image).replace(/'/g, "\\\\'")}')"` : '';
  const imgClass = image ? '' : 'og-img-empty';

  // Twitter / X — summary_large_image
  document.getElementById('og-twitter').innerHTML = `
    <div class="og-img ${imgClass}" ${imgStyle}></div>
    <div class="og-body">
      <div class="og-host">${ogEsc(ogHost(url) || site)}</div>
      <div class="og-title">${ogEsc(ogClampTitle(title, 70))}</div>
      <div class="og-desc">${ogEsc(ogClampTitle(desc, 200))}</div>
    </div>`;

  // Facebook
  document.getElementById('og-facebook').innerHTML = `
    <div class="og-img ${imgClass}" ${imgStyle}></div>
    <div class="og-body">
      <div class="og-host">${ogEsc(ogHost(url) || site)}</div>
      <div class="og-title">${ogEsc(ogClampTitle(title, 88))}</div>
      <div class="og-desc">${ogEsc(ogClampTitle(desc, 200))}</div>
    </div>`;

  // LinkedIn
  document.getElementById('og-linkedin').innerHTML = `
    <div class="og-img ${imgClass}" ${imgStyle}></div>
    <div class="og-body">
      <div class="og-title">${ogEsc(ogClampTitle(title, 100))}</div>
      <div class="og-host">${ogEsc(ogHost(url) || site)}</div>
    </div>`;

  // Discord
  document.getElementById('og-discord').innerHTML = `
    <div class="og-host">${ogEsc(site)}</div>
    <div class="og-title">${ogEsc(ogClampTitle(title, 100))}</div>
    <div class="og-desc">${ogEsc(ogClampTitle(desc, 300))}</div>
    <div class="og-img ${imgClass}" ${imgStyle}></div>`;
}

document.addEventListener('DOMContentLoaded', ogRender);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>When you share a link in Twitter/X, Facebook, LinkedIn, Discord, Slack or any modern chat or social app, the link is unfurled into a "card" — title, description, and image — based on the <a href="https://ogp.me/" target="_blank" rel="noopener noreferrer">Open Graph</a> meta tags in the page head. The various platforms render these cards differently and clip text at different lengths. This tool gives you side-by-side previews of how the same content will appear in each, without having to actually share the URL on every platform.</p>

<h3>When to use it</h3>
<ul>
  <li>You changed the OG image or copy and want to confirm it looks right before deploying.</li>
  <li>You're choosing a hero image and want to see whether the focal point will survive the 1.91:1 crop.</li>
  <li>You're writing the title/description copy and want to know where each platform will clip it.</li>
  <li>You inherited a page with no OG tags and want to draft them by previewing the rendered card.</li>
</ul>

<h3>The minimum tags</h3>
<ul>
  <li><code>&lt;meta property="og:title" content="…"&gt;</code></li>
  <li><code>&lt;meta property="og:description" content="…"&gt;</code></li>
  <li><code>&lt;meta property="og:image" content="https://…"&gt;</code> (absolute URL, 1200×630 ideal)</li>
  <li><code>&lt;meta property="og:url" content="https://…"&gt;</code></li>
  <li><code>&lt;meta property="og:type" content="website"&gt;</code></li>
  <li><code>&lt;meta name="twitter:card" content="summary_large_image"&gt;</code> (for the X/Twitter big-image style)</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>This is a static preview, not a live fetcher.</strong> Real platforms scrape your page from their servers; if your real site has a different image, this tool won't catch it. Use the platforms' own debuggers (Twitter's <a href="https://cards-dev.twitter.com/validator" target="_blank" rel="noopener noreferrer">card validator</a>, Facebook's Sharing Debugger, LinkedIn's Post Inspector) for the authoritative check.</li>
  <li><strong>Image URLs must be absolute.</strong> <code>/og.png</code> won't work — scrapers don't know your origin.</li>
  <li><strong>Image must be publicly reachable.</strong> Authentication walls, CDNs that require referer, or hot-link protection will leave you with a broken card.</li>
  <li><strong>Aspect ratio matters.</strong> 1.91:1 (1200×630 is canonical) renders well on every platform. Square or portrait crops badly.</li>
  <li><strong>File size matters.</strong> Some scrapers reject images over 8 MB; aim for &lt;1 MB to keep first-load snappy.</li>
  <li><strong>Cache invalidation is real.</strong> Once a platform has scraped your URL, it caches the card. Use the platform debuggers to force a re-scrape.</li>
  <li><strong>Title/description length limits vary.</strong> Twitter/X clips title around 70 chars; Facebook around 88; LinkedIn around 100. Front-load the important words.</li>
  <li><strong>Discord prefers <code>theme-color</code>.</strong> Adding <code>&lt;meta name="theme-color" content="#xxxxxx"&gt;</code> sets the left border colour on Discord embeds.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Quando você compartilha um link no Twitter/X, Facebook, LinkedIn, Discord, Slack ou qualquer chat ou app social moderno, o link é desdobrado em um "card" — título, descrição e imagem — com base nos meta tags <a href="https://ogp.me/" target="_blank" rel="noopener noreferrer">Open Graph</a> no head da página. Cada plataforma renderiza esses cards de um jeito diferente e corta o texto em comprimentos diferentes. Esta ferramenta te dá previews lado a lado de como o mesmo conteúdo vai aparecer em cada uma, sem você precisar compartilhar a URL em cada plataforma.</p>

<h3>Quando usar</h3>
<ul>
  <li>Você mudou a imagem OG ou o texto e quer confirmar que está certo antes de fazer o deploy.</li>
  <li>Você está escolhendo uma imagem hero e quer ver se o ponto focal vai sobreviver ao crop 1.91:1.</li>
  <li>Você está escrevendo o texto de título/descrição e quer saber onde cada plataforma vai cortar.</li>
  <li>Você herdou uma página sem tags OG e quer rascunhá-las visualizando o card renderizado.</li>
</ul>

<h3>As tags mínimas</h3>
<ul>
  <li><code>&lt;meta property="og:title" content="…"&gt;</code></li>
  <li><code>&lt;meta property="og:description" content="…"&gt;</code></li>
  <li><code>&lt;meta property="og:image" content="https://…"&gt;</code> (URL absoluta, 1200×630 ideal)</li>
  <li><code>&lt;meta property="og:url" content="https://…"&gt;</code></li>
  <li><code>&lt;meta property="og:type" content="website"&gt;</code></li>
  <li><code>&lt;meta name="twitter:card" content="summary_large_image"&gt;</code> (para o estilo big-image do X/Twitter)</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>Este é um preview estático, não um fetcher ao vivo.</strong> As plataformas reais raspam sua página dos servidores delas; se seu site real tiver outra imagem, esta ferramenta não pega. Use os debuggers oficiais (<a href="https://cards-dev.twitter.com/validator" target="_blank" rel="noopener noreferrer">card validator</a> do Twitter, Sharing Debugger do Facebook, Post Inspector do LinkedIn) para a checagem oficial.</li>
  <li><strong>URLs de imagem precisam ser absolutas.</strong> <code>/og.png</code> não funciona — os scrapers não conhecem sua origem.</li>
  <li><strong>A imagem precisa estar publicamente acessível.</strong> Paredes de autenticação, CDNs que exigem referer ou proteção contra hot-link vão te deixar com um card quebrado.</li>
  <li><strong>Aspect ratio importa.</strong> 1.91:1 (1200×630 é o canônico) renderiza bem em todas as plataformas. Quadrado ou retrato sofre crop ruim.</li>
  <li><strong>Tamanho de arquivo importa.</strong> Alguns scrapers rejeitam imagens acima de 8 MB; mire em &lt;1 MB para manter o first-load rápido.</li>
  <li><strong>Invalidação de cache é real.</strong> Uma vez que uma plataforma raspou sua URL, ela faz cache do card. Use os debuggers da plataforma para forçar um re-scrape.</li>
  <li><strong>Os limites de tamanho de título/descrição variam.</strong> Twitter/X corta título em torno de 70 caracteres; Facebook em torno de 88; LinkedIn em torno de 100. Coloque as palavras importantes no começo.</li>
  <li><strong>Discord prefere <code>theme-color</code>.</strong> Adicionar <code>&lt;meta name="theme-color" content="#xxxxxx"&gt;</code> define a cor da borda esquerda nos embeds do Discord.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>Wenn du einen Link auf Twitter/X, Facebook, LinkedIn, Discord oder Slack teilst, wird er zu einer Karte (Titel, Beschreibung, Bild) auf Basis der <a href="https://ogp.me/" target="_blank" rel="noopener noreferrer">Open-Graph</a>-Meta-Tags. Plattformen rendern unterschiedlich. Dieses Tool zeigt nebeneinander, wie dein Content erscheint.</p>
<h3>Wann verwenden</h3>
<ul>
<li>OG-Bild/Texte vor Deploy prüfen.</li>
<li>Hero-Bild auf 1,91:1-Crop testen.</li>
<li>Titel/Beschreibung auf Clip-Längen prüfen.</li>
<li>Fehlende OG-Tags entwerfen.</li>
</ul>
<h3>Mindest-Tags</h3>
<ul>
<li><code>og:title</code>, <code>og:description</code>, <code>og:image</code> (absolute URL), <code>og:url</code>, <code>og:type</code></li>
<li><code>twitter:card="summary_large_image"</code></li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>Statische Vorschau, kein Live-Fetch.</strong> Plattform-Debugger nutzen.</li>
<li><strong>Bild-URLs müssen absolut sein.</strong></li>
<li><strong>Bild muss öffentlich erreichbar sein.</strong></li>
<li><strong>Seitenverhältnis 1,91:1</strong> (1200×630) funktioniert überall.</li>
<li><strong>Dateigröße &lt;1 MB.</strong></li>
<li><strong>Caching</strong> — Re-Scrape via Plattform-Debugger erzwingen.</li>
<li><strong>Längenlimits unterschiedlich.</strong> Twitter ~70, FB ~88, LinkedIn ~100.</li>
<li><strong>Discord nutzt <code>theme-color</code></strong> für linken Rand.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>Al compartir un enlace en Twitter/X, Facebook, LinkedIn, Discord o Slack, se convierte en una tarjeta (título, descripción, imagen) según los meta-tags <a href="https://ogp.me/" target="_blank" rel="noopener noreferrer">Open Graph</a>. Cada plataforma renderiza distinto. Esta herramienta te muestra el contenido en paralelo.</p>
<h3>Cuándo usarlo</h3>
<ul>
<li>Verificar imagen OG / textos antes de desplegar.</li>
<li>Probar imagen hero en crop 1,91:1.</li>
<li>Comprobar dónde recorta cada plataforma el título/descripción.</li>
<li>Redactar tags OG ausentes.</li>
</ul>
<h3>Tags mínimos</h3>
<ul>
<li><code>og:title</code>, <code>og:description</code>, <code>og:image</code> (URL absoluta), <code>og:url</code>, <code>og:type</code></li>
<li><code>twitter:card="summary_large_image"</code></li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>Vista previa estática, no fetch en vivo.</strong> Usa los debuggers oficiales.</li>
<li><strong>URLs de imagen absolutas.</strong></li>
<li><strong>Imagen accesible públicamente.</strong></li>
<li><strong>Aspecto 1,91:1</strong> (1200×630) funciona en todas.</li>
<li><strong>Tamaño &lt;1 MB.</strong></li>
<li><strong>Caché</strong> — fuerza re-scrape con el debugger.</li>
<li><strong>Recortes diferentes:</strong> Twitter ~70, FB ~88, LinkedIn ~100.</li>
<li><strong>Discord usa <code>theme-color</code></strong> para el borde izquierdo.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Quand vous partagez un lien sur Twitter/X, Facebook, LinkedIn, Discord ou Slack, il devient une carte (titre, description, image) basée sur les meta-tags <a href="https://ogp.me/" target="_blank" rel="noopener noreferrer">Open Graph</a>. Chaque plateforme rend différemment. Cet outil affiche votre contenu côte à côte.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>Vérifier image OG / textes avant déploiement.</li>
<li>Tester l'image héro sur crop 1,91:1.</li>
<li>Vérifier où chaque plateforme tronque titre/description.</li>
<li>Rédiger des tags OG manquants.</li>
</ul>
<h3>Tags minimum</h3>
<ul>
<li><code>og:title</code>, <code>og:description</code>, <code>og:image</code> (URL absolue), <code>og:url</code>, <code>og:type</code></li>
<li><code>twitter:card="summary_large_image"</code></li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>Aperçu statique, pas de fetch en direct.</strong> Utiliser les debuggers officiels.</li>
<li><strong>URLs d'image absolues.</strong></li>
<li><strong>Image accessible publiquement.</strong></li>
<li><strong>Ratio 1,91:1</strong> (1200×630) fonctionne partout.</li>
<li><strong>Taille &lt;1 MB.</strong></li>
<li><strong>Cache</strong> — forcer re-scrape via debugger.</li>
<li><strong>Troncatures différentes :</strong> Twitter ~70, FB ~88, LinkedIn ~100.</li>
<li><strong>Discord utilise <code>theme-color</code></strong> pour la bordure gauche.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>Quando condividi un link su Twitter/X, Facebook, LinkedIn, Discord o Slack, viene reso come una card (titolo, descrizione, immagine) in base ai meta tag <a href="https://ogp.me/" target="_blank" rel="noopener noreferrer">Open Graph</a>. Ogni piattaforma renderizza diversamente. Questo strumento mostra il contenuto fianco a fianco.</p>
<h3>Quando usarlo</h3>
<ul>
<li>Verificare immagine OG / testi prima del deploy.</li>
<li>Testare immagine hero su crop 1,91:1.</li>
<li>Vedere dove ogni piattaforma taglia titolo/descrizione.</li>
<li>Redigere tag OG mancanti.</li>
</ul>
<h3>Tag minimi</h3>
<ul>
<li><code>og:title</code>, <code>og:description</code>, <code>og:image</code> (URL assoluto), <code>og:url</code>, <code>og:type</code></li>
<li><code>twitter:card="summary_large_image"</code></li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>Anteprima statica, non fetch in tempo reale.</strong> Usare i debugger ufficiali.</li>
<li><strong>URL immagine assoluti.</strong></li>
<li><strong>Immagine pubblicamente accessibile.</strong></li>
<li><strong>Aspect 1,91:1</strong> (1200×630) funziona ovunque.</li>
<li><strong>Dimensione &lt;1 MB.</strong></li>
<li><strong>Cache</strong> — forza re-scrape via debugger.</li>
<li><strong>Tagli diversi:</strong> Twitter ~70, FB ~88, LinkedIn ~100.</li>
<li><strong>Discord usa <code>theme-color</code></strong> per il bordo sinistro.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Gdy wrzucasz link na Twittera/X, Facebooka, LinkedIna, Discorda, Slacka albo dowolny nowoczesny czat lub social, link jest rozwijany w "card" — title, description i image — na podstawie meta tagów <a href="https://ogp.me/" target="_blank" rel="noopener noreferrer">Open Graph</a> w head-zie strony. Różne platformy renderują te cardy inaczej i ucinają tekst w różnych miejscach. To narzędzie pokazuje obok siebie podglądy, jak ten sam content wyświetli się w każdej, bez konieczności faktycznego udostępniania URL-a na każdej platformie.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Zmieniłeś OG image albo copy i chcesz potwierdzić, że dobrze wygląda przed deployem.</li>
  <li>Wybierasz hero image i chcesz zobaczyć, czy punkt centralny przeżyje crop 1.91:1.</li>
  <li>Piszesz tytuł/opis i chcesz wiedzieć, gdzie każda platforma to utnie.</li>
  <li>Odziedziczyłeś stronę bez tagów OG i chcesz je naszkicować, podglądając wyrenderowany card.</li>
</ul>

<h3>Minimalne tagi</h3>
<ul>
  <li><code>&lt;meta property="og:title" content="…"&gt;</code></li>
  <li><code>&lt;meta property="og:description" content="…"&gt;</code></li>
  <li><code>&lt;meta property="og:image" content="https://…"&gt;</code> (URL absolutny, ideał 1200×630)</li>
  <li><code>&lt;meta property="og:url" content="https://…"&gt;</code></li>
  <li><code>&lt;meta property="og:type" content="website"&gt;</code></li>
  <li><code>&lt;meta name="twitter:card" content="summary_large_image"&gt;</code> (dla stylu big-image w X/Twitterze)</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>To statyczny podgląd, nie żywy fetcher.</strong> Prawdziwe platformy scrape'ują twoją stronę z ich serwerów; jeśli twoja faktyczna witryna ma inny obrazek, to narzędzie tego nie złapie. Do autorytatywnego sprawdzenia używaj debuggerów platform (Twitterowy <a href="https://cards-dev.twitter.com/validator" target="_blank" rel="noopener noreferrer">card validator</a>, Facebook Sharing Debugger, LinkedIn Post Inspector).</li>
  <li><strong>URL-e obrazków muszą być absolutne.</strong> <code>/og.png</code> nie zadziała — scrape'ery nie znają twojego origina.</li>
  <li><strong>Obrazek musi być publicznie osiągalny.</strong> Ściany uwierzytelnienia, CDN-y wymagające referera, ochrona przed hot-linkiem zostawią cię z popsutym cardem.</li>
  <li><strong>Aspect ratio ma znaczenie.</strong> 1.91:1 (kanonicznie 1200×630) renderuje się dobrze na każdej platformie. Kwadrat albo portret dostają brzydki crop.</li>
  <li><strong>Rozmiar pliku ma znaczenie.</strong> Niektóre scrape'ery odrzucają obrazki powyżej 8 MB; celuj w &lt;1 MB, żeby first-load był szybki.</li>
  <li><strong>Inwalidacja cache jest realna.</strong> Gdy platforma raz zescrape'uje twój URL, zacache'uje carda. Używaj debuggerów platform, żeby wymusić re-scrape.</li>
  <li><strong>Limity długości title/description się różnią.</strong> Twitter/X ucina tytuł około 70 znaków; Facebook około 88; LinkedIn około 100. Stawiaj ważne słowa na początku.</li>
  <li><strong>Discord lubi <code>theme-color</code>.</strong> Dodanie <code>&lt;meta name="theme-color" content="#xxxxxx"&gt;</code> ustawia kolor lewej krawędzi w embedach Discorda.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>Twitter/X、Facebook、LinkedIn、Discord、Slack などにリンクを共有すると、ページの head にある <a href="https://ogp.me/" target="_blank" rel="noopener noreferrer">Open Graph</a> メタタグに基づいて「カード」（タイトル・説明・画像）に展開されます。各プラットフォームでカードのレンダリングや文字数のクリップは異なります。本ツールは、各プラットフォームに実際に投稿することなく、同じ内容がどう見えるかをサイドバイサイドでプレビューします。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>OG 画像やコピーを変更し、デプロイ前に問題ないか確認したいとき。</li>
  <li>ヒーロー画像を選ぶ際、1.91:1 のクロップで主要部分が残るか確認したいとき。</li>
  <li>タイトルや説明文を書く際、各プラットフォームでどこが切られるかを確認したいとき。</li>
  <li>OG タグがないページを引き継ぎ、レンダリング結果を見ながら下書きしたいとき。</li>
</ul>

<h3>最小限のタグ</h3>
<ul>
  <li><code>&lt;meta property="og:title" content="…"&gt;</code></li>
  <li><code>&lt;meta property="og:description" content="…"&gt;</code></li>
  <li><code>&lt;meta property="og:image" content="https://…"&gt;</code>（絶対 URL、1200×630 が理想）</li>
  <li><code>&lt;meta property="og:url" content="https://…"&gt;</code></li>
  <li><code>&lt;meta property="og:type" content="website"&gt;</code></li>
  <li><code>&lt;meta name="twitter:card" content="summary_large_image"&gt;</code>（X/Twitter の大きな画像表示用）</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>これは静的なプレビューであり、ライブフェッチではありません。</strong> 実際のプラットフォームは自分のサーバーからページをスクレイピングします。本番サイトに別の画像が出ても本ツールでは捕捉できません。最終確認は各プラットフォームの公式デバッガ（Twitter <a href="https://cards-dev.twitter.com/validator" target="_blank" rel="noopener noreferrer">card validator</a>、Facebook Sharing Debugger、LinkedIn Post Inspector）で行ってください。</li>
  <li><strong>画像 URL は絶対 URL である必要があります。</strong> <code>/og.png</code> ではダメで、スクレイパーはあなたのオリジンを知りません。</li>
  <li><strong>画像は公開アクセス可能でなければなりません。</strong> 認証ウォール、リファラを要求する CDN、ホットリンク防止が有効だとカードが壊れます。</li>
  <li><strong>アスペクト比が重要です。</strong> 1.91:1（標準は 1200×630）はどのプラットフォームでも綺麗に表示されます。正方形やポートレートはクロップで損をします。</li>
  <li><strong>ファイルサイズも重要。</strong> 8 MB を超える画像を拒否するスクレイパーもあります。初回読み込みを軽くするため 1 MB 未満を狙ってください。</li>
  <li><strong>キャッシュ無効化は現実問題です。</strong> 一度スクレイピングされるとカードがキャッシュされます。再スクレイプにはプラットフォームのデバッガを使ってください。</li>
  <li><strong>タイトル／説明の文字数上限はばらつきます。</strong> Twitter/X はおおむね 70、Facebook は 88、LinkedIn は 100 文字付近で切れます。重要語は前に置きましょう。</li>
  <li><strong>Discord は <code>theme-color</code> を好みます。</strong> <code>&lt;meta name="theme-color" content="#xxxxxx"&gt;</code> を追加すると、Discord の左ボーダーの色になります。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Wanneer je een link in Twitter/X, Facebook, LinkedIn, Discord, Slack of een moderne chat- of social-app deelt, wordt de link unfurled naar een "card" — title, description en image — gebaseerd op de <a href="https://ogp.me/" target="_blank" rel="noopener noreferrer">Open Graph</a> meta-tags in de page head. De verschillende platforms renderen deze cards anders en clippen tekst op verschillende lengtes. Deze tool geeft side-by-side previews van hoe dezelfde content in elk zal verschijnen, zonder dat je de URL daadwerkelijk op elk platform hoeft te delen.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Je hebt de OG-image of copy veranderd en wilt bevestigen dat het er goed uitziet voor deploy.</li>
  <li>Je kiest een hero-image en wilt zien of het focal point de 1.91:1 crop overleeft.</li>
  <li>Je schrijft de title/description-copy en wilt weten waar elk platform 'm zal clippen.</li>
  <li>Je hebt een pagina geërfd zonder OG-tags en wilt ze opstellen door de gerenderde card te previewen.</li>
</ul>

<h3>De minimum-tags</h3>
<ul>
  <li><code>&lt;meta property="og:title" content="…"&gt;</code></li>
  <li><code>&lt;meta property="og:description" content="…"&gt;</code></li>
  <li><code>&lt;meta property="og:image" content="https://…"&gt;</code> (absolute URL, 1200×630 ideaal)</li>
  <li><code>&lt;meta property="og:url" content="https://…"&gt;</code></li>
  <li><code>&lt;meta property="og:type" content="website"&gt;</code></li>
  <li><code>&lt;meta name="twitter:card" content="summary_large_image"&gt;</code> (voor de X/Twitter big-image stijl)</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Dit is een statische preview, geen live fetcher.</strong> Echte platforms scrapen je pagina vanaf hun servers; als je echte site een andere image heeft, vangt deze tool dat niet. Gebruik de eigen debuggers van de platforms (Twitter's <a href="https://cards-dev.twitter.com/validator" target="_blank" rel="noopener noreferrer">card validator</a>, Facebook's Sharing Debugger, LinkedIn's Post Inspector) voor de gezaghebbende check.</li>
  <li><strong>Image-URLs moeten absoluut zijn.</strong> <code>/og.png</code> werkt niet — scrapers kennen je origin niet.</li>
  <li><strong>Image moet publiek bereikbaar zijn.</strong> Authentication walls, CDNs die referer vereisen, of hot-link protection laten je achter met een gebroken card.</li>
  <li><strong>Aspect ratio doet ertoe.</strong> 1.91:1 (1200×630 is canoniek) rendert goed op elk platform. Vierkant of portret crop't slecht.</li>
  <li><strong>Bestandsgrootte doet ertoe.</strong> Sommige scrapers wijzen images boven 8 MB af; mik op &lt;1 MB om first-load snappy te houden.</li>
  <li><strong>Cache-invalidatie is echt.</strong> Zodra een platform je URL heeft gescraped, cached het de card. Gebruik de platform-debuggers om een re-scrape te forceren.</li>
  <li><strong>Title/description-lengte-limieten verschillen.</strong> Twitter/X clipt title rond 70 tekens; Facebook rond 88; LinkedIn rond 100. Zet de belangrijke woorden vooraan.</li>
  <li><strong>Discord prefereert <code>theme-color</code>.</strong> <code>&lt;meta name="theme-color" content="#xxxxxx"&gt;</code> toevoegen zet de linker rand-kleur op Discord embeds.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Twitter/X, Facebook, LinkedIn, Discord, Slack veya herhangi bir modern sohbet veya sosyal uygulamada bir link paylaştığında, link sayfa head'indeki <a href="https://ogp.me/" target="_blank" rel="noopener noreferrer">Open Graph</a> meta tag'lerine dayanarak bir "kart" — başlık, açıklama ve görsel — olarak açılır. Çeşitli platformlar bu kartları farklı render eder ve metni farklı uzunluklarda keser. Bu araç sana her platformda URL'i gerçekten paylaşmak zorunda kalmadan her birinde aynı içeriğin nasıl görüneceğinin yan yana önizlemelerini verir.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>OG görselini veya kopyayı değiştirdin ve deploy etmeden önce doğru göründüğünü doğrulamak istiyorsun.</li>
  <li>Bir hero görsel seçiyorsun ve odak noktasının 1.91:1 kırpmasından sağ çıkıp çıkmayacağını görmek istiyorsun.</li>
  <li>Başlık/açıklama kopyasını yazıyorsun ve her platformun nerede keseceğini bilmek istiyorsun.</li>
  <li>OG tag'i olmayan bir sayfayı miras aldın ve render edilen kartı önizleyerek bunları hazırlamak istiyorsun.</li>
</ul>

<h3>Minimum tag'ler</h3>
<ul>
  <li><code>&lt;meta property="og:title" content="…"&gt;</code></li>
  <li><code>&lt;meta property="og:description" content="…"&gt;</code></li>
  <li><code>&lt;meta property="og:image" content="https://…"&gt;</code> (mutlak URL, 1200×630 ideal)</li>
  <li><code>&lt;meta property="og:url" content="https://…"&gt;</code></li>
  <li><code>&lt;meta property="og:type" content="website"&gt;</code></li>
  <li><code>&lt;meta name="twitter:card" content="summary_large_image"&gt;</code> (X/Twitter büyük-görsel stili için)</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Bu statik bir önizleme, canlı bir fetcher değil.</strong> Gerçek platformlar sayfanı kendi sunucularından kazır; gerçek sitenin farklı bir görseli varsa, bu araç bunu yakalamayacaktır.</li>
  <li><strong>Görsel URL'leri mutlak olmalıdır.</strong> <code>/og.png</code> çalışmayacaktır — kazıyıcılar origin'ini bilmez.</li>
  <li><strong>Görsel kamuya ulaşılabilir olmalıdır.</strong> Auth duvarları, referer gerektiren CDN'ler veya hot-link koruması seni bozuk bir kartla bırakacaktır.</li>
  <li><strong>En-boy oranı önemlidir.</strong> 1.91:1 (1200×630 kanoniktir) her platformda iyi render olur. Kare veya portre kötü kırpılır.</li>
  <li><strong>Dosya boyutu önemlidir.</strong> Bazı kazıyıcılar 8 MB üzerindeki görselleri reddeder; ilk yükü hızlı tutmak için &lt;1 MB hedefle.</li>
  <li><strong>Cache geçersizleştirme gerçek.</strong> Bir platform URL'ini kazıdığında, kartı önbelleğe alır. Yeniden kazımayı zorlamak için platform debugger'larını kullan.</li>
  <li><strong>Başlık/açıklama uzunluk sınırları değişir.</strong> Twitter/X başlığı ~70 karakterde, Facebook ~88'de, LinkedIn ~100'de keser. Önemli kelimeleri öne yükle.</li>
  <li><strong>Discord <code>theme-color</code>'ı tercih eder.</strong> <code>&lt;meta name="theme-color" content="#xxxxxx"&gt;</code> eklemek Discord embed'lerindeki sol kenarlık rengini ayarlar.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Saat kamu membagikan sebuah link di Twitter/X, Facebook, LinkedIn, Discord, Slack, atau aplikasi chat atau social modern apa pun, link itu di-unfurl menjadi "card" — title, description, dan image — berdasarkan meta tag <a href="https://ogp.me/" target="_blank" rel="noopener noreferrer">Open Graph</a> di head halaman. Berbagai platform me-render card ini secara berbeda dan memotong teks pada panjang yang berbeda. Tool ini memberi kamu preview side-by-side bagaimana konten yang sama akan muncul di masing-masingnya, tanpa kamu harus benar-benar membagikan URL-nya di setiap platform.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Kamu mengganti OG image atau copy dan ingin memastikannya terlihat oke sebelum deploy.</li>
  <li>Kamu memilih hero image dan ingin lihat apakah focal point-nya selamat dari crop 1.91:1.</li>
  <li>Kamu menulis copy title/description dan ingin tahu di mana setiap platform akan memotongnya.</li>
  <li>Kamu mewarisi halaman tanpa OG tag dan ingin mendraft-nya dengan mem-preview card hasil render.</li>
</ul>

<h3>Tag minimum</h3>
<ul>
  <li><code>&lt;meta property="og:title" content="…"&gt;</code></li>
  <li><code>&lt;meta property="og:description" content="…"&gt;</code></li>
  <li><code>&lt;meta property="og:image" content="https://…"&gt;</code> (URL absolut, 1200×630 ideal)</li>
  <li><code>&lt;meta property="og:url" content="https://…"&gt;</code></li>
  <li><code>&lt;meta property="og:type" content="website"&gt;</code></li>
  <li><code>&lt;meta name="twitter:card" content="summary_large_image"&gt;</code> (untuk gaya big-image X/Twitter)</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Ini preview statis, bukan fetcher live.</strong> Platform sebenarnya men-scrape halaman kamu dari server mereka; kalau site asli kamu punya image yang berbeda, tool ini tidak akan menangkapnya. Pakai debugger milik platform sendiri (Twitter <a href="https://cards-dev.twitter.com/validator" target="_blank" rel="noopener noreferrer">card validator</a>, Facebook Sharing Debugger, LinkedIn Post Inspector) untuk pengecekan yang otoritatif.</li>
  <li><strong>URL image harus absolut.</strong> <code>/og.png</code> tidak akan bekerja — scraper tidak mengenal origin kamu.</li>
  <li><strong>Image harus bisa diakses publik.</strong> Auth wall, CDN yang butuh referer, atau hot-link protection akan meninggalkan kamu dengan card yang rusak.</li>
  <li><strong>Aspect ratio penting.</strong> 1.91:1 (1200×630 canonical) render bagus di setiap platform. Square atau portrait di-crop dengan buruk.</li>
  <li><strong>Ukuran file penting.</strong> Beberapa scraper menolak image di atas 8 MB; targetkan &lt;1 MB supaya first-load tetap cepat.</li>
  <li><strong>Cache invalidation itu nyata.</strong> Begitu sebuah platform men-scrape URL kamu, ia akan men-cache card-nya. Pakai debugger platform untuk memaksa re-scrape.</li>
  <li><strong>Batas panjang title/description berbeda-beda.</strong> Twitter/X memotong title sekitar 70 karakter; Facebook sekitar 88; LinkedIn sekitar 100. Letakkan kata-kata penting di depan.</li>
  <li><strong>Discord menyukai <code>theme-color</code>.</strong> Menambahkan <code>&lt;meta name="theme-color" content="#xxxxxx"&gt;</code> mengatur warna border kiri di embed Discord.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Open Graph (OG) tag điều khiển cách link được hiển thị khi share trên Twitter/X, Facebook, LinkedIn, Discord và các nền tảng social khác. Title, description và image là ba thẻ quan trọng nhất. Tool này cho phép bạn dán meta tag hoặc điền field thủ công, sau đó xem chính xác cách social card sẽ trông trên các nền tảng chính.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Trước khi launch một trang mới — kiểm tra OG image render đúng kích thước.</li>
  <li>Debug trang chia sẻ với link preview vỡ.</li>
  <li>So sánh trang của bạn với competitor để xem social card của họ trông như thế nào.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Twitter dùng <code>twitter:*</code> tag riêng.</strong> Nó fall back về OG, nhưng nếu bạn muốn kiểm soát chính xác kích thước card (summary_large_image vs summary), dùng twitter:card.</li>
  <li><strong>Kích thước image quan trọng.</strong> 1200×630 là sweet spot — quá nhỏ và scaler làm xấu nó; quá lớn và bị crop khó đoán.</li>
  <li><strong>Cache rất lâu.</strong> Khi bạn cập nhật OG tag, Facebook và Twitter có thể vẫn show phiên bản cũ. Dùng <a href="https://developers.facebook.com/tools/debug/">Facebook Sharing Debugger</a> để force refresh.</li>
</ul>
""",
    },
    "related": ["html-encoder", "url-parser", "placeholder-image", "qr-code-generator"],
    "howto": {"flow": "transform", "action": "convert", "noun": "URL"},
}
