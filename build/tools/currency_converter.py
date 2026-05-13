import json

# Hand-curated ECB euro reference rates + central-bank mid-rates as of 2025-04-30.
# EUR is the base. To convert A → B: amount_in_eur = amount / rates[A]; result = amount_in_eur * rates[B].
# These are a reference snapshot — exchange rates move continuously, so always verify with
# your bank or an FX desk before issuing an invoice or settling a payment.
_FX_REFERENCE = {
    "date": "2025-04-30",
    "source": "ECB euro reference rates + central-bank mid-rates",
    "base": "EUR",
    "groups": [
        {"key": "major", "label_en": "Major currencies", "codes": ["EUR", "USD", "GBP", "JPY", "CHF", "AUD", "CAD", "NZD", "CNY"]},
        {"key": "europe", "label_en": "Europe (non-euro)", "codes": ["SEK", "NOK", "DKK", "PLN", "CZK", "HUF", "RON", "BGN", "ISK", "TRY"]},
        {"key": "asia", "label_en": "Asia-Pacific", "codes": ["INR", "KRW", "SGD", "HKD", "TWD", "IDR", "PHP", "VND", "THB", "MYR"]},
        {"key": "americas", "label_en": "Americas", "codes": ["MXN", "BRL", "ARS", "CLP", "COP", "PEN"]},
        {"key": "mea", "label_en": "Middle East & Africa", "codes": ["AED", "SAR", "QAR", "KWD", "ILS", "EGP", "ZAR", "MAD"]},
    ],
    "rates": {
        # Major
        "EUR": 1.0,
        "USD": 1.13,
        "GBP": 0.85,
        "JPY": 161.5,
        "CHF": 0.93,
        "AUD": 1.77,
        "CAD": 1.57,
        "NZD": 1.91,
        "CNY": 8.21,
        # Europe (non-euro)
        "SEK": 10.95,
        "NOK": 11.85,
        "DKK": 7.46,
        "PLN": 4.28,
        "CZK": 25.10,
        "HUF": 405.0,
        "RON": 4.97,
        "BGN": 1.95583,  # pegged
        "ISK": 144.0,
        "TRY": 43.5,
        # Asia-Pacific
        "INR": 96.0,
        "KRW": 1620.0,
        "SGD": 1.48,
        "HKD": 8.80,
        "TWD": 36.7,
        "IDR": 18600.0,
        "PHP": 63.8,
        "VND": 29400.0,
        "THB": 37.5,
        "MYR": 4.95,
        # Americas
        "MXN": 22.10,
        "BRL": 6.40,
        "ARS": 1300.0,
        "CLP": 1070.0,
        "COP": 4750.0,
        "PEN": 4.20,
        # Middle East & Africa
        "AED": 4.15,
        "SAR": 4.24,
        "QAR": 4.12,
        "KWD": 0.347,
        "ILS": 4.12,
        "EGP": 57.5,
        "ZAR": 21.20,
        "MAD": 11.20,
    },
    "names": {
        "EUR": "Euro", "USD": "US Dollar", "GBP": "Pound Sterling", "JPY": "Japanese Yen",
        "CHF": "Swiss Franc", "AUD": "Australian Dollar", "CAD": "Canadian Dollar",
        "NZD": "New Zealand Dollar", "CNY": "Chinese Yuan Renminbi",
        "SEK": "Swedish Krona", "NOK": "Norwegian Krone", "DKK": "Danish Krone",
        "PLN": "Polish Zloty", "CZK": "Czech Koruna", "HUF": "Hungarian Forint",
        "RON": "Romanian Leu", "BGN": "Bulgarian Lev (EUR-pegged)", "ISK": "Icelandic Krona",
        "TRY": "Turkish Lira",
        "INR": "Indian Rupee", "KRW": "South Korean Won", "SGD": "Singapore Dollar",
        "HKD": "Hong Kong Dollar", "TWD": "New Taiwan Dollar", "IDR": "Indonesian Rupiah",
        "PHP": "Philippine Peso", "VND": "Vietnamese Dong", "THB": "Thai Baht",
        "MYR": "Malaysian Ringgit",
        "MXN": "Mexican Peso", "BRL": "Brazilian Real", "ARS": "Argentine Peso",
        "CLP": "Chilean Peso", "COP": "Colombian Peso", "PEN": "Peruvian Sol",
        "AED": "UAE Dirham", "SAR": "Saudi Riyal", "QAR": "Qatari Riyal",
        "KWD": "Kuwaiti Dinar", "ILS": "Israeli Shekel", "EGP": "Egyptian Pound",
        "ZAR": "South African Rand", "MAD": "Moroccan Dirham",
    },
}
_FX_JS = json.dumps(_FX_REFERENCE, ensure_ascii=False, separators=(",", ":"))

TOOL = {
    "slug": "currency-converter",
    "category": "math",
    "icon": "💱",
    "tags": ["currency", "converter", "exchange", "rate", "eur", "usd", "forex", "freelance"],
    "i18n": {
        "en": {
            "name": "Currency Converter",
            "tagline": "Convert between 50+ currencies with reference rates as of a known date. No live API, no tracking — useful for quick freelance estimates and quotes. Always verify before invoicing.",
            "description": "Free in-browser currency converter with hard-coded reference rates updated quarterly. Pick source + target currency, enter amount, see the converted value. Reference date is shown — always verify against your bank's actual rate before issuing an invoice. We deliberately don't fetch live rates: doing so would leak your queries to a third party. For accuracy in financial transactions, use your bank or an FX desk.",
        },
        "de": {
            "name": "Währungsrechner",
            "tagline": "Rechne zwischen 50+ Währungen mit Referenzkursen zu einem bekannten Datum um. Keine Live-API, kein Tracking — gut für schnelle Freelancer-Schätzungen und Angebote. Vor der Rechnung immer prüfen.",
            "description": "Kostenloser Währungsrechner im Browser mit fest hinterlegten Referenzkursen, quartalsweise aktualisiert. Quelle und Ziel auswählen, Betrag eingeben, Ergebnis ablesen. Das Referenzdatum wird angezeigt — vor dem Versand einer Rechnung immer mit dem tatsächlichen Bankkurs abgleichen. Wir holen bewusst keine Live-Kurse: das würde deine Anfragen an einen Dritten leaken. Für echte Zahlungen den Bank- oder FX-Kurs nutzen.",
        },
        "es": {
            "name": "Conversor de Divisas",
            "tagline": "Convierte entre 50+ divisas con tipos de referencia a una fecha conocida. Sin API en vivo, sin tracking — útil para estimaciones y presupuestos de freelance. Siempre verifica antes de facturar.",
            "description": "Conversor de divisas gratuito en el navegador con tipos de referencia incrustados, actualizados trimestralmente. Elige origen y destino, introduce el importe, ve el resultado. La fecha de referencia se muestra — verifica siempre con el tipo real de tu banco antes de emitir una factura. Deliberadamente no consultamos tipos en vivo: eso filtraría tus consultas a un tercero. Para transacciones reales, usa el tipo de tu banco o mesa de cambios.",
        },
        "fr": {
            "name": "Convertisseur de Devises",
            "tagline": "Convertissez entre 50+ devises avec des taux de référence à une date connue. Pas d'API live, pas de tracking — pratique pour devis et estimations freelance. Toujours vérifier avant facturation.",
            "description": "Convertisseur de devises gratuit dans le navigateur avec taux de référence intégrés, mis à jour chaque trimestre. Choisissez source et destination, entrez le montant, lisez le résultat. La date de référence est affichée — vérifiez toujours le taux réel de votre banque avant d'émettre une facture. Nous n'allons délibérément pas chercher de taux live : cela fuiterait vos requêtes vers un tiers. Pour les transactions réelles, utilisez votre banque ou un bureau de change.",
        },
        "it": {
            "name": "Convertitore di Valute",
            "tagline": "Converti tra 50+ valute con tassi di riferimento a una data nota. Niente API live, niente tracking — utile per stime e preventivi freelance. Verifica sempre prima di fatturare.",
            "description": "Convertitore di valute gratuito nel browser con tassi di riferimento integrati, aggiornati trimestralmente. Scegli origine e destinazione, inserisci l'importo, leggi il risultato. La data di riferimento è mostrata — verifica sempre col tasso reale della tua banca prima di emettere una fattura. Volutamente non recuperiamo tassi live: farebbe trapelare le tue richieste a terzi. Per i pagamenti reali, usa la banca o un FX desk.",
        },
        "pt": {
            "name": "Conversor de Moedas",
            "tagline": "Converte entre 50+ moedas com taxas de referência numa data conhecida. Sem API ao vivo, sem rastreamento — útil para estimativas e orçamentos freelance. Verifique sempre antes de faturar.",
            "description": "Conversor de moedas gratuito no navegador com taxas de referência incorporadas, atualizadas trimestralmente. Escolha origem e destino, digite o valor, veja o resultado. A data de referência é mostrada — verifique sempre com a taxa real do seu banco antes de emitir uma fatura. Deliberadamente não buscamos taxas ao vivo: isso vazaria suas consultas para terceiros. Para transações reais, use seu banco ou mesa de câmbio.",
        },
        "pl": {
            "name": "Przelicznik Walut",
            "tagline": "Przelicz między 50+ walutami z kursami referencyjnymi na znaną datę. Bez live API, bez śledzenia — przydatne dla freelancerów do szybkich wycen. Zawsze sprawdź przed wystawieniem faktury.",
            "description": "Darmowy przelicznik walut w przeglądarce z wbudowanymi kursami referencyjnymi, aktualizowanymi kwartalnie. Wybierz źródło i cel, wpisz kwotę, zobacz wynik. Data referencyjna jest widoczna — przed wystawieniem faktury zawsze sprawdź rzeczywisty kurs swojego banku. Celowo nie pobieramy kursów na żywo: to wyciekałoby twoje zapytania do strony trzeciej. Do realnych transakcji użyj banku lub kantoru.",
        },
        "ja": {
            "name": "通貨換算ツール",
            "tagline": "既知の基準日のリファレンスレートで 50 種以上の通貨を換算。ライブ API なし、トラッキングなし — フリーランスの見積もり概算に便利。請求前に必ず実勢レートと照合してください。",
            "description": "ブラウザだけで動く無料の通貨換算ツール。四半期ごとに更新されるリファレンスレートを内蔵。元通貨と目的通貨を選び、金額を入力すると結果が表示されます。基準日が表示されるので、請求書を出す前に必ず実際の銀行レートと照合してください。意図的にライブレートは取得していません — 取得するとあなたのクエリが第三者に漏れるためです。実際の決済には銀行や為替デスクのレートを使用してください。",
        },
        "nl": {
            "name": "Valutaconverter",
            "tagline": "Converteer tussen 50+ valuta's met referentiekoersen op een bekende datum. Geen live API, geen tracking — handig voor snelle freelance-inschattingen en offertes. Altijd verifiëren vóór factureren.",
            "description": "Gratis in-browser valutaconverter met ingebakken referentiekoersen, elk kwartaal bijgewerkt. Kies bron en doel, voer het bedrag in, lees het resultaat. De referentiedatum wordt getoond — controleer altijd de werkelijke koers van je bank voordat je een factuur stuurt. We halen bewust geen live koersen op: dat zou je queries naar een derde partij lekken. Voor echte transacties gebruik je je bank of FX-desk.",
        },
        "tr": {
            "name": "Döviz Çevirici",
            "tagline": "Bilinen bir tarihteki referans kurlarla 50+ döviz arasında çevir. Canlı API yok, takip yok — freelance tahminler ve teklifler için pratik. Faturalamadan önce mutlaka doğrula.",
            "description": "Üç ayda bir güncellenen, gömülü referans kurlu, tarayıcı içinde çalışan ücretsiz döviz çevirici. Kaynak ve hedef seç, tutarı gir, sonucu gör. Referans tarihi gösterilir — fatura kesmeden önce her zaman bankanın gerçek kurunu kontrol et. Canlı kur kasıtlı çekilmiyor: bu, sorgularınızı üçüncü tarafa sızdırırdı. Gerçek işlemler için bankanı veya bir döviz masasını kullan.",
        },
        "id": {
            "name": "Konverter Mata Uang",
            "tagline": "Konversi antara 50+ mata uang dengan kurs referensi per tanggal yang diketahui. Tanpa API live, tanpa tracking — berguna untuk estimasi dan quote freelance cepat. Selalu verifikasi sebelum invoice.",
            "description": "Konverter mata uang gratis di browser dengan kurs referensi tertanam, diperbarui kuartalan. Pilih asal dan tujuan, masukkan jumlah, lihat hasilnya. Tanggal referensi ditampilkan — selalu verifikasi dengan kurs aktual bankmu sebelum mengirim invoice. Kami sengaja tidak mengambil kurs live: melakukannya akan membocorkan query-mu ke pihak ketiga. Untuk transaksi nyata, gunakan bank atau FX desk.",
        },
        "vi": {
            "name": "Bộ Chuyển Đổi Tiền Tệ",
            "tagline": "Chuyển đổi giữa 50+ tiền tệ với tỷ giá tham chiếu tại ngày đã biết. Không API live, không tracking — hữu ích cho ước tính và báo giá freelance nhanh. Luôn xác minh trước khi xuất hóa đơn.",
            "description": "Bộ chuyển đổi tiền tệ miễn phí trong trình duyệt với tỷ giá tham chiếu nhúng sẵn, cập nhật hàng quý. Chọn nguồn và đích, nhập số tiền, xem kết quả. Ngày tham chiếu được hiển thị — luôn kiểm tra lại tỷ giá thực của ngân hàng trước khi gửi hóa đơn. Chúng tôi cố ý không lấy tỷ giá live: làm vậy sẽ rò rỉ truy vấn của bạn cho bên thứ ba. Với giao dịch thực, dùng ngân hàng hoặc bàn ngoại hối.",
        },
        "hi": {
            "name": "Currency Converter",
            "tagline": "50+ currencies के बीच एक ज्ञात date की reference rates के साथ convert करें। कोई live API नहीं, कोई tracking नहीं — freelance estimates और quotes के लिए उपयोगी। Invoicing से पहले हमेशा verify करें।",
            "description": "Free in-browser currency converter जिसमें hard-coded reference rates हैं, हर quarter update होती हैं। Source और target currency चुनें, amount डालें, converted value देखें। Reference date दिखाई देती है — invoice भेजने से पहले हमेशा अपने bank की actual rate से verify करें। हम जानबूझकर live rates नहीं लाते: वैसा करने से आपकी queries third party को leak हो जातीं। Financial transactions की accuracy के लिए अपना bank या FX desk इस्तेमाल करें।",
        },
        "sk": {
            "name": "Prevodník mien",
            "tagline": "Preveď medzi 50+ menami s referenčnými kurzami k známemu dátumu. Bez live API, bez sledovania — užitočné na rýchle odhady a cenové ponuky pre freelancera. Pred fakturáciou vždy over.",
            "description": "Bezplatný prevodník mien priamo v prehliadači s napevno zakódovanými referenčnými kurzami, aktualizovanými štvrťročne. Vyber zdroj a cieľ, zadaj sumu, prečítaj výsledok. Referenčný dátum je zobrazený — pred vystavením faktúry vždy over so skutočným kurzom svojej banky. Live kurzy zámerne neťaháme: prezradilo by to tvoje dotazy tretej strane. Na reálne transakcie použi banku alebo FX dealera.",
        },
        "cs": {
            "name": "Převodník měn",
            "tagline": "Převeď mezi 50+ měnami s referenčními kurzy k známému datu. Bez live API, bez sledování — užitečné pro rychlé odhady a cenové nabídky pro freelancera. Před fakturací vždy ověř.",
            "description": "Bezplatný převodník měn přímo v prohlížeči s napevno zakódovanými referenčními kurzy, aktualizovanými čtvrtletně. Vyber zdroj a cíl, zadej částku, přečti výsledek. Referenční datum je zobrazené — před vystavením faktury vždy ověř se skutečným kurzem své banky. Live kurzy záměrně netaháme: prozradilo by to tvé dotazy třetí straně. Pro reálné transakce použij banku nebo FX dealera.",
        },
    },
    "body": """
<div class="tool-card cc-banner">
  <strong>⚠️ Reference rates, not live.</strong>
  <span id="cc-asof"></span>
  Always verify with your bank before issuing an invoice or sending a payment.
</div>
<div class="tool-card">
  <div class="cc-quick">
    <span class="meta">Quick pairs:</span>
    <button type="button" class="secondary" onclick="ccPair('USD','EUR')">USD → EUR</button>
    <button type="button" class="secondary" onclick="ccPair('EUR','USD')">EUR → USD</button>
    <button type="button" class="secondary" onclick="ccPair('USD','GBP')">USD → GBP</button>
    <button type="button" class="secondary" onclick="ccPair('EUR','GBP')">EUR → GBP</button>
    <button type="button" class="secondary" onclick="ccPair('USD','JPY')">USD → JPY</button>
    <button type="button" class="secondary" onclick="ccPair('EUR','CHF')">EUR → CHF</button>
    <button type="button" class="secondary" onclick="ccPair('EUR','CZK')">EUR → CZK</button>
  </div>
</div>
<div class="tool-card">
  <div class="cc-grid">
    <div class="cc-side">
      <label for="cc-from-cur">{LBL_FROM}</label>
      <select id="cc-from-cur" onchange="ccRecalcFrom()"></select>
      <label for="cc-from-amt" style="margin-top:0.5rem">Amount</label>
      <input type="number" id="cc-from-amt" step="any" value="100" oninput="ccRecalcFrom()">
    </div>
    <div class="cc-swap-wrap">
      <button type="button" class="secondary cc-swap" onclick="ccSwap()" title="{LBL_SWAP}">⇄</button>
    </div>
    <div class="cc-side">
      <label for="cc-to-cur">{LBL_TO}</label>
      <select id="cc-to-cur" onchange="ccRecalcFrom()"></select>
      <label for="cc-to-amt" style="margin-top:0.5rem">Amount</label>
      <input type="number" id="cc-to-amt" step="any" value="0" oninput="ccRecalcTo()">
    </div>
  </div>
  <div id="cc-rate-line" class="meta" style="margin-top:0.7rem;text-align:center"></div>
</div>
""",
    "script": """
<style>
.cc-banner{background:#fff7ed;border:1px solid #fed7aa;color:#9a3412;font-size:0.92rem;line-height:1.5;padding:0.7rem 0.9rem}
:root[data-theme="dark"] .cc-banner{background:#3b1d0d;border-color:#7c2d12;color:#fed7aa}
.cc-banner strong{display:inline-block;margin-right:0.3rem}
.cc-quick{display:flex;gap:0.4rem;flex-wrap:wrap;align-items:center}
.cc-quick button{padding:0.35rem 0.7rem;font-size:0.82rem}
.cc-grid{display:grid;grid-template-columns:1fr auto 1fr;gap:0.8rem;align-items:start}
.cc-side{display:flex;flex-direction:column}
.cc-side input, .cc-side select{font-size:1.05rem;padding:0.55rem;width:100%;box-sizing:border-box}
.cc-swap-wrap{display:flex;align-items:center;justify-content:center;padding-top:1.8rem}
.cc-swap{padding:0.5rem 0.8rem;font-size:1.2rem}
@media(max-width:680px){
  .cc-grid{grid-template-columns:1fr}
  .cc-swap-wrap{padding-top:0}
}
</style>
<script>
const CC_DATA = __FX_DATA__;
const CC_FMT = new Intl.NumberFormat(undefined, {maximumFractionDigits: 6, minimumFractionDigits: 2});
function ccConvert(amount, from, to){
  if(!isFinite(amount)) return NaN;
  const fr = CC_DATA.rates[from], tr = CC_DATA.rates[to];
  if(!fr || !tr) return NaN;
  return amount / fr * tr;
}
function ccFmt(n){
  if(!isFinite(n)) return '—';
  // Avoid scientific notation on very small currency values
  return CC_FMT.format(n);
}
function ccPopulate(){
  const fromSel = document.getElementById('cc-from-cur');
  const toSel = document.getElementById('cc-to-cur');
  fromSel.innerHTML = ''; toSel.innerHTML = '';
  CC_DATA.groups.forEach(function(g){
    const ogFrom = document.createElement('optgroup'); ogFrom.label = g.label_en;
    const ogTo = document.createElement('optgroup'); ogTo.label = g.label_en;
    g.codes.forEach(function(code){
      const name = CC_DATA.names[code] || code;
      const oFrom = document.createElement('option'); oFrom.value = code; oFrom.textContent = code + ' — ' + name; ogFrom.appendChild(oFrom);
      const oTo = document.createElement('option'); oTo.value = code; oTo.textContent = code + ' — ' + name; ogTo.appendChild(oTo);
    });
    fromSel.appendChild(ogFrom);
    toSel.appendChild(ogTo);
  });
  fromSel.value = 'USD';
  toSel.value = 'EUR';
}
function ccRateLine(){
  const from = document.getElementById('cc-from-cur').value;
  const to = document.getElementById('cc-to-cur').value;
  if(from === to){
    document.getElementById('cc-rate-line').textContent = '1 ' + from + ' = 1 ' + to;
    return;
  }
  const r = ccConvert(1, from, to);
  const inv = ccConvert(1, to, from);
  document.getElementById('cc-rate-line').innerHTML =
    '1 ' + from + ' = ' + ccFmt(r) + ' ' + to +
    ' &nbsp;·&nbsp; 1 ' + to + ' = ' + ccFmt(inv) + ' ' + from;
}
function ccRecalcFrom(){
  const amt = parseFloat(document.getElementById('cc-from-amt').value);
  const from = document.getElementById('cc-from-cur').value;
  const to = document.getElementById('cc-to-cur').value;
  const r = ccConvert(amt, from, to);
  document.getElementById('cc-to-amt').value = isFinite(r) ? r.toFixed(4).replace(/\\.?0+$/, '') : '';
  ccRateLine();
}
function ccRecalcTo(){
  const amt = parseFloat(document.getElementById('cc-to-amt').value);
  const from = document.getElementById('cc-from-cur').value;
  const to = document.getElementById('cc-to-cur').value;
  const r = ccConvert(amt, to, from);
  document.getElementById('cc-from-amt').value = isFinite(r) ? r.toFixed(4).replace(/\\.?0+$/, '') : '';
  ccRateLine();
}
function ccSwap(){
  const fromSel = document.getElementById('cc-from-cur');
  const toSel = document.getElementById('cc-to-cur');
  const f = fromSel.value, t = toSel.value;
  fromSel.value = t; toSel.value = f;
  // After swap, recalc from the LEFT amount field so the user sees the new direction
  ccRecalcFrom();
}
function ccPair(from, to){
  document.getElementById('cc-from-cur').value = from;
  document.getElementById('cc-to-cur').value = to;
  ccRecalcFrom();
}
function ccInit(){
  ccPopulate();
  document.getElementById('cc-asof').textContent =
    ' Rates as of ' + CC_DATA.date + ' (' + CC_DATA.source + ').';
  ccRecalcFrom();
}
document.addEventListener('DOMContentLoaded', ccInit);
</script>
""".replace("__FX_DATA__", _FX_JS),
    "help": {
        "en": """
<h2>What this is — and isn't</h2>
<p>This is a quick reference currency converter. You pick a source currency, pick a target, enter an amount, and the tool divides by the source's EUR rate and multiplies by the target's EUR rate. That's it. The rates are <strong>hard-coded</strong> in the page — there is no network call, no API key, no tracking.</p>
<p>It is not a forex terminal. The rates were correct on the date shown beneath the result and are updated roughly quarterly. Real bank rates move every second and include a margin (typically 0.5–3% for retail, much tighter on FX desks), card-network fees, and weekend mark-ups. Before invoicing a client or sending an actual payment, look up the current rate from your bank, Wise, or a public FX feed.</p>

<h2>Why we don't fetch live rates</h2>
<p>Almost every "free" live-rate API in the wild logs the IP, referrer, and currency pair you queried. For a tool meant to be useful to freelancers checking quote ballparks all day, that's a metadata leak that compounds: each refresh is one more data point about your client mix and your typical contract size sitting in someone's database. A static reference table avoids the problem completely — your queries never leave the browser. The tradeoff is accuracy: don't blindly trust the result for transactions.</p>

<h2>Common gotchas</h2>
<ul>
  <li><strong>Pegged currencies look fixed but aren't always.</strong> BGN is hard-pegged to EUR at 1.95583 (and has been for years). DKK and HKD are pegged within bands. But the relationship can change overnight — the Swiss Franc cap was abandoned suddenly in 2015. Don't assume a peg holds for the future just because it held last year.</li>
  <li><strong>EUR-cross compounds error.</strong> Every conversion routes via EUR (USD → JPY = USD/EUR × EUR/JPY). Tiny rounding errors in two rates compound on illiquid pairs. The result is fine for ballpark; not fine for accounting.</li>
  <li><strong>Mid-rate ≠ what you get.</strong> The published "mid-rate" is the midpoint between buy and sell. Your bank quotes a buy price and a sell price; the spread between them is their margin. Card networks add another 1–3% on top. Expect to receive 1–4% less than the mid-rate quoted here.</li>
  <li><strong>Inflation-driven currencies move fast.</strong> ARS (Argentine Peso), TRY (Turkish Lira) and similar can move 5–10% in a month. A snapshot rate dated three months ago could be quite wrong. Treat the date label seriously.</li>
  <li><strong>Cash vs digital differ.</strong> Tourist cash bureaus, ATM withdrawals abroad, and card transactions each have different rate structures. The "mid-rate" applies most closely to bank transfers and FX-desk trades; cash conversion in an airport is typically 5–10% worse.</li>
</ul>

<h2>When this tool is useful</h2>
<ul>
  <li>Drafting a freelance quote for a client in another country and you want a ballpark in your home currency.</li>
  <li>Reading a foreign-currency invoice and quickly checking whether it's roughly what you expected.</li>
  <li>Comparing prices on two sites listed in different currencies.</li>
  <li>Sanity-checking that a wire transfer landed in the right ballpark after spread.</li>
</ul>
<p>It is not useful for: hedging, FX trading decisions, tax filings (use the rate published by your tax authority for the relevant date), or anything where being off by 1–3% matters.</p>
""",
        "de": """
<h2>Was das ist — und was nicht</h2>
<p>Ein schneller Referenz-Währungsrechner. Quelle, Ziel, Betrag — fertig. Die Kurse sind fest im Code, kein Netzwerkaufruf, kein Tracking. Aktualisierung etwa vierteljährlich, gültig zum angegebenen Datum.</p>
<p>Kein Forex-Terminal. Echte Bankkurse bewegen sich pro Sekunde und enthalten Margen (0,5–3 % bei Retail), Karten-Netzgebühren und Wochenend-Aufschläge. Vor einer Rechnung oder Überweisung den aktuellen Kurs bei Bank, Wise oder einem Public-FX-Feed nachschlagen.</p>
<h2>Warum keine Live-Kurse</h2>
<p>Fast jede „kostenlose“ Live-Rate-API loggt IP, Referrer und Währungspaar. Pro Refresh ein weiterer Metadaten-Punkt über deinen Kundenstamm. Statische Tabelle vermeidet das vollständig — Anfragen verlassen den Browser nicht.</p>
<h2>Häufige Stolperfallen</h2>
<ul>
  <li>Pegs gelten heute, nicht immer. CHF-Cap fiel 2015 plötzlich.</li>
  <li>EUR-Cross verstärkt Rundungsfehler bei seltenen Paaren.</li>
  <li>Mid-Rate ist nicht dein Auszahlungskurs — 1–4 % Spread/Marge.</li>
  <li>ARS, TRY bewegen sich monatsweise um 5–10 %.</li>
  <li>Bargeld am Flughafen ≠ Online-Banktransfer (5–10 % schlechter).</li>
</ul>
<h2>Wann sinnvoll</h2>
<ul>
  <li>Freelance-Angebot in anderer Währung — Hausnummer.</li>
  <li>Eingehende Auslandsrechnung plausibilisieren.</li>
  <li>Preisvergleich zwischen Shops in zwei Währungen.</li>
  <li>Schneller Sanity-Check einer Überweisung.</li>
</ul>
<p>Nicht für: Hedging, FX-Trading, Steuererklärung (nimm den Stichtagskurs der Finanzbehörde), oder wenn 1–3 % wirklich zählen.</p>
""",
        "es": """
<h2>Qué es y qué no es</h2>
<p>Un conversor de divisas de referencia rápido. Eliges origen y destino, introduces un importe, y la herramienta divide por el tipo EUR de origen y multiplica por el de destino. Los tipos están fijos en la página — sin llamada de red, sin API key, sin tracking.</p>
<p>No es una terminal forex. Los tipos eran correctos en la fecha mostrada y se actualizan trimestralmente. Los tipos reales del banco se mueven cada segundo e incluyen margen (0,5–3 % minorista), comisiones de red de tarjeta y recargos de fin de semana. Antes de facturar o enviar un pago real, mira el tipo actual en tu banco, Wise o un feed FX público.</p>
<h2>Por qué no buscamos tipos en vivo</h2>
<p>Casi todas las APIs "gratis" de tipos en vivo registran IP, referrer y par consultado. Para una herramienta que un freelance abre todo el día, cada refresh es otro dato sobre tu cartera de clientes. Una tabla estática elimina ese leak completamente.</p>
<h2>Errores comunes</h2>
<ul>
  <li>Las divisas pegged parecen fijas pero no siempre lo son (CHF rompió su tope en 2015).</li>
  <li>El paso por EUR amplifica errores en pares ilíquidos.</li>
  <li>El mid-rate no es lo que cobras: 1–4 % menos por margen y comisión.</li>
  <li>ARS y TRY pueden moverse 5–10 % en un mes.</li>
  <li>Caja en aeropuerto vs transferencia: 5–10 % peor en caja.</li>
</ul>
<h2>Cuándo es útil</h2>
<ul>
  <li>Redactar un presupuesto freelance en otra divisa — orientativo.</li>
  <li>Leer una factura extranjera y comprobar si está en rango.</li>
  <li>Comparar precios en dos webs en divisas distintas.</li>
  <li>Verificar que una transferencia llegó por la cantidad correcta.</li>
</ul>
<p>No sirve para: hedging, trading FX, declaraciones fiscales (usa el tipo oficial de tu agencia tributaria), o cualquier cosa donde 1–3 % importe.</p>
""",
        "fr": """
<h2>Ce que c'est — et ne l'est pas</h2>
<p>Un convertisseur de devises de référence rapide. Source, cible, montant — c'est tout. Les taux sont codés en dur dans la page — pas d'appel réseau, pas de clé API, pas de tracking. Mis à jour trimestriellement, valables à la date affichée.</p>
<p>Pas un terminal forex. Les vrais taux bancaires bougent à la seconde et incluent une marge (0,5–3 % en retail), des frais de réseau cartes, et des majorations de week-end. Avant de facturer ou d'envoyer un paiement, consultez le taux actuel chez votre banque, Wise, ou un feed FX public.</p>
<h2>Pourquoi pas de taux live</h2>
<p>Presque toutes les API "gratuites" de taux live loggent IP, referrer et paire consultée. Pour un outil ouvert toute la journée par un freelance, chaque refresh est un point de plus sur votre portefeuille client. Une table statique élimine cette fuite.</p>
<h2>Pièges courants</h2>
<ul>
  <li>Les pegs ne tiennent pas pour toujours (le plafond CHF est tombé en 2015).</li>
  <li>Le routage via EUR amplifie les erreurs d'arrondi sur paires illiquides.</li>
  <li>Le mid-rate n'est pas ce que vous touchez : 1–4 % de spread/commission.</li>
  <li>ARS et TRY peuvent bouger de 5–10 % en un mois.</li>
  <li>Bureau de change en aéroport : 5–10 % moins bon que virement.</li>
</ul>
<h2>Quand c'est utile</h2>
<ul>
  <li>Rédiger un devis freelance en devise étrangère — ordre de grandeur.</li>
  <li>Plausibiliser une facture en devise étrangère.</li>
  <li>Comparer des prix entre deux sites en devises différentes.</li>
  <li>Vérifier qu'un virement est arrivé dans la bonne fourchette.</li>
</ul>
<p>Pas pour : hedging, trading FX, déclarations fiscales (utilisez le taux officiel de l'administration), ou tout ce où 1–3 % compte vraiment.</p>
""",
        "it": """
<h2>Cosa è — e cosa non è</h2>
<p>Un convertitore di valute di riferimento rapido. Origine, destinazione, importo. I tassi sono cablati nella pagina — nessuna chiamata di rete, nessuna API key, nessun tracking. Aggiornati ogni trimestre, validi alla data mostrata.</p>
<p>Non è un terminale forex. I tassi reali della banca si muovono ogni secondo e includono margine (0,5–3 % retail), commissioni circuito carte e maggiorazioni weekend. Prima di fatturare o inviare un pagamento, controlla il tasso attuale presso la banca, Wise o un feed FX pubblico.</p>
<h2>Perché non tassi live</h2>
<p>Quasi tutte le API "gratuite" di tassi live loggano IP, referrer e coppia consultata. Per un freelance che la lascia aperta tutto il giorno, ogni refresh è un altro punto sui clienti. Una tabella statica elimina questa fuga.</p>
<h2>Errori comuni</h2>
<ul>
  <li>I peg sembrano fissi ma non lo sono (il tetto CHF è caduto nel 2015).</li>
  <li>Il passaggio via EUR amplifica gli errori di arrotondamento su coppie poco liquide.</li>
  <li>Il mid-rate non è quello che riceverai: 1–4 % di spread/commissioni.</li>
  <li>ARS e TRY possono muoversi del 5–10 % in un mese.</li>
  <li>Cambio in aeroporto: 5–10 % peggio di bonifico bancario.</li>
</ul>
<h2>Quando è utile</h2>
<ul>
  <li>Preparare un preventivo freelance in valuta estera — ordine di grandezza.</li>
  <li>Controllare una fattura estera.</li>
  <li>Confrontare prezzi tra due siti in valute diverse.</li>
  <li>Verificare un bonifico arrivato.</li>
</ul>
<p>Non per: hedging, FX trading, dichiarazione dei redditi (usa il tasso ufficiale dell'agenzia delle entrate), o dove l'1–3 % conta davvero.</p>
""",
        "pt": """
<h2>O que é — e o que não é</h2>
<p>Um conversor de moedas de referência rápido. Origem, destino, valor. As taxas estão fixas na página — sem chamada de rede, sem API key, sem rastreamento. Atualizadas trimestralmente, válidas na data mostrada.</p>
<p>Não é um terminal forex. As taxas reais do banco mudam por segundo e incluem margem (0,5–3 % no varejo), taxas da rede de cartões e markup de fim de semana. Antes de faturar ou enviar pagamento, consulte a taxa atual no seu banco, Wise ou um feed FX público.</p>
<h2>Por que não buscamos taxas ao vivo</h2>
<p>Quase toda API "grátis" de taxa ao vivo registra IP, referrer e o par consultado. Para uma ferramenta aberta o dia todo por um freelancer, cada refresh é mais um dado sobre sua carteira de clientes. Tabela estática elimina esse vazamento.</p>
<h2>Pegadinhas comuns</h2>
<ul>
  <li>Pegs parecem fixos mas não são sempre (o teto do CHF caiu em 2015).</li>
  <li>Passar pelo EUR amplifica erros de arredondamento em pares ilíquidos.</li>
  <li>O mid-rate não é o que você recebe: 1–4 % de spread/comissão.</li>
  <li>ARS e TRY podem mover 5–10 % em um mês.</li>
  <li>Casa de câmbio em aeroporto: 5–10 % pior que transferência bancária.</li>
</ul>
<h2>Quando é útil</h2>
<ul>
  <li>Fazer orçamento freelance em moeda estrangeira — ordem de grandeza.</li>
  <li>Conferir uma fatura estrangeira recebida.</li>
  <li>Comparar preços entre dois sites em moedas diferentes.</li>
  <li>Verificar se uma transferência chegou no valor esperado.</li>
</ul>
<p>Não serve para: hedge, FX trading, declaração de imposto (use a taxa oficial da Receita), ou onde 1–3 % importam mesmo.</p>
""",
        "pl": """
<h2>Czym to jest — i czym nie</h2>
<p>Szybki referencyjny przelicznik walut. Wybierasz źródło, cel, wpisujesz kwotę. Kursy są na sztywno wpisane w stronę — bez wywołań sieciowych, bez API key, bez śledzenia. Aktualizowane mniej więcej kwartalnie, ważne na wyświetlaną datę.</p>
<p>To nie terminal forex. Realne kursy bankowe ruszają się co sekundę i zawierają marżę (0,5–3 % w retailu), prowizje sieci kart i dopłaty weekendowe. Przed fakturą lub przelewem sprawdź aktualny kurs w swoim banku, Wise lub publicznym feedzie FX.</p>
<h2>Czemu nie pobieramy kursów live</h2>
<p>Niemal każde "darmowe" API live-kursów loguje IP, referrer i parę walut. Dla freelancera trzymającego stronę otwartą cały dzień każdy refresh to kolejny punkt o twoim portfelu klientów. Statyczna tabela całkowicie eliminuje ten wyciek.</p>
<h2>Częste pułapki</h2>
<ul>
  <li>Pegi wyglądają na stałe, ale nie zawsze są (sufit CHF padł nagle w 2015).</li>
  <li>Trasa przez EUR wzmacnia błędy zaokrąglenia na rzadkich parach.</li>
  <li>Mid-rate to nie kwota, którą dostaniesz: 1–4 % spreadu/prowizji.</li>
  <li>ARS i TRY potrafią ruszyć się o 5–10 % w miesiącu.</li>
  <li>Kantor na lotnisku: 5–10 % gorzej niż przelew bankowy.</li>
</ul>
<h2>Kiedy się przydaje</h2>
<ul>
  <li>Wycena freelance w obcej walucie — orientacyjnie.</li>
  <li>Sprawdzenie przychodzącej zagranicznej faktury.</li>
  <li>Porównanie cen między dwoma sklepami w różnych walutach.</li>
  <li>Sanity-check przelewu zagranicznego.</li>
</ul>
<p>Nie nadaje się do: hedgingu, tradingu FX, deklaracji podatkowych (użyj kursu urzędowego US/NBP na dany dzień) ani niczego, gdzie 1–3 % różnicy ma znaczenie.</p>
""",
        "ja": """
<h2>これは何 — そして何ではないか</h2>
<p>素早く参照するための通貨換算ツールです。元通貨、目的通貨、金額を入力すれば、EUR レートで除算・乗算して結果を出します。レートはページ内にハードコードされています — ネットワーク呼び出しなし、API キーなし、トラッキングなし。約四半期ごとに更新され、表示された基準日時点の値です。</p>
<p>これは FX ターミナルではありません。実際の銀行レートは秒単位で動き、マージン（リテールで 0.5〜3%）、カードネットワーク手数料、週末スプレッドを含みます。請求書や送金前には、銀行・Wise・公開 FX フィードで現在レートを確認してください。</p>
<h2>ライブレートを取らない理由</h2>
<p>多くの「無料」ライブレート API は IP、リファラ、参照した通貨ペアをログします。フリーランスが一日中開きっぱなしにするツールでは、リフレッシュごとに顧客構成や取引規模に関するメタデータが流出します。静的テーブルなら漏洩そのものを排除できます。</p>
<h2>よくある落とし穴</h2>
<ul>
  <li>ペッグは「今は固定」でも、永続ではありません（CHF キャップは 2015 年に突然撤廃）。</li>
  <li>EUR 経由のクロスは丸め誤差が累積します。</li>
  <li>ミッドレートは実際の受取額ではありません（スプレッドと手数料で 1〜4% 目減り）。</li>
  <li>ARS, TRY などインフレ通貨は 1 か月で 5〜10% 動きます。</li>
  <li>空港の両替所は銀行送金より 5〜10% 不利です。</li>
</ul>
<h2>使いどころ</h2>
<ul>
  <li>海外クライアント向け見積もりのざっくり把握。</li>
  <li>外貨建て請求書の妥当性チェック。</li>
  <li>異なる通貨で表示された 2 サイトの価格比較。</li>
  <li>海外送金が概ね期待通りに着金したかの確認。</li>
</ul>
<p>適さない用途: ヘッジ、FX 取引判断、税務申告（税務当局公示の基準日レートを使う）、1〜3% の差が問題になる場面。</p>
""",
        "nl": """
<h2>Wat dit is — en wat niet</h2>
<p>Een snelle referentie-valutaconverter. Kies bron, doel, bedrag. De koersen staan hard in de pagina — geen network call, geen API key, geen tracking. Updates ongeveer per kwartaal, geldig op de getoonde datum.</p>
<p>Geen forex-terminal. Echte bankkoersen bewegen per seconde en bevatten marge (0,5–3 % retail), kaartnetwerk-fees en weekendopslag. Vóór een factuur of betaling: koers ophalen bij bank, Wise of publieke FX-feed.</p>
<h2>Waarom geen live koersen</h2>
<p>Bijna elke "gratis" live-rate-API logt IP, referrer en het opgevraagde paar. Voor een freelancer die de tool de hele dag open heeft staan, is elke refresh een extra datapunt over je klantenbestand. Een statische tabel elimineert dat lek.</p>
<h2>Veelvoorkomende valkuilen</h2>
<ul>
  <li>Pegs lijken vast maar zijn niet altijd permanent (CHF-plafond viel in 2015).</li>
  <li>Routing via EUR versterkt afrondingsfouten op illiquide paren.</li>
  <li>Mid-rate ≠ wat je krijgt: 1–4 % spread/marge.</li>
  <li>ARS en TRY kunnen 5–10 % per maand bewegen.</li>
  <li>Wisselkantoor op vliegveld: 5–10 % slechter dan bankoverboeking.</li>
</ul>
<h2>Wanneer nuttig</h2>
<ul>
  <li>Freelance-offerte in buitenlandse valuta — orde van grootte.</li>
  <li>Inkomende buitenlandse factuur plausibel maken.</li>
  <li>Prijsvergelijking tussen sites in verschillende valuta.</li>
  <li>Snelle check of een overboeking ongeveer goed binnenkwam.</li>
</ul>
<p>Niet voor: hedging, FX-trading, belastingaangifte (gebruik de officiële belastingkoers), of als 1–3 % echt telt.</p>
""",
        "tr": """
<h2>Bu nedir — ve ne değildir</h2>
<p>Hızlı bir referans döviz çevirici. Kaynak, hedef, tutar — bu kadar. Kurlar sayfada gömülü; ağ çağrısı yok, API anahtarı yok, takip yok. Yaklaşık üç ayda bir güncelleniyor, gösterilen tarih için geçerlidir.</p>
<p>Forex terminali değil. Gerçek banka kurları saniyede değişir ve marj (perakendede %0,5–3), kart ağı ücretleri ve hafta sonu primleri içerir. Fatura kesmeden veya ödeme göndermeden önce bankan, Wise veya açık bir FX feed'den güncel kuru kontrol et.</p>
<h2>Niye canlı kur çekmiyoruz</h2>
<p>Çoğu "ücretsiz" canlı kur API'si IP, referrer ve sorgulanan döviz çiftini loglar. Freelancer'ın bütün gün açık tuttuğu bir araç için her yenileme, müşteri profilin hakkında bir veri noktası daha demek. Statik tablo bu sızıntıyı tamamen kaldırır.</p>
<h2>Yaygın hatalar</h2>
<ul>
  <li>Peg'ler bugün sabit, sonsuza dek değil (CHF tavanı 2015'te düştü).</li>
  <li>EUR üzerinden rota seyrek çiftlerde yuvarlama hatasını büyütür.</li>
  <li>Mid-rate alacağın tutar değildir: %1–4 spread/komisyon.</li>
  <li>ARS ve TRY bir ayda %5–10 hareket edebilir.</li>
  <li>Havalimanı bürosu: banka transferinden %5–10 kötü.</li>
</ul>
<h2>Ne zaman işe yarar</h2>
<ul>
  <li>Yabancı bir müşteriye freelance teklif — yaklaşık rakam.</li>
  <li>Gelen yabancı faturayı kontrol etmek.</li>
  <li>Farklı para birimindeki iki siteyi karşılaştırmak.</li>
  <li>Bir transferin doğru civarda geldiğini görmek.</li>
</ul>
<p>Şunlar için değil: hedging, FX ticareti, vergi beyanı (resmi gün kurunu kullan), %1–3'ün önemli olduğu işler.</p>
""",
        "id": """
<h2>Apa ini — dan bukan apa</h2>
<p>Konverter mata uang referensi cepat. Pilih asal, tujuan, masukkan jumlah. Kurs di-hardcode di halaman — tanpa panggilan jaringan, tanpa API key, tanpa tracking. Diperbarui sekitar kuartalan, valid pada tanggal yang ditampilkan.</p>
<p>Bukan terminal forex. Kurs bank nyata bergerak per detik dan termasuk margin (0,5–3 % ritel), biaya jaringan kartu, dan markup akhir pekan. Sebelum invoice atau kirim pembayaran, cek kurs aktual di bank, Wise, atau FX feed publik.</p>
<h2>Mengapa tidak fetch kurs live</h2>
<p>Hampir semua API "gratis" kurs live mencatat IP, referrer, dan pasangan yang ditanya. Untuk tool yang freelancer biarkan terbuka seharian, tiap refresh adalah satu titik data lagi tentang portofolio klienmu. Tabel statis menghilangkan kebocoran itu.</p>
<h2>Kesalahan umum</h2>
<ul>
  <li>Peg terlihat tetap tapi tidak selalu (langit CHF jatuh 2015).</li>
  <li>Rute via EUR memperbesar error pembulatan pada pair ilikuid.</li>
  <li>Mid-rate bukan yang kamu terima: 1–4 % spread/komisi.</li>
  <li>ARS dan TRY bisa bergerak 5–10 % per bulan.</li>
  <li>Money changer bandara: 5–10 % lebih jelek dari transfer bank.</li>
</ul>
<h2>Kapan berguna</h2>
<ul>
  <li>Bikin penawaran freelance dalam mata uang asing — kira-kira.</li>
  <li>Cek invoice asing yang masuk.</li>
  <li>Bandingkan harga dua situs dengan mata uang berbeda.</li>
  <li>Verifikasi transfer masuk di kisaran benar.</li>
</ul>
<p>Tidak untuk: hedging, FX trading, pajak (pakai kurs resmi pajak), atau hal di mana selisih 1–3 % berarti.</p>
""",
        "vi": """
<h2>Đây là gì — và không phải gì</h2>
<p>Bộ chuyển đổi tiền tệ tham chiếu nhanh. Chọn nguồn, đích, nhập số tiền. Tỷ giá được hardcode trong trang — không gọi mạng, không API key, không tracking. Cập nhật khoảng hàng quý, có hiệu lực tại ngày hiển thị.</p>
<p>Không phải terminal forex. Tỷ giá ngân hàng thực thay đổi từng giây và bao gồm biên (0,5–3 % bán lẻ), phí mạng thẻ và markup cuối tuần. Trước khi xuất hóa đơn hoặc chuyển khoản, kiểm tra tỷ giá hiện tại tại ngân hàng, Wise hoặc nguồn FX công khai.</p>
<h2>Vì sao không lấy tỷ giá live</h2>
<p>Gần như mọi API "miễn phí" tỷ giá live đều log IP, referrer và cặp được hỏi. Với công cụ mà freelancer mở cả ngày, mỗi lần refresh là thêm một điểm dữ liệu về danh mục khách hàng của bạn. Bảng tĩnh loại bỏ hoàn toàn rò rỉ đó.</p>
<h2>Lỗi thường gặp</h2>
<ul>
  <li>Peg hôm nay cố định, không vĩnh viễn (trần CHF rơi năm 2015).</li>
  <li>Đi qua EUR khuếch đại lỗi làm tròn ở cặp kém thanh khoản.</li>
  <li>Mid-rate không phải số bạn nhận: 1–4 % spread/phí.</li>
  <li>ARS và TRY có thể di chuyển 5–10 % mỗi tháng.</li>
  <li>Đổi tiền sân bay: kém 5–10 % so với chuyển khoản.</li>
</ul>
<h2>Khi nào hữu ích</h2>
<ul>
  <li>Lập báo giá freelance bằng ngoại tệ — ước lượng.</li>
  <li>Kiểm tra hóa đơn ngoại tệ đến.</li>
  <li>So sánh giá giữa hai site ở hai loại tiền.</li>
  <li>Kiểm tra chuyển khoản về đúng cỡ.</li>
</ul>
<p>Không dùng cho: hedging, giao dịch FX, khai thuế (dùng tỷ giá chính thức), nơi 1–3 % thực sự quan trọng.</p>
""",
        "hi": """
<h2>यह क्या है — और क्या नहीं</h2>
<p>एक त्वरित reference currency converter। Source, target, amount डालें। Rates page में hard-coded हैं — कोई network call नहीं, कोई API key नहीं, कोई tracking नहीं। लगभग quarterly update होती हैं, दिखाई गई date के लिए valid हैं।</p>
<p>यह forex terminal नहीं है। असली bank rates हर second बदलती हैं और इनमें margin (retail में 0.5–3%), card network fees, और weekend markup शामिल होते हैं। Invoice भेजने या payment करने से पहले अपने bank, Wise, या public FX feed से current rate देखें।</p>
<h2>हम live rates क्यों नहीं लाते</h2>
<p>लगभग हर "free" live-rate API आपकी IP, referrer और query किया गया pair log करती है। Freelancer के लिए जो दिनभर tool खुला रखता है, हर refresh आपके client portfolio के बारे में एक और data point है। Static table यह leak पूरी तरह हटा देती है।</p>
<h2>आम गलतियाँ</h2>
<ul>
  <li>Pegs आज fixed लगते हैं, हमेशा नहीं रहते (CHF cap 2015 में अचानक गिरा)।</li>
  <li>EUR के via routing से illiquid pairs पर rounding error बढ़ता है।</li>
  <li>Mid-rate वह नहीं जो आपको मिलेगा: 1–4% spread/commission।</li>
  <li>ARS और TRY एक महीने में 5–10% हिल सकते हैं।</li>
  <li>Airport money changer: bank transfer से 5–10% खराब।</li>
</ul>
<h2>कब उपयोगी है</h2>
<ul>
  <li>विदेशी currency में freelance quote draft करना — approximate।</li>
  <li>आने वाला विदेशी invoice check करना।</li>
  <li>दो websites पर अलग currencies में prices compare करना।</li>
  <li>Wire transfer सही range में पहुँचा है verify करना।</li>
</ul>
<p>इनके लिए नहीं: hedging, FX trading, tax filing (अपने tax authority का official rate use करें), या जहाँ 1–3% का फर्क मायने रखता हो।</p>
""",
        "sk": """
<h2>Čo to je — a čo nie</h2>
<p>Rýchly referenčný prevodník mien. Vyber zdroj, cieľ, zadaj sumu. Kurzy sú napevno v stránke — žiadne sieťové volania, žiadny API key, žiadne sledovanie. Aktualizujú sa zhruba štvrťročne, platia k zobrazenému dátumu.</p>
<p>Nie je to forex terminál. Skutočné bankové kurzy sa hýbu po sekundách a obsahujú maržu (0,5–3 % v retaile), poplatky kartových sietí a víkendové prirážky. Pred faktúrou alebo prevodom over aktuálny kurz v banke, vo Wise alebo v public FX feede.</p>
<h2>Prečo neťaháme live kurzy</h2>
<p>Skoro každé „bezplatné“ live-rate API loguje IP, referrer a požadovaný pár. Pre freelancera, ktorý má nástroj otvorený celý deň, je každý refresh ďalším bodom o tvojom klientskom portfóliu. Statická tabuľka tento únik úplne odstraňuje.</p>
<h2>Časté chyby</h2>
<ul>
  <li>Pegy dnes držia, navždy nie (CHF strop padol v roku 2015 zo dňa na deň).</li>
  <li>Trasa cez EUR zväčšuje zaokrúhľovacie chyby pri zriedkavých pároch.</li>
  <li>Mid-rate nie je to, čo dostaneš: 1–4 % spread/provízia.</li>
  <li>ARS a TRY sa môžu pohnúť o 5–10 % za mesiac.</li>
  <li>Zmenáreň na letisku: o 5–10 % horšie než bankový prevod.</li>
</ul>
<h2>Kedy je užitočný</h2>
<ul>
  <li>Pripraviť freelance cenovú ponuku v cudzej mene — rádovo.</li>
  <li>Skontrolovať prichádzajúcu zahraničnú faktúru.</li>
  <li>Porovnať ceny medzi dvomi e-shopmi v iných menách.</li>
  <li>Overiť, či prevod dorazil v približnej výške.</li>
</ul>
<p>Nie je na: hedging, FX trading, daňové priznanie (použi oficiálny kurz finančnej správy na daný deň) ani tam, kde 1–3 % skutočne rozhoduje.</p>
""",
        "cs": """
<h2>Co to je — a co ne</h2>
<p>Rychlý referenční převodník měn. Vyber zdroj, cíl, zadej částku. Kurzy jsou napevno ve stránce — žádné síťové volání, žádný API klíč, žádné sledování. Aktualizují se zhruba čtvrtletně, platí ke zobrazenému datu.</p>
<p>Není to forex terminál. Skutečné bankovní kurzy se hýbou každou sekundu a zahrnují marži (0,5–3 % v retailu), poplatky kartových sítí a víkendové přirážky. Před fakturou nebo platbou ověř aktuální kurz v bance, ve Wise nebo v public FX feedu.</p>
<h2>Proč netaháme live kurzy</h2>
<p>Skoro každé "bezplatné" live-rate API loguje IP, referrer a dotázaný pár. Pro freelancera, který má nástroj otevřený celý den, je každý refresh dalším bodem o tvém klientském portfoliu. Statická tabulka tento únik zcela odstraňuje.</p>
<h2>Časté chyby</h2>
<ul>
  <li>Pegy dnes drží, navždy ne (CHF strop padl v roce 2015 ze dne na den).</li>
  <li>Cesta přes EUR zvětšuje zaokrouhlovací chyby u vzácnějších párů.</li>
  <li>Mid-rate není to, co dostaneš: 1–4 % spread/provize.</li>
  <li>ARS a TRY se mohou pohnout o 5–10 % za měsíc.</li>
  <li>Směnárna na letišti: o 5–10 % horší než bankovní převod.</li>
</ul>
<h2>Kdy je užitečný</h2>
<ul>
  <li>Příprava freelance nabídky v cizí měně — řádově.</li>
  <li>Kontrola příchozí zahraniční faktury.</li>
  <li>Porovnání cen mezi dvěma e-shopy v různých měnách.</li>
  <li>Ověření, že převod dorazil v přibližné výši.</li>
</ul>
<p>Není pro: hedging, FX trading, daňové přiznání (použij oficiální kurz finanční správy ke dni) ani tam, kde 1–3 % skutečně rozhoduje.</p>
""",
    },
    "related": ["vat-calculator", "invoice-generator", "unit-converter"],
    "howto": {"flow": "calculate", "action": "convert", "noun": {"en": "currency", "de": "Währung", "es": "divisa", "fr": "devise", "it": "valuta", "pt": "moeda", "pl": "waluta", "ja": "通貨", "nl": "valuta", "tr": "döviz", "id": "mata uang", "vi": "tiền tệ", "hi": "currency", "sk": "menu", "cs": "měnu"}},
}
