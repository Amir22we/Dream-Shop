/* product_detail.js */

document.addEventListener('DOMContentLoaded', () => {

  // ─── 3D Tilt on Product Image ─────────────────────────────────
  const imageWrap = document.querySelector('.product-image-wrap');

  if (imageWrap) {
    imageWrap.addEventListener('mousemove', (e) => {
      const rect   = imageWrap.getBoundingClientRect();
      const cx     = rect.left + rect.width  / 2;
      const cy     = rect.top  + rect.height / 2;
      const dx     = (e.clientX - cx) / (rect.width  / 2);
      const dy     = (e.clientY - cy) / (rect.height / 2);
      const rotateX = dy * -10;
      const rotateY = dx *  10;

      imageWrap.style.transform = `perspective(900px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale(1.03)`;
      imageWrap.style.transition = 'transform 0.15s ease';
    });

    imageWrap.addEventListener('mouseleave', () => {
      imageWrap.style.transform = 'perspective(900px) rotateX(0deg) rotateY(0deg) scale(1)';
      imageWrap.style.transition = 'transform 0.9s cubic-bezier(0.16, 1, 0.3, 1)';
    });
  }

  // ─── Thumbnail Switch ─────────────────────────────────────────
  const thumbnails  = document.querySelectorAll('.thumbnail');
  const mainImage   = document.querySelector('.product-image');

  thumbnails.forEach(thumb => {
    thumb.addEventListener('click', () => {
      thumbnails.forEach(t => t.classList.remove('active'));
      thumb.classList.add('active');

      if (mainImage) {
        const src = thumb.dataset.src;
        if (src) {
          mainImage.style.opacity = '0';
          mainImage.style.transform = 'scale(0.96)';
          mainImage.style.transition = 'opacity 0.4s, transform 0.4s';

          setTimeout(() => {
            mainImage.src = src;
            mainImage.style.opacity = '1';
            mainImage.style.transform = 'scale(1)';
          }, 350);
        }
      }
    });
  });

  // ─── Variant Buttons ──────────────────────────────────────────
  const variantGroups = document.querySelectorAll('.variant-options');

  variantGroups.forEach(group => {
    const btns = group.querySelectorAll('.variant-btn');
    btns.forEach(btn => {
      btn.addEventListener('click', () => {
        btns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
      });
    });
  });

  const colorBtns = document.querySelectorAll('.color-btn');
  colorBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      colorBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
    });
  });

  // ─── Add to Cart ──────────────────────────────────────────────
  const cartBtn = document.querySelector('.btn-cart');

  if (cartBtn) {
    cartBtn.addEventListener('click', () => {
      if (cartBtn.disabled) return;

      const originalText = cartBtn.querySelector('span').textContent;
      const originalIcon = cartBtn.querySelector('svg')?.outerHTML || '';

      cartBtn.disabled = true;
      cartBtn.classList.add('success');
      cartBtn.querySelector('span').textContent = 'ДОБАВЛЕНО';

      // Bump cart counter
      const cartCount = document.querySelector('.cart-count');
      if (cartCount) {
        const current = parseInt(cartCount.textContent) || 0;
        cartCount.textContent = current + 1;
        cartCount.style.transform = 'scale(1.6)';
        cartCount.style.transition = 'transform 0.4s cubic-bezier(0.34, 1.56, 0.64, 1)';
        setTimeout(() => {
          cartCount.style.transform = 'scale(1)';
        }, 400);
      }

      // Ripple effect
      const ripple = document.createElement('div');
      ripple.style.cssText = `
        position: absolute;
        width: 200px; height: 200px;
        background: rgba(255, 255, 255, 0.15);
        border-radius: 50%;
        top: 50%; left: 50%;
        transform: translate(-50%, -50%) scale(0);
        animation: rippleAnim 0.8s ease-out forwards;
        pointer-events: none;
      `;
      cartBtn.appendChild(ripple);
      setTimeout(() => ripple.remove(), 800);

      setTimeout(() => {
        cartBtn.classList.remove('success');
        cartBtn.querySelector('span').textContent = originalText;
        cartBtn.disabled = false;
      }, 2200);
    });
  }

  // Inject ripple keyframes
  if (!document.querySelector('#ripple-style')) {
    const style = document.createElement('style');
    style.id = 'ripple-style';
    style.textContent = `
      @keyframes rippleAnim {
        to { transform: translate(-50%, -50%) scale(4); opacity: 0; }
      }
    `;
    document.head.appendChild(style);
  }

  // ─── Wishlist ─────────────────────────────────────────────────
  const wishlistBtn = document.querySelector('.btn-wishlist');

  if (wishlistBtn) {
    wishlistBtn.addEventListener('click', () => {
      wishlistBtn.classList.toggle('active');

      // Small spring animation
      wishlistBtn.style.transform = 'scale(0.85)';
      wishlistBtn.style.transition = 'transform 0.1s';
      setTimeout(() => {
        wishlistBtn.style.transform = '';
        wishlistBtn.style.transition = 'all 0.4s cubic-bezier(0.34, 1.56, 0.64, 1)';
      }, 100);
    });
  }

  // ─── Tabs ─────────────────────────────────────────────────────
  const tabBtns   = document.querySelectorAll('.tab-btn');
  const tabPanels = document.querySelectorAll('.tab-panel');

  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const target = btn.dataset.tab;

      tabBtns.forEach(b => b.classList.remove('active'));
      tabPanels.forEach(p => p.classList.remove('active'));

      btn.classList.add('active');
      const panel = document.querySelector(`.tab-panel[data-tab="${target}"]`);
      if (panel) panel.classList.add('active');
    });
  });

  // ─── Scroll-based Counter Animation ──────────────────────────
  const counters = document.querySelectorAll('[data-counter]');

  if (counters.length) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (!entry.isIntersecting) return;
        const el  = entry.target;
        const end = parseFloat(el.dataset.counter);
        const dec = el.dataset.decimals ? parseInt(el.dataset.decimals) : 0;
        let start = 0;
        const duration = 2000;
        const startTime = performance.now();

        function step(now) {
          const elapsed  = now - startTime;
          const progress = Math.min(elapsed / duration, 1);
          // easeOutExpo
          const ease = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
          const val  = start + (end - start) * ease;
          el.textContent = dec ? val.toFixed(dec) : Math.round(val).toLocaleString();
          if (progress < 1) requestAnimationFrame(step);
        }

        requestAnimationFrame(step);
        counterObserver.unobserve(el);
      });
    }, { threshold: 0.5 });

    counters.forEach(el => counterObserver.observe(el));
  }

  // ─── Parallax on Scroll ───────────────────────────────────────
  const imageSide = document.querySelector('.product-image-side');

  if (imageSide) {
    window.addEventListener('scroll', () => {
      const scrollY = window.scrollY;
      const bg = imageSide.querySelector('.product-image-bg');
      if (bg) {
        bg.style.transform = `translateY(${scrollY * 0.15}px)`;
      }
    }, { passive: true });
  }

});
