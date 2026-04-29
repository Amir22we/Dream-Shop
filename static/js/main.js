/* main.js */

document.addEventListener('DOMContentLoaded', () => {

  // ─── Page Loader ─────────────────────────────────────────────
  const loader = document.querySelector('.page-loader');
  if (loader) {
    setTimeout(() => {
      loader.classList.add('is-hidden');
    }, 1800);
  }

  // ─── Custom Cursor ────────────────────────────────────────────
  const cursor     = document.querySelector('.cursor');
  const cursorRing = document.querySelector('.cursor-ring');

  if (cursor && cursorRing) {
    let mouseX = 0, mouseY = 0;
    let ringX  = 0, ringY  = 0;

    document.addEventListener('mousemove', (e) => {
      mouseX = e.clientX;
      mouseY = e.clientY;
      cursor.style.left = mouseX + 'px';
      cursor.style.top  = mouseY + 'px';
    });

    // Ring follows with lag
    function animateRing() {
      ringX += (mouseX - ringX) * 0.12;
      ringY += (mouseY - ringY) * 0.12;
      cursorRing.style.left = ringX + 'px';
      cursorRing.style.top  = ringY + 'px';
      requestAnimationFrame(animateRing);
    }
    animateRing();

    // Hover states
    const hoverTargets = 'a, button, [data-cursor-hover], .thumbnail, .variant-btn, .color-btn, .tab-btn, .product-card';
    document.addEventListener('mouseover', (e) => {
      if (e.target.closest(hoverTargets)) {
        cursor.classList.add('is-hovering');
        cursorRing.classList.add('is-hovering');
      }
    });
    document.addEventListener('mouseout', (e) => {
      if (e.target.closest(hoverTargets)) {
        cursor.classList.remove('is-hovering');
        cursorRing.classList.remove('is-hovering');
      }
    });
  }

  // ─── Scroll Reveal ───────────────────────────────────────────
  const revealEls = document.querySelectorAll('[data-reveal]');

  if (revealEls.length) {
    const revealObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -60px 0px' });

    revealEls.forEach(el => revealObserver.observe(el));
  }

  // ─── Header Scroll State ──────────────────────────────────────
  const header = document.querySelector('.site-header');
  if (header) {
    window.addEventListener('scroll', () => {
      header.classList.toggle('scrolled', window.scrollY > 40);
    }, { passive: true });
  }

  // ─── Ticker Duplicate ─────────────────────────────────────────
  const ticker = document.querySelector('.ticker-track');
  if (ticker) {
    const clone = ticker.innerHTML;
    ticker.innerHTML = clone + clone;
  }

});
