#!/usr/bin/env python3
"""Builds the Coastline Map Labs pages from one shared header/footer.
Edit page content below, then run:  python3 build.py"""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
def has(p): return os.path.exists(os.path.join(HERE, p))
def img(name, fallback):  # use a photo if present, else contour art
    for ext in ('webp', 'jpg', 'png'):
        if has(f'assets/img/{name}.{ext}'): return f'assets/img/{name}.{ext}', True
    return f'assets/img/{fallback}', False

NAV = [('services.html', 'Services'), ('shop.html', 'Map Shop'), ('map-lab.html', 'Map Lab'),
       ('field-kit.html', 'Field Kit'), ('about.html', 'About')]

def page(fname, title, desc, body, extra_head='', extra_js=''):
    links = ''.join(f'<a href="{h}"{" aria-current=\"page\"" if h == fname else ""}>{t}</a>' for h, t in NAV)
    cta_cur = ' aria-current="page"' if fname == 'contact.html' else ''
    html = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:image" content="assets/brand/Coastline-Map-Labs-Logo-White-on-Dark.svg">
<link rel="icon" href="assets/brand/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://api.fontshare.com" crossorigin>
<link href="https://api.fontshare.com/v2/css?f[]=gambetta@400,500&f[]=switzer@400,500,600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="base.css">
<link rel="stylesheet" href="style.css">
{extra_head}
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-header">
  <div class="wrap">
    <a class="brand" href="index.html" aria-label="Coastline Map Labs home">
      <img src="assets/brand/Coastline-Map-Labs-Icon-White-Clear.svg" alt="" width="40" height="40">
      <span>Coastline<small>MAP LABS</small></span>
    </a>
    <button class="menu-btn" aria-expanded="false" aria-controls="site-nav" aria-label="Open menu">
      <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>
    </button>
    <nav id="site-nav" class="nav" aria-label="Main">{links}<a class="nav-cta" href="contact.html"{cta_cur}>Get a quote</a></nav>
  </div>
</header>
<main id="main">
{body}
</main>
<footer class="site-footer night">
  <div class="wrap">
    <div class="foot-grid">
      <div>
        <img src="assets/brand/Coastline-Map-Labs-Logo-White-Clear.svg" alt="Coastline Map Labs" width="352" height="132" loading="lazy">
        <p style="margin-top:var(--space-4)">Custom maps, land analysis, and GIS learning from Crescent City, California.</p>
      </div>
      <div>
        <h2>Explore</h2>
        <ul><li><a href="services.html">Services</a></li><li><a href="shop.html">Map Shop</a></li><li><a href="map-lab.html">Map Lab</a></li><li><a href="field-kit.html">Field Kit</a></li></ul>
      </div>
      <div>
        <h2>Studio</h2>
        <ul><li><a href="about.html">About Rob</a></li><li><a href="contact.html">Contact &amp; quotes</a></li><li><a data-email href="contact.html">Email</a></li></ul>
      </div>
    </div>
    <div class="foot-legal">
      <p>Affiliate disclosure: some links on this site are affiliate links. If you buy through them, Coastline Map Labs may earn a small commission at no extra cost to you.</p>
      <p>Maps and reports are for planning and education. They are not a substitute for a licensed survey, on-site soil test, or professional engineering advice.</p>
      <p>© 2026 Coastline Map Labs · coastlinemaplab.com</p>
    </div>
  </div>
</footer>
<script src="config.js"></script>
<script src="app.js" defer></script>
{extra_js}
</body>
</html>
'''
    open(os.path.join(HERE, fname), 'w').write(html)
    print('built', fname)

# ------------------------------------------------------------------ HOME
hero_photo, hero_is_photo = img('hero', 'hero-contours.svg')
hero_bg = f'<div class="hero-photo" style="background-image:url({hero_photo})"></div><div class="hero-shade"></div>' if hero_is_photo else ''
soil_img, soil_ph = img('soil-report', 'art-soil.svg')
print_img, print_ph = img('trail-print', 'art-print.svg')
kit_img, kit_ph = img('field-kit', 'art-lab.svg')

page('index.html', 'Coastline Map Labs — Custom maps & land analysis',
     'Custom soil-suitability reports, cartography, interactive web maps, map prints, and QGIS learning from Crescent City, California.',
f'''
<section class="hero night">
  {hero_bg}
  <div class="wrap">
    <p class="coords">41.7558° N · 124.2026° W · NORTH COAST, CALIFORNIA</p>
    <img class="hero-logo" src="assets/brand/Coastline-Map-Labs-Logo-White-Clear.svg" alt="Coastline Map Labs" width="720" height="270">
    <h1>Maps that answer real questions about land.</h1>
    <p class="lede">Soil-suitability reports for land buyers, custom maps and interactive web maps for businesses, and plain-English QGIS lessons for beginners.</p>
    <div class="btn-row">
      <a class="btn btn-primary" href="services.html">See services &amp; pricing</a>
      <a class="btn btn-ghost" href="map-lab.html">Try the Map Lab</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head reveal">
      <p class="eyebrow">What you can get here</p>
      <h2>Hire a mapmaker, buy a map, or learn to make your own.</h2>
    </div>
    <div class="paths reveal">
      <a class="path path--big" href="services.html">
        <div class="art{' photo' if soil_ph else ''}" style="background-image:url({soil_img})"></div>
        <p class="eyebrow path-label">Services</p>
        <h3>Soil-suitability reports &amp; custom maps</h3>
        <p>Know what a piece of land can support before you buy it. Clear maps and a written summary from USDA soil data.</p>
        <span class="go">Services &amp; pricing →</span>
      </a>
      <div class="stack">
        <a class="path" href="shop.html">
          <div class="art{' photo' if print_ph else ''}" style="background-image:url({print_img})"></div>
          <p class="eyebrow path-label">Map Shop</p>
          <h3>Prints, templates &amp; courses</h3>
          <p>Trail maps, QGIS style packs, and beginner lessons.</p>
          <span class="go">Browse the shop →</span>
        </a>
        <a class="path" href="field-kit.html">
          <div class="art{' photo' if kit_ph else ''}" style="background-image:url({kit_img})"></div>
          <p class="eyebrow path-label">Field Kit</p>
          <h3>The gear &amp; software I use</h3>
          <p>GPS units, drones, laptops, and GIS software picks.</p>
          <span class="go">See the kit →</span>
        </a>
      </div>
    </div>
  </div>
</section>

<section class="section night">
  <div class="wrap split">
    <div class="reveal">
      <p class="eyebrow">Map Lab</p>
      <h2 style="margin-block:var(--space-3) var(--space-4)">Drop a pin on any property and request a report.</h2>
      <p class="lede">The Map Lab is where interactive tools live. Click a spot on the map, and the coordinates go straight into your request, so I know exactly which land you mean.</p>
      <div class="btn-row" style="margin-top:var(--space-8)"><a class="btn btn-primary" href="map-lab.html">Open the Map Lab</a></div>
    </div>
    <ol class="steps reveal" style="color:var(--color-night-text)">
      <li><div><strong>Find the land</strong><span style="color:var(--color-night-muted)">Search an address or click the map.</span></div></li>
      <li><div><strong>Send the request</strong><span style="color:var(--color-night-muted)">Pick a report size. Your pin comes along.</span></div></li>
      <li><div><strong>Get your maps</strong><span style="color:var(--color-night-muted)">A PDF report and map files, usually within 3–5 days.</span></div></li>
    </ol>
  </div>
</section>

<section class="section">
  <div class="wrap split split--wide-left">
    <div class="reveal">
      <p class="eyebrow">Who’s behind the maps</p>
      <h2 style="margin-block:var(--space-3) var(--space-4)">Hi, I’m Rob Montini.</h2>
      <p>I’m a GIS and cartography student in Crescent City, California. I build maps in QGIS and ArcGIS Pro: soil and land analysis, trail and park maps, 3D terrain, and StoryMaps. I also teach beginners through GIS Made Simple, so every report I send comes with plain-English explanations.</p>
      <p style="margin-top:var(--space-6)"><a href="about.html">More about me and my work →</a></p>
    </div>
    <div class="figure reveal" style="aspect-ratio:1"><img src="assets/img/art-about.svg" alt="" loading="lazy" width="800" height="600"></div>
  </div>
</section>

<section class="section--tight" style="padding-top:0">
  <div class="wrap">
    <div class="band reveal">
      <div><h2>Have a parcel, a project, or a question?</h2><p class="muted" style="margin-top:var(--space-2)">Tell me what you need. Quotes are free, and I reply within one business day.</p></div>
      <a class="btn btn-primary" href="contact.html">Get a free quote</a>
    </div>
  </div>
</section>
''')

# ------------------------------------------------------------------ SERVICES
def tier(id_, name, price, unit, items, featured=False, badge=None, cta='Order'):
    lis = ''.join(f'<li>{i}</li>' for i in items)
    b = f'<span class="badge">{badge}</span>' if badge else ''
    return f'''<article class="tier{' tier--featured' if featured else ''}">{b}<h3>{name}</h3><p class="price">{price}<small>{unit}</small></p><ul>{lis}</ul><a class="btn {'btn-primary' if featured else 'btn-ghost'}" data-buy="{id_}" href="contact.html?item={id_}">{cta}</a></article>'''

page('services.html', 'Services & pricing — Coastline Map Labs',
     'Soil-suitability reports for land buyers, custom cartography, interactive web maps, and one-on-one QGIS tutoring.',
f'''
<section class="page-hero night"><div class="wrap">
  <p class="eyebrow">Services</p>
  <h1>Clear maps for land decisions, businesses, and learners.</h1>
  <p class="lede">Every project includes the map files, a short plain-English summary, and one round of revisions.</p>
</div></section>

<section class="section"><div class="wrap">
  <div class="offer-group reveal">
    <div class="group-head"><div><p class="eyebrow">For land buyers</p><h2>Soil-suitability reports</h2></div><a href="map-lab.html">Pin your parcel in the Map Lab →</a></div>
    <p class="lede">Find out which parts of a property suit building, gardening, septic, or grazing. Reports use USDA NRCS soil survey data (SSURGO).</p>
    <div class="tiers">
      {tier('soil-snapshot','Parcel Snapshot','$45','per parcel',['One-page soil map of your parcel','Soil types and acreage breakdown','Delivered as PDF in 3 days'])}
      {tier('soil-buyer-report','Land Buyer Report','$125','per parcel',['Everything in Snapshot','Suitability ratings for building, septic, and gardening','Slope and drainage maps','5–8 page PDF + map image files'],featured=True,badge='Most popular')}
      {tier('soil-custom','Custom Land Analysis','From $250','per project',['Multiple parcels or a whole property search','Your own criteria (farming, livestock, homestead)','Interactive web map you can share','Video walkthrough of the results'],cta='Request a quote')}
    </div>
  </div>

  <div class="offer-group reveal">
    <div class="group-head"><div><p class="eyebrow">For businesses &amp; organizations</p><h2>Maps &amp; web maps</h2></div></div>
    <div class="tiers">
      {tier('custom-map','Custom Cartography','From $75','per map',['Trail, park, property, or location maps','Print-ready PDF and web image','Matches your brand colors'])}
      {tier('web-map','Interactive Web Map','From $300','per map',['Clickable map for your website','Your locations, trails, or service areas','Popups with photos and links','Hosting setup help included'],featured=True,badge='New')}
    </div>
  </div>

  <div class="offer-group reveal">
    <div class="group-head"><div><p class="eyebrow">For learners</p><h2>QGIS tutoring</h2></div><a href="shop.html">Self-paced courses →</a></div>
    <div class="tiers">
      {tier('tutoring','One-on-one QGIS session','$35','per hour',['Live screen-share lesson','Bring your own project or data','Step-by-step, beginner-friendly','Recording and notes afterward'],cta='Book a session')}
    </div>
  </div>
</div></section>

<section class="section--tight" style="padding-top:0"><div class="wrap">
  <div class="band reveal"><div><h2>Not sure which one you need?</h2><p class="muted" style="margin-top:var(--space-2)">Describe your project and I’ll recommend the smallest option that works.</p></div><a class="btn btn-primary" href="contact.html">Ask a question</a></div>
</div></section>
''')

# ------------------------------------------------------------------ SHOP
def product(id_, kind, name, desc, price, art):
    src, _ = art
    return f'''<article class="product reveal"><div class="thumb" style="background-image:url({src})"><span class="kind">{kind}</span></div><div class="body"><h3>{name}</h3><p>{desc}</p><div class="row"><span class="price">{price}</span><a class="btn btn-primary" data-buy="{id_}" href="contact.html?item={id_}">Buy</a></div></div></article>'''

page('shop.html', 'Map Shop — Coastline Map Labs',
     'Printable trail maps, framed map prints, QGIS style templates, and beginner QGIS courses.',
f'''
<section class="page-hero night"><div class="wrap">
  <p class="eyebrow">Map Shop</p>
  <h1>Maps to hang, templates to use, and lessons to learn from.</h1>
  <p class="lede">Digital downloads arrive by email right after checkout. Prints ship within a week.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="products">
    {product('trail-map-pdf','Digital download','North Coast Trail Map (PDF)','A printable, pocket-size trail map with contours, trailheads, and mileage. Print at home or at a copy shop.','$12',img('trail-print','art-trail.svg'))}
    {product('wall-print','Print','Coastline Contour Wall Print','A line-art topographic print of the Del Norte coast on heavyweight matte paper. 12×16 in.','$35',img('wall-print','art-print.svg'))}
    {product('qgis-style-pack','Template','QGIS Cartography Style Pack','Ready-made QGIS styles and print layouts for clean, vintage-style maps. Drop in your data and export.','$19',img('qgis-pack','art-template.svg'))}
    {product('qgis-course','Course','QGIS From Zero','A beginner video course from GIS Made Simple: install QGIS, load data, style layers, and export your first map.','$49',img('course','art-course.svg'))}
  </div>
</div></section>
<section class="section--tight" style="padding-top:0"><div class="wrap">
  <div class="band reveal"><div><h2>Want a map of your own place?</h2><p class="muted" style="margin-top:var(--space-2)">Custom prints of your trail, ranch, town, or favorite coastline start at $75.</p></div><a class="btn btn-primary" href="contact.html?item=custom-map">Request a custom map</a></div>
</div></section>
''')

# ------------------------------------------------------------------ MAP LAB
page('map-lab.html', 'Map Lab — Coastline Map Labs',
     'Interactive map tools from Coastline Map Labs. Drop a pin on a property and request a soil-suitability report.',
'''
<section class="page-hero night"><div class="wrap">
  <p class="eyebrow">Map Lab</p>
  <h1>Interactive maps you can use right now.</h1>
  <p class="lede">Start with the parcel pin tool. More tools are added as they’re built.</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="lab reveal">
    <div class="lab-map"><div id="map" role="region" aria-label="Interactive map. Click to drop a pin."></div><p class="map-status" id="map-status">Loading map…</p></div>
    <aside class="lab-panel">
      <div><p class="eyebrow">Tool 01</p><h2>Parcel pin &amp; report request</h2><p class="small muted" style="margin-top:var(--space-2)">Search for a place, then click the exact spot. Drag the pin to adjust it.</p></div>
      <form id="place-form" class="field" role="search">
        <label for="place-q">Find a place</label>
        <div style="display:flex;gap:var(--space-2)"><input id="place-q" type="search" placeholder="Town, road, or ZIP" autocomplete="off"><button class="btn btn-ghost" type="submit">Go</button></div>
        <span class="hint" id="place-msg" aria-live="polite"></span>
      </form>
      <div>
        <p class="small" style="font-weight:600;margin-bottom:var(--space-2)">Basemap</p>
        <div class="seg" role="group" aria-label="Basemap">
          <button type="button" data-style="terrain" aria-pressed="true">Detailed</button>
          <button type="button" data-style="light" aria-pressed="false">Light</button>
          <button type="button" data-style="bright" aria-pressed="false">Bright</button>
        </div>
      </div>
      <div class="readout empty" id="readout" aria-live="polite">
        <span class="eyebrow">Pinned location</span>
        <span class="val" id="r-lat">Click the map</span>
        <span class="val" id="r-lng"></span>
      </div>
      <div class="btn-row" style="flex-direction:column">
        <a class="btn btn-primary" id="request-btn" href="contact.html" aria-disabled="true">Request a soil report here</a>
        <button class="btn btn-ghost" id="copy-btn" type="button" aria-disabled="true">Copy coordinates</button>
      </div>
    </aside>
  </div>
  <p class="small muted" style="margin-top:var(--space-3)">Basemap © OpenFreeMap, © OpenStreetMap contributors. Place search by OpenStreetMap Nominatim.</p>

  <div class="section-head reveal" style="margin-top:var(--space-20)"><p class="eyebrow">In the lab</p><h2>More tools on the way</h2></div>
  <div class="tools">
    <article class="tool reveal"><span class="status live">Live</span><h3>Parcel pin &amp; report request</h3><p>Mark a property and send its coordinates with your request.</p></article>
    <article class="tool reveal"><span class="status dev">In development</span><h3>Soil suitability explorer</h3><p>See soil ratings for building, septic, and gardening across Del Norte County.</p></article>
    <article class="tool reveal"><span class="status dev">In development</span><h3>North Coast trails &amp; parks</h3><p>Trailheads, distances, and elevation profiles for redwood and coastal trails.</p></article>
  </div>
</div></section>
''',
extra_head='<link href="https://unpkg.com/maplibre-gl@latest/dist/maplibre-gl.css" rel="stylesheet">',
extra_js='<script src="https://unpkg.com/maplibre-gl@latest/dist/maplibre-gl.js"></script>\n<script src="maplab.js"></script>')

# ------------------------------------------------------------------ FIELD KIT
def kit(aff, tag, name, why, cta='See it'):
    return f'''<div class="kit-item reveal"><span class="tag">{tag}</span><div><h3>{name}</h3><p>{why}</p></div><a class="btn btn-ghost" data-aff="{aff}" href="#" target="_blank" rel="sponsored noopener noreferrer">{cta} ↗</a></div>'''
page('field-kit.html', 'Field Kit — GIS software & gear — Coastline Map Labs',
     'The GIS software, GPS units, drones, laptops, and books Rob Montini recommends for mapping, with honest notes.',
f'''
<section class="page-hero night"><div class="wrap">
  <p class="eyebrow">Field Kit</p>
  <h1>The software and gear I actually use for mapping.</h1>
  <p class="lede">Honest picks for beginners and working mapmakers, with a note on why each one earns a place.</p>
</div></section>
<section class="section"><div class="wrap--narrow">
  <p class="disclosure reveal"><span><strong>Affiliate disclosure.</strong> Some links below are affiliate links. If you buy through them, I may earn a small commission at no extra cost to you. Free tools are listed because they’re good, not because they pay.</span></p>

  <div class="section-head reveal" style="margin-top:var(--space-16);margin-bottom:var(--space-4)"><h2>Software</h2></div>
  <div class="kit">
    {kit('qgis','Free','QGIS','The free, open-source desktop GIS I use for almost every map on this site. The best place for any beginner to start.','Download')}
    {kit('qfield','Free','QField','Takes your QGIS projects into the field on a phone or tablet for collecting points and photos.','Get QField')}
    {kit('arcgis-personal','Paid','ArcGIS for Personal Use','A low-cost way to learn ArcGIS Pro at home if you want industry-standard skills for jobs.')}
    {kit('felt','Free + paid','Felt','A fast way to make shareable web maps in a browser without writing code.')}
    {kit('canva','Free + paid','Canva','I use it to turn exported maps into posters, social posts, and report covers.')}
  </div>

  <div class="section-head reveal" style="margin-top:var(--space-16);margin-bottom:var(--space-4)"><h2>Hardware</h2></div>
  <div class="kit">
    {kit('garmin-gps','GPS','Handheld GPS (Garmin GPSMAP series)','Reliable positions under heavy redwood canopy, where phones often lose signal.')}
    {kit('dji-drone','Drone','Mapping drone (DJI Mini series)','Light enough for most hobby rules, and good for aerial photos of small parcels. Check local drone regulations first.')}
    {kit('gis-laptop','Computer','A GIS-ready laptop','Look for 32 GB of RAM and a dedicated graphics card. 3D terrain and big rasters need both.')}
    {kit('wacom','Tablet','Drawing tablet (Wacom)','Handy for hand-drawn map details, digitizing, and labeling.')}
  </div>

  <div class="section-head reveal" style="margin-top:var(--space-16);margin-bottom:var(--space-4)"><h2>Books</h2></div>
  <div class="kit">
    {kit('book-bolstad','Book','GIS Fundamentals by Paul Bolstad','A thorough textbook on how GIS works under the hood.')}
    {kit('book-brewer','Book','Designing Better Maps by Cynthia Brewer','A practical guide to color, type, and layout, from the creator of ColorBrewer.')}
  </div>
</div></section>
''')

# ------------------------------------------------------------------ ABOUT
page('about.html', 'About Rob Montini — Coastline Map Labs',
     'Rob Montini is a GIS and cartography student in Crescent City, California, making custom maps and teaching beginner QGIS.',
'''
<section class="page-hero night"><div class="wrap">
  <p class="eyebrow">About</p>
  <h1>A North Coast mapmaker who likes explaining things simply.</h1>
</div></section>
<section class="section"><div class="wrap split split--wide-left">
  <div class="reveal">
    <p>I’m Rob Montini, a GIS and cartography student based in Crescent City, California. I started Coastline Map Labs to turn what I’m learning into maps that help people make real decisions, like whether a piece of land will support a home, a garden, or a well-placed septic system.</p>
    <p style="margin-top:var(--space-4)">My work spans QGIS cartography, soil and land analysis, 3D terrain maps, and StoryMaps. I’m also learning Python to automate GIS work. Through GIS Made Simple, I make short, calm, beginner-friendly lessons for people who want to make their own maps.</p>
    <p style="margin-top:var(--space-4)">If you need a map, a report, or a patient teacher, I’d love to hear from you.</p>
    <div class="btn-row" style="margin-top:var(--space-8)"><a class="btn btn-primary" href="contact.html">Work with me</a><a class="btn btn-ghost" href="services.html">See services</a></div>
  </div>
  <div class="reveal">
    <ul class="facts">
      <li><b>Based in</b><span>Crescent City, California</span></li>
      <li><b>Tools</b><span>QGIS, ArcGIS Pro, StoryMaps, Python (learning)</span></li>
      <li><b>Specialties</b><span>Soil-suitability analysis, cartography, trail and park maps, 3D terrain</span></li>
      <li><b>Teaching</b><span>GIS Made Simple: beginner QGIS lessons and videos</span></li>
      <li><b>Also on</b><span>Fiverr, for quick custom map gigs</span></li>
    </ul>
  </div>
</div></section>
''')

# ------------------------------------------------------------------ CONTACT
page('contact.html', 'Contact & free quotes — Coastline Map Labs',
     'Request a soil-suitability report, custom map, web map, tutoring session, or shop item from Coastline Map Labs.',
'''
<section class="page-hero night"><div class="wrap">
  <p class="eyebrow">Contact</p>
  <h1>Tell me about your land or your map idea.</h1>
  <p class="lede">Quotes are free. I reply within one business day.</p>
</div></section>
<section class="section"><div class="wrap split split--wide-left" style="align-items:start">
  <form id="contact-form" class="form reveal" novalidate>
    <div class="two">
      <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" required autocomplete="name"></div>
      <div class="field"><label for="f-email">Email</label><input id="f-email" name="email" type="email" required autocomplete="email"></div>
    </div>
    <div class="field"><label for="f-service">What do you need?</label>
      <select id="f-service" name="service">
        <optgroup label="Soil reports">
          <option value="soil-snapshot">Parcel Snapshot ($45)</option>
          <option value="soil-buyer-report">Land Buyer Report ($125)</option>
          <option value="soil-custom">Custom Land Analysis (from $250)</option>
        </optgroup>
        <optgroup label="Maps">
          <option value="custom-map">Custom cartography (from $75)</option>
          <option value="web-map">Interactive web map (from $300)</option>
        </optgroup>
        <optgroup label="Learning">
          <option value="tutoring">QGIS tutoring ($35/hr)</option>
          <option value="qgis-course">QGIS From Zero course ($49)</option>
          <option value="qgis-style-pack">QGIS Cartography Style Pack ($19)</option>
        </optgroup>
        <optgroup label="Shop">
          <option value="trail-map-pdf">North Coast Trail Map PDF ($12)</option>
          <option value="wall-print">Coastline Contour Wall Print ($35)</option>
        </optgroup>
        <option value="other">Something else</option>
      </select>
    </div>
    <div class="field"><label for="f-location">Property address, parcel number, or coordinates</label><input id="f-location" name="location" placeholder="Optional"><span class="hint">Tip: drop a pin in the <a href="map-lab.html">Map Lab</a> and it fills this in.</span></div>
    <div class="field"><label for="f-msg">Project details</label><textarea id="f-msg" name="message" required placeholder="What are you planning, and when do you need it?"></textarea></div>
    <button class="btn btn-primary" type="submit">Send request</button>
    <p class="form-note" id="form-note" role="status"></p>
  </form>
  <aside class="reveal" style="display:grid;gap:var(--space-6)">
    <div><p class="eyebrow">Email</p><p style="margin-top:var(--space-2)"><a data-email href="#"></a></p></div>
    <div><p class="eyebrow">Based in</p><p style="margin-top:var(--space-2)">Crescent City, California. I work remotely with clients anywhere in the U.S.</p></div>
    <div><p class="eyebrow">What happens next</p><ol class="steps" style="margin-top:var(--space-3)"><li><div><strong>I review your request</strong><span>and confirm the price and timeline.</span></div></li><li><div><strong>You pay securely</strong><span>by card through a payment link.</span></div></li><li><div><strong>You get your maps</strong><span>as PDF and image files by email.</span></div></li></ol></div>
  </aside>
</div></section>
''')
