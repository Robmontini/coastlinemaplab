# Coastline Map Labs website

## Start selling (edit `config.js`)
- `email`: your business email.
- `formEndpoint`: optional Formspree URL so the contact form emails you.
- `buy`: paste a Stripe Payment Link (or a Gumroad, Etsy, or Fiverr link) for each item. Empty links send buyers to the Contact page.
- `affiliate`: replace the official-site links with your affiliate links.

## Edit pages
Page text lives in `build.py`. Edit it, then run `python3 build.py` to rebuild all pages.
To swap a photo, replace the file in `assets/img/` and keep the same name.

## Hosting
Static site. It works on GitHub Pages, Netlify, or Cloudflare Pages. Point coastlinemaplab.com at the host.

## Add a map to the Map Gallery
1. Save two images in `assets/gallery/`: `name.webp` (large) and `name-thumb.webp` (about 1100 px wide).
2. Add an entry to the `GALLERY` list in `build.py`.
3. Run `python3 build.py`.
