# Cork Solar & Electrical — Full Website Build

## Project Overview
Building a full multi-page website for Cork Solar & Electrical (CSAE), a residential and commercial electrician and solar company based in Cork, Ireland. Owner is David O'Leary.

## Brand
- Primary colour: Navy #1B2A4A
- Accent colour: Green #6DC535
- White: #FFFFFF
- Light grey background sections: #F5F5F5
- Font headings: Inter or Montserrat, bold
- Font body: Inter, regular
- Logo: CSAE monogram with green lightning bolt — will be provided as PNG, place as placeholder for now
- Zero border radius on buttons, sharp edges throughout
- Design inspiration: Prowired.co.uk (dark, authoritative, sectored) combined with Capital Electrical clean light sections

## Site Structure — Clean URL Subfolder Architecture

All pages live as `index.html` inside a named subfolder so Vercel serves them as clean URLs (e.g. `/residential/house-rewiring/`).

### Root Files
- `index.html` — Homepage (https://www.csae.ie/)
- `header.html` — Shared header component (reference only)
- `footer.html` — Shared footer component (reference only)

### Main Pages
- `about/index.html` → https://www.csae.ie/about/
- `residential/index.html` → https://www.csae.ie/residential/
- `commercial/index.html` → https://www.csae.ie/commercial/
- `solar/index.html` → https://www.csae.ie/solar/
- `contact/index.html` → https://www.csae.ie/contact/
- `privacy-policy/index.html` → https://www.csae.ie/privacy-policy/
- `thankyou/index.html` → https://www.csae.ie/thankyou/

### Residential Sub-Service Pages
- `residential/house-rewiring/index.html`
- `residential/new-build-electrical/index.html`
- `residential/fuse-board-upgrades/index.html`
- `residential/lighting-installation/index.html`
- `residential/ev-charger-installation/index.html`
- `residential/electrical-safety-inspections/index.html`
- `residential/socket-switch-installation/index.html`
- `residential/electric-shower-installation/index.html`
- `residential/kitchen-appliance-wiring/index.html`
- `residential/smoke-carbon-monoxide-alarms/index.html`
- `residential/outdoor-garden-lighting/index.html`
- `residential/emergency-electrical-repairs/index.html`
- `residential/electrical-consultancy/index.html`
- `residential/periodic-inspection-report/index.html`

### Commercial Sub-Service Pages
- `commercial/electrical-installation/index.html`
- `commercial/fuse-board-upgrades/index.html`
- `commercial/electrical-consultancy/index.html`
- `commercial/maintenance-contracts/index.html`
- `commercial/energy-efficiency-auditing/index.html`
- `commercial/factory-plant-wiring/index.html`
- `commercial/office-retail-fitouts/index.html`
- `commercial/emergency-lighting/index.html`
- `commercial/data-network-cabling/index.html`
- `commercial/led-lighting-upgrades/index.html`
- `commercial/security-systems/index.html`
- `commercial/generator-backup-systems/index.html`
- `commercial/periodic-inspection-report/index.html`

## Contact Details
- Phone: 0857188103
- Email: info@csae.ie
- Address: Cork Solar and Electrical, Railway Cottage, Ballinamona, Mourneabbey, Mallow, P51RR22
- Domain: https://www.csae.ie

## SEO Rules — Apply To Every Single Page
- Unique H1 per page targeting a specific keyword
- H2s for each major section
- H3s for sub-sections and service lists
- Unique meta title and meta description per page
- Schema markup on every page — LocalBusiness schema on homepage and contact, Service schema on all service pages
- Canonical tag on every page using https://www.csae.ie as base domain
- Alt text on every image placeholder
- Clean URL structure — all pages served as /path/ (no .html extensions)
- Target location keywords throughout: Cork, Mallow, Cork City, County Cork

## Asset Paths
- All asset paths use absolute paths from root: `/assets/filename.ext`
- Never use relative paths like `assets/` or `../assets/` — always `/assets/`

## Design Rules
- Fixed header with blur backdrop, logo left, nav centre, phone number + Get a Quote CTA button right
- Hero section on every page — full width, dark overlay on background image, H1 headline, subtext, two CTA buttons (Get a Quote + Call Now)
- Stats bar below hero on homepage — Years Trading, Jobs Completed, Areas Covered, Accreditations (use placeholder numbers)
- Every page must have a lead gen form — either inline contact form or a sticky CTA bar linking to contact page
- Contact form fields: First Name, Last Name, Phone, Email, Service Required (dropdown), Message, How did you hear about us (dropdown) — NO GHL iframe yet, just HTML form styled to brand
- Accreditation logos bar on homepage and about page — SEAI approved, RECI (placeholders, styled as grey boxes with text for now)
- Google Reviews section on homepage — show 3 placeholder review cards with 5 stars, name, and dummy text
- Testimonials carousel on about page
- Services grid on homepage — 4 cards residential, 4 cards commercial, each linking to relevant page
- About page — company story placeholder, team section placeholder, why choose us section, accreditations
- Each sub-service page — H1 service title, intro paragraph, why choose CSAE for this service, how it works (3 steps), related services, lead gen form at bottom
- Mobile first — hamburger menu on mobile, single column layouts, tap-to-call phone number
- Prowired-style dark sections alternating with Capital Electrical-style light sections throughout

## Image Placeholders
- All images use placeholder divs with background-color: #1B2A4A and a label describing what the image should be
- Label format: [IMAGE: Hero — electrician working on fuse board Cork]
- We will replace with Higgsfield AI generated images later

## Vercel Config
- `vercel.json` at root with `cleanUrls: true` and `trailingSlash: false`
- Deployed to: https://csae-website.vercel.app (confirm after deployment)

## Rules
- Always read this CLAUDE.md before doing anything
- Build one file at a time, show me when complete before moving to next
- Never invent contact details — use exactly what is provided above
- Use placeholder text [PLACEHOLDER: description] anywhere David's specific info is needed
- Every page must be fully self-contained HTML/CSS — no external frameworks except Google Fonts
- All CSS scoped to avoid Elementor conflicts when deployed to WordPress
- All internal links must use clean absolute paths (e.g. /residential/house-rewiring/) not .html filenames
- All asset paths must use /assets/ (absolute, not relative)
- Test mobile layout mentally before declaring each file done
