(function () {
  document.documentElement.classList.add('js');
  var C = window.CML_CONFIG || { buy: {}, affiliate: {} };

  // Mobile menu
  var btn = document.querySelector('.menu-btn');
  var nav = document.getElementById('site-nav');
  if (btn && nav) {
    btn.addEventListener('click', function () {
      var open = nav.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
    document.addEventListener('keydown', function (e) {
      if (e.key === 'Escape' && nav.classList.contains('open')) { nav.classList.remove('open'); btn.setAttribute('aria-expanded', 'false'); btn.focus(); }
    });
  }

  // Buy buttons: use the link from config.js, otherwise go to the Contact page
  document.querySelectorAll('[data-buy]').forEach(function (a) {
    var id = a.getAttribute('data-buy');
    var url = (C.buy || {})[id];
    if (url) {
      a.href = url; a.target = '_blank'; a.rel = 'noopener noreferrer';
    } else {
      a.href = 'contact.html?item=' + encodeURIComponent(id);
    }
  });

  // Affiliate links
  document.querySelectorAll('[data-aff]').forEach(function (a) {
    var url = (C.affiliate || {})[a.getAttribute('data-aff')];
    if (url) { a.href = url; a.target = '_blank'; a.rel = 'sponsored noopener noreferrer'; }
  });

  // Email links
  document.querySelectorAll('[data-email]').forEach(function (a) {
    if (C.email) { a.href = 'mailto:' + C.email; if (!a.textContent.trim()) a.textContent = C.email; }
  });

  // Reveal on scroll
  var els = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    els.forEach(function (el) { io.observe(el); });
  } else { els.forEach(function (el) { el.classList.add('in'); }); }

  // Map Gallery full-size viewer
  var lb = document.getElementById('lightbox');
  if (lb && lb.showModal) {
    var lbImg = document.getElementById('lb-img'), lbCap = document.getElementById('lb-cap');
    document.querySelectorAll('[data-zoom]').forEach(function (b) {
      b.addEventListener('click', function () {
        lbImg.src = b.getAttribute('data-zoom');
        lbImg.alt = b.getAttribute('data-caption') || '';
        lbCap.textContent = b.getAttribute('data-caption') || '';
        lb.showModal();
      });
    });
    lb.addEventListener('click', function (e) { if (e.target === lb) lb.close(); });
  } else {
    document.querySelectorAll('[data-zoom]').forEach(function (b) {
      b.addEventListener('click', function () { window.open(b.getAttribute('data-zoom'), '_blank'); });
    });
  }

  // Contact form
  var form = document.getElementById('contact-form');
  if (form) {
    var params = new URLSearchParams(location.search);
    var item = params.get('item');
    var sel = form.querySelector('#f-service');
    if (item && sel) {
      var opt = sel.querySelector('option[value="' + item + '"]');
      if (opt) sel.value = item;
    }
    var lat = params.get('lat'), lng = params.get('lng');
    if (lat && lng) {
      form.querySelector('#f-location').value = lat + ', ' + lng;
      if (sel && !item) sel.value = 'soil-buyer-report';
    }
    var note = document.getElementById('form-note');
    function show(msg, ok) { note.textContent = msg; note.className = 'form-note show ' + (ok ? 'ok' : 'err'); }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!form.checkValidity()) { form.reportValidity(); return; }
      var data = new FormData(form);
      var service = sel.options[sel.selectedIndex].text;
      if (C.formEndpoint) {
        var b = form.querySelector('button[type=submit]'); b.disabled = true; b.textContent = 'Sending…';
        fetch(C.formEndpoint, { method: 'POST', body: data, headers: { Accept: 'application/json' } })
          .then(function (r) { if (!r.ok) throw new Error(); show('Thanks — your request is in. I usually reply within one business day.', true); form.reset(); })
          .catch(function () { show('That didn’t send. Please email ' + C.email + ' directly.', false); })
          .finally(function () { b.disabled = false; b.textContent = 'Send request'; });
      } else {
        var body = 'Name: ' + data.get('name') + '\nEmail: ' + data.get('email') + '\nService: ' + service +
          '\nLocation / parcel: ' + (data.get('location') || '-') + '\n\n' + data.get('message');
        var href = 'mailto:' + C.email + '?subject=' + encodeURIComponent('Request: ' + service) + '&body=' + encodeURIComponent(body);
        window.open(href, '_blank');
        show('Your email app should open with the request filled in. If it doesn’t, email ' + C.email + '.', true);
      }
    });
  }
})();
