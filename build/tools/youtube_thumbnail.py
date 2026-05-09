TOOL = {
    "slug": "youtube-thumbnail",
    "category": "media",
    "icon": "▶",
    "tags": ["youtube", "thumbnail", "preview", "image", "download", "video"],
    "i18n": {
        "en": {
            "name": "YouTube Thumbnail Downloader",
            "tagline": "Paste any YouTube URL or video ID and grab every available thumbnail size — direct download links, no upload, no signup.",
            "description": "Free YouTube thumbnail downloader. Extracts the video ID from any YouTube URL (watch, youtu.be, shorts, embed, /v/) and shows all available thumbnail resolutions with direct download links.",
        },
        "de": {"name": "YouTube Thumbnail-Downloader", "tagline": "Füge eine YouTube-URL oder Video-ID ein und erhalte alle verfügbaren Thumbnail-Größen — direkte Download-Links, kein Upload.", "description": "Kostenloser YouTube-Thumbnail-Downloader. Extrahiert die Video-ID aus jeder YouTube-URL (watch, youtu.be, shorts, embed) und zeigt alle Thumbnail-Auflösungen mit direkten Download-Links."},
        "es": {"name": "Descargador de Miniaturas de YouTube", "tagline": "Pega cualquier URL de YouTube o ID de vídeo y obtén todos los tamaños de miniatura disponibles — descarga directa, sin registro.", "description": "Descargador gratuito de miniaturas de YouTube. Extrae el ID de vídeo de cualquier URL de YouTube y muestra todas las resoluciones de miniaturas con enlaces de descarga directa."},
        "fr": {"name": "Téléchargeur de Miniatures YouTube", "tagline": "Collez n'importe quelle URL YouTube ou ID vidéo et obtenez toutes les tailles de miniatures disponibles — téléchargement direct, sans inscription.", "description": "Téléchargeur gratuit de miniatures YouTube. Extrait l'ID vidéo de toute URL YouTube et affiche toutes les résolutions de miniatures avec liens de téléchargement directs."},
        "it": {"name": "Download Miniature YouTube", "tagline": "Incolla qualsiasi URL YouTube o ID video e ottieni tutte le dimensioni di miniatura disponibili — link diretti, nessuna registrazione.", "description": "Download gratuito di miniature YouTube. Estrae l'ID video da qualsiasi URL YouTube e mostra tutte le risoluzioni di miniature con link di download diretti."},
    },
    "body": """
<div class="tool-card">
  <label>YouTube URL or video ID</label>
  <input type="text" id="yt-input" oninput="ytRun()" placeholder="https://www.youtube.com/watch?v=dQw4w9WgXcQ" spellcheck="false" autocomplete="off">
  <div class="meta" style="margin-top:0.5rem">Supports <code>youtube.com/watch?v=</code>, <code>youtu.be/</code>, <code>youtube.com/shorts/</code>, <code>youtube.com/embed/</code>, <code>youtube.com/v/</code>, or just the 11-character ID.</div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="yt-out" class="output">{LBL_NO_INPUT}</div>
</div>
""",
    "script": """
<style>
.yt-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:0.8rem}
.yt-card{background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;overflow:hidden;display:flex;flex-direction:column}
.yt-card img{width:100%;height:auto;display:block;background:#000;aspect-ratio:16/9;object-fit:cover}
.yt-card .yt-info{padding:0.55rem 0.7rem;display:flex;flex-direction:column;gap:0.35rem;font-size:0.82rem}
.yt-card .yt-name{font-weight:600;color:var(--text)}
.yt-card .yt-meta{color:var(--text-muted);font-family:ui-monospace,monospace;font-size:0.78rem}
.yt-card .yt-actions{display:flex;gap:0.35rem;margin-top:0.25rem}
.yt-card a.yt-btn{flex:1;text-align:center;background:var(--accent);color:#fff;text-decoration:none;padding:0.4rem 0.55rem;border-radius:6px;font-size:0.78rem;font-weight:600}
.yt-card button.yt-btn{flex:1;font-size:0.78rem;padding:0.4rem 0.55rem}
.yt-id{margin-bottom:0.7rem;font-family:ui-monospace,monospace;font-size:0.85rem;color:var(--text-muted)}
.yt-id code{background:var(--bg-elev);padding:0.15rem 0.4rem;border-radius:4px;color:var(--text)}
</style>
<script>
const YT_VARIANTS = [
  {key:'maxresdefault', name:'Max Resolution', size:'1280×720', note:'Not always available'},
  {key:'sddefault',     name:'Standard',       size:'640×480',  note:''},
  {key:'hqdefault',     name:'High Quality',   size:'480×360',  note:'Always available'},
  {key:'mqdefault',     name:'Medium Quality', size:'320×180',  note:''},
  {key:'default',       name:'Default',        size:'120×90',   note:''},
];
function ytExtractId(s){
  s = s.trim();
  if(!s) return null;
  if(/^[A-Za-z0-9_-]{11}$/.test(s)) return s;
  // youtu.be/<id>
  let m = s.match(/youtu\\.be\\/([A-Za-z0-9_-]{11})/);
  if(m) return m[1];
  // youtube.com/watch?v=<id>
  m = s.match(/[?&]v=([A-Za-z0-9_-]{11})/);
  if(m) return m[1];
  // youtube.com/shorts/<id> | /embed/<id> | /v/<id>
  m = s.match(/youtube\\.com\\/(?:shorts|embed|v)\\/([A-Za-z0-9_-]{11})/);
  if(m) return m[1];
  return null;
}
function ytCopy(text, btn){
  navigator.clipboard.writeText(text);
  const old = btn.textContent;
  btn.textContent = '✓';
  setTimeout(()=>btn.textContent = old, 900);
}
function ytRun(){
  const raw = document.getElementById('yt-input').value;
  const out = document.getElementById('yt-out');
  out.classList.remove('error');
  if(!raw){ out.textContent = '{LBL_NO_INPUT}'; out.className='output'; return; }
  const id = ytExtractId(raw);
  if(!id){ out.classList.add('error'); out.textContent = '✗ Could not find an 11-character YouTube video ID. Check the URL and try again.'; return; }
  out.className = 'output';
  let html = `<div class="yt-id">Video ID: <code>${id}</code> · <a href="https://www.youtube.com/watch?v=${id}" target="_blank" rel="noopener noreferrer">open on YouTube ↗</a></div>`;
  html += '<div class="yt-grid">';
  for(const v of YT_VARIANTS){
    const url = `https://i.ytimg.com/vi/${id}/${v.key}.jpg`;
    html += `<div class="yt-card">
      <img src="${url}" alt="${v.name}" loading="lazy" onerror="this.style.opacity=0.25;this.parentElement.querySelector('.yt-meta').textContent='${v.size} — image returned 404'">
      <div class="yt-info">
        <div class="yt-name">${v.name}</div>
        <div class="yt-meta">${v.size}${v.note?' · '+v.note:''}</div>
        <div class="yt-actions">
          <a class="yt-btn" href="${url}" download="${id}-${v.key}.jpg" target="_blank" rel="noopener noreferrer">{LBL_DOWNLOAD}</a>
          <button class="yt-btn secondary" onclick="ytCopy('${url}', this)">{LBL_COPY}</button>
        </div>
      </div>
    </div>`;
  }
  html += '</div>';
  out.innerHTML = html;
}
document.addEventListener('DOMContentLoaded', ytRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Every YouTube video has a small set of pre-generated thumbnail images at predictable URLs — YouTube uses them itself in search results, embeds, and previews. This tool extracts the 11-character video ID from any YouTube URL form (watch, youtu.be, Shorts, embed, /v/) and lays out every available size with direct download links and copy-URL buttons. Useful when you need an offline preview, a hero image for a blog post, a Discord/Slack rich link, or a fallback poster for a custom video player.</p>

<h3>When to use it</h3>
<ul>
  <li>Embedding a YouTube video in a blog post and wanting the same thumbnail YouTube shows, hosted locally.</li>
  <li>Making a clickable "watch this video" tile in a Notion / Slack / email where you need a still image.</li>
  <li>Building a custom video player and needing a poster image before the iframe loads.</li>
  <li>Saving a thumbnail for offline use as reference, content, or moodboard material.</li>
  <li>Getting the highest-resolution thumbnail without faffing about with the YouTube Data API.</li>
</ul>

<h3>The variants explained</h3>
<ul>
  <li><strong>maxresdefault</strong> (1280×720) — the original full-HD thumbnail. Only exists for videos uploaded in HD; otherwise the URL returns 404 and the preview goes blank.</li>
  <li><strong>sddefault</strong> (640×480) — generated for most videos in the modern era.</li>
  <li><strong>hqdefault</strong> (480×360) — <strong>always exists</strong>, going back to the earliest YouTube videos. Use this as your fallback.</li>
  <li><strong>mqdefault</strong> (320×180) and <strong>default</strong> (120×90) — small previews; useful for in-list rendering.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>maxresdefault often 404s.</strong> Older or lower-resolution uploads don't have it. Build your fallback chain: <code>maxresdefault → sddefault → hqdefault</code>.</li>
  <li><strong>Black bars on hqdefault.</strong> The 480×360 thumbnail is letterboxed for non-4:3 sources — there are bars top and bottom. <code>mqdefault</code> (320×180) has the correct 16:9 aspect for modern uploads.</li>
  <li><strong>Frames 1/2/3.</strong> YouTube also exposes <code>1.jpg</code>, <code>2.jpg</code>, <code>3.jpg</code> at the same path — three auto-extracted frames from the video. Sometimes one of those is what you actually want for a custom poster, and they're not in the default variant list.</li>
  <li><strong>It's still YouTube's image.</strong> Hot-linking is fine; rehosting on your own CDN is fine technically but check the licensing if you're using it commercially. The video creator may have copyright on the visual content of the frame.</li>
  <li><strong>WebP not supported here.</strong> YouTube also serves <code>.webp</code> versions (smaller files), but they're served from a different CDN path and not exposed by this tool.</li>
  <li><strong>Live streams and Shorts</strong> work fine — the URL parser handles all the modern forms — but live-stream thumbnails change while the stream is on air.</li>
</ul>
""",
    },
    "related": ["qr-code-generator", "image-to-base64", "url-encoder"],
}
