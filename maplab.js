(function () {
  var el = document.getElementById('map');
  if (!el) return;
  var status = document.getElementById('map-status');
  if (!window.maplibregl) { status.textContent = 'The map could not load. Check your connection and refresh.'; return; }

  var STYLES = {
    terrain: 'https://tiles.openfreemap.org/styles/liberty',
    light: 'https://tiles.openfreemap.org/styles/positron',
    bright: 'https://tiles.openfreemap.org/styles/bright'
  };
  var map = new maplibregl.Map({
    container: 'map',
    style: STYLES.terrain,
    center: [-124.2, 41.76],   // Crescent City, CA
    zoom: 9.2,
    attributionControl: { compact: true }
  });
  map.addControl(new maplibregl.NavigationControl({ visualizePitch: false }), 'top-right');
  map.addControl(new maplibregl.ScaleControl({ unit: 'imperial' }), 'bottom-left');
  map.on('load', function () { status.remove(); });
  map.on('error', function () { /* tiles retry automatically */ });

  // Basemap switcher
  document.querySelectorAll('[data-style]').forEach(function (b) {
    b.addEventListener('click', function () {
      document.querySelectorAll('[data-style]').forEach(function (x) { x.setAttribute('aria-pressed', 'false'); });
      b.setAttribute('aria-pressed', 'true');
      map.setStyle(STYLES[b.getAttribute('data-style')]);
    });
  });

  // Drop a pin
  var marker = null;
  var readout = document.getElementById('readout');
  var latEl = document.getElementById('r-lat'), lngEl = document.getElementById('r-lng');
  var req = document.getElementById('request-btn');
  var copy = document.getElementById('copy-btn');
  function fmt(v, pos, neg) { return Math.abs(v).toFixed(5) + '° ' + (v >= 0 ? pos : neg); }
  function setPin(lngLat) {
    if (!marker) {
      var dot = document.createElement('div');
      dot.style.cssText = 'width:22px;height:22px;border-radius:50%;background:#1d6a72;border:3px solid #fffcf5;box-shadow:0 2px 6px rgba(20,27,38,.35)';
      marker = new maplibregl.Marker({ element: dot, draggable: true }).setLngLat(lngLat).addTo(map);
      marker.on('dragend', function () { update(marker.getLngLat()); });
    } else marker.setLngLat(lngLat);
    update(lngLat);
  }
  function update(ll) {
    var lat = ll.lat.toFixed(5), lng = ll.lng.toFixed(5);
    readout.classList.remove('empty');
    latEl.textContent = fmt(ll.lat, 'N', 'S');
    lngEl.textContent = fmt(ll.lng, 'E', 'W');
    req.href = 'contact.html?lat=' + lat + '&lng=' + lng;
    req.removeAttribute('aria-disabled');
    copy.removeAttribute('aria-disabled');
    copy.dataset.coords = lat + ', ' + lng;
  }
  map.on('click', function (e) { setPin(e.lngLat); });

  copy.addEventListener('click', function () {
    var t = copy.dataset.coords; if (!t) return;
    var done = function () { copy.textContent = 'Copied'; setTimeout(function () { copy.textContent = 'Copy coordinates'; }, 1600); };
    if (navigator.clipboard) navigator.clipboard.writeText(t).then(done, function () { copy.textContent = t; });
    else copy.textContent = t;
  });

  // Search a place (OpenStreetMap Nominatim)
  var form = document.getElementById('place-form');
  var msg = document.getElementById('place-msg');
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var q = document.getElementById('place-q').value.trim();
    if (!q) return;
    msg.textContent = 'Searching…';
    fetch('https://nominatim.openstreetmap.org/search?format=json&limit=1&q=' + encodeURIComponent(q))
      .then(function (r) { return r.json(); })
      .then(function (res) {
        if (!res.length) { msg.textContent = 'No match. Try a town, road, or ZIP code.'; return; }
        var ll = { lng: +res[0].lon, lat: +res[0].lat };
        map.flyTo({ center: [ll.lng, ll.lat], zoom: 14 });
        setPin(ll);
        msg.textContent = res[0].display_name.split(',').slice(0, 3).join(',');
      })
      .catch(function () { msg.textContent = 'Search is unavailable right now. Click the map instead.'; });
  });
})();
