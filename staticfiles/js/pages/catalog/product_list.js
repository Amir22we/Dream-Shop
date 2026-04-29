/* product_list.js */

document.addEventListener('DOMContentLoaded', () => {

  const grid = document.querySelector('.products-grid');

  // ─── View Toggle (Grid / List) ────────────────────────────────
  const viewBtns = document.querySelectorAll('.view-btn');

  viewBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      viewBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const isList = btn.dataset.view === 'list';
      grid?.classList.toggle('list-view', isList);
      localStorage.setItem('catalogView', btn.dataset.view);
    });
  });

  // Восстановить сохранённый вид
  const savedView = localStorage.getItem('catalogView');
  if (savedView === 'list' && grid) {
    grid.classList.add('list-view');
    document.querySelector('[data-view="list"]')?.classList.add('active');
    document.querySelector('[data-view="grid"]')?.classList.remove('active');
  }

  // ─── Add to Cart ──────────────────────────────────────────────
  document.querySelectorAll('.overlay-cart-btn').forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      e.stopPropagation();

      if (btn.disabled) return;
      btn.disabled = true;

      const original = btn.textContent;
      btn.textContent = '✓ ДОБАВЛЕНО';
      btn.style.background = 'var(--cyan)';
      btn.style.color = 'var(--bg)';

      // Bump cart count in header
      const cartCount = document.querySelector('.cart-count');
      if (cartCount) {
        const n = parseInt(cartCount.textContent) || 0;
        cartCount.textContent = n + 1;
        cartCount.style.transform = 'scale(1.6)';
        cartCount.style.transition = 'transform 0.4s cubic-bezier(0.34,1.56,0.64,1)';
        setTimeout(() => { cartCount.style.transform = ''; }, 400);
      }

      setTimeout(() => {
        btn.textContent = original;
        btn.style.background = '';
        btn.style.color = '';
        btn.disabled = false;
      }, 1800);
    });
  });

});
