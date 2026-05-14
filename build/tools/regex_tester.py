TOOL = {
    "slug": "regex-tester",
    "category": "developer",
    "icon": ".*",
    "tags": ["regex", "regular expression", "test", "match", "replace", "javascript"],
    "i18n": {
        "en": {
            "name": "Regex Tester",
            "tagline": "Test JavaScript regular expressions live. See matches, capture groups, and apply replacements as you type.",
            "description": "Free online JavaScript regex tester with live highlighting, capture groups, and replace mode. PCRE-compatible flags (g/i/m/s/u/y).",
        },
        "de": {
            "name": "Regex-Tester",
            "tagline": "JavaScript-Regex live testen. Treffer, Gruppen und Ersetzungen werden beim Tippen angezeigt.",
            "description": "Kostenloser JavaScript-Regex-Tester mit Live-Hervorhebung, Erfassungsgruppen und Ersetzungsmodus. PCRE-kompatible Flags.",
        },
        "es": {
            "name": "Probador de Regex",
            "tagline": "Prueba expresiones regulares de JavaScript en vivo. Coincidencias, grupos y reemplazos al instante.",
            "description": "Probador de regex JavaScript gratuito con resaltado en vivo, grupos de captura y modo reemplazo. Flags compatibles con PCRE.",
        },
        "fr": {
            "name": "Testeur Regex",
            "tagline": "Testez les expressions régulières JavaScript en direct. Correspondances, groupes de capture et remplacement instantanés.",
            "description": "Testeur regex JavaScript gratuit avec coloration en direct, groupes de capture et mode remplacement. Drapeaux compatibles PCRE.",
        },
        "it": {
            "name": "Tester Regex",
            "tagline": "Testa espressioni regolari JavaScript in tempo reale. Corrispondenze, gruppi di cattura e sostituzioni istantanee.",
            "description": "Tester regex JavaScript gratuito con evidenziazione live, gruppi di cattura e modalità sostituzione. Flag compatibili PCRE.",
        },
        "pt": {
            "name": "Testador de Regex",
            "tagline": "Teste regex de JavaScript ao vivo. Veja matches, grupos de captura e aplique substituições enquanto digita.",
            "description": "Testador de regex JavaScript gratuito com destaque ao vivo, grupos de captura e modo replace. Flags compatíveis com PCRE (g/i/m/s/u/y).",
        },
        "pl": {
            "name": "Tester Regex",
            "tagline": "Testuj regex JavaScript na żywo. Zobacz matche, grupy przechwytujące i aplikuj zamiany w trakcie pisania.",
            "description": "Darmowy online tester regex JavaScript z podświetlaniem na żywo, grupami przechwytującymi i trybem replace. Flagi zgodne z PCRE (g/i/m/s/u/y).",
        },
        "ja": {
            "name": "正規表現テスター",
            "tagline": "JavaScript の正規表現をライブテスト。マッチ、キャプチャグループ、置換結果を入力に応じて表示。",
            "description": "オンライン無料の JavaScript 正規表現テスター。ライブハイライト、キャプチャグループ表示、置換モードに対応。PCRE 互換のフラグ（g/i/m/s/u/y）。",
        },
        "nl": {"name": "Regex Tester", "tagline": "Test JavaScript regular expressions live. Zie matches, capture groups, en pas replacements toe terwijl je typt.", "description": "Gratis online JavaScript regex tester met live highlighting, capture groups en replace mode. PCRE-compatible flags (g/i/m/s/u/y)."},
        "tr": {"name": "Regex Tester", "tagline": "JavaScript düzenli ifadelerini canlı test et. Eşleşmeleri, capture gruplarını gör ve yazdıkça değiştirme uygula.", "description": "Canlı vurgulama, capture grupları ve değiştirme moduyla ücretsiz online JavaScript regex tester. PCRE uyumlu bayraklar (g/i/m/s/u/y)."},
        "id": {"name": "Regex Tester", "tagline": "Tes regex JavaScript secara langsung. Lihat match, capture group, dan terapkan replace sambil mengetik.", "description": "Regex tester online gratis. Tes regular expression JavaScript secara real-time terhadap teks sampel. Sorot semua match, lihat capture group dengan nomor dan nama, dan terapkan operasi replace sambil mengetik."},
        "vi": {"name": "Regex Tester", "tagline": "Test regex JavaScript trực tiếp. Xem match, capture group và áp dụng replace khi bạn gõ.", "description": "Regex tester miễn phí trực tuyến cho regex JavaScript. Xem match, capture group và áp dụng replace theo thời gian thực khi bạn gõ pattern và mẫu thử."},
        "hi": {"name": "Regex Tester", "tagline": "JavaScript regular expressions live test करें। Matches, capture groups देखें, और टाइप करते समय replacements लागू करें।", "description": "मुफ़्त ऑनलाइन JavaScript regex tester जिसमें live highlighting, capture groups, और replace mode है। PCRE-compatible flags (g/i/m/s/u/y)।"},
        "sk": {"name": 'Regex Tester', "tagline": 'Testuj JavaScript regular expressions naživo. Pozri matches, capture groups a aplikuj replacements pri písaní.', "description": 'Bezplatný online regex tester. Testuj JavaScript regulárne výrazy naživo, pozri si matches a capture groups, aplikuj replacements. Všetko naživo pri písaní. Beží v prehliadači.'},
        "cs": {"name": 'Regex Tester', "tagline": 'Testuj JavaScript regular expressions naživo. Podívej se na matches, capture groups a aplikuj replacements při psaní.', "description": 'Zdarma online regex tester. Testuj JavaScript regulární výrazy naživo, podívej se na matches a capture groups, aplikuj replacements. Vše naživo při psaní. Běží v prohlížeči.'},
    },
    "body": """
<div class="tool-card">
  <label>Pattern</label>
  <div style="display:flex;gap:0.5rem;align-items:center">
    <span style="color:var(--text-muted);font-family:ui-monospace,monospace">/</span>
    <input type="text" id="re-pattern" placeholder="\\b(\\w+)@(\\w+\\.\\w+)\\b" oninput="reRun()" style="flex:1">
    <span style="color:var(--text-muted);font-family:ui-monospace,monospace">/</span>
    <input type="text" id="re-flags" value="g" oninput="reRun()" style="width:90px" placeholder="gimsuy">
  </div>
  <div class="meta" style="margin-top:0.5rem">Flags: <code>g</code> global · <code>i</code> case-insensitive · <code>m</code> multi-line · <code>s</code> dotAll · <code>u</code> unicode · <code>y</code> sticky</div>
</div>
<div class="tool-card">
  <label>Test string</label>
  <textarea id="re-input" oninput="reRun()" placeholder="Reach me at hello@example.com or admin@toolhub.software" spellcheck="false">Reach me at hello@example.com or admin@toolhub.software</textarea>
</div>
<div class="tool-card">
  <label>Highlighted matches</label>
  <pre class="output" id="re-highlight" style="word-break:break-word;white-space:pre-wrap"></pre>
  <div class="meta" id="re-meta"></div>
</div>
<div class="tool-card">
  <label>Capture groups</label>
  <div id="re-groups" class="output" style="font-size:0.88rem">{LBL_NO_INPUT}</div>
</div>
<div class="tool-card">
  <label>Replace</label>
  <input type="text" id="re-replace" placeholder="<a href=&quot;mailto:$&amp;&quot;>$&amp;</a>" oninput="reRun()">
  <div class="meta" style="margin-top:0.5rem">Use <code>$1</code>, <code>$2</code> for groups · <code>$&amp;</code> for the whole match · <code>$$</code> for literal $</div>
  <pre class="output" id="re-replaced" style="margin-top:0.75rem;word-break:break-word;white-space:pre-wrap">{LBL_NO_INPUT}</pre>
</div>
""",
    "script": """
<script>
function reEsc(s){ return s.replace(/[&<>]/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;'}[c])); }
function reRun(){
  const pat = document.getElementById('re-pattern').value;
  const flags = document.getElementById('re-flags').value;
  const input = document.getElementById('re-input').value;
  const replaceWith = document.getElementById('re-replace').value;
  const hi = document.getElementById('re-highlight');
  const groupsEl = document.getElementById('re-groups');
  const meta = document.getElementById('re-meta');
  const repl = document.getElementById('re-replaced');
  if (!pat){ hi.textContent = ''; meta.textContent = ''; groupsEl.textContent = '{LBL_NO_INPUT}'; repl.textContent = ''; return; }
  let regex;
  try { regex = new RegExp(pat, flags); }
  catch(e){ hi.classList.add('error'); hi.textContent = '✗ ' + e.message; meta.textContent = ''; groupsEl.textContent = ''; repl.textContent = ''; return; }
  hi.classList.remove('error');
  // Highlight matches
  let out = '';
  let last = 0;
  let count = 0;
  const groups = [];
  const useGlobal = regex.global;
  if (useGlobal){
    let m;
    while ((m = regex.exec(input)) !== null){
      out += reEsc(input.slice(last, m.index));
      out += '<mark style="background:var(--accent);color:#fff;padding:0 2px;border-radius:2px">' + reEsc(m[0] || '') + '</mark>';
      last = m.index + (m[0]?.length || 0);
      count++;
      groups.push({index: m.index, match: m[0], groups: m.slice(1)});
      if (m[0] === '') { regex.lastIndex++; if (regex.lastIndex > input.length) break; }
      if (count > 10000) break;
    }
    out += reEsc(input.slice(last));
  } else {
    const m = regex.exec(input);
    if (m){
      out = reEsc(input.slice(0, m.index)) + '<mark style="background:var(--accent);color:#fff;padding:0 2px;border-radius:2px">' + reEsc(m[0]) + '</mark>' + reEsc(input.slice(m.index + m[0].length));
      count = 1;
      groups.push({index: m.index, match: m[0], groups: m.slice(1)});
    } else {
      out = reEsc(input);
    }
  }
  hi.innerHTML = out || '<span style="color:var(--text-muted)">(no matches)</span>';
  meta.textContent = count + ' match' + (count === 1 ? '' : 'es');
  // Capture groups
  if (groups.length === 0){
    groupsEl.textContent = '(no matches)';
  } else {
    groupsEl.innerHTML = groups.slice(0, 50).map((g, i) =>
      'Match ' + (i+1) + ' at index ' + g.index + ':\\n' +
      '  full: ' + reEsc(g.match) +
      (g.groups.length ? '\\n' + g.groups.map((cg, j) => '  $' + (j+1) + ': ' + reEsc(cg ?? '<undefined>')).join('\\n') : '')
    ).join('\\n\\n');
  }
  // Replace
  if (replaceWith !== ''){
    try {
      const replaced = input.replace(new RegExp(pat, flags), replaceWith);
      repl.textContent = replaced;
    } catch(e){ repl.textContent = '✗ ' + e.message; }
  } else {
    repl.textContent = '(enter a replacement above)';
  }
}
document.addEventListener('DOMContentLoaded', reRun);
document.addEventListener('toolhub:prefill', function(e) {
  var input = document.getElementById('re-input');
  if (!input) return;
  input.value = e.detail.data;
  reRun();
});
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Regular expressions are dense and unforgiving. The way to write one that actually works is iteratively — pattern, sample text, see what matches, adjust. This tool gives you that loop in your browser using the JavaScript engine's native <code>RegExp</code>, plus capture-group inspection and a replacement preview. Patterns and inputs never leave the page.</p>

<h3>When to use it</h3>
<ul>
  <li>Validating user input (email-shaped, phone-shaped, postcode-shaped) and seeing exactly which inputs pass and fail.</li>
  <li>Parsing log lines, extracting fields, building log filters.</li>
  <li>Designing find-and-replace patterns before running them across a real codebase.</li>
  <li>Debugging a regex you copied from Stack Overflow that doesn't work — paste it here, see what it actually matches.</li>
</ul>

<h3>Common patterns</h3>
<ul>
  <li><code>\\b\\w+@\\w+\\.\\w+\\b</code> — email-ish</li>
  <li><code>^\\s*$</code> — empty/whitespace-only line (with <code>m</code> flag)</li>
  <li><code>(?&lt;year&gt;\\d{4})-(?&lt;month&gt;\\d{2})</code> — named capture groups</li>
  <li><code>(?:.*)</code> — non-capturing group</li>
  <li><code>(?=foo)</code> / <code>(?!foo)</code> — lookahead / negative lookahead</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>JavaScript ≠ PCRE.</strong> No <code>\\K</code>, no recursive patterns, lookbehind only since ES2018. Patterns from Perl, PHP, or Python often need adjustment.</li>
  <li><strong>Without <code>g</code> flag you get the first match only.</strong> Add <code>g</code> for "find all"; combine with <code>m</code> if anchors should match per-line.</li>
  <li><strong>Greedy vs lazy.</strong> <code>.*</code> grabs as much as possible; <code>.*?</code> grabs as little. The difference between matching <code>&lt;b&gt;hi&lt;/b&gt; and &lt;i&gt;there&lt;/i&gt;</code> as one block vs two.</li>
  <li><strong>Anchors at line vs string boundaries.</strong> <code>^</code> and <code>$</code> match string ends by default; with <code>m</code> flag they match each line.</li>
  <li><strong>Replacement specials.</strong> <code>$&amp;</code> is the whole match; <code>$1</code>, <code>$2</code>, … are capture groups; <code>$$</code> is a literal <code>$</code>. Forgetting that is a common source of "why is my regex eating my dollars".</li>
  <li><strong>Don't parse HTML with regex</strong> for anything serious. The classic warning is true: nested tags, comments, and CDATA need a real parser. Regex is fine for one-off log scraping or controlled inputs.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Regex é denso e implacável. A forma de escrever uma que realmente funcione é iterativa — pattern, texto de exemplo, ver o que casa, ajustar. Esta ferramenta te dá esse loop no navegador usando o <code>RegExp</code> nativo do JavaScript, mais inspeção de grupos de captura e preview de substituição. Patterns e entradas nunca saem da página.</p>

<h3>Quando usar</h3>
<ul>
  <li>Validar entrada do usuário (formato de e-mail, telefone, CEP) e ver exatamente quais entradas passam e quais falham.</li>
  <li>Fazer parsing de linhas de log, extrair campos, montar filtros de log.</li>
  <li>Desenhar patterns de find-and-replace antes de rodar contra um codebase de verdade.</li>
  <li>Debugar uma regex que você copiou do Stack Overflow e não funciona — cole aqui, veja o que ela realmente casa.</li>
</ul>

<h3>Patterns comuns</h3>
<ul>
  <li><code>\\b\\w+@\\w+\\.\\w+\\b</code> — formato de e-mail</li>
  <li><code>^\\s*$</code> — linha vazia/só whitespace (com flag <code>m</code>)</li>
  <li><code>(?&lt;year&gt;\\d{4})-(?&lt;month&gt;\\d{2})</code> — grupos de captura nomeados</li>
  <li><code>(?:.*)</code> — grupo não-capturante</li>
  <li><code>(?=foo)</code> / <code>(?!foo)</code> — lookahead / lookahead negativo</li>
</ul>

<h3>Pegadinhas comuns</h3>
<ul>
  <li><strong>JavaScript ≠ PCRE.</strong> Sem <code>\\K</code>, sem patterns recursivos, lookbehind só desde ES2018. Patterns de Perl, PHP ou Python frequentemente precisam de ajuste.</li>
  <li><strong>Sem a flag <code>g</code> você só pega o primeiro match.</strong> Adicione <code>g</code> para "encontrar todos"; combine com <code>m</code> se os anchors devem casar por linha.</li>
  <li><strong>Greedy vs lazy.</strong> <code>.*</code> pega o máximo possível; <code>.*?</code> pega o mínimo. A diferença entre casar <code>&lt;b&gt;hi&lt;/b&gt; e &lt;i&gt;there&lt;/i&gt;</code> como um bloco ou como dois.</li>
  <li><strong>Anchors em limites de linha vs string.</strong> <code>^</code> e <code>$</code> casam fim de string por padrão; com a flag <code>m</code> casam cada linha.</li>
  <li><strong>Especiais de replacement.</strong> <code>$&amp;</code> é o match inteiro; <code>$1</code>, <code>$2</code>, … são grupos de captura; <code>$$</code> é um <code>$</code> literal. Esquecer disso é fonte clássica de "por que minha regex está comendo meus dólares".</li>
  <li><strong>Não faça parsing de HTML com regex</strong> para nada sério. O aviso clássico é verdadeiro: tags aninhadas, comentários e CDATA precisam de um parser de verdade. Regex serve para scraping pontual ou entradas controladas.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Wyrażenia regularne są gęste i bezlitosne. Sposób na napisanie takiego, który faktycznie działa, jest iteracyjny — pattern, przykładowy tekst, zobacz, co się matchuje, popraw. To narzędzie daje ci tę pętlę w przeglądarce, używając natywnego <code>RegExp</code> silnika JavaScriptu, plus podgląd grup przechwytujących i podgląd zamiany. Patterny i input nigdy nie opuszczają strony.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Walidacja inputu użytkownika (kształt maila, telefonu, kodu pocztowego) i widzenie dokładnie, które inputy przechodzą, a które padają.</li>
  <li>Parsowanie linii loga, wyciąganie pól, budowa filtrów logów.</li>
  <li>Projektowanie patternów find-and-replace przed odpaleniem ich na realnym codebasie.</li>
  <li>Debug regexa skopiowanego ze Stack Overflow, który nie działa — wklej tu, zobacz, co faktycznie matchuje.</li>
</ul>

<h3>Typowe patterny</h3>
<ul>
  <li><code>\\b\\w+@\\w+\\.\\w+\\b</code> — w stylu maila</li>
  <li><code>^\\s*$</code> — pusta linia / sama whitespace (z flagą <code>m</code>)</li>
  <li><code>(?&lt;year&gt;\\d{4})-(?&lt;month&gt;\\d{2})</code> — nazwane grupy przechwytujące</li>
  <li><code>(?:.*)</code> — grupa nieprzechwytująca</li>
  <li><code>(?=foo)</code> / <code>(?!foo)</code> — lookahead / negative lookahead</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>JavaScript ≠ PCRE.</strong> Brak <code>\\K</code>, brak rekurencyjnych patternów, lookbehind dopiero od ES2018. Patterny z Perla, PHP albo Pythona często wymagają poprawki.</li>
  <li><strong>Bez flagi <code>g</code> dostajesz tylko pierwszy match.</strong> Dodaj <code>g</code> dla "znajdź wszystkie"; połącz z <code>m</code>, jeśli anchory mają matchować per linia.</li>
  <li><strong>Greedy vs lazy.</strong> <code>.*</code> zżera maksimum; <code>.*?</code> zżera minimum. Różnica między matchowaniem <code>&lt;b&gt;hi&lt;/b&gt; i &lt;i&gt;there&lt;/i&gt;</code> jako jeden blok vs dwa.</li>
  <li><strong>Anchory na granicach linii vs stringa.</strong> <code>^</code> i <code>$</code> matchują końce stringa domyślnie; z flagą <code>m</code> matchują każdą linię.</li>
  <li><strong>Specjalne znaki w replacement.</strong> <code>$&amp;</code> to cały match; <code>$1</code>, <code>$2</code>, … to grupy przechwytujące; <code>$$</code> to literalny <code>$</code>. Zapomnienie tego to klasyczne źródło "dlaczego mój regex zżera moje dolary".</li>
  <li><strong>Nie parsuj HTML-a regexem</strong> w niczym poważnym. Klasyczne ostrzeżenie jest prawdziwe: zagnieżdżone tagi, komentarze i CDATA wymagają prawdziwego parsera. Regex jest OK do jednorazowego scrapingu logów albo kontrolowanych inputów.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>正規表現は密度が高く、容赦のない表現言語です。実用に耐えるパターンを書く近道は反復作業です。パターンを書き、サンプルテキストを見て、マッチを確認し、調整する、その繰り返しです。本ツールはこのループをブラウザ内で提供し、JavaScript エンジンの <code>RegExp</code> をそのまま使い、キャプチャグループの中身や置換のプレビューも確認できます。パターンも入力もページの外には出ません。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>ユーザー入力（メール風、電話番号風、郵便番号風など）の検証で、どの入力が通り、どれが落ちるかを正確に確認したいとき。</li>
  <li>ログ行のパース、フィールド抽出、ログフィルタの作成。</li>
  <li>実コードベースに find-and-replace を流す前にパターンを下書きしたいとき。</li>
  <li>Stack Overflow からコピペした正規表現がうまく動かないときに、何が実際にマッチしているかを確認するとき。</li>
</ul>

<h3>よく使うパターン</h3>
<ul>
  <li><code>\\b\\w+@\\w+\\.\\w+\\b</code> — メール風</li>
  <li><code>^\\s*$</code> — 空白だけの行（<code>m</code> フラグと併用）</li>
  <li><code>(?&lt;year&gt;\\d{4})-(?&lt;month&gt;\\d{2})</code> — 名前付きキャプチャ</li>
  <li><code>(?:.*)</code> — 非キャプチャグループ</li>
  <li><code>(?=foo)</code> / <code>(?!foo)</code> — 先読み／否定先読み</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>JavaScript は PCRE と同じではありません。</strong> <code>\\K</code> や再帰パターンはなく、後読みが入ったのは ES2018 以降です。Perl、PHP、Python のパターンは調整が必要なことがあります。</li>
  <li><strong><code>g</code> フラグなしでは最初のマッチしか得られません。</strong> 「全部見つける」なら <code>g</code>、行ごとのアンカーが要るなら <code>m</code> も併用します。</li>
  <li><strong>greedy と lazy。</strong> <code>.*</code> は最大一致、<code>.*?</code> は最小一致です。<code>&lt;b&gt;hi&lt;/b&gt; and &lt;i&gt;there&lt;/i&gt;</code> を 1 ブロックとマッチするか、2 ブロックに分けるかが変わります。</li>
  <li><strong>アンカーは行か文字列か。</strong> 既定では <code>^</code> と <code>$</code> は文字列の先頭・末尾です。<code>m</code> フラグで行ごとに切り替わります。</li>
  <li><strong>置換の特殊シーケンス。</strong> <code>$&amp;</code> はマッチ全体、<code>$1</code>、<code>$2</code> … はキャプチャグループ、<code>$$</code> はリテラルの <code>$</code>。これを忘れると「正規表現がドル記号を食う」現象に悩まされがちです。</li>
  <li><strong>真面目な用途で HTML を正規表現でパースしないこと。</strong> 入れ子タグ、コメント、CDATA は真のパーサーが必要です。一回限りのログスクレイピングや管理された入力では正規表現でも問題ありません。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Regular expressions zijn dicht en onverbiddelijk. De manier om er één te schrijven die ook echt werkt is iteratief — patroon, sample-tekst, zie wat matcht, pas aan. Deze tool geeft je die loop in je browser via de native <code>RegExp</code> van de JavaScript-engine, plus capture-group inspectie en een replacement-preview. Patronen en inputs verlaten de pagina nooit.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>User input valideren (email-shaped, phone-shaped, postcode-shaped) en precies zien welke inputs passeren en falen.</li>
  <li>Log lines parsen, velden extraheren, log filters bouwen.</li>
  <li>Find-and-replace patronen ontwerpen voor je ze over een echte codebase draait.</li>
  <li>Een regex debuggen die je van Stack Overflow hebt gekopieerd en niet werkt — plak 'm hier, zie wat hij daadwerkelijk matcht.</li>
</ul>

<h3>Veelvoorkomende patronen</h3>
<ul>
  <li><code>\b\w+@\w+\.\w+\b</code> — email-ish</li>
  <li><code>^\s*$</code> — lege/whitespace-only regel (met <code>m</code>-flag)</li>
  <li><code>(?&lt;year&gt;\d{4})-(?&lt;month&gt;\d{2})</code> — named capture groups</li>
  <li><code>(?:.*)</code> — non-capturing group</li>
  <li><code>(?=foo)</code> / <code>(?!foo)</code> — lookahead / negative lookahead</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>JavaScript ≠ PCRE.</strong> Geen <code>\K</code>, geen recursive patterns, lookbehind pas sinds ES2018. Patronen uit Perl, PHP of Python hebben vaak aanpassing nodig.</li>
  <li><strong>Zonder <code>g</code>-flag krijg je alleen de eerste match.</strong> Voeg <code>g</code> toe voor "find all"; combineer met <code>m</code> als anchors per-line moeten matchen.</li>
  <li><strong>Greedy vs lazy.</strong> <code>.*</code> grijpt zoveel mogelijk; <code>.*?</code> zo weinig mogelijk. Het verschil tussen <code>&lt;b&gt;hi&lt;/b&gt; and &lt;i&gt;there&lt;/i&gt;</code> als één blok matchen of twee.</li>
  <li><strong>Anchors op line- vs string-grenzen.</strong> <code>^</code> en <code>$</code> matchen standaard string-einden; met <code>m</code>-flag matchen ze elke regel.</li>
  <li><strong>Replacement-specials.</strong> <code>$&amp;</code> is de hele match; <code>$1</code>, <code>$2</code>, … zijn capture groups; <code>$$</code> is een letterlijke <code>$</code>. Dat vergeten is een gangbare bron van "waarom eet mijn regex mijn dollars".</li>
  <li><strong>Parse geen HTML met regex</strong> voor iets serieus. De klassieke waarschuwing klopt: nested tags, comments en CDATA hebben een echte parser nodig. Regex is prima voor eenmalig log-scrapen of gecontroleerde inputs.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Düzenli ifadeler yoğun ve affetmezdir. Gerçekten çalışan birini yazmanın yolu yinelemelidir — desen, örnek metin, ne eşleştiğini gör, ayarla. Bu araç tarayıcında JavaScript motorunun yerel <code>RegExp</code>'ini kullanarak bu döngüyü, artı capture-group incelemesi ve replacement önizlemesini verir. Desenler ve girdiler sayfayı asla terk etmez.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Kullanıcı girişini doğrulama (e-posta şekilli, telefon şekilli, posta kodu şekilli) ve tam olarak hangi girdilerin geçtiğini ve başarısız olduğunu görme.</li>
  <li>Log satırlarını parse etme, alanlar çıkarma, log filtreleri kurma.</li>
  <li>Gerçek bir kod tabanı boyunca çalıştırmadan önce find-and-replace desenlerini tasarlama.</li>
  <li>Çalışmayan Stack Overflow'dan kopyaladığın bir regex'i debug etme — buraya yapıştır, gerçekte neyi eşleştirdiğini gör.</li>
</ul>

<h3>Yaygın desenler</h3>
<ul>
  <li><code>\b\w+@\w+\.\w+\b</code> — e-postaya benzer</li>
  <li><code>^\s*$</code> — boş/sadece-boşluk satırı (<code>m</code> bayrağı ile)</li>
  <li><code>(?&lt;year&gt;\d{4})-(?&lt;month&gt;\d{2})</code> — adlandırılmış capture grupları</li>
  <li><code>(?:.*)</code> — non-capturing grup</li>
  <li><code>(?=foo)</code> / <code>(?!foo)</code> — lookahead / negatif lookahead</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>JavaScript ≠ PCRE.</strong> <code>\K</code> yok, recursive desenler yok, lookbehind sadece ES2018'den beri. Perl, PHP veya Python'dan gelen desenler sıklıkla ayarlama gerektirir.</li>
  <li><strong><code>g</code> bayrağı olmadan sadece ilk eşleşmeyi alırsın.</strong> "Hepsini bul" için <code>g</code> ekle; çapalar satır başına eşleşmeli ise <code>m</code> ile birleştir.</li>
  <li><strong>Greedy - lazy.</strong> <code>.*</code> mümkün olduğu kadar çok yakalar; <code>.*?</code> mümkün olduğu kadar az yakalar. <code>&lt;b&gt;hi&lt;/b&gt; and &lt;i&gt;there&lt;/i&gt;</code>'ı tek blok veya iki blok olarak eşleştirme arasındaki fark.</li>
  <li><strong>Satır - string sınırlarında çapalar.</strong> <code>^</code> ve <code>$</code> varsayılan olarak string uçlarıyla eşleşir; <code>m</code> bayrağı ile her satırla eşleşir.</li>
  <li><strong>Replacement özellikleri.</strong> <code>$&amp;</code> tüm eşleşmedir; <code>$1</code>, <code>$2</code>, … capture gruplarıdır; <code>$$</code> literal <code>$</code>'dır. Bunu unutmak "neden regex'im dolarlarımı yiyor"un yaygın bir kaynağıdır.</li>
  <li><strong>Ciddi bir şey için regex ile HTML parse etme.</strong> Klasik uyarı doğrudur: iç içe tag'ler, yorumlar ve CDATA gerçek bir parser gerektirir.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Regex itu padat dan tidak memaafkan. Cara menulis regex yang benar-benar bekerja adalah secara iteratif — pattern, sample text, lihat apa yang cocok, sesuaikan. Tool ini memberi kamu loop tersebut di browser menggunakan <code>RegExp</code> native dari engine JavaScript, plus inspeksi capture group dan preview replacement. Pattern dan input tidak pernah meninggalkan halaman.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Memvalidasi input user (berbentuk email, berbentuk telepon, berbentuk kode pos) dan melihat persis input mana yang lolos dan gagal.</li>
  <li>Mem-parse baris log, mengekstrak field, membangun filter log.</li>
  <li>Mendesain pattern find-and-replace sebelum menjalankannya di codebase nyata.</li>
  <li>Men-debug regex yang kamu copy dari Stack Overflow yang tidak bekerja — paste di sini, lihat apa yang sebenarnya cocok.</li>
</ul>

<h3>Pattern umum</h3>
<ul>
  <li><code>\\b\\w+@\\w+\\.\\w+\\b</code> — mirip email</li>
  <li><code>^\\s*$</code> — baris kosong/hanya whitespace (dengan flag <code>m</code>)</li>
  <li><code>(?&lt;year&gt;\\d{4})-(?&lt;month&gt;\\d{2})</code> — named capture group</li>
  <li><code>(?:.*)</code> — non-capturing group</li>
  <li><code>(?=foo)</code> / <code>(?!foo)</code> — lookahead / negative lookahead</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>JavaScript ≠ PCRE.</strong> Tidak ada <code>\\K</code>, tidak ada pattern recursive, lookbehind hanya sejak ES2018. Pattern dari Perl, PHP, atau Python sering butuh penyesuaian.</li>
  <li><strong>Tanpa flag <code>g</code> kamu hanya dapat match pertama.</strong> Tambahkan <code>g</code> untuk "find all"; kombinasikan dengan <code>m</code> jika anchor harus cocok per baris.</li>
  <li><strong>Greedy vs lazy.</strong> <code>.*</code> mengambil sebanyak mungkin; <code>.*?</code> mengambil sesedikit mungkin. Perbedaan antara mencocokkan <code>&lt;b&gt;hi&lt;/b&gt; and &lt;i&gt;there&lt;/i&gt;</code> sebagai satu blok atau dua.</li>
  <li><strong>Anchor di batas baris vs string.</strong> <code>^</code> dan <code>$</code> default cocok dengan ujung string; dengan flag <code>m</code> mereka cocok dengan tiap baris.</li>
  <li><strong>Replacement special.</strong> <code>$&amp;</code> adalah seluruh match; <code>$1</code>, <code>$2</code>, … adalah capture group; <code>$$</code> adalah literal <code>$</code>. Lupa ini adalah sumber umum "kenapa regex saya memakan dolar saya".</li>
  <li><strong>Jangan parse HTML dengan regex</strong> untuk apa pun yang serius. Peringatan klasik itu benar: nested tag, comment, dan CDATA butuh parser asli. Regex oke untuk scraping log sekali pakai atau input terkontrol.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Viết regex là trial-and-error. Tool này cho phép bạn gõ pattern, gõ văn bản test và xem ngay match nào (cộng với capture group) trên mỗi keystroke. Cũng cho phép áp dụng replace với pattern thay thế. Tất cả chạy trong trình duyệt — không có server-side regex engine.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Tinh chỉnh pattern cho input form validation hoặc URL routing.</li>
  <li>Test một pattern khó với nhiều input mẫu trước khi commit nó.</li>
  <li>Áp dụng replace global trên text để clean up data trước khi import.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Catastrophic backtracking.</strong> Một số pattern (như <code>(a+)+</code> trên string không match) có thể hang trình duyệt với input lớn. Cảnh giác với nested quantifier.</li>
  <li><strong>Flag matter.</strong> Không có flag <code>g</code>, replace chỉ thay match đầu tiên. Không có <code>i</code>, regex case-sensitive.</li>
  <li><strong>Regex JS khác Java/Python.</strong> Lookbehind chỉ là ES2018+. Một số escape khác (như <code>\d</code>, <code>\w</code>) khớp khác nhau với Unicode tùy flag.</li>
</ul>
""",
        "hi": """
<h2>यह किसके लिए है?</h2>
<p>Regular expressions घना और बिना क्षमा वाला होता है। एक काम करने वाला लिखने का तरीका iterative है — pattern, sample text, देखें क्या match होता है, adjust करें। यह tool आपको वह loop आपके browser में देता है JavaScript engine के native <code>RegExp</code> का इस्तेमाल करके, साथ ही capture-group inspection और एक replacement preview। Patterns और inputs कभी page से बाहर नहीं जाते।</p>

<h3>कब इस्तेमाल करें</h3>
<ul>
  <li>User input को validate करना (email-shaped, phone-shaped, postcode-shaped) और देखना कि कौन से inputs pass और fail होते हैं।</li>
  <li>Log lines parse करना, fields निकालना, log filters बनाना।</li>
  <li>एक वास्तविक codebase पर चलाने से पहले find-and-replace patterns design करना।</li>
  <li>Stack Overflow से copy किया गया regex debug करना जो काम नहीं कर रहा — यहाँ paste करें, देखें यह वास्तव में क्या match करता है।</li>
</ul>

<h3>आम patterns</h3>
<ul>
  <li><code>\\b\\w+@\\w+\\.\\w+\\b</code> — email जैसा</li>
  <li><code>^\\s*$</code> — खाली/केवल-whitespace line (<code>m</code> flag के साथ)</li>
  <li><code>(?&lt;year&gt;\\d{4})-(?&lt;month&gt;\\d{2})</code> — named capture groups</li>
  <li><code>(?:.*)</code> — non-capturing group</li>
  <li><code>(?=foo)</code> / <code>(?!foo)</code> — lookahead / negative lookahead</li>
</ul>

<h3>आम गलतियाँ</h3>
<ul>
  <li><strong>JavaScript ≠ PCRE।</strong> कोई <code>\\K</code> नहीं, कोई recursive patterns नहीं, lookbehind केवल ES2018 से। Perl, PHP, या Python से patterns को अक्सर adjustment की ज़रूरत होती है।</li>
  <li><strong><code>g</code> flag के बिना आपको केवल पहला match मिलता है।</strong> "सब खोजें" के लिए <code>g</code> जोड़ें; यदि anchors को per-line match करना चाहिए तो <code>m</code> के साथ combine करें।</li>
  <li><strong>Greedy vs lazy।</strong> <code>.*</code> जितना संभव हो उतना पकड़ता है; <code>.*?</code> जितना कम संभव हो। <code>&lt;b&gt;hi&lt;/b&gt; and &lt;i&gt;there&lt;/i&gt;</code> को एक block बनाम दो के रूप में match करने का अंतर।</li>
  <li><strong>Line vs string boundaries पर anchors।</strong> <code>^</code> और <code>$</code> default में string ends को match करते हैं; <code>m</code> flag के साथ वे हर line को match करते हैं।</li>
  <li><strong>Replacement specials।</strong> <code>$&amp;</code> पूरा match है; <code>$1</code>, <code>$2</code>, … capture groups हैं; <code>$$</code> एक literal <code>$</code> है। यह भूलना "मेरा regex मेरे dollars क्यों खा रहा है" का एक आम स्रोत है।</li>
  <li><strong>HTML को regex से parse न करें</strong> किसी भी गंभीर चीज़ के लिए। क्लासिक चेतावनी सच है: nested tags, comments, और CDATA को एक real parser की ज़रूरत है। Regex one-off log scraping या controlled inputs के लिए ठीक है।</li>
</ul>
""",
        "sk": """

<h2>Načo to slúži?</h2>
<p>Test JavaScript regulárnych výrazov naživo. Píšeš pattern, vidíš matches v inpute, capture groups a vieš naživo aplikovať replacement. Užitočné pri ladení regex-u, ktorý potom použiješ v kóde alebo find-and-replace v editore.</p>

<h3>Kedy to použiť</h3>
<ul>
  <li>Príprava regex-u na validáciu form-u (e-mail, postal code, identifikátor).</li>
  <li>Extrakcia dát z neštandardného textu (logy, scraped HTML).</li>
  <li>Search-and-replace v dokumente alebo v code-base-e.</li>
  <li>Učenie sa regex-u — uvidíš naživo, čo robí každý kúsok patternu.</li>
</ul>

<h3>Časté chyby</h3>
<ul>
  <li><strong>Flags.</strong> <code>g</code> = global, <code>i</code> = case-insensitive, <code>m</code> = multiline, <code>s</code> = dotall, <code>u</code> = unicode.</li>
  <li><strong>Bez <code>g</code> flagu vráti len prvý match.</strong> V real kóde to často chceš s globálnym.</li>
  <li><strong>$ a ^ s newline-mi.</strong> Bez <code>m</code> flagu sú $/^ start/end celého stringu, nie riadku.</li>
  <li><strong>Catastrophic backtracking.</strong> Pattern ako <code>(a+)+b</code> môže mať exponenciálnu zložitosť na vstupe <code>aaaaaaaa...</code>.</li>
  <li><strong>JS vs. PCRE.</strong> JS regex je trochu odlišný od PCRE (PHP) alebo RE2 (Go) — niektoré features sa neprenášajú.</li>
</ul>
""",
        "cs": """

<h2>K čemu to slouží?</h2>
<p>Test JavaScript regulárních výrazů živě. Píšeš pattern, vidíš matches v inputu, capture groups a umíš živě aplikovat replacement. Užitečné při ladění regexu, který pak použiješ v kódu nebo find-and-replace v editoru.</p>

<h3>Kdy to použít</h3>
<ul>
  <li>Příprava regexu na validaci formu (e-mail, postal code, identifikátor).</li>
  <li>Extrakce dat z nestandardního textu (logy, scraped HTML).</li>
  <li>Search-and-replace v dokumentu nebo v code-base.</li>
  <li>Učení se regexu — uvidíš živě, co dělá každý kousek patternu.</li>
</ul>

<h3>Časté chyby</h3>
<ul>
  <li><strong>Flags.</strong> <code>g</code> = global, <code>i</code> = case-insensitive, <code>m</code> = multiline, <code>s</code> = dotall, <code>u</code> = unicode.</li>
  <li><strong>Bez <code>g</code> flagu vrátí jen první match.</strong> V real kódu to často chceš s globálním.</li>
  <li><strong>$ a ^ s newliny.</strong> Bez <code>m</code> flagu jsou $/^ start/end celého stringu, ne řádku.</li>
  <li><strong>Catastrophic backtracking.</strong> Pattern jako <code>(a+)+b</code> může mít exponenciální složitost na vstupu <code>aaaaaaaa...</code>.</li>
  <li><strong>JS vs. PCRE.</strong> JS regex je trochu odlišný od PCRE (PHP) nebo RE2 (Go) — některé features se nepřenášejí.</li>
</ul>
""",
    },
    "related": ["json-formatter", "text-diff", "email-validator"],
    "howto": {"flow": "transform", "action": "validate","noun": "regex"},
}
