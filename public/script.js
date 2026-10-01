(function () {
  document.documentElement.classList.add('js');
  const body = document.body;
  const page = body.dataset.page;
  const nav = document.querySelector('#site-nav');
  const toggle = document.querySelector('.menu-toggle');
  if (page) {
    const active = document.querySelector('[data-nav="' + page + '"]');
    if (active) active.setAttribute('aria-current', 'page');
  }
  if (toggle && nav) {
    toggle.addEventListener('click', function () {
      const open = nav.classList.toggle('is-open');
      toggle.setAttribute('aria-expanded', String(open));
      toggle.textContent = open ? 'Close' : 'Menu';
    });
  }
  document.querySelectorAll('[data-year]').forEach(function (node) {
    node.textContent = String(new Date().getFullYear());
  });
}());
