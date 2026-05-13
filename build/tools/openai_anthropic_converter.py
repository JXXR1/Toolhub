TOOL = {
    "slug": "openai-anthropic-converter",
    "category": "ai",
    "icon": "🔁",
    "tags": ["openai", "anthropic", "claude", "converter", "messages", "api", "format", "tool-calling"],
    "i18n": {
        "en": {
            "name": "OpenAI ⇄ Anthropic Converter",
            "tagline": "Convert message arrays between OpenAI Chat Completions and Anthropic Messages API formats. Handles system messages, tool calls, image content blocks, multi-turn. In-browser, no API keys.",
            "description": "Free in-browser converter between OpenAI Chat Completions and Anthropic Messages API formats. Handles the major format diffs: system message placement (top-level field for Anthropic, role:'system' for OpenAI), tool-call format (tool_calls/tool_call_id vs tool_use/tool_result), image content blocks, multi-turn structure. Useful when migrating prompts between providers. Pure JS.",
        },
        "de": {
            "name": "OpenAI ⇄ Anthropic Konverter",
            "tagline": "Konvertiere Messages-Arrays zwischen OpenAI Chat Completions und Anthropic Messages API. Handhabt System-Messages, Tool-Calls, Image-Blocks, Multi-Turn. Im Browser, keine API-Keys.",
            "description": "Kostenloser Browser-Konverter zwischen OpenAI Chat Completions und Anthropic Messages API. Deckt die wichtigsten Format-Unterschiede ab: Platzierung der System-Message (Top-Level bei Anthropic, role:'system' bei OpenAI), Tool-Call-Format (tool_calls/tool_call_id vs tool_use/tool_result), Image-Content-Blöcke, Multi-Turn-Struktur. Nützlich beim Migrieren von Prompts zwischen Providern. Reines JS.",
        },
        "es": {
            "name": "Convertidor OpenAI ⇄ Anthropic",
            "tagline": "Convierte arrays de messages entre OpenAI Chat Completions y Anthropic Messages API. Maneja system messages, tool calls, bloques de imagen, multi-turno. En el navegador, sin API keys.",
            "description": "Convertidor gratuito en el navegador entre OpenAI Chat Completions y Anthropic Messages API. Cubre las diferencias principales: ubicación del system message (campo top-level en Anthropic, role:'system' en OpenAI), formato de tool-calls (tool_calls/tool_call_id vs tool_use/tool_result), bloques de imagen, estructura multi-turno. Útil al migrar prompts entre proveedores. JS puro.",
        },
        "fr": {
            "name": "Convertisseur OpenAI ⇄ Anthropic",
            "tagline": "Convertissez des tableaux de messages entre OpenAI Chat Completions et Anthropic Messages API. Gère les system messages, tool calls, blocs d'image, multi-tour. Dans le navigateur, sans API keys.",
            "description": "Convertisseur gratuit dans le navigateur entre OpenAI Chat Completions et Anthropic Messages API. Couvre les principales différences de format : placement du system message (champ top-level pour Anthropic, role:'system' pour OpenAI), format des tool-calls (tool_calls/tool_call_id vs tool_use/tool_result), blocs de contenu image, structure multi-tour. Utile lors de la migration de prompts entre fournisseurs. JS pur.",
        },
        "it": {
            "name": "Convertitore OpenAI ⇄ Anthropic",
            "tagline": "Converti array di messages tra OpenAI Chat Completions e Anthropic Messages API. Gestisce system message, tool call, blocchi immagine, multi-turno. Nel browser, senza API key.",
            "description": "Convertitore gratuito nel browser tra OpenAI Chat Completions e Anthropic Messages API. Copre le principali differenze di formato: posizione del system message (campo top-level su Anthropic, role:'system' su OpenAI), formato dei tool-call (tool_calls/tool_call_id vs tool_use/tool_result), blocchi di contenuto immagine, struttura multi-turno. Utile quando si migrano prompt tra provider. JS puro.",
        },
        "pt": {
            "name": "Conversor OpenAI ⇄ Anthropic",
            "tagline": "Converte arrays de messages entre OpenAI Chat Completions e Anthropic Messages API. Trata system messages, tool calls, blocos de imagem, multi-turno. No navegador, sem API keys.",
            "description": "Conversor grátis no navegador entre OpenAI Chat Completions e Anthropic Messages API. Cobre as principais diferenças de formato: posicionamento do system message (campo top-level na Anthropic, role:'system' na OpenAI), formato de tool-calls (tool_calls/tool_call_id vs tool_use/tool_result), blocos de conteúdo de imagem, estrutura multi-turno. Útil ao migrar prompts entre provedores. JS puro.",
        },
        "pl": {
            "name": "Konwerter OpenAI ⇄ Anthropic",
            "tagline": "Konwertuj tablice messages między OpenAI Chat Completions a Anthropic Messages API. Obsługuje system messages, tool calle, bloki obrazków, multi-turn. W przeglądarce, bez API keys.",
            "description": "Darmowy konwerter w przeglądarce między OpenAI Chat Completions a Anthropic Messages API. Pokrywa główne różnice formatów: umiejscowienie system message (pole top-level u Anthropica, role:'system' u OpenAI), format tool-calli (tool_calls/tool_call_id vs tool_use/tool_result), bloki contentu obrazków, strukturę multi-turn. Przydatne przy migracji promptów między providerami. Czysty JS.",
        },
        "ja": {
            "name": "OpenAI ⇄ Anthropic コンバーター",
            "tagline": "メッセージ配列を OpenAI Chat Completions と Anthropic Messages API のあいだで相互変換。system メッセージ・ツール呼び出し・画像ブロック・マルチターンに対応。ブラウザ完結、API キー不要。",
            "description": "OpenAI Chat Completions と Anthropic Messages API のあいだを変換する、ブラウザ完結の無料コンバーター（API キー不要）。主要なフォーマット差を扱います：system メッセージの位置（Anthropic ではトップレベルフィールド、OpenAI では role:'system'）、ツール呼び出しの形式（tool_calls/tool_call_id ⇄ tool_use/tool_result）、画像コンテンツブロック、マルチターン構造。プロバイダ間でプロンプトを移行するときに便利。純粋な JS で動作します。",
        },
        "nl": {
            "name": "OpenAI ⇄ Anthropic Converter",
            "tagline": "Converteer messages-arrays tussen OpenAI Chat Completions en Anthropic Messages API. Behandelt system messages, tool calls, image-blokken, multi-turn. In de browser, geen API keys.",
            "description": "Gratis in-browser converter tussen OpenAI Chat Completions en Anthropic Messages API. Behandelt de belangrijkste format-verschillen: plaatsing van het system message (top-level veld bij Anthropic, role:'system' bij OpenAI), tool-call format (tool_calls/tool_call_id vs tool_use/tool_result), image-content blokken, multi-turn structuur. Handig bij het migreren van prompts tussen providers. Pure JS.",
        },
        "tr": {
            "name": "OpenAI ⇄ Anthropic Dönüştürücü",
            "tagline": "Mesaj dizilerini OpenAI Chat Completions ile Anthropic Messages API arasında dönüştür. System mesajları, tool call'lar, görsel blokları, multi-turn'ü işler. Tarayıcıda, API anahtarı yok.",
            "description": "OpenAI Chat Completions ile Anthropic Messages API arasındaki ücretsiz tarayıcı içi dönüştürücü. Ana format farklarını ele alır: system mesaj yerleşimi (Anthropic için top-level alan, OpenAI için role:'system'), tool-call formatı (tool_calls/tool_call_id vs tool_use/tool_result), görsel content blokları, multi-turn yapı. Prompt'ları sağlayıcılar arasında taşırken yararlı. Saf JS.",
        },
        "id": {
            "name": "Konverter OpenAI ⇄ Anthropic",
            "tagline": "Konversi array messages antara OpenAI Chat Completions dan Anthropic Messages API. Menangani system messages, tool calls, blok gambar, multi-turn. Di browser, tanpa API keys.",
            "description": "Konverter gratis di browser antara OpenAI Chat Completions dan Anthropic Messages API. Menangani perbedaan format utama: penempatan system message (field top-level di Anthropic, role:'system' di OpenAI), format tool-call (tool_calls/tool_call_id vs tool_use/tool_result), blok konten gambar, struktur multi-turn. Berguna saat memigrasi prompt antar provider. JS murni.",
        },
        "vi": {
            "name": "Bộ chuyển đổi OpenAI ⇄ Anthropic",
            "tagline": "Chuyển đổi mảng messages giữa OpenAI Chat Completions và Anthropic Messages API. Xử lý system messages, tool calls, khối hình ảnh, multi-turn. Trong trình duyệt, không cần API key.",
            "description": "Bộ chuyển đổi miễn phí trong trình duyệt giữa OpenAI Chat Completions và Anthropic Messages API. Xử lý các khác biệt định dạng chính: vị trí system message (field top-level cho Anthropic, role:'system' cho OpenAI), định dạng tool-call (tool_calls/tool_call_id vs tool_use/tool_result), khối content hình ảnh, cấu trúc multi-turn. Hữu ích khi di chuyển prompt giữa các nhà cung cấp. JS thuần.",
        },
        "hi": {
            "name": "OpenAI ⇄ Anthropic Converter",
            "tagline": "OpenAI Chat Completions और Anthropic Messages API formats के बीच message arrays convert करें। System messages, tool calls, image content blocks, multi-turn handle करता है। In-browser, कोई API keys नहीं।",
            "description": "OpenAI Chat Completions और Anthropic Messages API formats के बीच मुफ़्त in-browser converter। मुख्य format differences को handle करता है: system message placement (Anthropic के लिए top-level field, OpenAI के लिए role:'system'), tool-call format (tool_calls/tool_call_id vs tool_use/tool_result), image content blocks, multi-turn structure। Providers के बीच prompts migrate करते समय उपयोगी। Pure JS।",
        },
        "sk": {
            "name": "Konvertor OpenAI ⇄ Anthropic",
            "tagline": "Konvertuj polia messages medzi OpenAI Chat Completions a Anthropic Messages API. Rieši system správy, tool cally, image bloky, multi-turn. V prehliadači, žiadne API kľúče.",
            "description": "Bezplatný konvertor v prehliadači medzi OpenAI Chat Completions a Anthropic Messages API. Rieši hlavné rozdiely formátov: umiestnenie system správy (top-level pole pri Anthropicu, role:'system' pri OpenAI), formát tool-callov (tool_calls/tool_call_id vs tool_use/tool_result), bloky obrazového obsahu, multi-turn štruktúru. Užitočné pri migrácii promptov medzi providermi. Čisté JS.",
        },
        "cs": {
            "name": "Konvertor OpenAI ⇄ Anthropic",
            "tagline": "Konvertuj pole messages mezi OpenAI Chat Completions a Anthropic Messages API. Řeší system zprávy, tool cally, image bloky, multi-turn. V prohlížeči, žádné API klíče.",
            "description": "Bezplatný konvertor v prohlížeči mezi OpenAI Chat Completions a Anthropic Messages API. Řeší hlavní rozdíly formátů: umístění system zprávy (top-level pole u Anthropicu, role:'system' u OpenAI), formát tool-callů (tool_calls/tool_call_id vs tool_use/tool_result), bloky obrazového obsahu, multi-turn strukturu. Užitečné při migraci promptů mezi providery. Čisté JS.",
        },
    },
    "body": """
<div class="tool-card">
  <div class="oac-dir">
    <label style="display:inline-flex;align-items:center;gap:0.4rem;cursor:pointer">
      <input type="radio" name="oac-dir" value="o2a" checked onchange="oacConvert()"> OpenAI → Anthropic
    </label>
    <label style="display:inline-flex;align-items:center;gap:0.4rem;cursor:pointer">
      <input type="radio" name="oac-dir" value="a2o" onchange="oacConvert()"> Anthropic → OpenAI
    </label>
    <button class="secondary" onclick="oacSwap()">⇅ Swap direction</button>
  </div>
</div>
<div class="tool-card oac-pair">
  <div class="oac-col">
    <label for="oac-input" id="oac-input-label">Source (OpenAI Chat Completions)</label>
    <textarea id="oac-input" oninput="oacConvert()" spellcheck="false" placeholder='[{"role":"system","content":"You are helpful."},{"role":"user","content":"Hi"}]'>[
  {"role": "system", "content": "You are a helpful weather assistant."},
  {"role": "user", "content": "What is the weather in Paris?"},
  {"role": "assistant", "content": null, "tool_calls": [
    {"id": "call_1", "type": "function", "function": {"name": "get_weather", "arguments": "{\\"city\\": \\"Paris\\"}"}}
  ]},
  {"role": "tool", "tool_call_id": "call_1", "content": "{\\"temp_c\\": 14, \\"condition\\": \\"cloudy\\"}"},
  {"role": "assistant", "content": "It's currently 14°C and cloudy in Paris."}
]</textarea>
  </div>
  <div class="oac-col">
    <div style="display:flex;justify-content:space-between;align-items:center">
      <label id="oac-output-label">Target (Anthropic Messages API)</label>
      <button class="secondary" id="oac-copy" onclick="oacCopy(this)">{LBL_COPY}</button>
    </div>
    <textarea id="oac-output" readonly spellcheck="false"></textarea>
  </div>
</div>
<div class="meta" id="oac-stats" style="margin-top:0.5rem"></div>
""",
    "script": """
<style>
.oac-dir{display:flex;gap:1rem;align-items:center;flex-wrap:wrap}
.oac-pair{display:grid;grid-template-columns:1fr 1fr;gap:1rem}
.oac-col{display:flex;flex-direction:column;gap:0.35rem}
.oac-col textarea{min-height:340px;font-family:ui-monospace,monospace;font-size:0.85rem}
.oac-err{color:#ef4444;font-weight:600}
.oac-warn{color:#f59e0b}
.oac-ok{color:#22c55e}
@media (max-width:780px){
  .oac-pair{grid-template-columns:1fr}
}
</style>
<script>
function oacDir(){
  const r = document.querySelector('input[name="oac-dir"]:checked');
  return r ? r.value : 'o2a';
}
function oacOpenaiToAnthropic(msgs){
  // Extract system into top-level, transform the rest.
  let systemText = '';
  const out = [];
  // First pass: merge stray adjacent "tool" messages into a single user tool_result content array
  for (let i = 0; i < msgs.length; i++){
    const m = msgs[i];
    if (!m || typeof m !== 'object') continue;
    if (m.role === 'system'){
      // Concatenate; Anthropic allows a single system string
      const t = typeof m.content === 'string' ? m.content : (Array.isArray(m.content) ? m.content.map(c => c && c.text ? c.text : '').join('\\n') : String(m.content ?? ''));
      systemText = systemText ? systemText + '\\n\\n' + t : t;
      continue;
    }
    if (m.role === 'tool'){
      // Becomes user.content[].tool_result. Coalesce consecutive tool messages.
      const block = { type: 'tool_result', tool_use_id: m.tool_call_id || '', content: m.content == null ? '' : m.content };
      const prev = out[out.length - 1];
      if (prev && prev.role === 'user' && Array.isArray(prev.content) && prev._fromTool){
        prev.content.push(block);
      } else {
        out.push({ role: 'user', content: [block], _fromTool: true });
      }
      continue;
    }
    if (m.role === 'assistant'){
      const blocks = [];
      // text content (may be null when only tool_calls are present)
      if (typeof m.content === 'string' && m.content){
        blocks.push({ type: 'text', text: m.content });
      } else if (Array.isArray(m.content)){
        for (const c of m.content){
          if (typeof c === 'string') blocks.push({ type: 'text', text: c });
          else if (c && c.type === 'text') blocks.push({ type: 'text', text: c.text || '' });
          else if (c) blocks.push(c);
        }
      }
      if (Array.isArray(m.tool_calls)){
        for (const tc of m.tool_calls){
          let input = {};
          const args = tc.function && tc.function.arguments;
          if (typeof args === 'string'){
            try { input = JSON.parse(args); } catch(_) { input = { _raw: args }; }
          } else if (args && typeof args === 'object'){
            input = args;
          }
          blocks.push({ type: 'tool_use', id: tc.id || '', name: (tc.function && tc.function.name) || tc.name || '', input });
        }
      }
      out.push({ role: 'assistant', content: blocks.length ? blocks : '' });
      continue;
    }
    if (m.role === 'user'){
      if (typeof m.content === 'string'){
        out.push({ role: 'user', content: m.content });
      } else if (Array.isArray(m.content)){
        const blocks = [];
        for (const c of m.content){
          if (typeof c === 'string'){ blocks.push({ type: 'text', text: c }); continue; }
          if (!c || typeof c !== 'object'){ continue; }
          if (c.type === 'text'){ blocks.push({ type: 'text', text: c.text || '' }); continue; }
          if (c.type === 'image_url'){
            const url = c.image_url && c.image_url.url || '';
            if (url.startsWith('data:')){
              const mm = url.match(/^data:([^;]+);base64,(.*)$/);
              if (mm){
                blocks.push({ type: 'image', source: { type: 'base64', media_type: mm[1], data: mm[2] } });
              } else {
                blocks.push({ type: 'image', source: { type: 'url', url } });
              }
            } else if (url){
              blocks.push({ type: 'image', source: { type: 'url', url } });
            }
            continue;
          }
          blocks.push(c);
        }
        out.push({ role: 'user', content: blocks });
      } else {
        out.push({ role: 'user', content: m.content == null ? '' : String(m.content) });
      }
      continue;
    }
    // Unknown role — pass through
    out.push(m);
  }
  // Strip our internal marker
  out.forEach(m => { if (m._fromTool) delete m._fromTool; });
  return { system: systemText, messages: out };
}
function oacAnthropicToOpenai(payload){
  // payload is either {system, messages} or [messages…]
  let system = '';
  let msgs;
  if (Array.isArray(payload)){
    msgs = payload;
  } else if (payload && Array.isArray(payload.messages)){
    msgs = payload.messages;
    if (typeof payload.system === 'string') system = payload.system;
    else if (Array.isArray(payload.system)) system = payload.system.map(b => b && b.text ? b.text : '').join('\\n');
  } else {
    throw new Error('Expected an array of messages or an object {system, messages}.');
  }
  const out = [];
  if (system) out.push({ role: 'system', content: system });
  for (const m of msgs){
    if (!m || typeof m !== 'object') continue;
    if (m.role === 'assistant'){
      let text = '';
      const toolCalls = [];
      if (typeof m.content === 'string'){
        text = m.content;
      } else if (Array.isArray(m.content)){
        for (const block of m.content){
          if (!block || typeof block !== 'object'){ if (typeof block === 'string') text += block; continue; }
          if (block.type === 'text') text += (text ? '' : '') + (block.text || '');
          else if (block.type === 'tool_use'){
            toolCalls.push({
              id: block.id || '',
              type: 'function',
              function: { name: block.name || '', arguments: JSON.stringify(block.input ?? {}) }
            });
          }
        }
      }
      const o = { role: 'assistant', content: text || null };
      if (toolCalls.length) o.tool_calls = toolCalls;
      out.push(o);
      continue;
    }
    if (m.role === 'user'){
      // Could contain tool_result blocks — those become role:'tool' messages in OpenAI
      if (Array.isArray(m.content)){
        const textParts = [];
        const imageParts = [];
        for (const block of m.content){
          if (!block || typeof block !== 'object'){ if (typeof block === 'string') textParts.push(block); continue; }
          if (block.type === 'text') textParts.push(block.text || '');
          else if (block.type === 'tool_result'){
            const content = typeof block.content === 'string' ? block.content : JSON.stringify(block.content ?? '');
            out.push({ role: 'tool', tool_call_id: block.tool_use_id || '', content });
          } else if (block.type === 'image'){
            const src = block.source || {};
            let url = '';
            if (src.type === 'base64') url = 'data:' + (src.media_type || 'image/png') + ';base64,' + (src.data || '');
            else if (src.type === 'url') url = src.url || '';
            else if (src.url) url = src.url;
            if (url) imageParts.push({ type: 'image_url', image_url: { url } });
          }
        }
        if (textParts.length || imageParts.length){
          if (imageParts.length){
            const blocks = [];
            if (textParts.length) blocks.push({ type: 'text', text: textParts.join('\\n') });
            blocks.push(...imageParts);
            out.push({ role: 'user', content: blocks });
          } else {
            out.push({ role: 'user', content: textParts.join('\\n') });
          }
        }
      } else if (typeof m.content === 'string'){
        out.push({ role: 'user', content: m.content });
      }
      continue;
    }
    if (m.role === 'system'){
      // System message inside the array (unusual for Anthropic but harmless)
      out.push({ role: 'system', content: typeof m.content === 'string' ? m.content : JSON.stringify(m.content) });
      continue;
    }
    out.push(m);
  }
  return out;
}
function oacUpdateLabels(){
  const dir = oacDir();
  const inLbl = document.getElementById('oac-input-label');
  const outLbl = document.getElementById('oac-output-label');
  if (dir === 'o2a'){
    inLbl.textContent = 'Source (OpenAI Chat Completions)';
    outLbl.textContent = 'Target (Anthropic Messages API)';
  } else {
    inLbl.textContent = 'Source (Anthropic Messages API)';
    outLbl.textContent = 'Target (OpenAI Chat Completions)';
  }
}
function oacConvert(){
  oacUpdateLabels();
  const raw = document.getElementById('oac-input').value.trim();
  const outEl = document.getElementById('oac-output');
  const stats = document.getElementById('oac-stats');
  if (!raw){ outEl.value = ''; stats.innerHTML = ''; return; }
  let parsed;
  try { parsed = JSON.parse(raw); }
  catch(e){ outEl.value = ''; stats.innerHTML = '<span class="oac-err">Invalid JSON: ' + e.message + '</span>'; return; }
  try {
    if (oacDir() === 'o2a'){
      let arr = parsed;
      if (!Array.isArray(arr)){
        if (arr && Array.isArray(arr.messages)) arr = arr.messages;
        else throw new Error('Expected an array of OpenAI messages, or {messages: [...]}.');
      }
      const result = oacOpenaiToAnthropic(arr);
      outEl.value = JSON.stringify(result, null, 2);
      stats.innerHTML = '<span class="oac-ok">✓ Converted</span> · ' + result.messages.length + ' messages · system: ' + (result.system ? '"' + result.system.slice(0, 50) + (result.system.length > 50 ? '…' : '') + '"' : '(none)');
    } else {
      const result = oacAnthropicToOpenai(parsed);
      outEl.value = JSON.stringify(result, null, 2);
      const sysMsgs = result.filter(m => m.role === 'system').length;
      stats.innerHTML = '<span class="oac-ok">✓ Converted</span> · ' + result.length + ' messages' + (sysMsgs ? ' (incl. ' + sysMsgs + ' system)' : '');
    }
  } catch(e){
    outEl.value = '';
    stats.innerHTML = '<span class="oac-err">✗ ' + (e.message || String(e)) + '</span>';
  }
}
function oacSwap(){
  const inEl = document.getElementById('oac-input');
  const outEl = document.getElementById('oac-output');
  const radios = document.querySelectorAll('input[name="oac-dir"]');
  const wasO2A = oacDir() === 'o2a';
  radios.forEach(r => r.checked = (r.value === (wasO2A ? 'a2o' : 'o2a')));
  // Move output into input and re-run
  inEl.value = outEl.value || inEl.value;
  oacConvert();
}
function oacCopy(btn){
  const v = document.getElementById('oac-output').value;
  if (!v) return;
  navigator.clipboard.writeText(v).then(() => {
    const orig = btn.textContent;
    btn.textContent = '✓';
    setTimeout(() => btn.textContent = orig, 1400);
  });
}
document.addEventListener('DOMContentLoaded', oacConvert);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>OpenAI's Chat Completions API and Anthropic's Messages API both let you send a multi-turn conversation, but they shape the JSON differently enough that prompts and tool-call traces don't drop in cleanly when you switch providers. The mismatches are small (system message placement, tool-call vs tool-use, image block shape, role: 'tool' vs content-array tool_result) but each one is a 10-minute rabbit hole when you're under deadline. This converter handles the translation so you can paste an OpenAI conversation and get back an Anthropic-shaped one (or vice versa).</p>

<h3>What gets translated</h3>
<ul>
  <li><strong>System messages.</strong> OpenAI puts the system instruction as a regular message with <code>role: "system"</code>. Anthropic puts it at the top level as a <code>system</code> field on the request. We move it across and concatenate if you have multiple. (Anthropic accepts a single string for system; multiple OpenAI system messages get joined with double newlines.)</li>
  <li><strong>Tool calls (assistant side).</strong> OpenAI: <code>tool_calls: [{id, type:'function', function:{name, arguments:'JSON-string'}}]</code>. Anthropic: a <code>tool_use</code> block inside the assistant's <code>content</code> array with <code>{id, name, input}</code> (parsed object, not a string). We parse OpenAI's escaped JSON arguments into the structured <code>input</code> Anthropic expects, and the reverse direction re-stringifies.</li>
  <li><strong>Tool results.</strong> OpenAI: a separate message with <code>role: "tool"</code>, <code>tool_call_id</code>, and <code>content</code>. Anthropic: a <code>tool_result</code> block inside the next <em>user</em> message's content array, with <code>tool_use_id</code>. Consecutive OpenAI <code>tool</code> messages get coalesced into one Anthropic user message containing multiple <code>tool_result</code> blocks (the shape Anthropic actually wants).</li>
  <li><strong>Images.</strong> OpenAI: <code>{type:'image_url', image_url:{url}}</code> inside a user content array. Anthropic: <code>{type:'image', source:{type:'base64',media_type,data}}</code> or <code>{type:'image', source:{type:'url',url}}</code>. We detect <code>data:</code> URLs and convert them; bare URLs pass through as URL-source images.</li>
  <li><strong>Plain text content.</strong> OpenAI uses a string; Anthropic accepts both a string and a one-element <code>[{type:'text', text}]</code> array. We use whichever is simpler.</li>
</ul>

<h3>What doesn't translate</h3>
<ul>
  <li><strong>Streaming events.</strong> This converter handles request/response JSON, not the SSE event streams. If you have a stream dump, reconstruct the full final message first.</li>
  <li><strong>Provider-specific fields.</strong> Things like OpenAI's <code>logprobs</code>, Anthropic's <code>stop_sequences</code>, sampling parameters, etc. live at the request top level, not inside messages — they're not part of the format we touch.</li>
  <li><strong>Cache control hints.</strong> Anthropic's <code>cache_control: {type:'ephemeral'}</code> hints have no OpenAI equivalent. They survive going OpenAI → Anthropic (no source to attach them to anyway), but are dropped when going Anthropic → OpenAI.</li>
  <li><strong>Tool definitions.</strong> The <em>schema</em> of your tools (the <code>tools</code> field on the request) lives outside the messages array. Each provider's tool-definition shape is different (OpenAI: function calling; Anthropic: <code>input_schema</code>). Convert those separately.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>OpenAI argument escaping.</strong> OpenAI's <code>arguments</code> is a JSON-encoded string, not a parsed object. If it's malformed (rare, but happens with tiny models), we put it under <code>_raw</code> in the Anthropic <code>input</code> instead of throwing.</li>
  <li><strong>Anthropic top-level system.</strong> When converting OpenAI → Anthropic, the result is <code>{system, messages}</code>. If you want just the messages array, use the <code>.messages</code> field — but remember to attach <code>system</code> to your API request separately.</li>
  <li><strong>Strict alternation.</strong> Anthropic requires user / assistant / user / assistant in strict alternation (after the optional system). The converter mostly preserves this, but if your OpenAI source has two consecutive user messages, the Anthropic output will too — and the API will reject it. Merge them first.</li>
  <li><strong>Multi-modal in OpenAI.</strong> An OpenAI user message with images uses a <em>content array</em> instead of a string. We handle this; just make sure your input parses as JSON (no Python-style <code>None</code>/single quotes).</li>
  <li><strong>Privacy.</strong> Nothing leaves the page. Conversion is pure JavaScript; no API keys, no network calls.</li>
</ul>
""",
        "de": """
<h2>Wozu ist das gut?</h2>
<p>Die Chat Completions API von OpenAI und die Messages API von Anthropic erlauben beide Multi-Turn-Konversationen, formen das JSON aber unterschiedlich genug, dass Prompts und Tool-Call-Traces beim Provider-Wechsel nicht sauber rüberkommen. Die Unterschiede sind klein (System-Message-Position, tool-call vs tool-use, Image-Block-Form, role: 'tool' vs Content-Array <code>tool_result</code>), aber jeder einzelne ist ein 10-Minuten-Kaninchenbau, wenn du unter Zeitdruck stehst. Dieser Konverter übernimmt die Übersetzung, damit du eine OpenAI-Konversation einfügen und eine Anthropic-geformte zurückbekommst (oder umgekehrt).</p>

<h3>Was übersetzt wird</h3>
<ul>
  <li><strong>System-Messages.</strong> OpenAI nutzt eine reguläre Nachricht mit <code>role: "system"</code>. Anthropic legt sie auf Request-Top-Level als <code>system</code>-Feld ab. Wir verschieben und verketten, wenn mehrere vorhanden sind.</li>
  <li><strong>Tool-Calls (assistant-Seite).</strong> OpenAI: <code>tool_calls: [{id, type:'function', function:{name, arguments:'JSON-string'}}]</code>. Anthropic: ein <code>tool_use</code>-Block im <code>content</code>-Array mit <code>{id, name, input}</code> (geparstes Objekt, kein String). Wir parsen OpenAIs escapte JSON-Argumente in das strukturierte <code>input</code> für Anthropic; die Gegenrichtung serialisiert zurück.</li>
  <li><strong>Tool-Ergebnisse.</strong> OpenAI: eigene Nachricht mit <code>role: "tool"</code>, <code>tool_call_id</code> und <code>content</code>. Anthropic: <code>tool_result</code>-Block im nächsten <em>user</em>-Content-Array mit <code>tool_use_id</code>. Aufeinanderfolgende OpenAI-<code>tool</code>-Nachrichten werden zu einer Anthropic-User-Message mit mehreren <code>tool_result</code>-Blöcken zusammengezogen.</li>
  <li><strong>Bilder.</strong> OpenAI: <code>{type:'image_url', image_url:{url}}</code>. Anthropic: <code>{type:'image', source:{type:'base64',media_type,data}}</code> oder <code>{type:'image', source:{type:'url',url}}</code>. Wir erkennen <code>data:</code>-URLs und konvertieren; reine URLs gehen als URL-Source-Image durch.</li>
  <li><strong>Reiner Text-Content.</strong> OpenAI nutzt einen String; Anthropic akzeptiert String <em>und</em> ein einelementiges <code>[{type:'text', text}]</code>-Array. Wir nehmen, was einfacher ist.</li>
</ul>

<h3>Was nicht übersetzt wird</h3>
<ul>
  <li><strong>Streaming-Events.</strong> Wir handhaben Request/Response-JSON, nicht die SSE-Event-Streams. Bei Stream-Dumps die finale Nachricht erst rekonstruieren.</li>
  <li><strong>Provider-spezifische Felder.</strong> Dinge wie OpenAIs <code>logprobs</code>, Anthropics <code>stop_sequences</code>, Sampling-Parameter — leben auf Request-Top-Level, nicht in Messages. Nicht Teil des Formats, das wir anfassen.</li>
  <li><strong>Cache-Control-Hints.</strong> Anthropics <code>cache_control: {type:'ephemeral'}</code> hat kein OpenAI-Äquivalent. Überlebt OpenAI → Anthropic (keine Quelle), wird aber bei Anthropic → OpenAI verworfen.</li>
  <li><strong>Tool-Definitionen.</strong> Das <em>Schema</em> deiner Tools (das <code>tools</code>-Feld auf dem Request) lebt außerhalb des Messages-Arrays. Format unterschiedlich zwischen den Providern — separat konvertieren.</li>
</ul>

<h3>Typische Stolperfallen</h3>
<ul>
  <li><strong>OpenAI-Argument-Escaping.</strong> OpenAIs <code>arguments</code> ist ein JSON-codierter String, kein geparstes Objekt. Bei kaputtem JSON (selten, aber bei kleinen Modellen vorkommend) packen wir es in <code>_raw</code> in Anthropics <code>input</code>, statt zu werfen.</li>
  <li><strong>Anthropic Top-Level-System.</strong> Bei OpenAI → Anthropic ist das Ergebnis <code>{system, messages}</code>. Wenn du nur das Messages-Array willst, nutze <code>.messages</code> — aber denk dran, <code>system</code> separat an den Request zu hängen.</li>
  <li><strong>Strikte Alternation.</strong> Anthropic verlangt strikten Wechsel user/assistant nach dem optionalen System. Konverter erhält das meistens; bei zwei aufeinanderfolgenden User-Messages in OpenAI hat die Anthropic-Ausgabe das auch — und die API lehnt es ab. Vorher mergen.</li>
  <li><strong>Multi-Modal in OpenAI.</strong> Eine OpenAI-User-Message mit Bildern nutzt ein <em>Content-Array</em> statt String. Handhaben wir; nur stell sicher, dass dein Input als JSON parst (kein Python-<code>None</code>, keine Single Quotes).</li>
  <li><strong>Privacy.</strong> Nichts verlässt die Seite. Konvertierung ist reines JS; keine API-Keys, keine Netzwerk-Calls.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>La Chat Completions API de OpenAI y la Messages API de Anthropic permiten conversaciones multi-turno, pero estructuran el JSON de forma suficientemente distinta como para que los prompts y trazas de tool-calls no caigan bien al cambiar de proveedor. Las diferencias son pequeñas (posición del system message, tool-call vs tool-use, forma de bloques de imagen, role: 'tool' vs <code>tool_result</code> en content) pero cada una es un agujero de 10 minutos cuando estás contra el reloj. Este convertidor hace la traducción para que pegues una conversación OpenAI y obtengas una versión Anthropic (o al revés).</p>

<h3>Qué se traduce</h3>
<ul>
  <li><strong>System messages.</strong> OpenAI usa un mensaje normal con <code>role: "system"</code>. Anthropic lo pone top-level como <code>system</code>. Movemos y concatenamos si hay varios.</li>
  <li><strong>Tool-calls (lado assistant).</strong> OpenAI: <code>tool_calls: [{id, type:'function', function:{name, arguments:'JSON-string'}}]</code>. Anthropic: bloque <code>tool_use</code> dentro de <code>content</code> con <code>{id, name, input}</code> (objeto parseado, no string). Parseamos los argumentos escapados de OpenAI a <code>input</code> estructurado para Anthropic; al revés se re-serializa.</li>
  <li><strong>Tool results.</strong> OpenAI: mensaje aparte con <code>role: "tool"</code>, <code>tool_call_id</code> y <code>content</code>. Anthropic: bloque <code>tool_result</code> dentro del siguiente mensaje <em>user</em> con <code>tool_use_id</code>. Mensajes <code>tool</code> consecutivos de OpenAI se fusionan en un user de Anthropic con múltiples <code>tool_result</code>.</li>
  <li><strong>Imágenes.</strong> OpenAI: <code>{type:'image_url', image_url:{url}}</code>. Anthropic: <code>{type:'image', source:{type:'base64',media_type,data}}</code> o URL-source. Detectamos URLs <code>data:</code> y convertimos; URLs simples pasan como URL-source.</li>
  <li><strong>Texto plano.</strong> OpenAI usa string; Anthropic acepta string <em>o</em> array <code>[{type:'text', text}]</code> de un elemento. Usamos lo más simple.</li>
</ul>

<h3>Qué no se traduce</h3>
<ul>
  <li><strong>Eventos de streaming.</strong> Manejamos JSON de request/response, no streams SSE. Si tienes un dump de stream, reconstruye el mensaje final primero.</li>
  <li><strong>Campos específicos del proveedor.</strong> Cosas como <code>logprobs</code> de OpenAI, <code>stop_sequences</code> de Anthropic, parámetros de sampling — viven en el top-level del request, no dentro de los messages.</li>
  <li><strong>Pistas de cache-control.</strong> El <code>cache_control: {type:'ephemeral'}</code> de Anthropic no tiene equivalente en OpenAI. Sobrevive OpenAI → Anthropic (no hay fuente), pero se descarta al revés.</li>
  <li><strong>Definiciones de tools.</strong> El <em>schema</em> de tus tools (campo <code>tools</code> del request) vive fuera del array de messages. Formato distinto entre proveedores — convierte aparte.</li>
</ul>

<h3>Errores comunes</h3>
<ul>
  <li><strong>Escaping de argumentos de OpenAI.</strong> <code>arguments</code> de OpenAI es un string JSON-codificado, no un objeto parseado. Si está roto (raro, pasa con modelos chicos), lo metemos en <code>_raw</code> en <code>input</code> de Anthropic en vez de lanzar.</li>
  <li><strong>System top-level de Anthropic.</strong> En OpenAI → Anthropic el resultado es <code>{system, messages}</code>. Si solo quieres el array, usa <code>.messages</code> — pero acuérdate de pasar <code>system</code> al request por separado.</li>
  <li><strong>Alternancia estricta.</strong> Anthropic exige user/assistant alternado (tras el system opcional). El convertidor lo preserva en general; si tu fuente OpenAI tiene dos users consecutivos, la salida Anthropic también — y la API lo rechazará. Fusiona antes.</li>
  <li><strong>Multi-modal en OpenAI.</strong> Un mensaje user de OpenAI con imágenes usa <em>content array</em> en vez de string. Lo manejamos; solo asegúrate de que tu entrada parsee como JSON.</li>
  <li><strong>Privacidad.</strong> Nada sale de la página. Conversión en JS puro; sin API keys, sin red.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>L'API Chat Completions d'OpenAI et l'API Messages d'Anthropic permettent toutes deux des conversations multi-tours, mais structurent le JSON de manière suffisamment différente pour que les prompts et traces de tool-calls ne tombent pas proprement quand on change de fournisseur. Les écarts sont petits (placement du system, tool-call vs tool-use, forme des blocs d'image, role: 'tool' vs <code>tool_result</code> en content) mais chacun est un trou de lapin de 10 minutes quand on est sous pression. Ce convertisseur fait la traduction pour que vous puissiez coller une conversation OpenAI et obtenir une version Anthropic (ou l'inverse).</p>

<h3>Ce qui est traduit</h3>
<ul>
  <li><strong>System messages.</strong> OpenAI : message normal avec <code>role: "system"</code>. Anthropic : champ <code>system</code> au top-level du request. On déplace et concatène s'il y en a plusieurs.</li>
  <li><strong>Tool-calls (côté assistant).</strong> OpenAI : <code>tool_calls: [{id, type:'function', function:{name, arguments:'JSON-string'}}]</code>. Anthropic : bloc <code>tool_use</code> dans <code>content</code> avec <code>{id, name, input}</code> (objet parsé, pas une chaîne). On parse les arguments échappés d'OpenAI vers <code>input</code> structuré ; le sens inverse re-sérialise.</li>
  <li><strong>Tool results.</strong> OpenAI : message à part avec <code>role: "tool"</code>, <code>tool_call_id</code>, <code>content</code>. Anthropic : bloc <code>tool_result</code> dans le contenu du prochain message <em>user</em> avec <code>tool_use_id</code>. Les messages <code>tool</code> consécutifs d'OpenAI fusionnent en un user Anthropic avec plusieurs <code>tool_result</code>.</li>
  <li><strong>Images.</strong> OpenAI : <code>{type:'image_url', image_url:{url}}</code>. Anthropic : <code>{type:'image', source:{type:'base64',media_type,data}}</code> ou URL-source. On détecte les URLs <code>data:</code> et on convertit ; les URLs simples passent en URL-source.</li>
  <li><strong>Texte brut.</strong> OpenAI utilise une string ; Anthropic accepte string <em>ou</em> tableau <code>[{type:'text', text}]</code> à un élément. On prend ce qui est le plus simple.</li>
</ul>

<h3>Ce qui n'est pas traduit</h3>
<ul>
  <li><strong>Événements de streaming.</strong> On gère JSON de request/response, pas les streams SSE. Si vous avez un dump de stream, reconstruisez le message final d'abord.</li>
  <li><strong>Champs spécifiques au fournisseur.</strong> <code>logprobs</code> d'OpenAI, <code>stop_sequences</code> d'Anthropic, paramètres de sampling — vivent au top-level du request, pas dans les messages.</li>
  <li><strong>Hints cache-control.</strong> Le <code>cache_control: {type:'ephemeral'}</code> d'Anthropic n'a pas d'équivalent OpenAI. Survit en OpenAI → Anthropic (pas de source), mais est jeté en Anthropic → OpenAI.</li>
  <li><strong>Définitions de tools.</strong> Le <em>schéma</em> de vos tools (champ <code>tools</code> du request) vit hors du tableau messages. Format différent entre fournisseurs — convertir séparément.</li>
</ul>

<h3>Pièges courants</h3>
<ul>
  <li><strong>Échappement des arguments OpenAI.</strong> <code>arguments</code> d'OpenAI est une chaîne JSON-encodée, pas un objet parsé. Si elle est cassée (rare, arrive avec petits modèles), on le met dans <code>_raw</code> dans <code>input</code> Anthropic plutôt que de jeter.</li>
  <li><strong>System top-level d'Anthropic.</strong> En OpenAI → Anthropic le résultat est <code>{system, messages}</code>. Si vous voulez juste le tableau, utilisez <code>.messages</code> — mais pensez à passer <code>system</code> au request séparément.</li>
  <li><strong>Alternance stricte.</strong> Anthropic exige user/assistant en alternance stricte (après le system optionnel). Le convertisseur préserve en général ; si votre source OpenAI a deux user consécutifs, la sortie Anthropic aussi — et l'API rejettera. Fusionnez avant.</li>
  <li><strong>Multi-modal en OpenAI.</strong> Un message user OpenAI avec images utilise un <em>content array</em> au lieu d'une string. On gère ; assurez-vous juste que votre entrée parse en JSON.</li>
  <li><strong>Privacy.</strong> Rien ne quitte la page. Conversion en JS pur ; pas d'API keys, pas de réseau.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>L'API Chat Completions di OpenAI e la Messages API di Anthropic permettono entrambe conversazioni multi-turno, ma strutturano il JSON in modo abbastanza diverso da impedire ai prompt e alle trace di tool-call di transitare puliti quando cambi provider. Le differenze sono piccole (posizione del system message, tool-call vs tool-use, forma dei blocchi immagine, role: 'tool' vs <code>tool_result</code> nel content) ma ognuna è una tana di coniglio da 10 minuti quando sei sotto deadline. Questo convertitore fa la traduzione: incolli una conversazione OpenAI e ottieni la versione Anthropic (o viceversa).</p>

<h3>Cosa viene tradotto</h3>
<ul>
  <li><strong>System messages.</strong> OpenAI: messaggio normale con <code>role: "system"</code>. Anthropic: campo <code>system</code> top-level sul request. Spostiamo e concateniamo se ne hai più di uno.</li>
  <li><strong>Tool-call (lato assistant).</strong> OpenAI: <code>tool_calls: [{id, type:'function', function:{name, arguments:'JSON-string'}}]</code>. Anthropic: blocco <code>tool_use</code> dentro <code>content</code> con <code>{id, name, input}</code> (oggetto parsato, non stringa). Parsiamo gli arguments escapati di OpenAI in <code>input</code> strutturato; il senso opposto ri-serializza.</li>
  <li><strong>Tool result.</strong> OpenAI: messaggio separato con <code>role: "tool"</code>, <code>tool_call_id</code>, <code>content</code>. Anthropic: blocco <code>tool_result</code> nel content del prossimo messaggio <em>user</em> con <code>tool_use_id</code>. Messaggi <code>tool</code> consecutivi di OpenAI vengono coalesced in un singolo user Anthropic con più <code>tool_result</code>.</li>
  <li><strong>Immagini.</strong> OpenAI: <code>{type:'image_url', image_url:{url}}</code>. Anthropic: <code>{type:'image', source:{type:'base64',media_type,data}}</code> o URL-source. Rileviamo URL <code>data:</code> e convertiamo; URL semplici passano come URL-source.</li>
  <li><strong>Testo semplice.</strong> OpenAI usa stringa; Anthropic accetta stringa <em>o</em> array <code>[{type:'text', text}]</code> a un elemento. Usiamo ciò che è più semplice.</li>
</ul>

<h3>Cosa non viene tradotto</h3>
<ul>
  <li><strong>Eventi di streaming.</strong> Gestiamo JSON di request/response, non gli stream SSE. Se hai un dump di stream, ricostruisci prima il messaggio finale.</li>
  <li><strong>Campi provider-specifici.</strong> <code>logprobs</code> di OpenAI, <code>stop_sequences</code> di Anthropic, parametri di sampling — stanno al top-level del request, non dentro i messaggi.</li>
  <li><strong>Hint cache-control.</strong> Il <code>cache_control: {type:'ephemeral'}</code> di Anthropic non ha equivalente OpenAI. Sopravvive a OpenAI → Anthropic (nessuna sorgente), ma viene scartato in Anthropic → OpenAI.</li>
  <li><strong>Definizioni di tool.</strong> Lo <em>schema</em> dei tuoi tool (campo <code>tools</code> del request) sta fuori dall'array messages. Formato diverso tra provider — converti separatamente.</li>
</ul>

<h3>Trappole comuni</h3>
<ul>
  <li><strong>Escaping arguments OpenAI.</strong> <code>arguments</code> di OpenAI è una stringa JSON-encoded, non oggetto parsato. Se è malformato (raro, capita con modelli piccoli), lo mettiamo in <code>_raw</code> dentro <code>input</code> Anthropic invece di lanciare.</li>
  <li><strong>System top-level Anthropic.</strong> In OpenAI → Anthropic il risultato è <code>{system, messages}</code>. Se vuoi solo l'array, usa <code>.messages</code> — ma ricordati di attaccare <code>system</code> al request separatamente.</li>
  <li><strong>Alternanza stretta.</strong> Anthropic esige user/assistant in alternanza stretta (dopo il system opzionale). Il convertitore preserva in generale; se la sorgente OpenAI ha due user consecutivi, anche l'output Anthropic — e l'API rifiuterà. Mergeli prima.</li>
  <li><strong>Multi-modal in OpenAI.</strong> Un messaggio user OpenAI con immagini usa un <em>content array</em> invece di stringa. Lo gestiamo; assicurati solo che il tuo input parsi come JSON.</li>
  <li><strong>Privacy.</strong> Niente lascia la pagina. Conversione in JS puro; nessuna API key, nessuna chiamata di rete.</li>
</ul>
""",
        "pt": """
<h2>Pra que serve?</h2>
<p>A Chat Completions API da OpenAI e a Messages API da Anthropic permitem conversas multi-turno, mas estruturam o JSON de forma diferente o suficiente pra prompts e traces de tool-call não caírem limpos quando você troca de provider. As diferenças são pequenas (posição do system message, tool-call vs tool-use, formato de blocos de imagem, role: 'tool' vs <code>tool_result</code> em content) mas cada uma é um buraco de coelho de 10 minutos quando você tá no prazo. Esse conversor faz a tradução: cola uma conversa OpenAI e recebe versão Anthropic (ou vice-versa).</p>

<h3>O que é traduzido</h3>
<ul>
  <li><strong>System messages.</strong> OpenAI: mensagem normal com <code>role: "system"</code>. Anthropic: campo <code>system</code> top-level do request. Movemos e concatenamos se houver vários.</li>
  <li><strong>Tool-calls (lado assistant).</strong> OpenAI: <code>tool_calls: [{id, type:'function', function:{name, arguments:'JSON-string'}}]</code>. Anthropic: bloco <code>tool_use</code> dentro do <code>content</code> com <code>{id, name, input}</code> (objeto parseado, não string). Parseamos os arguments escapados da OpenAI pra <code>input</code> estruturado; sentido oposto re-serializa.</li>
  <li><strong>Tool results.</strong> OpenAI: mensagem separada com <code>role: "tool"</code>, <code>tool_call_id</code>, <code>content</code>. Anthropic: bloco <code>tool_result</code> dentro do content do próximo <em>user</em> com <code>tool_use_id</code>. Mensagens <code>tool</code> consecutivas da OpenAI são coalescidas em um único user Anthropic com múltiplos <code>tool_result</code>.</li>
  <li><strong>Imagens.</strong> OpenAI: <code>{type:'image_url', image_url:{url}}</code>. Anthropic: <code>{type:'image', source:{type:'base64',media_type,data}}</code> ou URL-source. Detectamos URLs <code>data:</code> e convertemos; URLs simples passam como URL-source.</li>
  <li><strong>Texto puro.</strong> OpenAI usa string; Anthropic aceita string <em>ou</em> array <code>[{type:'text', text}]</code> de um elemento. Usamos o mais simples.</li>
</ul>

<h3>O que não é traduzido</h3>
<ul>
  <li><strong>Eventos de streaming.</strong> Tratamos JSON de request/response, não streams SSE. Se você tem dump de stream, reconstrua a mensagem final primeiro.</li>
  <li><strong>Campos específicos do provider.</strong> <code>logprobs</code> da OpenAI, <code>stop_sequences</code> da Anthropic, parâmetros de sampling — ficam no top-level do request, não dentro dos messages.</li>
  <li><strong>Hints de cache-control.</strong> O <code>cache_control: {type:'ephemeral'}</code> da Anthropic não tem equivalente OpenAI. Sobrevive a OpenAI → Anthropic (sem fonte), mas é descartado em Anthropic → OpenAI.</li>
  <li><strong>Definições de tool.</strong> O <em>schema</em> dos seus tools (campo <code>tools</code> do request) fica fora do array messages. Formato diferente entre providers — converta separadamente.</li>
</ul>

<h3>Pegadinhas comuns</h3>
<ul>
  <li><strong>Escaping dos arguments da OpenAI.</strong> <code>arguments</code> da OpenAI é string JSON-encoded, não objeto parseado. Se tá malformado (raro, acontece com modelos pequenos), colocamos em <code>_raw</code> no <code>input</code> da Anthropic em vez de lançar erro.</li>
  <li><strong>System top-level da Anthropic.</strong> Em OpenAI → Anthropic o resultado é <code>{system, messages}</code>. Se você quer só o array, use <code>.messages</code> — mas lembre de anexar <code>system</code> ao request separadamente.</li>
  <li><strong>Alternância estrita.</strong> Anthropic exige user/assistant em alternância estrita (após o system opcional). O conversor preserva em geral; se sua fonte OpenAI tem dois user seguidos, a saída Anthropic também — e a API rejeita. Faça merge antes.</li>
  <li><strong>Multi-modal na OpenAI.</strong> Mensagem user da OpenAI com imagens usa <em>content array</em> em vez de string. Tratamos; só garanta que seu input parse como JSON.</li>
  <li><strong>Privacidade.</strong> Nada sai da página. Conversão em JS puro; sem API keys, sem rede.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>API Chat Completions od OpenAI i Messages API od Anthropica pozwalają na rozmowy multi-turn, ale strukturyzują JSON na tyle różnie, że prompty i trace tool-calli nie wpadają czysto przy zmianie providera. Różnice są małe (umiejscowienie system message, tool-call vs tool-use, kształt bloków obrazków, role: 'tool' vs <code>tool_result</code> w content) ale każda to 10-minutowa królicza nora gdy masz deadline. Ten konwerter robi tłumaczenie: wklejasz rozmowę OpenAI, dostajesz wersję Anthropic (lub odwrotnie).</p>

<h3>Co jest tłumaczone</h3>
<ul>
  <li><strong>System messages.</strong> OpenAI: zwykła wiadomość z <code>role: "system"</code>. Anthropic: pole <code>system</code> top-level w requeście. Przenosimy i konkatenujemy jeśli jest kilka.</li>
  <li><strong>Tool-calle (strona assistanta).</strong> OpenAI: <code>tool_calls: [{id, type:'function', function:{name, arguments:'JSON-string'}}]</code>. Anthropic: blok <code>tool_use</code> wewnątrz <code>content</code> z <code>{id, name, input}</code> (sparsowany obiekt, nie string). Parsujemy escapowane arguments OpenAI do strukturyzowanego <code>input</code> dla Anthropica; odwrotny kierunek re-serializuje.</li>
  <li><strong>Tool results.</strong> OpenAI: oddzielna wiadomość z <code>role: "tool"</code>, <code>tool_call_id</code> i <code>content</code>. Anthropic: blok <code>tool_result</code> wewnątrz content następnej wiadomości <em>user</em> z <code>tool_use_id</code>. Kolejne wiadomości <code>tool</code> OpenAI łączą się w jedną user Anthropica z wieloma <code>tool_result</code>.</li>
  <li><strong>Obrazki.</strong> OpenAI: <code>{type:'image_url', image_url:{url}}</code>. Anthropic: <code>{type:'image', source:{type:'base64',media_type,data}}</code> albo URL-source. Wykrywamy URLe <code>data:</code> i konwertujemy; gołe URLe przechodzą jako URL-source.</li>
  <li><strong>Zwykły tekst.</strong> OpenAI używa stringa; Anthropic akceptuje stringa <em>lub</em> jednoelementową tablicę <code>[{type:'text', text}]</code>. Używamy czego prostsze.</li>
</ul>

<h3>Czego się nie tłumaczy</h3>
<ul>
  <li><strong>Eventy streamingowe.</strong> Obsługujemy JSON request/response, nie strumienie SSE. Z dumpem streamingowym najpierw zrekonstruuj końcową wiadomość.</li>
  <li><strong>Pola specyficzne dla providera.</strong> <code>logprobs</code> OpenAI, <code>stop_sequences</code> Anthropica, parametry samplingu — żyją w top-level requestu, nie w messages.</li>
  <li><strong>Wskazówki cache-control.</strong> <code>cache_control: {type:'ephemeral'}</code> Anthropica nie ma odpowiednika w OpenAI. Przeżywa OpenAI → Anthropic (brak źródła), ale jest porzucany przy Anthropic → OpenAI.</li>
  <li><strong>Definicje toolów.</strong> <em>Schemat</em> twoich toolów (pole <code>tools</code> requestu) żyje poza tablicą messages. Format różny między providerami — konwertuj osobno.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Escapowanie argumentów OpenAI.</strong> <code>arguments</code> OpenAI to string JSON-zakodowany, nie sparsowany obiekt. Jeśli zepsuty (rzadko, zdarza się z małymi modelami), wkładamy do <code>_raw</code> w <code>input</code> Anthropica zamiast rzucać.</li>
  <li><strong>System top-level Anthropica.</strong> W OpenAI → Anthropic wynik to <code>{system, messages}</code>. Jeśli chcesz tylko tablicę, użyj <code>.messages</code> — ale pamiętaj dołączyć <code>system</code> do requestu osobno.</li>
  <li><strong>Ścisła alternacja.</strong> Anthropic wymaga user/assistant w ścisłej alternacji (po opcjonalnym system). Konwerter zazwyczaj zachowuje; jeśli twoje źródło OpenAI ma dwa user pod rząd, wyjście Anthropic też — i API odrzuci. Zmerguj wcześniej.</li>
  <li><strong>Multi-modal w OpenAI.</strong> Wiadomość user OpenAI z obrazkami używa <em>content array</em> zamiast stringa. Obsługujemy; tylko upewnij się że twój input parsuje jako JSON.</li>
  <li><strong>Prywatność.</strong> Nic nie opuszcza strony. Konwersja w czystym JS; bez API keys, bez sieci.</li>
</ul>
""",
        "ja": """
<h2>これは何のため？</h2>
<p>OpenAI の Chat Completions API と Anthropic の Messages API はどちらもマルチターン会話を扱えますが、JSON 構造が微妙に違うため、プロバイダを切り替えるとプロンプトやツール呼び出しのトレースがそのままでは通りません。差分は小さい（system メッセージの位置、tool-call と tool-use、画像ブロックの形、role: 'tool' と content 内の <code>tool_result</code>）ですが、締切に追われているときには 1 つ 1 つが 10 分の落とし穴になります。このコンバーターはその翻訳を担当し、OpenAI 形式の会話を貼れば Anthropic 形式が返ってきます（逆方向も同じ）。</p>

<h3>翻訳される内容</h3>
<ul>
  <li><strong>system メッセージ。</strong> OpenAI は <code>role: "system"</code> の通常メッセージ。Anthropic はリクエストのトップレベル <code>system</code> フィールド。移動し、複数あれば連結します。</li>
  <li><strong>ツール呼び出し（assistant 側）。</strong> OpenAI: <code>tool_calls: [{id, type:'function', function:{name, arguments:'JSON-string'}}]</code>。Anthropic: <code>content</code> 配列内の <code>tool_use</code> ブロック <code>{id, name, input}</code>（パース済みオブジェクト、文字列ではない）。OpenAI のエスケープされた arguments を Anthropic の構造化 <code>input</code> にパースします。逆方向は再シリアライズします。</li>
  <li><strong>ツール結果。</strong> OpenAI: <code>role: "tool"</code>、<code>tool_call_id</code>、<code>content</code> を持つ別メッセージ。Anthropic: 次の <em>user</em> メッセージの content 配列内の <code>tool_result</code> ブロックで <code>tool_use_id</code> を持つ。OpenAI で連続する <code>tool</code> メッセージは、複数の <code>tool_result</code> を含む 1 つの Anthropic user メッセージに統合されます。</li>
  <li><strong>画像。</strong> OpenAI: <code>{type:'image_url', image_url:{url}}</code>。Anthropic: <code>{type:'image', source:{type:'base64',media_type,data}}</code> または URL-source。<code>data:</code> URL を検知して変換、それ以外の URL は URL-source として通します。</li>
  <li><strong>プレーンテキスト。</strong> OpenAI は文字列、Anthropic は文字列または 1 要素の <code>[{type:'text', text}]</code> 配列のどちらも受け付けます。シンプルな方を使います。</li>
</ul>

<h3>翻訳されない内容</h3>
<ul>
  <li><strong>ストリーミングイベント。</strong> リクエスト／レスポンスの JSON が対象で、SSE イベントストリームは扱いません。ストリームのダンプがある場合は、まず最終メッセージを再構築してください。</li>
  <li><strong>プロバイダ固有のフィールド。</strong> OpenAI の <code>logprobs</code>、Anthropic の <code>stop_sequences</code>、サンプリングパラメータなどは、リクエストのトップレベルにあり messages の中ではないため、この変換の対象外です。</li>
  <li><strong>キャッシュ制御のヒント。</strong> Anthropic の <code>cache_control: {type:'ephemeral'}</code> に対応する OpenAI の構造はありません。OpenAI → Anthropic では生き残ります（付与する元情報がないため）が、Anthropic → OpenAI では落とされます。</li>
  <li><strong>ツール定義。</strong> ツールの <em>スキーマ</em>（リクエストの <code>tools</code> フィールド）は messages 配列の外にあります。プロバイダごとに形が違うので別途変換してください。</li>
</ul>

<h3>よくある落とし穴</h3>
<ul>
  <li><strong>OpenAI の引数エスケープ。</strong> OpenAI の <code>arguments</code> は JSON エンコードされた文字列で、パース済みオブジェクトではありません。壊れている場合（稀ですが小さなモデルで起こります）、例外を投げず Anthropic の <code>input</code> に <code>_raw</code> として格納します。</li>
  <li><strong>Anthropic のトップレベル system。</strong> OpenAI → Anthropic の結果は <code>{system, messages}</code> です。messages 配列だけ欲しい場合は <code>.messages</code> を使い、API リクエストには <code>system</code> を別途付ける点に注意してください。</li>
  <li><strong>厳格な交互順。</strong> Anthropic は（任意の system のあと）user / assistant の厳格な交互順を要求します。コンバーターは概ね保ちますが、OpenAI ソースに user が連続している場合は Anthropic 出力でも連続するため、API は拒否します。事前にマージしてください。</li>
  <li><strong>OpenAI のマルチモーダル。</strong> 画像を含む OpenAI user メッセージは文字列ではなく <em>content 配列</em> を使います。これも処理しますが、入力が JSON としてパースできることを確認してください（Python の <code>None</code> やシングルクォートは不可）。</li>
  <li><strong>プライバシー。</strong> 何もページ外に出ません。変換は純粋な JS、API キーもネットワーク呼び出しもありません。</li>
</ul>
""",
        "nl": """
<h2>Waar is dit voor?</h2>
<p>OpenAI's Chat Completions API en Anthropic's Messages API laten je beide multi-turn conversaties versturen, maar vormen het JSON net genoeg verschillend dat prompts en tool-call traces niet schoon overgaan als je van provider wisselt. De verschillen zijn klein (system message-plaatsing, tool-call vs tool-use, image-blok-vorm, role: 'tool' vs <code>tool_result</code> in content) maar elk is een 10-minuten konijnenhol als je deadline hebt. Deze converter doet de vertaling: plak een OpenAI-conversatie en krijg een Anthropic-versie terug (of andersom).</p>

<h3>Wat er vertaald wordt</h3>
<ul>
  <li><strong>System messages.</strong> OpenAI: gewoon bericht met <code>role: "system"</code>. Anthropic: top-level <code>system</code>-veld op het request. We verplaatsen en concateneren bij meerdere.</li>
  <li><strong>Tool-calls (assistant-kant).</strong> OpenAI: <code>tool_calls: [{id, type:'function', function:{name, arguments:'JSON-string'}}]</code>. Anthropic: <code>tool_use</code>-blok binnen <code>content</code> met <code>{id, name, input}</code> (geparseerd object, geen string). We parseren OpenAI's geëscapete arguments naar gestructureerde <code>input</code> voor Anthropic; de omgekeerde richting re-serializeert.</li>
  <li><strong>Tool results.</strong> OpenAI: apart bericht met <code>role: "tool"</code>, <code>tool_call_id</code>, <code>content</code>. Anthropic: <code>tool_result</code>-blok binnen de content van het volgende <em>user</em>-bericht met <code>tool_use_id</code>. Opeenvolgende OpenAI <code>tool</code>-berichten worden samengevoegd tot één Anthropic user met meerdere <code>tool_result</code>-blokken.</li>
  <li><strong>Afbeeldingen.</strong> OpenAI: <code>{type:'image_url', image_url:{url}}</code>. Anthropic: <code>{type:'image', source:{type:'base64',media_type,data}}</code> of URL-source. We detecteren <code>data:</code>-URLs en converteren; kale URLs gaan door als URL-source.</li>
  <li><strong>Platte tekst.</strong> OpenAI gebruikt een string; Anthropic accepteert een string <em>of</em> één-element-array <code>[{type:'text', text}]</code>. We nemen wat eenvoudiger is.</li>
</ul>

<h3>Wat niet vertaald wordt</h3>
<ul>
  <li><strong>Streaming-events.</strong> We behandelen request/response-JSON, geen SSE event-streams. Bij een stream-dump eerst het volledige eindbericht reconstrueren.</li>
  <li><strong>Provider-specifieke velden.</strong> OpenAI's <code>logprobs</code>, Anthropic's <code>stop_sequences</code>, sampling-parameters — leven op request-top-level, niet binnen messages.</li>
  <li><strong>Cache-control hints.</strong> Anthropic's <code>cache_control: {type:'ephemeral'}</code> heeft geen OpenAI-equivalent. Overleeft OpenAI → Anthropic (geen bron), maar wordt gedropt bij Anthropic → OpenAI.</li>
  <li><strong>Tool-definities.</strong> Het <em>schema</em> van je tools (het <code>tools</code>-veld op het request) leeft buiten de messages-array. Format verschilt per provider — los converteren.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>OpenAI argument-escaping.</strong> OpenAI's <code>arguments</code> is een JSON-encoded string, geen geparseerd object. Bij kapot JSON (zeldzaam, gebeurt bij kleine modellen) zetten we het in <code>_raw</code> in Anthropic's <code>input</code> in plaats van gooien.</li>
  <li><strong>Anthropic top-level system.</strong> Bij OpenAI → Anthropic is het resultaat <code>{system, messages}</code>. Wil je alleen de array, gebruik <code>.messages</code> — maar onthoud <code>system</code> apart aan je API-request te hangen.</li>
  <li><strong>Strikte alternatie.</strong> Anthropic vereist user/assistant strikte alternatie (na het optionele system). De converter behoudt dit meestal; als je OpenAI-bron twee user-berichten achter elkaar heeft, heeft de Anthropic-output dat ook — en de API weigert. Eerst mergen.</li>
  <li><strong>Multi-modaal in OpenAI.</strong> Een OpenAI user-bericht met afbeeldingen gebruikt een <em>content array</em> in plaats van een string. We behandelen dit; zorg alleen dat je input als JSON parseert.</li>
  <li><strong>Privacy.</strong> Niets verlaat de pagina. Conversie is pure JS; geen API keys, geen netwerk-calls.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>OpenAI'nin Chat Completions API'si ve Anthropic'in Messages API'si ikisi de multi-turn konuşma göndermene izin verir, ama JSON'u yeterince farklı şekillendirirler ki provider değiştirdiğinde prompt'lar ve tool-call trace'leri temizce geçmez. Farklar küçük (system mesaj yerleşimi, tool-call vs tool-use, görsel blok şekli, role: 'tool' vs content içinde <code>tool_result</code>) ama her biri deadline'dayken 10 dakikalık tavşan deliği. Bu dönüştürücü çeviriyi yapar: OpenAI konuşması yapıştır, Anthropic versiyonunu geri al (veya tersi).</p>

<h3>Ne çevriliyor</h3>
<ul>
  <li><strong>System mesajları.</strong> OpenAI: <code>role: "system"</code> ile normal mesaj. Anthropic: request'in top-level'inde <code>system</code> alanı. Birden fazlaysa taşıyıp birleştiriyoruz.</li>
  <li><strong>Tool-call'lar (assistant tarafı).</strong> OpenAI: <code>tool_calls: [{id, type:'function', function:{name, arguments:'JSON-string'}}]</code>. Anthropic: <code>content</code> içinde <code>tool_use</code> bloğu <code>{id, name, input}</code> ile (parse edilmiş nesne, string değil). OpenAI'nin escape'lenmiş arguments'ını Anthropic'in beklediği yapılandırılmış <code>input</code>'a parse ediyoruz; tersi yön tekrar string yapıyor.</li>
  <li><strong>Tool sonuçları.</strong> OpenAI: <code>role: "tool"</code>, <code>tool_call_id</code> ve <code>content</code> içeren ayrı mesaj. Anthropic: sonraki <em>user</em> mesajının content dizisinde <code>tool_use_id</code> içeren <code>tool_result</code> bloğu. Ardışık OpenAI <code>tool</code> mesajları birden fazla <code>tool_result</code> içeren tek bir Anthropic user mesajında birleştiriliyor.</li>
  <li><strong>Görseller.</strong> OpenAI: <code>{type:'image_url', image_url:{url}}</code>. Anthropic: <code>{type:'image', source:{type:'base64',media_type,data}}</code> veya URL-source. <code>data:</code> URL'leri tespit edip dönüştürüyoruz; çıplak URL'ler URL-source olarak geçiyor.</li>
  <li><strong>Düz metin.</strong> OpenAI string kullanır; Anthropic string <em>veya</em> tek elemanlı <code>[{type:'text', text}]</code> dizisi kabul eder. Daha basit olanı kullanıyoruz.</li>
</ul>

<h3>Ne çevrilmiyor</h3>
<ul>
  <li><strong>Streaming event'leri.</strong> Request/response JSON'unu ele alıyoruz, SSE event stream'lerini değil. Stream dump'ın varsa önce tam final mesajı yeniden oluştur.</li>
  <li><strong>Sağlayıcıya özgü alanlar.</strong> OpenAI'nin <code>logprobs</code>'u, Anthropic'in <code>stop_sequences</code>'i, sampling parametreleri — request top-level'inde yaşar, messages içinde değil.</li>
  <li><strong>Cache-control ipuçları.</strong> Anthropic'in <code>cache_control: {type:'ephemeral'}</code>'i OpenAI eşdeğerine sahip değil. OpenAI → Anthropic'te hayatta kalır (kaynak yok), ama Anthropic → OpenAI'de düşürülür.</li>
  <li><strong>Tool tanımları.</strong> Tool'larının <em>şeması</em> (request'in <code>tools</code> alanı) messages dizisinin dışında yaşar. Sağlayıcılar arasında format farklı — ayrı dönüştür.</li>
</ul>

<h3>Yaygın tuzaklar</h3>
<ul>
  <li><strong>OpenAI argument escape'i.</strong> OpenAI'nin <code>arguments</code>'ı JSON-encoded string, parse edilmiş nesne değil. Bozuksa (nadir, küçük modellerde olur), hata atmak yerine Anthropic <code>input</code>'unda <code>_raw</code> altına koyuyoruz.</li>
  <li><strong>Anthropic top-level system.</strong> OpenAI → Anthropic'te sonuç <code>{system, messages}</code>. Sadece diziyi istiyorsan <code>.messages</code> kullan — ama <code>system</code>'i API request'ine ayrı eklemeyi unutma.</li>
  <li><strong>Katı dönüşüm.</strong> Anthropic user/assistant katı dönüşümünü gerektirir (opsiyonel system'den sonra). Dönüştürücü genelde korur; OpenAI kaynağında ardışık iki user mesajı varsa, Anthropic çıktısında da olur — ve API reddeder. Önce merge et.</li>
  <li><strong>OpenAI'de multi-modal.</strong> Görsellerle OpenAI user mesajı string yerine <em>content array</em> kullanır. Bunu hallediyoruz; sadece input'unun JSON olarak parse olduğundan emin ol.</li>
  <li><strong>Gizlilik.</strong> Hiçbir şey sayfadan çıkmaz. Dönüştürme saf JS; API anahtarı yok, network çağrısı yok.</li>
</ul>
""",
        "id": """
<h2>Buat apa ini?</h2>
<p>API Chat Completions OpenAI dan Messages API Anthropic sama-sama membiarkanmu mengirim percakapan multi-turn, tapi membentuk JSON cukup berbeda sehingga prompt dan trace tool-call tidak masuk dengan rapi saat kamu ganti provider. Perbedaannya kecil (penempatan system message, tool-call vs tool-use, bentuk blok gambar, role: 'tool' vs <code>tool_result</code> di content) tapi setiap satunya adalah lubang kelinci 10 menit saat kamu di bawah deadline. Konverter ini menangani terjemahannya: tempel percakapan OpenAI dan dapatkan versi Anthropic kembali (atau sebaliknya).</p>

<h3>Apa yang diterjemahkan</h3>
<ul>
  <li><strong>System messages.</strong> OpenAI: pesan biasa dengan <code>role: "system"</code>. Anthropic: field <code>system</code> top-level di request. Kami pindahkan dan gabungkan kalau ada beberapa.</li>
  <li><strong>Tool-call (sisi assistant).</strong> OpenAI: <code>tool_calls: [{id, type:'function', function:{name, arguments:'JSON-string'}}]</code>. Anthropic: blok <code>tool_use</code> di dalam <code>content</code> dengan <code>{id, name, input}</code> (objek di-parse, bukan string). Kami parse arguments yang di-escape dari OpenAI ke <code>input</code> terstruktur yang Anthropic harapkan; arah sebaliknya men-stringify lagi.</li>
  <li><strong>Tool results.</strong> OpenAI: pesan terpisah dengan <code>role: "tool"</code>, <code>tool_call_id</code>, <code>content</code>. Anthropic: blok <code>tool_result</code> di dalam content pesan <em>user</em> berikutnya dengan <code>tool_use_id</code>. Pesan <code>tool</code> OpenAI berurutan digabung jadi satu user Anthropic dengan beberapa <code>tool_result</code>.</li>
  <li><strong>Gambar.</strong> OpenAI: <code>{type:'image_url', image_url:{url}}</code>. Anthropic: <code>{type:'image', source:{type:'base64',media_type,data}}</code> atau URL-source. Kami deteksi URL <code>data:</code> dan konversi; URL biasa lewat sebagai URL-source.</li>
  <li><strong>Teks polos.</strong> OpenAI pakai string; Anthropic terima string <em>atau</em> array satu elemen <code>[{type:'text', text}]</code>. Kami pakai yang lebih sederhana.</li>
</ul>

<h3>Apa yang tidak diterjemahkan</h3>
<ul>
  <li><strong>Event streaming.</strong> Kami menangani JSON request/response, bukan stream SSE. Kalau punya dump stream, rekonstruksi pesan final dulu.</li>
  <li><strong>Field spesifik provider.</strong> <code>logprobs</code> OpenAI, <code>stop_sequences</code> Anthropic, parameter sampling — tinggal di top-level request, bukan di messages.</li>
  <li><strong>Hint cache-control.</strong> <code>cache_control: {type:'ephemeral'}</code> Anthropic tidak ada padanan OpenAI. Selamat di OpenAI → Anthropic (tidak ada sumber), tapi dibuang di Anthropic → OpenAI.</li>
  <li><strong>Definisi tool.</strong> <em>Schema</em> tool-mu (field <code>tools</code> di request) tinggal di luar array messages. Format beda antar provider — konversi terpisah.</li>
</ul>

<h3>Jebakan umum</h3>
<ul>
  <li><strong>Escaping arguments OpenAI.</strong> <code>arguments</code> OpenAI adalah string JSON-encoded, bukan objek di-parse. Kalau rusak (jarang, terjadi dengan model kecil), kami taruh di <code>_raw</code> di <code>input</code> Anthropic alih-alih melempar error.</li>
  <li><strong>System top-level Anthropic.</strong> Di OpenAI → Anthropic hasilnya <code>{system, messages}</code>. Kalau cuma mau array, pakai <code>.messages</code> — tapi ingat lampirkan <code>system</code> ke request API secara terpisah.</li>
  <li><strong>Alternasi ketat.</strong> Anthropic mengharuskan alternasi user/assistant yang ketat (setelah system opsional). Konverter umumnya menjaganya; kalau sumber OpenAI-mu punya dua user berturut-turut, output Anthropic juga — dan API akan menolak. Merge dulu.</li>
  <li><strong>Multi-modal di OpenAI.</strong> Pesan user OpenAI dengan gambar pakai <em>content array</em> alih-alih string. Kami tangani; pastikan saja input-mu parse sebagai JSON.</li>
  <li><strong>Privasi.</strong> Tidak ada yang keluar dari halaman. Konversi JS murni; tanpa API key, tanpa panggilan network.</li>
</ul>
""",
        "vi": """
<h2>Cái này để làm gì?</h2>
<p>API Chat Completions của OpenAI và Messages API của Anthropic đều cho phép bạn gửi hội thoại multi-turn, nhưng định hình JSON đủ khác để prompt và trace tool-call không trôi sạch khi bạn đổi nhà cung cấp. Khác biệt nhỏ (vị trí system message, tool-call vs tool-use, hình dạng khối hình, role: 'tool' vs <code>tool_result</code> trong content) nhưng mỗi cái là một hố thỏ 10 phút khi bạn đang trong deadline. Bộ chuyển đổi này xử lý dịch thuật: dán hội thoại OpenAI, nhận lại phiên bản Anthropic (hoặc ngược lại).</p>

<h3>Cái gì được dịch</h3>
<ul>
  <li><strong>System messages.</strong> OpenAI: tin nhắn thông thường với <code>role: "system"</code>. Anthropic: field <code>system</code> top-level trên request. Chúng tôi di chuyển và ghép nối nếu có nhiều.</li>
  <li><strong>Tool-call (phía assistant).</strong> OpenAI: <code>tool_calls: [{id, type:'function', function:{name, arguments:'JSON-string'}}]</code>. Anthropic: khối <code>tool_use</code> bên trong <code>content</code> với <code>{id, name, input}</code> (object đã parse, không phải string). Chúng tôi parse arguments đã escape của OpenAI thành <code>input</code> có cấu trúc Anthropic mong đợi; chiều ngược lại re-stringify.</li>
  <li><strong>Tool results.</strong> OpenAI: tin nhắn riêng với <code>role: "tool"</code>, <code>tool_call_id</code>, <code>content</code>. Anthropic: khối <code>tool_result</code> bên trong content của tin nhắn <em>user</em> tiếp theo với <code>tool_use_id</code>. Tin nhắn <code>tool</code> liên tiếp của OpenAI được gộp thành một user Anthropic với nhiều <code>tool_result</code>.</li>
  <li><strong>Hình ảnh.</strong> OpenAI: <code>{type:'image_url', image_url:{url}}</code>. Anthropic: <code>{type:'image', source:{type:'base64',media_type,data}}</code> hoặc URL-source. Chúng tôi phát hiện URL <code>data:</code> và chuyển đổi; URL trần qua như URL-source.</li>
  <li><strong>Văn bản thuần.</strong> OpenAI dùng string; Anthropic chấp nhận string <em>hoặc</em> mảng một phần tử <code>[{type:'text', text}]</code>. Chúng tôi dùng cái đơn giản hơn.</li>
</ul>

<h3>Cái gì không được dịch</h3>
<ul>
  <li><strong>Sự kiện streaming.</strong> Chúng tôi xử lý JSON request/response, không phải stream SSE. Nếu có dump stream, tái tạo tin nhắn cuối trước.</li>
  <li><strong>Field riêng của nhà cung cấp.</strong> <code>logprobs</code> của OpenAI, <code>stop_sequences</code> của Anthropic, tham số sampling — sống ở top-level của request, không trong messages.</li>
  <li><strong>Hint cache-control.</strong> <code>cache_control: {type:'ephemeral'}</code> của Anthropic không có tương đương OpenAI. Sống sót qua OpenAI → Anthropic (không có nguồn), nhưng bị bỏ trong Anthropic → OpenAI.</li>
  <li><strong>Định nghĩa tool.</strong> <em>Schema</em> của tool (field <code>tools</code> trên request) sống ngoài mảng messages. Định dạng khác giữa các nhà cung cấp — chuyển đổi riêng.</li>
</ul>

<h3>Bẫy thường gặp</h3>
<ul>
  <li><strong>Escaping arguments OpenAI.</strong> <code>arguments</code> của OpenAI là string JSON-encoded, không phải object đã parse. Nếu hỏng (hiếm, xảy ra với model nhỏ), chúng tôi đặt vào <code>_raw</code> trong <code>input</code> Anthropic thay vì ném lỗi.</li>
  <li><strong>System top-level Anthropic.</strong> Trong OpenAI → Anthropic kết quả là <code>{system, messages}</code>. Nếu chỉ muốn mảng, dùng <code>.messages</code> — nhưng nhớ đính kèm <code>system</code> vào request API riêng.</li>
  <li><strong>Luân phiên nghiêm ngặt.</strong> Anthropic yêu cầu user/assistant luân phiên nghiêm ngặt (sau system tùy chọn). Bộ chuyển đổi nói chung giữ; nếu nguồn OpenAI có hai user liên tiếp, output Anthropic cũng có — và API sẽ từ chối. Merge trước.</li>
  <li><strong>Multi-modal trong OpenAI.</strong> Tin nhắn user OpenAI với hình ảnh dùng <em>content array</em> thay vì string. Chúng tôi xử lý; chỉ cần đảm bảo input của bạn parse được như JSON.</li>
  <li><strong>Quyền riêng tư.</strong> Không gì rời khỏi trang. Chuyển đổi JS thuần; không API key, không gọi network.</li>
</ul>
""",
        "hi": """
<h2>यह किसके लिए है?</h2>
<p>OpenAI की Chat Completions API और Anthropic की Messages API दोनों आपको multi-turn conversation भेजने देती हैं, लेकिन JSON को इतना अलग shape करती हैं कि provider switch करने पर prompts और tool-call traces cleanly drop in नहीं होते। Differences छोटे हैं (system message placement, tool-call vs tool-use, image block shape, role: 'tool' vs content में <code>tool_result</code>) लेकिन हर एक deadline के नीचे होने पर 10-minute rabbit hole है। यह converter translation handle करता है ताकि आप OpenAI conversation paste करें और Anthropic-shaped version back मिले (या उल्टा)।</p>

<h3>क्या translate होता है</h3>
<ul>
  <li><strong>System messages।</strong> OpenAI <code>role: "system"</code> के साथ regular message रखता है। Anthropic इसे top-level <code>system</code> field के रूप में request पर रखता है। हम move करते हैं और concatenate करते हैं अगर एक से ज़्यादा हों।</li>
  <li><strong>Tool calls (assistant side)।</strong> OpenAI: <code>tool_calls: [{id, type:'function', function:{name, arguments:'JSON-string'}}]</code>। Anthropic: assistant के <code>content</code> array के अंदर <code>tool_use</code> block <code>{id, name, input}</code> के साथ (parsed object, string नहीं)। हम OpenAI के escaped JSON arguments को structured <code>input</code> में parse करते हैं; reverse direction फिर से stringify करता है।</li>
  <li><strong>Tool results।</strong> OpenAI: separate message <code>role: "tool"</code>, <code>tool_call_id</code>, और <code>content</code> के साथ। Anthropic: next <em>user</em> message के content array के अंदर <code>tool_result</code> block <code>tool_use_id</code> के साथ। Consecutive OpenAI <code>tool</code> messages एक Anthropic user message में coalesce होते हैं जिसमें multiple <code>tool_result</code> blocks होते हैं।</li>
  <li><strong>Images।</strong> OpenAI: <code>{type:'image_url', image_url:{url}}</code>। Anthropic: <code>{type:'image', source:{type:'base64',media_type,data}}</code> या URL-source। हम <code>data:</code> URLs detect करते हैं और convert करते हैं; bare URLs URL-source images के रूप में pass through होते हैं।</li>
  <li><strong>Plain text content।</strong> OpenAI string use करता है; Anthropic string <em>और</em> one-element <code>[{type:'text', text}]</code> array दोनों accept करता है। हम जो simpler है वो use करते हैं।</li>
</ul>

<h3>क्या translate नहीं होता</h3>
<ul>
  <li><strong>Streaming events।</strong> यह converter request/response JSON handle करता है, SSE event streams नहीं। अगर आपके पास stream dump है, पहले full final message reconstruct करें।</li>
  <li><strong>Provider-specific fields।</strong> OpenAI के <code>logprobs</code>, Anthropic के <code>stop_sequences</code>, sampling parameters — ये request top-level पर रहते हैं, messages के अंदर नहीं।</li>
  <li><strong>Cache control hints।</strong> Anthropic के <code>cache_control: {type:'ephemeral'}</code> hints का कोई OpenAI equivalent नहीं है। OpenAI → Anthropic में survive करते हैं (कोई source attach करने को नहीं), लेकिन Anthropic → OpenAI में drop होते हैं।</li>
  <li><strong>Tool definitions।</strong> आपके tools का <em>schema</em> (request पर <code>tools</code> field) messages array के बाहर रहता है। हर provider का tool-definition shape अलग है — उन्हें अलग से convert करें।</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>OpenAI argument escaping।</strong> OpenAI का <code>arguments</code> JSON-encoded string है, parsed object नहीं। अगर malformed है (rare, छोटे models के साथ होता है), हम इसे throw करने के बजाय Anthropic <code>input</code> में <code>_raw</code> के नीचे डालते हैं।</li>
  <li><strong>Anthropic top-level system।</strong> OpenAI → Anthropic convert करते समय result <code>{system, messages}</code> है। अगर आप सिर्फ messages array चाहते हैं, <code>.messages</code> field use करें — लेकिन याद रखें <code>system</code> को अपने API request के साथ separately attach करना है।</li>
  <li><strong>Strict alternation।</strong> Anthropic strict alternation में user/assistant/user/assistant की मांग करता है (optional system के बाद)। Converter generally preserve करता है; अगर आपके OpenAI source में दो consecutive user messages हैं, तो Anthropic output में भी होंगे — और API reject करेगी। पहले merge करें।</li>
  <li><strong>OpenAI में multi-modal।</strong> Images के साथ OpenAI user message string के बजाय <em>content array</em> use करता है। हम handle करते हैं; बस make sure करें कि आपका input JSON parse करे।</li>
  <li><strong>Privacy।</strong> कुछ भी page से बाहर नहीं जाता। Conversion pure JavaScript है; कोई API keys नहीं, कोई network calls नहीं।</li>
</ul>
""",
        "sk": """
<h2>Načo to slúži?</h2>
<p>Chat Completions API od OpenAI a Messages API od Anthropicu obe umožňujú multi-turn konverzácie, ale formujú JSON dostatočne odlišne, aby prompty a tool-call trace nepasovali čisto pri prechode medzi providermi. Rozdiely sú malé (umiestnenie system správy, tool-call vs tool-use, tvar blokov obrázkov, role: 'tool' vs <code>tool_result</code> v content) ale každý je 10-minútová králičia diera, keď máš deadline. Tento konvertor robí preklad: vlož OpenAI konverzáciu a dostaneš Anthropic verziu (alebo naopak).</p>

<h3>Čo sa prekladá</h3>
<ul>
  <li><strong>System správy.</strong> OpenAI: bežná správa s <code>role: "system"</code>. Anthropic: top-level pole <code>system</code> na requeste. Presúvame a konkatenujeme ak ich je viac.</li>
  <li><strong>Tool-cally (strana assistanta).</strong> OpenAI: <code>tool_calls: [{id, type:'function', function:{name, arguments:'JSON-string'}}]</code>. Anthropic: blok <code>tool_use</code> vnútri <code>content</code> s <code>{id, name, input}</code> (sparsovaný objekt, nie string). Parsujeme escapované argumenty OpenAI do štruktúrovaného <code>input</code> pre Anthropic; opačný smer reserializuje.</li>
  <li><strong>Tool výsledky.</strong> OpenAI: samostatná správa s <code>role: "tool"</code>, <code>tool_call_id</code>, <code>content</code>. Anthropic: blok <code>tool_result</code> v content nasledujúcej <em>user</em> správy s <code>tool_use_id</code>. Po sebe idúce OpenAI <code>tool</code> správy sa zlučujú do jednej Anthropic user správy s viacerými <code>tool_result</code> blokmi.</li>
  <li><strong>Obrázky.</strong> OpenAI: <code>{type:'image_url', image_url:{url}}</code>. Anthropic: <code>{type:'image', source:{type:'base64',media_type,data}}</code> alebo URL-source. Detegujeme <code>data:</code> URL a konvertujeme; čisté URL prechádzajú ako URL-source.</li>
  <li><strong>Čistý text.</strong> OpenAI používa string; Anthropic akceptuje string <em>aj</em> jednoprvkové pole <code>[{type:'text', text}]</code>. Používame jednoduchšiu formu.</li>
</ul>

<h3>Čo sa neprekladá</h3>
<ul>
  <li><strong>Streamingové eventy.</strong> Riešime JSON request/response, nie SSE streamy. Pri dumpe streamu najprv zrekonštruuj finálnu správu.</li>
  <li><strong>Provider-špecifické polia.</strong> <code>logprobs</code> OpenAI, <code>stop_sequences</code> Anthropicu, sampling parametre — žijú na top-level requestu, nie v messages.</li>
  <li><strong>Cache-control hinty.</strong> <code>cache_control: {type:'ephemeral'}</code> Anthropicu nemá OpenAI ekvivalent. Prežíva OpenAI → Anthropic (žiadny zdroj), ale je odhodené pri Anthropic → OpenAI.</li>
  <li><strong>Definície toolov.</strong> <em>Schéma</em> tvojich toolov (pole <code>tools</code> na requeste) žije mimo poľa messages. Formát rôzny medzi providermi — konvertuj samostatne.</li>
</ul>

<h3>Časté pasce</h3>
<ul>
  <li><strong>Escapovanie argumentov OpenAI.</strong> <code>arguments</code> OpenAI je JSON-encoded string, nie sparsovaný objekt. Ak je pokazený (zriedka, stáva sa pri malých modeloch), namiesto hodenia chyby ho ukladáme do <code>_raw</code> v Anthropic <code>input</code>.</li>
  <li><strong>Anthropic top-level system.</strong> Pri OpenAI → Anthropic je výsledok <code>{system, messages}</code>. Ak chceš len pole, použi <code>.messages</code> — ale pamätaj pridať <code>system</code> k API requestu samostatne.</li>
  <li><strong>Striktná alternácia.</strong> Anthropic vyžaduje striktnú alternáciu user/assistant (po voliteľnom system). Konvertor to zvyčajne zachová; ak má tvoj OpenAI zdroj dve user správy za sebou, Anthropic výstup tiež — a API to odmietne. Najprv ich zlúč.</li>
  <li><strong>Multi-modal v OpenAI.</strong> OpenAI user správa s obrázkami používa <em>content array</em> namiesto stringu. Riešime to; len zabezpeč, že tvoj vstup sa parsuje ako JSON.</li>
  <li><strong>Súkromie.</strong> Nič neopustí stránku. Konverzia v čistom JS; žiadne API kľúče, žiadne sieťové volania.</li>
</ul>
""",
        "cs": """
<h2>K čemu to slouží?</h2>
<p>Chat Completions API od OpenAI a Messages API od Anthropicu obě umožňují multi-turn konverzace, ale formují JSON dostatečně odlišně, aby prompty a tool-call trace nepasovaly čistě při přechodu mezi providery. Rozdíly jsou malé (umístění system zprávy, tool-call vs tool-use, tvar bloků obrázků, role: 'tool' vs <code>tool_result</code> v content) ale každý je 10-minutová králičí nora, když máš deadline. Tenhle konvertor dělá překlad: vlož OpenAI konverzaci a dostaneš Anthropic verzi (nebo naopak).</p>

<h3>Co se překládá</h3>
<ul>
  <li><strong>System zprávy.</strong> OpenAI: běžná zpráva s <code>role: "system"</code>. Anthropic: top-level pole <code>system</code> na requestu. Přesouváme a konkatenujeme, pokud jich je víc.</li>
  <li><strong>Tool-cally (strana assistanta).</strong> OpenAI: <code>tool_calls: [{id, type:'function', function:{name, arguments:'JSON-string'}}]</code>. Anthropic: blok <code>tool_use</code> uvnitř <code>content</code> s <code>{id, name, input}</code> (sparsovaný objekt, ne string). Parsujeme escapované argumenty OpenAI do strukturovaného <code>input</code> pro Anthropic; opačný směr reserializuje.</li>
  <li><strong>Tool výsledky.</strong> OpenAI: samostatná zpráva s <code>role: "tool"</code>, <code>tool_call_id</code>, <code>content</code>. Anthropic: blok <code>tool_result</code> v content následující <em>user</em> zprávy s <code>tool_use_id</code>. Po sobě jdoucí OpenAI <code>tool</code> zprávy se slučují do jedné Anthropic user zprávy s více <code>tool_result</code> bloky.</li>
  <li><strong>Obrázky.</strong> OpenAI: <code>{type:'image_url', image_url:{url}}</code>. Anthropic: <code>{type:'image', source:{type:'base64',media_type,data}}</code> nebo URL-source. Detekujeme <code>data:</code> URL a konvertujeme; čisté URL procházejí jako URL-source.</li>
  <li><strong>Čistý text.</strong> OpenAI používá string; Anthropic akceptuje string <em>i</em> jednoprvkové pole <code>[{type:'text', text}]</code>. Používáme jednodušší formu.</li>
</ul>

<h3>Co se nepřekládá</h3>
<ul>
  <li><strong>Streamingové eventy.</strong> Řešíme JSON request/response, ne SSE streamy. U dumpu streamu nejprve zrekonstruuj finální zprávu.</li>
  <li><strong>Provider-specifická pole.</strong> <code>logprobs</code> OpenAI, <code>stop_sequences</code> Anthropicu, sampling parametry — žijí na top-level requestu, ne v messages.</li>
  <li><strong>Cache-control hinty.</strong> <code>cache_control: {type:'ephemeral'}</code> Anthropicu nemá OpenAI ekvivalent. Přežívá OpenAI → Anthropic (žádný zdroj), ale je odhozeno při Anthropic → OpenAI.</li>
  <li><strong>Definice toolů.</strong> <em>Schéma</em> tvých toolů (pole <code>tools</code> na requestu) žije mimo pole messages. Formát různý mezi providery — konvertuj samostatně.</li>
</ul>

<h3>Časté pasti</h3>
<ul>
  <li><strong>Escapování argumentů OpenAI.</strong> <code>arguments</code> OpenAI je JSON-encoded string, ne sparsovaný objekt. Pokud je rozbitý (zřídka, stává se u malých modelů), místo házení chyby ho ukládáme do <code>_raw</code> v Anthropic <code>input</code>.</li>
  <li><strong>Anthropic top-level system.</strong> Při OpenAI → Anthropic je výsledek <code>{system, messages}</code>. Pokud chceš jen pole, použij <code>.messages</code> — ale nezapomeň přidat <code>system</code> k API requestu samostatně.</li>
  <li><strong>Striktní alternace.</strong> Anthropic vyžaduje striktní alternaci user/assistant (po volitelném system). Konvertor to obvykle zachová; pokud má tvůj OpenAI zdroj dvě user zprávy po sobě, Anthropic výstup taky — a API to odmítne. Nejprve je sluč.</li>
  <li><strong>Multi-modal v OpenAI.</strong> OpenAI user zpráva s obrázky používá <em>content array</em> místo stringu. Řešíme to; jen zajisti, že tvůj vstup parsuje jako JSON.</li>
  <li><strong>Soukromí.</strong> Nic neopustí stránku. Konverze v čistém JS; žádné API klíče, žádná síťová volání.</li>
</ul>
""",
    },
    "related": ["chat-thread-viewer", "jsonl-viewer", "system-prompt-linter"],
    "howto": {"flow": "transform", "action": "convert", "noun": "messages"},
}
