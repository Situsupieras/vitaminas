/* NAVBAR */
const nav = document.getElementById('nav');
window.addEventListener('scroll', () => nav.classList.toggle('scrolled', scrollY > 60), {passive:true});

/* FADE IN */
const io = new IntersectionObserver(entries => {
  entries.forEach(e => { if(e.isIntersecting){ e.target.classList.add('vis'); io.unobserve(e.target); } });
}, {threshold:0.12});
document.querySelectorAll('.fi').forEach(el => io.observe(el));

/* COUNTER */
function animCount(el, target, dur) {
  let start = 0;
  const tick = ts => {
    if (!start) start = ts;
    const p = Math.min((ts - start) / dur, 1);
    const e = 1 - Math.pow(1 - p, 3);
    el.textContent = Math.floor(e * target).toLocaleString();
    if (p < 1) requestAnimationFrame(tick);
  };
  requestAnimationFrame(tick);
}
const cEl = document.getElementById('cnum');
new IntersectionObserver(entries => {
  entries.forEach(e => { if(e.isIntersecting){ animCount(cEl, 2847, 1800); } });
}, {threshold:.5}).observe(cEl);
