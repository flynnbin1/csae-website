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

## Site Structure — Build Each As Separate HTML File
- header.html (fixed nav, phone number, logo, CTA button)
- footer.html (logo, links, contact details, accreditations, copyright)
- index.html (Homepage)
- about.html (About Page)
- residential.html (Residential Services overview)
- commercial.html (Commercial Services overview)
- solar.html (Solar Page)
- contact.html (Contact Page)

### Residential Sub-Service Pages (each a separate file)
- house-rewiring.html
- new-build-electrical.html
- fuse-board-upgrades.html
- lighting-installation.html
- ev-charger-installation.html
- electrical-safety-inspections.html
- socket-switch-installation.html
- electric-shower-installation.html
- kitchen-appliance-wiring.html
- smoke-carbon-monoxide-alarms.html
- outdoor-garden-lighting.html
- emergency-electrical-repairs.html

### Commercial Sub-Service Pages (each a separate file)
- commercial-electrical-installation.html
- security-systems-access-control.html
- generator-backup-systems.html
- energy-efficiency-auditing.html
- factory-plant-wiring.html
- machinery-installations.html
- industrial-lighting.html
- office-retail-fitouts.html
- emergency-lighting.html
- electrical-maintenance-contracts.html
- data-network-cabling.html
- commercial-fuse-board-upgrades.html
- led-lighting-upgrades.html
- periodic-electrical-inspections.html

## Contact Details
- Phone: 0857188103
- Email: info@csae.ie
- Address: Cork Solar and Electrical, Railway Cottage, Ballinamona, Mourneabbey, Mallow, P51RR22
- Domain: corksolarandelectrical.ie

## SEO Rules — Apply To Every Single Page
- Unique H1 per page targeting a specific keyword
- H2s for each major section
- H3s for sub-sections and service lists
- Unique meta title and meta description per page
- Schema markup on every page — LocalBusiness schema on homepage and contact, Service schema on all service pages
- Canonical tag on every page
- Alt text on every image placeholder
- Clean URL structure matching the filenames above
- Target location keywords throughout: Cork, Mallow, Cork City, County Cork

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

## Build Order
1. header.html
2. footer.html
3. index.html
4. about.html
5. residential.html
6. commercial.html
7. solar.html
8. contact.html
9. Then all residential sub-service pages
10. Then all commercial sub-service pages

## Rules
- Always read this CLAUDE.md before doing anything
- Build one file at a time, show me when complete before moving to next
- Never invent contact details — use exactly what is provided above
- Use placeholder text [PLACEHOLDER: description] anywhere David's specific info is needed
- Every page must be fully self-contained HTML/CSS — no external frameworks except Google Fonts
- All CSS scoped to avoid Elementor conflicts when deployed to WordPress
- Test mobile layout mentally before declaring each file done
