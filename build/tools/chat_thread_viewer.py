TOOL = {
    "slug": "chat-thread-viewer",
    "category": "ai",
    "icon": "💬",
    "tags": ["chat", "messages", "openai", "anthropic", "viewer", "thread", "llm", "conversation", "render"],
    "i18n": {
        "en": {
            "name": "Chat Thread Viewer",
            "tagline": "Paste an OpenAI or Anthropic messages array (JSON) and see it rendered as a readable chat thread. Color-coded by role. Tool-call params expanded. Pure browser, no upload.",
            "description": "Free in-browser viewer for LLM conversation history. Paste a JSON messages array (OpenAI chat completions format, Anthropic Messages API format, or LangChain dump) and get a clean chat-thread render: role-colored bubbles, expandable tool-call parameters, syntax-highlighted code blocks, image references. Designed for debugging long conversations and audit-reviewing prompts post-hoc.",
        },
        "de": {
            "name": "Chat-Thread-Viewer",
            "tagline": "Füge ein OpenAI- oder Anthropic-Messages-Array (JSON) ein und sieh es als lesbaren Chat-Thread. Nach Rolle farbcodiert. Tool-Call-Parameter ausklappbar. Reiner Browser, kein Upload.",
            "description": "Kostenloser Browser-Viewer für LLM-Konversationshistorien. Füge ein JSON-Messages-Array ein (OpenAI Chat Completions, Anthropic Messages API oder LangChain-Dump) und erhalte eine saubere Chat-Thread-Ansicht: rollenfarbige Bubbles, ausklappbare Tool-Call-Parameter, syntax-hervorgehobene Codeblöcke, Bildverweise. Gemacht für Debugging langer Konversationen und nachträgliche Prompt-Reviews.",
        },
        "es": {
            "name": "Visor de Hilos de Chat",
            "tagline": "Pega un array de messages de OpenAI o Anthropic (JSON) y míralo como un hilo de chat legible. Coloreado por rol. Parámetros de tool-calls expandibles. Solo navegador, sin subida.",
            "description": "Visor gratuito en el navegador para historiales de conversación con LLMs. Pega un array JSON de messages (formato OpenAI Chat Completions, Anthropic Messages API o dump de LangChain) y obtén un render limpio: burbujas coloreadas por rol, parámetros de tool-calls expandibles, bloques de código resaltados, referencias a imágenes. Pensado para depurar conversaciones largas y revisar prompts a posteriori.",
        },
        "fr": {
            "name": "Visualiseur de Fil de Chat",
            "tagline": "Collez un tableau de messages OpenAI ou Anthropic (JSON) et voyez-le rendu en fil de chat lisible. Code couleur par rôle. Paramètres de tool-calls dépliables. Pur navigateur, sans upload.",
            "description": "Visualiseur gratuit dans le navigateur pour les historiques de conversation LLM. Collez un tableau JSON de messages (format OpenAI Chat Completions, Anthropic Messages API ou dump LangChain) et obtenez un rendu propre : bulles colorées par rôle, paramètres de tool-calls dépliables, blocs de code colorés, références d'image. Conçu pour déboguer de longues conversations et auditer les prompts a posteriori.",
        },
        "it": {
            "name": "Visualizzatore Thread di Chat",
            "tagline": "Incolla un array di messages OpenAI o Anthropic (JSON) e vedilo come thread di chat leggibile. Colorato per ruolo. Parametri tool-call espandibili. Solo browser, niente upload.",
            "description": "Visualizzatore gratuito nel browser per gli storici di conversazione con LLM. Incolla un array JSON di messages (formato OpenAI Chat Completions, Anthropic Messages API o dump LangChain) e ottieni un rendering pulito: bolle colorate per ruolo, parametri di tool-call espandibili, blocchi di codice evidenziati, riferimenti a immagini. Pensato per debuggare conversazioni lunghe e per audit dei prompt a posteriori.",
        },
        "pt": {
            "name": "Visualizador de Thread de Chat",
            "tagline": "Cole um array de messages OpenAI ou Anthropic (JSON) e veja como uma thread de chat legível. Cor por papel. Parâmetros de tool-call expansíveis. Só navegador, sem upload.",
            "description": "Visualizador grátis no navegador pra histórico de conversa de LLM. Cole um array JSON de messages (formato OpenAI Chat Completions, Anthropic Messages API ou dump do LangChain) e tenha um render limpo: balões coloridos por papel, parâmetros de tool-call expansíveis, blocos de código realçados, referências de imagem. Feito pra depurar conversas longas e revisar prompts depois do fato.",
        },
        "pl": {
            "name": "Przeglądarka Wątków Chatu",
            "tagline": "Wklej tablicę messages OpenAI lub Anthropic (JSON) i zobacz ją jako czytelny wątek czatu. Kolory wg roli. Parametry tool-calli rozwijane. Tylko przeglądarka, bez uploadu.",
            "description": "Darmowa przeglądarka historii rozmów z LLM-ami w przeglądarce. Wklej tablicę JSON messages (format OpenAI Chat Completions, Anthropic Messages API albo dump z LangChain) i dostaniesz czysty render: kolorowe dymki wg roli, rozwijane parametry tool-calli, podświetlone bloki kodu, odwołania do obrazków. Do debugowania długich rozmów i audytu promptów po fakcie.",
        },
        "ja": {
            "name": "チャットスレッドビューア",
            "tagline": "OpenAI または Anthropic の messages 配列（JSON）を貼り付けると、読みやすいチャットスレッドとして表示。ロール別に色分け。ツールコールの引数も展開可能。ブラウザ完結・アップロードなし。",
            "description": "LLM 会話履歴のためのブラウザ完結ビューア（無料）。messages の JSON 配列（OpenAI Chat Completions 形式、Anthropic Messages API 形式、または LangChain のダンプ）を貼り付けると、見やすいチャットスレッドにレンダリングします。ロール別に色分けされたバブル、展開可能なツールコール引数、コードブロックのシンタックスハイライト、画像参照を表示。長い会話のデバッグや、プロンプトの事後監査に便利です。",
        },
        "nl": {
            "name": "Chat Thread Viewer",
            "tagline": "Plak een OpenAI- of Anthropic-messages-array (JSON) en zie het als leesbare chat-thread. Kleur per rol. Tool-call-parameters uitklapbaar. Pure browser, geen upload.",
            "description": "Gratis in-browser viewer voor LLM-conversatiehistorie. Plak een JSON-messages-array (OpenAI Chat Completions-formaat, Anthropic Messages API-formaat of LangChain-dump) en krijg een schone chat-thread-render: rol-gekleurde bubbels, uitklapbare tool-call-parameters, syntax-gehighlighte codeblokken, image-verwijzingen. Voor het debuggen van lange conversaties en post-hoc prompt-audits.",
        },
        "tr": {
            "name": "Sohbet Thread Görüntüleyici",
            "tagline": "OpenAI veya Anthropic messages dizisini (JSON) yapıştır, okunabilir bir sohbet thread'i olarak göster. Role göre renkli. Tool-call parametreleri açılabilir. Tamamen tarayıcıda, yükleme yok.",
            "description": "LLM konuşma geçmişi için ücretsiz tarayıcı içi görüntüleyici. JSON messages dizisini yapıştır (OpenAI Chat Completions formatı, Anthropic Messages API formatı veya LangChain dump'ı), temiz bir sohbet thread render'ı al: role göre renkli baloncuklar, açılabilir tool-call parametreleri, sözdizimi renklendirmesi olan kod blokları, görsel referansları. Uzun konuşmaları debug etmek ve prompt'ları sonradan denetlemek için tasarlandı.",
        },
        "id": {
            "name": "Penampil Thread Chat",
            "tagline": "Tempel array messages OpenAI atau Anthropic (JSON) dan lihat sebagai thread chat yang mudah dibaca. Diwarnai per role. Parameter tool-call bisa diexpand. Murni browser, tanpa upload.",
            "description": "Penampil gratis di browser untuk riwayat percakapan LLM. Tempel array JSON messages (format OpenAI Chat Completions, Anthropic Messages API, atau dump LangChain) dan dapatkan render thread chat yang bersih: gelembung berwarna sesuai role, parameter tool-call yang bisa diexpand, blok kode dengan syntax highlight, referensi gambar. Dirancang untuk debug percakapan panjang dan audit prompt setelah fakta.",
        },
        "vi": {
            "name": "Trình Xem Thread Chat",
            "tagline": "Dán mảng messages của OpenAI hoặc Anthropic (JSON) và xem dưới dạng thread chat dễ đọc. Tô màu theo vai trò. Tham số tool-call có thể mở rộng. Hoàn toàn trên trình duyệt, không upload.",
            "description": "Trình xem miễn phí trong trình duyệt cho lịch sử hội thoại LLM. Dán mảng JSON messages (định dạng OpenAI Chat Completions, Anthropic Messages API, hoặc dump LangChain) và nhận được render thread chat sạch sẽ: bong bóng tô màu theo vai trò, tham số tool-call mở rộng được, khối code được tô sáng cú pháp, tham chiếu hình ảnh. Dành cho việc debug các hội thoại dài và audit prompt sau khi xảy ra.",
        },
        "hi": {
            "name": "Chat Thread Viewer",
            "tagline": "OpenAI या Anthropic का messages array (JSON) paste करें और एक readable chat thread के रूप में देखें। Role-wise color-coded। Tool-call parameters expandable। Pure browser, कोई upload नहीं।",
            "description": "LLM conversation history के लिए मुफ़्त in-browser viewer। JSON messages array paste करें (OpenAI Chat Completions format, Anthropic Messages API format, या LangChain dump) और एक clean chat-thread render पाएं: role-colored bubbles, expandable tool-call parameters, syntax-highlighted code blocks, image references। लंबी conversations को debug करने और prompts को बाद में audit करने के लिए बनाया गया।",
        },
        "sk": {
            "name": "Prehliadač chat threadov",
            "tagline": "Vlož pole messages od OpenAI alebo Anthropicu (JSON) a uvidíš ho ako čitateľný chat thread. Farby podľa roly. Parametre tool-callov rozbaliteľné. Čisto v prehliadači, žiadny upload.",
            "description": "Bezplatný prehliadač histórie konverzácií s LLM v prehliadači. Vlož JSON pole messages (formát OpenAI Chat Completions, Anthropic Messages API alebo dump LangChain) a dostaneš čistý render chat threadu: farebné bubliny podľa roly, rozbaliteľné parametre tool-callov, code bloky so syntaxovým zvýraznením, referencie na obrázky. Na debugovanie dlhých konverzácií a spätný audit promptov.",
        },
        "cs": {
            "name": "Prohlížeč chat threadů",
            "tagline": "Vlož pole messages od OpenAI nebo Anthropicu (JSON) a uvidíš ho jako čitelný chat thread. Barvy podle role. Parametry tool-callů rozbalitelné. Čistě v prohlížeči, žádný upload.",
            "description": "Bezplatný prohlížeč historie konverzací s LLM v prohlížeči. Vlož JSON pole messages (formát OpenAI Chat Completions, Anthropic Messages API nebo dump LangChain) a dostaneš čistý render chat threadu: barevné bubliny podle role, rozbalitelné parametry tool-callů, code bloky se syntaktickým zvýrazněním, odkazy na obrázky. Na debugování dlouhých konverzací a zpětný audit promptů.",
        },
    },
    "body": """
<div class="tool-card">
  <label for="ctv-input">Paste messages JSON (OpenAI / Anthropic / LangChain)</label>
  <textarea id="ctv-input" oninput="ctvRun()" spellcheck="false" placeholder='[{"role": "user", "content": "Hello"}, {"role": "assistant", "content": "Hi there!"}]'>[
  {"role": "system", "content": "You are a helpful assistant. Answer concisely."},
  {"role": "user", "content": "What is the capital of France?"},
  {"role": "assistant", "content": "The capital of France is Paris."},
  {"role": "user", "content": "What's the weather there?"},
  {"role": "assistant", "content": null, "tool_calls": [{"id": "call_abc123", "type": "function", "function": {"name": "get_weather", "arguments": "{\\"city\\": \\"Paris\\"}"}}]},
  {"role": "tool", "tool_call_id": "call_abc123", "content": "{\\"temp_c\\": 14, \\"condition\\": \\"cloudy\\"}"},
  {"role": "assistant", "content": "It's currently 14°C and cloudy in Paris."}
]</textarea>
  <div class="button-row" style="margin-top:0.5rem">
    <input type="text" id="ctv-search" oninput="ctvRender()" placeholder="🔍 Search within thread…" style="flex:1;min-width:200px">
    <button class="secondary" onclick="document.getElementById('ctv-input').value='';ctvRun()">{LBL_CLEAR}</button>
  </div>
  <div class="meta" id="ctv-stats" style="margin-top:0.5rem"></div>
</div>
<div class="tool-card">
  <div id="ctv-thread" class="ctv-thread"></div>
</div>
""",
    "script": """
<style>
.ctv-thread{display:flex;flex-direction:column;gap:0.7rem;max-height:760px;overflow-y:auto;padding:0.4rem}
.ctv-empty{padding:1.5rem;color:var(--text-muted);text-align:center}
.ctv-msg{display:flex;flex-direction:column;max-width:88%;border-radius:10px;padding:0.65rem 0.85rem;border:1px solid var(--border);font-size:0.92rem;line-height:1.5}
.ctv-msg-system{background:rgba(148,163,184,0.10);border-color:rgba(148,163,184,0.3);align-self:center;max-width:96%;font-size:0.86rem;color:var(--text-muted)}
.ctv-msg-user{background:rgba(99,102,241,0.10);border-color:rgba(99,102,241,0.35);align-self:flex-end}
.ctv-msg-assistant{background:var(--bg-elev);align-self:flex-start}
.ctv-msg-tool{background:rgba(34,197,94,0.08);border-color:rgba(34,197,94,0.35);align-self:flex-start;font-family:ui-monospace,monospace;font-size:0.82rem}
.ctv-msg-error{background:rgba(239,68,68,0.10);border-color:rgba(239,68,68,0.4);align-self:center;color:#ef4444}
.ctv-role{font-size:0.72rem;text-transform:uppercase;letter-spacing:0.05em;font-weight:600;margin-bottom:0.35rem;opacity:0.75}
.ctv-msg-user .ctv-role{color:#6366f1}
.ctv-msg-assistant .ctv-role{color:var(--accent)}
.ctv-msg-tool .ctv-role{color:#22c55e}
.ctv-content{white-space:pre-wrap;word-break:break-word}
.ctv-content code{background:rgba(0,0,0,0.08);padding:0.05rem 0.3rem;border-radius:3px;font-size:0.9em}
.ctv-content pre{background:rgba(0,0,0,0.10);padding:0.55rem 0.75rem;border-radius:6px;overflow:auto;margin:0.35rem 0;font-size:0.82rem;border:1px solid var(--border)}
.ctv-toolcall{margin-top:0.4rem;padding:0.45rem 0.6rem;background:rgba(0,0,0,0.06);border:1px dashed var(--border);border-radius:6px;font-family:ui-monospace,monospace;font-size:0.8rem}
.ctv-toolcall summary{cursor:pointer;font-weight:600;color:#22c55e}
.ctv-toolcall pre{margin:0.4rem 0 0 0;background:transparent;padding:0;border:none}
.ctv-img{display:inline-block;margin-top:0.4rem;padding:0.35rem 0.55rem;background:rgba(0,0,0,0.06);border:1px solid var(--border);border-radius:6px;font-family:ui-monospace,monospace;font-size:0.78rem;color:var(--text-muted)}
.ctv-mark{background:rgba(251,191,36,0.45);color:inherit;padding:0 2px;border-radius:2px}
.ctv-fmt{display:inline-block;padding:0.15rem 0.5rem;border-radius:99px;background:rgba(99,102,241,0.15);color:#6366f1;font-size:0.72rem;font-weight:600;font-family:ui-monospace,monospace}
.ctv-stat{display:inline-block;margin-right:1rem}
.ctv-stat strong{color:var(--text)}
</style>
<script>
let ctvMessages = [];
let ctvFormat = '—';
let ctvError = null;
function ctvEsc(s){ return String(s ?? '').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
function ctvDetectFormat(arr){
  if (!Array.isArray(arr) || arr.length === 0) return 'empty';
  const first = arr[0];
  if (first && typeof first.type === 'string' && !first.role) return 'langchain';
  for (const m of arr){
    if (m && Array.isArray(m.content)){
      for (const block of m.content){
        if (block && typeof block === 'object' && (block.type === 'tool_use' || block.type === 'tool_result' || block.type === 'text' || block.type === 'image')) return 'anthropic';
      }
    }
  }
  for (const m of arr){
    if (m && (m.tool_calls || m.role === 'tool' || (m.role === 'system'))) return 'openai';
  }
  return 'openai';
}
function ctvRun(){
  const raw = document.getElementById('ctv-input').value.trim();
  ctvError = null;
  if (!raw){ ctvMessages = []; ctvFormat = '—'; ctvRender(); return; }
  let parsed;
  try { parsed = JSON.parse(raw); }
  catch(e){ ctvError = 'Invalid JSON: ' + e.message; ctvMessages = []; ctvRender(); return; }
  // Accept either an array, or an object with .messages
  let arr = parsed;
  if (!Array.isArray(parsed)){
    if (parsed && Array.isArray(parsed.messages)) arr = parsed.messages;
    else if (parsed && Array.isArray(parsed.input)) arr = parsed.input;
    else { ctvError = 'Expected a JSON array of messages, or an object with a "messages" array.'; ctvMessages = []; ctvRender(); return; }
  }
  ctvFormat = ctvDetectFormat(arr);
  ctvMessages = arr;
  ctvRender();
}
function ctvRenderMarkdown(text){
  if (text == null) return '';
  let s = ctvEsc(text);
  // fenced code blocks
  s = s.replace(/```(\\w*)\\n([\\s\\S]*?)```/g, function(_, lang, code){
    return '<pre><code>' + code.replace(/\\n$/, '') + '</code></pre>';
  });
  // inline code
  s = s.replace(/`([^`\\n]+)`/g, '<code>$1</code>');
  return s;
}
function ctvHighlight(html, q){
  if (!q) return html;
  const lower = html.toLowerCase();
  const needle = q.toLowerCase();
  let out = '';
  let i = 0;
  while (i < html.length){
    const j = lower.indexOf(needle, i);
    if (j === -1){ out += html.slice(i); break; }
    // skip if inside a tag (rough heuristic)
    const lastLt = html.lastIndexOf('<', j);
    const lastGt = html.lastIndexOf('>', j);
    if (lastLt > lastGt){
      out += html.slice(i, j + needle.length);
      i = j + needle.length;
      continue;
    }
    out += html.slice(i, j) + '<span class="ctv-mark">' + html.slice(j, j + needle.length) + '</span>';
    i = j + needle.length;
  }
  return out;
}
function ctvEstimateTokens(text){
  if (!text) return 0;
  const s = typeof text === 'string' ? text : JSON.stringify(text);
  const cjk = (s.match(/[぀-ヿ㐀-䶿一-鿿가-힯]/g) || []).length;
  const len = s.length;
  return Math.ceil((len - cjk) / 3.8 + cjk);
}
function ctvRenderOne(m, q){
  const role = (m && m.role) || (m && m.type) || 'unknown';
  let cls = 'ctv-msg-' + role;
  if (role === 'human') cls = 'ctv-msg-user';
  if (role === 'ai') cls = 'ctv-msg-assistant';
  if (!['user','assistant','system','tool','human','ai'].includes(role)) cls = 'ctv-msg-assistant';
  const displayRole = role === 'human' ? 'user' : (role === 'ai' ? 'assistant' : role);
  let bodyHtml = '';
  let toolCalls = 0;
  // Anthropic-style content array
  if (Array.isArray(m.content)){
    for (const block of m.content){
      if (!block || typeof block !== 'object'){
        bodyHtml += '<div class="ctv-content">' + ctvHighlight(ctvRenderMarkdown(String(block)), q) + '</div>';
        continue;
      }
      if (block.type === 'text'){
        bodyHtml += '<div class="ctv-content">' + ctvHighlight(ctvRenderMarkdown(block.text || ''), q) + '</div>';
      } else if (block.type === 'tool_use'){
        toolCalls++;
        const inputPretty = JSON.stringify(block.input ?? {}, null, 2);
        bodyHtml += '<details class="ctv-toolcall" open><summary>🔧 tool_use: ' + ctvEsc(block.name || '?') + ' (' + ctvEsc(block.id || '') + ')</summary><pre>' + ctvHighlight(ctvEsc(inputPretty), q) + '</pre></details>';
      } else if (block.type === 'tool_result'){
        const content = typeof block.content === 'string' ? block.content : JSON.stringify(block.content, null, 2);
        bodyHtml += '<details class="ctv-toolcall" open><summary>📤 tool_result (' + ctvEsc(block.tool_use_id || '') + ')</summary><pre>' + ctvHighlight(ctvEsc(content), q) + '</pre></details>';
      } else if (block.type === 'image'){
        const src = block.source && (block.source.url || block.source.media_type || '[base64]');
        bodyHtml += '<div class="ctv-img">🖼 image — ' + ctvEsc(src || '?') + '</div>';
      } else {
        bodyHtml += '<details class="ctv-toolcall" open><summary>' + ctvEsc(block.type || 'block') + '</summary><pre>' + ctvHighlight(ctvEsc(JSON.stringify(block, null, 2)), q) + '</pre></details>';
      }
    }
  } else if (typeof m.content === 'string'){
    bodyHtml += '<div class="ctv-content">' + ctvHighlight(ctvRenderMarkdown(m.content), q) + '</div>';
  } else if (m.content == null && Array.isArray(m.tool_calls)){
    // OpenAI assistant tool calls
    // body rendered below
  } else if (m.content != null){
    bodyHtml += '<div class="ctv-content">' + ctvHighlight(ctvEsc(JSON.stringify(m.content)), q) + '</div>';
  }
  // OpenAI-style tool_calls field on assistant message
  if (Array.isArray(m.tool_calls)){
    for (const tc of m.tool_calls){
      toolCalls++;
      const name = tc.function && tc.function.name || tc.name || '?';
      let args = tc.function && tc.function.arguments || tc.arguments || '';
      let argsPretty = args;
      if (typeof args === 'string'){
        try { argsPretty = JSON.stringify(JSON.parse(args), null, 2); } catch(_){}
      } else {
        argsPretty = JSON.stringify(args, null, 2);
      }
      bodyHtml += '<details class="ctv-toolcall" open><summary>🔧 tool_call: ' + ctvEsc(name) + ' (' + ctvEsc(tc.id || '') + ')</summary><pre>' + ctvHighlight(ctvEsc(argsPretty), q) + '</pre></details>';
    }
  }
  // OpenAI-style tool result message
  if (m.role === 'tool' && typeof m.content === 'string' && m.tool_call_id){
    bodyHtml = '<div class="ctv-role">tool · ' + ctvEsc(m.tool_call_id) + '</div>' +
               '<div class="ctv-content">' + ctvHighlight(ctvEsc(m.content), q) + '</div>';
    return { html: '<div class="ctv-msg ctv-msg-tool">' + bodyHtml + '</div>', toolCalls };
  }
  const header = '<div class="ctv-role">' + ctvEsc(displayRole) + (m.name ? ' · ' + ctvEsc(m.name) : '') + '</div>';
  return { html: '<div class="ctv-msg ' + cls + '">' + header + bodyHtml + '</div>', toolCalls };
}
function ctvRender(){
  const container = document.getElementById('ctv-thread');
  const statsEl = document.getElementById('ctv-stats');
  if (ctvError){
    container.innerHTML = '<div class="ctv-msg ctv-msg-error">' + ctvEsc(ctvError) + '</div>';
    statsEl.innerHTML = '';
    return;
  }
  if (!ctvMessages.length){
    container.innerHTML = '<div class="ctv-empty">Paste a JSON messages array above to render the chat thread.</div>';
    statsEl.innerHTML = '';
    return;
  }
  const q = document.getElementById('ctv-search').value;
  let toolCalls = 0;
  let totalTokens = 0;
  const pieces = ctvMessages.map(m => {
    const { html, toolCalls: tc } = ctvRenderOne(m, q);
    toolCalls += tc;
    totalTokens += ctvEstimateTokens(JSON.stringify(m));
    return html;
  });
  container.innerHTML = pieces.join('');
  const fmtLabel = ctvFormat === 'openai' ? 'OpenAI' : ctvFormat === 'anthropic' ? 'Anthropic' : ctvFormat === 'langchain' ? 'LangChain' : ctvFormat;
  statsEl.innerHTML =
    '<span class="ctv-stat"><span class="ctv-fmt">' + ctvEsc(fmtLabel) + '</span></span>' +
    '<span class="ctv-stat"><strong>' + ctvMessages.length + '</strong> messages</span>' +
    '<span class="ctv-stat"><strong>' + toolCalls + '</strong> tool calls</span>' +
    '<span class="ctv-stat">~<strong>' + totalTokens.toLocaleString() + '</strong> tokens (est)</span>';
}
document.addEventListener('DOMContentLoaded', ctvRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>LLM applications log their conversations as JSON arrays of messages — that's what gets sent to the API and what you'll see in audit logs, evaluation traces, fine-tuning datasets, and SDK debug output. Reading those arrays as a human is awful: walls of escaped strings, tool-call arguments wrapped in escaped JSON-inside-JSON, system prompts mashed in with the rest of the flow. This tool gives you a quick chat-bubble render so you can scan the actual conversation, see which messages contained tool calls, and spot the one prompt that went sideways.</p>

<h3>What formats it understands</h3>
<ul>
  <li><strong>OpenAI Chat Completions.</strong> <code>[{role, content}, ...]</code> with optional <code>tool_calls</code> on assistant messages and <code>role: "tool"</code> for tool results. The most common shape.</li>
  <li><strong>Anthropic Messages API.</strong> <code>[{role, content: [...]}]</code> where <code>content</code> is an array of blocks (<code>text</code>, <code>tool_use</code>, <code>tool_result</code>, <code>image</code>). System prompt is usually top-level — paste it as a system message if you want it shown.</li>
  <li><strong>LangChain message dumps.</strong> <code>[{type: "human" | "ai" | "system", content: ...}]</code> — older LangChain shape, still common in saved traces.</li>
  <li><strong>Wrapper objects.</strong> If you paste <code>{"messages": [...]}</code> or <code>{"input": [...]}</code>, the wrapper gets unwrapped automatically.</li>
</ul>

<h3>What gets rendered</h3>
<ul>
  <li><strong>Role-coloured bubbles.</strong> System = grey centred, user = indigo right-aligned, assistant = neutral left-aligned, tool result = green.</li>
  <li><strong>Tool calls.</strong> Expanded by default with pretty-printed arguments. Both OpenAI's <code>tool_calls</code> form and Anthropic's <code>tool_use</code> block style are handled. Tool result messages render as a separate bubble with the result content.</li>
  <li><strong>Code fences and inline code.</strong> Triple-backtick blocks render as <code>&lt;pre&gt;</code> with monospace, single-backtick spans render as inline code. No syntax highlighting (we don't ship a tokenizer for that), but indentation is preserved.</li>
  <li><strong>Image references.</strong> Anthropic image blocks render a small pill showing the source URL or media type — we don't actually load the image (keeps the tool offline).</li>
  <li><strong>Stats line.</strong> Format detected, message count, tool-call count, and a rough token estimate using the same heuristic as our Token Counter (chars / 3.8 for English, 1 token per CJK char).</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Trailing commas.</strong> Standard JSON doesn't allow them. If you copied from a debugger or REPL output, you may need to clean up <code>{...},]</code> → <code>{...}]</code> before pasting.</li>
  <li><strong>Single quotes.</strong> Python's <code>repr</code> uses single quotes. Run it through <code>json.dumps</code> before pasting, or use a Python-literal-to-JSON converter.</li>
  <li><strong>Anthropic system prompt.</strong> The system instruction in Anthropic's API is a top-level field, not a message. If your dump only has the messages array, the system prompt won't be in there — paste it as <code>{"role": "system", "content": "..."}</code> at the start to see it.</li>
  <li><strong>Tool-call arguments as escaped JSON.</strong> OpenAI returns <code>arguments</code> as a string of JSON. We unescape and pretty-print it. If your JSON-in-string is malformed, the raw string is shown instead.</li>
  <li><strong>Privacy.</strong> Nothing leaves the page. The whole render runs in JS on whatever JSON you paste. Don't paste anything you wouldn't paste into a notepad app.</li>
</ul>
""",
        "de": """
<h2>Wozu ist das gut?</h2>
<p>LLM-Anwendungen protokollieren ihre Konversationen als JSON-Arrays von Nachrichten — das wird an die API geschickt und taucht in Audit-Logs, Evaluation-Traces, Fine-Tuning-Datensätzen und SDK-Debug-Output auf. Diese Arrays als Mensch zu lesen ist grauenhaft: Mauern aus escapten Strings, Tool-Call-Argumente in escaptem JSON-in-JSON, System-Prompts mit dem Rest vermischt. Dieses Tool rendert dir schnell Chat-Bubbles, damit du die tatsächliche Konversation überblickst, siehst welche Nachrichten Tool-Calls enthielten und den einen Prompt findest, der schiefging.</p>

<h3>Welche Formate erkannt werden</h3>
<ul>
  <li><strong>OpenAI Chat Completions.</strong> <code>[{role, content}, ...]</code> mit optionalen <code>tool_calls</code> auf Assistant-Nachrichten und <code>role: "tool"</code> für Tool-Ergebnisse. Die häufigste Form.</li>
  <li><strong>Anthropic Messages API.</strong> <code>[{role, content: [...]}]</code> wo <code>content</code> ein Array von Blöcken ist (<code>text</code>, <code>tool_use</code>, <code>tool_result</code>, <code>image</code>). System-Prompt ist meist Top-Level — füg ihn als System-Message ein, wenn du ihn sehen willst.</li>
  <li><strong>LangChain-Message-Dumps.</strong> <code>[{type: "human" | "ai" | "system", content: ...}]</code> — ältere LangChain-Form, in gespeicherten Traces noch häufig.</li>
  <li><strong>Wrapper-Objekte.</strong> Bei <code>{"messages": [...]}</code> oder <code>{"input": [...]}</code> wird der Wrapper automatisch entpackt.</li>
</ul>

<h3>Was gerendert wird</h3>
<ul>
  <li><strong>Rollenfarbige Bubbles.</strong> System = grau zentriert, User = indigo rechts, Assistant = neutral links, Tool-Ergebnis = grün.</li>
  <li><strong>Tool-Calls.</strong> Standardmäßig aufgeklappt mit hübsch gedruckten Argumenten. OpenAIs <code>tool_calls</code> und Anthropics <code>tool_use</code>-Blöcke werden beide unterstützt. Tool-Ergebnis-Nachrichten erscheinen als eigene Bubble.</li>
  <li><strong>Code-Fences und Inline-Code.</strong> Dreifach-Backtick-Blöcke werden zu <code>&lt;pre&gt;</code> in Monospace, einfache Backticks zu Inline-Code. Kein Syntax-Highlighting (wir liefern keinen Tokenizer dafür), Einrückung bleibt erhalten.</li>
  <li><strong>Bildverweise.</strong> Anthropic-Image-Blöcke werden als kleine Pille mit Source-URL oder Media-Type angezeigt — das Bild wird nicht geladen (Tool bleibt offline).</li>
  <li><strong>Stats-Zeile.</strong> Erkanntes Format, Nachrichtenzahl, Tool-Call-Zahl und grobe Token-Schätzung mit derselben Heuristik wie unser Token Counter.</li>
</ul>

<h3>Typische Stolperfallen</h3>
<ul>
  <li><strong>Trailing commas.</strong> Standard-JSON erlaubt sie nicht. Aus Debugger- oder REPL-Output musst du eventuell <code>{...},]</code> → <code>{...}]</code> säubern.</li>
  <li><strong>Single Quotes.</strong> Pythons <code>repr</code> nutzt Single Quotes. Lass es durch <code>json.dumps</code> laufen, oder nutze einen Python-Literal-zu-JSON-Konverter.</li>
  <li><strong>Anthropic-System-Prompt.</strong> Die System-Anweisung ist in Anthropics API ein Top-Level-Feld, keine Nachricht. Wenn dein Dump nur das Messages-Array enthält, ist der System-Prompt nicht drin — füg ihn als <code>{"role": "system", "content": "..."}</code> am Anfang ein.</li>
  <li><strong>Tool-Call-Argumente als escapte JSON.</strong> OpenAI gibt <code>arguments</code> als JSON-String zurück. Wir entescape und hübsch drucken. Wenn das JSON im String kaputt ist, wird der rohe String gezeigt.</li>
  <li><strong>Privacy.</strong> Nichts verlässt die Seite. Alles läuft in JS auf dem JSON, das du einfügst. Füg nichts ein, was du nicht in einen Notepad einfügen würdest.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>Las apps de LLM registran sus conversaciones como arrays JSON de mensajes — eso es lo que se envía a la API y lo que ves en logs de auditoría, trazas de evaluación, datasets de fine-tuning y debug del SDK. Leer esos arrays a ojo es horrible: muros de strings escapados, argumentos de tool-call envueltos en JSON-dentro-de-JSON escapado, prompts de sistema mezclados con el resto. Esta herramienta te da un render rápido en burbujas para que escanees la conversación real, veas qué mensajes incluyeron tool-calls y encuentres el prompt que descarriló.</p>

<h3>Qué formatos entiende</h3>
<ul>
  <li><strong>OpenAI Chat Completions.</strong> <code>[{role, content}, ...]</code> con <code>tool_calls</code> opcionales en mensajes de asistente y <code>role: "tool"</code> para resultados de tool. La forma más común.</li>
  <li><strong>Anthropic Messages API.</strong> <code>[{role, content: [...]}]</code> donde <code>content</code> es un array de bloques (<code>text</code>, <code>tool_use</code>, <code>tool_result</code>, <code>image</code>). El system prompt suele ir top-level — pégalo como mensaje de sistema si quieres verlo.</li>
  <li><strong>Dumps de mensajes de LangChain.</strong> <code>[{type: "human" | "ai" | "system", content: ...}]</code> — forma antigua de LangChain, aún común en trazas guardadas.</li>
  <li><strong>Objetos wrapper.</strong> Si pegas <code>{"messages": [...]}</code> o <code>{"input": [...]}</code>, se desenvuelve automáticamente.</li>
</ul>

<h3>Qué se renderiza</h3>
<ul>
  <li><strong>Burbujas coloreadas por rol.</strong> System = gris centrado, user = índigo a la derecha, assistant = neutro a la izquierda, tool result = verde.</li>
  <li><strong>Tool-calls.</strong> Expandidos por defecto con argumentos formateados. Se soportan tanto <code>tool_calls</code> de OpenAI como bloques <code>tool_use</code> de Anthropic. Los mensajes de resultado aparecen en su propia burbuja.</li>
  <li><strong>Code fences e inline code.</strong> Bloques con triple backtick van a <code>&lt;pre&gt;</code> en monoespaciado, backticks simples a inline. Sin resaltado de sintaxis (no llevamos tokenizer), la indentación se preserva.</li>
  <li><strong>Referencias de imagen.</strong> Los bloques de imagen de Anthropic se muestran como una píldora con la URL o media-type — no cargamos la imagen (la herramienta queda offline).</li>
  <li><strong>Línea de stats.</strong> Formato detectado, número de mensajes, número de tool-calls y estimación rápida de tokens con la misma heurística que nuestro Token Counter.</li>
</ul>

<h3>Errores comunes</h3>
<ul>
  <li><strong>Comas finales.</strong> El JSON estándar no las permite. Si copiaste de un debugger o REPL, puede que tengas que limpiar <code>{...},]</code> → <code>{...}]</code> antes de pegar.</li>
  <li><strong>Comillas simples.</strong> El <code>repr</code> de Python usa simples. Pásalo por <code>json.dumps</code>, o usa un convertidor Python-literal a JSON.</li>
  <li><strong>System prompt de Anthropic.</strong> La instrucción de sistema en la API de Anthropic es un campo top-level, no un mensaje. Si tu dump solo tiene el array de messages, el system prompt no estará — pégalo como <code>{"role": "system", "content": "..."}</code> al principio.</li>
  <li><strong>Argumentos de tool-call como JSON escapado.</strong> OpenAI devuelve <code>arguments</code> como string JSON. Lo desescapamos y formateamos. Si el JSON dentro del string está roto, se muestra el string crudo.</li>
  <li><strong>Privacidad.</strong> Nada sale de la página. Todo el render corre en JS sobre el JSON que pegas. No pegues nada que no pegarías en una app de notas.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Les applis LLM journalisent leurs conversations en tableaux JSON de messages — c'est ce qui est envoyé à l'API et ce que vous verrez dans les audit logs, traces d'évaluation, datasets de fine-tuning et debug SDK. Lire ces tableaux à l'œil nu est pénible : murs de chaînes échappées, arguments de tool-calls enveloppés dans du JSON-dans-JSON échappé, system prompts mélangés au reste. Cet outil vous donne un rendu rapide en bulles pour scanner la vraie conversation, voir quels messages contenaient des tool-calls, et repérer le prompt qui a déraillé.</p>

<h3>Quels formats il comprend</h3>
<ul>
  <li><strong>OpenAI Chat Completions.</strong> <code>[{role, content}, ...]</code> avec <code>tool_calls</code> optionnels sur les messages assistant et <code>role: "tool"</code> pour les résultats de tool. La forme la plus courante.</li>
  <li><strong>Anthropic Messages API.</strong> <code>[{role, content: [...]}]</code> où <code>content</code> est un tableau de blocs (<code>text</code>, <code>tool_use</code>, <code>tool_result</code>, <code>image</code>). Le system prompt est généralement au niveau racine — collez-le comme message system si vous voulez le voir.</li>
  <li><strong>Dumps de messages LangChain.</strong> <code>[{type: "human" | "ai" | "system", content: ...}]</code> — ancienne forme LangChain, encore courante dans les traces sauvegardées.</li>
  <li><strong>Objets wrapper.</strong> Si vous collez <code>{"messages": [...]}</code> ou <code>{"input": [...]}</code>, le wrapper est déballé automatiquement.</li>
</ul>

<h3>Ce qui est rendu</h3>
<ul>
  <li><strong>Bulles colorées par rôle.</strong> System = gris centré, user = indigo à droite, assistant = neutre à gauche, résultat de tool = vert.</li>
  <li><strong>Tool-calls.</strong> Dépliés par défaut avec arguments mis en forme. Les <code>tool_calls</code> d'OpenAI et les blocs <code>tool_use</code> d'Anthropic sont tous deux gérés. Les messages de résultat apparaissent dans leur propre bulle.</li>
  <li><strong>Code fences et inline code.</strong> Blocs triples backticks rendus en <code>&lt;pre&gt;</code> monospace, backticks simples en code inline. Pas de coloration syntaxique (on n'embarque pas de tokenizer pour ça), l'indentation est préservée.</li>
  <li><strong>Références d'image.</strong> Les blocs image d'Anthropic affichent une petite pastille avec l'URL ou le media-type — on ne charge pas l'image (l'outil reste offline).</li>
  <li><strong>Ligne de stats.</strong> Format détecté, nombre de messages, nombre de tool-calls, et estimation grossière de tokens avec la même heuristique que notre Token Counter.</li>
</ul>

<h3>Pièges courants</h3>
<ul>
  <li><strong>Virgules en fin.</strong> Le JSON standard ne les autorise pas. Si vous avez copié depuis un debugger ou REPL, vous devrez peut-être nettoyer <code>{...},]</code> → <code>{...}]</code> avant de coller.</li>
  <li><strong>Quotes simples.</strong> Le <code>repr</code> Python utilise les simples. Passez-le par <code>json.dumps</code>, ou utilisez un convertisseur Python-literal vers JSON.</li>
  <li><strong>System prompt Anthropic.</strong> L'instruction system dans l'API Anthropic est un champ top-level, pas un message. Si votre dump ne contient que le tableau messages, le system prompt n'y sera pas — collez-le comme <code>{"role": "system", "content": "..."}</code> en tête.</li>
  <li><strong>Arguments de tool-call en JSON échappé.</strong> OpenAI renvoie <code>arguments</code> comme string JSON. On le désescappe et le formate. Si le JSON-dans-string est cassé, la string brute est affichée.</li>
  <li><strong>Privacy.</strong> Rien ne quitte la page. Tout le rendu tourne en JS sur le JSON collé. Ne collez rien que vous ne colleriez pas dans une appli de notes.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>Le app LLM loggano le conversazioni come array JSON di messaggi — è ciò che viene mandato all'API e ciò che vedi negli audit log, nelle trace di valutazione, nei dataset di fine-tuning e nel debug dell'SDK. Leggere quegli array a occhio è atroce: muri di stringhe escapate, argomenti di tool-call avvolti in JSON-dentro-JSON escapato, system prompt mischiati col resto. Questo strumento ti dà un render rapido a bolle per scorrere la conversazione vera, vedere quali messaggi contenevano tool-call e individuare il prompt che è andato fuori strada.</p>

<h3>Quali formati capisce</h3>
<ul>
  <li><strong>OpenAI Chat Completions.</strong> <code>[{role, content}, ...]</code> con <code>tool_calls</code> opzionali sui messaggi assistant e <code>role: "tool"</code> per i risultati. La forma più comune.</li>
  <li><strong>Anthropic Messages API.</strong> <code>[{role, content: [...]}]</code> dove <code>content</code> è un array di blocchi (<code>text</code>, <code>tool_use</code>, <code>tool_result</code>, <code>image</code>). Il system prompt è di solito top-level — incollalo come messaggio system se vuoi vederlo.</li>
  <li><strong>Dump messaggi LangChain.</strong> <code>[{type: "human" | "ai" | "system", content: ...}]</code> — forma più vecchia di LangChain, ancora comune nelle trace salvate.</li>
  <li><strong>Oggetti wrapper.</strong> Se incolli <code>{"messages": [...]}</code> o <code>{"input": [...]}</code>, il wrapper viene scartato automaticamente.</li>
</ul>

<h3>Cosa viene renderizzato</h3>
<ul>
  <li><strong>Bolle colorate per ruolo.</strong> System = grigio centrato, user = indaco a destra, assistant = neutro a sinistra, tool result = verde.</li>
  <li><strong>Tool-call.</strong> Espansi di default con argomenti pretty-printed. Sia <code>tool_calls</code> di OpenAI sia i blocchi <code>tool_use</code> di Anthropic sono gestiti. I messaggi di risultato appaiono in una bolla separata.</li>
  <li><strong>Code fence e inline code.</strong> Blocchi tripli backtick come <code>&lt;pre&gt;</code> in monospace, singoli backtick come inline. Niente syntax highlighting (non spediamo un tokenizer per quello), l'indentazione è preservata.</li>
  <li><strong>Riferimenti immagini.</strong> I blocchi image di Anthropic mostrano una pillola piccola con URL o media-type — non carichiamo l'immagine (lo strumento resta offline).</li>
  <li><strong>Riga di stats.</strong> Formato rilevato, numero messaggi, numero tool-call e stima grezza di token con la stessa euristica del nostro Token Counter.</li>
</ul>

<h3>Trappole comuni</h3>
<ul>
  <li><strong>Virgole finali.</strong> Il JSON standard non le permette. Se hai copiato da debugger o REPL, potresti dover pulire <code>{...},]</code> → <code>{...}]</code> prima di incollare.</li>
  <li><strong>Apici singoli.</strong> Il <code>repr</code> di Python usa apici singoli. Passalo per <code>json.dumps</code>, o usa un convertitore Python-literal a JSON.</li>
  <li><strong>System prompt Anthropic.</strong> L'istruzione system nell'API Anthropic è un campo top-level, non un messaggio. Se il tuo dump ha solo l'array di messages, il system prompt non c'è — incollalo come <code>{"role": "system", "content": "..."}</code> all'inizio.</li>
  <li><strong>Argomenti tool-call come JSON escapato.</strong> OpenAI restituisce <code>arguments</code> come stringa JSON. Noi de-escappiamo e pretty-printiamo. Se il JSON nella stringa è rotto, viene mostrata la stringa grezza.</li>
  <li><strong>Privacy.</strong> Niente lascia la pagina. Tutto gira in JS sul JSON che incolli. Non incollare nulla che non incolleresti in una app di note.</li>
</ul>
""",
        "pt": """
<h2>Pra que serve?</h2>
<p>Apps de LLM logam suas conversas como arrays JSON de mensagens — é o que vai pra API e o que aparece em audit logs, traces de avaliação, datasets de fine-tuning e debug do SDK. Ler esses arrays a olho nu é doloroso: muros de strings escapadas, argumentos de tool-call envolvidos em JSON-dentro-de-JSON escapado, system prompts misturados com o resto. Esta ferramenta te dá um render rápido em balões pra você escanear a conversa real, ver quais mensagens tiveram tool-calls e achar o prompt que descarrilou.</p>

<h3>Quais formatos entende</h3>
<ul>
  <li><strong>OpenAI Chat Completions.</strong> <code>[{role, content}, ...]</code> com <code>tool_calls</code> opcionais em mensagens assistant e <code>role: "tool"</code> pra resultados de tool. A forma mais comum.</li>
  <li><strong>Anthropic Messages API.</strong> <code>[{role, content: [...]}]</code> onde <code>content</code> é um array de blocos (<code>text</code>, <code>tool_use</code>, <code>tool_result</code>, <code>image</code>). System prompt geralmente é top-level — cole como mensagem system se quiser ver.</li>
  <li><strong>Dumps de mensagens LangChain.</strong> <code>[{type: "human" | "ai" | "system", content: ...}]</code> — forma antiga do LangChain, ainda comum em traces salvos.</li>
  <li><strong>Objetos wrapper.</strong> Se você colar <code>{"messages": [...]}</code> ou <code>{"input": [...]}</code>, o wrapper é desempacotado automaticamente.</li>
</ul>

<h3>O que é renderizado</h3>
<ul>
  <li><strong>Balões coloridos por papel.</strong> System = cinza centralizado, user = índigo à direita, assistant = neutro à esquerda, tool result = verde.</li>
  <li><strong>Tool-calls.</strong> Expandidos por padrão com argumentos formatados. Tanto <code>tool_calls</code> da OpenAI quanto blocos <code>tool_use</code> da Anthropic são tratados. Mensagens de resultado aparecem em seu próprio balão.</li>
  <li><strong>Code fences e inline code.</strong> Blocos com triplo backtick viram <code>&lt;pre&gt;</code> em monoespaçado, backticks simples viram inline. Sem destaque de sintaxe (não levamos tokenizer pra isso), indentação preservada.</li>
  <li><strong>Referências de imagem.</strong> Blocos de imagem da Anthropic mostram uma pílula pequena com URL ou media-type — não carregamos a imagem (a ferramenta fica offline).</li>
  <li><strong>Linha de stats.</strong> Formato detectado, número de mensagens, número de tool-calls e estimativa aproximada de tokens com a mesma heurística do nosso Token Counter.</li>
</ul>

<h3>Pegadinhas comuns</h3>
<ul>
  <li><strong>Vírgulas finais.</strong> JSON padrão não permite. Se copiou de debugger ou REPL, talvez precise limpar <code>{...},]</code> → <code>{...}]</code> antes de colar.</li>
  <li><strong>Aspas simples.</strong> O <code>repr</code> do Python usa simples. Passe por <code>json.dumps</code>, ou use um conversor Python-literal pra JSON.</li>
  <li><strong>System prompt da Anthropic.</strong> A instrução system na API da Anthropic é campo top-level, não mensagem. Se seu dump só tem o array de messages, o system prompt não tá lá — cole como <code>{"role": "system", "content": "..."}</code> no começo.</li>
  <li><strong>Argumentos de tool-call como JSON escapado.</strong> OpenAI devolve <code>arguments</code> como string JSON. A gente desescapa e formata. Se o JSON dentro da string tá quebrado, mostra a string crua.</li>
  <li><strong>Privacidade.</strong> Nada sai da página. Tudo roda em JS no JSON que você cola. Não cole nada que não colaria num app de notas.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Aplikacje LLM logują rozmowy jako tablice JSON wiadomości — to jest to, co leci do API i co zobaczysz w audit logach, trace'ach ewaluacji, datasetach fine-tuningu i debugu SDK. Czytanie tych tablic gołym okiem to koszmar: ściany ucharowanych stringów, argumenty tool-calli zawinięte w escapowany JSON-w-JSON, system prompty pomieszane z resztą. To narzędzie daje ci szybki render w dymkach, żebyś przeszedł właściwą rozmowę, zobaczył które wiadomości zawierały tool-calle i znalazł ten jeden prompt, który wyleciał z torów.</p>

<h3>Jakie formaty rozumie</h3>
<ul>
  <li><strong>OpenAI Chat Completions.</strong> <code>[{role, content}, ...]</code> z opcjonalnymi <code>tool_calls</code> na wiadomościach assistanta i <code>role: "tool"</code> dla wyników tool. Najczęstsza forma.</li>
  <li><strong>Anthropic Messages API.</strong> <code>[{role, content: [...]}]</code> gdzie <code>content</code> to tablica bloków (<code>text</code>, <code>tool_use</code>, <code>tool_result</code>, <code>image</code>). System prompt jest zwykle top-level — wklej go jako wiadomość system, jeśli chcesz go zobaczyć.</li>
  <li><strong>Dumpy wiadomości LangChain.</strong> <code>[{type: "human" | "ai" | "system", content: ...}]</code> — starsza forma LangChain, wciąż częsta w zapisanych trace'ach.</li>
  <li><strong>Obiekty wrappery.</strong> Jak wkleisz <code>{"messages": [...]}</code> albo <code>{"input": [...]}</code>, wrapper jest automatycznie rozpakowany.</li>
</ul>

<h3>Co jest renderowane</h3>
<ul>
  <li><strong>Dymki kolorowane wg roli.</strong> System = szary wyśrodkowany, user = indygo po prawej, assistant = neutralny po lewej, tool result = zielony.</li>
  <li><strong>Tool-calle.</strong> Domyślnie rozwinięte z ładnie sformatowanymi argumentami. Obsługiwane są zarówno <code>tool_calls</code> z OpenAI jak i bloki <code>tool_use</code> z Anthropica. Wiadomości wyników pojawiają się w osobnym dymku.</li>
  <li><strong>Code fence'y i inline code.</strong> Bloki potrójnych backticków renderowane jako <code>&lt;pre&gt;</code> monospace, pojedyncze backticki jako inline code. Bez syntax highlightingu (nie wozimy tokenizera dla tego), wcięcia zachowane.</li>
  <li><strong>Odwołania do obrazków.</strong> Bloki image Anthropica pokazują małą pigułkę z URL-em albo media-type — obrazka nie ładujemy (narzędzie zostaje offline).</li>
  <li><strong>Linia statystyk.</strong> Wykryty format, liczba wiadomości, liczba tool-calli i przybliżona estymacja tokenów z tą samą heurystyką co Token Counter.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Trailing comma.</strong> Standardowe JSON ich nie pozwala. Jeśli skopiowałeś z debuggera albo REPLa, możesz musieć posprzątać <code>{...},]</code> → <code>{...}]</code> przed wklejeniem.</li>
  <li><strong>Pojedyncze cudzysłowy.</strong> <code>repr</code> Pythona używa pojedynczych. Przepuść przez <code>json.dumps</code>, albo użyj konwertera Python-literal do JSON.</li>
  <li><strong>System prompt Anthropica.</strong> Instrukcja system w API Anthropica to pole top-level, nie wiadomość. Jeśli twój dump ma tylko tablicę messages, system prompta tam nie ma — wklej jako <code>{"role": "system", "content": "..."}</code> na początku.</li>
  <li><strong>Argumenty tool-calli jako escapowany JSON.</strong> OpenAI zwraca <code>arguments</code> jako string JSON. Odescape'ujemy i ładnie drukujemy. Jeśli JSON w stringu jest zepsuty, pokazywany jest surowy string.</li>
  <li><strong>Prywatność.</strong> Nic nie opuszcza strony. Cały render leci w JS na wklejonym JSONie. Nie wklejaj nic, czego nie wkleiłbyś do appki notatek.</li>
</ul>
""",
        "ja": """
<h2>これは何のため？</h2>
<p>LLM アプリは会話を JSON のメッセージ配列としてログ化します — API に送られるのも、監査ログ・評価トレース・ファインチューニング用データセット・SDK のデバッグ出力に現れるのも、同じ形です。これを人間が直接読むのは辛い：エスケープされた文字列の壁、JSON in JSON でエスケープされたツール呼び出し引数、システムプロンプトが他のメッセージと混ざっている。このツールはそれをチャットバブルとして素早くレンダリングして、実際の会話を眺め、どのメッセージにツール呼び出しが含まれていたか確認し、おかしくなったプロンプトを特定できるようにします。</p>

<h3>対応フォーマット</h3>
<ul>
  <li><strong>OpenAI Chat Completions。</strong> <code>[{role, content}, ...]</code> 形式。assistant メッセージにはオプションで <code>tool_calls</code>、ツール結果は <code>role: "tool"</code>。最も一般的な形式です。</li>
  <li><strong>Anthropic Messages API。</strong> <code>[{role, content: [...]}]</code> で、<code>content</code> はブロック配列（<code>text</code>、<code>tool_use</code>、<code>tool_result</code>、<code>image</code>）。システムプロンプトは通常トップレベル — 表示したい場合は system メッセージとして貼り付けてください。</li>
  <li><strong>LangChain のメッセージダンプ。</strong> <code>[{type: "human" | "ai" | "system", content: ...}]</code> — 古めの LangChain 形式ですが、保存されたトレースでは今もよく使われます。</li>
  <li><strong>ラッパーオブジェクト。</strong> <code>{"messages": [...]}</code> や <code>{"input": [...]}</code> を貼り付けると、ラッパーは自動でアンラップされます。</li>
</ul>

<h3>表示内容</h3>
<ul>
  <li><strong>ロール別の色分けバブル。</strong> system = 中央寄せのグレー、user = 右寄せのインディゴ、assistant = 左寄せのニュートラル、tool result = グリーン。</li>
  <li><strong>ツール呼び出し。</strong> 既定で展開され、引数は整形表示。OpenAI の <code>tool_calls</code> と Anthropic の <code>tool_use</code> ブロックの両方に対応。ツール結果メッセージは別バブルで表示されます。</li>
  <li><strong>コードフェンスとインラインコード。</strong> トリプルバッククォートは <code>&lt;pre&gt;</code> 等幅でレンダリング、シングルバッククォートはインラインコード。シンタックスハイライトはありません（そのためのトークナイザを同梱していません）が、インデントは保持されます。</li>
  <li><strong>画像参照。</strong> Anthropic の image ブロックは、ソース URL またはメディアタイプを示す小さなピル状の UI で表示 — 画像自体は読み込みません（オフライン動作のため）。</li>
  <li><strong>統計行。</strong> 検出されたフォーマット、メッセージ数、ツール呼び出し数、Token Counter と同じヒューリスティックによる概算トークン数。</li>
</ul>

<h3>よくある落とし穴</h3>
<ul>
  <li><strong>末尾カンマ。</strong> 標準 JSON では許されません。デバッガや REPL の出力からコピーした場合は、貼り付け前に <code>{...},]</code> → <code>{...}]</code> を整える必要があるかもしれません。</li>
  <li><strong>シングルクォート。</strong> Python の <code>repr</code> はシングルクォートを使います。<code>json.dumps</code> を通すか、Python リテラル → JSON 変換ツールを使ってください。</li>
  <li><strong>Anthropic のシステムプロンプト。</strong> Anthropic API ではシステム指示はトップレベルのフィールドで、メッセージではありません。messages 配列だけのダンプにはシステムプロンプトが含まれないので、先頭に <code>{"role": "system", "content": "..."}</code> として貼り付けてください。</li>
  <li><strong>エスケープされた JSON のツール引数。</strong> OpenAI は <code>arguments</code> を JSON 文字列で返します。これをアンエスケープして整形します。文字列内 JSON が壊れている場合は生の文字列を表示します。</li>
  <li><strong>プライバシー。</strong> 何もページ外に出ません。レンダリングはすべて、貼り付けた JSON 上で JS が処理します。メモ帳に貼り付けたくないものは貼り付けないでください。</li>
</ul>
""",
        "nl": """
<h2>Waar is dit voor?</h2>
<p>LLM-apps loggen hun conversaties als JSON-arrays van messages — dat is wat naar de API gaat en wat je ziet in audit logs, evaluatie-traces, fine-tuning datasets en SDK debug-output. Die arrays met het blote oog lezen is verschrikkelijk: muren van geëscapete strings, tool-call argumenten verpakt in geëscapete JSON-in-JSON, system prompts vermengd met de rest. Deze tool geeft je een snelle chat-bubble render zodat je de echte conversatie kan scannen, ziet welke berichten tool-calls bevatten, en die ene prompt vindt die uit de bocht ging.</p>

<h3>Welke formats het begrijpt</h3>
<ul>
  <li><strong>OpenAI Chat Completions.</strong> <code>[{role, content}, ...]</code> met optionele <code>tool_calls</code> op assistant-berichten en <code>role: "tool"</code> voor tool-resultaten. De meest voorkomende vorm.</li>
  <li><strong>Anthropic Messages API.</strong> <code>[{role, content: [...]}]</code> waar <code>content</code> een array van blokken is (<code>text</code>, <code>tool_use</code>, <code>tool_result</code>, <code>image</code>). System prompt zit meestal top-level — plak hem als system-bericht als je hem wil zien.</li>
  <li><strong>LangChain message dumps.</strong> <code>[{type: "human" | "ai" | "system", content: ...}]</code> — oudere LangChain-vorm, nog steeds gangbaar in opgeslagen traces.</li>
  <li><strong>Wrapper-objecten.</strong> Als je <code>{"messages": [...]}</code> of <code>{"input": [...]}</code> plakt, wordt de wrapper automatisch uitgepakt.</li>
</ul>

<h3>Wat er gerenderd wordt</h3>
<ul>
  <li><strong>Rol-gekleurde bubbels.</strong> System = grijs gecentreerd, user = indigo rechts, assistant = neutraal links, tool result = groen.</li>
  <li><strong>Tool-calls.</strong> Standaard uitgeklapt met pretty-printed argumenten. Zowel OpenAI's <code>tool_calls</code> als Anthropic's <code>tool_use</code>-blokken worden afgehandeld. Tool-resultaat berichten verschijnen in een aparte bubbel.</li>
  <li><strong>Code fences en inline code.</strong> Triple-backtick blokken renderen als <code>&lt;pre&gt;</code> monospace, enkele backticks als inline code. Geen syntax highlighting (we leveren geen tokenizer daarvoor), indentatie blijft behouden.</li>
  <li><strong>Image-verwijzingen.</strong> Anthropic image-blokken tonen een klein pilletje met de bron-URL of media-type — we laden de image zelf niet (tool blijft offline).</li>
  <li><strong>Stats-regel.</strong> Gedetecteerd format, aantal berichten, aantal tool-calls en een ruwe token-schatting met dezelfde heuristiek als onze Token Counter.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Trailing comma's.</strong> Standaard-JSON staat ze niet toe. Als je vanuit een debugger of REPL-output kopieerde, moet je misschien <code>{...},]</code> → <code>{...}]</code> opschonen voor je plakt.</li>
  <li><strong>Enkele aanhalingstekens.</strong> Python's <code>repr</code> gebruikt enkele. Loop het door <code>json.dumps</code>, of gebruik een Python-literal-naar-JSON converter.</li>
  <li><strong>Anthropic system prompt.</strong> De system-instructie in Anthropic's API is een top-level veld, geen bericht. Als je dump alleen de messages-array bevat, zit de system prompt er niet in — plak hem als <code>{"role": "system", "content": "..."}</code> aan het begin.</li>
  <li><strong>Tool-call argumenten als geëscapete JSON.</strong> OpenAI retourneert <code>arguments</code> als een JSON-string. Wij unescapen en pretty-printen het. Als de JSON-in-string kapot is, wordt de rauwe string getoond.</li>
  <li><strong>Privacy.</strong> Niets verlaat de pagina. De hele render draait in JS op de JSON die je plakt. Plak niets wat je niet in een notitie-app zou plakken.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>LLM uygulamaları konuşmalarını JSON message dizileri olarak loglar — API'ye gönderilen şey budur ve audit log'larında, değerlendirme trace'lerinde, fine-tuning veri setlerinde ve SDK debug çıktısında gördüğün de budur. Bu dizileri çıplak gözle okumak işkencedir: escape'lenmiş string duvarları, escape'lenmiş JSON-içinde-JSON ile sarılmış tool-call argümanları, geri kalanla karışmış system prompt'lar. Bu araç sana hızlı bir baloncuk render'ı verir, böylece gerçek konuşmayı tarayabilir, hangi mesajlarda tool-call olduğunu görebilir ve raydan çıkan o tek prompt'u bulabilirsin.</p>

<h3>Hangi formatları anlar</h3>
<ul>
  <li><strong>OpenAI Chat Completions.</strong> <code>[{role, content}, ...]</code> formatı, assistant mesajlarında opsiyonel <code>tool_calls</code> ve tool sonuçları için <code>role: "tool"</code>. En yaygın biçim.</li>
  <li><strong>Anthropic Messages API.</strong> <code>[{role, content: [...]}]</code>, <code>content</code> blok dizisi (<code>text</code>, <code>tool_use</code>, <code>tool_result</code>, <code>image</code>). System prompt genelde top-level — görmek istiyorsan system mesajı olarak yapıştır.</li>
  <li><strong>LangChain mesaj dump'ları.</strong> <code>[{type: "human" | "ai" | "system", content: ...}]</code> — eski LangChain biçimi, kaydedilmiş trace'lerde hâlâ yaygın.</li>
  <li><strong>Wrapper nesneleri.</strong> <code>{"messages": [...]}</code> veya <code>{"input": [...]}</code> yapıştırırsan, wrapper otomatik açılır.</li>
</ul>

<h3>Ne render edilir</h3>
<ul>
  <li><strong>Role göre renkli baloncuklar.</strong> System = ortada gri, user = sağda indigo, assistant = solda nötr, tool result = yeşil.</li>
  <li><strong>Tool-call'lar.</strong> Varsayılan olarak açık, argümanlar formatlanmış. Hem OpenAI'nin <code>tool_calls</code> formu hem Anthropic'in <code>tool_use</code> blokları desteklenir. Tool sonuç mesajları kendi baloncuğunda görünür.</li>
  <li><strong>Code fence'ler ve inline kod.</strong> Üçlü backtick blokları <code>&lt;pre&gt;</code> monospace olarak render edilir, tekli backtick'ler inline kod olarak. Sözdizimi vurgulaması yok (onun için tokenizer taşımıyoruz), girinti korunur.</li>
  <li><strong>Görsel referansları.</strong> Anthropic görsel blokları, kaynak URL'sini veya media-type'ı gösteren küçük bir hap olarak render edilir — görseli aslında yüklemeyiz (araç offline kalır).</li>
  <li><strong>İstatistik satırı.</strong> Algılanan format, mesaj sayısı, tool-call sayısı ve Token Counter'ımızla aynı sezgisel yöntemi kullanan kaba bir token tahmini.</li>
</ul>

<h3>Yaygın tuzaklar</h3>
<ul>
  <li><strong>Sondaki virgüller.</strong> Standart JSON izin vermez. Debugger veya REPL çıktısından kopyaladıysan, yapıştırmadan önce <code>{...},]</code> → <code>{...}]</code> temizlemen gerekebilir.</li>
  <li><strong>Tek tırnaklar.</strong> Python'un <code>repr</code>'ı tek tırnak kullanır. <code>json.dumps</code>'tan geçir veya Python-literal'dan JSON'a dönüştürücü kullan.</li>
  <li><strong>Anthropic system prompt'u.</strong> Anthropic API'sinde system talimatı top-level alandır, mesaj değildir. Dump'ında sadece messages dizisi varsa, system prompt orada olmaz — başa <code>{"role": "system", "content": "..."}</code> olarak yapıştır.</li>
  <li><strong>Escape'lenmiş JSON olarak tool-call argümanları.</strong> OpenAI <code>arguments</code>'ı JSON string olarak döner. Biz unescape edip pretty-print ederiz. String içindeki JSON bozuksa, ham string gösterilir.</li>
  <li><strong>Gizlilik.</strong> Sayfadan hiçbir şey çıkmaz. Tüm render yapıştırdığın JSON üzerinde JS'de çalışır. Bir not uygulamasına yapıştırmayacağın hiçbir şeyi yapıştırma.</li>
</ul>
""",
        "id": """
<h2>Buat apa ini?</h2>
<p>App LLM mencatat percakapan mereka sebagai array JSON pesan — itu yang dikirim ke API dan yang kamu lihat di audit log, trace evaluasi, dataset fine-tuning, dan debug output SDK. Membaca array itu sebagai manusia menyiksa: dinding string yang di-escape, argumen tool-call dibungkus JSON-dalam-JSON yang di-escape, system prompt tercampur dengan sisanya. Tool ini memberimu render bubble cepat supaya kamu bisa scan percakapan sebenarnya, lihat pesan mana yang punya tool-call, dan temukan prompt yang melenceng.</p>

<h3>Format apa yang dipahami</h3>
<ul>
  <li><strong>OpenAI Chat Completions.</strong> <code>[{role, content}, ...]</code> dengan <code>tool_calls</code> opsional di pesan assistant dan <code>role: "tool"</code> untuk hasil tool. Bentuk paling umum.</li>
  <li><strong>Anthropic Messages API.</strong> <code>[{role, content: [...]}]</code> di mana <code>content</code> adalah array blok (<code>text</code>, <code>tool_use</code>, <code>tool_result</code>, <code>image</code>). System prompt biasanya top-level — tempel sebagai pesan system kalau mau lihat.</li>
  <li><strong>Dump pesan LangChain.</strong> <code>[{type: "human" | "ai" | "system", content: ...}]</code> — bentuk LangChain lama, masih umum di trace yang disimpan.</li>
  <li><strong>Objek wrapper.</strong> Kalau kamu tempel <code>{"messages": [...]}</code> atau <code>{"input": [...]}</code>, wrapper di-unwrap otomatis.</li>
</ul>

<h3>Apa yang dirender</h3>
<ul>
  <li><strong>Bubble berwarna sesuai role.</strong> System = abu di tengah, user = indigo kanan, assistant = netral kiri, tool result = hijau.</li>
  <li><strong>Tool-call.</strong> Diperluas default dengan argumen yang diformat rapi. Baik <code>tool_calls</code> OpenAI maupun blok <code>tool_use</code> Anthropic ditangani. Pesan hasil tool muncul di bubble sendiri.</li>
  <li><strong>Code fence dan inline code.</strong> Blok triple backtick jadi <code>&lt;pre&gt;</code> monospace, single backtick jadi inline. Tanpa syntax highlighting (kami nggak bawa tokenizer untuk itu), indentasi dipertahankan.</li>
  <li><strong>Referensi gambar.</strong> Blok image Anthropic menampilkan pill kecil dengan URL atau media-type — gambarnya tidak kami load (tool tetap offline).</li>
  <li><strong>Baris stats.</strong> Format yang terdeteksi, jumlah pesan, jumlah tool-call, dan estimasi token kasar dengan heuristik yang sama seperti Token Counter kami.</li>
</ul>

<h3>Jebakan umum</h3>
<ul>
  <li><strong>Koma akhir.</strong> JSON standar nggak mengizinkan. Kalau kamu copy dari debugger atau REPL, mungkin perlu bersihkan <code>{...},]</code> → <code>{...}]</code> sebelum tempel.</li>
  <li><strong>Single quote.</strong> <code>repr</code> Python pakai single quote. Lewatkan via <code>json.dumps</code>, atau pakai converter Python-literal ke JSON.</li>
  <li><strong>System prompt Anthropic.</strong> Instruksi system di API Anthropic adalah field top-level, bukan pesan. Kalau dump-mu cuma punya array messages, system prompt-nya nggak ada — tempel sebagai <code>{"role": "system", "content": "..."}</code> di awal.</li>
  <li><strong>Argumen tool-call sebagai JSON ter-escape.</strong> OpenAI mengembalikan <code>arguments</code> sebagai string JSON. Kami unescape dan pretty-print. Kalau JSON dalam string-nya rusak, string mentah ditampilkan.</li>
  <li><strong>Privasi.</strong> Tidak ada yang keluar dari halaman. Seluruh render jalan di JS pada JSON yang kamu tempel. Jangan tempel apa pun yang tidak akan kamu tempel ke app catatan.</li>
</ul>
""",
        "vi": """
<h2>Cái này để làm gì?</h2>
<p>Các app LLM ghi log hội thoại của chúng dưới dạng mảng JSON các message — đó là cái được gửi tới API và là cái bạn thấy trong audit log, evaluation trace, dataset fine-tuning và debug output của SDK. Đọc các mảng đó bằng mắt thường rất khổ: những bức tường string đã escape, tham số tool-call bọc trong JSON-trong-JSON đã escape, system prompt trộn lẫn với phần còn lại. Công cụ này cho bạn render bubble nhanh để bạn có thể quét cuộc hội thoại thực, xem message nào có tool-call, và tìm ra cái prompt đã chạy lệch.</p>

<h3>Hiểu những định dạng nào</h3>
<ul>
  <li><strong>OpenAI Chat Completions.</strong> <code>[{role, content}, ...]</code> với <code>tool_calls</code> tùy chọn trên message assistant và <code>role: "tool"</code> cho kết quả tool. Dạng phổ biến nhất.</li>
  <li><strong>Anthropic Messages API.</strong> <code>[{role, content: [...]}]</code> trong đó <code>content</code> là mảng các block (<code>text</code>, <code>tool_use</code>, <code>tool_result</code>, <code>image</code>). System prompt thường ở top-level — dán nó như message system nếu muốn thấy.</li>
  <li><strong>Dump message LangChain.</strong> <code>[{type: "human" | "ai" | "system", content: ...}]</code> — dạng LangChain cũ, vẫn phổ biến trong các trace đã lưu.</li>
  <li><strong>Object wrapper.</strong> Nếu bạn dán <code>{"messages": [...]}</code> hoặc <code>{"input": [...]}</code>, wrapper được unwrap tự động.</li>
</ul>

<h3>Cái gì được render</h3>
<ul>
  <li><strong>Bubble màu theo vai trò.</strong> System = xám giữa, user = chàm phải, assistant = trung tính trái, tool result = xanh lá.</li>
  <li><strong>Tool-call.</strong> Mở rộng mặc định với tham số được format đẹp. Cả <code>tool_calls</code> của OpenAI và block <code>tool_use</code> của Anthropic đều được xử lý. Message kết quả tool xuất hiện trong bubble riêng.</li>
  <li><strong>Code fence và inline code.</strong> Block triple backtick render thành <code>&lt;pre&gt;</code> monospace, single backtick thành inline code. Không syntax highlight (chúng tôi không mang tokenizer cho việc đó), indent được giữ.</li>
  <li><strong>Tham chiếu hình ảnh.</strong> Block image của Anthropic render thành pill nhỏ hiển thị URL hoặc media-type — chúng tôi không thực sự load image (giữ công cụ offline).</li>
  <li><strong>Dòng stats.</strong> Định dạng phát hiện, số message, số tool-call, và ước tính token thô bằng cùng heuristic như Token Counter của chúng tôi.</li>
</ul>

<h3>Bẫy thường gặp</h3>
<ul>
  <li><strong>Dấu phẩy cuối.</strong> JSON chuẩn không cho phép. Nếu bạn copy từ debugger hoặc REPL, có thể cần làm sạch <code>{...},]</code> → <code>{...}]</code> trước khi dán.</li>
  <li><strong>Dấu nháy đơn.</strong> <code>repr</code> của Python dùng nháy đơn. Cho qua <code>json.dumps</code>, hoặc dùng converter Python-literal sang JSON.</li>
  <li><strong>System prompt Anthropic.</strong> Lệnh system trong API Anthropic là field top-level, không phải message. Nếu dump của bạn chỉ có mảng messages, system prompt sẽ không có ở đó — dán nó như <code>{"role": "system", "content": "..."}</code> ở đầu.</li>
  <li><strong>Tham số tool-call dưới dạng JSON đã escape.</strong> OpenAI trả về <code>arguments</code> dưới dạng string JSON. Chúng tôi unescape và format đẹp. Nếu JSON trong string bị hỏng, hiển thị string thô.</li>
  <li><strong>Quyền riêng tư.</strong> Không gì rời khỏi trang. Toàn bộ render chạy trong JS trên JSON bạn dán. Đừng dán bất cứ gì bạn không dán vào app ghi chú.</li>
</ul>
""",
        "hi": """
<h2>यह किसके लिए है?</h2>
<p>LLM applications अपनी conversations को JSON arrays of messages के रूप में log करती हैं — यही API को भेजा जाता है और यही audit logs, evaluation traces, fine-tuning datasets, और SDK debug output में दिखता है। उन arrays को इंसान की तरह पढ़ना मुश्किल है: escaped strings की दीवारें, escaped JSON-में-JSON में लिपटे tool-call arguments, बाकी flow में मिले-जुले system prompts। यह tool आपको एक quick chat-bubble render देता है ताकि आप actual conversation को scan कर सकें, देख सकें कि किन messages में tool calls थे, और वो एक prompt पहचान सकें जो गलत हो गया।</p>

<h3>यह कौन-से formats समझता है</h3>
<ul>
  <li><strong>OpenAI Chat Completions।</strong> <code>[{role, content}, ...]</code> with optional <code>tool_calls</code> on assistant messages and <code>role: "tool"</code> for tool results। सबसे common shape।</li>
  <li><strong>Anthropic Messages API।</strong> <code>[{role, content: [...]}]</code> जहाँ <code>content</code> blocks का array है (<code>text</code>, <code>tool_use</code>, <code>tool_result</code>, <code>image</code>)। System prompt usually top-level होता है — अगर देखना है तो उसे system message के रूप में paste करें।</li>
  <li><strong>LangChain message dumps।</strong> <code>[{type: "human" | "ai" | "system", content: ...}]</code> — पुरानी LangChain shape, अब भी saved traces में common।</li>
  <li><strong>Wrapper objects।</strong> अगर आप <code>{"messages": [...]}</code> या <code>{"input": [...]}</code> paste करते हैं, तो wrapper automatically unwrap हो जाता है।</li>
</ul>

<h3>क्या render होता है</h3>
<ul>
  <li><strong>Role-colored bubbles।</strong> System = grey centered, user = indigo right-aligned, assistant = neutral left-aligned, tool result = green।</li>
  <li><strong>Tool calls।</strong> Default में expand के साथ pretty-printed arguments। OpenAI के <code>tool_calls</code> form और Anthropic के <code>tool_use</code> block दोनों handle होते हैं। Tool result messages अलग bubble में दिखते हैं।</li>
  <li><strong>Code fences और inline code।</strong> Triple-backtick blocks <code>&lt;pre&gt;</code> as monospace render होते हैं, single-backtick spans inline code। कोई syntax highlighting नहीं (हम उसके लिए tokenizer नहीं भेजते), indentation preserve होती है।</li>
  <li><strong>Image references।</strong> Anthropic image blocks एक छोटी pill के रूप में source URL या media type दिखाते हैं — हम image actually load नहीं करते (tool offline रहती है)।</li>
  <li><strong>Stats line।</strong> Detected format, message count, tool-call count, और हमारे Token Counter जैसी heuristic से rough token estimate।</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Trailing commas।</strong> Standard JSON इन्हें allow नहीं करता। अगर आपने debugger या REPL output से copy किया है, तो paste से पहले <code>{...},]</code> → <code>{...}]</code> साफ करना पड़ सकता है।</li>
  <li><strong>Single quotes।</strong> Python का <code>repr</code> single quotes use करता है। <code>json.dumps</code> से चलाएं, या Python-literal-to-JSON converter use करें।</li>
  <li><strong>Anthropic system prompt।</strong> Anthropic API में system instruction top-level field है, message नहीं। अगर आपके dump में सिर्फ messages array है, तो system prompt वहां नहीं होगा — start में <code>{"role": "system", "content": "..."}</code> के रूप में paste करें।</li>
  <li><strong>Escaped JSON के रूप में tool-call arguments।</strong> OpenAI <code>arguments</code> को JSON string के रूप में return करता है। हम unescape करके pretty-print करते हैं। अगर JSON-in-string malformed है, तो raw string दिखाई जाती है।</li>
  <li><strong>Privacy।</strong> कुछ भी page से बाहर नहीं जाता। पूरी render आपके paste किए JSON पर JS में चलती है। कुछ ऐसा paste न करें जो किसी notepad app में paste न करें।</li>
</ul>
""",
        "sk": """
<h2>Načo to slúži?</h2>
<p>LLM aplikácie logujú konverzácie ako JSON polia správ — to sa posiela do API a to vidíš v audit logoch, evaluation traceoch, dataseteh na fine-tuning a debug výstupe SDK. Čítať tie polia ako človek je trápenie: steny escapovaných stringov, argumenty tool-callov zabalené v escapovanom JSON-v-JSONe, system prompty pomiešané so zvyškom. Tento nástroj ti dá rýchly render do bublín, aby si prešiel skutočnú konverzáciu, videl ktoré správy obsahovali tool-cally a našiel ten jeden prompt, ktorý sa pokašľal.</p>

<h3>Aké formáty rozumie</h3>
<ul>
  <li><strong>OpenAI Chat Completions.</strong> <code>[{role, content}, ...]</code> s voliteľnými <code>tool_calls</code> na správach assistanta a <code>role: "tool"</code> pre výsledky tool. Najbežnejšia forma.</li>
  <li><strong>Anthropic Messages API.</strong> <code>[{role, content: [...]}]</code> kde <code>content</code> je pole blokov (<code>text</code>, <code>tool_use</code>, <code>tool_result</code>, <code>image</code>). System prompt je zvyčajne top-level — vlož ho ako system správu, ak ho chceš vidieť.</li>
  <li><strong>Dumpy správ LangChain.</strong> <code>[{type: "human" | "ai" | "system", content: ...}]</code> — staršia LangChain forma, stále bežná v uložených trace-och.</li>
  <li><strong>Wrapper objekty.</strong> Ak vložíš <code>{"messages": [...]}</code> alebo <code>{"input": [...]}</code>, wrapper sa automaticky rozbalí.</li>
</ul>

<h3>Čo sa renderuje</h3>
<ul>
  <li><strong>Bubliny farebné podľa roly.</strong> System = sivá v strede, user = indigo vpravo, assistant = neutrálny vľavo, tool result = zelená.</li>
  <li><strong>Tool-cally.</strong> V predvolenom stave rozbalené s pekne formátovanými argumentmi. <code>tool_calls</code> z OpenAI aj bloky <code>tool_use</code> z Anthropicu sú riešené. Správy s výsledkom toolu sa zobrazia ako vlastná bublina.</li>
  <li><strong>Code fence a inline code.</strong> Bloky troch backtickov sa renderujú ako <code>&lt;pre&gt;</code> v monospace, jednotlivé backticky ako inline code. Bez syntax highlight (na to nevozíme tokenizer), odsadenie zachované.</li>
  <li><strong>Odkazy na obrázky.</strong> Image bloky Anthropicu sa zobrazia ako malá pilulka so source URL alebo media-type — obrázok reálne nenahrávame (nástroj zostáva offline).</li>
  <li><strong>Stats riadok.</strong> Zistený formát, počet správ, počet tool-callov a hrubý odhad tokenov rovnakou heuristikou ako Token Counter.</li>
</ul>

<h3>Časté pasce</h3>
<ul>
  <li><strong>Čiarky na konci.</strong> Štandardné JSON ich nedovolí. Ak si kopíroval z debuggera alebo REPL výstupu, možno musíš pred vložením vyčistiť <code>{...},]</code> → <code>{...}]</code>.</li>
  <li><strong>Jednoduché úvodzovky.</strong> Pythonov <code>repr</code> používa jednoduché. Prežeň to cez <code>json.dumps</code>, alebo použi konvertor Python-literal na JSON.</li>
  <li><strong>System prompt Anthropicu.</strong> System inštrukcia v API Anthropicu je top-level pole, nie správa. Ak má tvoj dump len pole messages, system prompt tam nebude — vlož ho ako <code>{"role": "system", "content": "..."}</code> na začiatok.</li>
  <li><strong>Argumenty tool-callov ako escapovaný JSON.</strong> OpenAI vracia <code>arguments</code> ako JSON string. My de-escape-ujeme a pekne tlačíme. Ak je JSON v stringu pokazený, ukáže sa surový string.</li>
  <li><strong>Súkromie.</strong> Nič neopustí stránku. Celý render beží v JS nad JSONom, ktorý vložíš. Nevkladaj nič, čo by si nevložil do notepad appky.</li>
</ul>
""",
        "cs": """
<h2>K čemu to slouží?</h2>
<p>LLM aplikace logují konverzace jako JSON pole zpráv — to se posílá do API a to vidíš v audit lozích, evaluation traceech, datasetech na fine-tuning a debug výstupu SDK. Číst ta pole jako člověk je utrpení: zdi escapovaných stringů, argumenty tool-callů zabalené v escapovaném JSON-v-JSONu, system prompty pomíchané se zbytkem. Tenhle nástroj ti dá rychlý render do bublin, abys prošel skutečnou konverzaci, viděl které zprávy obsahovaly tool-cally a našel ten jeden prompt, který se zvrhl.</p>

<h3>Jaké formáty rozumí</h3>
<ul>
  <li><strong>OpenAI Chat Completions.</strong> <code>[{role, content}, ...]</code> s volitelnými <code>tool_calls</code> na zprávách assistanta a <code>role: "tool"</code> pro výsledky tool. Nejběžnější forma.</li>
  <li><strong>Anthropic Messages API.</strong> <code>[{role, content: [...]}]</code> kde <code>content</code> je pole bloků (<code>text</code>, <code>tool_use</code>, <code>tool_result</code>, <code>image</code>). System prompt je obvykle top-level — vlož ho jako system zprávu, jestli ho chceš vidět.</li>
  <li><strong>Dumpy zpráv LangChain.</strong> <code>[{type: "human" | "ai" | "system", content: ...}]</code> — starší LangChain forma, pořád běžná v uložených trace-ech.</li>
  <li><strong>Wrapper objekty.</strong> Pokud vložíš <code>{"messages": [...]}</code> nebo <code>{"input": [...]}</code>, wrapper se automaticky rozbalí.</li>
</ul>

<h3>Co se renderuje</h3>
<ul>
  <li><strong>Bubliny barevné podle role.</strong> System = šedá uprostřed, user = indigo vpravo, assistant = neutrální vlevo, tool result = zelená.</li>
  <li><strong>Tool-cally.</strong> Ve výchozím stavu rozbalené s hezky formátovanými argumenty. <code>tool_calls</code> z OpenAI i bloky <code>tool_use</code> z Anthropicu jsou řešeny. Zprávy s výsledkem toolu se zobrazí jako vlastní bublina.</li>
  <li><strong>Code fence a inline code.</strong> Bloky tří backticků se renderují jako <code>&lt;pre&gt;</code> v monospace, jednotlivé backticky jako inline code. Bez syntax highlight (na to nevozíme tokenizer), odsazení zachováno.</li>
  <li><strong>Odkazy na obrázky.</strong> Image bloky Anthropicu se zobrazí jako malá pilulka se source URL nebo media-type — obrázek reálně nenahráváme (nástroj zůstává offline).</li>
  <li><strong>Stats řádek.</strong> Zjištěný formát, počet zpráv, počet tool-callů a hrubý odhad tokenů stejnou heuristikou jako Token Counter.</li>
</ul>

<h3>Časté pasti</h3>
<ul>
  <li><strong>Čárky na konci.</strong> Standardní JSON je nepovoluje. Pokud jsi kopíroval z debuggeru nebo REPL výstupu, možná musíš před vložením vyčistit <code>{...},]</code> → <code>{...}]</code>.</li>
  <li><strong>Jednoduché uvozovky.</strong> Pythonův <code>repr</code> používá jednoduché. Prožeň to přes <code>json.dumps</code>, nebo použij konvertor Python-literal na JSON.</li>
  <li><strong>System prompt Anthropicu.</strong> System instrukce v API Anthropicu je top-level pole, ne zpráva. Pokud má tvůj dump jen pole messages, system prompt tam nebude — vlož ho jako <code>{"role": "system", "content": "..."}</code> na začátek.</li>
  <li><strong>Argumenty tool-callů jako escapovaný JSON.</strong> OpenAI vrací <code>arguments</code> jako JSON string. My de-escape-ujeme a hezky tiskneme. Pokud je JSON ve stringu rozbitý, ukáže se surový string.</li>
  <li><strong>Soukromí.</strong> Nic neopustí stránku. Celý render běží v JS nad JSONem, který vložíš. Nevkládej nic, co bys nevložil do notepad appky.</li>
</ul>
""",
    },
    "related": ["jsonl-viewer", "token-counter", "system-prompt-linter"],
    "howto": {"flow": "transform", "action": "format", "noun": "messages"},
}
