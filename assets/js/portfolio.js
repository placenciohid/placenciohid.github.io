/* Progressive enhancements; projects and articles remain readable without JS. */
(function () {
  'use strict';
  function init() {
    var menu = document.getElementById('menu'), toggle = document.querySelector('.menu-toggle');
    var wrapper = document.getElementById('wrapper');
    if (menu && toggle) {
      document.body.appendChild(menu);
      var opener;
      function closeMenu() {
        if (!document.body.classList.contains('is-menu-visible')) return;
        document.body.classList.remove('is-menu-visible');
        menu.setAttribute('aria-hidden', 'true'); menu.removeAttribute('aria-modal');
        toggle.setAttribute('aria-expanded', 'false'); wrapper.inert = false;
        if (opener) opener.focus();
      }
      toggle.addEventListener('click', function (event) {
        event.preventDefault(); opener = document.activeElement;
        menu.setAttribute('role', 'dialog'); menu.setAttribute('aria-hidden', 'false');
        menu.setAttribute('aria-modal', 'true'); toggle.setAttribute('aria-expanded', 'true');
        wrapper.inert = true; document.body.classList.add('is-menu-visible');
        menu.querySelector('a').focus();
      });
      menu.querySelector('.close').addEventListener('click', closeMenu);
      menu.addEventListener('click', function (event) { if (event.target === menu || event.target.closest('a')) closeMenu(); });
      document.addEventListener('keydown', function (event) {
        if (!document.body.classList.contains('is-menu-visible')) return;
        if (event.key === 'Escape') { event.preventDefault(); closeMenu(); }
        if (event.key === 'Tab') {
          var controls = Array.from(menu.querySelectorAll('a, button'));
          var first = controls[0], last = controls[controls.length - 1];
          if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
          else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
        }
      });
    }
    var browser = document.querySelector('[data-project-browser]');
    if (browser) {
      var query = document.getElementById('project-query');
      var filters = Array.from(browser.querySelectorAll('[data-filter]'));
      var projects = Array.from(document.querySelectorAll('[data-project]')), currentFilter = 'all';
      function normalize(value) { return value.normalize('NFD').replace(/[\u0300-\u036f]/g, '').toLowerCase(); }
      function update() {
        var terms = normalize(query.value).trim().split(/\s+/).filter(Boolean), count = 0;
        projects.forEach(function (project) {
          var matches = (currentFilter === 'all' || project.dataset.group === currentFilter) &&
            terms.every(function (term) { return normalize(project.dataset.search).includes(term); });
          project.hidden = !matches; if (matches) count++;
        });
        document.querySelectorAll('[data-project-group]').forEach(function (section) {
          section.hidden = !Array.from(section.querySelectorAll('[data-project]')).some(function (p) { return !p.hidden; });
        });
        filters.forEach(function (filter) { filter.setAttribute('aria-pressed', String(filter.dataset.filter === currentFilter)); });
        document.getElementById('project-count').textContent = count + (count === 1 ? ' project' : ' projects') +
          (terms.length || currentFilter !== 'all' ? ' match your filters.' : ' across professional work, implementations, and studies.');
        document.getElementById('no-projects').hidden = count > 0;
      }
      function clear() { query.value = ''; currentFilter = 'all'; update(); query.focus(); }
      filters.forEach(function (filter) { filter.addEventListener('click', function () { currentFilter = filter.dataset.filter; update(); }); });
      query.addEventListener('input', update);
      document.getElementById('clear-projects').addEventListener('click', clear);
      document.querySelectorAll('[data-clear-projects]').forEach(function (control) { control.addEventListener('click', clear); });
      browser.hidden = false; update();
    }
    var body = document.querySelector('.article-body'), contents = document.querySelector('.article-contents');
    if (body && contents) {
      var headings = Array.from(body.querySelectorAll('h2[id]'));
      if (headings.length > 2) {
        var list = contents.querySelector('ol');
        headings.forEach(function (heading) {
          var row = document.createElement('li'), link = document.createElement('a');
          link.href = '#' + heading.id; link.textContent = heading.textContent;
          link.addEventListener('click', function () { var details = heading.closest('details'); if (details) details.open = true; });
          row.appendChild(link); list.appendChild(row);
        });
        contents.hidden = false;
      }
      body.querySelectorAll('table').forEach(function (table) {
        var container = document.createElement('div'); container.className = 'table-scroll';
        table.parentNode.insertBefore(container, table); container.appendChild(table);
        function resize() {
          if (container.scrollWidth > container.clientWidth + 1) {
            container.tabIndex = 0; container.setAttribute('role', 'region');
            container.setAttribute('aria-label', 'Data table, scroll horizontally to see all columns');
          } else { container.removeAttribute('tabindex'); container.removeAttribute('role'); container.removeAttribute('aria-label'); }
        }
        resize(); if (window.ResizeObserver) new ResizeObserver(resize).observe(container);
      });
      body.querySelectorAll('pre').forEach(function (pre) {
        var code = pre.querySelector('code'); if (!code) return;
        var button = document.createElement('button'); button.type = 'button'; button.className = 'copy-code'; button.textContent = 'Copy code';
        function selectCode() {
          var selection = window.getSelection(), range = document.createRange();
          range.selectNodeContents(code); selection.removeAllRanges(); selection.addRange(range); button.textContent = 'Code selected';
        }
        button.addEventListener('click', function () {
          if (navigator.clipboard && window.isSecureContext) {
            navigator.clipboard.writeText(code.textContent).then(function () {
              button.textContent = 'Copied'; window.setTimeout(function () { button.textContent = 'Copy code'; }, 1600);
            }).catch(selectCode);
          } else selectCode();
        });
        pre.appendChild(button);
      });
    }
    window.addEventListener('pageshow', function () {
      document.querySelectorAll('.is-transitioning').forEach(function (element) { element.classList.remove('is-transitioning'); });
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init); else init();
}());
