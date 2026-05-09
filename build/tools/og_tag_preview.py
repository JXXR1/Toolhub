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
    },
    "related": ["html-encoder", "url-parser", "placeholder-image", "qr-code-generator"],
}
