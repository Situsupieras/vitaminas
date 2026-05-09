const qd = {};
let step = 1;
const goalLabels = {
  energia:'Energía', sueno:'Sueño', inmunidad:'Inmunidad',
  belleza:'Belleza', articulaciones:'Articulaciones', digestion:'Digestión'
};
const recs = {
  energia:        { p:'Complejo B + CoQ10',               d:'La combinación ideal para energía celular sostenida. El Complejo B activa el metabolismo energético y el CoQ10 potencia la producción de ATP en cada célula.' },
  sueno:          { p:'Magnesio Glicinato + Melatonina',   d:'El Magnesio Glicinato relaja el sistema nervioso de forma profunda, mientras que la Melatonina regula tu ciclo de sueño. La combinación más efectiva para sueño reparador.' },
  inmunidad:      { p:'Vitamina C 1000mg + Zinc',          d:'El dúo de inmunidad más completo. Vitamina C activa defensas, Zinc las mantiene fuertes. Con asesoría personalizada para elegir la dosis correcta para vos.' },
  belleza:        { p:'Biotina + Colágeno Hidrolizado',    d:'Biotina para cabello y uñas más fuertes, Colágeno para piel más firme y luminosa. Resultados visibles desde adentro.' },
  articulaciones: { p:'D3+K2 + Glucosamina',              d:'D3 y K2 trabajan juntas para llevar calcio a los huesos correctamente, y la Glucosamina lubrica y regenera el cartílago articular.' },
  digestion:      { p:'Probiótico 50B + Enzimas Digestivas', d:'Un intestino equilibrado es la base de todo. El Probiótico restaura tu flora y las Enzimas mejoran la absorción de nutrientes.' }
};

function pick(el, k, v) {
  el.closest('.qstep').querySelectorAll('.q-opt').forEach(o => o.classList.remove('sel'));
  el.classList.add('sel');
  qd[k] = v;
  setTimeout(next, 340);
}

function next() {
  if (step < 4) {
    document.getElementById('s'+step).classList.remove('active');
    step++;
    document.getElementById('s'+step).classList.add('active');
    document.getElementById('b'+step).classList.add('on');
  } else { showRes(); }
}

function startSubmit() {
  const nameEl = document.getElementById('lead-name');
  const phoneEl = document.getElementById('lead-phone');
  nameEl.classList.remove('error');
  phoneEl.classList.remove('error');
  let valid = true;
  if (!nameEl.value.trim()) { nameEl.classList.add('error'); valid = false; }
  if (!phoneEl.value.trim()) { phoneEl.classList.add('error'); valid = false; }
  if (!valid) return;
  const btn = document.querySelector('#s4 .btn-primary');
  btn.disabled = true;
  btn.innerHTML = '<span class="spinner-dot"></span> Calculando...';
  setTimeout(submitLead, 1000);
}

function submitLead() {
  const nameEl = document.getElementById('lead-name');
  const name = nameEl.value.trim();
  const leads = JSON.parse(localStorage.getItem('esvitamina_leads') || '[]');
  leads.push({name, phone:document.getElementById('lead-phone').value.trim(), goal:qd.goal, age:qd.age, urgency:qd.urgency, timestamp:new Date().toISOString()});
  localStorage.setItem('esvitamina_leads', JSON.stringify(leads));
  document.getElementById('s4').classList.remove('active');
  ['b1','b2','b3','b4'].forEach(id => document.getElementById(id).classList.add('on'));
  const r = recs[qd.goal] || recs.energia;
  const msg = encodeURIComponent('Hola! Soy ' + name + ', hice el quiz y me recomendó ' + r.p + '. ¿Me pueden asesorar?');
  document.getElementById('r-title').textContent = '¡Listo, ' + name + '! 🎉';
  document.getElementById('r-subtitle').textContent = 'Basado en tu objetivo de ' + (goalLabels[qd.goal] || qd.goal) + ', esta es tu recomendación personalizada:';
  document.getElementById('r-prod').textContent = r.p;
  document.getElementById('r-desc').textContent = r.d;
  document.getElementById('r-cta').href = 'https://wa.me/50230139416?text=' + msg;
  document.getElementById('qres').classList.add('active');
  window.scrollTo({ top: document.getElementById('qres').offsetTop - 100, behavior: 'smooth' });
}

function showRes() {
  document.getElementById('s3').classList.remove('active');
  ['b1','b2','b3','b4'].forEach(id => document.getElementById(id).classList.add('on'));
  const r = recs[qd.goal] || recs.energia;
  const msg = encodeURIComponent('Hola! Hice el quiz y me recomendó ' + r.p + '. ¿Me pueden asesorar?');
  document.getElementById('r-prod').textContent = r.p;
  document.getElementById('r-desc').textContent = r.d;
  document.getElementById('r-cta').href = 'https://wa.me/50230139416?text=' + msg;
  document.getElementById('qres').classList.add('active');
  window.scrollTo({ top: document.getElementById('qres').offsetTop - 100, behavior: 'smooth' });
}

function toggleSymptom(el) {
  el.classList.toggle('chk');
  const msg = document.getElementById('pf-msg');
  if (document.querySelectorAll('.symptom-card.chk').length) { msg.classList.add('show'); } else { msg.classList.remove('show'); }
}

function toggleExtra(btn) {
  const body = document.getElementById('extra-cats');
  const open = body.classList.toggle('open');
  btn.setAttribute('aria-expanded', open);
  document.getElementById('toggle-arr').textContent = open ? '▲' : '▼';
}
