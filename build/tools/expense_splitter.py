TOOL = {
    "slug": "expense-splitter",
    "category": "math",
    "icon": "👥",
    "tags": ["split", "expense", "bill", "group", "share", "even", "uneven", "travel"],
    "i18n": {
        "en": {
            "name": "Expense Splitter",
            "tagline": "Split a group expense evenly or by custom shares (percentages or fixed amounts). Output per-person totals + transfer instructions ('A owes B €X').",
            "description": "Free in-browser expense splitter. Add expenses (who paid, amount, who owes), define groups, get per-person balance + minimal-transfers settlement ('Alice owes Bob €X' format). Supports uneven splits (one person owes more, etc.) and multiple currencies (single currency per group; conversion not done). For trips, shared apartments, group dinners.",
        },
        "de": {
            "name": "Ausgaben-Splitter",
            "tagline": "Gruppenausgaben gleichmäßig oder mit benutzerdefinierten Anteilen (Prozente oder feste Beträge) aufteilen. Ausgabe: Salden pro Person + Überweisungsanweisungen („A schuldet B X €“).",
            "description": "Kostenloser Ausgaben-Splitter im Browser. Ausgaben hinzufügen (wer hat gezahlt, Betrag, wer schuldet), Gruppe definieren, Saldo pro Person + minimale Überweisungen erhalten („Alice schuldet Bob X €“). Unterstützt ungleiche Aufteilungen (eine Person zahlt mehr usw.) und mehrere Währungen (eine Währung pro Gruppe; keine Umrechnung). Für Reisen, WGs, Gruppen-Dinner.",
        },
        "es": {
            "name": "Divisor de Gastos",
            "tagline": "Divide un gasto grupal a partes iguales o por cuotas personalizadas (porcentajes o importes fijos). Salida: totales por persona + instrucciones de transferencia ('A debe a B X €').",
            "description": "Divisor de gastos gratuito en el navegador. Añade gastos (quién pagó, importe, quién debe), define grupos, obtén el balance por persona + liquidación con transferencias mínimas ('Alice debe a Bob X €'). Soporta divisiones desiguales (uno paga más, etc.) y múltiples divisas (una por grupo; no se hace conversión). Para viajes, pisos compartidos, cenas de grupo.",
        },
        "fr": {
            "name": "Diviseur de Dépenses",
            "tagline": "Divisez une dépense de groupe à parts égales ou par parts personnalisées (pourcentages ou montants fixes). Sortie : totaux par personne + instructions de virement (« A doit B X € »).",
            "description": "Diviseur de dépenses gratuit dans le navigateur. Ajoutez des dépenses (qui a payé, montant, qui doit), définissez le groupe, obtenez le solde par personne + règlement à virements minimaux (« Alice doit Bob X € »). Gère les partages inégaux (une personne paie plus, etc.) et plusieurs devises (une seule par groupe ; pas de conversion). Pour voyages, colocations, dîners de groupe.",
        },
        "it": {
            "name": "Divisore di Spese",
            "tagline": "Dividi una spesa di gruppo equamente o con quote personalizzate (percentuali o importi fissi). Output: totali per persona + istruzioni di trasferimento ('A deve a B X €').",
            "description": "Divisore di spese gratuito nel browser. Aggiungi spese (chi ha pagato, importo, chi deve), definisci gruppi, ottieni saldo per persona + regolamento a trasferimenti minimi ('Alice deve a Bob X €'). Supporta divisioni non paritarie (una persona deve di più, ecc.) e valute multiple (una sola valuta per gruppo; conversione non fatta). Per viaggi, coinquilini, cene di gruppo.",
        },
        "pt": {
            "name": "Divisor de Despesas",
            "tagline": "Divide uma despesa em grupo igualmente ou por quotas personalizadas (percentagens ou valores fixos). Saída: totais por pessoa + instruções de transferência ('A deve a B €X').",
            "description": "Divisor de despesas gratuito no navegador. Adicione despesas (quem pagou, valor, quem deve), defina grupos, obtenha saldo por pessoa + acerto com transferências mínimas ('Alice deve a Bob €X'). Suporta divisões desiguais (uma pessoa deve mais, etc.) e várias moedas (uma por grupo; sem conversão). Para viagens, apartamentos partilhados, jantares de grupo.",
        },
        "pl": {
            "name": "Dzielnik Wydatków",
            "tagline": "Podziel wydatek grupowy po równo lub własnymi udziałami (procenty lub kwoty stałe). Wynik: kwoty per osoba + instrukcje przelewu ('A wisi B X €').",
            "description": "Darmowy dzielnik wydatków w przeglądarce. Dodawaj wydatki (kto zapłacił, kwota, kto winien), zdefiniuj grupę, dostań saldo per osoba + rozliczenie z minimalną liczbą przelewów ('Alice winna Bobowi X €'). Obsługuje nierówne podziały (jedna osoba winna więcej itp.) i wiele walut (jedna na grupę; bez konwersji). Dla wyjazdów, mieszkań współdzielonych, kolacji grupowych.",
        },
        "ja": {
            "name": "経費割り勘ツール",
            "tagline": "グループの支出を均等または独自の割合（パーセントや固定額）で分割。出力は各自の残高と振込指示（「A は B に X 円返す」）。",
            "description": "ブラウザだけで動く無料の経費割り勘ツール。支出（誰が払ったか、金額、誰が負担するか）を追加し、グループを定義すると、各自の純残高と最小限の振込で精算する手順（「Alice は Bob に X 円返す」）を得られます。不均等な分担（一人が多めに負担、など）に対応し、グループあたり 1 通貨を扱えます（換算は行いません）。旅行・シェアハウス・グループでの食事に便利。",
        },
        "nl": {
            "name": "Uitgavenverdeler",
            "tagline": "Splits een groepsuitgave gelijk of met aangepaste delen (percentages of vaste bedragen). Uitvoer: totaal per persoon + overboekingsinstructies ('A schuldt B €X').",
            "description": "Gratis in-browser uitgavenverdeler. Voeg uitgaven toe (wie betaalde, bedrag, wie schuldt), definieer groepen, krijg saldo per persoon + afrekening met minimale overboekingen ('Alice schuldt Bob €X'). Ondersteunt ongelijke splits (één persoon schuldt meer enz.) en meerdere valuta (één per groep; geen conversie). Voor reizen, gedeelde appartementen, groepsdiners.",
        },
        "tr": {
            "name": "Masraf Bölüştürücü",
            "tagline": "Bir grup masrafını eşit veya özel paylarla (yüzde veya sabit tutar) böl. Çıktı: kişi başına toplam + transfer talimatı ('A, B'ye €X borçlu').",
            "description": "Tarayıcıda çalışan ücretsiz masraf bölüştürücü. Masraf ekle (kim ödedi, tutar, kim borçlu), grup tanımla, kişi başı net bakiye + minimum transferli kapanış al ('Alice, Bob'a €X borçlu'). Eşit olmayan bölüşmeyi (biri daha fazla borçlu vb.) ve birden çok para birimini destekler (grup başına tek para birimi; çeviri yapılmaz). Geziler, ev arkadaşlığı, grup yemekleri için.",
        },
        "id": {
            "name": "Pembagi Pengeluaran",
            "tagline": "Bagi pengeluaran grup rata atau dengan share custom (persentase atau jumlah tetap). Output: total per orang + instruksi transfer ('A utang ke B €X').",
            "description": "Pembagi pengeluaran gratis di browser. Tambahkan pengeluaran (siapa bayar, jumlah, siapa utang), definisikan grup, dapatkan saldo per orang + settlement dengan transfer minimal ('Alice utang ke Bob €X'). Mendukung pembagian tidak rata (satu orang utang lebih banyak, dll.) dan banyak mata uang (satu mata uang per grup; tanpa konversi). Untuk perjalanan, kos-kosan, makan grup.",
        },
        "vi": {
            "name": "Chia Chi Phí",
            "tagline": "Chia một chi phí nhóm đều nhau hoặc theo phần tùy chỉnh (tỷ lệ phần trăm hoặc số tiền cố định). Đầu ra: tổng theo người + chỉ dẫn chuyển khoản ('A nợ B €X').",
            "description": "Bộ chia chi phí miễn phí trong trình duyệt. Thêm chi phí (ai trả, số tiền, ai nợ), xác định nhóm, nhận số dư mỗi người + thanh toán với số chuyển khoản tối thiểu ('Alice nợ Bob €X'). Hỗ trợ chia không đều (một người nợ nhiều hơn, v.v.) và nhiều tiền tệ (một tiền tệ mỗi nhóm; không chuyển đổi). Cho chuyến đi, ở chung, ăn nhóm.",
        },
        "hi": {
            "name": "Expense Splitter",
            "tagline": "Group expense को बराबर या custom shares (percentages या fixed amounts) में split करें। Output: per-person totals + transfer instructions ('A, B को €X देय')।",
            "description": "Free in-browser expense splitter। Expenses जोड़ें (किसने pay किया, amount, कौन देय), groups define करें, per-person balance + minimal-transfers settlement पाएं ('Alice, Bob को €X देय' format में)। Uneven splits support करता है (एक व्यक्ति ज़्यादा देय आदि) और multiple currencies (group में एक currency; conversion नहीं)। Trips, shared apartments, group dinners के लिए।",
        },
        "sk": {
            "name": "Delič výdavkov",
            "tagline": "Rozdeľ skupinový výdavok rovnomerne alebo vlastnými podielmi (percentá alebo pevné sumy). Výstup: súčty na osobu + pokyny na prevody („A dlhuje B €X“).",
            "description": "Bezplatný delič výdavkov v prehliadači. Pridaj výdavky (kto platil, suma, kto je dlžný), definuj skupinu, dostaň zostatok na osobu + vyrovnanie s minimálnym počtom prevodov („Alice dlhuje Bobovi €X“). Podporuje nerovnomerné rozdelenia (jeden dlhuje viac atď.) a viacero mien (jedna mena na skupinu; bez konverzie). Na výlety, spoločné byty, skupinové večere.",
        },
        "cs": {
            "name": "Dělič výdajů",
            "tagline": "Rozděl skupinový výdaj rovnoměrně nebo vlastními podíly (procenta nebo pevné částky). Výstup: součty na osobu + pokyny k převodům („A dluží B €X“).",
            "description": "Bezplatný dělič výdajů v prohlížeči. Přidej výdaje (kdo platil, částka, kdo je dlužen), definuj skupinu, dostaň zůstatek na osobu + vyrovnání s minimálním počtem převodů („Alice dluží Bobovi €X“). Podporuje nerovnoměrná rozdělení (jeden dluží více atd.) a více měn (jedna měna na skupinu; bez konverze). Na výlety, sdílené byty, skupinové večeře.",
        },
    },
    "body": """
<div class="tool-card">
  <div class="row-2col">
    <div>
      <label>Group name (optional)</label>
      <input type="text" id="es-group" value="Weekend trip" oninput="esRun()">
    </div>
    <div>
      <label>Currency</label>
      <select id="es-cur" onchange="esRun()">
        <option value="€">€ EUR</option>
        <option value="$">$ USD</option>
        <option value="£">£ GBP</option>
        <option value="¥">¥ JPY</option>
        <option value="CHF ">CHF</option>
        <option value="kr ">SEK / NOK / DKK kr</option>
        <option value="zł ">PLN zł</option>
        <option value="Kč ">CZK Kč</option>
        <option value="₹">₹ INR</option>
        <option value="₺">₺ TRY</option>
        <option value="R$">R$ BRL</option>
      </select>
    </div>
  </div>
</div>

<div class="tool-card">
  <label>Members</label>
  <div class="es-members" id="es-members"></div>
  <div class="button-row" style="margin-top:0.5rem">
    <input type="text" id="es-new-name" placeholder="Add member name" style="max-width:200px" onkeydown="if(event.key==='Enter'){esAddMember();event.preventDefault();}">
    <button type="button" class="secondary" onclick="esAddMember()">+ Add member</button>
  </div>
</div>

<div class="tool-card">
  <label>Expenses</label>
  <div id="es-expenses"></div>
  <div class="button-row" style="margin-top:0.5rem">
    <button type="button" class="secondary" onclick="esAddExpense()">+ Add expense</button>
    <button type="button" class="secondary" onclick="esSaveState()">🔗 Save state in URL</button>
  </div>
</div>

<div class="tool-card">
  <label>Per-person balance</label>
  <div id="es-balances" class="es-balances"></div>
</div>

<div class="tool-card">
  <label>Settlement — minimum transfers</label>
  <div id="es-settlement" class="es-settlement"></div>
  <div class="meta" style="margin-top:0.4rem;color:var(--text-muted);font-size:0.82rem">
    Greedy algorithm: largest debtor pays largest creditor until everyone clears.
    This is usually optimal but not always provably minimum for adversarial cases.
  </div>
</div>
""",
    "script": """
<style>
.es-members{display:flex;gap:0.5rem;flex-wrap:wrap}
.es-mem-chip{background:var(--bg-elev);border:1px solid var(--border);padding:0.35rem 0.4rem 0.35rem 0.65rem;border-radius:999px;display:inline-flex;align-items:center;gap:0.3rem;font-size:0.92rem}
.es-mem-chip .es-mem-del{background:transparent;border:none;color:var(--text-muted);cursor:pointer;font-size:1.1rem;line-height:1;padding:0 0.15rem}
.es-mem-chip .es-mem-del:hover{color:#e11d48}
.es-exp{border:1px solid var(--border);border-radius:8px;padding:0.7rem 0.9rem;margin-bottom:0.6rem;background:var(--bg-elev)}
.es-exp-head{display:flex;gap:0.5rem;flex-wrap:wrap;align-items:center}
.es-exp-head input.es-desc{flex:1 1 200px;min-width:140px}
.es-exp-head input.es-amt{width:120px;text-align:right;font-family:ui-monospace,monospace}
.es-exp-head select.es-payer, .es-exp-head select.es-mode{padding:0.4rem}
.es-exp-head .es-exp-del{background:transparent;color:var(--text-muted);border:1px solid var(--border);padding:0.3rem 0.55rem;font-size:0.9rem;cursor:pointer;border-radius:4px}
.es-exp-split{margin-top:0.6rem;padding-top:0.5rem;border-top:1px dashed var(--border)}
.es-exp-split label.es-share{display:inline-flex;align-items:center;gap:0.4rem;margin:0.2rem 0.7rem 0.2rem 0;font-size:0.9rem}
.es-exp-split label.es-share input[type=number]{width:80px;font-family:ui-monospace,monospace;font-size:0.9rem;padding:0.3rem}
.es-exp-split label.es-share input[type=checkbox]{width:auto}
.es-balances{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:0.5rem}
.es-bal{background:var(--bg-elev);border:1px solid var(--border);border-radius:8px;padding:0.55rem 0.8rem;font-family:ui-monospace,monospace}
.es-bal-name{font-weight:600;margin-bottom:0.2rem}
.es-bal-pos{color:#059669}
.es-bal-neg{color:#dc2626}
.es-bal-zero{color:var(--text-muted)}
.es-settlement{font-family:ui-monospace,monospace}
.es-pay{padding:0.4rem 0.6rem;border-left:3px solid var(--accent);margin-bottom:0.35rem;background:var(--bg-elev);border-radius:4px}
.es-zero-msg{padding:0.5rem;color:var(--text-muted);font-style:italic;font-family:system-ui,sans-serif}
.es-warn{background:#fff7ed;border:1px solid #fed7aa;color:#9a3412;padding:0.5rem 0.7rem;border-radius:4px;font-size:0.88rem;margin-bottom:0.5rem;font-family:system-ui,sans-serif}
:root[data-theme="dark"] .es-warn{background:#3b1d0d;border-color:#7c2d12;color:#fed7aa}
</style>
<script>
let ES_STATE = {
  members: ['Alice', 'Bob', 'Charlie'],
  expenses: []  // {id, desc, payer, amount, mode:'equal'|'percent'|'fixed', participants:Set, shares:{name:number}}
};
let ES_NEXT_ID = 1;

function esCur(){ return document.getElementById('es-cur').value; }
function esFmt(n){
  const sym = esCur();
  if(!isFinite(n)) return sym + '0.00';
  return sym + (n >= 0 ? '' : '−') + Math.abs(n).toFixed(2);
}
function esRenderMembers(){
  const host = document.getElementById('es-members');
  host.innerHTML = '';
  ES_STATE.members.forEach(function(name, i){
    const chip = document.createElement('span');
    chip.className = 'es-mem-chip';
    const span = document.createElement('span');
    span.textContent = name;
    chip.appendChild(span);
    const del = document.createElement('button');
    del.className = 'es-mem-del';
    del.type = 'button';
    del.textContent = '×';
    del.title = 'Remove member';
    del.onclick = function(){ esRemoveMember(i); };
    chip.appendChild(del);
    host.appendChild(chip);
  });
}
function esAddMember(){
  const inp = document.getElementById('es-new-name');
  const name = (inp.value || '').trim();
  if(!name) return;
  if(ES_STATE.members.indexOf(name) >= 0){ inp.value=''; return; }
  ES_STATE.members.push(name);
  inp.value = '';
  // Add new member to all expenses' default participants
  ES_STATE.expenses.forEach(function(e){
    e.participants[name] = true;
    if(e.mode === 'percent' || e.mode === 'fixed') e.shares[name] = 0;
  });
  esRender();
}
function esRemoveMember(i){
  const name = ES_STATE.members[i];
  ES_STATE.members.splice(i, 1);
  // Strip from expenses
  ES_STATE.expenses.forEach(function(e){
    delete e.participants[name];
    delete e.shares[name];
    if(e.payer === name) e.payer = ES_STATE.members[0] || '';
  });
  esRender();
}
function esAddExpense(){
  if(ES_STATE.members.length === 0){ alert('Add members first.'); return; }
  const participants = {};
  ES_STATE.members.forEach(function(n){ participants[n] = true; });
  const shares = {};
  ES_STATE.members.forEach(function(n){ shares[n] = 0; });
  ES_STATE.expenses.push({
    id: ES_NEXT_ID++,
    desc: 'Expense ' + ES_STATE.expenses.length,
    payer: ES_STATE.members[0],
    amount: 50,
    mode: 'equal',
    participants: participants,
    shares: shares
  });
  esRender();
}
function esRemoveExpense(id){
  ES_STATE.expenses = ES_STATE.expenses.filter(function(e){ return e.id !== id; });
  esRender();
}
function esRenderExpenses(){
  const host = document.getElementById('es-expenses');
  host.innerHTML = '';
  if(ES_STATE.expenses.length === 0){
    host.innerHTML = '<div class="es-zero-msg">No expenses yet. Click "Add expense" to start.</div>';
    return;
  }
  ES_STATE.expenses.forEach(function(e){
    const row = document.createElement('div');
    row.className = 'es-exp';
    let payerOpts = ES_STATE.members.map(function(n){
      return '<option value="' + n + '"' + (n === e.payer ? ' selected' : '') + '>' + n + '</option>';
    }).join('');
    row.innerHTML =
      '<div class="es-exp-head">' +
        '<input type="text" class="es-desc" value="' + e.desc.replace(/"/g, '&quot;') + '" placeholder="Description">' +
        '<select class="es-payer">' + payerOpts + '</select>' +
        '<span class="meta" style="font-size:0.85rem">paid</span>' +
        '<input type="number" class="es-amt" step="0.01" min="0" value="' + e.amount + '">' +
        '<select class="es-mode">' +
          '<option value="equal"' + (e.mode==='equal'?' selected':'') + '>Equal split</option>' +
          '<option value="percent"' + (e.mode==='percent'?' selected':'') + '>% shares</option>' +
          '<option value="fixed"' + (e.mode==='fixed'?' selected':'') + '>Fixed amounts</option>' +
        '</select>' +
        '<button type="button" class="es-exp-del">×</button>' +
      '</div>' +
      '<div class="es-exp-split"></div>';
    // Bind handlers
    row.querySelector('.es-desc').oninput = function(ev){ e.desc = ev.target.value; esCompute(); };
    row.querySelector('.es-payer').onchange = function(ev){ e.payer = ev.target.value; esCompute(); };
    row.querySelector('.es-amt').oninput = function(ev){ e.amount = parseFloat(ev.target.value) || 0; esCompute(); };
    row.querySelector('.es-mode').onchange = function(ev){ e.mode = ev.target.value; esRender(); };
    row.querySelector('.es-exp-del').onclick = function(){ esRemoveExpense(e.id); };
    // Split detail
    const split = row.querySelector('.es-exp-split');
    if(e.mode === 'equal'){
      ES_STATE.members.forEach(function(n){
        const lbl = document.createElement('label');
        lbl.className = 'es-share';
        lbl.innerHTML = '<input type="checkbox"' + (e.participants[n] ? ' checked' : '') + '> ' + n;
        const cb = lbl.querySelector('input');
        cb.onchange = function(){ e.participants[n] = cb.checked; esCompute(); };
        split.appendChild(lbl);
      });
    } else {
      const note = document.createElement('div');
      note.className = 'meta';
      note.style.cssText = 'font-size:0.82rem;color:var(--text-muted);margin-bottom:0.3rem';
      note.textContent = e.mode === 'percent' ? 'Shares as % of expense (should sum to 100)' : 'Shares as fixed amounts (should sum to the expense)';
      split.appendChild(note);
      ES_STATE.members.forEach(function(n){
        const lbl = document.createElement('label');
        lbl.className = 'es-share';
        const val = e.shares[n] !== undefined ? e.shares[n] : 0;
        lbl.innerHTML = n + ' <input type="number" step="0.01" min="0" value="' + val + '">';
        const inp = lbl.querySelector('input');
        inp.oninput = function(){ e.shares[n] = parseFloat(inp.value) || 0; esCompute(); };
        split.appendChild(lbl);
      });
    }
    host.appendChild(row);
  });
}
function esCompute(){
  const balances = {};
  ES_STATE.members.forEach(function(n){ balances[n] = 0; });
  const warnings = [];
  ES_STATE.expenses.forEach(function(e){
    const amt = e.amount;
    if(amt <= 0) return;
    if(!balances.hasOwnProperty(e.payer)) return;
    balances[e.payer] += amt;
    if(e.mode === 'equal'){
      const parts = ES_STATE.members.filter(function(n){ return e.participants[n]; });
      if(parts.length === 0){ warnings.push('"' + e.desc + '" has no participants — skipped.'); return; }
      const each = amt / parts.length;
      parts.forEach(function(n){ balances[n] -= each; });
    } else if(e.mode === 'percent'){
      let totalPct = 0;
      ES_STATE.members.forEach(function(n){ totalPct += e.shares[n] || 0; });
      if(totalPct <= 0){ warnings.push('"' + e.desc + '" has zero total percent — skipped.'); return; }
      if(Math.abs(totalPct - 100) > 0.5) warnings.push('"' + e.desc + '" percentages sum to ' + totalPct.toFixed(1) + '% (not 100). Splitting proportionally anyway.');
      ES_STATE.members.forEach(function(n){
        const pct = e.shares[n] || 0;
        balances[n] -= amt * pct / totalPct;
      });
    } else if(e.mode === 'fixed'){
      let totalFx = 0;
      ES_STATE.members.forEach(function(n){ totalFx += e.shares[n] || 0; });
      if(totalFx <= 0){ warnings.push('"' + e.desc + '" has zero total fixed shares — skipped.'); return; }
      if(Math.abs(totalFx - amt) > 0.01) warnings.push('"' + e.desc + '" fixed shares sum to ' + totalFx.toFixed(2) + ' but expense is ' + amt.toFixed(2) + '. Splitting proportionally.');
      ES_STATE.members.forEach(function(n){
        const fx = e.shares[n] || 0;
        balances[n] -= amt * fx / totalFx;
      });
    }
  });
  esShowBalances(balances, warnings);
  esShowSettlement(balances);
}
function esShowBalances(balances, warnings){
  const host = document.getElementById('es-balances');
  host.innerHTML = '';
  warnings.forEach(function(w){
    const div = document.createElement('div');
    div.className = 'es-warn';
    div.textContent = '⚠ ' + w;
    host.appendChild(div);
  });
  if(ES_STATE.members.length === 0){
    const div = document.createElement('div');
    div.className = 'es-zero-msg';
    div.textContent = 'Add members above to see balances.';
    host.appendChild(div);
    return;
  }
  ES_STATE.members.forEach(function(n){
    const bal = balances[n];
    const cls = Math.abs(bal) < 0.005 ? 'es-bal-zero' : (bal > 0 ? 'es-bal-pos' : 'es-bal-neg');
    const note = Math.abs(bal) < 0.005 ? 'settled' : (bal > 0 ? 'is owed' : 'owes');
    const div = document.createElement('div');
    div.className = 'es-bal';
    div.innerHTML = '<div class="es-bal-name">' + n + '</div><div class="' + cls + '">' + esFmt(bal) + ' (' + note + ')</div>';
    host.appendChild(div);
  });
}
// Greedy settlement: match largest creditor with largest debtor, transfer min(abs).
// Not guaranteed minimum for adversarial cases (the true minimum-transactions problem
// is NP-hard) but optimal for almost all real-world group settlements.
function esSettle(balances){
  const eps = 0.005;
  const creditors = [];
  const debtors = [];
  ES_STATE.members.forEach(function(n){
    const v = balances[n];
    if(v > eps) creditors.push({name:n, amt:v});
    else if(v < -eps) debtors.push({name:n, amt:-v});
  });
  creditors.sort(function(a,b){ return b.amt - a.amt; });
  debtors.sort(function(a,b){ return b.amt - a.amt; });
  const transfers = [];
  let ci = 0, di = 0;
  while(ci < creditors.length && di < debtors.length){
    const pay = Math.min(creditors[ci].amt, debtors[di].amt);
    transfers.push({from: debtors[di].name, to: creditors[ci].name, amt: pay});
    creditors[ci].amt -= pay;
    debtors[di].amt -= pay;
    if(creditors[ci].amt < eps) ci++;
    if(debtors[di].amt < eps) di++;
  }
  return transfers;
}
function esShowSettlement(balances){
  const host = document.getElementById('es-settlement');
  host.innerHTML = '';
  if(ES_STATE.expenses.length === 0){
    host.innerHTML = '<div class="es-zero-msg">Add expenses to compute the settlement.</div>';
    return;
  }
  const transfers = esSettle(balances);
  if(transfers.length === 0){
    host.innerHTML = '<div class="es-zero-msg">Everyone is even. No transfers needed.</div>';
    return;
  }
  transfers.forEach(function(t){
    const div = document.createElement('div');
    div.className = 'es-pay';
    div.textContent = t.from + ' → ' + t.to + ': ' + esCur() + t.amt.toFixed(2);
    host.appendChild(div);
  });
}
function esRender(){
  esRenderMembers();
  esRenderExpenses();
  esCompute();
}
function esRun(){
  // Currency changed: just recompute display (balances depend on currency for display only)
  esCompute();
}
function esSaveState(){
  const persisted = {
    group: document.getElementById('es-group').value,
    cur: document.getElementById('es-cur').value,
    members: ES_STATE.members,
    expenses: ES_STATE.expenses.map(function(e){
      return {desc:e.desc, payer:e.payer, amount:e.amount, mode:e.mode, participants:e.participants, shares:e.shares};
    })
  };
  const b64 = btoa(unescape(encodeURIComponent(JSON.stringify(persisted))));
  const url = location.origin + location.pathname + '#es=' + b64;
  history.replaceState(null, '', url);
  navigator.clipboard.writeText(url).then(function(){
    alert('Saved. URL copied to clipboard — share it with your group.');
  }, function(){
    prompt('Copy this URL:', url);
  });
}
function esLoadState(){
  const m = location.hash.match(/es=([^&]+)/);
  if(!m) return false;
  try{
    const s = JSON.parse(decodeURIComponent(escape(atob(m[1]))));
    if(s.group) document.getElementById('es-group').value = s.group;
    if(s.cur) document.getElementById('es-cur').value = s.cur;
    if(Array.isArray(s.members)) ES_STATE.members = s.members.slice();
    if(Array.isArray(s.expenses)){
      ES_STATE.expenses = s.expenses.map(function(e){
        return {id:ES_NEXT_ID++, desc:e.desc, payer:e.payer, amount:e.amount, mode:e.mode, participants:e.participants||{}, shares:e.shares||{}};
      });
    }
    return true;
  }catch(err){ return false; }
}
function esInit(){
  if(!esLoadState()){
    // Default demo state
    ES_STATE.expenses = [
      {id: ES_NEXT_ID++, desc:'Hotel', payer:'Alice', amount:240, mode:'equal',
       participants:{Alice:true,Bob:true,Charlie:true}, shares:{Alice:0,Bob:0,Charlie:0}},
      {id: ES_NEXT_ID++, desc:'Dinner', payer:'Bob', amount:90, mode:'equal',
       participants:{Alice:true,Bob:true,Charlie:true}, shares:{Alice:0,Bob:0,Charlie:0}},
    ];
  }
  esRender();
}
document.addEventListener('DOMContentLoaded', esInit);
</script>
""",
    "help": {
        "en": """
<h2>What this does and when it's useful</h2>
<p>This is the "we went on a weekend trip and now we need to figure out who owes who" calculator. You list the people in the group, log who paid what, mark who that expense was for, and the tool computes (a) each person's net position and (b) the minimum number of bank transfers that settles everyone up. Everything runs in your browser — no server, no signup, no accounts to share.</p>

<h2>How to use it</h2>
<ol>
  <li><strong>Add members.</strong> Type each person's name and press Enter or "Add member".</li>
  <li><strong>Add expenses.</strong> For each one: who paid (the person who fronted the money), how much, and who it should be split among. You can split:
    <ul>
      <li><strong>Equally</strong> — uncheck anyone who shouldn't be included (e.g. a vegetarian skipping the steak dinner).</li>
      <li><strong>By percentages</strong> — for cases like "Alice 50%, Bob 30%, Charlie 20%". The tool warns if your percentages don't add to 100 but will still split proportionally.</li>
      <li><strong>By fixed amounts</strong> — for cases like "Alice owes €15 for her wine, Bob owes €5 for his coffee". The fixed amounts should sum to the expense; the tool warns if they don't.</li>
    </ul>
  </li>
  <li><strong>Read the balances.</strong> Each person ends up with a single net figure — positive means they're owed that much, negative means they owe.</li>
  <li><strong>Settle.</strong> The tool computes the actual transfers needed. With 4 people who all owe each other small amounts, the worst case is 3 transfers (n−1), not 12 (n·(n−1)).</li>
  <li><strong>Share.</strong> Click "Save state in URL" — the whole group state goes into the URL fragment. Send the link to the group; they see the same state.</li>
</ol>

<h2>About "minimum transfers"</h2>
<p>The true minimum-transactions debt-simplification problem is NP-hard, so this tool uses a greedy algorithm: repeatedly take the largest debtor and the largest creditor, and have the debtor pay the creditor either the full debt or the full credit, whichever is smaller. This produces an optimal answer for almost every real-world group settlement (it's only suboptimal in adversarial cases where pairings let one person settle two debts in one transfer). For 99% of weekend-trip and dinner-tab scenarios you'll see, the greedy result is the minimum.</p>
<p>A property worth knowing: with n people who all owe each other, the minimum is at most n−1 transfers — because each transfer can fully settle at least one person, leaving n−1 people, n−2 people, etc.</p>

<h2>Currency handling</h2>
<p>One group = one currency. If you mixed currencies on a trip (paid hotel in EUR, restaurants in CZK, etc.), the honest answer is to convert each expense to a common currency before entering it, using the actual rates from each transaction (bank statements). Doing FX conversion live inside the splitter would mean fetching live rates and would introduce rounding ambiguity over who paid what. Better to lock the rate per transaction.</p>

<h2>Sharing safely</h2>
<p>The "Save state in URL" button base64-encodes the entire group state — names, amounts, payer info — into the URL fragment. Browser fragments are <em>not</em> sent over HTTP, so the data never reaches a server. But the URL itself contains the data, so anyone with the link can read everything. Share it through your trip's group chat, not in public.</p>

<h2>Common gotchas</h2>
<ul>
  <li><strong>"Who paid" vs "who should pay".</strong> The <em>payer</em> is the person whose card or cash got used at the till. The <em>split</em> is who that cost should ultimately be borne by. Many tools confuse this — make sure the payer is correct or the balances flip.</li>
  <li><strong>Equal split with one person opting out.</strong> Use the checkboxes — uncheck the person to remove them from that expense only. They still appear in other expenses.</li>
  <li><strong>Cash payments confuse balances.</strong> If Alice paid €30 cash to Bob "for her share of dinner" before logging the expense, either don't log that bilateral payment as an expense, or log it as a stand-alone "Cash to Bob" expense paid by Alice with Bob as the sole participant — the math works out either way.</li>
  <li><strong>Splitwise import/export.</strong> This tool doesn't read or write Splitwise format. If you've been using Splitwise and want to migrate, copy the ledger manually.</li>
  <li><strong>Rounding errors compound.</strong> The tool shows two-decimal output, but the balances are computed in full precision. If you see a "1 cent off" warning, it's usually a rounding artifact from percentage splits.</li>
  <li><strong>The browser keeps no history.</strong> Refresh the page and your data is gone unless you saved the URL. Bookmark the saved-state URL for any trip you want to refer back to.</li>
</ul>
""",
        "de": """
<h2>Wofür</h2>
<p>Der „Wir waren im Wochenend-Trip — wer schuldet wem?“-Rechner. Mitglieder, Ausgaben (wer zahlte, wer trägt's), und das Tool berechnet Netto-Saldo plus minimale Überweisungen. Alles im Browser.</p>
<h2>So geht's</h2>
<ol>
<li>Mitglieder hinzufügen.</li>
<li>Ausgabe: wer zahlte, Betrag, Aufteilung (gleich / %-Anteile / feste Beträge).</li>
<li>Salden ablesen — positiv = bekommt zurück, negativ = schuldet.</li>
<li>Zahlungen ausführen (n Personen → max. n−1 Überweisungen).</li>
<li>„URL speichern“ teilt den Zustand mit der Gruppe.</li>
</ol>
<h2>Algorithmus</h2>
<p>Das echte Minimum-Transaktionen-Problem ist NP-schwer. Wir nehmen greedy: größter Schuldner zahlt größtem Gläubiger. In fast allen Alltagsfällen optimal.</p>
<h2>Währungen</h2>
<p>Eine Gruppe = eine Währung. Bei gemischter Reise: jede Ausgabe vorher mit Tageskurs der Belastung umrechnen.</p>
<h2>URL teilen</h2>
<p>Daten landen im Fragment — wird nie zum Server gesendet, aber wer die URL hat, sieht alles. In privater Gruppe teilen.</p>
<h2>Stolperfallen</h2>
<ul>
<li>„Wer zahlte“ ≠ „Wer trägt's“.</li>
<li>Equal-Split: Person abwählen, wenn sie nicht teilnimmt.</li>
<li>Bilaterale Bar-Zahlungen separat eintragen oder gar nicht.</li>
<li>Refresh löscht alles — vorher URL speichern.</li>
</ul>
""",
        "es": """
<h2>Para qué</h2>
<p>La calculadora "estuvimos de viaje y ahora quién debe a quién". Miembros, gastos (quién pagó, a quién cargar), saldo neto y transferencias mínimas.</p>
<h2>Cómo usar</h2>
<ol>
<li>Añadir miembros.</li>
<li>Añadir gasto: quién pagó, importe, división (igual / % / importes fijos).</li>
<li>Lee los saldos — positivo = le deben, negativo = debe.</li>
<li>Liquida (n personas → máx. n−1 transferencias).</li>
<li>"Guardar URL" para compartir con el grupo.</li>
</ol>
<h2>Algoritmo</h2>
<p>El problema mínimo-de-transacciones real es NP-difícil. Usamos greedy: el mayor deudor paga al mayor acreedor. Óptimo en casi todos los casos cotidianos.</p>
<h2>Divisas</h2>
<p>Un grupo = una divisa. Si mezclasteis monedas, convertid cada gasto al tipo del día antes de meterlo.</p>
<h2>Compartir</h2>
<p>El fragmento de URL nunca llega al servidor, pero quien tenga el enlace ve todo. Compartir en chat privado.</p>
<h2>Errores comunes</h2>
<ul>
<li>"Quién pagó" ≠ "a quién corresponde".</li>
<li>División igual: desmarca a quien no participe.</li>
<li>Pagos en efectivo bilaterales: regístralos como gasto separado o no los apuntes.</li>
<li>Recargar la página borra todo — guarda la URL antes.</li>
</ul>
""",
        "fr": """
<h2>À quoi ça sert</h2>
<p>La calculatrice « on est partis en week-end, qui doit quoi à qui ». Membres, dépenses (qui a payé, à charge de qui), solde net et virements minimaux.</p>
<h2>Utilisation</h2>
<ol>
<li>Ajouter les membres.</li>
<li>Ajouter une dépense : payeur, montant, partage (égal / % / montants fixes).</li>
<li>Lire les soldes — positif = créancier, négatif = débiteur.</li>
<li>Régler (n personnes → au plus n−1 virements).</li>
<li>« Sauver URL » pour partager avec le groupe.</li>
</ol>
<h2>Algorithme</h2>
<p>Le vrai problème du minimum de transactions est NP-difficile. On utilise un glouton : plus grand débiteur paye plus grand créancier. Optimal en pratique.</p>
<h2>Devises</h2>
<p>Un groupe = une devise. Pour un voyage en devises mixtes, convertir chaque dépense au taux du jour avant de l'entrer.</p>
<h2>Partage</h2>
<p>Le fragment d'URL ne va jamais au serveur, mais qui a l'URL voit tout. Partager dans le chat privé du voyage.</p>
<h2>Pièges courants</h2>
<ul>
<li>« Qui a payé » ≠ « à qui ça incombe ».</li>
<li>Partage égal : décochez ceux qui n'y participent pas.</li>
<li>Paiements bilatéraux en liquide : à enregistrer séparément ou pas du tout.</li>
<li>Recharger la page efface tout — sauvegardez l'URL avant.</li>
</ul>
""",
        "it": """
<h2>A cosa serve</h2>
<p>La calcolatrice "siamo andati in gita, ora chi deve a chi". Membri, spese (chi ha pagato, a carico di chi), saldo netto e trasferimenti minimi.</p>
<h2>Come si usa</h2>
<ol>
<li>Aggiungi i membri.</li>
<li>Aggiungi spesa: chi ha pagato, importo, divisione (paritaria / % / importi fissi).</li>
<li>Leggi i saldi — positivo = a credito, negativo = a debito.</li>
<li>Salda (n persone → max n−1 trasferimenti).</li>
<li>"Salva URL" per condividere col gruppo.</li>
</ol>
<h2>Algoritmo</h2>
<p>Il vero problema del minimo di transazioni è NP-difficile. Usiamo greedy: massimo debitore paga al massimo creditore. Ottimo nella pratica.</p>
<h2>Valute</h2>
<p>Un gruppo = una valuta. In viaggio con valute miste, converti ogni spesa al tasso del giorno prima di inserirla.</p>
<h2>Condivisione</h2>
<p>Il fragment dell'URL non va al server, ma chi ha l'URL vede tutto. Condividilo nella chat privata del gruppo.</p>
<h2>Errori comuni</h2>
<ul>
<li>"Chi ha pagato" ≠ "a chi spetta".</li>
<li>Divisione paritaria: deseleziona chi non partecipa a quella voce.</li>
<li>Pagamenti bilaterali in contanti: registra come voce separata o non registrarli.</li>
<li>Ricaricare la pagina cancella tutto — salva l'URL prima.</li>
</ul>
""",
        "pt": """
<h2>Para que serve</h2>
<p>A calculadora "fomos numa viagem, agora quem deve a quem". Membros, despesas (quem pagou, a cargo de quem), saldo líquido e transferências mínimas.</p>
<h2>Como usar</h2>
<ol>
<li>Adicione os membros.</li>
<li>Adicione despesa: quem pagou, valor, divisão (igual / % / valores fixos).</li>
<li>Leia os saldos — positivo = receber, negativo = pagar.</li>
<li>Acerte (n pessoas → no máximo n−1 transferências).</li>
<li>"Salvar URL" para compartilhar com o grupo.</li>
</ol>
<h2>Algoritmo</h2>
<p>O verdadeiro problema do mínimo de transações é NP-difícil. Usamos guloso: maior devedor paga ao maior credor. Ótimo na prática.</p>
<h2>Moedas</h2>
<p>Um grupo = uma moeda. Em viagem com moedas mistas, converta cada despesa pela taxa do dia antes de lançar.</p>
<h2>Compartilhar</h2>
<p>O fragmento da URL nunca vai para o servidor, mas quem tem a URL vê tudo. Compartilhe no chat privado.</p>
<h2>Pegadinhas comuns</h2>
<ul>
<li>"Quem pagou" ≠ "a quem cabe".</li>
<li>Divisão igual: desmarque quem não participa daquela despesa.</li>
<li>Pagamentos bilaterais em dinheiro: registre como despesa separada ou não registre.</li>
<li>Recarregar a página apaga tudo — salve a URL antes.</li>
</ul>
""",
        "pl": """
<h2>Do czego to służy</h2>
<p>Kalkulator typu „pojechaliśmy na weekend i kto teraz komu wisi“. Członkowie, wydatki (kto zapłacił, na kogo idzie), saldo netto i minimalne przelewy.</p>
<h2>Jak używać</h2>
<ol>
<li>Dodaj członków.</li>
<li>Dodaj wydatek: kto zapłacił, kwota, podział (równy / % / kwoty stałe).</li>
<li>Czytaj salda — dodatnie = ma dostać, ujemne = winien.</li>
<li>Rozlicz się (n osób → maks. n−1 przelewów).</li>
<li>„Zapisz URL“ by dzielić się stanem z grupą.</li>
</ol>
<h2>Algorytm</h2>
<p>Prawdziwy problem minimum transakcji jest NP-trudny. Używamy zachłannego: największy dłużnik płaci największemu wierzycielowi. Optymalne w praktyce.</p>
<h2>Waluty</h2>
<p>Jedna grupa = jedna waluta. Wyjazd z mieszanymi walutami — przelicz każdy wydatek po kursie z dnia, zanim go wpiszesz.</p>
<h2>Udostępnianie</h2>
<p>Fragment URL nie idzie na serwer, ale kto ma link, widzi wszystko. Wrzuć do prywatnego chatu wyjazdu.</p>
<h2>Częste pułapki</h2>
<ul>
<li>„Kto zapłacił“ ≠ „komu to przypisać“.</li>
<li>Równy podział: odhacz osoby nieuczestniczące w tej pozycji.</li>
<li>Płatności gotówkowe między dwoma osobami: rejestruj jako osobny wydatek lub wcale.</li>
<li>Odświeżenie strony kasuje wszystko — najpierw zapisz URL.</li>
</ul>
""",
        "ja": """
<h2>用途</h2>
<p>「週末の旅行に行って、誰が誰にいくら返すんだっけ？」用の計算機です。メンバー、支出（誰が支払い、誰の分か）を登録すれば、各自の純残高と最小限の振込手順を計算します。</p>
<h2>使い方</h2>
<ol>
<li>メンバーを追加。</li>
<li>支出を追加：支払者、金額、分担（均等／％／固定額）。</li>
<li>残高を確認 — プラス＝受取、マイナス＝支払い。</li>
<li>精算（n 人なら最大 n−1 件の振込で完結）。</li>
<li>「URL に保存」でグループ全体に共有。</li>
</ol>
<h2>アルゴリズム</h2>
<p>厳密な最小振込問題は NP 困難なため、貪欲法を使います: 最大の債務者が最大の債権者に支払う。実用上はほぼ最適です。</p>
<h2>通貨</h2>
<p>1 グループ＝1 通貨。複数通貨の旅行では、決済日の実勢レートで各支出を共通通貨に換算してから入力してください。</p>
<h2>共有</h2>
<p>URL フラグメントはサーバーに送信されませんが、URL を持つ人は中身を全部見られます。旅行のプライベートチャットでのみ共有してください。</p>
<h2>よくある落とし穴</h2>
<ul>
<li>「誰が支払ったか」と「誰の負担か」は別物。</li>
<li>均等割では、参加しない人のチェックを外す。</li>
<li>個人間の現金返済は別の支出として記録するか、まったく記録しない。</li>
<li>ページを再読み込みすると消えるので、先に URL を保存。</li>
</ul>
""",
        "nl": """
<h2>Waarvoor</h2>
<p>De "we zijn op weekend trip geweest, wie schuldt nu wie wat"-calculator. Leden, uitgaven (wie betaalde, voor wie), nettosaldo en minimale overboekingen.</p>
<h2>Gebruik</h2>
<ol>
<li>Voeg leden toe.</li>
<li>Voeg uitgave toe: wie betaalde, bedrag, verdeling (gelijk / % / vaste bedragen).</li>
<li>Lees saldi — positief = krijgt terug, negatief = schuldt.</li>
<li>Verreken (n personen → max. n−1 overboekingen).</li>
<li>"URL opslaan" om met de groep te delen.</li>
</ol>
<h2>Algoritme</h2>
<p>Het echte minimum-transactie-probleem is NP-moeilijk. We gebruiken greedy: grootste debiteur betaalt grootste crediteur. In de praktijk optimaal.</p>
<h2>Valuta</h2>
<p>Eén groep = één valuta. Bij gemixte valuta op een reis: zet elke uitgave om naar één valuta tegen de koers van die dag vóór invoeren.</p>
<h2>Delen</h2>
<p>Het URL-fragment gaat nooit naar de server, maar wie de URL heeft, ziet alles. Deel het in de privé groepschat.</p>
<h2>Veelvoorkomende valkuilen</h2>
<ul>
<li>"Wie betaalde" ≠ "voor wie het is".</li>
<li>Gelijke split: vink uit wie niet meedeed.</li>
<li>Onderlinge contante betalingen: registreer als aparte uitgave of helemaal niet.</li>
<li>Pagina herladen wist alles — sla eerst de URL op.</li>
</ul>
""",
        "tr": """
<h2>Ne işe yarar</h2>
<p>"Hafta sonu geziye çıktık, şimdi kim kime ne borçlu" hesaplayıcı. Üyeler, masraflar (kim ödedi, kime ait), net bakiye ve minimum transferler.</p>
<h2>Kullanım</h2>
<ol>
<li>Üye ekle.</li>
<li>Masraf ekle: kim ödedi, tutar, bölünme (eşit / % / sabit tutarlar).</li>
<li>Bakiyeleri oku — pozitif = alacaklı, negatif = borçlu.</li>
<li>Kapatma (n kişi için en fazla n−1 transfer).</li>
<li>"URL'ye Kaydet" ile grupla paylaş.</li>
</ol>
<h2>Algoritma</h2>
<p>Gerçek minimum-işlem problemi NP-zor. Açgözlü yöntem kullanıyoruz: en büyük borçlu en büyük alacaklıya öder. Pratikte neredeyse her zaman optimal.</p>
<h2>Para birimleri</h2>
<p>Bir grup = bir para birimi. Karma para birimli gezide her masrafı günün kuruyla tek bir para birimine çevirip öyle gir.</p>
<h2>Paylaşım</h2>
<p>URL parçası asla sunucuya gitmez ama URL'yi alan her şeyi görür. Sadece gezinin özel chat'inde paylaş.</p>
<h2>Sık yapılan hatalar</h2>
<ul>
<li>"Kim ödedi" ≠ "kime ait".</li>
<li>Eşit bölüşmede o masrafa katılmayanın işaretini kaldır.</li>
<li>Kişiler arası nakit ödemeleri ayrı masraf olarak gir veya hiç girme.</li>
<li>Sayfa yenilemek her şeyi siler — önce URL'yi kaydet.</li>
</ul>
""",
        "id": """
<h2>Kegunaan</h2>
<p>Kalkulator "kami pergi liburan akhir pekan, sekarang siapa utang ke siapa". Anggota, pengeluaran (siapa bayar, atas tanggungan siapa), saldo bersih dan transfer minimum.</p>
<h2>Cara pakai</h2>
<ol>
<li>Tambah anggota.</li>
<li>Tambah pengeluaran: siapa bayar, jumlah, pembagian (rata / % / jumlah tetap).</li>
<li>Baca saldo — positif = terima, negatif = bayar.</li>
<li>Selesaikan (n orang → maksimal n−1 transfer).</li>
<li>"Simpan URL" untuk dibagikan ke grup.</li>
</ol>
<h2>Algoritma</h2>
<p>Masalah minimum-transaksi sungguhan adalah NP-sulit. Kami pakai greedy: debitur terbesar bayar kreditor terbesar. Hampir selalu optimal di kenyataan.</p>
<h2>Mata uang</h2>
<p>Satu grup = satu mata uang. Untuk perjalanan dengan mata uang campur, konversi setiap pengeluaran ke satu mata uang dengan kurs hari itu sebelum di-input.</p>
<h2>Berbagi</h2>
<p>Fragmen URL tidak pernah dikirim ke server, tapi siapa pun yang punya URL melihat semuanya. Bagikan di chat pribadi grup.</p>
<h2>Kesalahan umum</h2>
<ul>
<li>"Siapa bayar" ≠ "untuk siapa".</li>
<li>Pembagian rata: hapus centang orang yang tidak ikut pengeluaran itu.</li>
<li>Pembayaran tunai antar dua orang: catat sebagai pengeluaran terpisah atau jangan dicatat.</li>
<li>Refresh halaman menghapus semuanya — simpan URL dulu.</li>
</ul>
""",
        "vi": """
<h2>Dùng để làm gì</h2>
<p>Máy tính "đi du lịch cuối tuần xong, ai nợ ai bao nhiêu". Thành viên, chi phí (ai trả, cho ai), số dư ròng và số chuyển khoản tối thiểu.</p>
<h2>Cách dùng</h2>
<ol>
<li>Thêm thành viên.</li>
<li>Thêm chi phí: ai trả, số tiền, cách chia (đều / % / số tiền cố định).</li>
<li>Đọc số dư — dương = được nhận, âm = nợ.</li>
<li>Thanh toán (n người → tối đa n−1 chuyển khoản).</li>
<li>"Lưu URL" để chia sẻ với nhóm.</li>
</ol>
<h2>Thuật toán</h2>
<p>Bài toán tối thiểu giao dịch thật sự là NP-khó. Chúng tôi dùng greedy: con nợ lớn nhất trả chủ nợ lớn nhất. Hầu như luôn tối ưu trong thực tế.</p>
<h2>Tiền tệ</h2>
<p>Một nhóm = một tiền tệ. Trong chuyến đi nhiều tiền tệ, hãy quy đổi từng chi phí theo tỷ giá ngày đó sang một tiền tệ chung trước khi nhập.</p>
<h2>Chia sẻ</h2>
<p>Fragment URL không bao giờ gửi đến server, nhưng ai có URL đều xem được mọi thứ. Chỉ chia sẻ trong chat riêng của nhóm.</p>
<h2>Lỗi thường gặp</h2>
<ul>
<li>"Ai trả" khác với "thuộc về ai".</li>
<li>Chia đều: bỏ tick người không tham gia chi phí đó.</li>
<li>Thanh toán tiền mặt song phương: ghi thành chi phí riêng hoặc không ghi gì cả.</li>
<li>Tải lại trang xóa hết — lưu URL trước.</li>
</ul>
""",
        "hi": """
<h2>उपयोग</h2>
<p>"Weekend trip पर गए थे, अब कौन किसका कितना देय" calculator। Members, expenses (किसने pay किया, किसके लिए), net balance और minimum transfers।</p>
<h2>उपयोग कैसे करें</h2>
<ol>
<li>Members जोड़ें।</li>
<li>Expense जोड़ें: किसने pay किया, amount, बंटवारा (बराबर / % / fixed amounts)।</li>
<li>Balances पढ़ें — positive = मिलना है, negative = देना है।</li>
<li>Settle करें (n लोग → अधिकतम n−1 transfers)।</li>
<li>"Save URL" से group को share करें।</li>
</ol>
<h2>Algorithm</h2>
<p>असली minimum-transactions problem NP-hard है। हम greedy use करते हैं: सबसे बड़ा debtor सबसे बड़े creditor को pay करता है। Real-world में लगभग हमेशा optimal।</p>
<h2>Currencies</h2>
<p>एक group = एक currency। Trip में mixed currencies हों तो हर expense को उस दिन के rate से एक currency में convert करके डालें।</p>
<h2>Sharing</h2>
<p>URL fragment server पर कभी नहीं जाता, पर जिसके पास URL हो वो सब देख सकता है। Trip के private chat में share करें।</p>
<h2>आम गलतियाँ</h2>
<ul>
<li>"किसने pay किया" ≠ "किसके लिए"।</li>
<li>Equal split: जो उस expense में नहीं था उसका checkbox uncheck करें।</li>
<li>दो लोगों के बीच cash payment: अलग expense के रूप में record करें या record न करें।</li>
<li>Page refresh सब मिटा देता है — पहले URL save करें।</li>
</ul>
""",
        "sk": """
<h2>Načo to slúži</h2>
<p>Kalkulačka „boli sme na víkende a teraz kto komu dlhuje“. Členovia, výdavky (kto platil, komu sa to účtuje), čistý zostatok a minimálne prevody.</p>
<h2>Ako používať</h2>
<ol>
<li>Pridaj členov.</li>
<li>Pridaj výdavok: kto platil, suma, rozdelenie (rovnomerne / % / pevné sumy).</li>
<li>Prečítaj zostatky — kladný = dostáva, záporný = dlhuje.</li>
<li>Vyrovnaj (n ľudí → max. n−1 prevodov).</li>
<li>„Ulož URL“ — zdieľaj so skupinou.</li>
</ol>
<h2>Algoritmus</h2>
<p>Skutočný problém minima transakcií je NP-ťažký. Používame greedy: najväčší dlžník platí najväčšiemu veriteľovi. Takmer vždy optimálne v praxi.</p>
<h2>Meny</h2>
<p>Jedna skupina = jedna mena. Pri zájazde s viacerými menami preveď každý výdavok kurzom v daný deň, predtým ako ho zadáš.</p>
<h2>Zdieľanie</h2>
<p>URL fragment nikdy nejde na server, ale kto má URL, vidí všetko. Zdieľaj len v súkromnom chate.</p>
<h2>Časté chyby</h2>
<ul>
<li>„Kto platil“ ≠ „komu to patrí“.</li>
<li>Rovnomerné rozdelenie: odčiarkni toho, kto v tom výdavku nebol.</li>
<li>Hotovostné platby medzi dvomi: zapíš ako samostatný výdavok alebo vôbec.</li>
<li>Refresh stránky vymaže všetko — vopred ulož URL.</li>
</ul>
""",
        "cs": """
<h2>K čemu to slouží</h2>
<p>Kalkulačka „byli jsme na víkendu a teď kdo komu dluží“. Členové, výdaje (kdo platil, komu se to účtuje), čistý zůstatek a minimální převody.</p>
<h2>Jak používat</h2>
<ol>
<li>Přidej členy.</li>
<li>Přidej výdaj: kdo platil, částka, rozdělení (rovnoměrně / % / pevné částky).</li>
<li>Přečti zůstatky — kladný = dostává, záporný = dluží.</li>
<li>Vyrovnej (n lidí → max. n−1 převodů).</li>
<li>„Ulož URL“ — sdílej se skupinou.</li>
</ol>
<h2>Algoritmus</h2>
<p>Skutečný problém minima transakcí je NP-těžký. Používáme greedy: největší dlužník platí největšímu věřiteli. Téměř vždy optimální v praxi.</p>
<h2>Měny</h2>
<p>Jedna skupina = jedna měna. Při zájezdu s více měnami převed každý výdaj kurzem v daný den, než ho zadáš.</p>
<h2>Sdílení</h2>
<p>URL fragment nikdy nejde na server, ale kdo má URL, vidí vše. Sdílej jen v soukromém chatu.</p>
<h2>Časté chyby</h2>
<ul>
<li>„Kdo platil“ ≠ „komu to patří“.</li>
<li>Rovnoměrné rozdělení: odškrtni toho, kdo v tom výdaji nebyl.</li>
<li>Hotovostní platby mezi dvěma: zapiš jako samostatný výdaj nebo vůbec.</li>
<li>Refresh stránky smaže vše — předem ulož URL.</li>
</ul>
""",
    },
    "related": ["tip-split-calculator", "currency-converter", "percentage-calculator"],
    "howto": {"flow": "calculate", "action": "format", "noun": {"en": "shared expense", "de": "geteilte Ausgabe", "es": "gasto compartido", "fr": "dépense partagée", "it": "spesa condivisa", "pt": "despesa partilhada", "pl": "wspólny wydatek", "ja": "共同支出", "nl": "gedeelde uitgave", "tr": "ortak masraf", "id": "pengeluaran bersama", "vi": "chi phí chung", "hi": "shared expense", "sk": "spoločný výdavok", "cs": "společný výdaj"}},
}
