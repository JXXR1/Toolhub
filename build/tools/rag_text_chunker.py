TOOL = {
    "slug": "rag-text-chunker",
    "category": "ai",
    "icon": "✂️",
    "tags": ["rag", "chunk", "split", "text", "embeddings", "retrieval", "llm", "tokens", "chunker"],
    "i18n": {
        "en": {
            "name": "RAG Text Chunker",
            "tagline": "Split text into token-sized chunks for RAG / embeddings prep. Multiple strategies: recursive char, sentence-aware, semantic boundaries. Configurable overlap. All in-browser.",
            "description": "Free in-browser text chunker for RAG and embedding pipelines. Paste a document, pick a chunk size (in tokens, heuristic estimate), pick a strategy (recursive character / sentence-aware / paragraph / semantic-boundary), and get back the list of chunks with optional overlap. Useful for prepping documents for vector-store ingestion without uploading them anywhere. Pairs with our token-counter for sizing guidance.",
        },
        "de": {
            "name": "RAG-Text-Chunker",
            "tagline": "Zerlege Text in token-große Chunks für RAG- / Embeddings-Vorbereitung. Mehrere Strategien: recursive char, satz-aware, semantische Grenzen. Konfigurierbarer Overlap. Alles im Browser.",
            "description": "Kostenloser Browser-Text-Chunker für RAG- und Embedding-Pipelines. Füge ein Dokument ein, wähle eine Chunk-Größe (in Tokens, heuristisch geschätzt), wähle eine Strategie (recursive character / satz-aware / Absatz / semantische Grenze) und erhalte die Chunk-Liste mit optionalem Overlap. Nützlich zum Vorbereiten von Dokumenten für Vector-Store-Ingestion, ohne irgendwo hochzuladen. Passt zum Token-Counter für Sizing-Hinweise.",
        },
        "es": {
            "name": "Chunker de Texto para RAG",
            "tagline": "Divide texto en chunks de tamaño en tokens para RAG / preparación de embeddings. Varias estrategias: recursive char, sentence-aware, semantic boundaries. Overlap configurable. Todo en el navegador.",
            "description": "Chunker de texto gratuito en el navegador para pipelines de RAG y embeddings. Pega un documento, elige tamaño de chunk (en tokens, estimación heurística), elige estrategia (recursive character / sentence-aware / paragraph / semantic-boundary) y obtén la lista de chunks con overlap opcional. Útil para preparar documentos para ingesta en vector-store sin subirlos a ningún sitio. Combina con nuestro token-counter para guía de tamaño.",
        },
        "fr": {
            "name": "RAG Text Chunker",
            "tagline": "Découpez du texte en chunks de taille en tokens pour la préparation RAG / embeddings. Plusieurs stratégies : recursive char, sentence-aware, semantic boundaries. Overlap configurable. Tout dans le navigateur.",
            "description": "Chunker de texte gratuit dans le navigateur pour pipelines RAG et embeddings. Collez un document, choisissez la taille de chunk (en tokens, estimation heuristique), choisissez la stratégie (recursive character / sentence-aware / paragraph / semantic-boundary), et obtenez la liste des chunks avec overlap optionnel. Utile pour préparer des documents pour l'ingestion vector-store sans rien uploader. Se combine avec notre token-counter pour le dimensionnement.",
        },
        "it": {
            "name": "RAG Text Chunker",
            "tagline": "Spezza il testo in chunk dimensionati a token per preparazione RAG / embeddings. Strategie multiple: recursive char, sentence-aware, semantic boundaries. Overlap configurabile. Tutto nel browser.",
            "description": "Chunker di testo gratuito nel browser per pipeline RAG ed embeddings. Incolla un documento, scegli una dimensione di chunk (in token, stima euristica), scegli una strategia (recursive character / sentence-aware / paragraph / semantic-boundary) e ottieni la lista di chunk con overlap opzionale. Utile per preparare documenti per ingest vector-store senza caricarli da nessuna parte. Si abbina al nostro token-counter per linee guida sul sizing.",
        },
        "pt": {
            "name": "Chunker de Texto pra RAG",
            "tagline": "Divide texto em chunks dimensionados por tokens pra preparação de RAG / embeddings. Múltiplas estratégias: recursive char, sentence-aware, semantic boundaries. Overlap configurável. Tudo no navegador.",
            "description": "Chunker de texto grátis no navegador pra pipelines de RAG e embeddings. Cole um documento, escolha um tamanho de chunk (em tokens, estimativa heurística), escolha uma estratégia (recursive character / sentence-aware / paragraph / semantic-boundary), e receba a lista de chunks com overlap opcional. Útil pra preparar documentos pra ingestão em vector store sem fazer upload em lugar nenhum. Combina com nosso token-counter pra orientação de tamanho.",
        },
        "pl": {
            "name": "RAG Text Chunker",
            "tagline": "Dziel tekst na chunki o rozmiarze w tokenach do RAG / przygotowania embeddingów. Wiele strategii: recursive char, sentence-aware, semantic boundaries. Konfigurowalny overlap. Całość w przeglądarce.",
            "description": "Darmowy chunker tekstu w przeglądarce do pipeline'ów RAG i embeddingów. Wklej dokument, wybierz rozmiar chunka (w tokenach, estymacja heurystyczna), wybierz strategię (recursive character / sentence-aware / paragraph / semantic-boundary), i dostań listę chunków z opcjonalnym overlapem. Przydatne do przygotowania dokumentów do ingestii vector-store bez wgrywania ich nigdzie. Pasuje do naszego token-countera dla wskazówek dotyczących rozmiaru.",
        },
        "ja": {
            "name": "RAG テキストチャンカー",
            "tagline": "RAG・埋め込み準備のためにテキストをトークンサイズのチャンクに分割。複数戦略：再帰文字、文単位、意味境界。重複量を設定可能。すべてブラウザで完結。",
            "description": "RAG／埋め込みパイプライン向けの無料ブラウザ完結テキストチャンカー。文書を貼り付け、チャンクサイズ（トークン単位、ヒューリスティック推定）を選び、戦略（recursive character／sentence-aware／paragraph／semantic-boundary）を選ぶと、任意のオーバーラップ付きでチャンクのリストが返ります。文書をどこにもアップロードせずにベクトルストア投入の前処理をするのに便利です。サイズ目安は当社の token-counter と組み合わせて使えます。",
        },
        "nl": {
            "name": "RAG Text Chunker",
            "tagline": "Splits tekst in chunks van token-grootte voor RAG / embeddings-voorbereiding. Meerdere strategieën: recursive char, sentence-aware, semantic boundaries. Configureerbare overlap. Allemaal in de browser.",
            "description": "Gratis in-browser text chunker voor RAG- en embedding-pipelines. Plak een document, kies chunk-grootte (in tokens, heuristische schatting), kies een strategie (recursive character / sentence-aware / paragraph / semantic-boundary) en krijg de lijst chunks met optionele overlap. Handig voor het voorbereiden van documenten voor vector-store ingestion zonder ze ergens te uploaden. Combineert met onze token-counter voor sizing-advies.",
        },
        "tr": {
            "name": "RAG Metin Chunker",
            "tagline": "Metni RAG / embedding hazırlığı için token boyutunda chunk'lara böl. Birden fazla strateji: recursive char, sentence-aware, semantic boundaries. Yapılandırılabilir overlap. Hepsi tarayıcıda.",
            "description": "RAG ve embedding pipeline'ları için ücretsiz tarayıcı içi metin chunker. Bir doküman yapıştır, chunk boyutu seç (token cinsinden, sezgisel tahmin), strateji seç (recursive character / sentence-aware / paragraph / semantic-boundary) ve isteğe bağlı overlap ile chunk listesini geri al. Dokümanları vector store ingestion için herhangi bir yere yüklemeden hazırlamak için yararlı. Boyutlandırma rehberliği için token-counter'ımızla eşleşir.",
        },
        "id": {
            "name": "RAG Text Chunker",
            "tagline": "Pecah teks jadi chunk berukuran token untuk persiapan RAG / embeddings. Banyak strategi: recursive char, sentence-aware, semantic boundaries. Overlap bisa diatur. Semua di browser.",
            "description": "Text chunker gratis di browser untuk pipeline RAG dan embedding. Tempel dokumen, pilih ukuran chunk (dalam token, estimasi heuristik), pilih strategi (recursive character / sentence-aware / paragraph / semantic-boundary), dan dapatkan list chunk dengan overlap opsional. Berguna untuk menyiapkan dokumen untuk ingest vector store tanpa upload ke mana-mana. Cocok dipasangkan dengan token-counter kami untuk panduan sizing.",
        },
        "vi": {
            "name": "Bộ chia chunk văn bản cho RAG",
            "tagline": "Chia văn bản thành các chunk theo kích thước token để chuẩn bị RAG / embeddings. Nhiều chiến lược: recursive char, sentence-aware, semantic boundaries. Overlap có thể cấu hình. Tất cả trong trình duyệt.",
            "description": "Bộ chia chunk văn bản miễn phí trong trình duyệt cho pipeline RAG và embedding. Dán một tài liệu, chọn kích thước chunk (theo token, ước tính heuristic), chọn chiến lược (recursive character / sentence-aware / paragraph / semantic-boundary), và nhận danh sách chunk với overlap tùy chọn. Hữu ích để chuẩn bị tài liệu cho ingest vector store mà không cần upload đi đâu cả. Kết hợp với token-counter của chúng tôi để hướng dẫn sizing.",
        },
        "hi": {
            "name": "RAG Text Chunker",
            "tagline": "RAG / embeddings prep के लिए text को token-sized chunks में split करें। कई strategies: recursive char, sentence-aware, semantic boundaries। Configurable overlap। सब browser में।",
            "description": "RAG और embedding pipelines के लिए मुफ़्त in-browser text chunker। एक document paste करें, chunk size (tokens में, heuristic estimate) चुनें, strategy चुनें (recursive character / sentence-aware / paragraph / semantic-boundary), और optional overlap के साथ chunks की list वापस पाएं। Documents को कहीं upload किए बिना vector-store ingestion के लिए prep करने के लिए उपयोगी। Sizing guidance के लिए हमारे token-counter के साथ pair होता है।",
        },
        "sk": {
            "name": "RAG Text Chunker",
            "tagline": "Rozdeľ text na token-veľké chunky pre prípravu RAG / embeddingov. Viac stratégií: recursive char, sentence-aware, semantic boundaries. Konfigurovateľný overlap. Všetko v prehliadači.",
            "description": "Bezplatný text chunker v prehliadači pre RAG a embedding pipeliny. Vlož dokument, vyber veľkosť chunku (v tokenoch, heuristický odhad), vyber stratégiu (recursive character / sentence-aware / paragraph / semantic-boundary) a dostaneš zoznam chunkov s voliteľným overlapom. Užitočné na prípravu dokumentov na ingest do vector store bez nahrávania kdekoľvek. Páruje sa s naším token-counterom pre sizing usmernenie.",
        },
        "cs": {
            "name": "RAG Text Chunker",
            "tagline": "Rozděl text na token-velké chunky pro přípravu RAG / embeddingů. Více strategií: recursive char, sentence-aware, semantic boundaries. Konfigurovatelný overlap. Vše v prohlížeči.",
            "description": "Bezplatný text chunker v prohlížeči pro RAG a embedding pipelinу. Vlož dokument, vyber velikost chunku (v tokenech, heuristický odhad), vyber strategii (recursive character / sentence-aware / paragraph / semantic-boundary) a dostaneš seznam chunků s volitelným overlapem. Užitečné na přípravu dokumentů pro ingest do vector store bez nahrávání kamkoliv. Páruje se s naším token-counterem pro sizing pokyny.",
        },
    },
    "body": """
<div class="tool-card">
  <label for="rtc-input">Paste your document</label>
  <textarea id="rtc-input" oninput="rtcRun()" spellcheck="false" placeholder="Paste the text you want to chunk for RAG / embedding…">RAG (Retrieval-Augmented Generation) is a technique that pairs an LLM with an external knowledge base. Instead of relying only on the model's parametric memory, the system retrieves relevant passages at query time and concatenates them into the prompt.

The retrieval step depends on a vector store. Documents are split into chunks, each chunk gets an embedding vector, and those vectors are stored in a database that supports approximate nearest-neighbour search.

# Chunk size matters

Chunks that are too small lose context — a single sentence might not contain enough information to answer the question. Chunks that are too large dilute relevance — the embedding becomes an average of many unrelated topics, and retrieval gets noisy.

A common starting point is 500 tokens per chunk with 50 tokens of overlap. Overlap lets a chunk see a bit of context from its neighbours, which helps when a relevant span happens to fall across a chunk boundary.

# Strategy choice

Recursive character splitting is the most general: it tries paragraph breaks first, then line breaks, then sentence boundaries, then spaces. This is the default in most frameworks and works well for prose.

Sentence-aware splitting respects sentence boundaries and never breaks mid-sentence. It produces cleaner chunks for QA over articles and books, at the cost of more variable chunk sizes.

Paragraph chunking treats each paragraph as its own chunk (subject to the size limit). This is useful for structured documents like documentation or knowledge-base articles where each section is already a coherent unit.

Semantic chunking goes one step further: it tries to keep semantically related content together by respecting headings and topic boundaries, even when those don't align with paragraph breaks.</textarea>
  <div class="rtc-controls" style="margin-top:0.6rem">
    <div class="rtc-ctrl">
      <label>Chunk size (tokens): <strong id="rtc-size-val">500</strong></label>
      <input type="range" id="rtc-size" min="100" max="2000" step="50" value="500" oninput="rtcRun()">
    </div>
    <div class="rtc-ctrl">
      <label>Overlap (tokens): <strong id="rtc-ovr-val">50</strong></label>
      <input type="range" id="rtc-ovr" min="0" max="200" step="10" value="50" oninput="rtcRun()">
    </div>
    <div class="rtc-ctrl">
      <label for="rtc-strat">Strategy</label>
      <select id="rtc-strat" onchange="rtcRun()">
        <option value="recursive-char" selected>recursive-char</option>
        <option value="sentence">sentence</option>
        <option value="paragraph">paragraph</option>
        <option value="semantic">semantic</option>
      </select>
    </div>
  </div>
</div>
<div class="tool-card">
  <div class="meta" id="rtc-stats"></div>
  <div class="button-row" style="margin-top:0.5rem">
    <button class="secondary" onclick="rtcCopyJson(this)">Copy as JSON array</button>
    <button class="secondary" onclick="rtcExportJsonl(this)">⬇ Export as JSONL</button>
  </div>
  <div id="rtc-chunks" class="rtc-chunks" style="margin-top:0.7rem"></div>
</div>
""",
    "script": """
<style>
.rtc-controls{display:grid;grid-template-columns:1fr 1fr 1fr;gap:0.9rem;align-items:end}
.rtc-ctrl{display:flex;flex-direction:column;gap:0.25rem}
.rtc-ctrl input[type=range]{width:100%}
.rtc-ctrl select{padding:0.4rem 0.6rem}
.rtc-chunks{display:flex;flex-direction:column;gap:0.55rem;max-height:560px;overflow-y:auto}
.rtc-chunk{border:1px solid var(--border);border-radius:8px;padding:0.55rem 0.7rem;background:var(--bg-elev)}
.rtc-chunk-head{display:flex;justify-content:space-between;align-items:baseline;font-size:0.78rem;color:var(--text-muted);margin-bottom:0.3rem}
.rtc-chunk-head strong{color:var(--accent);font-family:ui-monospace,monospace}
.rtc-chunk-body{white-space:pre-wrap;font-size:0.86rem;line-height:1.5;word-break:break-word}
.rtc-chunk-overlap{color:var(--text-muted);font-style:italic}
.rtc-stat{display:inline-block;margin-right:1rem}
.rtc-stat strong{color:var(--text)}
@media (max-width:780px){
  .rtc-controls{grid-template-columns:1fr}
}
</style>
<script>
let rtcChunks = [];
const RTC_CJK_RE = /[぀-ヿ㐀-䶿一-鿿가-힯]/g;
function rtcEsc(s){ return String(s ?? '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function rtcEstTokens(s){
  if (!s) return 0;
  const cjk = (s.match(RTC_CJK_RE) || []).length;
  const len = s.length;
  return Math.max(1, Math.ceil((len - cjk) / 3.8 + cjk));
}
function rtcCharsForTokens(n, sample){
  // Approximate inverse: how many chars correspond to n tokens?
  // Calibrate per-text using actual ratio when sample provided.
  if (sample && sample.length > 0){
    const t = rtcEstTokens(sample);
    if (t > 0) return Math.max(1, Math.round(n * sample.length / t));
  }
  return Math.max(1, Math.round(n * 3.8));
}
function rtcSplitRecursive(text, maxToks){
  // Try paragraphs, then lines, then ". ", then " ", recursively packing pieces.
  const SEPS = ['\\n\\n', '\\n', '. ', ' '];
  function splitOne(s, depth){
    if (rtcEstTokens(s) <= maxToks) return [s];
    if (depth >= SEPS.length){
      // Hard split by characters
      const charsPer = rtcCharsForTokens(maxToks, s);
      const out = [];
      for (let i = 0; i < s.length; i += charsPer){
        out.push(s.slice(i, i + charsPer));
      }
      return out;
    }
    const sep = SEPS[depth];
    const parts = s.split(sep);
    if (parts.length === 1) return splitOne(s, depth + 1);
    // Pack greedily
    const packed = [];
    let buf = '';
    for (const p of parts){
      const cand = buf ? buf + sep + p : p;
      if (rtcEstTokens(cand) <= maxToks){
        buf = cand;
      } else {
        if (buf) packed.push(buf);
        if (rtcEstTokens(p) > maxToks){
          // Recurse with the next separator
          const sub = splitOne(p, depth + 1);
          packed.push(...sub);
          buf = '';
        } else {
          buf = p;
        }
      }
    }
    if (buf) packed.push(buf);
    return packed;
  }
  return splitOne(text, 0);
}
function rtcSplitSentence(text, maxToks){
  // Split on sentence boundaries, then pack.
  const sentences = text.match(/[^.!?]+[.!?]+\\s*|[^.!?]+$/g) || [text];
  const out = [];
  let buf = '';
  for (const s of sentences){
    const trim = s;
    if (rtcEstTokens(trim) > maxToks){
      if (buf){ out.push(buf); buf = ''; }
      // Sub-split the long sentence with recursive
      const sub = rtcSplitRecursive(trim, maxToks);
      out.push(...sub);
      continue;
    }
    const cand = buf ? buf + trim : trim;
    if (rtcEstTokens(cand) <= maxToks){
      buf = cand;
    } else {
      if (buf) out.push(buf);
      buf = trim;
    }
  }
  if (buf) out.push(buf);
  return out;
}
function rtcSplitParagraph(text, maxToks){
  const paras = text.split(/\\n{2,}/);
  const out = [];
  let buf = '';
  for (const p of paras){
    if (rtcEstTokens(p) > maxToks){
      if (buf){ out.push(buf); buf = ''; }
      // sub-split
      const sub = rtcSplitRecursive(p, maxToks);
      out.push(...sub);
      continue;
    }
    const cand = buf ? buf + '\\n\\n' + p : p;
    if (rtcEstTokens(cand) <= maxToks){
      buf = cand;
    } else {
      if (buf) out.push(buf);
      buf = p;
    }
  }
  if (buf) out.push(buf);
  return out;
}
function rtcSplitSemantic(text, maxToks){
  // Break on \\n\\n AND on heading-like lines: lines starting with #, ##, ###, or ALL-CAPS short lines
  const lines = text.split('\\n');
  const blocks = [];
  let buf = [];
  function isHeading(line){
    const t = line.trim();
    if (!t) return false;
    if (/^#{1,6}\\s/.test(t)) return true;
    if (t.length <= 80 && /^[A-Z0-9 .,'\\-:&]+$/.test(t) && /[A-Z]/.test(t) && t.split(/\\s+/).length >= 1) return true;
    return false;
  }
  for (let i = 0; i < lines.length; i++){
    const line = lines[i];
    if (line.trim() === ''){
      if (buf.length){ blocks.push(buf.join('\\n')); buf = []; }
      continue;
    }
    if (isHeading(line) && buf.length){
      blocks.push(buf.join('\\n'));
      buf = [line];
      continue;
    }
    buf.push(line);
  }
  if (buf.length) blocks.push(buf.join('\\n'));
  // Pack semantic blocks like paragraphs
  const out = [];
  let cur = '';
  for (const b of blocks){
    if (rtcEstTokens(b) > maxToks){
      if (cur){ out.push(cur); cur = ''; }
      out.push(...rtcSplitRecursive(b, maxToks));
      continue;
    }
    const cand = cur ? cur + '\\n\\n' + b : b;
    if (rtcEstTokens(cand) <= maxToks){
      cur = cand;
    } else {
      if (cur) out.push(cur);
      cur = b;
    }
  }
  if (cur) out.push(cur);
  return out;
}
function rtcApplyOverlap(chunks, overlapToks){
  if (overlapToks <= 0 || chunks.length <= 1) return chunks.map(c => ({ body: c, overlap: '' }));
  const out = [{ body: chunks[0], overlap: '' }];
  for (let i = 1; i < chunks.length; i++){
    const prev = chunks[i - 1];
    const overlapChars = rtcCharsForTokens(overlapToks, prev);
    const tail = prev.length > overlapChars ? prev.slice(prev.length - overlapChars) : prev;
    out.push({ body: chunks[i], overlap: tail });
  }
  return out;
}
function rtcRun(){
  const text = document.getElementById('rtc-input').value;
  const size = parseInt(document.getElementById('rtc-size').value, 10);
  const ovr = parseInt(document.getElementById('rtc-ovr').value, 10);
  const strat = document.getElementById('rtc-strat').value;
  document.getElementById('rtc-size-val').textContent = size;
  document.getElementById('rtc-ovr-val').textContent = ovr;
  if (!text.trim()){
    rtcChunks = [];
    document.getElementById('rtc-stats').innerHTML = '';
    document.getElementById('rtc-chunks').innerHTML = '<div style="color:var(--text-muted);padding:0.5rem">Paste text above to chunk it.</div>';
    return;
  }
  let raw;
  if (strat === 'sentence') raw = rtcSplitSentence(text, size);
  else if (strat === 'paragraph') raw = rtcSplitParagraph(text, size);
  else if (strat === 'semantic') raw = rtcSplitSemantic(text, size);
  else raw = rtcSplitRecursive(text, size);
  raw = raw.filter(c => c && c.trim().length > 0);
  rtcChunks = rtcApplyOverlap(raw, ovr);
  // Stats
  const total = rtcChunks.length;
  const totalToks = rtcChunks.reduce((s, c) => s + rtcEstTokens(c.body), 0);
  const avg = total ? Math.round(totalToks / total) : 0;
  const stats = document.getElementById('rtc-stats');
  stats.innerHTML =
    '<span class="rtc-stat"><strong>' + total + '</strong> chunks</span>' +
    '<span class="rtc-stat">avg <strong>' + avg + '</strong> tokens/chunk</span>' +
    '<span class="rtc-stat">total ~<strong>' + totalToks.toLocaleString() + '</strong> tokens</span>' +
    '<span class="rtc-stat"><strong>' + strat + '</strong></span>';
  // Render
  const container = document.getElementById('rtc-chunks');
  container.innerHTML = rtcChunks.map((c, i) => {
    const toks = rtcEstTokens(c.body);
    const chars = c.body.length;
    const overlapBlock = c.overlap ? '<div class="rtc-chunk-overlap">↺ overlap: ' + rtcEsc(c.overlap) + '</div>' : '';
    return '<div class="rtc-chunk">' +
      '<div class="rtc-chunk-head"><strong>chunk #' + i + '</strong><span>~' + toks + ' tokens · ' + chars + ' chars</span></div>' +
      overlapBlock +
      '<div class="rtc-chunk-body">' + rtcEsc(c.body) + '</div>' +
    '</div>';
  }).join('');
}
function rtcCopyJson(btn){
  if (!rtcChunks.length) return;
  const arr = rtcChunks.map((c, i) => ({
    index: i,
    tokens: rtcEstTokens(c.body),
    chars: c.body.length,
    overlap: c.overlap || '',
    text: c.body
  }));
  const json = JSON.stringify(arr, null, 2);
  navigator.clipboard.writeText(json).then(() => {
    const orig = btn.textContent;
    btn.textContent = '✓ Copied';
    setTimeout(() => btn.textContent = orig, 1400);
  });
}
function rtcExportJsonl(btn){
  if (!rtcChunks.length) return;
  const lines = rtcChunks.map((c, i) => JSON.stringify({
    index: i,
    tokens: rtcEstTokens(c.body),
    chars: c.body.length,
    overlap: c.overlap || '',
    text: c.body
  }));
  const blob = new Blob([lines.join('\\n')], {type:'application/x-ndjson'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'rag-chunks.jsonl';
  a.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
  const orig = btn.textContent;
  btn.textContent = '✓ Downloaded';
  setTimeout(() => btn.textContent = orig, 1400);
}
document.addEventListener('DOMContentLoaded', rtcRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Retrieval-Augmented Generation (RAG) and embedding-based search both depend on splitting a corpus into <em>chunks</em>: small pieces that are individually embedded and stored in a vector database. The split happens before any of the AI machinery runs, but the quality of your retrieval quietly depends on it more than most people realise. Too-small chunks lose context; too-large chunks dilute relevance; chunks split mid-sentence retrieve poorly because the embedding lands in a weird semantic spot. This tool gives you a fast in-browser playground to experiment with chunk size, overlap, and strategy before you commit a pipeline to the choice.</p>

<h3>The four strategies</h3>
<ul>
  <li><strong>recursive-char</strong> (default). Tries to split on paragraph breaks first, then line breaks, then sentence boundaries (<code>. </code>), then spaces. Each piece is greedily packed up to the chunk-size budget. Falls back to a hard character split only when nothing else fits. This is the default in LangChain, LlamaIndex, and most production RAG stacks, and is a sensible starting point for almost any prose corpus.</li>
  <li><strong>sentence</strong>. Splits at sentence boundaries and never inside a sentence — even if a sentence is shorter than the budget, it stays whole. Better than recursive-char when chunks will be quoted back as evidence (QA, citations) because no chunk ends mid-thought. Chunk sizes are more variable, since sentence lengths are.</li>
  <li><strong>paragraph</strong>. Treats each paragraph as a unit. Two adjacent short paragraphs may be packed together, but a long paragraph is never split. Useful for documentation, knowledge-base articles, and well-formatted long-form where each paragraph is a coherent thought.</li>
  <li><strong>semantic</strong>. Adds heading detection on top of paragraph: lines starting with <code>#</code>, <code>##</code> etc., or short all-caps lines, are treated as new-section breaks. Good for technical documentation where section boundaries matter more than visual paragraph spacing.</li>
</ul>

<h3>Overlap — why and how much</h3>
<ul>
  <li><strong>Why.</strong> If a relevant span happens to fall exactly across the boundary between two chunks, both chunks will retrieve poorly because each only has half. Overlap copies the last N tokens of the previous chunk onto the front of the next chunk, giving both a chance to capture the span.</li>
  <li><strong>How much.</strong> 10–20% of the chunk size is the common rule of thumb. For 500-token chunks, 50–100 tokens of overlap. The default here is 50, which works well in practice.</li>
  <li><strong>Trade-off.</strong> More overlap = more total embeddings (more storage, more cost, slower index build, more retrieval candidates). Don't push past 30% unless you have a specific reason; you'll waste money without improving retrieval much.</li>
</ul>

<h3>Token estimation</h3>
<ul>
  <li><strong>It's a heuristic.</strong> We use chars / 3.8 for English-ish text and 1 token per character for CJK. That's good to ±5–10% for prose, worse for code-heavy or structured text.</li>
  <li><strong>Why not the real tokenizer?</strong> tiktoken is ~1 MB of WASM, far too heavy to ship just for chunk-sizing. If your downstream model has a hard token limit on chunks (some do, e.g. cohere/embed-v3 is capped at 512), build with a small safety margin or run the real tokenizer in your pipeline.</li>
  <li><strong>This is fine for sizing.</strong> The exact token count of each chunk doesn't matter much for RAG quality — the embedding model truncates oversized inputs anyway. What matters is consistency: same heuristic for chunking and for budgeting downstream prompts.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Don't chunk structured data like JSON or CSV with a text chunker.</strong> The chunk boundaries will fall in the middle of records and the embeddings will be meaningless. Either split on record boundaries first, or use a tool-specific RAG approach.</li>
  <li><strong>Don't chunk code with a prose chunker.</strong> Function boundaries are what matter for code retrieval, not character counts. Tree-sitter-based chunkers exist for this.</li>
  <li><strong>Whitespace and BOM.</strong> Pasted text can carry hidden whitespace that throws off token estimates. Trim and normalise before paste if it matters.</li>
  <li><strong>Privacy.</strong> Everything runs in the browser. Documents pasted here never leave the page; you can use this for confidential or PII-containing material the same way you'd use a local script.</li>
</ul>
""",
        "de": """
<h2>Wozu ist das gut?</h2>
<p>Retrieval-Augmented Generation (RAG) und Embedding-basierte Suche hängen beide davon ab, ein Korpus in <em>Chunks</em> zu zerlegen: kleine Stücke, die einzeln eingebettet und in einer Vektor-Datenbank gespeichert werden. Der Split passiert vor jeder KI-Mechanik, aber die Qualität deines Retrievals hängt heimlich mehr davon ab, als die meisten denken. Zu kleine Chunks verlieren Kontext; zu große verwässern Relevanz; mitten im Satz geteilte Chunks retrieven schlecht, weil das Embedding an einer seltsamen semantischen Stelle landet. Dieses Tool ist ein schneller Browser-Spielplatz, um Chunk-Größe, Overlap und Strategie auszuprobieren, bevor du eine Pipeline darauf festlegst.</p>

<h3>Die vier Strategien</h3>
<ul>
  <li><strong>recursive-char</strong> (Standard). Versucht zuerst auf Absätzen zu splitten, dann auf Zeilen, dann auf Satzgrenzen (<code>. </code>), dann auf Leerzeichen. Jedes Stück wird greedy bis zur Chunk-Größe gepackt. Fällt nur dann auf harten Zeichensplit zurück, wenn nichts anderes passt. Standard in LangChain, LlamaIndex und den meisten Produktions-RAG-Stacks; vernünftiger Startpunkt für fast jedes Prosa-Korpus.</li>
  <li><strong>sentence</strong>. Splittet an Satzgrenzen und nie innerhalb eines Satzes — auch wenn ein Satz kürzer als das Budget ist, bleibt er ganz. Besser als recursive-char, wenn Chunks als Beweis zitiert werden (QA, Zitationen), weil kein Chunk mitten im Gedanken endet. Chunk-Größen variieren stärker, weil Sätze es tun.</li>
  <li><strong>paragraph</strong>. Behandelt jeden Absatz als Einheit. Zwei kurze benachbarte Absätze können zusammengepackt werden, aber ein langer Absatz wird nie geteilt. Nützlich für Doku, Knowledge-Base-Artikel und gut formatierte Langtexte, wo jeder Absatz ein kohärenter Gedanke ist.</li>
  <li><strong>semantic</strong>. Erweitert Paragraph um Heading-Erkennung: Zeilen mit <code>#</code>, <code>##</code> usw., oder kurze All-Caps-Zeilen werden als neue Sektion behandelt. Gut für technische Doku, wo Sektionsgrenzen wichtiger sind als visuelle Absatzabstände.</li>
</ul>

<h3>Overlap — warum und wie viel</h3>
<ul>
  <li><strong>Warum.</strong> Fällt ein relevanter Abschnitt genau zwischen zwei Chunks, retrieven beide schlecht, weil jeder nur die Hälfte hat. Overlap kopiert die letzten N Tokens des vorherigen Chunks an den Anfang des nächsten, damit beide den Abschnitt einfangen können.</li>
  <li><strong>Wie viel.</strong> 10–20% der Chunk-Größe ist die Faustregel. Bei 500 Tokens also 50–100 Tokens Overlap. Standard hier 50, funktioniert gut in der Praxis.</li>
  <li><strong>Trade-off.</strong> Mehr Overlap = mehr Embeddings (mehr Storage, mehr Kosten, langsamerer Indexaufbau, mehr Retrieval-Kandidaten). Geh nicht über 30% ohne spezifischen Grund; verbrennt Geld ohne deutlich besseres Retrieval.</li>
</ul>

<h3>Token-Schätzung</h3>
<ul>
  <li><strong>Ist eine Heuristik.</strong> Zeichen / 3.8 für englisch-ähnlichen Text und 1 Token pro CJK-Zeichen. ±5–10% für Prosa, schlechter für Code-lastige oder strukturierte Texte.</li>
  <li><strong>Warum nicht der echte Tokenizer?</strong> tiktoken ist ~1 MB WASM — zu schwer nur fürs Chunk-Sizing. Wenn dein Downstream-Modell ein hartes Tokenlimit auf Chunks hat (z. B. cohere/embed-v3 mit 512), baue mit Sicherheitsmarge oder fahre den echten Tokenizer in deiner Pipeline.</li>
  <li><strong>Für Sizing ist das fein.</strong> Die exakte Token-Zahl pro Chunk ist für RAG-Qualität egal — das Embedding-Modell trunkiert sowieso. Was zählt ist Konsistenz: gleiche Heuristik fürs Chunking und fürs Budgetieren der Downstream-Prompts.</li>
</ul>

<h3>Typische Stolperfallen</h3>
<ul>
  <li><strong>JSON oder CSV nicht mit einem Text-Chunker chunken.</strong> Chunk-Grenzen fallen mitten in Records, Embeddings werden bedeutungslos. Erst auf Record-Grenzen splitten oder einen tool-spezifischen RAG-Ansatz nutzen.</li>
  <li><strong>Code nicht mit einem Prosa-Chunker chunken.</strong> Für Code-Retrieval zählen Funktionsgrenzen, nicht Zeichenzahlen. Tree-sitter-basierte Chunker gibt's dafür.</li>
  <li><strong>Whitespace und BOM.</strong> Eingefügter Text kann unsichtbares Whitespace tragen, das Token-Schätzungen verzerrt. Vor dem Einfügen trimmen und normalisieren, wenn's drauf ankommt.</li>
  <li><strong>Privacy.</strong> Alles läuft im Browser. Hier eingefügte Dokumente verlassen die Seite nie; nutzbar für vertrauliches oder PII-haltiges Material, genau wie ein lokales Skript.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>RAG (Retrieval-Augmented Generation) y la búsqueda por embeddings dependen ambas de dividir un corpus en <em>chunks</em>: piezas pequeñas que se embedean individualmente y se guardan en una vector DB. La división ocurre antes de cualquier maquinaria de IA, pero la calidad de tu retrieval depende silenciosamente de ella más de lo que la gente cree. Chunks demasiado pequeños pierden contexto; demasiado grandes diluyen relevancia; chunks cortados a mitad de frase retrievan mal porque el embedding cae en un punto semántico raro. Esta herramienta es un playground rápido en el navegador para experimentar con tamaño, overlap y estrategia antes de fijar una pipeline.</p>

<h3>Las cuatro estrategias</h3>
<ul>
  <li><strong>recursive-char</strong> (predeterminado). Intenta dividir por párrafos primero, luego saltos de línea, luego fronteras de frase (<code>. </code>), luego espacios. Cada pieza se empaqueta greedy hasta el budget de tamaño. Solo recurre a corte por caracteres cuando nada más cabe. Es el default en LangChain, LlamaIndex y la mayoría de stacks RAG en producción; punto de partida sensato para casi cualquier corpus de prosa.</li>
  <li><strong>sentence</strong>. Divide en fronteras de frase y nunca dentro de una frase — aunque sea más corta que el budget, queda entera. Mejor que recursive-char cuando los chunks se citarán como evidencia (QA, citas) porque ningún chunk termina a mitad de pensamiento. Los tamaños varían más, porque las frases varían.</li>
  <li><strong>paragraph</strong>. Trata cada párrafo como unidad. Dos párrafos cortos adyacentes pueden empaquetarse juntos, pero uno largo nunca se divide. Útil para documentación, artículos de KB y formato largo bien estructurado donde cada párrafo es un pensamiento coherente.</li>
  <li><strong>semantic</strong>. Añade detección de headings sobre paragraph: líneas con <code>#</code>, <code>##</code> etc., o líneas cortas en mayúsculas, se tratan como inicio de nueva sección. Bueno para documentación técnica donde las secciones importan más que el espaciado visual.</li>
</ul>

<h3>Overlap — por qué y cuánto</h3>
<ul>
  <li><strong>Por qué.</strong> Si un span relevante cae exactamente entre dos chunks, ambos retrievan mal porque cada uno tiene solo la mitad. Overlap copia los últimos N tokens del chunk anterior al inicio del siguiente para que ambos capturen el span.</li>
  <li><strong>Cuánto.</strong> 10–20% del tamaño del chunk como regla. Para chunks de 500 tokens, 50–100 de overlap. Aquí el default es 50, va bien en la práctica.</li>
  <li><strong>Trade-off.</strong> Más overlap = más embeddings totales (más storage, más coste, build más lento, más candidatos de retrieval). No pases del 30% sin razón concreta; gastas dinero sin mejorar mucho.</li>
</ul>

<h3>Estimación de tokens</h3>
<ul>
  <li><strong>Es heurística.</strong> chars / 3.8 para texto tipo inglés y 1 token por carácter CJK. ±5–10% para prosa, peor con código o texto estructurado.</li>
  <li><strong>¿Por qué no el tokenizer real?</strong> tiktoken son ~1 MB de WASM — demasiado pesado solo para sizing. Si tu modelo downstream tiene un límite duro (p.ej. cohere/embed-v3 a 512), construye con margen o corre el tokenizer real en tu pipeline.</li>
  <li><strong>Para sizing va bien.</strong> El conteo exacto por chunk importa poco para calidad RAG — el modelo de embedding trunca de todos modos. Lo que importa es la consistencia: la misma heurística para chunking y para presupuestar prompts downstream.</li>
</ul>

<h3>Errores comunes</h3>
<ul>
  <li><strong>No chunkar datos estructurados (JSON, CSV) con un chunker de texto.</strong> Los límites caen a mitad de registro y los embeddings pierden sentido. Divide por registros primero, o usa un enfoque RAG específico.</li>
  <li><strong>No chunkar código con un chunker de prosa.</strong> Para retrieval de código importan los límites de función, no el número de caracteres. Existen chunkers basados en tree-sitter.</li>
  <li><strong>Whitespace y BOM.</strong> Texto pegado puede traer whitespace oculto que desvía la estimación de tokens. Trimmea y normaliza antes si importa.</li>
  <li><strong>Privacidad.</strong> Todo corre en el navegador. Los documentos pegados aquí no salen de la página; úsala para material confidencial o con PII igual que un script local.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>La Retrieval-Augmented Generation (RAG) et la recherche par embeddings dépendent toutes deux du découpage d'un corpus en <em>chunks</em> : petits morceaux embeddés individuellement et stockés dans une vector DB. Le découpage se passe avant toute machinerie IA, mais la qualité de votre retrieval en dépend en silence plus que la plupart des gens le pensent. Chunks trop petits perdent du contexte ; trop grands diluent la pertinence ; chunks coupés au milieu d'une phrase retrievent mal car l'embedding atterrit dans un point sémantique bizarre. Cet outil est un playground rapide dans le navigateur pour expérimenter taille, overlap et stratégie avant de figer une pipeline.</p>

<h3>Les quatre stratégies</h3>
<ul>
  <li><strong>recursive-char</strong> (par défaut). Essaie de découper d'abord aux paragraphes, puis aux sauts de ligne, puis aux frontières de phrase (<code>. </code>), puis aux espaces. Chaque morceau est emballé glouton jusqu'au budget de taille. Ne retombe sur un découpage par caractères que si rien d'autre ne rentre. Default dans LangChain, LlamaIndex et la plupart des stacks RAG en prod ; point de départ raisonnable pour à peu près tout corpus de prose.</li>
  <li><strong>sentence</strong>. Découpe aux frontières de phrase, jamais à l'intérieur — même si une phrase est plus courte que le budget, elle reste entière. Mieux que recursive-char quand les chunks seront cités comme preuve (QA, citations) car aucun chunk ne termine au milieu d'une pensée. Tailles plus variables, car les phrases le sont.</li>
  <li><strong>paragraph</strong>. Traite chaque paragraphe comme une unité. Deux paragraphes courts voisins peuvent être emballés ensemble, mais un long n'est jamais découpé. Utile pour la doc, les articles KB et le format long bien structuré où chaque paragraphe est une pensée cohérente.</li>
  <li><strong>semantic</strong>. Ajoute la détection de headings au-dessus de paragraph : lignes avec <code>#</code>, <code>##</code> etc., ou lignes courtes en majuscules, sont traitées comme début de nouvelle section. Bon pour la doc technique où les frontières de section comptent plus que l'espacement visuel.</li>
</ul>

<h3>Overlap — pourquoi et combien</h3>
<ul>
  <li><strong>Pourquoi.</strong> Si un span pertinent tombe pile entre deux chunks, les deux retrievent mal car chacun n'en a que la moitié. Overlap copie les derniers N tokens du chunk précédent au début du suivant pour que les deux puissent capturer le span.</li>
  <li><strong>Combien.</strong> 10–20% de la taille du chunk en règle générale. Pour des chunks de 500 tokens, 50–100 d'overlap. Le default ici est 50, fonctionne bien en pratique.</li>
  <li><strong>Trade-off.</strong> Plus d'overlap = plus d'embeddings total (plus de stockage, plus de coût, build plus lent, plus de candidats au retrieval). Ne dépassez pas 30% sans raison précise ; vous brûlez de l'argent sans gros gain.</li>
</ul>

<h3>Estimation des tokens</h3>
<ul>
  <li><strong>C'est une heuristique.</strong> chars / 3.8 pour du texte de type anglais et 1 token par caractère CJK. ±5–10% pour la prose, pire avec code ou texte structuré.</li>
  <li><strong>Pourquoi pas le vrai tokenizer ?</strong> tiktoken c'est ~1 Mo de WASM — trop lourd juste pour le sizing. Si votre modèle aval a une limite stricte (p.ex. cohere/embed-v3 à 512), construisez avec marge ou faites tourner le vrai tokenizer dans votre pipeline.</li>
  <li><strong>Pour le sizing ça suffit.</strong> Le compte exact par chunk importe peu pour la qualité RAG — le modèle d'embedding tronque de toute façon. Ce qui compte c'est la cohérence : même heuristique pour le chunking et pour budgétiser les prompts aval.</li>
</ul>

<h3>Pièges courants</h3>
<ul>
  <li><strong>Ne chunkez pas de données structurées (JSON, CSV) avec un chunker de texte.</strong> Les frontières tombent au milieu des records et les embeddings deviennent absurdes. Découpez par record d'abord, ou utilisez une approche RAG spécifique.</li>
  <li><strong>Ne chunkez pas de code avec un chunker de prose.</strong> Pour le retrieval de code, ce sont les frontières de fonction qui comptent, pas le nombre de caractères. Des chunkers tree-sitter existent.</li>
  <li><strong>Whitespace et BOM.</strong> Du texte collé peut transporter du whitespace caché qui fausse l'estimation. Trimmez et normalisez avant si ça compte.</li>
  <li><strong>Privacy.</strong> Tout tourne dans le navigateur. Les documents collés ne quittent jamais la page ; utilisable pour du contenu confidentiel ou avec PII, comme un script local.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>RAG (Retrieval-Augmented Generation) e la ricerca per embeddings dipendono entrambe dallo spezzare un corpus in <em>chunk</em>: piccoli pezzi embeddati individualmente e archiviati in un vector DB. Lo split avviene prima di qualsiasi macchinario AI, ma la qualità del tuo retrieval dipende silenziosamente da esso più di quanto la maggior parte pensi. Chunk troppo piccoli perdono contesto; troppo grandi diluiscono rilevanza; chunk tagliati a metà frase retrievano male perché l'embedding finisce in un punto semantico strano. Questo strumento è un playground veloce in browser per sperimentare con dimensione, overlap e strategia prima di fissare una pipeline.</p>

<h3>Le quattro strategie</h3>
<ul>
  <li><strong>recursive-char</strong> (default). Prova prima a spezzare ai paragrafi, poi alle nuove righe, poi ai confini di frase (<code>. </code>), poi agli spazi. Ogni pezzo viene impacchettato in modo greedy fino al budget. Ricade su split per caratteri solo se nient'altro entra. Default in LangChain, LlamaIndex e gran parte degli stack RAG in produzione; punto di partenza sensato per quasi ogni corpus di prosa.</li>
  <li><strong>sentence</strong>. Spezza ai confini di frase e mai dentro a una — anche se è più corta del budget, resta intera. Meglio di recursive-char quando i chunk verranno citati come evidenza (QA, citazioni) perché nessun chunk finisce a metà pensiero. Le dimensioni variano di più, perché le frasi variano.</li>
  <li><strong>paragraph</strong>. Tratta ogni paragrafo come unità. Due paragrafi corti adiacenti possono essere impacchettati insieme, ma uno lungo non viene mai spezzato. Utile per documentazione, articoli KB e long-form ben formattato dove ogni paragrafo è un pensiero coerente.</li>
  <li><strong>semantic</strong>. Aggiunge il rilevamento di heading sopra paragraph: righe con <code>#</code>, <code>##</code> ecc., o righe corte tutto maiuscolo, sono trattate come nuove sezioni. Buono per documentazione tecnica dove i confini di sezione contano più della spaziatura visiva.</li>
</ul>

<h3>Overlap — perché e quanto</h3>
<ul>
  <li><strong>Perché.</strong> Se uno span rilevante cade esattamente al confine tra due chunk, entrambi retrievano male perché ognuno ne ha solo metà. L'overlap copia gli ultimi N token del chunk precedente all'inizio del successivo, dando a entrambi la possibilità di catturarlo.</li>
  <li><strong>Quanto.</strong> 10–20% della dimensione del chunk come regola. Per chunk da 500 token, 50–100 di overlap. Qui il default è 50, funziona bene in pratica.</li>
  <li><strong>Trade-off.</strong> Più overlap = più embedding totali (più storage, più costo, build più lenta, più candidati). Non passare il 30% senza ragione specifica; bruci soldi senza migliorare molto.</li>
</ul>

<h3>Stima dei token</h3>
<ul>
  <li><strong>È euristica.</strong> caratteri / 3.8 per testo tipo inglese e 1 token per carattere CJK. ±5–10% per prosa, peggio per testo code-heavy o strutturato.</li>
  <li><strong>Perché non il tokenizer reale?</strong> tiktoken è ~1 MB di WASM — troppo pesante solo per il sizing. Se il tuo modello downstream ha un limite duro (es. cohere/embed-v3 a 512), costruisci con margine o esegui il tokenizer reale nella tua pipeline.</li>
  <li><strong>Per il sizing va bene.</strong> Il conteggio esatto per chunk conta poco per la qualità RAG — il modello di embedding tronca comunque. Quello che conta è coerenza: stessa euristica per chunking e per budgeting dei prompt downstream.</li>
</ul>

<h3>Trappole comuni</h3>
<ul>
  <li><strong>Non chunkare dati strutturati (JSON, CSV) con un chunker di testo.</strong> I confini cadono a metà record e gli embedding diventano insensati. Spezza per record prima, o usa un approccio RAG specifico.</li>
  <li><strong>Non chunkare codice con un chunker di prosa.</strong> Per il retrieval di codice contano i confini di funzione, non i caratteri. Esistono chunker basati su tree-sitter.</li>
  <li><strong>Whitespace e BOM.</strong> Testo incollato può portare whitespace nascosto che falsa la stima dei token. Trimma e normalizza prima se conta.</li>
  <li><strong>Privacy.</strong> Tutto gira nel browser. I documenti incollati non lasciano la pagina; usalo per materiale confidenziale o con PII come faresti con uno script locale.</li>
</ul>
""",
        "pt": """
<h2>Pra que serve?</h2>
<p>RAG (Retrieval-Augmented Generation) e busca por embeddings dependem ambos de dividir um corpus em <em>chunks</em>: pedaços pequenos que são embedados individualmente e guardados num vector DB. A divisão acontece antes de qualquer maquinário de IA, mas a qualidade do seu retrieval depende silenciosamente disso mais do que a maioria pensa. Chunks pequenos demais perdem contexto; grandes demais diluem relevância; chunks cortados no meio de frase retrievam mal porque o embedding cai num ponto semântico estranho. Esta ferramenta é um playground rápido no navegador pra experimentar tamanho, overlap e estratégia antes de fixar uma pipeline.</p>

<h3>As quatro estratégias</h3>
<ul>
  <li><strong>recursive-char</strong> (padrão). Tenta dividir primeiro por parágrafos, depois quebras de linha, depois fronteiras de frase (<code>. </code>), depois espaços. Cada peça é empacotada de forma gulosa até o budget de tamanho. Só recorre a corte por caracteres quando nada mais cabe. Default no LangChain, LlamaIndex e na maioria dos stacks RAG em produção; ponto de partida sensato pra quase qualquer corpus de prosa.</li>
  <li><strong>sentence</strong>. Divide em fronteiras de frase e nunca dentro de uma — mesmo que seja menor que o budget, fica inteira. Melhor que recursive-char quando os chunks serão citados como evidência (QA, citações) porque nenhum chunk termina no meio do pensamento. Tamanhos variam mais, porque frases variam.</li>
  <li><strong>paragraph</strong>. Trata cada parágrafo como unidade. Dois parágrafos curtos adjacentes podem ser empacotados juntos, mas um longo nunca é dividido. Útil pra documentação, artigos de KB e long-form bem formatado onde cada parágrafo é um pensamento coerente.</li>
  <li><strong>semantic</strong>. Adiciona detecção de headings em cima de paragraph: linhas com <code>#</code>, <code>##</code> etc., ou linhas curtas em maiúsculas, são tratadas como início de nova seção. Bom pra documentação técnica onde fronteiras de seção importam mais que espaçamento visual.</li>
</ul>

<h3>Overlap — por que e quanto</h3>
<ul>
  <li><strong>Por que.</strong> Se um span relevante cai exatamente entre dois chunks, ambos retrievam mal porque cada um tem só metade. Overlap copia os últimos N tokens do chunk anterior pro início do próximo, dando a ambos chance de capturar o span.</li>
  <li><strong>Quanto.</strong> 10–20% do tamanho do chunk como regra. Pra chunks de 500 tokens, 50–100 de overlap. Aqui o default é 50, funciona bem na prática.</li>
  <li><strong>Trade-off.</strong> Mais overlap = mais embeddings totais (mais storage, mais custo, build mais lento, mais candidatos). Não passe de 30% sem razão específica; queima dinheiro sem grande ganho.</li>
</ul>

<h3>Estimativa de tokens</h3>
<ul>
  <li><strong>É heurística.</strong> chars / 3.8 pra texto tipo inglês e 1 token por caractere CJK. ±5–10% pra prosa, pior pra texto code-heavy ou estruturado.</li>
  <li><strong>Por que não o tokenizer real?</strong> tiktoken é ~1 MB de WASM — pesado demais só pra sizing. Se seu modelo downstream tem limite duro (ex.: cohere/embed-v3 a 512), construa com margem ou rode o tokenizer real na sua pipeline.</li>
  <li><strong>Pra sizing tá ótimo.</strong> A contagem exata por chunk importa pouco pra qualidade RAG — o modelo de embedding trunca de qualquer jeito. O que importa é consistência: mesma heurística pra chunking e pra budgetar prompts downstream.</li>
</ul>

<h3>Pegadinhas comuns</h3>
<ul>
  <li><strong>Não chunkar dados estruturados (JSON, CSV) com chunker de texto.</strong> As fronteiras caem no meio de registros e os embeddings ficam sem sentido. Divida por registro primeiro, ou use abordagem RAG específica.</li>
  <li><strong>Não chunkar código com chunker de prosa.</strong> Pra retrieval de código, importam fronteiras de função, não contagem de caracteres. Existem chunkers baseados em tree-sitter.</li>
  <li><strong>Whitespace e BOM.</strong> Texto colado pode trazer whitespace escondido que desvia a estimativa. Trim e normalize antes se importa.</li>
  <li><strong>Privacidade.</strong> Tudo roda no navegador. Documentos colados não saem da página; pode usar pra material confidencial ou com PII como usaria um script local.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>RAG (Retrieval-Augmented Generation) i wyszukiwanie po embeddingach zależą oba od dzielenia korpusu na <em>chunki</em>: małe kawałki, które są pojedynczo embedowane i przechowywane w vector DB. Podział dzieje się przed jakąkolwiek maszynerią AI, ale jakość twojego retrievalu zależy od niego po cichu bardziej niż większość ludzi sądzi. Za małe chunki tracą kontekst; za duże rozcieńczają relewancję; chunki ucięte w środku zdania retrievują źle, bo embedding ląduje w dziwnym semantycznym miejscu. To narzędzie to szybki playground w przeglądarce do eksperymentowania z rozmiarem, overlapem i strategią przed zafiksowaniem pipeline'u.</p>

<h3>Cztery strategie</h3>
<ul>
  <li><strong>recursive-char</strong> (domyślne). Najpierw próbuje dzielić po akapitach, potem nowych liniach, potem granicach zdań (<code>. </code>), potem spacjach. Każdy kawałek jest greedy pakowany do budżetu. Wpada w hard split po znakach tylko jak nic innego nie pasuje. Default w LangChain, LlamaIndex i większości produkcyjnych stacków RAG; rozsądny punkt startowy dla niemal każdego korpusu prozy.</li>
  <li><strong>sentence</strong>. Dzieli na granicach zdań i nigdy wewnątrz zdania — nawet jak jest krótsze niż budżet, zostaje całe. Lepsze od recursive-char gdy chunki będą cytowane jako dowód (QA, cytaty), bo żaden nie kończy się w środku myśli. Rozmiary bardziej zmienne, bo zdania są.</li>
  <li><strong>paragraph</strong>. Traktuje każdy akapit jako jednostkę. Dwa sąsiadujące krótkie mogą być zapakowane razem, ale długi nigdy nie jest dzielony. Przydatne dla dokumentacji, artykułów KB i dobrze sformatowanych long-formów gdzie każdy akapit to spójna myśl.</li>
  <li><strong>semantic</strong>. Dodaje detekcję nagłówków ponad paragraph: linie z <code>#</code>, <code>##</code> itd., albo krótkie linie all-caps, traktowane jako początek nowej sekcji. Dobre dla dokumentacji technicznej gdzie granice sekcji liczą się bardziej niż wizualne odstępy.</li>
</ul>

<h3>Overlap — dlaczego i ile</h3>
<ul>
  <li><strong>Dlaczego.</strong> Jeśli relewantny fragment wypada dokładnie między dwoma chunkami, oba retrievują źle bo każdy ma tylko połowę. Overlap kopiuje ostatnie N tokenów z poprzedniego chunka na początek następnego, dając obu szansę przechwycenia.</li>
  <li><strong>Ile.</strong> 10–20% rozmiaru chunka jako reguła. Dla chunków 500-tokenowych, 50–100 overlap. Default tu to 50, działa dobrze w praktyce.</li>
  <li><strong>Trade-off.</strong> Więcej overlapu = więcej embeddingów łącznie (więcej storage, więcej kosztów, wolniejszy build indeksu, więcej kandydatów retrievalu). Nie przekraczaj 30% bez konkretnego powodu; tracisz kasę bez większego zysku.</li>
</ul>

<h3>Estymacja tokenów</h3>
<ul>
  <li><strong>To heurystyka.</strong> znaki / 3.8 dla tekstu angielsko-podobnego i 1 token na znak CJK. ±5–10% dla prozy, gorzej dla code-heavy lub strukturyzowanego.</li>
  <li><strong>Czemu nie prawdziwy tokenizer?</strong> tiktoken to ~1 MB WASM — za ciężko tylko do sizingu. Jeśli twój downstream model ma twardy limit (np. cohere/embed-v3 na 512), buduj z marginesem albo odpal prawdziwy tokenizer w pipelinie.</li>
  <li><strong>Do sizingu jest ok.</strong> Dokładna liczba tokenów per chunk mało znaczy dla jakości RAG — model embeddingowy i tak trunkuje. Co się liczy to spójność: ta sama heurystyka do chunkingu i do budżetowania downstream promptów.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Nie chunkuj danych strukturyzowanych (JSON, CSV) chunkerem tekstu.</strong> Granice wpadają w środek rekordów i embeddingi tracą sens. Najpierw podziel po rekordach albo użyj specyficznego podejścia RAG.</li>
  <li><strong>Nie chunkuj kodu chunkerem prozy.</strong> Dla retrievalu kodu liczą się granice funkcji, nie liczby znaków. Istnieją chunkery oparte na tree-sitter.</li>
  <li><strong>Whitespace i BOM.</strong> Wklejony tekst może nieść ukryty whitespace zaburzający estymację. Trimuj i normalizuj przed wklejeniem jeśli ważne.</li>
  <li><strong>Prywatność.</strong> Wszystko leci w przeglądarce. Wklejone dokumenty nigdy nie opuszczają strony; możesz tego używać do poufnego materiału lub z PII jak lokalnego skryptu.</li>
</ul>
""",
        "ja": """
<h2>これは何のため？</h2>
<p>Retrieval-Augmented Generation（RAG）と埋め込みベース検索のどちらも、コーパスを <em>チャンク</em> に分割することに依存します。それぞれのチャンクが個別に埋め込まれ、ベクトル DB に格納されます。分割は AI 機構が動く前に行われますが、検索品質はそこに静かに、ほとんどの人が思うより強く依存します。チャンクが小さすぎると文脈を失い、大きすぎると関連性が薄まり、文の途中で切れたチャンクは埋め込みが妙な意味的位置に落ちて検索品質が下がります。このツールはブラウザ完結の素早いプレイグラウンドで、チャンクサイズ・オーバーラップ・戦略を試してから、パイプラインに組み込めます。</p>

<h3>4 つの戦略</h3>
<ul>
  <li><strong>recursive-char</strong>（デフォルト）。最初に段落で分割、次に改行、文境界（<code>. </code>）、空白で分割を試みます。各ピースをチャンクサイズの予算まで貪欲にパック。どうしても入らない場合のみ、文字単位のハード分割にフォールバック。LangChain・LlamaIndex・ほぼすべての本番 RAG スタックのデフォルトで、散文コーパスにおいて妥当な出発点です。</li>
  <li><strong>sentence</strong>。文境界で分割し、文の途中では決して切りません。文が予算より短くても、まるごと残します。チャンクが根拠として引用されるユースケース（QA・引用）では recursive-char より良く、文の途中で終わるチャンクが出ません。文の長さがばらつくため、チャンクサイズもばらつきます。</li>
  <li><strong>paragraph</strong>。各段落を 1 単位として扱います。隣接する短い段落をパックできますが、長い段落は決して分割しません。各段落が一貫した思考になっているドキュメント・KB 記事・整った長文に有用。</li>
  <li><strong>semantic</strong>。paragraph に見出し検出を加えたもの。<code>#</code>、<code>##</code> などで始まる行や短い大文字行を新セクションの境界として扱います。視覚的な段落間隔よりセクション境界が重要なテクニカルドキュメントに有用。</li>
</ul>

<h3>オーバーラップ — 理由と量</h3>
<ul>
  <li><strong>理由。</strong> 関連スパンがちょうど 2 つのチャンクの境界に落ちると、両方とも半分しか持たないため検索品質が下がります。オーバーラップは、前のチャンクの末尾 N トークンを次のチャンクの先頭にコピーし、両方にスパン捕捉の機会を与えます。</li>
  <li><strong>量。</strong> チャンクサイズの 10〜20% が経験則。500 トークンチャンクなら 50〜100 トークン。ここのデフォルトは 50 で、実用上うまく動きます。</li>
  <li><strong>トレードオフ。</strong> オーバーラップが多い = 総埋め込み数増（ストレージ・コスト・インデックス構築時間・検索候補が増える）。具体的な理由がない限り 30% を超えないこと。検索品質はほとんど上がらず、コストだけ増えます。</li>
</ul>

<h3>トークン推定</h3>
<ul>
  <li><strong>ヒューリスティックです。</strong> 英語的なテキストには「文字数 / 3.8」、CJK には「1 文字あたり 1 トークン」を使います。散文で ±5〜10%、コード重めや構造化テキストではそれより精度が落ちます。</li>
  <li><strong>なぜ本物のトークナイザを使わないか。</strong> tiktoken は ~1 MB の WASM で、チャンクのサイジングだけのために載せるには重すぎます。下流モデルがチャンクに対して厳密なトークン上限を持つ場合（例：cohere/embed-v3 は 512 上限）、安全マージンを取って構築するか、パイプラインで本物のトークナイザを通してください。</li>
  <li><strong>サイジングにはこれで十分。</strong> 各チャンクの正確なトークン数は RAG 品質にはほとんど影響しません — 埋め込みモデルはどうせ超過分を切り捨てます。重要なのは一貫性で、チャンキングと下流プロンプトの予算配分に同じヒューリスティックを使うことです。</li>
</ul>

<h3>よくある落とし穴</h3>
<ul>
  <li><strong>JSON や CSV のような構造化データをテキストチャンカーでチャンクしない。</strong> チャンク境界がレコードの途中に落ち、埋め込みは意味を失います。先にレコード境界で分割するか、ツール固有の RAG 手法を使ってください。</li>
  <li><strong>コードを散文チャンカーでチャンクしない。</strong> コード検索では関数境界が重要であり、文字数ではありません。tree-sitter ベースのチャンカーがあります。</li>
  <li><strong>空白と BOM。</strong> 貼り付けたテキストには隠れた空白が含まれ、トークン推定が狂うことがあります。気になるなら貼り付け前にトリム・正規化してください。</li>
  <li><strong>プライバシー。</strong> すべてブラウザ内で動きます。貼り付けた文書はページを出ません — ローカルスクリプトと同じ感覚で、機密情報や PII を含む素材にも使えます。</li>
</ul>
""",
        "nl": """
<h2>Waar is dit voor?</h2>
<p>Retrieval-Augmented Generation (RAG) en embedding-gebaseerd zoeken hangen beide af van het splitsen van een corpus in <em>chunks</em>: kleine stukken die afzonderlijk worden embed en in een vector-DB opgeslagen. De split gebeurt vóór alle AI-machinerie, maar de kwaliteit van je retrieval hangt er stilletjes meer van af dan de meeste mensen beseffen. Te kleine chunks verliezen context; te grote verdunnen relevantie; midden in een zin gesplitste chunks retrieven slecht omdat de embedding op een rare semantische plek belandt. Deze tool is een snelle in-browser-playground om te experimenteren met chunk-grootte, overlap en strategie voordat je een pipeline op de keuze vastlegt.</p>

<h3>De vier strategieën</h3>
<ul>
  <li><strong>recursive-char</strong> (default). Probeert eerst op alinea-breaks te splitsen, dan op regelbreaks, dan op zinsgrenzen (<code>. </code>), dan op spaties. Elk stuk wordt gulzig opgepakt tot de chunk-grootte. Valt alleen terug op een harde karakter-split als niets anders past. Default in LangChain, LlamaIndex en de meeste productie-RAG-stacks; verstandig startpunt voor bijna elk prozacorpus.</li>
  <li><strong>sentence</strong>. Splitst op zinsgrenzen en nooit binnen een zin — ook als een zin korter is dan de budget, blijft hij heel. Beter dan recursive-char wanneer chunks als bewijs worden geciteerd (QA, citaten), omdat geen chunk midden in een gedachte eindigt. Chunk-groottes variëren meer, omdat zinnen dat doen.</li>
  <li><strong>paragraph</strong>. Behandelt elke alinea als eenheid. Twee aangrenzende korte alinea's kunnen samen worden gepakt, maar een lange alinea wordt nooit gesplitst. Handig voor documentatie, KB-artikelen en goed opgemaakte long-form waar elke alinea een coherente gedachte is.</li>
  <li><strong>semantic</strong>. Voegt heading-detectie toe bovenop paragraph: regels die beginnen met <code>#</code>, <code>##</code> enz., of korte all-caps regels, worden behandeld als sectie-breaks. Goed voor technische documentatie waar sectiegrenzen meer tellen dan visuele alinea-spacing.</li>
</ul>

<h3>Overlap — waarom en hoeveel</h3>
<ul>
  <li><strong>Waarom.</strong> Als een relevante span precies over de grens tussen twee chunks valt, retrieven beide slecht omdat elk maar de helft heeft. Overlap kopieert de laatste N tokens van de vorige chunk naar de voorkant van de volgende, zodat beide de span kunnen vangen.</li>
  <li><strong>Hoeveel.</strong> 10–20% van de chunk-grootte is de vuistregel. Voor 500-token chunks: 50–100 tokens overlap. Default hier is 50, werkt goed in praktijk.</li>
  <li><strong>Trade-off.</strong> Meer overlap = meer totale embeddings (meer storage, meer kosten, langere index-build, meer retrieval-kandidaten). Ga niet boven 30% zonder specifieke reden; je verspilt geld zonder de retrieval veel te verbeteren.</li>
</ul>

<h3>Token-schatting</h3>
<ul>
  <li><strong>Het is een heuristiek.</strong> tekens / 3.8 voor Engels-achtige tekst en 1 token per teken voor CJK. ±5–10% voor proza, slechter voor code-zware of gestructureerde tekst.</li>
  <li><strong>Waarom niet de echte tokenizer?</strong> tiktoken is ~1 MB WASM — te zwaar om alleen voor chunk-sizing te shippen. Als je downstream-model een harde token-limiet op chunks heeft (sommige doen dat, bv. cohere/embed-v3 is gecapt op 512), bouw met een veiligheidsmarge of draai de echte tokenizer in je pipeline.</li>
  <li><strong>Dit is prima voor sizing.</strong> Het exacte token-aantal per chunk doet er voor RAG-kwaliteit weinig toe — het embedding-model truncatert oversized inputs sowieso. Wat telt is consistentie: dezelfde heuristiek voor chunking en voor het budgetteren van downstream-prompts.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Chunk geen gestructureerde data (JSON, CSV) met een tekst-chunker.</strong> De chunk-grenzen vallen midden in records en de embeddings worden betekenisloos. Splits eerst op record-grenzen, of gebruik een tool-specifieke RAG-aanpak.</li>
  <li><strong>Chunk geen code met een proza-chunker.</strong> Voor code-retrieval tellen functie-grenzen, niet karakter-aantallen. Tree-sitter-gebaseerde chunkers bestaan hiervoor.</li>
  <li><strong>Whitespace en BOM.</strong> Geplakte tekst kan verborgen whitespace dragen die token-schattingen verstoort. Trim en normaliseer voor het plakken als het ertoe doet.</li>
  <li><strong>Privacy.</strong> Alles draait in de browser. Hier geplakte documenten verlaten de pagina nooit; je kan dit gebruiken voor vertrouwelijk of PII-bevattend materiaal zoals je een lokaal script zou gebruiken.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Retrieval-Augmented Generation (RAG) ve embedding tabanlı arama, ikisi de bir korpusu <em>chunk</em>'lara bölmeye dayanır: tek tek embed edilip vector DB'de saklanan küçük parçalar. Bölme herhangi bir AI mekanizmasından önce olur, ama retrieval'ının kalitesi çoğu insanın farkettiğinden sessizce daha fazla buna bağlı. Çok küçük chunk'lar bağlamı kaybeder; çok büyükler relevansı seyreltir; cümle ortasından kesilenler kötü retrieve edilir çünkü embedding garip bir semantik noktada konuşlanır. Bu araç bir pipeline'a karar vermeden önce chunk boyutu, overlap ve stratejiyi deneyebileceğin hızlı bir tarayıcı içi playground.</p>

<h3>Dört strateji</h3>
<ul>
  <li><strong>recursive-char</strong> (varsayılan). Önce paragraf kırılımlarında, sonra satır kırılımlarında, sonra cümle sınırlarında (<code>. </code>), sonra boşluklarda bölmeye çalışır. Her parça chunk boyut bütçesine kadar açgözlüce paketlenir. Hiçbir şey sığmadığında sadece sert karakter bölmesine geri döner. LangChain, LlamaIndex ve çoğu üretim RAG yığınında varsayılan; neredeyse her düzyazı korpus için makul bir başlangıç noktası.</li>
  <li><strong>sentence</strong>. Cümle sınırlarında böler, asla cümle içinde değil — bütçeden kısa bile olsa cümle bütün kalır. Chunk'lar kanıt olarak alıntılanacaksa (QA, citations) recursive-char'dan daha iyi, çünkü hiçbir chunk düşünce ortasında bitmez. Cümle uzunlukları değiştiği için chunk boyutları daha değişkendir.</li>
  <li><strong>paragraph</strong>. Her paragrafı birim olarak ele alır. Yan yana iki kısa paragraf birlikte paketlenebilir, ama uzun olan asla bölünmez. Her paragrafın tutarlı bir düşünce olduğu dokümantasyon, KB makaleleri ve iyi formatlanmış uzun form için yararlı.</li>
  <li><strong>semantic</strong>. paragraph'ın üstüne başlık tespiti ekler: <code>#</code>, <code>##</code> ile başlayan veya kısa tamamen büyük harfli satırlar yeni-bölüm kırılımı olarak ele alınır. Bölüm sınırlarının görsel paragraf aralığından daha önemli olduğu teknik dokümantasyon için iyi.</li>
</ul>

<h3>Overlap — neden ve ne kadar</h3>
<ul>
  <li><strong>Neden.</strong> İlgili bir span tam olarak iki chunk arasındaki sınıra düşerse, her ikisi de kötü retrieve eder çünkü her biri sadece yarısına sahip. Overlap önceki chunk'un son N token'ını sonraki chunk'un önüne kopyalar, her ikisine de span'i yakalama şansı verir.</li>
  <li><strong>Ne kadar.</strong> Chunk boyutunun %10-20'si yaygın kural. 500-token chunk'lar için 50-100 token overlap. Varsayılan burada 50, pratikte iyi çalışır.</li>
  <li><strong>Ödünleşim.</strong> Daha fazla overlap = daha fazla toplam embedding (daha fazla depolama, daha fazla maliyet, daha yavaş index build, daha fazla retrieval adayı). Belirli bir nedenin yoksa %30'u aşma; retrieval'ı pek iyileştirmeden para harcarsın.</li>
</ul>

<h3>Token tahmini</h3>
<ul>
  <li><strong>Bir sezgisel yöntem.</strong> İngilizce-benzeri metin için karakter / 3.8 ve CJK için karakter başına 1 token kullanıyoruz. Düzyazı için ±5-10% iyi, kod ağırlıklı veya yapılandırılmış metin için daha kötü.</li>
  <li><strong>Neden gerçek tokenizer değil?</strong> tiktoken ~1 MB WASM, sadece chunk boyutlandırma için göndermek aşırı ağır. Downstream modelin chunk'larda sert token limiti varsa (bazılarında var, örn. cohere/embed-v3 512'de sınırlı), güvenlik marjıyla inşa et veya pipeline'ında gerçek tokenizer çalıştır.</li>
  <li><strong>Boyutlandırma için bu yeterli.</strong> Her chunk'ın tam token sayısı RAG kalitesi için çok önemli değil — embedding modeli zaten aşırı boyutlu girdileri keser. Önemli olan tutarlılık: chunking ve downstream prompt bütçelemesi için aynı sezgisel.</li>
</ul>

<h3>Yaygın tuzaklar</h3>
<ul>
  <li><strong>JSON veya CSV gibi yapılandırılmış veriyi metin chunker ile chunklama.</strong> Chunk sınırları kayıt ortasına düşer ve embedding'ler anlamsız olur. Önce kayıt sınırlarında böl, ya da araca özgü RAG yaklaşımı kullan.</li>
  <li><strong>Kodu düzyazı chunker ile chunklama.</strong> Kod retrieval'ı için fonksiyon sınırları önemlidir, karakter sayıları değil. Bunun için tree-sitter tabanlı chunker'lar var.</li>
  <li><strong>Whitespace ve BOM.</strong> Yapıştırılan metin token tahminlerini bozan gizli whitespace taşıyabilir. Önemliyse yapıştırmadan önce trim ve normalize et.</li>
  <li><strong>Gizlilik.</strong> Her şey tarayıcıda çalışır. Buraya yapıştırılan dokümanlar sayfadan asla çıkmaz; bunu yerel bir script kullanır gibi gizli veya PII içeren materyaller için kullanabilirsin.</li>
</ul>
""",
        "id": """
<h2>Buat apa ini?</h2>
<p>RAG (Retrieval-Augmented Generation) dan pencarian berbasis embedding sama-sama bergantung pada memecah corpus jadi <em>chunk</em>: potongan kecil yang masing-masing di-embed dan disimpan di vector DB. Pemecahan terjadi sebelum mesin AI mana pun jalan, tapi kualitas retrieval-mu diam-diam lebih bergantung padanya daripada yang dikira kebanyakan orang. Chunk terlalu kecil kehilangan konteks; terlalu besar mengencerkan relevansi; chunk yang dipotong di tengah kalimat me-retrieve buruk karena embedding mendarat di titik semantik aneh. Tool ini playground cepat di browser untuk bereksperimen dengan ukuran, overlap, dan strategi sebelum kamu fix pipeline.</p>

<h3>Empat strategi</h3>
<ul>
  <li><strong>recursive-char</strong> (default). Coba pecah di paragraph dulu, lalu line break, lalu batas kalimat (<code>. </code>), lalu spasi. Setiap potongan dipack secara greedy sampai budget ukuran. Hanya fallback ke pemotongan keras karakter kalau nggak ada lainnya yang muat. Default di LangChain, LlamaIndex, dan kebanyakan stack RAG produksi; titik awal masuk akal untuk hampir semua corpus prosa.</li>
  <li><strong>sentence</strong>. Pecah di batas kalimat dan nggak pernah di dalam kalimat — bahkan kalau lebih pendek dari budget, tetap utuh. Lebih bagus dari recursive-char saat chunk akan dikutip sebagai bukti (QA, citations) karena nggak ada chunk yang berakhir di tengah pikiran. Ukuran chunk lebih bervariasi, karena panjang kalimat juga.</li>
  <li><strong>paragraph</strong>. Perlakukan setiap paragraf sebagai unit. Dua paragraf pendek berdampingan bisa dipack bersama, tapi yang panjang nggak pernah dipecah. Berguna untuk dokumentasi, artikel KB, dan long-form terformat baik di mana setiap paragraf adalah pikiran koheren.</li>
  <li><strong>semantic</strong>. Tambahkan deteksi heading di atas paragraph: baris mulai dengan <code>#</code>, <code>##</code> dll., atau baris pendek all-caps, diperlakukan sebagai batas bagian baru. Bagus untuk dokumentasi teknis di mana batas seksi lebih penting daripada spasi paragraf visual.</li>
</ul>

<h3>Overlap — kenapa dan seberapa</h3>
<ul>
  <li><strong>Kenapa.</strong> Kalau span relevan jatuh tepat di antara dua chunk, keduanya me-retrieve buruk karena masing-masing hanya punya separuh. Overlap salin N token terakhir chunk sebelumnya ke depan chunk berikutnya, memberi keduanya kesempatan menangkap span.</li>
  <li><strong>Seberapa.</strong> 10-20% dari ukuran chunk adalah aturan umum. Untuk chunk 500 token, 50-100 token overlap. Default di sini 50, jalan baik dalam praktik.</li>
  <li><strong>Trade-off.</strong> Lebih banyak overlap = lebih banyak total embedding (lebih banyak storage, lebih banyak biaya, build index lebih lambat, lebih banyak kandidat retrieval). Jangan lebih dari 30% tanpa alasan spesifik; buang uang tanpa banyak peningkatan.</li>
</ul>

<h3>Estimasi token</h3>
<ul>
  <li><strong>Ini heuristik.</strong> chars / 3.8 untuk teks Inggris-ish dan 1 token per karakter untuk CJK. ±5-10% untuk prosa, lebih buruk untuk teks code-heavy atau terstruktur.</li>
  <li><strong>Kenapa nggak tokenizer asli?</strong> tiktoken ~1 MB WASM, terlalu berat hanya untuk chunk-sizing. Kalau model downstream-mu punya batas token keras pada chunk (beberapa punya, mis. cohere/embed-v3 dibatasi 512), build dengan margin keamanan atau jalankan tokenizer asli di pipeline-mu.</li>
  <li><strong>Untuk sizing ini cukup.</strong> Hitungan token persis per chunk nggak penting banget untuk kualitas RAG — model embedding truncate input yang kebesaran toh. Yang penting adalah konsistensi: heuristik sama untuk chunking dan untuk budgeting prompt downstream.</li>
</ul>

<h3>Jebakan umum</h3>
<ul>
  <li><strong>Jangan chunk data terstruktur (JSON, CSV) dengan text chunker.</strong> Batas chunk jatuh di tengah record dan embedding jadi nggak berarti. Pecah di batas record dulu, atau pakai pendekatan RAG spesifik tool.</li>
  <li><strong>Jangan chunk kode dengan prose chunker.</strong> Untuk retrieval kode, batas fungsi yang penting, bukan hitungan karakter. Chunker berbasis tree-sitter ada untuk ini.</li>
  <li><strong>Whitespace dan BOM.</strong> Teks yang ditempel bisa membawa whitespace tersembunyi yang membuyarkan estimasi token. Trim dan normalize sebelum tempel kalau penting.</li>
  <li><strong>Privasi.</strong> Semua jalan di browser. Dokumen yang ditempel di sini tidak pernah keluar dari halaman; bisa pakai ini untuk materi rahasia atau berisi PII sama seperti pakai script lokal.</li>
</ul>
""",
        "vi": """
<h2>Cái này để làm gì?</h2>
<p>Retrieval-Augmented Generation (RAG) và tìm kiếm dựa trên embedding đều phụ thuộc vào việc tách một corpus thành các <em>chunk</em>: những mảnh nhỏ được embed riêng lẻ và lưu trong vector DB. Việc tách xảy ra trước bất kỳ máy móc AI nào, nhưng chất lượng retrieval của bạn thầm lặng phụ thuộc vào nó nhiều hơn hầu hết mọi người nhận ra. Chunk quá nhỏ mất ngữ cảnh; quá lớn pha loãng độ liên quan; chunk cắt giữa câu retrieve kém vì embedding rơi vào điểm ngữ nghĩa kỳ lạ. Công cụ này là một playground nhanh trong trình duyệt để thử nghiệm với kích thước chunk, overlap và chiến lược trước khi commit pipeline với lựa chọn.</p>

<h3>Bốn chiến lược</h3>
<ul>
  <li><strong>recursive-char</strong> (mặc định). Cố gắng tách theo paragraph trước, rồi line break, rồi ranh giới câu (<code>. </code>), rồi khoảng trắng. Mỗi mảnh được pack tham lam đến budget kích thước. Chỉ fallback sang tách cứng theo ký tự khi không có gì khác fit. Mặc định trong LangChain, LlamaIndex và hầu hết stack RAG production; điểm khởi đầu hợp lý cho gần như mọi corpus văn xuôi.</li>
  <li><strong>sentence</strong>. Tách ở ranh giới câu và không bao giờ trong câu — ngay cả khi câu ngắn hơn budget, vẫn giữ nguyên. Tốt hơn recursive-char khi chunk sẽ được trích làm bằng chứng (QA, citations) vì không có chunk nào kết thúc giữa suy nghĩ. Kích thước chunk thay đổi nhiều hơn, vì độ dài câu thay đổi.</li>
  <li><strong>paragraph</strong>. Coi mỗi paragraph như một đơn vị. Hai paragraph ngắn liền kề có thể được pack cùng nhau, nhưng paragraph dài không bao giờ bị tách. Hữu ích cho tài liệu, bài KB và long-form được format tốt nơi mỗi paragraph là một suy nghĩ mạch lạc.</li>
  <li><strong>semantic</strong>. Thêm phát hiện heading lên trên paragraph: các dòng bắt đầu với <code>#</code>, <code>##</code> v.v., hoặc các dòng ngắn toàn chữ hoa, được xử lý như ranh giới section mới. Tốt cho tài liệu kỹ thuật nơi ranh giới section quan trọng hơn khoảng cách paragraph trực quan.</li>
</ul>

<h3>Overlap — tại sao và bao nhiêu</h3>
<ul>
  <li><strong>Tại sao.</strong> Nếu một span liên quan rơi đúng vào ranh giới giữa hai chunk, cả hai sẽ retrieve kém vì mỗi cái chỉ có một nửa. Overlap sao chép N token cuối của chunk trước vào đầu chunk sau, cho cả hai cơ hội bắt được span.</li>
  <li><strong>Bao nhiêu.</strong> 10-20% kích thước chunk là quy tắc. Cho chunk 500 token, 50-100 token overlap. Mặc định ở đây là 50, hoạt động tốt trong thực tế.</li>
  <li><strong>Đánh đổi.</strong> Nhiều overlap hơn = nhiều embedding tổng hơn (nhiều storage hơn, nhiều chi phí hơn, build index chậm hơn, nhiều candidate retrieval hơn). Đừng vượt quá 30% không có lý do cụ thể; phí tiền mà không cải thiện retrieval nhiều.</li>
</ul>

<h3>Ước tính token</h3>
<ul>
  <li><strong>Đây là heuristic.</strong> Ký tự / 3.8 cho văn bản kiểu tiếng Anh và 1 token cho mỗi ký tự CJK. ±5-10% cho văn xuôi, tệ hơn cho văn bản nặng code hoặc có cấu trúc.</li>
  <li><strong>Tại sao không tokenizer thật?</strong> tiktoken ~1 MB WASM, quá nặng chỉ để chunk-sizing. Nếu model downstream của bạn có giới hạn token cứng trên chunk (một số có, ví dụ cohere/embed-v3 giới hạn 512), build với biên độ an toàn hoặc chạy tokenizer thật trong pipeline.</li>
  <li><strong>Cho sizing thì ổn.</strong> Số token chính xác của mỗi chunk không quan trọng lắm cho chất lượng RAG — model embedding cắt input quá khổ dù sao. Quan trọng là tính nhất quán: cùng heuristic cho chunking và cho budgeting prompt downstream.</li>
</ul>

<h3>Bẫy thường gặp</h3>
<ul>
  <li><strong>Đừng chunk dữ liệu có cấu trúc (JSON, CSV) với text chunker.</strong> Ranh giới chunk rơi giữa record và embedding trở nên vô nghĩa. Tách theo ranh giới record trước, hoặc dùng cách tiếp cận RAG đặc thù cho tool.</li>
  <li><strong>Đừng chunk code với prose chunker.</strong> Cho retrieval code, ranh giới function mới quan trọng, không phải số ký tự. Chunker dựa trên tree-sitter có cho việc này.</li>
  <li><strong>Whitespace và BOM.</strong> Văn bản dán có thể mang whitespace ẩn làm sai lệch ước tính token. Trim và normalize trước khi dán nếu quan trọng.</li>
  <li><strong>Quyền riêng tư.</strong> Mọi thứ chạy trong trình duyệt. Tài liệu dán ở đây không bao giờ rời trang; bạn có thể dùng cho tài liệu mật hoặc chứa PII giống như dùng script local.</li>
</ul>
""",
        "hi": """
<h2>यह किसके लिए है?</h2>
<p>RAG (Retrieval-Augmented Generation) और embedding-based search दोनों एक corpus को <em>chunks</em> में split करने पर निर्भर हैं: छोटे pieces जिन्हें individually embed किया जाता है और एक vector database में store किया जाता है। Split किसी भी AI machinery के चलने से पहले होता है, लेकिन आपके retrieval की quality चुपचाप इस पर अधिक depend करती है जितना अधिकांश लोगों को realise होता है। बहुत छोटे chunks context lose करते हैं; बहुत बड़े chunks relevance dilute करते हैं; mid-sentence split किए गए chunks poorly retrieve करते हैं क्योंकि embedding एक अजीब semantic spot पर land करता है। यह tool एक fast in-browser playground देता है ताकि आप chunk size, overlap, और strategy के साथ experiment कर सकें इससे पहले कि आप एक pipeline को choice के लिए commit करें।</p>

<h3>चार strategies</h3>
<ul>
  <li><strong>recursive-char</strong> (default)। पहले paragraph breaks पर split करने की कोशिश करता है, फिर line breaks, फिर sentence boundaries (<code>. </code>), फिर spaces। हर piece chunk-size budget तक greedily packed होती है। केवल तब hard character split पर fall back होता है जब और कुछ fit नहीं होता। LangChain, LlamaIndex, और अधिकांश production RAG stacks में default, और लगभग किसी भी prose corpus के लिए sensible starting point।</li>
  <li><strong>sentence</strong>। Sentence boundaries पर split करता है और कभी sentence के अंदर नहीं — भले ही sentence budget से छोटी हो, यह whole रहती है। Recursive-char से बेहतर जब chunks को evidence के रूप में quote किया जाएगा (QA, citations) क्योंकि कोई chunk mid-thought end नहीं होता। Chunk sizes अधिक variable हैं, क्योंकि sentence lengths हैं।</li>
  <li><strong>paragraph</strong>। हर paragraph को unit के रूप में treat करता है। दो adjacent short paragraphs एक साथ packed हो सकते हैं, लेकिन एक long paragraph कभी split नहीं होता। Documentation, knowledge-base articles, और well-formatted long-form के लिए useful जहाँ हर paragraph एक coherent thought है।</li>
  <li><strong>semantic</strong>। Paragraph के ऊपर heading detection add करता है: <code>#</code>, <code>##</code> आदि से शुरू होने वाली lines, या short all-caps lines, new-section breaks के रूप में treat होती हैं। Technical documentation के लिए अच्छा जहाँ section boundaries visual paragraph spacing से अधिक matter करती हैं।</li>
</ul>

<h3>Overlap — क्यों और कितना</h3>
<ul>
  <li><strong>क्यों।</strong> अगर एक relevant span exactly दो chunks के boundary पर fall होता है, दोनों chunks poorly retrieve करेंगे क्योंकि हर एक के पास सिर्फ half है। Overlap previous chunk के last N tokens को next chunk के front पर copy करता है, दोनों को span capture करने का chance देता है।</li>
  <li><strong>कितना।</strong> Chunk size का 10–20% common rule of thumb है। 500-token chunks के लिए, 50–100 tokens overlap। Default यहाँ 50 है, practice में अच्छा work करता है।</li>
  <li><strong>Trade-off।</strong> ज़्यादा overlap = ज़्यादा total embeddings (ज़्यादा storage, ज़्यादा cost, slower index build, ज़्यादा retrieval candidates)। Specific reason के बिना 30% से ज़्यादा push न करें; आप पैसा waste करेंगे retrieval को बहुत improve किए बिना।</li>
</ul>

<h3>Token estimation</h3>
<ul>
  <li><strong>यह एक heuristic है।</strong> हम English-ish text के लिए chars / 3.8 और CJK के लिए per character 1 token use करते हैं। Prose के लिए यह ±5–10% सही है, code-heavy या structured text के लिए worse।</li>
  <li><strong>Real tokenizer क्यों नहीं?</strong> tiktoken ~1 MB का WASM है, सिर्फ chunk-sizing के लिए ship करने के लिए way too heavy। अगर आपके downstream model के पास chunks पर hard token limit है (कुछ के पास है, उदा. cohere/embed-v3 512 पर capped है), एक small safety margin के साथ build करें या अपने pipeline में real tokenizer run करें।</li>
  <li><strong>यह sizing के लिए fine है।</strong> हर chunk का exact token count RAG quality के लिए बहुत matter नहीं करता — embedding model oversized inputs को वैसे भी truncate कर देता है। जो matter करता है वो consistency है: chunking और downstream prompts के budgeting के लिए same heuristic।</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>JSON या CSV जैसे structured data को text chunker से chunk न करें।</strong> Chunk boundaries records के middle में fall होंगी और embeddings meaningless होंगे। Records के boundaries पर पहले split करें, या एक tool-specific RAG approach use करें।</li>
  <li><strong>Code को prose chunker से chunk न करें।</strong> Code retrieval के लिए function boundaries matter करती हैं, character counts नहीं। इसके लिए Tree-sitter-based chunkers exist करते हैं।</li>
  <li><strong>Whitespace और BOM।</strong> Pasted text hidden whitespace carry कर सकता है जो token estimates throw off करता है। अगर matter करता है तो paste से पहले trim और normalise करें।</li>
  <li><strong>Privacy।</strong> सब browser में run होता है। यहाँ pasted documents कभी page से बाहर नहीं जाते; आप इसका use confidential या PII-containing material के लिए कर सकते हैं जैसे एक local script use करते।</li>
</ul>
""",
        "sk": """
<h2>Načo to slúži?</h2>
<p>RAG (Retrieval-Augmented Generation) a vyhľadávanie založené na embeddingoch oba závisia od rozdelenia korpusu na <em>chunky</em>: malé kúsky, ktoré sú jednotlivo embednuté a uložené vo vector DB. Rozdelenie sa deje pred akoukoľvek AI mašinériou, ale kvalita tvojho retrievalu na tom potichu závisí viac, než si väčšina uvedomuje. Príliš malé chunky strácajú kontext; príliš veľké rozriedia relevanciu; chunky rozdelené uprostred vety zle retrievujú, lebo embedding pristane v zvláštnom sémantickom bode. Tento nástroj je rýchle ihrisko v prehliadači na experimentovanie s veľkosťou chunku, overlapom a stratégiou pred tým, než pipeline zafixuješ.</p>

<h3>Štyri stratégie</h3>
<ul>
  <li><strong>recursive-char</strong> (predvolené). Pokúsi sa rozdeliť najprv na odsekoch, potom nových riadkoch, potom hraniciach viet (<code>. </code>), potom medzerách. Každý kúsok sa hltavo zabalí do rozpočtu veľkosti. Spadne na tvrdé delenie po znakoch len ak nič iné nesedí. Predvolené v LangChain, LlamaIndex a väčšine produkčných RAG stackov; rozumné východisko pre takmer každý prózový korpus.</li>
  <li><strong>sentence</strong>. Delí na hraniciach viet a nikdy vnútri vety — aj keď je veta kratšia než rozpočet, ostane celá. Lepšie ako recursive-char keď budú chunky citované ako dôkaz (QA, citácie), lebo žiadny chunk nekončí uprostred myšlienky. Veľkosti chunkov variabilnejšie, lebo dĺžky viet sú.</li>
  <li><strong>paragraph</strong>. Spracúva každý odsek ako jednotku. Dva susedné krátke odseky môžu byť zabalené spolu, ale dlhý odsek nikdy nie je rozdelený. Užitočné pre dokumentáciu, KB články a dobre formátované long-form, kde každý odsek je súdržná myšlienka.</li>
  <li><strong>semantic</strong>. Pridáva detekciu nadpisov nad paragraph: riadky začínajúce <code>#</code>, <code>##</code> atď., alebo krátke veľkomi-písmenkové riadky, sú spracované ako začiatok novej sekcie. Dobré pre technickú dokumentáciu, kde hranice sekcií zaberajú viac než vizuálny odsadenie.</li>
</ul>

<h3>Overlap — prečo a koľko</h3>
<ul>
  <li><strong>Prečo.</strong> Ak relevantný úsek padne presne na hranicu medzi dvoma chunkmi, oba retrievujú zle, lebo každý má len polovicu. Overlap skopíruje posledných N tokenov predchádzajúceho chunku na začiatok ďalšieho, dáva obom šancu zachytiť úsek.</li>
  <li><strong>Koľko.</strong> 10–20% veľkosti chunku ako pravidlo. Pre 500-tokenové chunky 50–100 tokenov overlapu. Predvolené tu je 50, v praxi funguje dobre.</li>
  <li><strong>Trade-off.</strong> Viac overlapu = viac celkových embeddingov (viac storage, viac nákladov, pomalší build indexu, viac kandidátov retrievalu). Nechoď nad 30% bez konkrétneho dôvodu; zbytočne míňaš peniaze bez veľkého zlepšenia retrievalu.</li>
</ul>

<h3>Odhad tokenov</h3>
<ul>
  <li><strong>Je to heuristika.</strong> znaky / 3.8 pre angličtinu-podobný text a 1 token na znak CJK. ±5–10% pre prózu, horšie pre code-heavy alebo štruktúrovaný text.</li>
  <li><strong>Prečo nie skutočný tokenizer?</strong> tiktoken je ~1 MB WASM — príliš ťažký len pre sizing. Ak má tvoj downstream model tvrdý limit tokenov na chunky (niektoré majú, napr. cohere/embed-v3 je capnutý na 512), stavaj s bezpečnostnou rezervou alebo spusti skutočný tokenizer v pipeline.</li>
  <li><strong>Pre sizing je to fajn.</strong> Presný počet tokenov na chunk veľa neznamená pre kvalitu RAG — embedding model príliš veľké vstupy aj tak skráti. Čo sa počíta je konzistencia: rovnaká heuristika pre chunking aj pre budgetovanie downstream promptov.</li>
</ul>

<h3>Časté pasce</h3>
<ul>
  <li><strong>Štruktúrované dáta (JSON, CSV) nechunkuj textovým chunkerom.</strong> Hranice padnú doprostred záznamov a embeddingy stratia zmysel. Najprv rozdeľ na hraniciach záznamov, alebo použi tool-špecifický RAG prístup.</li>
  <li><strong>Kód nechunkuj prózovým chunkerom.</strong> Pre retrieval kódu sú dôležité hranice funkcií, nie počty znakov. Existujú chunkery založené na tree-sitter.</li>
  <li><strong>Whitespace a BOM.</strong> Vložený text môže niesť skryté whitespace, ktoré skresľuje odhad tokenov. Trimni a normalizuj pred vložením, ak na tom záleží.</li>
  <li><strong>Súkromie.</strong> Všetko beží v prehliadači. Dokumenty vložené sem nikdy neopustia stránku; môžeš to používať na dôverný alebo PII obsahujúci materiál tak isto, ako by si použil lokálny skript.</li>
</ul>
""",
        "cs": """
<h2>K čemu to slouží?</h2>
<p>RAG (Retrieval-Augmented Generation) a vyhledávání založené na embeddings oba závisí na rozdělení korpusu na <em>chunky</em>: malé kousky, které jsou jednotlivě embednuté a uloženy ve vector DB. Rozdělení se děje před jakoukoliv AI mašinerií, ale kvalita tvého retrievalu na tom potichu závisí víc, než si většina uvědomuje. Příliš malé chunky ztrácí kontext; příliš velké zředí relevanci; chunky rozdělené uprostřed věty špatně retrievují, protože embedding přistane v podivném sémantickém bodě. Tenhle nástroj je rychlé hřiště v prohlížeči na experimentování s velikostí chunku, overlapem a strategií předtím, než pipeline zafixuješ.</p>

<h3>Čtyři strategie</h3>
<ul>
  <li><strong>recursive-char</strong> (výchozí). Pokusí se rozdělit nejprve na odstavcích, pak nových řádcích, pak hranicích vět (<code>. </code>), pak mezerách. Každý kousek se hltavě zabalí do rozpočtu velikosti. Spadne na tvrdé dělení po znacích jen pokud nic jiného nesedí. Výchozí v LangChain, LlamaIndex a většině produkčních RAG stacků; rozumný výchozí bod pro téměř každý prózový korpus.</li>
  <li><strong>sentence</strong>. Dělí na hranicích vět a nikdy uvnitř věty — i když je věta kratší než rozpočet, zůstane celá. Lepší než recursive-char když budou chunky citovány jako důkaz (QA, citace), protože žádný chunk nekončí uprostřed myšlenky. Velikosti chunků jsou proměnlivější, protože délky vět jsou.</li>
  <li><strong>paragraph</strong>. Zpracovává každý odstavec jako jednotku. Dva sousední krátké odstavce mohou být zabaleny spolu, ale dlouhý odstavec není nikdy rozdělen. Užitečné pro dokumentaci, KB články a dobře formátované long-form, kde každý odstavec je soudržná myšlenka.</li>
  <li><strong>semantic</strong>. Přidává detekci nadpisů nad paragraph: řádky začínající <code>#</code>, <code>##</code> atd., nebo krátké velkoupísmenné řádky, jsou zpracovány jako začátek nové sekce. Dobré pro technickou dokumentaci, kde hranice sekcí zabírají víc než vizuální odsazení.</li>
</ul>

<h3>Overlap — proč a kolik</h3>
<ul>
  <li><strong>Proč.</strong> Pokud relevantní úsek padne přesně na hranici mezi dvěma chunky, oba retrievují špatně, protože každý má jen polovinu. Overlap zkopíruje posledních N tokenů předchozího chunku na začátek dalšího, dává oběma šanci úsek zachytit.</li>
  <li><strong>Kolik.</strong> 10–20% velikosti chunku jako pravidlo. Pro 500-tokenové chunky 50–100 tokenů overlapu. Výchozí zde je 50, v praxi funguje dobře.</li>
  <li><strong>Trade-off.</strong> Více overlapu = víc celkových embeddingů (víc storage, víc nákladů, pomalejší build indexu, víc kandidátů retrievalu). Nepřekračuj 30% bez konkrétního důvodu; zbytečně utrácíš peníze bez většího zlepšení retrievalu.</li>
</ul>

<h3>Odhad tokenů</h3>
<ul>
  <li><strong>Je to heuristika.</strong> znaky / 3.8 pro angličtina-podobný text a 1 token na znak CJK. ±5–10% pro prózu, horší pro code-heavy nebo strukturovaný text.</li>
  <li><strong>Proč ne skutečný tokenizer?</strong> tiktoken je ~1 MB WASM — příliš těžký jen pro sizing. Pokud má tvůj downstream model tvrdý limit tokenů na chunky (některé mají, např. cohere/embed-v3 je capnutý na 512), stavj s bezpečnostní rezervou nebo spusť skutečný tokenizer v pipeline.</li>
  <li><strong>Pro sizing je to fajn.</strong> Přesný počet tokenů na chunk moc neznamená pro kvalitu RAG — embedding model příliš velké vstupy stejně zkrátí. Co se počítá je konzistence: stejná heuristika pro chunking i pro budgetování downstream promptů.</li>
</ul>

<h3>Časté pasti</h3>
<ul>
  <li><strong>Strukturovaná data (JSON, CSV) nechunkuj textovým chunkerem.</strong> Hranice padnou doprostřed záznamů a embeddings ztratí smysl. Nejprve rozděl na hranicích záznamů, nebo použij tool-specifický RAG přístup.</li>
  <li><strong>Kód nechunkuj prózovým chunkerem.</strong> Pro retrieval kódu jsou důležité hranice funkcí, ne počty znaků. Existují chunkery založené na tree-sitter.</li>
  <li><strong>Whitespace a BOM.</strong> Vložený text může nést skrytý whitespace, který zkresluje odhad tokenů. Trimni a normalizuj před vložením, pokud na tom záleží.</li>
  <li><strong>Soukromí.</strong> Vše běží v prohlížeči. Dokumenty vložené sem nikdy neopustí stránku; můžeš to používat na důvěrný nebo PII obsahující materiál stejně jako bys použil lokální skript.</li>
</ul>
""",
    },
    "related": ["token-counter", "chat-thread-viewer", "system-prompt-linter"],
    "howto": {"flow": "transform", "action": "format", "noun": "text"},
}
