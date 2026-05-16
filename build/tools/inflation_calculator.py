TOOL = {
    "slug": "inflation-calculator",
    "category": "finance",
    "icon": "📉",
    "tags": ["inflation", "purchasing-power", "real-value", "cpi", "calculator", "personal-finance"],
    "i18n": {
        "en": {
            "name": "Inflation Calculator",
            "tagline": "See how inflation erodes purchasing power. Enter amount + years + inflation rate → real value today (or future). Useful for raises, retirement targets, savings goals.",
            "description": "Free in-browser inflation calculator. Enter a starting amount, a start year and end year (or number of years), and an annual inflation rate (default 3% — or supply your country's actual rate). See: equivalent purchasing power in today's money (or future money), cumulative inflation %, and a year-by-year erosion table. Switch direction: 'what's £100 today worth in 10 years' OR 'what was £100 in 2010 worth now'. All math runs in your browser — no government API, you control the rate.",
        },
        "de": {"name": "Inflationsrechner", "tagline": "Sieh, wie Inflation Kaufkraft auffrisst. Betrag + Jahre + Inflationsrate → realer Wert heute (oder in der Zukunft). Nützlich für Gehaltserhöhung, Renten- und Sparziele.", "description": "Kostenloser Inflationsrechner im Browser. Startbetrag, Start- und Endjahr (oder Anzahl Jahre) und jährliche Inflationsrate eingeben (Standard 3% — oder eigener Landeswert). Erhalte den entsprechenden Wert in heutigem (oder zukünftigem) Geld, kumulierte Inflation in %, und eine Jahres-Erosionstabelle. Richtung umschaltbar: „was sind 100 € heute in 10 Jahren wert“ oder „was waren 100 € von 2010 heute wert“. Alle Berechnungen im Browser — keine Behörden-API, du kontrollierst den Wert."},
        "es": {"name": "Calculadora de Inflación", "tagline": "Mira cómo la inflación erosiona el poder adquisitivo. Importe + años + tasa de inflación → valor real hoy (o en el futuro). Útil para subidas, objetivos de jubilación y ahorro.", "description": "Calculadora gratuita de inflación en el navegador. Introduce un importe inicial, un año de inicio y un año final (o número de años), y la tasa anual de inflación (3% por defecto — o aporta la real de tu país). Obtén el poder adquisitivo equivalente en dinero de hoy (o del futuro), la inflación acumulada en %, y una tabla año a año de la erosión. Cambia de dirección: «¿cuánto vale 100 € hoy dentro de 10 años?» o «¿cuánto valían 100 € en 2010 hoy?». Todo el cálculo se ejecuta en tu navegador — sin APIs de gobierno, tú controlas la tasa."},
        "fr": {"name": "Calculatrice d'Inflation", "tagline": "Voyez comment l'inflation érode le pouvoir d'achat. Montant + années + taux d'inflation → valeur réelle aujourd'hui (ou demain). Utile pour augmentations, objectifs retraite, épargne.", "description": "Calculatrice d'inflation gratuite en navigateur. Saisissez un montant de départ, une année de début et une année de fin (ou un nombre d'années), et un taux d'inflation annuel (3% par défaut — ou le taux réel de votre pays). Obtenez le pouvoir d'achat équivalent en euros d'aujourd'hui (ou de demain), l'inflation cumulée en %, et un tableau année par année de l'érosion. Direction inversable : « combien valent 100 € d'aujourd'hui dans 10 ans » OU « combien valaient 100 € de 2010 aujourd'hui ». Tout dans votre navigateur — pas d'API publique, vous contrôlez le taux."},
        "it": {"name": "Calcolatore di Inflazione", "tagline": "Vedi come l'inflazione erode il potere d'acquisto. Importo + anni + tasso d'inflazione → valore reale oggi (o futuro). Utile per aumenti, obiettivi pensionistici, risparmio.", "description": "Calcolatore di inflazione gratuito nel browser. Inserisci un importo iniziale, un anno di partenza e un anno finale (o un numero di anni), e un tasso d'inflazione annuo (3% di default — o il tasso reale del tuo paese). Ottieni il potere d'acquisto equivalente in euro di oggi (o di domani), l'inflazione cumulata in %, e una tabella anno per anno dell'erosione. Direzione invertibile: «quanto valgono 100 € di oggi tra 10 anni» OPPURE «quanto valevano 100 € del 2010 oggi». Tutto nel browser — niente API ISTAT, controlli tu il tasso."},
        "pt": {"name": "Calculadora de Inflação", "tagline": "Veja como a inflação corrói o poder de compra. Valor + anos + taxa de inflação → valor real hoje (ou no futuro). Útil para reajustes, metas de aposentadoria, poupança.", "description": "Calculadora de inflação gratuita no navegador. Informe um valor inicial, um ano de início e um ano final (ou número de anos), e uma taxa anual de inflação (3% padrão — ou forneça a real do seu país). Veja o poder de compra equivalente em dinheiro de hoje (ou do futuro), a inflação acumulada em %, e uma tabela ano a ano da erosão. Direção invertível: «quanto valem R$100 hoje em 10 anos» OU «quanto valiam R$100 em 2010 hoje». Todo o cálculo roda no navegador — sem API do IBGE, você controla a taxa."},
        "pl": {"name": "Kalkulator Inflacji", "tagline": "Zobacz, jak inflacja zjada siłę nabywczą. Kwota + lata + stopa inflacji → realna wartość dziś (lub w przyszłości). Przydatne dla podwyżek, celów emerytalnych, oszczędności.", "description": "Darmowy kalkulator inflacji w przeglądarce. Wpisz kwotę początkową, rok startowy i końcowy (albo liczbę lat) oraz roczną stopę inflacji (domyślnie 3% — albo własna stopa twojego kraju). Otrzymasz odpowiednią siłę nabywczą w pieniądzu dzisiejszym (lub przyszłym), inflację skumulowaną w %, oraz tabelę erozji rok po roku. Przełączalny kierunek: „ile warte jest 100 zł dziś za 10 lat“ LUB „ile warte było 100 zł w 2010 dzisiaj“. Wszystkie obliczenia w przeglądarce — bez API GUS, sam kontrolujesz stopę."},
        "ja": {"name": "インフレ計算機", "tagline": "インフレが購買力をどれだけ削るかを可視化。金額 + 年数 + インフレ率 → 今日（または将来）の実質価値。昇給・退職資金・貯蓄目標に。", "description": "ブラウザ完結の無料インフレ計算ツール。金額、開始年・終了年（または年数）、年率インフレ率（既定 3% — または各国の実値）を入力。今日（または将来）の購買力換算、累積インフレ %、年ごとの価値減衰表を表示。方向は切替可：「今日の 100 円は 10 年後にどれだけか」「2010 年の 100 円は今いくらか」。政府 API は使わず、レートを自分で指定。すべてブラウザで完結。"},
        "nl": {"name": "Inflatie Calculator", "tagline": "Zie hoe inflatie de koopkracht uitholt. Bedrag + jaren + inflatiepercentage → reële waarde vandaag (of toekomst). Handig voor loonsverhoging, pensioendoelen, spaardoelen.", "description": "Gratis inflatiecalculator in de browser. Voer een beginbedrag, een startjaar en eindjaar (of aantal jaren) en een jaarlijks inflatiepercentage in (standaard 3% — of het cijfer van je eigen land). Zie de equivalente koopkracht in geld van vandaag (of de toekomst), cumulatieve inflatie in %, en een jaar-voor-jaar erosietabel. Schakelbare richting: «wat is € 100 vandaag waard over 10 jaar» OF «wat was € 100 in 2010 nu waard». Alles in je browser — geen overheids-API, jij bepaalt het tarief."},
        "tr": {"name": "Enflasyon Hesaplayıcı", "tagline": "Enflasyonun alım gücünü nasıl erittiğini gör. Tutar + yıl + enflasyon oranı → bugünkü (veya gelecekteki) reel değer. Zam, emeklilik hedefi, birikim için faydalı.", "description": "Tarayıcıda ücretsiz enflasyon hesaplayıcı. Başlangıç tutarı, başlangıç ve bitiş yılı (veya yıl sayısı) ve yıllık enflasyon oranı (varsayılan %3 — veya kendi ülkenin gerçek oranı) gir. Bugünkü (veya gelecekteki) eşdeğer alım gücünü, kümülatif enflasyonu %, ve yıl yıl erozyon tablosunu gör. Yön değiştirilebilir: «bugün 100 TL 10 yıl sonra ne kadar» VEYA «2010'da 100 TL bugün ne kadar». Tüm hesaplama tarayıcıda — devlet API'si yok, oranı sen kontrol ediyorsun."},
        "id": {"name": "Kalkulator Inflasi", "tagline": "Lihat bagaimana inflasi menggerus daya beli. Jumlah + tahun + tingkat inflasi → nilai riil hari ini (atau masa depan). Berguna untuk kenaikan gaji, target pensiun, tujuan tabungan.", "description": "Kalkulator inflasi gratis di browser. Masukkan jumlah awal, tahun mulai dan tahun akhir (atau jumlah tahun), dan tingkat inflasi tahunan (default 3% — atau angka resmi negaramu). Lihat daya beli ekivalen dalam uang hari ini (atau masa depan), inflasi kumulatif %, dan tabel erosi tahun demi tahun. Arah bisa dibalik: «berapa Rp 100 hari ini dalam 10 tahun» ATAU «berapa Rp 100 tahun 2010 hari ini». Semua kalkulasi di browser — tanpa API pemerintah, kamu kontrol tingkatnya."},
        "vi": {"name": "Máy tính Lạm Phát", "tagline": "Xem lạm phát bào mòn sức mua thế nào. Số tiền + số năm + tỷ lệ lạm phát → giá trị thực hôm nay (hoặc tương lai). Hữu ích cho tăng lương, mục tiêu hưu trí, tiết kiệm.", "description": "Máy tính lạm phát miễn phí trên trình duyệt. Nhập số tiền ban đầu, năm bắt đầu và năm kết thúc (hoặc số năm), và tỷ lệ lạm phát hàng năm (mặc định 3% — hoặc tỷ lệ thực của quốc gia bạn). Xem sức mua tương đương theo tiền hôm nay (hoặc tương lai), lạm phát tích lũy %, và bảng bào mòn theo từng năm. Đổi chiều: «100 ngàn hôm nay đáng bao nhiêu sau 10 năm» HOẶC «100 ngàn năm 2010 đáng bao nhiêu hôm nay». Tất cả tính toán trên trình duyệt — không API chính phủ, bạn kiểm soát tỷ lệ."},
        "hi": {"name": "Inflation Calculator", "tagline": "देखें inflation purchasing power को कैसे erode करता है। Amount + years + inflation rate → real value today (या future में)। Raises, retirement targets, savings goals के लिए useful।", "description": "मुफ़्त in-browser inflation calculator। Starting amount, start year और end year (या number of years), और annual inflation rate डालें (default 3% — या अपने देश की actual rate)। देखें: equivalent purchasing power today's money में (या future money में), cumulative inflation %, और year-by-year erosion table। Direction switch करें: 'आज के ₹100 10 साल बाद कितने होंगे' या '2010 के ₹100 आज कितने'। सारा math आपके browser में चलता है — कोई government API नहीं, rate आप control करते हैं।"},
        "sk": {"name": "Kalkulačka inflácie", "tagline": "Pozri sa, ako inflácia žerie kúpnu silu. Suma + roky + miera inflácie → reálna hodnota dnes (alebo v budúcnosti). Užitočné pri zvyšovaní platu, dôchodkových cieľoch, sporení.", "description": "Bezplatná kalkulačka inflácie v prehliadači. Zadaj počiatočnú sumu, počiatočný a koncový rok (alebo počet rokov) a ročnú mieru inflácie (východisko 3 % — alebo skutočná hodnota tvojej krajiny). Dostaneš ekvivalentnú kúpnu silu v dnešných peniazoch (alebo budúcich), kumulovanú infláciu v %, a tabuľku erózie rok po roku. Smer prepínateľný: „koľko stojí 100 € dnes o 10 rokov“ ALEBO „koľko stálo 100 € v roku 2010 dnes“. Všetky výpočty v prehliadači — bez API úradu, sám si nastavíš sadzbu."},
        "cs": {"name": "Kalkulačka inflace", "tagline": "Podívej se, jak inflace ujídá kupní sílu. Částka + roky + míra inflace → reálná hodnota dnes (nebo v budoucnu). Užitečné pro zvyšování platu, důchodové cíle, spoření.", "description": "Bezplatná kalkulačka inflace v prohlížeči. Zadej počáteční částku, počáteční a koncový rok (nebo počet let) a roční míru inflace (výchozí 3 % — nebo skutečná hodnota tvojí země). Dostaneš ekvivalentní kupní sílu v dnešních penězích (nebo budoucích), kumulovanou inflaci v %, a tabulku eroze rok po roce. Směr přepínatelný: „kolik stojí 100 Kč dnes za 10 let“ NEBO „kolik stálo 100 Kč v roce 2010 dnes“. Všechny výpočty v prohlížeči — bez API úřadu, sazbu si nastavíš sám."},
    },
    "body": """
<div class="tool-card">
  <div class="inf-disclaimer">Inflation rates vary by country and year. This tool uses a single assumed rate — for precise historical figures, consult your national statistics office (BLS, ONS, Eurostat, etc).</div>
  <div class="row-2col">
    <div>
      <label>Direction</label>
      <select id="inf-dir" onchange="infRun()">
        <option value="future" selected>Today → Future (forecast)</option>
        <option value="past">Past → Today (historical look-back)</option>
      </select>
    </div>
    <div>
      <label>Currency symbol</label>
      <input type="text" id="inf-cur" maxlength="4" value="$" oninput="infRun()">
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Amount</label>
      <input type="number" id="inf-amount" step="any" min="0" value="1000" oninput="infRun()">
    </div>
    <div>
      <label>Years</label>
      <input type="number" id="inf-years" step="1" min="1" max="100" value="20" oninput="infRun()">
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Inflation preset</label>
      <select id="inf-preset" onchange="infPreset()">
        <option value="2.5">Conservative — 2.5%</option>
        <option value="3" selected>Long-term avg — 3%</option>
        <option value="5">High-inflation era — 5%</option>
        <option value="7">Recent (2022-era) — 7%</option>
        <option value="">Custom</option>
      </select>
    </div>
    <div>
      <label>Annual inflation rate (%)</label>
      <input type="number" id="inf-rate" step="0.01" min="0" value="3" oninput="infCustom(); infRun()">
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Sync with URL</label>
      <select id="inf-sync" onchange="infRun()">
        <option value="off" selected>Off</option>
        <option value="on">Save state in URL fragment</option>
      </select>
    </div>
    <div></div>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="inf-out" class="output"></div>
</div>
""",
    "script": """
<style>
.inf-disclaimer{background:var(--bg-elev);border-left:3px solid #c97a4a;padding:0.5rem 0.8rem;border-radius:0 6px 6px 0;font-size:0.78rem;color:var(--text-muted);margin-bottom:0.8rem;line-height:1.4}
.inf-hero{background:var(--accent);color:#fff;padding:1rem 1.2rem;border-radius:8px;text-align:center;margin-bottom:0.8rem}
.inf-hero .inf-big{font-family:ui-monospace,monospace;font-size:1.8rem;font-weight:700;line-height:1.1}
.inf-hero .inf-sub{font-size:0.82rem;opacity:0.9;margin-top:0.3rem;line-height:1.35}
.inf-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:0.6rem;margin-bottom:0.8rem}
.inf-stat{background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;padding:0.7rem 0.85rem}
.inf-stat .inf-num{font-family:ui-monospace,monospace;font-size:1.1rem;font-weight:600;color:var(--accent);word-break:break-all}
.inf-stat .inf-num.neg{color:#c97a4a}
.inf-stat .inf-lbl{font-size:0.74rem;color:var(--text-muted);margin-top:0.15rem}
.inf-chart-wrap{background:var(--bg-elev);border:1px solid var(--border);border-radius:6px;padding:0.6rem;margin-bottom:0.8rem}
.inf-chart-wrap svg{display:block;width:100%;height:auto}
.inf-chart-legend{display:flex;gap:1rem;font-size:0.75rem;color:var(--text-muted);margin-top:0.4rem;flex-wrap:wrap}
.inf-chart-legend span::before{content:'';display:inline-block;width:10px;height:10px;border-radius:2px;margin-right:0.4rem;vertical-align:middle}
.inf-chart-legend .inf-l-v::before{background:var(--accent)}
.inf-chart-legend .inf-l-b::before{background:#888}
.inf-tab{width:100%;border-collapse:collapse;font-family:ui-monospace,monospace;font-size:0.78rem}
.inf-tab th,.inf-tab td{padding:0.3rem 0.45rem;border-bottom:1px solid var(--border);text-align:right}
.inf-tab th{color:var(--text-muted);font-weight:600;background:var(--bg-elev);position:sticky;top:0}
.inf-tab th:first-child,.inf-tab td:first-child{text-align:left;color:var(--text-muted)}
.inf-tab-wrap{max-height:340px;overflow:auto;border:1px solid var(--border);border-radius:6px}
</style>
<script>
function infFmt(n, cur){
  if(!isFinite(n)) return '—';
  return cur + Math.round(n).toLocaleString('en-US');
}
function infFmt2(n, cur){
  if(!isFinite(n)) return '—';
  return cur + (Math.round(n * 100) / 100).toLocaleString('en-US', {minimumFractionDigits:2, maximumFractionDigits:2});
}
function infCustom(){
  // If the rate is edited directly, dropdown should switch to "Custom"
  const r = document.getElementById('inf-rate').value;
  const sel = document.getElementById('inf-preset');
  const exists = Array.from(sel.options).some(o => o.value === String(parseFloat(r)));
  sel.value = exists ? String(parseFloat(r)) : '';
}
function infPreset(){
  const v = document.getElementById('inf-preset').value;
  if(v !== ''){
    document.getElementById('inf-rate').value = v;
    infRun();
  }
}
function infCompute(amount, years, rate, dir){
  // dir = 'future': today's amount → future nominal cost of same basket
  //   future_cost = amount × (1+r)^t  (you'd need this much nominal $ in the future)
  //   real_value  = amount / (1+r)^t  (what today's amount buys in tomorrow's money,
  //                                    expressed in today's purchasing power) — wait, simpler:
  //   For "Today → Future", the user is asking "how much will the same basket cost",
  //   and conversely "what is the real value of today's $ at that point" — we report both.
  // dir = 'past': past amount → today's equivalent purchasing power
  //   today_equivalent = amount × (1+r)^t
  const rows = [];
  const factor = Math.pow(1 + rate, years);
  for(let y = 0; y <= years; y++){
    const f = Math.pow(1 + rate, y);
    if(dir === 'future'){
      // Each future year: nominal cost of the same basket (rises);
      //                   real value of original $ (falls)
      rows.push({
        year: y,
        nominalCost: amount * f,
        realValue: amount / f,
        cumInflation: (f - 1) * 100,
      });
    } else {
      // dir === 'past': year 0 = past year; year `years` = today.
      // Show how the same basket's price grows from past → today.
      rows.push({
        year: y,
        nominalCost: amount * f,
        realValue: amount * f / factor, // expressed in today's money as fraction of growth
        cumInflation: (f - 1) * 100,
      });
    }
  }
  return rows;
}
function infChart(rows, cur, dir, amount){
  if(rows.length < 2) return '';
  const W = 600, H = 200, padL = 50, padR = 8, padT = 12, padB = 22;
  // For 'future': plot real value (purchasing power decline) of today's $
  // For 'past':   plot nominal cost growth (basket price)
  const series = dir === 'future' ? rows.map(r => r.realValue) : rows.map(r => r.nominalCost);
  const maxV = Math.max(...series, amount);
  const minV = 0;
  const xs = i => padL + (i / (rows.length - 1)) * (W - padL - padR);
  const ys = v => H - padB - ((v - minV) / (maxV - minV || 1)) * (H - padT - padB);
  const pts = ['M ' + xs(0) + ' ' + ys(series[0])];
  series.forEach((v, i) => { if(i > 0) pts.push('L ' + xs(i) + ' ' + ys(v)); });
  // Baseline = original amount (for "future" the today value reference; for "past" the past value)
  const baseY = ys(amount);
  const baseLine = `<line x1="${padL}" y1="${baseY}" x2="${W-padR}" y2="${baseY}" stroke="#888" stroke-width="1" stroke-dasharray="3,3"/>`;
  // Fill under line
  const fill = pts.join(' ') + ` L ${xs(rows.length-1)} ${ys(0)} L ${xs(0)} ${ys(0)} Z`;
  // Axis ticks
  const ticks = [0, Math.floor((rows.length-1)/2), rows.length - 1];
  const tickLabels = ticks.map(t => `<text x="${xs(t)}" y="${H-6}" text-anchor="middle" fill="var(--text-muted)" font-size="10">${dir === 'future' ? '+' + t + 'y' : 'y' + t}</text>`).join('');
  const yLabels = [maxV, maxV/2, 0].map(v => `<text x="${padL-4}" y="${ys(v)+3}" text-anchor="end" fill="var(--text-muted)" font-size="10">${cur}${Math.round(v).toLocaleString('en-US')}</text>`).join('');
  const lineLabel = dir === 'future' ? 'Real value of today\\'s ' + cur + Math.round(amount).toLocaleString('en-US') : 'Cost of same basket';
  return `
    <svg viewBox="0 0 ${W} ${H}" preserveAspectRatio="none" role="img" aria-label="Inflation chart">
      <rect x="${padL}" y="${padT}" width="${W-padL-padR}" height="${H-padT-padB}" fill="transparent" stroke="var(--border)"/>
      <path d="${fill}" fill="var(--accent)" opacity="0.2"/>
      <path d="${pts.join(' ')}" fill="none" stroke="var(--accent)" stroke-width="2"/>
      ${baseLine}
      ${tickLabels}
      ${yLabels}
    </svg>
    <div class="inf-chart-legend">
      <span class="inf-l-v">${lineLabel}</span>
      <span class="inf-l-b">Original amount</span>
    </div>
  `;
}
function infSyncUrl(){
  const sync = document.getElementById('inf-sync').value;
  if(sync !== 'on'){ if(location.hash) history.replaceState(null, '', location.pathname); return; }
  const p = new URLSearchParams();
  ['inf-dir','inf-amount','inf-years','inf-rate','inf-cur'].forEach(id => p.set(id, document.getElementById(id).value));
  history.replaceState(null, '', '#' + p.toString());
}
function infReadUrl(){
  if(!location.hash) return;
  const p = new URLSearchParams(location.hash.slice(1));
  ['inf-dir','inf-amount','inf-years','inf-rate','inf-cur'].forEach(id => {
    if(p.has(id)){ const el = document.getElementById(id); if(el) el.value = p.get(id); }
  });
  infCustom();
  document.getElementById('inf-sync').value = 'on';
}
function infRun(){
  const dir = document.getElementById('inf-dir').value;
  const amount = parseFloat(document.getElementById('inf-amount').value) || 0;
  const years = Math.max(1, parseInt(document.getElementById('inf-years').value, 10) || 0);
  const ratePct = parseFloat(document.getElementById('inf-rate').value) || 0;
  const rate = ratePct / 100;
  const cur = document.getElementById('inf-cur').value || '';
  const out = document.getElementById('inf-out');
  if(amount <= 0){ out.textContent = '{LBL_NO_INPUT}'; return; }
  const rows = infCompute(amount, years, rate, dir);
  const final = rows[rows.length - 1];
  const cumInflationPct = final.cumInflation;
  let heroBig, heroSub, plLabel, plValue, plClass;
  if(dir === 'future'){
    // Future: today's amount loses purchasing power; same basket costs more
    const realToday = final.realValue;
    const lossPct = ((amount - realToday) / amount) * 100;
    heroBig = infFmt(realToday, cur);
    heroSub = `Real purchasing power of ${infFmt(amount, cur)} in ${years} years at ${ratePct}% annual inflation. Same basket will cost ${infFmt(final.nominalCost, cur)} then.`;
    plLabel = 'Purchasing-power loss';
    plValue = '−' + lossPct.toFixed(1) + '%';
    plClass = 'neg';
  } else {
    // Past: amount from N years ago is worth more today (in nominal)
    const todayEquiv = final.nominalCost;
    heroBig = infFmt(todayEquiv, cur);
    heroSub = `${infFmt(amount, cur)} from ${years} years ago, in today's money at ${ratePct}% annual inflation. The same basket cost the same back then.`;
    plLabel = 'Nominal growth';
    plValue = '+' + cumInflationPct.toFixed(1) + '%';
    plClass = '';
  }
  // Table
  const tableRows = rows.map(r => {
    const yLbl = dir === 'future' ? ('+' + r.year + 'y') : ('y' + r.year);
    return `<tr><td>${yLbl}</td><td>${infFmt2(r.nominalCost, cur)}</td><td>${infFmt2(r.realValue, cur)}</td><td>${r.cumInflation.toFixed(2)}%</td></tr>`;
  }).join('');
  out.innerHTML = `
    <div class="inf-hero">
      <div class="inf-big">${heroBig}</div>
      <div class="inf-sub">${heroSub}</div>
    </div>
    <div class="inf-grid">
      <div class="inf-stat"><div class="inf-num">${cumInflationPct.toFixed(1)}%</div><div class="inf-lbl">Cumulative inflation</div></div>
      <div class="inf-stat"><div class="inf-num ${plClass}">${plValue}</div><div class="inf-lbl">${plLabel}</div></div>
      <div class="inf-stat"><div class="inf-num">${(Math.pow(1 + rate, 1) - 1) * 100 === 0 ? '—' : (Math.log(2) / Math.log(1 + rate)).toFixed(1) + ' yrs'}</div><div class="inf-lbl">Time for prices to double</div></div>
      <div class="inf-stat"><div class="inf-num">${ratePct}%</div><div class="inf-lbl">Annual rate (your input)</div></div>
    </div>
    <div class="inf-chart-wrap">${infChart(rows, cur, dir, amount)}</div>
    <div><strong>Year-by-year</strong></div>
    <div class="inf-tab-wrap" style="margin-top:0.4rem">
      <table class="inf-tab">
        <thead><tr><th>Year</th><th>Basket cost</th><th>${dir === 'future' ? "Real value of today's " + cur : "Value (today's " + cur + ")"}</th><th>Cum. inflation</th></tr></thead>
        <tbody>${tableRows}</tbody>
      </table>
    </div>
  `;
  infSyncUrl();
}
document.addEventListener('DOMContentLoaded', () => { infReadUrl(); infRun(); });
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Inflation is the quiet tax on every dollar that doesn't earn interest. Wages that look like raises don't always keep up; "safe" cash savings shrink in purchasing power over time; a retirement target set in today's money needs to grow each year just to stand still. This tool puts a real number on that erosion: enter an amount, a time horizon, and an inflation rate, and see what the same money actually <em>buys</em> at the other end.</p>

<h3>The math</h3>
<p>Future cost of the same basket: <code>basket_today × (1 + rate)^years</code>. Real value (purchasing power) of today's amount in N years: <code>amount ÷ (1 + rate)^years</code>. Cumulative inflation: <code>(1 + rate)^years − 1</code>, expressed as percent.</p>

<h3>The Rule of 72 for inflation</h3>
<p>Prices roughly double every <code>72 ÷ inflation_rate%</code> years. At 3% inflation, the basket doubles in about 24 years; at 7%, in just 10 years. This is why early-career raises and long-horizon savings rates matter more than people think — the second doubling is bigger than the first in absolute terms.</p>

<h3>What rate to use?</h3>
<ul>
  <li><strong>Long-term average</strong>: most developed economies have averaged 2–3% over the last 50 years.</li>
  <li><strong>Recent (post-COVID) era</strong>: 5–8% spikes were common in 2022, falling back since.</li>
  <li><strong>Emerging markets</strong>: Brazil ~5%, Turkey >30% in 2024, Argentina >100%. National statistics agencies publish the official CPI/HICP series.</li>
  <li><strong>Your personal inflation</strong> may differ — rent, healthcare, and education typically outpace headline CPI; electronics and clothing often lag.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Headline CPI is an average.</strong> Your basket isn't average. Retirees with high healthcare exposure typically experience inflation above headline; young adults with mostly housing exposure can be much higher still in renter-heavy cities.</li>
  <li><strong>Wage inflation ≠ price inflation.</strong> A 4% raise in a 5% inflation year is a real-terms pay cut.</li>
  <li><strong>"Inflation-protected" savings have limits.</strong> Inflation-linked bonds (TIPS, I-Bonds, ILBs) track an official index — useful but not perfect coverage for your basket.</li>
  <li><strong>Compounding works both ways.</strong> Just like savings, inflation compounds: 3% for 30 years is +143% cumulative, not 90%.</li>
  <li><strong>The "doubling" intuition.</strong> Tell yourself the year prices will double — it's a more visceral framing than abstract percentages.</li>
</ul>

<h3>Pairs with</h3>
<ul>
  <li><strong>compound-interest-calculator</strong> — see whether your savings rate outruns inflation.</li>
  <li><strong>retirement-projection</strong> — inflation-adjusted retirement target.</li>
  <li><strong>roi-calculator</strong> — convert nominal ROI to real ROI.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>Inflation ist die stille Steuer auf jeden Euro, der keinen Zins erwirtschaftet. „Gehaltserhöhungen“ halten oft nicht Schritt; Bargeld auf dem Konto verliert real; ein Rentenziel in heutigen Euro muss jährlich wachsen, nur um stehenzubleiben. Dieses Tool macht die Erosion greifbar.</p>
<h3>Die Formel</h3>
<pre>Zukunftspreis = Heute × (1+r)^t
Realwert heutigen Geldes = Betrag / (1+r)^t
Kumulierte Inflation = (1+r)^t − 1</pre>
<h3>72er-Regel</h3>
<p>Preise verdoppeln sich etwa alle <code>72 / Inflationsrate %</code> Jahre. Bei 3 % → 24 Jahre, bei 7 % → 10 Jahre.</p>
<h3>Welche Rate?</h3>
<ul>
<li><strong>Langfristiger Schnitt EUR-Raum</strong>: 2–2,5 % (Inflationsziel EZB).</li>
<li><strong>Post-COVID</strong>: 6–10 % in DE/AT 2022, seitdem rückläufig.</li>
<li><strong>Persönliche Inflation</strong> weicht ab — Miete und Energie liegen oft über VPI.</li>
</ul>
<h3>Kombiniert mit</h3>
<ul>
<li><strong>compound-interest-calculator</strong> — Sparrate vs. Inflation prüfen.</li>
<li><strong>retirement-projection</strong> — inflationsbereinigtes Rentenziel.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>La inflación es el impuesto silencioso sobre cada euro que no genera interés. Los aumentos no siempre la siguen; el efectivo en cuenta pierde poder real; una meta de jubilación en euros de hoy tiene que crecer cada año solo para quedarse igual. Esta herramienta pone un número concreto a esa erosión.</p>
<h3>La fórmula</h3>
<pre>Precio futuro = Hoy × (1+r)^t
Valor real del dinero de hoy = Importe / (1+r)^t
Inflación acumulada = (1+r)^t − 1</pre>
<h3>Regla del 72</h3>
<p>Los precios se duplican cada <code>72 / tasa%</code> años. A 3 % → 24 años; a 7 % → 10 años.</p>
<h3>¿Qué tasa usar?</h3>
<ul>
<li><strong>Media a largo plazo</strong> en zona euro: 2–2,5 % (objetivo BCE).</li>
<li><strong>Post-COVID</strong>: 8–10 % en ES 2022, bajando desde entonces.</li>
<li><strong>Tu inflación personal</strong> puede diferir — alquiler y energía suelen ir por encima del IPC general.</li>
</ul>
<h3>Se combina con</h3>
<ul>
<li><strong>compound-interest-calculator</strong> — ¿tu rentabilidad supera la inflación?</li>
<li><strong>retirement-projection</strong> — objetivo de jubilación ajustado.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>L'inflation est l'impôt silencieux sur chaque euro qui ne rapporte rien. Les augmentations de salaire ne suivent pas toujours ; les liquidités perdent en pouvoir d'achat ; un objectif de retraite en euros d'aujourd'hui doit croître chaque année juste pour rester sur place. Cet outil chiffre cette érosion.</p>
<h3>La formule</h3>
<pre>Prix futur = aujourd'hui × (1+r)^t
Valeur réelle de l'argent d'aujourd'hui = montant / (1+r)^t
Inflation cumulée = (1+r)^t − 1</pre>
<h3>Règle de 72</h3>
<p>Les prix doublent tous les <code>72 / taux %</code> ans environ. À 3 % → 24 ans ; à 7 % → 10 ans.</p>
<h3>Quel taux utiliser ?</h3>
<ul>
<li><strong>Moyenne long terme zone euro</strong> : 2–2,5 % (cible BCE).</li>
<li><strong>Post-COVID</strong> : 5–6 % en FR en 2022, en baisse depuis.</li>
<li><strong>Votre inflation personnelle</strong> peut différer — loyer et énergie dépassent souvent l'IPC.</li>
</ul>
<h3>Se combine avec</h3>
<ul>
<li><strong>compound-interest-calculator</strong> — votre taux d'épargne bat-il l'inflation ?</li>
<li><strong>retirement-projection</strong> — objectif retraite corrigé.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>L'inflazione è la tassa silenziosa su ogni euro che non rende interesse. Gli aumenti di stipendio non sempre tengono il passo; il contante in conto perde potere d'acquisto; un obiettivo pensione in euro di oggi deve crescere ogni anno solo per restare fermo. Questo strumento dà un numero concreto a quell'erosione.</p>
<h3>La formula</h3>
<pre>Prezzo futuro = oggi × (1+r)^t
Valore reale del denaro di oggi = importo / (1+r)^t
Inflazione cumulata = (1+r)^t − 1</pre>
<h3>Regola del 72</h3>
<p>I prezzi raddoppiano ogni <code>72 / tasso %</code> anni circa. Al 3 % → 24 anni; al 7 % → 10 anni.</p>
<h3>Quale tasso usare?</h3>
<ul>
<li><strong>Media lungo termine area euro</strong>: 2–2,5 % (obiettivo BCE).</li>
<li><strong>Post-COVID</strong>: 8–11 % in IT nel 2022, in calo da allora.</li>
<li><strong>L'inflazione personale</strong> può differire — affitto ed energia spesso superano l'IPCA.</li>
</ul>
<h3>Si combina con</h3>
<ul>
<li><strong>compound-interest-calculator</strong> — il tuo rendimento batte l'inflazione?</li>
<li><strong>retirement-projection</strong> — obiettivo pensione corretto.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>A inflação é o imposto silencioso sobre cada real que não rende juros. Reajustes nem sempre acompanham; dinheiro parado na conta perde poder de compra; uma meta de aposentadoria em reais de hoje precisa crescer todo ano só para ficar parada. Esta ferramenta coloca um número concreto nessa erosão.</p>
<h3>A fórmula</h3>
<pre>Preço futuro = hoje × (1+r)^t
Valor real do dinheiro de hoje = valor / (1+r)^t
Inflação acumulada = (1+r)^t − 1</pre>
<h3>Regra do 72</h3>
<p>Os preços dobram a cada <code>72 / taxa %</code> anos aproximadamente. A 3 % → 24 anos; a 7 % → 10 anos.</p>
<h3>Qual taxa usar?</h3>
<ul>
<li><strong>Média de longo prazo no Brasil</strong>: 4–6 % (meta + tolerância do BC ~3,5 % ± 1,5 %).</li>
<li><strong>Anos recentes</strong>: 10 % em 2022, abaixo da meta em 2023.</li>
<li><strong>Sua inflação pessoal</strong> pode diferir — aluguel, mensalidade escolar e saúde costumam superar o IPCA.</li>
</ul>
<h3>Combina com</h3>
<ul>
<li><strong>compound-interest-calculator</strong> — sua poupança supera a inflação?</li>
<li><strong>retirement-projection</strong> — meta de aposentadoria ajustada.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Inflacja to cichy podatek od każdej złotówki, która nie pracuje. Podwyżki nie zawsze nadążają; gotówka na koncie traci realną wartość; cel emerytalny w dzisiejszych złotówkach musi rosnąć co roku tylko po to, by stać w miejscu. To narzędzie nadaje konkretną liczbę tej erozji.</p>
<h3>Wzory</h3>
<pre>Cena przyszła = dziś × (1+r)^t
Realna wartość dzisiejszych pieniędzy = kwota / (1+r)^t
Inflacja skumulowana = (1+r)^t − 1</pre>
<h3>Reguła 72</h3>
<p>Ceny podwajają się co <code>72 / stopa %</code> lat. Przy 3 % → 24 lata; przy 7 % → 10 lat.</p>
<h3>Jaką stopę przyjąć?</h3>
<ul>
<li><strong>Cel NBP</strong>: 2,5 % ± 1 p.p.</li>
<li><strong>Post-COVID</strong>: ponad 15 % w PL w 2023, spadek od tamtej pory.</li>
<li><strong>Twoja osobista inflacja</strong> może być wyższa — czynsz, energia, żywność często powyżej CPI ogółem.</li>
</ul>
<h3>Łączy się z</h3>
<ul>
<li><strong>compound-interest-calculator</strong> — czy oszczędzanie pobija inflację?</li>
<li><strong>retirement-projection</strong> — cel emerytalny po korekcie.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>インフレは「利息を生まないお金にかかる静かな税金」です。賃上げが追いつかないことも多く、口座に置いた現金は実質目減りし、今日の円建てで設定した老後資金目標も毎年成長させなければ実質後退します。本ツールはその侵食を具体的な数値で示します。</p>
<h3>計算式</h3>
<pre>将来価格 = 現在 × (1+r)^t
今日の金額の実質価値 = 金額 / (1+r)^t
累積インフレ率 = (1+r)^t − 1</pre>
<h3>72 の法則</h3>
<p>物価は <code>72 / インフレ率%</code> 年ごとに約 2 倍になります。3% → 24 年、7% → 10 年。</p>
<h3>どのレートを使う？</h3>
<ul>
<li><strong>日銀の物価目標</strong>: 2%（コア CPI 基準）。</li>
<li><strong>長期平均（日本）</strong>: 1990 年代以降は 0–1% 近辺で推移していたが、2022 年以降は 2–4% へ。</li>
<li><strong>個人インフレ</strong>はバスケット依存 — 食料・光熱費は CPI を上回ることが多い。</li>
</ul>
<h3>組み合わせ</h3>
<ul>
<li><strong>compound-interest-calculator</strong> ── 貯蓄利回りはインフレを超えるか？</li>
<li><strong>retirement-projection</strong> ── インフレ調整後の老後目標額。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Inflatie is de stille belasting op elke euro die geen rente verdient. Salarisverhogingen houden niet altijd gelijk; cash op je rekening verliest reëel; een pensioendoel in euro's van vandaag moet jaarlijks groeien om stil te blijven staan. Deze tool zet een concreet getal op die uitholling.</p>
<h3>De formule</h3>
<pre>Toekomstprijs = vandaag × (1+r)^t
Reële waarde van geld van vandaag = bedrag / (1+r)^t
Cumulatieve inflatie = (1+r)^t − 1</pre>
<h3>Regel van 72</h3>
<p>Prijzen verdubbelen elke <code>72 / inflatie %</code> jaar. Bij 3 % → 24 jaar; bij 7 % → 10 jaar.</p>
<h3>Welk tarief gebruiken?</h3>
<ul>
<li><strong>ECB-doel</strong>: 2 %.</li>
<li><strong>NL post-COVID</strong>: 10–14 % in 2022, gedaald sindsdien.</li>
<li><strong>Persoonlijke inflatie</strong> kan afwijken — huur en energie liggen vaak boven het CPI.</li>
</ul>
<h3>Combineert met</h3>
<ul>
<li><strong>compound-interest-calculator</strong> — verslaat je rendement de inflatie?</li>
<li><strong>retirement-projection</strong> — gecorrigeerd pensioendoel.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Enflasyon, faiz getirmeyen her liranın üzerine eklenen sessiz vergidir. Zamlar her zaman yetişmez; hesaptaki nakit reel olarak erir; bugünkü TL ile koyduğun emeklilik hedefi yerinde durmak için bile her yıl büyümek zorundadır. Bu araç bu erozyona somut bir sayı verir.</p>
<h3>Formüller</h3>
<pre>Gelecek fiyat = bugün × (1+r)^t
Bugünkü paranın reel değeri = tutar / (1+r)^t
Kümülatif enflasyon = (1+r)^t − 1</pre>
<h3>72 Kuralı</h3>
<p>Fiyatlar yaklaşık her <code>72 / enflasyon %</code> yılda bir ikiye katlanır. %3 → 24 yıl; %7 → 10 yıl; %30 → ~2,4 yıl.</p>
<h3>Hangi oranı kullanmalı?</h3>
<ul>
<li><strong>TR son yıllar</strong>: TÜFE 2022–2024'te %40–%85 bandında dalgalandı.</li>
<li><strong>TCMB hedefi</strong>: orta vade %5, ancak son yıllarda çok üzerinde.</li>
<li><strong>Kişisel enflasyon</strong> sepete bağlı — kira ve gıda genellikle manşet TÜFE'nin üzerinde.</li>
</ul>
<h3>Eşleşir</h3>
<ul>
<li><strong>compound-interest-calculator</strong> — birikimin enflasyonu geçiyor mu?</li>
<li><strong>retirement-projection</strong> — enflasyona göre düzeltilmiş hedef.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Inflasi adalah pajak senyap atas setiap rupiah yang tidak menghasilkan bunga. Kenaikan gaji tak selalu mengejarnya; uang tunai di rekening kehilangan daya beli; target pensiun dalam rupiah hari ini harus tumbuh tiap tahun hanya untuk berdiri di tempat. Tool ini memberi angka konkret untuk erosi itu.</p>
<h3>Formula</h3>
<pre>Harga masa depan = hari ini × (1+r)^t
Nilai riil uang hari ini = jumlah / (1+r)^t
Inflasi kumulatif = (1+r)^t − 1</pre>
<h3>Aturan 72</h3>
<p>Harga berlipat dua setiap <code>72 / tingkat %</code> tahun. Pada 3 % → 24 tahun; 7 % → 10 tahun.</p>
<h3>Pakai tingkat berapa?</h3>
<ul>
<li><strong>Target BI</strong>: ~3 % ± 1 %.</li>
<li><strong>ID 2022–2024</strong>: berada di kisaran 2–6 %.</li>
<li><strong>Inflasi pribadimu</strong> bisa berbeda — sewa, BBM, pendidikan kerap di atas IHK umum.</li>
</ul>
<h3>Pasangan</h3>
<ul>
<li><strong>compound-interest-calculator</strong> — apakah return-mu mengalahkan inflasi?</li>
<li><strong>retirement-projection</strong> — target pensiun yang dikoreksi inflasi.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Lạm phát là thuế thầm lặng đánh lên mọi đồng tiền không sinh lãi. Mức tăng lương không phải lúc nào cũng theo kịp; tiền mặt trong tài khoản giảm sức mua thực; mục tiêu hưu trí theo tiền hôm nay phải tăng mỗi năm chỉ để đứng yên. Công cụ này đặt một con số cụ thể cho sự bào mòn đó.</p>
<h3>Công thức</h3>
<pre>Giá tương lai = hôm nay × (1+r)^t
Giá trị thực của tiền hôm nay = số tiền / (1+r)^t
Lạm phát tích lũy = (1+r)^t − 1</pre>
<h3>Quy tắc 72</h3>
<p>Giá tăng gấp đôi sau khoảng <code>72 / tỷ lệ %</code> năm. Ở 3 % → 24 năm; 7 % → 10 năm.</p>
<h3>Dùng tỷ lệ nào?</h3>
<ul>
<li><strong>Mục tiêu CPI VN</strong>: ~4 %/năm (chỉ tiêu Quốc hội).</li>
<li><strong>Vài năm gần đây</strong>: dao động trong khoảng 2–4 %.</li>
<li><strong>Lạm phát cá nhân</strong> có thể khác — học phí, y tế, ăn uống thường cao hơn CPI chung.</li>
</ul>
<h3>Đi cùng</h3>
<ul>
<li><strong>compound-interest-calculator</strong> — tích lũy có vượt lạm phát không?</li>
<li><strong>retirement-projection</strong> — mục tiêu hưu trí đã điều chỉnh.</li>
</ul>
""",
        "hi": """
<h2>यह किसके लिए है?</h2>
<p>Inflation हर उस rupee पर silent tax है जो interest नहीं कमा रहा। Wages जो raises जैसी लगती हैं हमेशा keep up नहीं करतीं; "safe" cash savings समय के साथ purchasing power में सिकुड़ते हैं; today's money में set किया गया retirement target हर साल grow करना ज़रूरी है सिर्फ़ standstill पर रहने के लिए। यह tool उस erosion पर एक real number देता है।</p>
<h3>Math</h3>
<pre>भविष्य की कीमत = आज × (1+r)^t
आज के पैसे का real value = amount / (1+r)^t
Cumulative inflation = (1+r)^t − 1</pre>
<h3>72 का Rule</h3>
<p>Prices roughly हर <code>72 / inflation_rate%</code> साल में double हो जाती हैं। 3% inflation पर ~24 साल; 7% पर ~10 साल।</p>
<h3>कौन सी rate use करें?</h3>
<ul>
<li><strong>RBI target</strong>: 4% ± 2% (CPI inflation)।</li>
<li><strong>India recent</strong>: 2022–2024 में 4–7% band में।</li>
<li><strong>आपकी personal inflation</strong> भिन्न हो सकती है — rent, healthcare, education अक्सर headline CPI से ज़्यादा।</li>
</ul>
<h3>साथ pairs</h3>
<ul>
<li><strong>compound-interest-calculator</strong> — क्या आपकी savings rate inflation को beat कर रही है?</li>
<li><strong>retirement-projection</strong> — inflation-adjusted retirement target।</li>
</ul>
""",
        "sk": """
<h2>Načo to slúži?</h2>
<p>Inflácia je tichá daň na každé euro, ktoré nezarába úrok. Zvýšenia platu jej nemusia stačiť; hotovosť na účte reálne klesá; dôchodkový cieľ v dnešných eurách musí každý rok rásť len preto, aby zostal na mieste. Tento nástroj dáva eróziu do konkrétneho čísla.</p>
<h3>Vzorce</h3>
<pre>Budúca cena = dnes × (1+r)^t
Reálna hodnota dnešných peňazí = suma / (1+r)^t
Kumulovaná inflácia = (1+r)^t − 1</pre>
<h3>Pravidlo 72</h3>
<p>Ceny sa zdvojnásobia približne každých <code>72 / sadzba %</code> rokov. Pri 3 % → 24 rokov; pri 7 % → 10 rokov.</p>
<h3>Aký kurz použiť?</h3>
<ul>
<li><strong>Cieľ ECB</strong>: 2 %.</li>
<li><strong>SR post-COVID</strong>: 12–14 % v 2022, klesá od vtedy.</li>
<li><strong>Tvoja osobná inflácia</strong> sa môže líšiť — nájom a energia bývajú nad CPI.</li>
</ul>
<h3>Spolu s</h3>
<ul>
<li><strong>compound-interest-calculator</strong> — prekonáva tvoj výnos infláciu?</li>
<li><strong>retirement-projection</strong> — opravený dôchodkový cieľ.</li>
</ul>
""",
        "cs": """
<h2>K čemu to slouží?</h2>
<p>Inflace je tichá daň na každou korunu, která nenese úrok. Zvyšování mzdy jí nemusí stačit; hotovost na účtu reálně klesá; důchodový cíl v dnešních korunách musí každý rok růst jen proto, aby zůstal na místě. Tento nástroj dává erozi konkrétní číslo.</p>
<h3>Vzorce</h3>
<pre>Budoucí cena = dnes × (1+r)^t
Reálná hodnota dnešních peněz = částka / (1+r)^t
Kumulovaná inflace = (1+r)^t − 1</pre>
<h3>Pravidlo 72</h3>
<p>Ceny se zdvojnásobí přibližně každých <code>72 / sazba %</code> let. Při 3 % → 24 let; při 7 % → 10 let.</p>
<h3>Jakou sazbu použít?</h3>
<ul>
<li><strong>Cíl ČNB</strong>: 2 % ± 1 p.b.</li>
<li><strong>ČR post-COVID</strong>: 15–18 % v 2022–2023, klesá od té doby.</li>
<li><strong>Tvoje osobní inflace</strong> se může lišit — nájem a energie obvykle převyšují CPI.</li>
</ul>
<h3>Spolu s</h3>
<ul>
<li><strong>compound-interest-calculator</strong> — překonává tvůj výnos inflaci?</li>
<li><strong>retirement-projection</strong> — opravený důchodový cíl.</li>
</ul>
""",
    },
    "related": ["compound-interest-calculator", "retirement-projection", "roi-calculator", "currency-converter"],
    "howto": {"flow": "calculate", "action": "convert", "noun": "inflation-adjusted value"},
}
