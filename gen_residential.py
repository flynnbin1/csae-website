#!/usr/bin/env python3
"""Generate all 11 remaining residential sub-service pages from house-rewiring.html template."""
import os, re

BASE = 'C:/Users/niall/Desktop/csae-website'

with open(f'{BASE}/house-rewiring.html', 'r', encoding='utf-8') as f:
    TMPL = f.read()

# ── SVG icon helpers ────────────────────────────────────────────────────────
I_SHIELD = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
I_DOC    = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>'
I_HOME   = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M3 9l9-7 9 7v11a2 2 0 01-2 2H5a2 2 0 01-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>'
I_ZAP    = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>'
I_CLOCK  = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="2"/><polyline points="12,7 12,12 15,15" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'
I_CHECK  = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2"/></svg>'
I_TOOL   = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg>'
I_ALERT  = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>'
I_SUN    = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="5" stroke="currentColor" stroke-width="2"/><line x1="12" y1="2" x2="12" y2="4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="12" y1="20" x2="12" y2="22" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="2" y1="12" x2="4" y2="12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="20" y1="12" x2="22" y2="12" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'

# ── Related card lookup ─────────────────────────────────────────────────────
RC = {
    'house-rewiring': ('assets/csae-res-house-rewiring.jpg.png', 'House rewiring in Cork', 'House Rewiring', 'Full and partial house rewires to ETCI standards. RECI registered electricians across Cork City and County Cork.', 'house-rewiring.html'),
    'new-build-electrical': ('assets/csae-res-new-build.jpg.png', 'New build electrical installation in Cork', 'New Build Electrical', 'Full first fix to final fix electrical installations for new build homes across Cork.', 'new-build-electrical.html'),
    'fuse-board-upgrades': ('assets/csae-res-fuse-board.jpg.png', 'Fuse board upgrade in Cork', 'Fuse Board Upgrades', 'Upgrade your old fuse board to a modern consumer unit with RCD protection and a Completion Certificate.', 'fuse-board-upgrades.html'),
    'lighting-installation': ('assets/csae-res-lighting.jpg.png', 'Lighting installation in Cork', 'Lighting Installation', 'LED downlights, pendants, dimmer switches and full lighting circuit installations across Cork.', 'lighting-installation.html'),
    'ev-charger-installation': ('assets/csae-res-ev-charger.jpg.png', 'EV charger installation in Cork', 'EV Charger Installation', 'SEAI approved home EV charger installations. Eligible for the SEAI EV Home Charger Grant.', 'ev-charger-installation.html'),
    'electrical-safety-inspections': ('assets/csae-res-safety-inspection.jpg.png', 'Electrical safety inspection in Cork', 'Electrical Safety Inspections', 'Periodic Inspection Reports (PIR) for homeowners, landlords and property buyers in Cork.', 'electrical-safety-inspections.html'),
    'socket-switch-installation': ('assets/csae-res-socket-light.jpg.png', 'Socket and switch installation in Cork', 'Socket &amp; Switch Installation', 'Additional sockets, USB outlets and switch replacements professionally installed throughout your home.', 'socket-switch-installation.html'),
    'electric-shower-installation': ('assets/csae-res-electric-shower.jpg.png', 'Electric shower installation in Cork', 'Electric Shower Installation', 'Dedicated circuit installation and shower wiring to ETCI Part P bathroom regulations.', 'electric-shower-installation.html'),
    'kitchen-appliance-wiring': ('assets/csae-res-house-rewiring.jpg.png', 'Kitchen appliance wiring in Cork', 'Kitchen Appliance Wiring', 'Cooker, hob, dishwasher and kitchen appliance circuit installation and safe connection.', 'kitchen-appliance-wiring.html'),
    'smoke-carbon-monoxide-alarms': ('assets/csae-res-smoke-alarms.jpg.png', 'Smoke and CO alarm installation in Cork', 'Smoke &amp; CO Alarms', 'Mains-wired interconnected smoke alarms and carbon monoxide detectors for your home.', 'smoke-carbon-monoxide-alarms.html'),
    'outdoor-garden-lighting': ('assets/csae-res-garden-lighting.jpg.png', 'Outdoor and garden lighting in Cork', 'Outdoor &amp; Garden Lighting', 'Security floodlights, garden feature lighting and outdoor socket installation in Cork.', 'outdoor-garden-lighting.html'),
    'emergency-electrical-repairs': ('assets/csae-res-emergency-callout.jpg.png', 'Emergency electrical callout in Cork', 'Emergency Electrical Repairs', 'Fast response to electrical faults, tripping fuses and power failures across Cork City and County.', 'emergency-electrical-repairs.html'),
}

def related_card(key):
    img, alt, title, desc, href = RC[key]
    return f'''
                    <div class="csae-related-card">
                        <img src="{img}" alt="{alt}" class="csae-related-card__img" width="400" height="180" loading="lazy">
                        <h3 class="csae-related-card__title">{title}</h3>
                        <p class="csae-related-card__desc">{desc}</p>
                        <a href="{href}" class="csae-related-card__link">Learn More &rarr;</a>
                    </div>'''

def reasons_block(label, h2, intro, r1, r2, r3):
    """r1/r2/r3 = (icon_svg, title, desc)"""
    def card(icon, title, desc):
        return f'''
                    <div class="csae-reason-card">
                        <div class="csae-reason-card__icon" aria-hidden="true">
                            {icon}
                        </div>
                        <h3 class="csae-reason-card__title">{title}</h3>
                        <p class="csae-reason-card__desc">{desc}</p>
                    </div>'''
    return (
        f'        <!-- ===== 3. WHY STRIP ===== -->\n'
        f'        <section class="csae-reasons" id="why-rewire" aria-labelledby="reasons-heading">\n'
        f'            <div class="csae-container">\n'
        f'                <div class="csae-reasons__header">\n'
        f'                    <span class="csae-section-label">{label}</span>\n'
        f'                    <h2 class="csae-section-title" id="reasons-heading">{h2}</h2>\n'
        f'                    <p class="csae-section-intro">{intro}</p>\n'
        f'                </div>\n'
        f'                <div class="csae-reasons__grid">'
        + card(*r1) + card(*r2) + card(*r3) +
        f'\n                </div>\n'
        f'            </div>\n'
        f'        </section>\n\n'
    )

def related_block(related_intro, *keys):
    cards = ''.join(related_card(k) for k in keys)
    return (
        f'        <!-- ===== 6. RELATED SERVICES ===== -->\n'
        f'        <section class="csae-related" id="related" aria-labelledby="related-heading">\n'
        f'            <div class="csae-container">\n'
        f'                <div class="csae-related__header">\n'
        f'                    <span class="csae-section-label">Also From CSAE</span>\n'
        f'                    <h2 class="csae-section-title" id="related-heading">Related Services</h2>\n'
        f'                    <p class="csae-section-intro">{related_intro}</p>\n'
        f'                </div>\n'
        f'                <div class="csae-related__grid">'
        + cards +
        f'\n                </div>\n'
        f'            </div>\n'
        f'        </section>\n\n'
    )

def intro_content(label, h2, paras, checks):
    p_html = ''.join(f'\n                        <p class="csae-sub-intro__body">{p}</p>' for p in paras)
    li_html = ''.join(f'\n                            <li class="csae-sub-intro__check">{c}</li>' for c in checks)
    return (
        f'                        <span class="csae-sub-intro__label">{label}</span>\n'
        f'                        <h2 class="csae-sub-intro__title" id="intro-heading">{h2}</h2>'
        + p_html +
        f'\n                        <ul class="csae-sub-intro__checks" aria-label="Service highlights">'
        + li_html +
        f'\n                        </ul>'
    )

def replace_block(html, start_marker, end_marker, new_content):
    parts = html.split(start_marker, 1)
    after = parts[1].split(end_marker, 1)
    return parts[0] + new_content + end_marker + after[1]

def generate(page):
    html = TMPL

    # ── SEO ────────────────────────────────────────────────────────────────
    html = html.replace(
        '<title>House Rewiring Cork | Cork Solar &amp; Electrical</title>',
        f'<title>{page["title"]} | Cork Solar &amp; Electrical</title>'
    )
    html = html.replace(
        '<meta name="description" content="Professional house rewiring services across Cork City and County Cork. Full and partial rewires to ETCI standards. RECI registered, Safe Electric approved. Free quotes. Call 085 216 8789.">',
        f'<meta name="description" content="{page["meta_desc"]}">'
    )
    html = html.replace(
        '<link rel="canonical" href="https://corksolarandelectrical.ie/house-rewiring.html">',
        f'<link rel="canonical" href="https://corksolarandelectrical.ie/{page["filename"]}">'
    )
    html = html.replace(
        '<meta property="og:title" content="House Rewiring Cork | Cork Solar &amp; Electrical">',
        f'<meta property="og:title" content="{page["title"]} | Cork Solar &amp; Electrical">'
    )
    html = html.replace(
        '<meta property="og:description" content="Expert house rewiring in Cork City and County Cork. Full and partial rewires, ETCI certified. RECI registered electricians. Free no-obligation quotes.">',
        f'<meta property="og:description" content="{page["og_desc"]}">'
    )
    html = html.replace(
        '<meta property="og:url" content="https://corksolarandelectrical.ie/house-rewiring.html">',
        f'<meta property="og:url" content="https://corksolarandelectrical.ie/{page["filename"]}">'
    )

    # ── Schema ────────────────────────────────────────────────────────────
    html = html.replace(
        '"serviceType": "House Rewiring",',
        f'"serviceType": "{page["schema_type"]}",'
    )
    html = html.replace(
        '"name": "House Rewiring Cork",',
        f'"name": "{page["schema_name"]}",'
    )
    html = html.replace(
        '"description": "Professional full and partial house rewiring across Cork City and County Cork. All work carried out to ETCI wiring regulations by RECI registered, Safe Electric approved electricians.",',
        f'"description": "{page["schema_desc"]}",'
    )

    # ── Hero ──────────────────────────────────────────────────────────────
    html = html.replace(
        'aria-label="House rewiring hero"',
        f'aria-label="{page["hero_aria"]}"'
    )
    html = html.replace(
        '<strong aria-current="page">House Rewiring</strong>',
        f'<strong aria-current="page">{page["breadcrumb"]}</strong>'
    )
    html = html.replace(
        '<h1>House Rewiring <span>Cork</span></h1>',
        f'<h1>{page["h1"]}</h1>'
    )
    html = html.replace(
        '<p class="csae-hero__sub">Professional full and partial house rewiring across Cork City and County. ETCI certified, RECI registered electricians.</p>',
        f'<p class="csae-hero__sub">{page["hero_sub"]}</p>'
    )

    # ── Intro image ───────────────────────────────────────────────────────
    html = html.replace(
        'src="assets/csae-res-house-rewiring.jpg.png" alt="Electrician carrying out house rewiring in Cork" class="csae-sub-intro__img"',
        f'src="{page["intro_img"]}" alt="{page["intro_img_alt"]}" class="csae-sub-intro__img"'
    )

    # ── Intro text block (label → end of checklist ul) ────────────────────
    intro_start = '                        <span class="csae-sub-intro__label">Residential Rewiring</span>'
    intro_end   = '                        </ul>'
    new_intro   = intro_content(page["intro_label"], page["intro_h2"], page["paras"], page["checks"])
    html = replace_block(html, intro_start, intro_end, new_intro)

    # ── Why / Reasons section ─────────────────────────────────────────────
    reasons_start = '        <!-- ===== 3. WHY REWIRE STRIP ===== -->'
    reasons_end   = '        <!-- ===== 4. HOW IT WORKS ===== -->'
    html = replace_block(html, reasons_start, reasons_end,
                         reasons_block(*page["reasons"]))

    # ── How It Works heading ──────────────────────────────────────────────
    html = html.replace(
        '<h2 class="csae-section-title" id="hiw-heading">How Our Rewiring Service Works</h2>',
        f'<h2 class="csae-section-title" id="hiw-heading">How Our {page["hiw_service"]} Service Works</h2>'
    )

    # ── Related Services section ──────────────────────────────────────────
    related_start = '        <!-- ===== 6. RELATED SERVICES ===== -->'
    related_end   = '        <!-- ===== 7. LEAD GEN FORM ===== -->'
    html = replace_block(html, related_start, related_end,
                         related_block(page["related_intro"], *page["related_keys"]))

    # ── Quote heading & body ───────────────────────────────────────────────
    html = html.replace(
        'Get a Free Rewiring Quote Today',
        page["quote_h2"]
    )
    html = html.replace(
        "Fill in the form and we'll be in touch to arrange a convenient time to assess your home and provide a clear, written quote \u2014 no call-out fee, no obligation.",
        page["quote_body"]
    )

    # ── Form aria-label ────────────────────────────────────────────────────
    html = html.replace(
        'aria-label="House rewiring quote request form"',
        f'aria-label="{page["form_aria"]}"'
    )

    out = f'{BASE}/{page["filename"]}'
    with open(out, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  Written: {page["filename"]}')


# ════════════════════════════════════════════════════════════════════════════
#  PAGE DEFINITIONS
# ════════════════════════════════════════════════════════════════════════════
PAGES = [

# ── 1. New Build Electrical ──────────────────────────────────────────────────
{
    'filename': 'new-build-electrical.html',
    'title': 'New Build Electrical Installations Cork',
    'meta_desc': 'Expert electrical installations for new build homes across Cork City and County Cork. Full first fix to final fix wiring. RECI registered. Free quotes. Call 085 216 8789.',
    'og_desc': 'New build electrical installations in Cork. First fix to final fix wiring by RECI registered electricians. Free no-obligation quotes.',
    'schema_type': 'New Build Electrical Installations',
    'schema_name': 'New Build Electrical Installations Cork',
    'schema_desc': 'Full new build electrical installations across Cork City and County Cork, from first fix to final fix, carried out by RECI registered, Safe Electric approved electricians.',
    'hero_aria': 'New build electrical hero',
    'breadcrumb': 'New Build Electrical',
    'h1': 'New Build Electrical <span>Installations Cork</span>',
    'hero_sub': 'Full first fix to final fix electrical installations for new build homes across Cork City and County Cork.',
    'intro_img': 'assets/csae-res-new-build.jpg.png',
    'intro_img_alt': 'Electrician wiring a new build home in Cork',
    'intro_label': 'New Build Wiring',
    'intro_h2': 'New Build Electrical Installations in Cork',
    'paras': [
        'Cork Solar &amp; Electrical provide complete electrical installations for new build homes across Cork City and County Cork. We work closely with builders, contractors and self-builders to deliver a full first fix and second fix wiring service that meets all current ETCI wiring regulations and Building Control Requirements.',
        'Our team of six qualified electricians handle everything from your consumer unit and cable routes through to final connections, sockets, switches and lighting circuits. We work to your build programme and co-ordinate directly with your main contractor to keep the project on schedule.',
        'Whether you are building a single dwelling or a small residential development, we provide competitive fixed-price quotations and issue a full Electrical Installation Completion Certificate on handover. Contact us today for a free quote.',
    ],
    'checks': [
        'Complete first fix and second fix wiring service',
        'Domestic wiring to current ETCI regulations',
        'Full Electrical Installation Completion Certificate on handover',
        'Working alongside builders, contractors and self-builders',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Key Considerations', 'Why Use a Specialist for New Build Wiring?',
        'Involving your electrician early avoids costly rerouting, delays and compliance failures at the end of a build.',
        (I_SHIELD, 'Plan Ahead, Avoid Problems', 'Getting your electrician involved at the design stage avoids costly cable rerouting and programme delays later. We advise on circuit layouts, consumer unit position and first-fix routes before walls are closed in.'),
        (I_ZAP,    'Future-Ready Wiring',         'We install wiring infrastructure for EV chargers, solar PV systems, smart home controls and additional circuits from the outset — ensuring your new home is ready for the technology of today and tomorrow.'),
        (I_DOC,    'ETCI Certified Handover',     'Every new build we complete is tested and commissioned to current ETCI wiring regulations. You receive a full Electrical Installation Completion Certificate for your lender, insurer and local authority at handover.'),
    ),
    'hiw_service': 'New Build Electrical',
    'related_intro': 'Other electrical services you may need alongside your new build wiring.',
    'related_keys': ['fuse-board-upgrades', 'ev-charger-installation', 'lighting-installation'],
    'quote_h2': 'Get a Free New Build Electrical Quote Today',
    'quote_body': "Fill in the form and we'll be in touch to discuss your project requirements and arrange a free site visit \u2014 no call-out fee, no obligation.",
    'form_aria': 'New build electrical quote request form',
},

# ── 2. Fuse Board Upgrades ───────────────────────────────────────────────────
{
    'filename': 'fuse-board-upgrades.html',
    'title': 'Fuse Board Upgrades Cork',
    'meta_desc': 'Professional fuse board and consumer unit upgrades across Cork City and County Cork. Dual RCD protection to ETCI standards. Completion certificate same day. Free quotes. Call 085 216 8789.',
    'og_desc': 'Fuse board and consumer unit upgrades in Cork. Dual RCD protection, certified same day. RECI registered electricians. Free no-obligation quotes.',
    'schema_type': 'Fuse Board Upgrades',
    'schema_name': 'Fuse Board Upgrades Cork',
    'schema_desc': 'Professional fuse board and consumer unit upgrades across Cork City and County Cork. Dual RCD protection installed to current ETCI wiring regulations by RECI registered electricians.',
    'hero_aria': 'Fuse board upgrades hero',
    'breadcrumb': 'Fuse Board Upgrades',
    'h1': 'Fuse Board Upgrades <span>Cork</span>',
    'hero_sub': 'Replace your old fuse board with a modern consumer unit with full RCD protection. ETCI certified, same-day completion.',
    'intro_img': 'assets/csae-res-fuse-board.jpg.png',
    'intro_img_alt': 'New consumer unit installed in a Cork home',
    'intro_label': 'Consumer Unit Upgrades',
    'intro_h2': 'Fuse Board Upgrades in Cork',
    'paras': [
        'Cork Solar &amp; Electrical replace outdated fuse boards and consumer units in homes across Cork City and County Cork. An old fuse board — particularly one with ceramic fuses or no RCD protection — is a serious safety risk and may leave your home uninsurable or non-compliant with current standards.',
        'We replace old fuse boards with modern dual RCD consumer units that fully meet current ETCI wiring regulations. The work is typically completed in a single day with minimal disruption. We isolate the power, remove the old unit, install the new consumer unit, test all circuits, and issue your Electrical Installation Completion Certificate on the same day.',
        'Fuse board upgrades are also required when adding EV chargers, solar panels, electric showers or additional circuits. If your board is full or outdated, contact us today for a free assessment and written quote.',
    ],
    'checks': [
        'Replacement of old fuse boards and consumer units',
        'Dual RCD protection to current ETCI standards',
        'Typically completed in a single day',
        'Electrical Installation Completion Certificate issued same day',
        'Free no-obligation quote and on-site assessment',
    ],
    'reasons': (
        'Why It Matters', 'Why Upgrade Your Fuse Board?',
        'An outdated fuse board is one of the most common electrical hazards in Irish homes. Here is why an upgrade may be essential for your property.',
        (I_SHIELD, 'Protect Your Home',       'Old fuse boards with ceramic fuses or no RCD protection cannot safely handle the demands of a modern home. An upgrade eliminates shock and fire risks and ensures every circuit is properly protected under current regulations.'),
        (I_DOC,    'Meet Insurance Requirements', 'Many home insurers now require a modern consumer unit with RCD protection. A fuse board upgrade with a Completion Certificate can resolve insurance issues, support mortgage applications and prepare a property for sale.'),
        (I_ZAP,    'Enable Future Upgrades',  'Adding an EV charger, solar system or electric shower requires a spare circuit and a consumer unit with sufficient capacity. A new unit ensures your home can accommodate these additions without further electrical works.'),
    ),
    'hiw_service': 'Fuse Board Upgrade',
    'related_intro': 'Other residential electrical services often carried out alongside a fuse board upgrade.',
    'related_keys': ['house-rewiring', 'electrical-safety-inspections', 'ev-charger-installation'],
    'quote_h2': 'Get a Free Fuse Board Upgrade Quote Today',
    'quote_body': "Fill in the form and we'll be in touch to arrange a convenient time to assess your current setup and provide a clear, written quote \u2014 no call-out fee, no obligation.",
    'form_aria': 'Fuse board upgrade quote request form',
},

# ── 3. Lighting Installation ─────────────────────────────────────────────────
{
    'filename': 'lighting-installation.html',
    'title': 'Lighting Installation Cork',
    'meta_desc': 'Professional lighting installation services across Cork City and County Cork. LED downlights, pendants, dimmer switches and full lighting circuits. RECI registered. Free quotes. Call 085 216 8789.',
    'og_desc': 'Lighting installation in Cork. LED downlights, dimmers, pendants and full lighting circuits by RECI registered electricians. Free no-obligation quotes.',
    'schema_type': 'Lighting Installation',
    'schema_name': 'Lighting Installation Cork',
    'schema_desc': 'Professional residential lighting installation across Cork City and County Cork, including LED downlights, pendant lighting, dimmer switches and full circuit installations by RECI registered electricians.',
    'hero_aria': 'Lighting installation hero',
    'breadcrumb': 'Lighting Installation',
    'h1': 'Lighting Installation <span>Cork</span>',
    'hero_sub': 'LED downlights, pendant lighting, dimmer switches and full lighting circuit installations across Cork City and County Cork.',
    'intro_img': 'assets/csae-res-lighting.jpg.png',
    'intro_img_alt': 'LED lighting installation in a Cork home',
    'intro_label': 'Residential Lighting',
    'intro_h2': 'Lighting Installation Services in Cork',
    'paras': [
        'Cork Solar &amp; Electrical install all types of residential lighting across Cork City and County Cork. Whether you are fitting LED downlights throughout a new extension, installing pendant lighting in a kitchen renovation, or upgrading to LED throughout your home, our qualified electricians carry out every installation safely and to the highest standard.',
        'We work with homeowners, interior designers and contractors across Cork to deliver lighting schemes that are safe, energy-efficient and professionally finished. From basic ceiling light replacements to full multi-room lighting circuits with dimmers and smart controls, we handle it all.',
        'All our lighting installations are carried out to current ETCI wiring regulations and include full testing and sign-off. Contact us for a free, no-obligation quote.',
    ],
    'checks': [
        'LED downlight and pendant lighting installation',
        'Dimmer switches and smart lighting wiring',
        'Outdoor security and feature lighting',
        'Full multi-room lighting circuit installation',
        'ETCI certified, fully tested and signed off',
    ],
    'reasons': (
        'Why It Matters', 'What to Expect From a Professional Lighting Installation',
        'A properly designed and installed lighting scheme is safer, more energy-efficient and more enjoyable to live with than a DIY solution.',
        (I_SHIELD, 'Safe &amp; Certified Installations', 'All lighting installations are carried out to ETCI wiring regulations by our RECI registered electricians. Every installation is fully tested and certified — no shortcuts, no loose connections, no fire risks from overloaded rose boxes.'),
        (I_ZAP,    'Energy-Efficient LED Solutions',    'We specify and install high-quality LED fittings that dramatically reduce your electricity bills. Switching a full home from halogen to LED can cut lighting energy use by over 80% with no compromise on quality of light.'),
        (I_HOME,   'Neat, Professional Finish',         'Our electricians take pride in tidy, discreet cable routing and clean finishes. We work carefully in finished rooms to minimise disruption and mess — and always leave your home the way we found it.'),
    ),
    'hiw_service': 'Lighting Installation',
    'related_intro': 'Other residential electrical services you may need alongside a lighting installation.',
    'related_keys': ['house-rewiring', 'socket-switch-installation', 'outdoor-garden-lighting'],
    'quote_h2': 'Get a Free Lighting Installation Quote Today',
    'quote_body': "Fill in the form and we'll be in touch to discuss your lighting project and arrange a free site visit \u2014 no call-out fee, no obligation.",
    'form_aria': 'Lighting installation quote request form',
},

# ── 4. EV Charger Installation ───────────────────────────────────────────────
{
    'filename': 'ev-charger-installation.html',
    'title': 'EV Charger Installation Cork',
    'meta_desc': 'SEAI approved home EV charger installation across Cork City and County Cork. Eligible for SEAI EV Home Charger Grant. RECI registered electricians. Free quotes. Call 085 216 8789.',
    'og_desc': 'SEAI approved EV charger installation in Cork. Eligible for the SEAI EV Home Charger Grant. RECI registered electricians. Free no-obligation quotes.',
    'schema_type': 'EV Charger Installation',
    'schema_name': 'EV Charger Installation Cork',
    'schema_desc': 'SEAI approved home EV charger installations across Cork City and County Cork. Eligible for the SEAI EV Home Charger Grant. Carried out by RECI registered, Safe Electric approved electricians.',
    'hero_aria': 'EV charger installation hero',
    'breadcrumb': 'EV Charger Installation',
    'h1': 'EV Charger Installation <span>Cork</span>',
    'hero_sub': 'SEAI approved home EV charger installations across Cork City and County Cork. Eligible for the SEAI EV Home Charger Grant.',
    'intro_img': 'assets/csae-res-ev-charger.jpg.png',
    'intro_img_alt': 'Home EV charger installation in Cork',
    'intro_label': 'EV Charging Solutions',
    'intro_h2': 'EV Charger Installation in Cork',
    'paras': [
        'Cork Solar &amp; Electrical install home EV chargers for electric and hybrid vehicle owners across Cork City and County Cork. We are SEAI approved contractors, making us one of the few electricians authorised to install home chargers that qualify for the SEAI EV Home Charger Grant — currently worth up to &euro;300.',
        'We install Type 2 AC home chargers from leading manufacturers and ensure every installation is fully compliant with current ETCI wiring regulations. Our electricians assess your consumer unit, install the correct cable run, mount your charger in the most practical location and commission the unit before handing over.',
        'From apartments and townhouses to detached homes and farmhouses across County Cork, we find the right charging solution for every property. Contact us today for a free quote and to confirm your eligibility for the SEAI grant.',
    ],
    'checks': [
        'SEAI approved EV charger installation',
        'Eligible for the SEAI EV Home Charger Grant (up to \u20ac300)',
        'Type 2 AC charger installation from leading brands',
        'Full ETCI wiring compliance and Completion Certificate',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Why It Matters', 'Why Install a Home EV Charger?',
        'A dedicated home charger is faster, safer and cheaper to run than using a three-pin socket. Here is what you need to know before installing.',
        (I_DOC,   'SEAI Grant Eligible',      'As SEAI approved contractors, we can install your home EV charger under the SEAI EV Home Charger Grant scheme, worth up to \u20ac300. We guide you through the grant application and handle all required documentation on your behalf.'),
        (I_SHIELD,'Safe &amp; Certified Installation', 'EV charger installation must be carried out by a qualified, registered electrician. Our team ensures the correct cable sizing, MCB protection and earthing are in place for a safe, compliant and long-lasting installation.'),
        (I_ZAP,   'Future-Proof Your Home',  'A dedicated charging point is faster and far safer than a 3-pin extension lead. With EV ownership growing rapidly, having a proper charging circuit also makes your home more attractive to future buyers.'),
    ),
    'hiw_service': 'EV Charger Installation',
    'related_intro': 'Other residential electrical services that complement a home EV charger installation.',
    'related_keys': ['fuse-board-upgrades', 'house-rewiring', 'electrical-safety-inspections'],
    'quote_h2': 'Get a Free EV Charger Installation Quote Today',
    'quote_body': "Fill in the form and we'll be in touch to discuss your EV charger requirements and confirm your eligibility for the SEAI grant \u2014 no call-out fee, no obligation.",
    'form_aria': 'EV charger installation quote request form',
},

# ── 5. Electrical Safety Inspections ────────────────────────────────────────
{
    'filename': 'electrical-safety-inspections.html',
    'title': 'Electrical Safety Inspections Cork',
    'meta_desc': 'Periodic Inspection Reports (PIR) for homeowners, landlords and property buyers across Cork City and County Cork. RECI registered electricians. Free quotes. Call 085 216 8789.',
    'og_desc': 'Electrical safety inspections and Periodic Inspection Reports in Cork. For homeowners, landlords and property buyers. RECI registered electricians. Free no-obligation quotes.',
    'schema_type': 'Electrical Safety Inspections',
    'schema_name': 'Electrical Safety Inspections Cork',
    'schema_desc': 'Periodic Inspection Reports (PIR) for homeowners, landlords and property buyers across Cork City and County Cork, carried out by RECI registered, Safe Electric approved electricians.',
    'hero_aria': 'Electrical safety inspection hero',
    'breadcrumb': 'Electrical Safety Inspections',
    'h1': 'Electrical Safety Inspections <span>Cork</span>',
    'hero_sub': 'Periodic Inspection Reports (PIR) for homeowners, landlords and property buyers across Cork City and County Cork.',
    'intro_img': 'assets/csae-res-safety-inspection.jpg.png',
    'intro_img_alt': 'Electrician carrying out an electrical safety inspection in Cork',
    'intro_label': 'Periodic Inspection Reports',
    'intro_h2': 'Electrical Safety Inspections in Cork',
    'paras': [
        'Cork Solar &amp; Electrical carry out Periodic Inspection Reports (PIR) for homeowners, landlords and property buyers across Cork City and County Cork. An electrical safety inspection gives you a clear picture of the condition of your property\'s wiring and identifies any faults, defects or areas that fall short of current ETCI standards.',
        'Our RECI registered electricians carry out a full visual inspection and live testing of all circuits, sockets, switches, fuse boards and bonding. We issue a detailed written report with observations categorised by urgency — Code 1 (Dangerous), Code 2 (Potentially Dangerous) or Code 3 (Improvement Recommended).',
        'Inspections are required by landlords under Irish rental legislation, recommended for any home over 25 years old, and often required by lenders and insurers. Contact us today for a free quote on your inspection.',
    ],
    'checks': [
        'Periodic Inspection Reports (PIR) to current ETCI standards',
        'Full visual and live circuit testing by RECI registered electricians',
        'Detailed written report with categorised observations',
        'Required for landlords under Irish rental legislation',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Why It Matters', 'Who Needs an Electrical Safety Inspection?',
        'Electrical inspections are not just for older homes. Here are the most common reasons homeowners, landlords and buyers request a PIR.',
        (I_DOC,   'Required for Landlords',      'Under Irish rental legislation, landlords must maintain properties to a safe electrical standard. A Periodic Inspection Report demonstrates compliance and protects both landlord and tenant. We provide documentation ready for inspection.'),
        (I_SHIELD,'Peace of Mind for Buyers',    'Buying a property without knowing the true condition of its wiring carries serious risk. Our PIR identifies dangerous wiring, outdated systems and hidden hazards before you commit — giving you the full picture before signing.'),
        (I_CHECK, 'Insurance &amp; Mortgage Support', 'Many insurers and lenders now require a current electrical inspection report before issuing cover or mortgage approval. We provide a clear, certified report that meets all standard requirements for homeowners and landlords alike.'),
    ),
    'hiw_service': 'Electrical Inspection',
    'related_intro': 'Other residential electrical services that commonly follow an inspection report.',
    'related_keys': ['house-rewiring', 'fuse-board-upgrades', 'emergency-electrical-repairs'],
    'quote_h2': 'Book an Electrical Safety Inspection Today',
    'quote_body': "Fill in the form and we'll get back to you to arrange a convenient time to carry out your inspection and issue a full written report \u2014 no call-out fee, no obligation.",
    'form_aria': 'Electrical safety inspection quote request form',
},

# ── 6. Socket & Switch Installation ─────────────────────────────────────────
{
    'filename': 'socket-switch-installation.html',
    'title': 'Socket &amp; Switch Installation Cork',
    'meta_desc': 'Professional socket and switch installation across Cork City and County Cork. Additional sockets, USB outlets, dimmer switches and full upgrades. RECI registered. Free quotes. Call 085 216 8789.',
    'og_desc': 'Socket and switch installation in Cork. Additional sockets, USB outlets and dimmer switches installed by RECI registered electricians. Free no-obligation quotes.',
    'schema_type': 'Socket and Switch Installation',
    'schema_name': 'Socket and Switch Installation Cork',
    'schema_desc': 'Professional socket and switch installation across Cork City and County Cork, including additional sockets, USB outlets and dimmer switches, by RECI registered, Safe Electric approved electricians.',
    'hero_aria': 'Socket and switch installation hero',
    'breadcrumb': 'Socket &amp; Switch Installation',
    'h1': 'Socket &amp; Switch Installation <span>Cork</span>',
    'hero_sub': 'Additional sockets, USB outlets, dimmer switches and switch upgrades professionally installed across Cork City and County Cork.',
    'intro_img': 'assets/csae-res-socket-light.jpg.png',
    'intro_img_alt': 'Electrician installing sockets and switches in a Cork home',
    'intro_label': 'Sockets &amp; Switches',
    'intro_h2': 'Socket &amp; Switch Installation in Cork',
    'paras': [
        'Cork Solar &amp; Electrical install and upgrade sockets, switches and USB outlets in homes across Cork City and County Cork. Whether you need additional sockets in a newly renovated room, USB charging outlets in a bedroom or a full socket upgrade throughout your home, our qualified electricians complete every installation safely and to ETCI standards.',
        'We install a wide range of socket and switch styles to complement any interior — from standard white to brushed chrome and matt black finishes. All installations are properly wired, fully tested and finished neatly, with no visible surface cables unless agreed with the homeowner.',
        'Additional sockets are one of the most common requests we receive after a house purchase or renovation. If you are relying on extension leads to cover a shortage of sockets, it is time to get them added properly. Contact us for a free, no-obligation quote.',
    ],
    'checks': [
        'Additional socket and USB outlet installation',
        'Switch, dimmer and smart switch replacement',
        'Surface and flush installations available',
        'All wiring to ETCI standards, fully tested',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Why It Matters', 'Why Have Sockets &amp; Switches Professionally Installed?',
        'Properly installed sockets are safer, neater and far more reliable than extension leads or DIY additions.',
        (I_SHIELD,'Eliminate Extension Lead Dangers', 'Overloaded extension leads are a leading cause of electrical fires. Properly installed fixed sockets eliminate this risk, distribute load correctly across your circuits and give a much cleaner, safer result that will last for decades.'),
        (I_HOME,  'Wide Range of Finishes',           'We supply and install sockets and switches in standard white, brushed steel, satin chrome and matt black. Whatever your interior style, we can match it with quality brand-name fittings that look great and last.'),
        (I_CHECK, 'Neat &amp; Discreet',              'Our electricians route cables neatly and discreetly wherever possible, keeping surface runs to a minimum in finished rooms. The result is a clean, professional installation with no unsightly trunking or trailing wires.'),
    ),
    'hiw_service': 'Socket &amp; Switch Installation',
    'related_intro': 'Other residential electrical services that complement a socket or switch installation.',
    'related_keys': ['lighting-installation', 'house-rewiring', 'fuse-board-upgrades'],
    'quote_h2': 'Get a Free Socket &amp; Switch Installation Quote',
    'quote_body': "Fill in the form and we'll be in touch to discuss your requirements and arrange a free site visit \u2014 no call-out fee, no obligation.",
    'form_aria': 'Socket and switch installation quote request form',
},

# ── 7. Electric Shower Installation ─────────────────────────────────────────
{
    'filename': 'electric-shower-installation.html',
    'title': 'Electric Shower Installation Cork',
    'meta_desc': 'Professional electric shower installation across Cork City and County Cork. Dedicated circuits, ETCI Part P bathroom compliance, completion certificate. RECI registered. Free quotes. Call 085 216 8789.',
    'og_desc': 'Electric shower installation in Cork. Dedicated circuit, ETCI Part P bathroom wiring. RECI registered electricians. Free no-obligation quotes.',
    'schema_type': 'Electric Shower Installation',
    'schema_name': 'Electric Shower Installation Cork',
    'schema_desc': 'Professional electric shower installation across Cork City and County Cork. Dedicated circuit installation to ETCI Part P bathroom regulations by RECI registered, Safe Electric approved electricians.',
    'hero_aria': 'Electric shower installation hero',
    'breadcrumb': 'Electric Shower Installation',
    'h1': 'Electric Shower Installation <span>Cork</span>',
    'hero_sub': 'Dedicated circuit installation and electric shower wiring to ETCI Part P bathroom regulations across Cork City and County Cork.',
    'intro_img': 'assets/csae-res-electric-shower.jpg.png',
    'intro_img_alt': 'Electric shower installation in a Cork bathroom',
    'intro_label': 'Electric Shower Wiring',
    'intro_h2': 'Electric Shower Installation in Cork',
    'paras': [
        'Cork Solar &amp; Electrical install and replace electric showers in homes across Cork City and County Cork. Electric showers are high-demand appliances that require a dedicated circuit, correct cable sizing and proper RCD protection — work that must be carried out by a qualified, RECI registered electrician.',
        'We install all major brands of electric shower and run a dedicated circuit from your consumer unit, ensuring the correct cable size for the kW rating of the unit, a properly installed pull cord isolator, and full compliance with ETCI Part P bathroom wiring regulations.',
        'Whether you are replacing an old shower unit, fitting a new shower in a bathroom renovation or adding one to an en-suite, we provide a safe, certified installation with a Completion Certificate included. Contact us today for a free, no-obligation quote.',
    ],
    'checks': [
        'Dedicated circuit installation from consumer unit',
        'All kW ratings — 7.5kW, 8.5kW, 9.5kW, 10.5kW and above',
        'ETCI Part P bathroom wiring compliance',
        'Full RCD protection and Completion Certificate',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Why It Matters', 'Why Electric Shower Wiring Must Be Done Correctly',
        'Bathrooms are a special location under ETCI wiring regulations. Here is why professional installation is essential.',
        (I_ZAP,   'Dedicated Circuit Required',       'Electric showers draw 30\u201350 amps depending on their kW rating and must have their own dedicated circuit from the consumer unit. Connecting to a shared circuit is both dangerous and non-compliant. We install the circuit correctly from the outset.'),
        (I_SHIELD,'Bathroom Wiring Regulations',      'Bathrooms are classified as special locations under ETCI wiring regulations with strict zoning requirements. Only qualified, registered electricians should carry out shower wiring — our team is fully trained in all Part P requirements.'),
        (I_CLOCK, 'Same-Day Installation',            'In most cases we can install your electric shower circuit and unit in a single day. We work neatly, leave your bathroom clean and issue your Completion Certificate before we leave — so you can use your new shower straight away.'),
    ),
    'hiw_service': 'Electric Shower Installation',
    'related_intro': 'Other residential electrical services that complement a new electric shower installation.',
    'related_keys': ['house-rewiring', 'fuse-board-upgrades', 'socket-switch-installation'],
    'quote_h2': 'Get a Free Electric Shower Installation Quote',
    'quote_body': "Fill in the form and we'll get back to you to discuss your shower installation and arrange a free assessment \u2014 no call-out fee, no obligation.",
    'form_aria': 'Electric shower installation quote request form',
},

# ── 8. Kitchen Appliance Wiring ──────────────────────────────────────────────
{
    'filename': 'kitchen-appliance-wiring.html',
    'title': 'Kitchen Appliance Wiring Cork',
    'meta_desc': 'Professional kitchen appliance wiring across Cork City and County Cork. Cookers, hobs, dishwashers, washing machines and integrated appliances. RECI registered. Free quotes. Call 085 216 8789.',
    'og_desc': 'Kitchen appliance wiring in Cork. Cookers, hobs, dishwashers and integrated appliances wired correctly by RECI registered electricians. Free no-obligation quotes.',
    'schema_type': 'Kitchen Appliance Wiring',
    'schema_name': 'Kitchen Appliance Wiring Cork',
    'schema_desc': 'Professional kitchen appliance wiring across Cork City and County Cork, including cookers, hobs, dishwashers and integrated appliances, by RECI registered, Safe Electric approved electricians.',
    'hero_aria': 'Kitchen appliance wiring hero',
    'breadcrumb': 'Kitchen Appliance Wiring',
    'h1': 'Kitchen Appliance Wiring <span>Cork</span>',
    'hero_sub': 'Cookers, hobs, dishwashers and integrated kitchen appliances correctly wired and connected across Cork City and County Cork.',
    'intro_img': 'assets/csae-res-house-rewiring.jpg.png',
    'intro_img_alt': 'Electrician wiring kitchen appliances in a Cork home',
    'intro_label': 'Appliance Wiring',
    'intro_h2': 'Kitchen Appliance Wiring in Cork',
    'paras': [
        'Cork Solar &amp; Electrical wire and connect kitchen appliances for homeowners across Cork City and County Cork. From electric cookers and induction hobs to dishwashers, washing machines, tumble dryers and integrated appliances, our qualified electricians ensure every connection is safe, correct and fully compliant with ETCI wiring regulations.',
        'Kitchen appliances often require dedicated circuits, correct cable sizing and accessible isolation switches. We install the full circuit from your consumer unit, fit the appropriate connection unit or outlet, and connect your appliance safely. We also upgrade existing circuits where the cable is too light for the appliance load.',
        'Planning a kitchen installation or fitting a new range cooker? Our electricians work alongside your kitchen fitter to ensure all appliances are wired and ready when needed — no delays, no damage to your new kitchen. Contact us for a free, no-obligation quote.',
    ],
    'checks': [
        'Cooker, hob and oven circuit installation',
        'Dishwasher, washing machine and tumble dryer connections',
        'Fused spur and isolation switch installation',
        'Dedicated circuits sized correctly to appliance load',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Why It Matters', 'Why Kitchen Appliance Wiring Must Be Done Right',
        'Getting the electrical side of a kitchen installation wrong creates serious risks. Here is what makes a professional installation different.',
        (I_ZAP,   'Correct Cable Sizing Matters',  'High-draw appliances like range cookers and induction hobs require heavier cable than standard sockets. Using an undersized cable is a serious fire risk. We specify and install the correct cable size for every appliance load.'),
        (I_SHIELD,'Proper Isolation Switches',     'Cookers, hobs and built-in appliances must have a readily accessible isolation switch within sight of the appliance. We install these correctly and to the required distance, ensuring both safety and ETCI compliance.'),
        (I_TOOL,  'Coordinated With Your Kitchen Fit', 'We work to your kitchen fitter\'s programme, ensuring appliances are wired at the right stage of the installation — no delays to your project and no risk of damage to your new units or worktops.'),
    ),
    'hiw_service': 'Kitchen Appliance Wiring',
    'related_intro': 'Other residential electrical services that complement kitchen appliance wiring.',
    'related_keys': ['socket-switch-installation', 'lighting-installation', 'fuse-board-upgrades'],
    'quote_h2': 'Get a Free Kitchen Wiring Quote Today',
    'quote_body': "Fill in the form and we'll be in touch to discuss your kitchen appliance wiring requirements and arrange a free assessment \u2014 no call-out fee, no obligation.",
    'form_aria': 'Kitchen appliance wiring quote request form',
},

# ── 9. Smoke & CO Alarms ────────────────────────────────────────────────────
{
    'filename': 'smoke-carbon-monoxide-alarms.html',
    'title': 'Smoke &amp; Carbon Monoxide Alarms Cork',
    'meta_desc': 'Mains-wired smoke alarms and carbon monoxide detector installation across Cork City and County Cork. Interconnected alarm systems for homeowners and landlords. RECI registered. Free quotes. Call 085 216 8789.',
    'og_desc': 'Smoke and carbon monoxide alarm installation in Cork. Mains-wired interconnected systems for homeowners and landlords. RECI registered electricians. Free no-obligation quotes.',
    'schema_type': 'Smoke and Carbon Monoxide Alarm Installation',
    'schema_name': 'Smoke and Carbon Monoxide Alarm Installation Cork',
    'schema_desc': 'Mains-wired smoke alarm and carbon monoxide detector installation across Cork City and County Cork, for homeowners and landlords, by RECI registered, Safe Electric approved electricians.',
    'hero_aria': 'Smoke and CO alarm installation hero',
    'breadcrumb': 'Smoke &amp; CO Alarms',
    'h1': 'Smoke &amp; Carbon Monoxide Alarms <span>Cork</span>',
    'hero_sub': 'Mains-wired interconnected smoke alarms and carbon monoxide detectors installed across Cork City and County Cork for homeowners and landlords.',
    'intro_img': 'assets/csae-res-smoke-alarms.jpg.png',
    'intro_img_alt': 'Mains-wired smoke alarm installation in a Cork home',
    'intro_label': 'Alarm Installations',
    'intro_h2': 'Smoke &amp; Carbon Monoxide Alarm Installation in Cork',
    'paras': [
        'Cork Solar &amp; Electrical install mains-wired smoke alarms and carbon monoxide detectors in homes across Cork City and County Cork. Under Irish Building Regulations, new builds and significantly renovated properties must have mains-wired smoke detection installed. Landlords are also legally required to have working smoke and CO alarms in all rental properties.',
        'We install interconnected mains-wired alarm systems so that if one alarm triggers, every alarm in the house sounds simultaneously. This gives maximum warning time to all occupants regardless of where the fire or CO source is located — far safer than independent battery-only alarms.',
        'We supply and install leading alarm brands and provide a Completion Certificate for all mains-wired installations. Battery alarms can also be supplied and fitted where mains wiring is not required. Contact us for a free quote.',
    ],
    'checks': [
        'Mains-wired smoke, heat and CO alarm installation',
        'Interconnected alarm systems for maximum coverage',
        'Compliant with Irish Building Regulations',
        'Certificate of Completion provided for all mains installations',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Why It Matters', 'Why Mains-Wired Alarms Are Worth Installing',
        'Mains-wired interconnected alarms offer significantly better protection than battery alternatives. Here is why they matter.',
        (I_ALERT, 'Required by Law for Landlords',  'Irish rental legislation requires landlords to install and maintain working smoke alarms in all rental properties. We install, certify and provide documentation for all landlord alarm installations, giving you a clear record of compliance.'),
        (I_SHIELD,'Interconnected for Maximum Safety', 'Our mains-wired alarm systems are interconnected — when one detector triggers, every alarm in the house sounds at once. This is far safer than individual battery alarms and is required in new and significantly renovated properties under Irish Building Regulations.'),
        (I_ZAP,   'CO Protection Saves Lives',       'Carbon monoxide is odourless and colourless — you cannot detect it without an alarm. We install CO detectors in all rooms with fuel-burning appliances and boilers, protecting your household from a threat that is completely invisible without the right equipment.'),
    ),
    'hiw_service': 'Alarm Installation',
    'related_intro': 'Other residential electrical services that complement a smoke and CO alarm installation.',
    'related_keys': ['electrical-safety-inspections', 'house-rewiring', 'emergency-electrical-repairs'],
    'quote_h2': 'Get a Free Alarm Installation Quote Today',
    'quote_body': "Fill in the form and we'll be in touch to discuss your alarm requirements and arrange a convenient time to carry out the installation \u2014 no call-out fee, no obligation.",
    'form_aria': 'Smoke and CO alarm installation quote request form',
},

# ── 10. Outdoor & Garden Lighting ────────────────────────────────────────────
{
    'filename': 'outdoor-garden-lighting.html',
    'title': 'Outdoor &amp; Garden Lighting Cork',
    'meta_desc': 'Professional outdoor and garden lighting installation across Cork City and County Cork. Security floodlights, feature lighting, pathway lights and outdoor sockets. RECI registered. Free quotes. Call 085 216 8789.',
    'og_desc': 'Outdoor and garden lighting installation in Cork. Security floodlights, garden feature lighting and outdoor sockets. RECI registered electricians. Free no-obligation quotes.',
    'schema_type': 'Outdoor and Garden Lighting Installation',
    'schema_name': 'Outdoor and Garden Lighting Cork',
    'schema_desc': 'Professional outdoor and garden lighting installation across Cork City and County Cork, including security floodlights, garden feature lighting and outdoor sockets, by RECI registered electricians.',
    'hero_aria': 'Outdoor and garden lighting hero',
    'breadcrumb': 'Outdoor &amp; Garden Lighting',
    'h1': 'Outdoor &amp; Garden Lighting <span>Cork</span>',
    'hero_sub': 'Security floodlights, garden feature lighting, pathway lights and outdoor sockets professionally installed across Cork City and County Cork.',
    'intro_img': 'assets/csae-res-garden-lighting.jpg.png',
    'intro_img_alt': 'Outdoor garden lighting installation in Cork',
    'intro_label': 'Outdoor Electrical',
    'intro_h2': 'Outdoor &amp; Garden Lighting in Cork',
    'paras': [
        'Cork Solar &amp; Electrical install outdoor and garden lighting for homes across Cork City and County Cork. From security floodlights and PIR-activated lights to decorative garden feature lighting, pathway lighting and outdoor sockets, our qualified electricians carry out every outdoor installation safely and to current ETCI standards.',
        'All outdoor electrical installations require weatherproof fittings, correctly IP-rated cables and proper earthing — work that must be carried out by a qualified, registered electrician. We ensure every installation is safe for the Irish climate and fully meets all relevant ETCI wiring regulations.',
        'Whether you are lighting a new garden design, adding security lighting to your driveway or installing outdoor sockets for a summer kitchen or workshop, we have a solution for your property. Contact us for a free, no-obligation quote.',
    ],
    'checks': [
        'Security floodlights and PIR-activated lighting',
        'Decorative garden and pathway feature lighting',
        'Outdoor weatherproof socket installation',
        'IP-rated cables and fittings throughout',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Why It Matters', 'What to Know Before Installing Outdoor Lighting',
        'Outdoor electrical work has specific requirements that make professional installation essential for safety and longevity.',
        (I_SHIELD,'Outdoor Wiring Must Be Safe',   'Outdoor electrical installations are exposed to rain, frost and UV. All cables, fittings and connections must be correctly rated for outdoor use. Our electricians specify and install only IP-rated, weatherproof components suitable for the Irish climate.'),
        (I_ZAP,   'Security &amp; Peace of Mind', 'PIR-activated security lighting deters intruders and improves safety around your home at night. We position lights to maximise coverage of driveways, gates and entry points while minimising light spillage into neighbours\' properties.'),
        (I_HOME,  'Enhance Your Outdoor Space',   'Well-designed garden lighting transforms an outdoor space and extends the time you can enjoy it after dark. We work with your garden layout to position lights for maximum effect — creating atmosphere without over-illuminating.'),
    ),
    'hiw_service': 'Outdoor Lighting Installation',
    'related_intro': 'Other residential electrical services that complement an outdoor lighting installation.',
    'related_keys': ['lighting-installation', 'socket-switch-installation', 'house-rewiring'],
    'quote_h2': 'Get a Free Outdoor Lighting Quote Today',
    'quote_body': "Fill in the form and we'll be in touch to discuss your outdoor lighting project and arrange a free site visit \u2014 no call-out fee, no obligation.",
    'form_aria': 'Outdoor and garden lighting quote request form',
},

# ── 11. Emergency Electrical Repairs ─────────────────────────────────────────
{
    'filename': 'emergency-electrical-repairs.html',
    'title': 'Emergency Electrical Repairs Cork',
    'meta_desc': 'Fast emergency electrical repairs across Cork City and County Cork. Tripping fuses, power failures, burning smells and fault diagnosis. RECI registered. Call 085 216 8789.',
    'og_desc': 'Emergency electrical repairs in Cork. Fast response to faults, tripping RCDs and power failures. RECI registered electricians. Call 085 216 8789.',
    'schema_type': 'Emergency Electrical Repairs',
    'schema_name': 'Emergency Electrical Repairs Cork',
    'schema_desc': 'Fast emergency electrical repair callouts across Cork City and County Cork, including fault diagnosis, tripping fuses, power failures and urgent electrical issues, by RECI registered electricians.',
    'hero_aria': 'Emergency electrical repairs hero',
    'breadcrumb': 'Emergency Electrical Repairs',
    'h1': 'Emergency Electrical Repairs <span>Cork</span>',
    'hero_sub': 'Fast response to electrical faults, tripping fuses, power failures and dangerous electrical issues across Cork City and County Cork.',
    'intro_img': 'assets/csae-res-emergency-callout.jpg.png',
    'intro_img_alt': 'Electrician carrying out emergency electrical repairs in Cork',
    'intro_label': 'Emergency Electrical',
    'intro_h2': 'Emergency Electrical Repairs in Cork',
    'paras': [
        'Cork Solar &amp; Electrical provide a fast emergency callout service for electrical faults, tripping fuses, power failures and dangerous electrical issues across Cork City and County Cork. Our qualified, RECI registered electricians are available for urgent callouts when you need safe, expert help quickly.',
        'Common emergency callouts we handle include: complete power loss, circuit breakers or RCDs tripping repeatedly, burning smells from sockets or fuse boards, sparking outlets, faults following storm damage, and electrical hazards identified during property inspections that require immediate attention.',
        'If you smell burning, see sparking, or have a situation that feels dangerous — turn off power at the mains if it is safe to do so, move away from the area, and call us immediately on 085 216 8789. Do not attempt repairs on live circuits.',
    ],
    'checks': [
        'Fast response to electrical emergencies across Cork',
        'Fault diagnosis and safe rectification by RECI registered electricians',
        'Tripping fuses, RCDs and circuit breakers',
        'Burning smells, sparking outlets and visible damage',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Warning Signs', "Don't Ignore These Warning Signs",
        'Some electrical problems feel minor but can quickly become dangerous. Here is what to watch for and what to do.',
        (I_ALERT,'Don\'t Ignore Warning Signs',      'Burning smells, repeated tripping, sparking sockets and flickering lights are all signs of a developing electrical fault. Ignoring them puts your household at serious risk. Call us and we will diagnose and make safe without delay.'),
        (I_TOOL, 'Qualified Fault Diagnosis',        'Emergency electrical work requires skilled fault finding, not guesswork. Our electricians carry the diagnostic equipment and experience to identify the root cause of any electrical fault quickly and safely — first time.'),
        (I_CHECK,'Safe Rectification, Not a Quick Fix', "We don't just reset the breaker and leave. We identify why the fault occurred, carry out the necessary repairs to make the circuit fully safe, and advise you on any further work required to prevent a recurrence."),
    ),
    'hiw_service': 'Emergency Electrical',
    'related_intro': 'Other residential electrical services that may be needed after an emergency callout.',
    'related_keys': ['house-rewiring', 'fuse-board-upgrades', 'electrical-safety-inspections'],
    'quote_h2': 'Call Us for Emergency Electrical Help',
    'quote_body': "Fill in the form for non-urgent electrical issues and we'll get back to you promptly. For immediate emergencies please call us directly on 085\u00a0216\u00a08789.",
    'form_aria': 'Emergency electrical repair quote request form',
},

]

# ── Generate ─────────────────────────────────────────────────────────────────
print(f'Generating {len(PAGES)} residential sub-service pages...')
for page in PAGES:
    try:
        generate(page)
    except Exception as e:
        print(f'  ERROR on {page["filename"]}: {e}')

print('Done.')
