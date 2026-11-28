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

NAV = [('services.html', 'Services'), ('gallery.html', 'Map Gallery'), ('shop.html', 'Map Shop'), ('map-lab.html', 'Map Lab'),
       ('before-you-buy.html', 'Free Story Map'), ('field-kit.html', 'Field Kit'), ('about.html', 'About')]

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
        <img src="assets/brand/Coastline-Map-Labs-Logo-White-Clear.svg" alt="Coastline Map Labs" width="352" height="132">
        <p style="margin-top:var(--space-4)">Custom maps, land analysis, and GIS learning from Crescent City, California.</p>
      </div>
      <div>
        <h2>Explore</h2>
        <ul><li><a href="services.html">Services</a></li><li><a href="gallery.html">Map Gallery</a></li><li><a href="shop.html">Map Shop</a></li><li><a href="map-lab.html">Map Lab</a></li><li><a href="field-kit.html">Field Kit</a></li><li><a href="trail-gear.html">Trail Gear</a></li><li><a href="before-you-buy.html">Free Story Map</a></li></ul>
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

<section class="section--tight" style="padding-top:0">
  <div class="wrap">
    <a class="free-card reveal" href="before-you-buy.html">
      <img src="assets/storymap/step-score.webp" alt="The free story map's weighted soil suitability map of the Smith River plain" width="1280" height="744" loading="lazy">
      <div class="free-body">
        <span class="free-badge">Free</span>
        <p class="eyebrow">Before You Buy · Story map</p>
        <h3>Read the ground before you buy it.</h3>
        <p>A free, step-by-step soil walkthrough for land buyers. Move the sliders and watch the map change.</p>
        <span class="go">See the free story map →</span>
      </div>
    </a>
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
    <div class="figure figure--night reveal" style="aspect-ratio:1"><img src="assets/brand/Coastline-Map-Labs-Icon-White-Clear.svg" alt="Coastline Map Labs compass rose" loading="lazy" width="280" height="280"></div>
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
      {tier('soil-buyer-report','Land Buyer Report','$150','per parcel',['Everything in Snapshot','Suitability ratings for building, septic, and gardening','Slope and drainage maps','5–8 page PDF + map image files'],featured=True,badge='Most popular')}
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
def product(id_, kind, name, desc, price, art, cta='Buy'):
    src, _ = art
    return f'''<article class="product reveal"><div class="thumb" style="background-image:url({src})"><span class="kind">{kind}</span></div><div class="body"><h3>{name}</h3><p>{desc}</p><div class="row"><span class="price">{price}</span><a class="btn btn-primary" data-buy="{id_}" href="contact.html?item={id_}">{cta}</a></div></div></article>'''

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
    {product('custom-trail-map','Custom map','Pick-Your-Trail Map','Name any trail and I’ll map it in the same style as my Stout Grove map, with trailheads, the route, nearby trails, and a print-ready PDF. <a href="gallery.html">See the sample →</a>','Custom quote',('assets/gallery/stout-grove-thumb.webp',True),cta='Pick your trail')}
    {product('wall-print','Print','Coastline Contour Wall Print','A line-art topographic print of the Del Norte coast on heavyweight matte paper. 12×16 in.','From $35',img('wall-print','art-print.svg'))}
    {product('qgis-style-pack','Template','QGIS Cartography Style Pack','Ready-made QGIS styles and print layouts for clean, vintage-style maps. Drop in your data and export.','From $35',img('qgis-pack','art-template.svg'))}
    {product('qgis-course','Course','QGIS From Zero','A beginner video course from GIS Made Simple: install QGIS, load data, style layers, and export your first map.','$49',img('course','art-course.svg'))}
  </div>
</div></section>
<section class="section--tight" style="padding-top:0"><div class="wrap">
  <div class="band reveal"><div><h2>Want a map of your own place?</h2><p class="muted" style="margin-top:var(--space-2)">Custom prints of your trail, ranch, town, or favorite coastline start at $75.</p></div><a class="btn btn-primary" href="contact.html?item=custom-map">Request a custom map</a></div>
</div></section>
''')


# ------------------------------------------------------------------ MAP GALLERY
# To add a map: put a big image (name.webp) and a ~1100px image (name-thumb.webp)
# in assets/gallery/, add one entry to GALLERY below, then run  python3 build.py
GALLERY = [
    dict(slug='stout-grove', type='Trail & park maps',
         title='Stout Grove Trail', place='Jedediah Smith Redwoods State Park, California',
         desc='A custom trail map of the Stout Memorial Grove loop, with trailheads, the seasonal bridge, the nearby River, Hiouchi, and Little Bald Hills trails, roads, creeks, and a scale bar over aerial imagery.',
         made='QGIS, USGS imagery, and OpenStreetMap data', item='custom-trail-map', cta='I want a map like this'),
]

# group: 'custom' = custom map creation, 'thematic' = data/thematic maps, 'show' = samples of my work
# w/h = size of the -thumb.webp image
MORE_MAPS = [
    dict(group='custom', slug='nez-perce-1877', good='History classes, museums, authors, and family-history projects.', type='Historical route map', w=850, h=1100,
         title='The 1877 Flight of the Nez Perce', place='Oregon, Idaho, and Montana Territory',
         desc='A historical route map of the Nez Perce (Nimiipuu) and Chief Joseph, from the Wallowa Valley toward Canada. It marks battle sites with dates and pairs the map with a written account.',
         made='ESRI, Natural Earth, and Kenneth Townsend sources'),
    dict(group='custom', slug='mexico-zacatecas', good='Family roots, travel stories, gifts, and hometown wall art.', type='Reference map with inset', w=1100, h=850,
         title='Mexico and Zacatecas', place='Mexico and the U.S. Gulf Coast',
         desc='A grid-referenced map of Mexico that highlights the state of Zacatecas over imagery, with major cities, an Old World style, and an aerial inset of the town of San Jose.',
         made='ESRI, NHGIS, and USGS Earth Explorer data'),
    dict(group='custom', slug='mount-rainier-3d', good='Climbers, hikers, cabins, and outdoor gifts.', type='3D terrain maps', w=850, h=1100,
         title='Mount Rainier in 3D', place='Mount Rainier, Washington',
         desc='A 3D terrain view of Mount Rainier, with elevation colors that run from green valleys to a red and gray summit.',
         made=''),
    dict(group='thematic', slug='florida-dengue', good='Public health reports, research posters, and grant proposals.', type='Thematic maps', w=736, h=520,
         title='Dengue Fever Cases and Mosquito Counts', place='Florida, by county',
         desc='A two-variable map: county colors show reported dengue fever cases, and circles show mosquito counts. A locator globe shows where Florida sits.',
         made=''),
    dict(group='thematic', slug='east-africa-refugees', good='Nonprofits, reports, classrooms, and presentations.', type='Thematic maps', w=850, h=1100,
         title='Central and East African Refugee Populations', place='Central and East Africa, 2023',
         desc='Graduated circles compare refugees by country of asylum, and shaded countries show refugees by country of origin, over shaded relief.',
         made='ESRI, World Bank Group, and Shaded Relief Archive data'),
    dict(group='thematic', slug='california-poverty', good='Community groups, local government, and school projects.', type='Thematic maps', w=940, h=1100,
         title='California Poverty Level, 2016 to 2020', place='California, by local government',
         desc='A choropleth map of poverty by local government area across California, in six classes from light to dark red.',
         made=''),
    dict(group='show', slug='smith-river-elevation', good='Watershed groups, anglers, lodges, and wall prints.', type='3D terrain maps', w=1100, h=850,
         title='Smith River: From Mountain to Sea', place='Smith River Watershed, Del Norte County, California',
         desc='Shaded relief of the 797 square mile Smith River watershed, with the river and its forks traced from Bear Mountain at 6,402 feet to the river mouth at sea level.',
         made='USGS 3DEP elevation, the USGS Watershed Boundary Dataset, and OpenStreetMap rivers'),
    dict(group='show', slug='beachfront-park', good='Parks departments, events, rentals, and visitor guides.', type='Trail & park maps', w=1100, h=850,
         title='Beachfront Park', place='Crescent City, California',
         desc='A park locator map that highlights Beachfront Park on the Crescent City waterfront, with the other city parks and streets over aerial imagery.',
         made='USGS National Map imagery and OpenStreetMap data'),
    dict(group='show', slug='elk-valley-property', good='Land buyers, sellers, realtors, and rental listings.', type='Property maps', w=1100, h=840,
         title='Property Snapshot: Elk Valley Cross Road', place='Crescent City, California',
         desc='A one-page property map: a 3.88 acre parcel on aerial imagery, plus a locator map with straight-line distances to the hospital, schools, the airport, downtown, and the redwoods.',
         made='Del Norte County parcels, USGS imagery, and OpenStreetMap data',
         item='soil-buyer-report', buy=True, cta='Order a Land Buyer Report', price='Land Buyer Report: $150'),
]
GROUPS = [
    dict(key='custom', title='Custom maps', intro='Made to order around a place, a story, or a request.',
         item='custom-map', cta='Order one like this', price='Custom maps from $75',
         pitch_eyebrow='Pick your place', pitch_h='Tell me the story. I’ll map it.',
         pitch='A family hometown, a historic route, a mountain you climbed. You get a map designed around it, ready to print or share.',
         steps=[('Tell me the place or story', 'A town, a route, a mountain, or a few notes and photos.'),
                ('I design the map', 'Labels, imagery, insets, and a style that fits.'),
                ('You get the files', 'A print-ready PDF and an image for phones and social posts.')]),
    dict(key='thematic', title='Thematic maps', intro='Data turned into a clear picture: counts, rates, and patterns across a region.',
         item='thematic-map', cta='Order one like this', price='Custom quote',
         pitch_eyebrow='Map your data', pitch_h='Send me a spreadsheet. I’ll make it a map.',
         pitch='Cases by county, people by country, income by city. A thematic map shows the pattern at a glance for reports, grants, and presentations.',
         steps=[('Send your data', 'A spreadsheet or a link to public data, plus the area you care about.'),
                ('I map the pattern', 'Clean classes, clear colors, and a legend anyone can read.'),
                ('You get the files', 'A print-ready PDF and a high-resolution image for slides and reports.')]),
    dict(key='show', title='More of my work', intro='Terrain, park, and property maps from around Del Norte County.',
         item='custom-map', cta='I want a map like this', price='From $75',
         pitch_eyebrow='Your land, your town', pitch_h='Want one for your place?',
         pitch='A watershed, a park, or a property you’re buying or selling. Name the spot and I’ll make a map in the same style.',
         steps=[('Name the spot', 'An address, a parcel number, a park, or a river.'),
                ('I design the map', 'Terrain, imagery, distances, and the details that matter to you.'),
                ('You get the files', 'A print-ready PDF and an image for listings and social posts.')]),
]
MAP_TYPES = [
    ('Trail & park maps', 'Any trail you love, with trailheads, loops, and nearby routes. Print-ready.', 'custom-trail-map'),
    ('Soil & land suitability', 'Which parts of a property suit building, septic, or gardening.', 'soil-buyer-report'),
    ('3D terrain maps', 'Shaded relief and 3D views that show the shape of the land.', 'custom-map'),
    ('Thematic maps', 'Your data on a map: cases, counts, rates, and trends by area.', 'thematic-map'),
    ('Interactive web maps', 'Clickable maps for your website, like the one in the Map Lab.', 'web-map'),
    ('StoryMaps', 'Maps, photos, and text that walk readers through a place or project.', 'custom-map'),
]

def gallery_card(g, featured=False):
    cap = f"{g['title']} · {g['place']}"
    return f'''<article class="gcard{' gcard--featured' if featured else ''} reveal">
  <button class="gimg" type="button" data-zoom="assets/gallery/{g['slug']}.webp" data-caption="{cap}" aria-label="View the {g['title']} map full size">
    <img src="assets/gallery/{g['slug']}-thumb.webp" alt="{g['title']} map, {g['place']}" loading="lazy" width="{g.get('w', 1100)}" height="{g.get('h', 850)}">
    <span class="zoom-hint">View full size</span>
  </button>
  <div class="gbody">
    <p class="eyebrow">{g['type']}</p>
    <h2 class="gtitle">{g['title']}</h2>
    <p class="gplace">{g['place']}</p>
    <p>{g['desc']}</p>
    {f'<p class="gfor"><strong>Great for:</strong> {g["good"]}</p>' if g.get('good') else ''}
    {f'<p class="small muted">Made with {g["made"]}.</p>' if g.get('made') else ''}
    {f'<p class="gprice">{g["price"]}</p>' if g.get('price') else ''}
    <div class="btn-row"><a class="btn btn-primary"{' data-buy="' + g['item'] + '"' if g.get('buy') else ''} href="contact.html?item={g['item']}">{g['cta']}</a><button class="btn btn-ghost" type="button" data-zoom="assets/gallery/{g['slug']}.webp" data-caption="{cap}">View full size</button></div>
  </div>
</article>'''

_have = {g['type'] for g in GALLERY + MORE_MAPS}
def _type_card(t, d, i):
    live = t in _have
    status = '<span class="status live">Samples above</span>' if live else '<span class="status dev">Samples coming soon</span>'
    return f'<article class="tool reveal">{status}<h3>{t}</h3><p>{d}</p><a class="small" href="contact.html?item={i}">Ask about this &rarr;</a></article>'
types_html = ''.join(_type_card(*m) for m in MAP_TYPES)
cards = ''.join(gallery_card(g, i == 0 and len(GALLERY) % 2 == 1) for i, g in enumerate(GALLERY))
def _group_section(G):
    maps = [dict(dict(item=G['item'], cta=G['cta'], price=G['price']), **m) for m in MORE_MAPS if m['group'] == G['key']]
    if not maps: return ''
    steps = ''.join(f'<li><div><strong>{t}</strong><span style="color:var(--color-night-muted)">{d}</span></div></li>' for t, d in G['steps'])
    return f'''<section class="section gsection" id="{G['key']}"><div class="wrap">
  <div class="section-head reveal"><p class="eyebrow">{G['title']}</p><h2>{G['intro']}</h2></div>
  <div class="gallery gallery--three">{''.join(gallery_card(m) for m in maps)}</div>
</div></section>
<section class="section night"><div class="wrap split">
  <div class="reveal">
    <p class="eyebrow">{G['pitch_eyebrow']}</p>
    <h2 style="margin-block:var(--space-3) var(--space-4)">{G['pitch_h']}</h2>
    <p class="lede">{G['pitch']}</p>
    <p class="gprice gprice--night">{G['price']}</p>
    <div class="btn-row" style="margin-top:var(--space-6)"><a class="btn btn-primary" href="contact.html?item={G['item']}">{G['cta'].replace(' one like this', ' yours').replace('I want a map like this', 'Get a map of your place')}</a></div>
  </div>
  <ol class="steps reveal" style="color:var(--color-night-text)">{steps}</ol>
</div></section>
'''
group_html = ''.join(_group_section(g) for g in GROUPS)
jump_html = ' · '.join(f'<a href="#{g["key"]}">{g["title"]}</a>' for g in GROUPS)

page('gallery.html', 'Map Gallery — Coastline Map Labs',
     'Sample maps by Rob Montini: custom trail maps, soil and land maps, 3D terrain, and web maps. Find a style you like and order one of your own.',
f'''
<section class="page-hero night"><div class="wrap">
  <p class="eyebrow">Map Gallery</p>
  <h1>See the kinds of maps I make.</h1>
  <p class="lede">Find a style you like, then tell me your place. I’ll make one just for you.</p>
  <p class="gjump">Jump to: {jump_html}</p>
</div></section>
<section class="section"><div class="wrap">
  <div class="gallery">{cards}</div>
</div></section>
<section class="section night"><div class="wrap split">
  <div class="reveal">
    <p class="eyebrow">Pick your trail</p>
    <h2 style="margin-block:var(--space-3) var(--space-4)">Name a trail. I’ll map it.</h2>
    <p class="lede">Your favorite hike, a park you manage, or a trail for your guests. You get a map in the same style as Stout Grove.</p>
    <div class="btn-row" style="margin-top:var(--space-8)"><a class="btn btn-primary" href="contact.html?item=custom-trail-map">Pick your trail</a></div>
  </div>
  <ol class="steps reveal" style="color:var(--color-night-text)">
    <li><div><strong>Tell me the trail</strong><span style="color:var(--color-night-muted)">A name, a park, or a link to the trailhead.</span></div></li>
    <li><div><strong>I design the map</strong><span style="color:var(--color-night-muted)">Trailheads, the route, nearby trails, roads, and water.</span></div></li>
    <li><div><strong>You get the files</strong><span style="color:var(--color-night-muted)">A print-ready PDF and an image for phones and social posts.</span></div></li>
  </ol>
</div></section>
{group_html}<section class="section"><div class="wrap">
  <div class="section-head reveal"><p class="eyebrow">Map types</p><h2>What I can make for you</h2></div>
  <div class="tools tools--five">{types_html}</div>
</div></section>
<dialog id="lightbox" class="lightbox" aria-label="Full-size map">
  <form method="dialog"><button class="lb-close" aria-label="Close">&times;</button></form>
  <img alt="" id="lb-img">
  <p id="lb-cap"></p>
</dialog>
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
  <div class="tools tools--four">
    <article class="tool reveal"><span class="status live">Live · Free</span><h3>Before You Buy story map</h3><p>A free soil walkthrough for land buyers, with a map you can change.</p><a class="small" href="before-you-buy.html">Try it free &rarr;</a></article>
    <article class="tool reveal"><span class="status live">Live</span><h3>Parcel pin &amp; report request</h3><p>Mark a property and send its coordinates with your request.</p></article>
    <article class="tool reveal"><span class="status dev">In development</span><h3>Soil suitability explorer</h3><p>See soil ratings for building, septic, and gardening across Del Norte County.</p></article>
    <article class="tool reveal"><span class="status dev">In development</span><h3>North Coast trails &amp; parks</h3><p>Trailheads, distances, and elevation profiles for redwood and coastal trails.</p></article>
  </div>
</div></section>
''',
extra_head='<link href="https://unpkg.com/maplibre-gl@5.24.1/dist/maplibre-gl.css" rel="stylesheet">',
extra_js='<script src="https://unpkg.com/maplibre-gl@5.24.1/dist/maplibre-gl.js"></script>\n<script src="maplab.js"></script>')

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

  <p class="reveal" style="margin-top:var(--space-6)">Heading outside? See my <a href="trail-gear.html">Trail Gear picks</a> for hiking and field mapping.</p>

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


# ------------------------------------------------------------------ TRAIL GEAR
# Amazon buttons use the "affiliate" keys in config.js. Until you are approved
# by Amazon, they open a plain Amazon search (no commission). After approval,
# paste each product's SiteStripe link into config.js. Do not show prices here:
# Amazon's rules don't allow hand-typed prices on your site.
def gear(aff, tag, name, why, tip):
    return (f'<div class="kit-item reveal"><span class="tag">{tag}</span><div><h3>{name}</h3><p>{why}</p>'
            f'<p class="gear-tip"><strong>Mapmaker tip:</strong> {tip}</p></div>'
            f'<a class="btn btn-ghost" data-aff="{aff}" href="#" target="_blank" rel="sponsored noopener noreferrer">See on Amazon ↗</a></div>')

def gear_group(title, intro, items):
    return (f'  <div class="section-head reveal" style="margin-top:var(--space-16);margin-bottom:var(--space-4)"><h2>{title}</h2><p class="muted">{intro}</p></div>\n'
            f'  <div class="kit">\n    ' + '\n    '.join(items) + '\n  </div>\n')

TRAIL_GEAR = (
'<section class="page-hero night"><div class="wrap">\n'
'  <p class="eyebrow">Trail Gear · As seen on my TikTok</p>\n'
'  <h1>What a mapmaker carries on the trail.</h1>\n'
'  <p class="lede">The navigation and trail gear I use when I hike and map redwood and coastal trails. Short, honest notes on why each one is in my pack.</p>\n'
'</div></section>\n'
'<section class="section"><div class="wrap--narrow">\n'
'  <p class="disclosure reveal"><span><strong>Affiliate disclosure.</strong> As an Amazon Associate I earn from qualifying purchases. If you buy through these links, I may earn a small commission at no extra cost to you.</span></p>\n'
+ gear_group('Find your way', 'A phone is great until the battery or signal quits. These are my backups.', [
    gear('amz-compass', 'Compass', 'Suunto A-10 baseplate compass', 'A simple, reliable compass made for reading paper maps.', 'Set it on a printed trail map and turn both until north lines up. That one move makes a map make sense.'),
    gear('amz-etrex-se', 'GPS', 'Garmin eTrex SE handheld GPS', 'A budget GPS that runs on two AA batteries for days.', 'Record your hike as a track, then open it in QGIS and turn it into your own trail map.'),
    gear('amz-etrex-32x', 'GPS', 'Garmin eTrex 32x handheld GPS', 'Adds topo maps, an electronic compass, and an altimeter.', 'The altimeter lets you build an elevation profile of your hike.'),
    gear('amz-inreach', 'Safety', 'Garmin inReach Mini 2', 'Satellite texting and SOS where there is no cell signal. Needs a subscription.', 'Worth it if you hike alone or go off-trail in the backcountry.'),
])
+ gear_group('Light and warmth', 'Days are short on the North Coast in winter, and the fog rolls in fast.', [
    gear('amz-headlamp', 'Light', 'Rechargeable motion-sensor headlamp (2-pack)', 'Hands-free light that charges by USB. A best seller in camping gear.', 'Use red-light mode to read a map at night without ruining your night vision.'),
    gear('amz-handwarmers', 'Warmth', 'Rechargeable hand warmers (2-pack)', 'Pocket warmers you can recharge instead of throwing away.', 'Cold fingers can’t work a GPS or a compass. Keep these in your jacket pocket.'),
])
+ gear_group('Water and safety', 'The small things that turn a bad day into an okay one.', [
    gear('amz-lifestraw', 'Water', 'LifeStraw personal water filter', 'Drink straight from a stream. Light enough to forget it’s there.', 'Mark creeks and springs as waypoints so you know where you can refill next time.'),
    gear('amz-sawyer', 'Water', 'Sawyer Mini water filter', 'A 2-ounce filter that screws onto a bottle or pouch.', 'Good for longer days when you need to filter more water.'),
    gear('amz-firstaid', 'Safety', 'Compact waterproof first aid kit', 'A small, organized kit for blisters, cuts, and scrapes.', 'Pack it at the top of your bag, not the bottom.'),
])
+ gear_group('On the trail', 'For steep, muddy, rooty trails like the ones in the redwoods.', [
    gear('amz-poles', 'Support', 'Collapsible trekking poles with cork grips', 'Take strain off your knees on the way down.', 'A pole held upright next to a feature makes a handy scale in your field photos.'),
])
+ '  <div class="band reveal" style="margin-top:var(--space-16)">\n'
  '    <div><h2>Want a map of your favorite trail?</h2><p class="muted" style="margin-top:var(--space-2)">I make custom trail maps with trailheads, loops, and nearby routes.</p></div>\n'
  '    <a class="btn btn-primary" href="gallery.html">See trail map samples</a>\n'
  '  </div>\n'
  '  <p class="small muted" style="margin-top:var(--space-6)">Also see my <a href="field-kit.html">Field Kit</a> for GIS software, laptops, and books.</p>\n'
  '</div></section>\n'
)
page('trail-gear.html', 'Trail Gear — What a mapmaker carries — Coastline Map Labs',
     'The trail and navigation gear Rob Montini carries for hiking and field mapping on the North Coast, with Amazon links.',
     TRAIL_GEAR)

# ------------------------------------------------------------------ FREE STORY MAP
STORY_URL = 'https://gis-made-simple-soils.pplx.app'
SHOTS = [
    ('step-ph', 'Step 3: Is the soil sour? A pH map of the Smith River plain.', 768, 744),
    ('step-score', 'Step 6: Move the sliders and the suitability map recalculates.', 1280, 744),
    ('step-parcel', 'Step 7: Clip to a parcel and count the good acres.', 1280, 744),
    ('checklist', 'A printable soil checklist for your next property visit.', 1280, 644),
]
shots_html = ''.join(
    f'<figure class="sm-shot reveal"><button class="gimg" type="button" data-zoom="assets/storymap/{n}.webp" data-caption="{c}" aria-label="View larger: {c}">'
    f'<img src="assets/storymap/{n}.webp" alt="{c}" width="{w}" height="{h}" loading="lazy"><span class="zoom-hint">View larger</span></button>'
    f'<figcaption>{c}</figcaption></figure>'
    for n, c, w, h in SHOTS)

def night_step(title, sub):
    return f'<li><div><strong>{title}</strong><span style="color:var(--color-night-muted)">{sub}</span></div></li>'

BYB = (
f'''<section class="page-hero night"><div class="wrap">
  <p class="eyebrow">Before You Buy · Free story map</p>
  <h1>Read the ground before you buy it.</h1>
  <p class="lede">A listing that says “great soil” doesn’t tell you whether grass will grow for your animals. This free story map walks you through a full soil check, one small step at a time.</p>
  <div class="btn-row">
    <a class="btn btn-primary btn-free" href="{STORY_URL}" target="_blank" rel="noopener">Try the free story map ↗</a>
    <a class="btn btn-ghost" href="#inside">See what’s inside</a>
  </div>
  <p class="small" style="color:var(--color-night-muted)">Free · No sign-up · Works on phone and computer</p>
</div></section>

<section class="section" id="inside"><div class="wrap">
  <div class="section-head reveal"><p class="eyebrow">What’s inside</p><h2>Real USDA soil data, explained in plain English.</h2><p class="muted">The example is the Smith River plain in Del Norte County, with a made-up 39-acre parcel. Tap any picture to see it larger.</p></div>
  <div class="sm-grid">{shots_html}</div>
  <div class="btn-row reveal" style="margin-top:var(--space-10);justify-content:center">
    <a class="btn btn-primary btn-free" href="{STORY_URL}" target="_blank" rel="noopener">Open the free story map ↗</a>
  </div>
</div></section>

<section class="section night"><div class="wrap split">
  <div class="reveal">
    <p class="eyebrow">How it works</p>
    <h2 style="margin-block:var(--space-3) var(--space-4)">Six questions every land buyer should ask the soil.</h2>
    <p class="lede">Each step shows one layer on the map, so you only learn one thing at a time.</p>
  </div>
  <ol class="steps reveal" style="color:var(--color-night-text)">
    {night_step('Is the soil sour?', 'Soil pH, and when lime can fix it.')}
    {night_step('Do roots sit in water?', 'Drainage classes and wet spots.')}
    {night_step('Will it last through summer?', 'How much water the soil holds.')}
    {night_step('Is it too steep or too low?', 'Slope, flood zones, and wetlands.')}
    {night_step('How does it score overall?', 'A weighted map you can change yourself.')}
    {night_step('How many good acres?', 'Clip to the parcel and add it up.')}
  </ol>
</div></section>

<section class="section--tight"><div class="wrap">
  <div class="band reveal">
    <div><h2>Looking at a real property?</h2><p class="muted" style="margin-top:var(--space-2)">The story map is an example. I can run the same check on the land you’re thinking of buying.</p></div>
    <div class="btn-row"><a class="btn btn-primary" data-buy="soil-buyer-report" href="contact.html?item=soil-buyer-report">Get a Land Buyer Report</a><a class="btn btn-ghost" href="map-lab.html">Pin your parcel</a></div>
  </div>
  <p class="small muted" style="margin-top:var(--space-4)">Educational example only. Soil survey data is mapped at a broad scale and isn’t a site-specific test.</p>
</div></section>
<dialog id="lightbox" class="lightbox" aria-label="Full-size picture">
  <form method="dialog"><button class="lb-close" aria-label="Close">&times;</button></form>
  <img alt="" id="lb-img">
  <p id="lb-cap"></p>
</dialog>
''')
page('before-you-buy.html', 'Before You Buy — Free soil story map for land buyers — Coastline Map Labs',
     'Read the ground before you buy it. A free, interactive soil suitability story map for homestead land buyers, built with free USDA data and QGIS.',
     BYB)

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
          <option value="soil-buyer-report">Land Buyer Report ($150)</option>
          <option value="soil-custom">Custom Land Analysis (from $250)</option>
        </optgroup>
        <optgroup label="Maps">
          <option value="custom-trail-map">Custom trail map (pick your trail)</option>
          <option value="custom-map">Custom cartography (from $75)</option>
          <option value="thematic-map">Thematic / data map (custom quote)</option>
          <option value="web-map">Interactive web map (from $300)</option>
        </optgroup>
        <optgroup label="Learning">
          <option value="tutoring">QGIS tutoring ($35/hr)</option>
          <option value="qgis-course">QGIS From Zero course ($49)</option>
          <option value="qgis-style-pack">QGIS Cartography Style Pack (from $35)</option>
        </optgroup>
        <optgroup label="Shop">
          <option value="wall-print">Coastline Contour Wall Print (from $35)</option>
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
