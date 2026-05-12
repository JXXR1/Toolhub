TOOL = {
    "slug": "tip-split-calculator",
    "category": "math",
    "icon": "💵",
    "tags": ["tip", "split", "bill", "restaurant", "calculator", "people", "share"],
    "i18n": {
        "en": {
            "name": "Tip & Split Calculator",
            "tagline": "Bill total + tip % + people = per-person amount. Round-up option, tip and grand total shown.",
            "description": "Free tip and bill split calculator. Enter the bill, tip percentage, and number of people. See the tip amount, the grand total, and the per-person share. Optional round-up.",
        },
        "de": {"name": "Trinkgeld- & Aufteilen-Rechner", "tagline": "Rechnung + Trinkgeld-% + Personen = Betrag pro Person. Aufrunden möglich, Trinkgeld und Gesamtsumme angezeigt.", "description": "Kostenloser Trinkgeld- und Rechnungs-Splitter. Gib Rechnung, Trinkgeld-% und Personenzahl ein. Trinkgeld, Gesamtbetrag und pro-Person-Anteil werden berechnet. Aufrunden optional."},
        "es": {"name": "Calculadora de Propina y División", "tagline": "Cuenta + propina % + personas = importe por persona. Opción de redondeo. Propina y total mostrados.", "description": "Calculadora gratuita de propina y división de cuenta. Introduce el total, el % de propina y el número de personas. Verás propina, total y reparto por persona. Redondeo opcional."},
        "fr": {"name": "Calculateur de Pourboire et Partage", "tagline": "Addition + pourboire % + personnes = montant par personne. Arrondi en option. Pourboire et total affichés.", "description": "Calculateur gratuit de pourboire et partage. Entrez l'addition, le pourcentage et le nombre de personnes. Pourboire, total et part par personne calculés. Arrondi en option."},
        "it": {"name": "Calcolatore Mancia e Conto Diviso", "tagline": "Conto + mancia % + persone = importo per persona. Arrotondamento opzionale. Mancia e totale mostrati.", "description": "Calcolatore gratuito mancia e divisione conto. Inserisci conto, percentuale di mancia e numero di persone. Mancia, totale e quota per persona calcolati. Arrotondamento opzionale."},
        "pt": {"name": "Calculadora de Gorjeta e Rachar a Conta", "tagline": "Total da conta + gorjeta % + pessoas = valor por pessoa. Opção de arredondar para cima, mostra gorjeta e total geral.", "description": "Calculadora gratuita de gorjeta e divisão de conta. Informe a conta, a porcentagem de gorjeta e o número de pessoas. Veja o valor da gorjeta, o total geral e a parte de cada um. Arredondamento opcional para cima."},
        "pl": {"name": "Kalkulator Napiwku i Podziału Rachunku", "tagline": "Rachunek + napiwek % + liczba osób = kwota na osobę. Opcja zaokrąglenia w górę, pokazuje napiwek i sumę całkowitą.", "description": "Darmowy kalkulator napiwku i podziału rachunku. Wpisz rachunek, procent napiwku i liczbę osób. Zobacz kwotę napiwku, sumę całkowitą i udział na osobę. Opcjonalne zaokrąglenie w górę."},
        "ja": {"name": "チップ＆割り勘計算機", "tagline": "請求額 + チップ % + 人数 = 1 人あたり。切り上げオプションあり、チップ額と合計を表示。", "description": "無料のチップ・割り勘計算ツール。請求額、チップ率、人数を入力すると、チップ額、合計、1 人あたりの支払額が表示されます。切り上げオプションも利用可能です。"},
        "nl": {"name": "Tip & Split Calculator", "tagline": "Rekeningtotaal + tip % + personen = per-persoon bedrag. Round-up optie, tip en grand total getoond.", "description": "Gratis tip- en rekening-split-calculator. Voer de rekening, tip-percentage en aantal personen in. Zie het tip-bedrag, het grand total en het per-persoon-aandeel. Optionele round-up."},
        "tr": {"name": "Bahşiş & Bölüştürme Hesaplayıcı", "tagline": "Hesap toplamı + bahşiş % + kişi sayısı = kişi başı tutar. Yukarı yuvarlama seçeneği, bahşiş ve genel toplam gösterilir.", "description": "Ücretsiz bahşiş ve hesap bölüştürme hesaplayıcı. Hesabı, bahşiş yüzdesini ve kişi sayısını gir. Bahşiş tutarını, genel toplamı ve kişi başı payı gör. Opsiyonel yukarı yuvarlama."},
        "id": {"name": "Kalkulator Tip & Bagi Tagihan", "tagline": "Total tagihan + % tip + jumlah orang = jumlah per orang. Opsi pembulatan ke atas, menampilkan tip dan grand total.", "description": "Kalkulator tip dan bagi tagihan gratis. Masukkan jumlah tagihan, persentase tip, dan jumlah orang — dapatkan jumlah per orang, total tip, dan grand total. Opsi pembulatan ke atas untuk angka yang rapi."},
        "vi": {"name": "Máy tính Tip & Chia Hóa đơn", "tagline": "Tổng hóa đơn + % tip + số người = số tiền mỗi người. Tùy chọn làm tròn lên, hiển thị tip và grand total.", "description": "Máy tính tip và chia hóa đơn miễn phí trực tuyến. Nhập tổng hóa đơn, % tip và số người để xem số tiền mỗi người trả, với tùy chọn làm tròn lên đến đồng tiền gần nhất."},
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Bill total</label>
      <input type="number" id="ts-bill" step="0.01" min="0" value="100" oninput="tsRun()">
    </div>
    <div>
      <label>Tip percentage</label>
      <input type="number" id="ts-tip" step="0.5" min="0" value="15" oninput="tsRun()">
    </div>
  </div>
  <div class="row-2col" style="margin-top:0.7rem">
    <div>
      <label>Number of people</label>
      <input type="number" id="ts-people" step="1" min="1" value="4" oninput="tsRun()">
    </div>
    <div>
      <label>Currency symbol</label>
      <input type="text" id="ts-cur" maxlength="4" value="$" oninput="tsRun()">
    </div>
  </div>
  <div class="meta" style="margin-top:0.7rem">
    <label style="display:inline-flex;gap:0.4rem;align-items:center;color:var(--text-muted);font-size:0.85rem"><input type="checkbox" id="ts-round" onchange="tsRun()" style="width:auto"> Round per-person up to nearest whole unit (be generous)</label>
  </div>
  <div class="button-row" style="margin-top:0.7rem;flex-wrap:wrap">
    <button type="button" class="secondary" onclick="tsPreset(0)" style="padding:0.4rem 0.8rem;font-size:0.85rem">No tip</button>
    <button type="button" class="secondary" onclick="tsPreset(10)" style="padding:0.4rem 0.8rem;font-size:0.85rem">10%</button>
    <button type="button" class="secondary" onclick="tsPreset(15)" style="padding:0.4rem 0.8rem;font-size:0.85rem">15%</button>
    <button type="button" class="secondary" onclick="tsPreset(18)" style="padding:0.4rem 0.8rem;font-size:0.85rem">18%</button>
    <button type="button" class="secondary" onclick="tsPreset(20)" style="padding:0.4rem 0.8rem;font-size:0.85rem">20%</button>
    <button type="button" class="secondary" onclick="tsPreset(25)" style="padding:0.4rem 0.8rem;font-size:0.85rem">25%</button>
  </div>
</div>
<div class="tool-card">
  <label>{LBL_RESULT}</label>
  <div id="ts-out" class="output"></div>
</div>
""",
    "script": """
<style>
.ts-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:0.6rem;margin-bottom:0.5rem}
.ts-stat{background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;padding:0.7rem 0.85rem}
.ts-stat .ts-num{font-family:ui-monospace,monospace;font-size:1.3rem;font-weight:600;color:var(--accent)}
.ts-stat .ts-lbl{font-size:0.78rem;color:var(--text-muted);margin-top:0.15rem}
.ts-pp{margin-top:0.5rem;background:var(--accent);color:#fff;padding:0.85rem 1rem;border-radius:8px;text-align:center;font-family:ui-monospace,monospace;font-size:1.2rem;font-weight:600}
.ts-rounding{color:var(--text-muted);font-size:0.78rem;margin-top:0.4rem;text-align:center}
</style>
<script>
function tsFmt(n, cur){
  return cur + n.toFixed(2);
}
function tsPreset(p){
  document.getElementById('ts-tip').value = p;
  tsRun();
}
function tsRun(){
  const bill = parseFloat(document.getElementById('ts-bill').value) || 0;
  const tipPct = parseFloat(document.getElementById('ts-tip').value);
  const people = Math.max(1, Math.floor(parseFloat(document.getElementById('ts-people').value) || 1));
  const cur = document.getElementById('ts-cur').value || '';
  const round = document.getElementById('ts-round').checked;
  const out = document.getElementById('ts-out');
  if(!isFinite(bill) || bill < 0 || !isFinite(tipPct) || tipPct < 0){ out.textContent = '{LBL_NO_INPUT}'; return; }
  const tip = bill * tipPct / 100;
  const total = bill + tip;
  let pp = total / people;
  let bumpedTotal = total;
  let rounded = false;
  if(round){
    const ppCeil = Math.ceil(pp);
    if(ppCeil > pp){
      pp = ppCeil;
      bumpedTotal = ppCeil * people;
      rounded = true;
    }
  }
  out.innerHTML = `
    <div class="ts-grid">
      <div class="ts-stat"><div class="ts-num">${tsFmt(bill, cur)}</div><div class="ts-lbl">Bill</div></div>
      <div class="ts-stat"><div class="ts-num">${tsFmt(tip, cur)}</div><div class="ts-lbl">Tip (${tipPct}%)</div></div>
      <div class="ts-stat"><div class="ts-num">${tsFmt(bumpedTotal, cur)}</div><div class="ts-lbl">Grand total</div></div>
      <div class="ts-stat"><div class="ts-num">${people}</div><div class="ts-lbl">People</div></div>
    </div>
    <div class="ts-pp">${tsFmt(pp, cur)} per person</div>
    ${rounded ? `<div class="ts-rounding">Rounded up — total paid is ${tsFmt(bumpedTotal-total, cur)} above the bill+tip.</div>` : ''}
  `;
}
document.addEventListener('DOMContentLoaded', tsRun);
</script>
""",
    "help": {
        "en": """
<h2>What is this for?</h2>
<p>Splitting a restaurant bill at the end of dinner is the classic case of "easy maths, but the wine has been flowing". Three numbers go in (bill, tip percentage, number of people) and three come out (tip amount, grand total, per-person share). This tool does that without sending anything to a server, plus an optional round-up so the per-person figure lands on a whole unit and you tip a little more rather than juggling small change.</p>

<h3>When to use it</h3>
<ul>
  <li>End of a group meal — even split.</li>
  <li>Adding a known tip percentage to a service bill.</li>
  <li>Quickly testing different tip levels (10/15/18/20/25) before deciding.</li>
  <li>Settling a coffee round, a taxi, or any per-head share.</li>
</ul>

<h3>Common gotchas</h3>
<ul>
  <li><strong>Tipping convention varies wildly.</strong> United States: 18–22% is normal; under 15% is a complaint. Most of Europe: round up or 5–10%; service often included. Japan: don't tip — it can be considered rude. Always check local custom rather than blindly applying a percentage.</li>
  <li><strong>Tip on pre-tax or post-tax?</strong> In the US tipping on the pre-tax subtotal is common etiquette but most card terminals offer post-tax percentages. The tool computes the percentage of whatever bill total you enter — pick the base intentionally.</li>
  <li><strong>Service charge ≠ tip.</strong> If a "service charge" is already on the bill (common in UK groups of 6+ and most of continental Europe), additional tipping is optional. Some venues split service charges with the kitchen; tip cash directly if you want it to reach the server.</li>
  <li><strong>Per-person rounding can hide unequal eating.</strong> An even split is fastest but unfair if one person had wine and another had water — switch to itemised splitting in that case.</li>
  <li><strong>Cash vs card.</strong> Some staff prefer cash tips because card tips are pooled, taxed-immediately, or skimmed by the venue. If the per-person figure on this calculator includes the tip, decide whether you want to settle the tip in cash on top.</li>
</ul>
""",
        "pt": """
<h2>Para que serve?</h2>
<p>Rachar a conta de um restaurante no fim do jantar é o caso clássico de "matemática fácil, mas o vinho rolou". Três números entram (conta, porcentagem de gorjeta, número de pessoas) e três saem (valor da gorjeta, total geral, parte por pessoa). Esta ferramenta faz isso sem mandar nada para um servidor, mais uma opção de arredondar para cima, para que o valor por pessoa caia em uma unidade inteira e você dê uma gorjeta um pouco maior em vez de ficar mexendo com troco.</p>

<h3>Quando usar</h3>
<ul>
  <li>Fim de uma refeição em grupo — divisão igual.</li>
  <li>Adicionar uma porcentagem de gorjeta conhecida a uma conta de serviço.</li>
  <li>Testar rapidamente diferentes níveis de gorjeta (10/15/18/20/25) antes de decidir.</li>
  <li>Acertar uma rodada de café, um táxi ou qualquer parte por cabeça.</li>
</ul>

<h3>Pegadinhas comuns</h3>
<ul>
  <li><strong>Costume de gorjeta varia muito.</strong> Estados Unidos: 18–22% é normal; abaixo de 15% é reclamação. Maior parte da Europa: arredondar ou 5–10%; serviço em geral incluso. Japão: não dê gorjeta — pode ser visto como rude. Brasil: 10% é o padrão e geralmente já vem na conta. Sempre confira o costume local em vez de aplicar uma porcentagem cegamente.</li>
  <li><strong>Gorjeta sobre o valor antes ou depois de impostos?</strong> Nos EUA, dar gorjeta sobre o subtotal pré-imposto é etiqueta comum, mas a maioria das maquininhas oferece percentuais sobre o pós-imposto. A ferramenta calcula a porcentagem do total que você inserir — escolha a base de propósito.</li>
  <li><strong>Taxa de serviço ≠ gorjeta.</strong> Se uma "taxa de serviço" já está na conta (comum em grupos de 6+ no Reino Unido e na maior parte da Europa continental), gorjeta adicional é opcional. Alguns lugares dividem a taxa de serviço com a cozinha; dê gorjeta em dinheiro direto se você quiser que chegue ao garçom.</li>
  <li><strong>Arredondamento por pessoa pode esconder consumo desigual.</strong> Divisão igual é a mais rápida, mas injusta se uma pessoa tomou vinho e outra água — nesse caso, mude para divisão por item.</li>
  <li><strong>Dinheiro vs cartão.</strong> Alguns funcionários preferem gorjeta em dinheiro porque gorjetas no cartão são divididas, tributadas na hora ou retidas pela casa. Se o valor por pessoa nesta calculadora inclui a gorjeta, decida se quer acertar a gorjeta em dinheiro por cima.</li>
</ul>
""",
        "de": """
<h2>Wofür ist das?</h2>
<p>Eine Restaurantrechnung am Ende des Abends aufteilen ist einfache Mathematik — aber der Wein ist geflossen. Rechnung, Trinkgeld-% und Personenanzahl rein, Trinkgeld, Gesamtbetrag und Anteil pro Person raus. Optional Aufrunden, damit der Pro-Person-Betrag glatt wird.</p>
<h3>Wann verwenden</h3>
<ul>
<li>Nach einem gemeinsamen Essen — gleich aufgeteilt.</li>
<li>Trinkgeld-Prozentsatz auf eine Rechnung anwenden.</li>
<li>Verschiedene Trinkgeld-Stufen schnell vergleichen.</li>
<li>Kaffeerunde, Taxi oder andere Pro-Kopf-Beträge.</li>
</ul>
<h3>Häufige Stolperfallen</h3>
<ul>
<li><strong>Trinkgeldgepflogenheiten variieren.</strong> USA: 18–22%. Europa: aufrunden oder 5–10%. Japan: kein Trinkgeld — kann unhöflich wirken.</li>
<li><strong>Vor- oder nach Steuer?</strong> In den USA üblicherweise auf den Nettobetrag, Kartenleser bieten oft den Bruttobetrag.</li>
<li><strong>Servicecharge ≠ Trinkgeld.</strong> Bei bereits aufgeführtem Service ist zusätzliches Trinkgeld optional. Bargeld erreicht das Personal eher direkt.</li>
<li><strong>Gleicher Anteil ist unfair</strong>, wenn einer Wein hatte und der andere Wasser — dann posten-genau aufteilen.</li>
<li><strong>Bar oder Karte.</strong> Bargeld-Trinkgeld umgeht oft Pool und sofortige Versteuerung.</li>
</ul>
""",
        "es": """
<h2>¿Para qué sirve?</h2>
<p>Repartir la cuenta al final de una cena es matemática fácil, pero el vino ha corrido. Importe, % de propina y número de personas entran; propina, total y parte por persona salen. Redondeo opcional para que el por persona quede entero.</p>
<h3>Cuándo usarlo</h3>
<ul>
<li>Al final de una comida en grupo — partes iguales.</li>
<li>Aplicar un porcentaje de propina conocido.</li>
<li>Comparar rápidamente distintos porcentajes (10/15/18/20).</li>
<li>Café, taxi u otros gastos compartidos.</li>
</ul>
<h3>Errores comunes</h3>
<ul>
<li><strong>La costumbre varía.</strong> EE.UU.: 18–22%. Mayor parte de Europa: redondear o 5–10%. Japón: no se da propina.</li>
<li><strong>¿Antes o después de impuestos?</strong> En EE.UU. suele ser sobre el subtotal pre-tax; los TPV ofrecen post-tax.</li>
<li><strong>Servicio ≠ propina.</strong> Si ya hay un cargo de servicio, una propina extra es opcional.</li>
<li><strong>Repartir igual es injusto</strong> si uno tomó vino y otro agua — usa reparto por consumición.</li>
<li><strong>Efectivo vs tarjeta.</strong> En efectivo suele ir más directo al personal.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert ?</h2>
<p>Partager l'addition à la fin du dîner relève d'un calcul simple, mais le vin a coulé. Addition, % de pourboire et nombre de convives → pourboire, total et part par personne. Arrondi en option pour tomber sur un nombre rond.</p>
<h3>Quand l'utiliser</h3>
<ul>
<li>Fin d'un repas en groupe — partage égal.</li>
<li>Appliquer un pourcentage connu de pourboire.</li>
<li>Comparer rapidement plusieurs taux (10/15/18/20).</li>
<li>Café, taxi ou autre dépense partagée.</li>
</ul>
<h3>Pièges courants</h3>
<ul>
<li><strong>L'usage varie fortement.</strong> USA : 18–22 %. Europe : arrondir ou 5–10 %. Japon : pas de pourboire.</li>
<li><strong>Avant ou après taxes ?</strong> Aux USA souvent sur le HT ; les TPE proposent souvent le TTC.</li>
<li><strong>Service ≠ pourboire.</strong> Si le service est déjà compté, le pourboire est optionnel.</li>
<li><strong>Partage égal injuste</strong> si l'un a pris du vin et l'autre de l'eau — partage à l'item alors.</li>
<li><strong>Espèces vs carte.</strong> Le pourboire en liquide va plus directement au personnel.</li>
</ul>
""",
        "it": """
<h2>A cosa serve?</h2>
<p>Dividere il conto a fine cena è matematica facile — ma il vino è andato giù. Conto, % di mancia e numero di persone → mancia, totale e quota per persona. Arrotondamento opzionale per ottenere una cifra tonda.</p>
<h3>Quando usarlo</h3>
<ul>
<li>Fine di un pasto in gruppo — divisione paritaria.</li>
<li>Applicare una percentuale di mancia.</li>
<li>Confrontare rapidamente diverse percentuali (10/15/18/20).</li>
<li>Caffè, taxi o altre spese condivise.</li>
</ul>
<h3>Errori comuni</h3>
<ul>
<li><strong>La consuetudine varia.</strong> USA: 18–22%. Europa: arrotondare o 5–10%. Giappone: non si lascia mancia.</li>
<li><strong>Prima o dopo le tasse?</strong> Negli USA in genere sul subtotale; i POS offrono il post-IVA.</li>
<li><strong>Coperto/servizio ≠ mancia.</strong> Se è già in conto, la mancia è opzionale.</li>
<li><strong>Divisione paritaria iniqua</strong> se uno ha preso vino e l'altro acqua — meglio dividere per voce.</li>
<li><strong>Contanti vs carta.</strong> La mancia in contanti spesso arriva più direttamente al personale.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy?</h2>
<p>Podział restauracyjnego rachunku na końcu kolacji to klasyczny przypadek "łatwa matma, ale wino płynęło". Trzy liczby na wejściu (rachunek, procent napiwku, liczba osób) i trzy na wyjściu (kwota napiwku, suma całkowita, udział na osobę). To narzędzie robi to bez wysyłania czegokolwiek na serwer, plus opcjonalne zaokrąglenie w górę, żeby kwota na osobę wpadła na okrągłą jednostkę i napiwek wyszedł trochę większy zamiast żonglerki drobnymi.</p>

<h3>Kiedy tego użyć</h3>
<ul>
  <li>Koniec posiłku w grupie — równy podział.</li>
  <li>Doliczanie znanego procentu napiwku do rachunku za usługę.</li>
  <li>Szybkie testowanie różnych poziomów napiwku (10/15/18/20/25) przed decyzją.</li>
  <li>Rozliczenie rundy kawy, taxi albo dowolnej składki na osobę.</li>
</ul>

<h3>Częste pułapki</h3>
<ul>
  <li><strong>Konwencje napiwków bardzo się różnią.</strong> USA: 18–22% to norma; poniżej 15% to skarga. Większość Europy: zaokrąglić albo 5–10%; serwis często wliczony. Polska: 10% to typowy ukłon, ale nie obowiązkowy. Japonia: nie dawaj napiwku — może zostać odebrany jako niegrzeczność. Zawsze sprawdzaj lokalny obyczaj zamiast ślepo aplikować procent.</li>
  <li><strong>Napiwek od kwoty przed czy po podatku?</strong> W USA dawanie napiwku od subtotalu pre-tax to typowa etykieta, ale większość terminali kart oferuje procenty od kwoty po podatku. Narzędzie liczy procent od kwoty rachunku, którą wpiszesz — wybierz bazę świadomie.</li>
  <li><strong>Service charge ≠ napiwek.</strong> Jeśli "service charge" jest już w rachunku (typowe w UK przy 6+ osobach i większości kontynentalnej Europy), dodatkowy napiwek jest opcjonalny. Niektóre lokale dzielą service charge z kuchnią; daj napiwek gotówką wprost, jeśli chcesz, żeby trafił do kelnera.</li>
  <li><strong>Zaokrąglenie na osobę może ukryć nierówne jedzenie.</strong> Równy podział jest najszybszy, ale niesprawiedliwy, gdy jedna osoba miała wino, a druga wodę — w takim wypadku przejdź na podział pozycyjny.</li>
  <li><strong>Gotówka vs karta.</strong> Niektóra obsługa woli napiwki w gotówce, bo karciane są dzielone, opodatkowane od razu albo skubane przez lokal. Jeśli kwota na osobę w tym kalkulatorze zawiera napiwek, zdecyduj, czy chcesz dorzucić napiwek w gotówce na wierzch.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>食事の終わりにレストランの会計を割るのは、「計算は簡単だがワインが入ったあと」の典型例です。3 つの数（請求額、チップ率、人数）を入れて、3 つの数（チップ額、合計、1 人あたり）を出します。本ツールはサーバーに何も送らずにこれを行い、1 人あたりが端数なくキリの良い金額になるよう切り上げるオプションもあります。</p>

<h3>使うべきタイミング</h3>
<ul>
  <li>グループ食事の最後に、均等割で分けたいとき。</li>
  <li>サービス料金に既知のチップ率を上乗せしたいとき。</li>
  <li>10/15/18/20/25 など複数のチップ率を素早く比較したいとき。</li>
  <li>コーヒー代、タクシー代など、人数で割りたい場面。</li>
</ul>

<h3>よくある注意点</h3>
<ul>
  <li><strong>チップの慣習は地域差が大きいです。</strong> 米国は 18〜22% が普通、15% 未満は不満の意思表示。欧州の多くは切り上げか 5〜10%、サービス料込みのことも多い。日本ではチップは不要で、むしろ失礼に取られることもあります。安易にパーセンテージを当てる前に、現地の慣習を確認してください。</li>
  <li><strong>税抜き／税込みのどちらに対するチップ？</strong> 米国では税抜き小計に対するのが一般的ですが、カード端末は税込みでパーセンテージを提示しがちです。本ツールは入力した金額に対する % を計算するので、基準値は意図して選んでください。</li>
  <li><strong>サービス料 ≠ チップ。</strong> イギリスの 6 名以上のグループ、欧州大陸の多くで会計に「サービス料」が含まれている場合、追加チップは任意です。サービス料の一部を厨房に分配する店もあるので、サーバー本人へ確実に渡したいなら現金で直接渡してください。</li>
  <li><strong>1 人あたり丸め込みは食事量の差を覆い隠します。</strong> 均等割は早いですが、ワインを飲んだ人と水だけの人がいる場合は不公平です。その場合は項目別の割り勘に切り替えてください。</li>
  <li><strong>現金とカード。</strong> カードでのチップはプール、即時課税、店側のピンハネが起きる場合があるため、現金チップを好むスタッフもいます。本ツールの 1 人あたり額にチップが含まれているかどうかを確認し、必要なら現金で別に渡すことを検討してください。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor is dit?</h2>
<p>Een restaurantrekening splitsen aan het einde van het diner is het klassieke geval van "makkelijke rekensom, maar de wijn heeft gevloeid". Drie nummers gaan erin (rekening, tip-percentage, aantal personen) en drie komen eruit (tip-bedrag, grand total, per-persoon-aandeel). Deze tool doet dat zonder iets naar een server te sturen, plus een optionele round-up zodat het per-persoon-getal op een hele eenheid landt en je iets meer fooi geeft in plaats van met klein geld te jongleren.</p>

<h3>Wanneer gebruiken</h3>
<ul>
  <li>Einde van een groepsmaaltijd — even split.</li>
  <li>Een bekend tip-percentage optellen bij een service-rekening.</li>
  <li>Snel verschillende tip-niveaus testen (10/15/18/20/25) voor je beslist.</li>
  <li>Een koffierondje, een taxi of elk per-hoofd-aandeel beslechten.</li>
</ul>

<h3>Veelvoorkomende valkuilen</h3>
<ul>
  <li><strong>Fooi-conventies verschillen sterk.</strong> VS: 18–22% is normaal; onder 15% is een klacht. Nederland en de meeste van Europa: afronden of 5–10%; service vaak inbegrepen. Japan: niet fooien — het kan onbeleefd zijn. Check altijd lokaal gebruik in plaats van blind een percentage toe te passen.</li>
  <li><strong>Fooi op pre-tax of post-tax?</strong> In de VS is fooi over de pre-tax subtotal gangbare etiquette maar de meeste betaalterminals bieden post-tax-percentages. De tool berekent het percentage van welk rekeningtotaal je ook invoert — kies de basis bewust.</li>
  <li><strong>Service charge ≠ fooi.</strong> Als een "service charge" al op de rekening staat (gangbaar in UK groepen van 6+ en de meeste van continentaal Europa), is extra fooi optioneel. Sommige venues splitsen service charges met de keuken; geef cash-fooi direct als je wil dat het de bediening bereikt.</li>
  <li><strong>Per-persoon-afronding kan ongelijk eten verbergen.</strong> Een even split is het snelst maar oneerlijk als één persoon wijn had en een ander water — schakel in dat geval naar itemised splitting.</li>
  <li><strong>Cash vs card.</strong> Sommige medewerkers prefereren cash-fooi omdat card-fooien gepoold, direct belast of door de venue gestreken worden. Als het per-persoon-bedrag op deze calculator de fooi bevat, besluit of je de fooi cash bovenop wil voldoen.</li>
</ul>
""",
        "tr": """
<h2>Bu ne işe yarar?</h2>
<p>Akşam yemeğinin sonunda bir restoran hesabını bölmek "kolay matematik, ama şarap akıyor"un klasik durumudur. Üç sayı girer (hesap, tip yüzdesi, kişi sayısı) ve üçü çıkar (tip tutarı, genel toplam, kişi başı pay). Bu araç sunucuya hiçbir şey göndermeden bunu yapar, artı isteğe bağlı yuvarlama, böylece kişi başı rakam tam bir birime düşer ve küçük bozuklukla cebelleşmek yerine biraz fazla tip verirsin.</p>

<h3>Ne zaman kullanılır</h3>
<ul>
  <li>Bir grup yemeğinin sonu — eşit bölme.</li>
  <li>Hizmet faturasına bilinen bir tip yüzdesi ekleme.</li>
  <li>Karar vermeden önce farklı tip seviyelerini (10/15/18/20/25) hızlıca test etme.</li>
  <li>Bir kahve turu, bir taksi veya kişi başı herhangi bir payı çözme.</li>
</ul>

<h3>Sık yapılan hatalar</h3>
<ul>
  <li><strong>Tip konvansiyonu vahşice değişir.</strong> Amerika Birleşik Devletleri: %18–22 normaldir; %15 altı bir şikayettir. Çoğu Avrupa: yuvarla veya %5–10; servis sıklıkla dahildir. Japonya: tip verme — kaba kabul edilebilir. Yüzdeyi körü körüne uygulamak yerine her zaman yerel adetleri kontrol et.</li>
  <li><strong>Vergi öncesi mi vergi sonrası tip mi?</strong> ABD'de vergi öncesi ara toplamda tip vermek yaygın görgüdür ama çoğu kart terminali vergi sonrası yüzdeler sunar. Araç girdiğin hesap totalinin yüzdesini hesaplar — temeli kasıtlı olarak seç.</li>
  <li><strong>Hizmet ücreti ≠ tip.</strong> Hesapta zaten bir "hizmet ücreti" varsa (6+ kişilik İngiltere gruplarında ve çoğu kıta Avrupa'sında yaygın), ek tip vermek isteğe bağlıdır. Bazı mekanlar hizmet ücretlerini mutfakla böler; sunucuya ulaşmasını istiyorsan doğrudan nakit tip ver.</li>
  <li><strong>Kişi başına yuvarlama eşit olmayan yemeyi gizleyebilir.</strong> Eşit bölme en hızlıdır ama biri şarap içtiyken diğeri su içtiyse adil değildir — bu durumda kalemli bölüşmeye geç.</li>
  <li><strong>Nakit - kart.</strong> Bazı personel nakit tipleri tercih eder çünkü kart tipleri toplanır, hemen vergilendirilir veya mekan tarafından sıyrılır. Bu hesaplayıcıdaki kişi başı rakam tip'i içeriyorsa, tip'i üstüne nakit olarak kapatmak isteyip istemediğine karar ver.</li>
</ul>
""",
        "id": """
<h2>Untuk apa ini?</h2>
<p>Membagi tagihan restoran di akhir makan malam adalah contoh klasik "matematikanya mudah, tapi wine-nya sudah mengalir". Tiga angka masuk (tagihan, persentase tip, jumlah orang) dan tiga keluar (jumlah tip, total keseluruhan, bagian per orang). Tool ini melakukan itu tanpa mengirim apa pun ke server, plus opsi round-up sehingga angka per orang jatuh ke unit bulat dan kamu kasih tip sedikit lebih banyak daripada repot dengan recehan kecil.</p>

<h3>Kapan digunakan</h3>
<ul>
  <li>Akhir makan grup — split rata.</li>
  <li>Menambahkan persentase tip yang sudah diketahui ke tagihan layanan.</li>
  <li>Cepat menguji berbagai level tip (10/15/18/20/25) sebelum memutuskan.</li>
  <li>Menyelesaikan ronde kopi, taksi, atau bagian per kepala apa pun.</li>
</ul>

<h3>Kesalahan umum</h3>
<ul>
  <li><strong>Konvensi tip sangat bervariasi.</strong> Amerika Serikat: 18–22% itu normal; di bawah 15% adalah keluhan. Sebagian besar Eropa: bulatkan ke atas atau 5–10%; service sering sudah termasuk. Jepang: jangan kasih tip — bisa dianggap kasar. Selalu cek kebiasaan lokal daripada menerapkan persentase secara membabi buta.</li>
  <li><strong>Tip pre-tax atau post-tax?</strong> Di AS, kasih tip dari subtotal pre-tax itu etiket umum tapi sebagian besar terminal kartu menawarkan persentase post-tax. Tool ini menghitung persentase dari total tagihan yang kamu masukkan — pilih base-nya secara sengaja.</li>
  <li><strong>Service charge ≠ tip.</strong> Jika "service charge" sudah ada di tagihan (umum di grup 6+ orang di UK dan sebagian besar Eropa kontinental), tip tambahan sifatnya opsional. Beberapa tempat membagi service charge dengan dapur; kasih tip cash langsung jika kamu ingin sampai ke server.</li>
  <li><strong>Pembulatan per orang bisa menyembunyikan makan yang tidak setara.</strong> Split rata itu paling cepat tapi tidak adil jika satu orang minum wine dan yang lain minum air — beralih ke itemised splitting dalam kasus itu.</li>
  <li><strong>Cash vs kartu.</strong> Sebagian staf lebih suka tip cash karena tip kartu di-pool, langsung kena pajak, atau dipotong tempat. Jika angka per orang di kalkulator ini sudah termasuk tip, putuskan apakah kamu ingin melunasi tip secara cash di atasnya.</li>
</ul>
""",
        "vi": """
<h2>Công cụ này để làm gì?</h2>
<p>Tính tip và chia hóa đơn nhà hàng giữa nhóm trông đơn giản nhưng dễ sai khi mọi người ăn không đều và có người muốn round-up. Tool này thực hiện toán: tổng hóa đơn + % tip + chia số người, với tùy chọn round-up đến đồng tiền gần nhất.</p>

<h3>Khi nào nên dùng</h3>
<ul>
  <li>Chia tab nhà hàng đều giữa nhóm.</li>
  <li>Tính tip cho dịch vụ với % tip khu vực không quen thuộc.</li>
  <li>Round-up tip thành số đẹp khi trả mặt.</li>
</ul>

<h3>Lưu ý thường gặp</h3>
<ul>
  <li><strong>Tip pre-tax vs post-tax.</strong> Tip theo tradition tính trên subtotal trước thuế; nhiều người mặc định trên total có thuế (mà bao gồm tip nhiều hơn 8-10%).</li>
  <li><strong>Quy ước tip khác nhau theo quốc gia.</strong> 15-20% chuẩn Mỹ; nhiều nước châu Âu thêm service charge tự động và tip thêm là tùy chọn; Nhật không có tip.</li>
  <li><strong>Đều khác công bằng.</strong> Nếu một người ăn đắt hơn nhiều, "chia đều" có thể không công bằng. Tool này giả định chia đều — đối với split không đều, tính từng cái một.</li>
</ul>
""",
    },
    "related": ["percentage-calculator", "bmi-calculator", "unit-converter"],
    "howto": {"flow": "calculate", "action": "format",  "noun": "bill"},
}
