// Shared nav and footer injected on every page
// Call initPage(activePage) at bottom of each page
// activePage: 'home' | 'remodels' | 'adu' | 'new-construction' | 'about' | 'contact'

function initPage(activePage) {
  const root = document.documentElement;

  // Inject nav
  document.getElementById('site-nav').innerHTML = `
    <nav>
      <a href="/" class="nav-logo">
        <img src="/images/logo.png" alt="RAE Homes" />
      </a>
      <ul class="nav-links">
        <li><a href="/remodels/" class="${activePage === 'remodels' ? 'active' : ''}">Remodels</a></li>
        <li><a href="/adu/" class="${activePage === 'adu' ? 'active' : ''}">ADUs</a></li>
        <li><a href="/new-construction/" class="${activePage === 'new-construction' ? 'active' : ''}">New Construction</a></li>
        <li><a href="/about/" class="${activePage === 'about' ? 'active' : ''}">About</a></li>
        <li><a href="/#contact" class="cta-link ${activePage === 'contact' ? 'active' : ''}">Contact</a></li>
      </ul>
      <button class="hamburger" onclick="toggleMenu()" aria-label="Menu">
        <span></span><span></span><span></span>
      </button>
    </nav>
    <nav class="mobile-menu" id="mobileMenu">
      <a href="/remodels/" onclick="toggleMenu()">Remodels</a>
      <a href="/adu/" onclick="toggleMenu()">ADUs</a>
      <a href="/new-construction/" onclick="toggleMenu()">New Construction</a>
      <a href="/about/" onclick="toggleMenu()">About</a>
      <a href="/#contact" class="cta" onclick="toggleMenu()">Contact</a>
    </nav>
  `;

  // Inject footer
  document.getElementById('site-footer').innerHTML = `
    <footer>
      <div class="footer-logo">
        <img src="/images/logo.png" alt="RAE Homes" />
      </div>
      <p class="footer-copy">© 2026 RAE Homes &nbsp;·&nbsp; Denver, Colorado &nbsp;·&nbsp; Licensed &amp; Insured</p>
      <ul class="footer-links">
        <li><a href="/remodels/">Remodels</a></li>
        <li><a href="/adu/">ADUs</a></li>
        <li><a href="/new-construction/">New Construction</a></li>
        <li><a href="/about/">About</a></li>
        <li><a href="/#contact">Contact</a></li>
      </ul>
    </footer>
  `;

  // Smooth scroll for same-page anchor links
  document.querySelectorAll('a[href^="#"]').forEach(a => {
    a.addEventListener('click', e => {
      const target = document.querySelector(a.getAttribute('href'));
      if (target) { e.preventDefault(); target.scrollIntoView({ behavior: 'smooth', block: 'start' }); }
    });
  });
}

function toggleMenu() {
  document.getElementById('mobileMenu').classList.toggle('open');
}

function handleSubmit(e) {
  e.preventDefault();
  const btn = e.target.querySelector('button[type=submit]');
  btn.textContent = 'Sending...';
  btn.disabled = true;
  setTimeout(() => {
    btn.textContent = 'Message Sent ✓';
    e.target.reset();
    setTimeout(() => { btn.textContent = 'Send Message'; btn.disabled = false; }, 3000);
  }, 1200);
}
