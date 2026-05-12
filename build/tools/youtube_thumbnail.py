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
        "pt": {"name": "Baixar Thumbnail do YouTube", "tagline": "Cole qualquer URL ou ID de vídeo do YouTube e baixe todos os tamanhos de thumbnail disponíveis — links diretos, sem upload, sem cadastro.", "description": "Downloader de thumbnails do YouTube gratuito. Extrai o ID do vídeo de qualquer URL do YouTube (watch, youtu.be, shorts, embed, /v/) e mostra todas as resoluções de thumbnail disponíveis com links de download diretos."},
        "pl": {"name": "Pobieranie Miniatur YouTube", "tagline": "Wklej dowolny URL albo ID wideo YouTube i pobierz każdy dostępny rozmiar miniatury — bezpośrednie linki, bez uploadu, bez rejestracji.", "description": "Darmowy downloader miniatur YouTube. Wyciąga ID wideo z dowolnej formy URL YouTube (watch, youtu.be, shorts, embed, /v/) i pokazuje wszystkie dostępne rozdzielczości miniatur z bezpośrednimi linkami do pobrania."},
        "ja": {"name": "YouTube サムネイルダウンローダー", "tagline": "YouTube の URL や動画 ID を貼り付けて、利用可能な全サイズのサムネイルを取得 — 直接ダウンロード、登録不要。", "description": "無料の YouTube サムネイルダウンローダー。YouTube の各種 URL 形式（watch、youtu.be、shorts、embed、/v/）から動画 ID を抽出し、利用可能なすべての解像度のサムネイルを直接ダウンロードリンクとともに表示します。"},
        "nl": {"name": "YouTube Thumbnail Downloader", "tagline": "Plak elke YouTube-URL of video-ID en grijp elke beschikbare thumbnail-size — directe downloadlinks, geen upload, geen registratie.", "description": "Gratis YouTube thumbnail downloader. Extraheert de video-ID uit elke YouTube-URL (watch, youtu.be, shorts, embed, /v/) en toont alle beschikbare thumbnail-resoluties met directe downloadlinks."},
        "tr": {"name": "YouTube Thumbnail İndirici", "tagline": "Herhangi bir YouTube URL'i veya video ID'sini yapıştır ve mevcut her thumbnail boyutunu yakala — doğrudan indirme linkleri, upload yok, kayıt yok.", "description": "Ücretsiz YouTube thumbnail indirici. Herhangi bir YouTube URL'inden (watch, youtu.be, shorts, embed, /v/) video ID'sini çıkarır ve doğrudan indirme linkleriyle mevcut tüm thumbnail çözünürlüklerini gösterir."},
        "id": {"name": "Pengunduh Thumbnail YouTube", "tagline": "Tempel URL YouTube atau ID video, dan ambil setiap ukuran thumbnail yang tersedia — link unduh langsung, tanpa upload, tanpa pendaftaran.", "description": "Pengunduh thumbnail YouTube gratis. Tempel URL YouTube atau ID video dan dapatkan link unduh langsung untuk setiap ukuran thumbnail yang tersedia (default, medium, high, standard, maxres). Tanpa upload, tanpa pelacakan."},
        "vi": {"name": "Tải Thumbnail YouTube", "tagline": "Dán URL YouTube hoặc ID video, và lấy mọi kích thước thumbnail có sẵn — link tải trực tiếp, không upload, không đăng ký.", "description": "Trình tải thumbnail YouTube miễn phí trực tuyến. Dán bất kỳ URL YouTube nào hoặc ID video và lấy tất cả các kích thước thumbnail có sẵn (mặc định, hq, mq, sd, maxres). Trình duyệt của bạn fetch trực tiếp từ CDN của YouTube — không có upload."},
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
        "pt": """
<h2>Para que serve?</h2>
<p>Todo vídeo do YouTube tem um pequeno conjunto de imagens de thumbnail pré-geradas em URLs previsíveis — o próprio YouTube as usa em resultados de busca, embeds e previews. Esta ferramenta extrai o ID de 11 caracteres do vídeo de qualquer formato de URL do YouTube (watch, youtu.be, Shorts, embed, /v/) e organiza todos os tamanhos disponíveis com links de download direto e botões para copiar a URL. Útil quando você precisa de um preview offline, uma imagem de destaque para um post de blog, um rich link no Discord/Slack ou um poster de fallback para um player de vídeo customizado.</p>

<h3>Quando usar</h3>
<ul>
  <li>Embedando um vídeo do YouTube em um post de blog e querendo o mesmo thumbnail que o YouTube mostra, hospedado localmente.</li>
  <li>Fazendo um tile clicável de "assista este vídeo" no Notion / Slack / e-mail onde você precisa de uma imagem estática.</li>
  <li>Construindo um player de vídeo customizado e precisando de uma imagem de poster antes do iframe carregar.</li>
  <li>Salvando uma thumbnail para uso offline como referência, conteúdo ou material de moodboard.</li>
  <li>Pegando a thumbnail de maior resolução sem ter que mexer com a YouTube Data API.</li>
</ul>

<h3>As variantes explicadas</h3>
<ul>
  <li><strong>maxresdefault</strong> (1280×720) — a thumbnail original em full-HD. Só existe para vídeos enviados em HD; caso contrário a URL retorna 404 e o preview fica em branco.</li>
  <li><strong>sddefault</strong> (640×480) — gerada para a maioria dos vídeos da era moderna.</li>
  <li><strong>hqdefault</strong> (480×360) — <strong>sempre existe</strong>, valendo desde os vídeos mais antigos do YouTube. Use como fallback.</li>
  <li><strong>mqdefault</strong> (320×180) e <strong>default</strong> (120×90) — previews pequenos; úteis para renderização em listas.</li>
</ul>

<h3>Cuidados comuns</h3>
<ul>
  <li><strong>maxresdefault frequentemente dá 404.</strong> Uploads antigos ou de baixa resolução não têm. Monte sua cadeia de fallback: <code>maxresdefault → sddefault → hqdefault</code>.</li>
  <li><strong>Barras pretas no hqdefault.</strong> A thumbnail 480×360 é letterboxed para fontes que não são 4:3 — há barras em cima e embaixo. O <code>mqdefault</code> (320×180) tem o aspect ratio 16:9 correto para uploads modernos.</li>
  <li><strong>Frames 1/2/3.</strong> O YouTube também expõe <code>1.jpg</code>, <code>2.jpg</code>, <code>3.jpg</code> no mesmo path — três frames auto-extraídos do vídeo. Às vezes um deles é o que você realmente quer para um poster customizado, e eles não estão na lista de variantes default.</li>
  <li><strong>A imagem ainda é do YouTube.</strong> Hot-linking é OK; rehospedar no seu próprio CDN tecnicamente é OK, mas verifique o licenciamento se for uso comercial. O criador do vídeo pode ter copyright sobre o conteúdo visual do frame.</li>
  <li><strong>WebP não é suportado aqui.</strong> O YouTube também serve versões <code>.webp</code> (arquivos menores), mas são servidas de um path de CDN diferente e não estão expostas por esta ferramenta.</li>
  <li><strong>Live streams e Shorts</strong> funcionam bem — o parser de URL trata todas as formas modernas — mas thumbnails de live stream mudam enquanto o stream está no ar.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Każde wideo na YouTube ma mały zestaw pre-generowanych obrazków miniatur pod przewidywalnymi URL-ami — sam YouTube ich używa w wynikach wyszukiwania, embedach i podglądach. To narzędzie wyciąga 11-znakowe ID wideo z dowolnej formy URL YouTube (watch, youtu.be, Shorts, embed, /v/) i rozkłada każdy dostępny rozmiar z bezpośrednimi linkami do pobrania i przyciskami copy URL. Przydatne, gdy potrzebujesz podglądu offline, hero image do posta blogowego, rich linka do Discorda/Slacka albo poster fallback dla custom video playera.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Embedowanie wideo YouTube w poście blogowym i chęć wykorzystania tej samej miniatury, którą pokazuje YouTube, hostowanej lokalnie.</li>
  <li>Robienie klikalnego kafla "obejrzyj to wideo" w Notion / Slacku / mailu, gdzie potrzebujesz statycznego obrazka.</li>
  <li>Budowa custom video playera i potrzeba poster image przed załadowaniem iframe'a.</li>
  <li>Zapis miniatury do offline'owego użycia jako referencja, treść albo materiał do moodboarda.</li>
  <li>Wyciągnięcie najwyższej rozdzielczości miniatury bez babrania się z YouTube Data API.</li>
</ul>

<h3>Warianty wytłumaczone</h3>
<ul>
  <li><strong>maxresdefault</strong> (1280×720) — oryginalna miniatura full-HD. Istnieje tylko dla wideo wgranych w HD; w przeciwnym razie URL zwraca 404 i podgląd zostaje pusty.</li>
  <li><strong>sddefault</strong> (640×480) — generowana dla większości wideo z nowoczesnej ery.</li>
  <li><strong>hqdefault</strong> (480×360) — <strong>zawsze istnieje</strong>, sięga najstarszych wideo YouTube. Używaj jako fallback.</li>
  <li><strong>mqdefault</strong> (320×180) i <strong>default</strong> (120×90) — małe podglądy; przydatne do renderowania na listach.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>maxresdefault często rzuca 404.</strong> Starsze albo niskorozdzielcze uploady tego nie mają. Zbuduj łańcuch fallbacków: <code>maxresdefault → sddefault → hqdefault</code>.</li>
  <li><strong>Czarne paski na hqdefault.</strong> Miniatura 480×360 jest letterboxowana dla źródeł nie-4:3 — z paskami na górze i dole. <code>mqdefault</code> (320×180) ma poprawne 16:9 dla nowoczesnych uploadów.</li>
  <li><strong>Klatki 1/2/3.</strong> YouTube wystawia też <code>1.jpg</code>, <code>2.jpg</code>, <code>3.jpg</code> pod tą samą ścieżką — trzy auto-wyciągnięte klatki z wideo. Czasem jedna z nich to faktycznie to, czego chcesz do custom postera, a nie ma ich w domyślnej liście wariantów.</li>
  <li><strong>To wciąż obrazek YouTube'a.</strong> Hot-linking jest OK; rehosting na własnym CDN-ie technicznie też, ale sprawdź licencjonowanie, jeśli używasz komercyjnie. Twórca wideo może mieć copyright na wizualną treść klatki.</li>
  <li><strong>WebP nieobsługiwany tutaj.</strong> YouTube serwuje też wersje <code>.webp</code> (mniejsze pliki), ale są podawane z innej ścieżki CDN i nie są wystawione przez to narzędzie.</li>
  <li><strong>Live streamy i Shortsy</strong> działają dobrze — parser URL obsługuje wszystkie nowoczesne formy — ale miniatury live streamu zmieniają się, gdy stream jest na żywo.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>YouTube のすべての動画には、予測可能な URL に置かれた事前生成のサムネイル画像があります。YouTube 自身も検索結果、埋め込み、プレビューに使っています。本ツールは YouTube のあらゆる URL 形式（watch、youtu.be、Shorts、embed、/v/）から 11 文字の動画 ID を取り出し、利用可能なすべてのサイズを直接ダウンロードリンクと URL コピーボタン付きで並べます。オフラインのプレビュー、ブログ記事のヒーロー画像、Discord/Slack のリッチリンク、自前プレイヤーのフォールバックポスターなどに便利です。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>ブログ記事に YouTube 動画を埋め込み、YouTube が表示するのと同じサムネイルを自前ホスティングしたいとき。</li>
  <li>Notion / Slack / メールで「この動画を見る」のクリック可能タイル用に静止画が欲しいとき。</li>
  <li>iframe 読み込み前のポスター画像が必要な、自前ビデオプレイヤーを作るとき。</li>
  <li>参考、コンテンツ、ムードボード用にサムネイルをオフライン保存したいとき。</li>
  <li>YouTube Data API を使わず最高解像度のサムネイルを取得したいとき。</li>
</ul>

<h3>各バリアントの説明</h3>
<ul>
  <li><strong>maxresdefault</strong>（1280×720） — オリジナルのフル HD サムネイル。HD でアップロードされた動画にのみ存在。なければ URL は 404 で、プレビューが空になります。</li>
  <li><strong>sddefault</strong>（640×480） — 比較的近年の動画では大抵生成されています。</li>
  <li><strong>hqdefault</strong>（480×360） — <strong>常に存在</strong>。最初期の YouTube 動画にもあります。フォールバックの定番。</li>
  <li><strong>mqdefault</strong>（320×180）と <strong>default</strong>（120×90） — 小さなプレビュー。リスト表示などに有用。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>maxresdefault はしばしば 404 です。</strong> 古い動画や低解像度動画には存在しません。フォールバック連鎖を組みましょう：<code>maxresdefault → sddefault → hqdefault</code>。</li>
  <li><strong>hqdefault は黒帯が付きます。</strong> 480×360 サムネイルは 4:3 以外のソースをレターボックス化するため、上下に帯が入ります。<code>mqdefault</code>（320×180）はモダンな動画と合った 16:9 です。</li>
  <li><strong>フレーム 1/2/3。</strong> YouTube は同じパスに <code>1.jpg</code>、<code>2.jpg</code>、<code>3.jpg</code> も公開しており、動画から自動抽出された 3 フレームです。カスタムポスターにはこれが向くこともあります。デフォルトのバリアント一覧には含まれません。</li>
  <li><strong>画像は YouTube のものです。</strong> ホットリンクは問題ありません。自前 CDN への再ホスティングも技術的には可能ですが、商用利用ならライセンスを確認してください。動画フレームの視覚内容に作者の著作権がある場合があります。</li>
  <li><strong>本ツールは WebP に対応しません。</strong> YouTube は <code>.webp</code> 版（より小さい）も配信していますが、別の CDN パスから提供されており、本ツールでは扱いません。</li>
  <li><strong>ライブ配信や Shorts</strong> も問題なく動作します（URL パーサが現代的な形式を網羅）。ただしライブ配信のサムネイルは配信中に変化します。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Elke YouTube-video heeft een kleine set pre-gegenereerde thumbnail-images op voorspelbare URLs — YouTube gebruikt ze zelf in zoekresultaten, embeds en previews. Deze tool extraheert de 11-karakter video-ID uit elke YouTube-URL-vorm (watch, youtu.be, Shorts, embed, /v/) en zet elke beschikbare size uit met directe downloadlinks en copy-URL-knoppen. Nuttig als je een offline preview nodig hebt, een hero-image voor een blogpost, een Discord/Slack rich link of een fallback-poster voor een custom video player.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Een YouTube-video embedden in een blogpost en dezelfde thumbnail willen die YouTube toont, lokaal gehost.</li>
  <li>Een klikbare "watch this video"-tile maken in Notion / Slack / email waar je een still image nodig hebt.</li>
  <li>Een custom video player bouwen en een poster-image nodig hebben voor de iframe laadt.</li>
  <li>Een thumbnail opslaan voor offline gebruik als referentie, content of moodboard-materiaal.</li>
  <li>De thumbnail in hoogste resolutie krijgen zonder gedoe met de YouTube Data API.</li>
</ul>

<h3>De varianten uitgelegd</h3>
<ul>
  <li><strong>maxresdefault</strong> (1280×720) — de originele full-HD thumbnail. Bestaat alleen voor video's geüpload in HD; anders geeft de URL 404 en blijft de preview leeg.</li>
  <li><strong>sddefault</strong> (640×480) — gegenereerd voor de meeste video's in het moderne tijdperk.</li>
  <li><strong>hqdefault</strong> (480×360) — <strong>bestaat altijd</strong>, terug tot de vroegste YouTube-video's. Gebruik dit als je fallback.</li>
  <li><strong>mqdefault</strong> (320×180) en <strong>default</strong> (120×90) — kleine previews; nuttig voor in-list rendering.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>maxresdefault 404't vaak.</strong> Oudere of lager-resolutie uploads hebben hem niet. Bouw je fallback-ketting: <code>maxresdefault → sddefault → hqdefault</code>.</li>
  <li><strong>Zwarte balken op hqdefault.</strong> De 480×360 thumbnail is letterboxed voor non-4:3 bronnen — er zijn balken boven en onder. <code>mqdefault</code> (320×180) heeft de juiste 16:9 aspect voor moderne uploads.</li>
  <li><strong>Frames 1/2/3.</strong> YouTube exposet ook <code>1.jpg</code>, <code>2.jpg</code>, <code>3.jpg</code> op hetzelfde pad — drie auto-extracted frames uit de video. Soms is een daarvan wat je daadwerkelijk wil voor een custom poster, en ze staan niet in de default-variantenlijst.</li>
  <li><strong>Het is nog steeds YouTube's image.</strong> Hot-linking is prima; rehosten op je eigen CDN is technisch prima maar check de licensing als je het commercieel gebruikt. De videomaker kan copyright hebben op de visuele content van het frame.</li>
  <li><strong>WebP hier niet ondersteund.</strong> YouTube serveert ook <code>.webp</code>-versies (kleinere files), maar die worden vanaf een ander CDN-pad geserveerd en niet door deze tool blootgesteld.</li>
  <li><strong>Live streams en Shorts</strong> werken prima — de URL-parser handelt alle moderne vormen af — maar live-stream thumbnails veranderen terwijl de stream live is.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Her YouTube videosunun öngörülebilir URL'lerde önceden üretilmiş küçük bir thumbnail görsel seti vardır — YouTube bunları kendisi arama sonuçlarında, embed'lerde ve önizlemelerde kullanır. Bu araç herhangi bir YouTube URL biçiminden (watch, youtu.be, Shorts, embed, /v/) 11 karakterlik video ID'sini çıkarır ve mevcut her boyutu doğrudan indirme linkleri ve URL-kopyala düğmeleriyle düzenler. Çevrimdışı önizlemeye, bir blog gönderisi için hero görseline, Discord/Slack zengin linkine veya özel video player için yedek poster'a ihtiyacın olduğunda kullanışlıdır.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Bir blog gönderisine bir YouTube videosu gömme ve YouTube'un gösterdiği aynı thumbnail'i, yerel olarak barındırma.</li>
  <li>Hâlâ bir görsele ihtiyacın olduğu Notion / Slack / e-postada tıklanabilir "bu videoyu izle" tile yapma.</li>
  <li>Özel video player kurma ve iframe yüklenmeden önce bir poster görseline ihtiyaç duyma.</li>
  <li>Referans, içerik veya moodboard materyali olarak çevrimdışı kullanım için bir thumbnail kaydetme.</li>
  <li>YouTube Data API ile uğraşmadan en yüksek çözünürlüklü thumbnail'i alma.</li>
</ul>

<h3>Varyantlar açıklandı</h3>
<ul>
  <li><strong>maxresdefault</strong> (1280×720) — orijinal full-HD thumbnail. Yalnızca HD yüklenen videolar için var; aksi takdirde URL 404 döner ve önizleme boş olur.</li>
  <li><strong>sddefault</strong> (640×480) — modern çağda çoğu video için üretilir.</li>
  <li><strong>hqdefault</strong> (480×360) — <strong>her zaman vardır</strong>, en eski YouTube videolarına kadar gider. Bunu yedek olarak kullan.</li>
  <li><strong>mqdefault</strong> (320×180) ve <strong>default</strong> (120×90) — küçük önizlemeler; in-list render için kullanışlıdır.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>maxresdefault sıklıkla 404 verir.</strong> Eski veya düşük çözünürlüklü yüklemelerde yok. Yedek zincirini kur: <code>maxresdefault → sddefault → hqdefault</code>.</li>
  <li><strong>hqdefault'ta siyah bantlar.</strong> 480×360 thumbnail 4:3 olmayan kaynaklar için letterbox edilir — üstte ve altta bantlar vardır. <code>mqdefault</code> (320×180) modern yüklemeler için doğru 16:9 en-boyuna sahiptir.</li>
  <li><strong>1/2/3 kareleri.</strong> YouTube aynı path'te <code>1.jpg</code>, <code>2.jpg</code>, <code>3.jpg</code>'i de açığa çıkarır — videodan otomatik olarak çıkarılan üç kare. Bazen özel bir poster için gerçekten istediğin biri budur ve varsayılan varyant listesinde değildirler.</li>
  <li><strong>Hâlâ YouTube'un görseli.</strong> Hot-link yapma iyidir; kendi CDN'inde yeniden barındırma teknik olarak iyidir ama ticari kullanıyorsan lisanslamayı kontrol et. Video oluşturucusu karenin görsel içeriği üzerinde telif hakkına sahip olabilir.</li>
  <li><strong>WebP burada desteklenmiyor.</strong> YouTube ayrıca <code>.webp</code> sürümlerini de sunar (daha küçük dosyalar), ama farklı bir CDN path'ten servis edilirler ve bu araç tarafından açığa çıkarılmazlar.</li>
  <li><strong>Canlı yayınlar ve Shorts</strong> iyi çalışır — URL parser tüm modern formları işler — ama canlı yayın thumbnail'leri yayın sırasında değişir.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Setiap video YouTube punya sekumpulan thumbnail image yang sudah di-generate sebelumnya di URL yang bisa diprediksi — YouTube sendiri menggunakannya di hasil pencarian, embed, dan preview. Tool ini mengekstrak video ID 11 karakter dari bentuk URL YouTube apa pun (watch, youtu.be, Shorts, embed, /v/) dan menyusun setiap ukuran yang tersedia dengan link download langsung dan tombol copy-URL. Berguna saat kamu butuh preview offline, hero image untuk blog post, rich link Discord/Slack, atau poster fallback untuk video player custom.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Mengembed video YouTube di blog post dan meng-host sendiri thumbnail yang sama dengan yang ditampilkan YouTube.</li>
  <li>Membuat tile "tonton video ini" yang clickable di Notion / Slack / email di mana kamu masih perlu image.</li>
  <li>Menyiapkan video player custom dan butuh poster image sebelum iframe dimuat.</li>
  <li>Menyimpan thumbnail untuk pemakaian offline sebagai referensi, materi konten, atau moodboard.</li>
  <li>Mendapatkan thumbnail resolusi tertinggi tanpa berurusan dengan YouTube Data API.</li>
</ul>

<h3>Varian dijelaskan</h3>
<ul>
  <li><strong>maxresdefault</strong> (1280×720) — thumbnail full-HD orisinal. Hanya ada untuk video yang di-upload di HD; jika tidak, URL mengembalikan 404 dan preview akan kosong.</li>
  <li><strong>sddefault</strong> (640×480) — di-generate untuk sebagian besar video di era modern.</li>
  <li><strong>hqdefault</strong> (480×360) — <strong>selalu ada</strong>, kembali ke video YouTube paling awal. Pakai ini sebagai fallback.</li>
  <li><strong>mqdefault</strong> (320×180) dan <strong>default</strong> (120×90) — preview kecil; berguna untuk render in-list.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>maxresdefault sering 404.</strong> Tidak ada di upload lama atau resolusi rendah. Susun rantai fallback: <code>maxresdefault → sddefault → hqdefault</code>.</li>
  <li><strong>Black bar di hqdefault.</strong> Thumbnail 480×360 di-letterbox untuk sumber non-4:3 — ada bar di atas dan bawah. <code>mqdefault</code> (320×180) punya aspect ratio 16:9 yang benar untuk upload modern.</li>
  <li><strong>Frame 1/2/3.</strong> YouTube juga meng-expose <code>1.jpg</code>, <code>2.jpg</code>, <code>3.jpg</code> di path yang sama — tiga frame yang diekstrak otomatis dari video. Kadang salah satunya adalah yang sebenarnya kamu inginkan untuk poster custom, dan mereka tidak ada di daftar varian default.</li>
  <li><strong>Tetap image milik YouTube.</strong> Hot-linking baik-baik saja; meng-host ulang di CDN sendiri secara teknis boleh tapi cek lisensi jika kamu menggunakannya secara komersial. Pembuat video mungkin punya copyright atas konten visual frame.</li>
  <li><strong>WebP tidak didukung di sini.</strong> YouTube juga menyajikan versi <code>.webp</code> (file lebih kecil), tapi disajikan dari path CDN berbeda dan tidak di-expose oleh tool ini.</li>
  <li><strong>Live stream dan Shorts</strong> bekerja dengan baik — URL parser menangani semua bentuk modern — tapi thumbnail live stream berubah selama broadcast.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>YouTube tự động sinh thumbnail cho mỗi video ở nhiều kích thước (default, hq, mq, sd, maxres). Bạn có thể fetch chúng trực tiếp từ CDN của YouTube mà không cần API key, login hoặc upload — chỉ cần biết video ID. Tool này dán URL YouTube hoặc ID, hiển thị từng thumbnail có sẵn với link tải trực tiếp.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Tạo content cover với thumbnail của video YouTube được embed.</li>
  <li>Lấy ảnh archive của thumbnail trước khi creator update nó.</li>
  <li>Build công cụ liệt kê hiển thị thumbnail video.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>maxres không phải lúc nào cũng có.</strong> YouTube tạo maxresdefault.jpg chỉ cho video độ phân giải đủ cao. Đối với video cũ hoặc thấp, fetch return 404.</li>
  <li><strong>Thumbnail thay đổi.</strong> Creator có thể update thumbnail bất cứ lúc nào. URL ổn định nhưng image bytes thay đổi — nếu bạn cần lock version cụ thể, download và lưu trữ.</li>
  <li><strong>Đừng share trái phép.</strong> Thumbnail có copyright. OK để embed video YouTube; xem điều khoản trước khi dùng thumbnail trong context khác.</li>
</ul>
""",
    },
    "related": ["qr-code-generator", "image-to-base64", "url-encoder"],
    "howto": {"flow": "transform", "action": "convert", "noun": "YouTube URL"},
}
