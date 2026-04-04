#!/usr/bin/env python3
"""Generate all 10 commercial sub-service pages from house-rewiring.html template."""

BASE = 'C:/Users/niall/Desktop/csae-website'

with open(f'{BASE}/house-rewiring.html', 'r', encoding='utf-8') as f:
    TMPL = f.read()

# ── SVG icons ────────────────────────────────────────────────────────────────
I_SHIELD = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>'
I_DOC    = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M14 2H6a2 2 0 00-2 2v16a2 2 0 002 2h12a2 2 0 002-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg>'
I_ZAP    = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>'
I_CLOCK  = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><circle cx="12" cy="12" r="9" stroke="currentColor" stroke-width="2"/><polyline points="12,7 12,12 15,15" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'
I_CHECK  = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M9 12l2 2 4-4"/><circle cx="12" cy="12" r="10" fill="none" stroke="currentColor" stroke-width="2"/></svg>'
I_TOOL   = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M14.7 6.3a1 1 0 000 1.4l1.6 1.6a1 1 0 001.4 0l3.77-3.77a6 6 0 01-7.94 7.94l-6.91 6.91a2.12 2.12 0 01-3-3l6.91-6.91a6 6 0 017.94-7.94l-3.76 3.76z"/></svg>'
I_ALERT  = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M10.29 3.86L1.82 18a2 2 0 001.71 3h16.94a2 2 0 001.71-3L13.71 3.86a2 2 0 00-3.42 0z"/><line x1="12" y1="9" x2="12" y2="13"/><line x1="12" y1="17" x2="12.01" y2="17"/></svg>'
I_LAYERS = '<svg viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>'
I_CHART  = '<svg viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><line x1="18" y1="20" x2="18" y2="10" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="12" y1="20" x2="12" y2="4" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><line x1="6" y1="20" x2="6" y2="14" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg>'

# ── Related card lookup ──────────────────────────────────────────────────────
RC = {
    'commercial-electrical-installation': ('assets/csae-com-installation.jpg.png', 'Commercial electrical installation in Cork', 'Commercial Electrical Installation', 'Full electrical design and installation for offices, retail units and commercial premises across Cork.', 'commercial-electrical-installation.html'),
    'office-retail-fitouts': ('assets/csae-com-office-fitout.jpg.png', 'Office and retail electrical fit-out in Cork', 'Office &amp; Retail Fit-Outs', 'Complete electrical fit-outs for offices and retail spaces — lighting, power, data and consumer units.', 'office-retail-fitouts.html'),
    'emergency-lighting': ('assets/csae-com-emergency-lighting.jpg.png', 'Emergency lighting installation in Cork', 'Emergency Lighting', 'Supply, installation and testing of emergency lighting systems compliant with Irish Fire Services regulations.', 'emergency-lighting.html'),
    'electrical-maintenance-contracts': ('assets/csae-com-maintenance.jpg.png', 'Commercial electrical maintenance in Cork', 'Electrical Maintenance Contracts', 'Tailored planned preventative maintenance contracts with priority emergency callout for Cork businesses.', 'electrical-maintenance-contracts.html'),
    'commercial-fuse-board-upgrades': ('assets/csae-com-fuse-board.jpg.png', 'Commercial fuse board upgrade in Cork', 'Commercial Fuse Board Upgrades', 'Distribution board upgrades and fault diagnostics for commercial premises across Cork City and County.', 'commercial-fuse-board-upgrades.html'),
    'led-lighting-upgrades': ('assets/csae-com-led-upgrades.jpg.png', 'LED lighting upgrade in Cork', 'LED Lighting Upgrades', 'Full LED lighting upgrades for commercial premises — reduce energy costs and improve workplace lighting.', 'led-lighting-upgrades.html'),
    'data-network-cabling': ('assets/csae-com-data-cabling.jpg.png', 'Data and network cabling in Cork', 'Data &amp; Network Cabling', 'Structured data and network cabling for offices and commercial premises across Cork City and County.', 'data-network-cabling.html'),
    'periodic-electrical-inspections': ('assets/csae-com-periodic-inspection.jpg.png', 'Commercial periodic electrical inspection in Cork', 'Periodic Electrical Inspections', 'Full commercial periodic inspection and testing with compliance certification across Cork.', 'periodic-electrical-inspections.html'),
    'energy-efficiency-auditing': ('assets/csae-com-energy-audit.jpg.png', 'Energy efficiency audit in Cork', 'Energy Efficiency Auditing', 'Electrical energy audits identifying cost-saving opportunities for commercial premises across Cork.', 'energy-efficiency-auditing.html'),
    'factory-plant-wiring': ('assets/csae-com-factory-wiring.jpg.png', 'Factory and plant wiring in Cork', 'Factory &amp; Plant Wiring', 'Heavy-duty industrial and factory wiring, including three-phase power, for facilities across Cork.', 'factory-plant-wiring.html'),
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
    p_html  = ''.join(f'\n                        <p class="csae-sub-intro__body">{p}</p>' for p in paras)
    li_html = ''.join(f'\n                            <li class="csae-sub-intro__check">{c}</li>' for c in checks)
    return (
        f'                        <span class="csae-sub-intro__label">{label}</span>\n'
        f'                        <h2 class="csae-sub-intro__title" id="intro-heading">{h2}</h2>'
        + p_html +
        f'\n                        <ul class="csae-sub-intro__checks" aria-label="Service highlights">'
        + li_html +
        f'\n                        </ul>'
    )

def replace_block(html, start, end, replacement):
    parts = html.split(start, 1)
    after = parts[1].split(end, 1)
    return parts[0] + replacement + end + after[1]

def generate(page):
    html = TMPL

    # ── Swap active nav: Residential → Commercial ────────────────────────────
    html = html.replace(
        '<a href="residential.html" class="csae-header__nav-link csae-active" aria-haspopup="true">Residential</a>',
        '<a href="residential.html" class="csae-header__nav-link" aria-haspopup="true">Residential</a>'
    )
    html = html.replace(
        '<a href="commercial.html" class="csae-header__nav-link" aria-haspopup="true">Commercial</a>',
        '<a href="commercial.html" class="csae-header__nav-link csae-active" aria-haspopup="true">Commercial</a>'
    )

    # ── Swap drawer active: Residential → Commercial ─────────────────────────
    html = html.replace(
        '<button class="csae-drawer__accordion" aria-expanded="false" aria-controls="csae-acc-residential" style="color:#6DC535;">',
        '<button class="csae-drawer__accordion" aria-expanded="false" aria-controls="csae-acc-residential">'
    )
    html = html.replace(
        '<button class="csae-drawer__accordion" aria-expanded="false" aria-controls="csae-acc-commercial">',
        '<button class="csae-drawer__accordion" aria-expanded="false" aria-controls="csae-acc-commercial" style="color:#6DC535;">'
    )

    # ── Hero background image: residential → commercial ──────────────────────
    html = html.replace(
        "url('assets/csae-res-feature.jpg.png')",
        "url('assets/csae-com-feature.jpg.png')"
    )

    # ── SEO ──────────────────────────────────────────────────────────────────
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

    # ── Schema ───────────────────────────────────────────────────────────────
    html = html.replace('"serviceType": "House Rewiring",',
                        f'"serviceType": "{page["schema_type"]}",')
    html = html.replace('"name": "House Rewiring Cork",',
                        f'"name": "{page["schema_name"]}",')
    html = html.replace(
        '"description": "Professional full and partial house rewiring across Cork City and County Cork. All work carried out to ETCI wiring regulations by RECI registered, Safe Electric approved electricians.",',
        f'"description": "{page["schema_desc"]}",'
    )

    # ── Hero content ─────────────────────────────────────────────────────────
    html = html.replace('aria-label="House rewiring hero"',
                        f'aria-label="{page["hero_aria"]}"')
    html = html.replace('<a href="residential.html">Residential</a>',
                        '<a href="commercial.html">Commercial</a>')
    html = html.replace('<strong aria-current="page">House Rewiring</strong>',
                        f'<strong aria-current="page">{page["breadcrumb"]}</strong>')
    html = html.replace('<h1>House Rewiring <span>Cork</span></h1>',
                        f'<h1>{page["h1"]}</h1>')
    html = html.replace(
        '<p class="csae-hero__sub">Professional full and partial house rewiring across Cork City and County. ETCI certified, RECI registered electricians.</p>',
        f'<p class="csae-hero__sub">{page["hero_sub"]}</p>'
    )

    # ── Intro image ──────────────────────────────────────────────────────────
    html = html.replace(
        'src="assets/csae-res-house-rewiring.jpg.png" alt="Electrician carrying out house rewiring in Cork" class="csae-sub-intro__img"',
        f'src="{page["intro_img"]}" alt="{page["intro_img_alt"]}" class="csae-sub-intro__img"'
    )

    # ── Intro text block ─────────────────────────────────────────────────────
    intro_start = '                        <span class="csae-sub-intro__label">Residential Rewiring</span>'
    intro_end   = '                        </ul>'
    new_intro   = intro_content(page["intro_label"], page["intro_h2"],
                                page["paras"], page["checks"])
    html = replace_block(html, intro_start, intro_end, new_intro)

    # ── Reasons section ──────────────────────────────────────────────────────
    html = replace_block(
        html,
        '        <!-- ===== 3. WHY REWIRE STRIP ===== -->',
        '        <!-- ===== 4. HOW IT WORKS ===== -->',
        reasons_block(*page["reasons"])
    )

    # ── How It Works heading ─────────────────────────────────────────────────
    html = html.replace(
        '<h2 class="csae-section-title" id="hiw-heading">How Our Rewiring Service Works</h2>',
        f'<h2 class="csae-section-title" id="hiw-heading">How Our {page["hiw_service"]} Service Works</h2>'
    )

    # ── Related services ─────────────────────────────────────────────────────
    html = replace_block(
        html,
        '        <!-- ===== 6. RELATED SERVICES ===== -->',
        '        <!-- ===== 7. LEAD GEN FORM ===== -->',
        related_block(page["related_intro"], *page["related_keys"])
    )

    # ── Quote section ────────────────────────────────────────────────────────
    html = html.replace('Get a Free Rewiring Quote Today', page["quote_h2"])
    html = html.replace(
        "Fill in the form and we'll be in touch to arrange a convenient time to assess your home and provide a clear, written quote \u2014 no call-out fee, no obligation.",
        page["quote_body"]
    )
    html = html.replace('aria-label="House rewiring quote request form"',
                        f'aria-label="{page["form_aria"]}"')

    with open(f'{BASE}/{page["filename"]}', 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  Written: {page["filename"]}')


# ════════════════════════════════════════════════════════════════════════════
#  PAGE DATA
# ════════════════════════════════════════════════════════════════════════════
PAGES = [

# ── 1. Commercial Electrical Installation ────────────────────────────────────
{
    'filename': 'commercial-electrical-installation.html',
    'title': 'Commercial Electrical Installation Cork',
    'meta_desc': 'Full commercial electrical installations for offices, retail units and business premises across Cork City and County Cork. RECI registered, Safe Electric approved. Free quotes. Call 085 216 8789.',
    'og_desc': 'Commercial electrical installations in Cork for offices, retail units and business premises. RECI registered electricians. Free no-obligation quotes.',
    'schema_type': 'Commercial Electrical Installations',
    'schema_name': 'Commercial Electrical Installations Cork',
    'schema_desc': 'Full commercial electrical design and installation for offices, retail units and business premises across Cork City and County Cork, by RECI registered, Safe Electric approved electricians.',
    'hero_aria': 'Commercial electrical installation hero',
    'breadcrumb': 'Commercial Electrical Installation',
    'h1': 'Commercial Electrical <span>Installation Cork</span>',
    'hero_sub': 'Full electrical design and installation for offices, retail units and commercial premises across Cork City and County Cork.',
    'intro_img': 'assets/csae-com-installation.jpg.png',
    'intro_img_alt': 'Commercial electrical installation in a Cork business premises',
    'intro_label': 'Commercial Wiring',
    'intro_h2': 'Commercial Electrical Installations in Cork',
    'paras': [
        'Cork Solar &amp; Electrical deliver full commercial electrical installations for offices, retail units, warehouses and business premises across Cork City and County Cork. From initial design through to installation, testing and certification, we manage the complete electrical scope of your commercial project to current Irish wiring regulations and building standards.',
        'Our team of six qualified electricians work closely with main contractors, project managers and business owners to deliver each installation on programme and to specification. We co-ordinate directly with other trades and provide all required compliance documentation, including an Electrical Installation Completion Certificate, on handover.',
        'Whether you are fitting out a new commercial unit, expanding an existing premises or upgrading an older building\'s electrical infrastructure, we provide competitive fixed-price quotations and reliable project delivery. Contact us today for a free, no-obligation quote.',
    ],
    'checks': [
        'Full electrical design and installation service',
        'Compliant with current Irish wiring regulations',
        'RECI registered and Safe Electric approved electricians',
        'Full Electrical Installation Completion Certificate on handover',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Why It Matters', 'What Sets a Commercial Electrical Installation Apart',
        'Commercial electrical work demands higher capacity, stricter compliance and tighter programme management than residential. Here is what to look for in a contractor.',
        (I_DOC,    'Full Compliance Documentation',  'Commercial installations require Electrical Installation Completion Certificates, test results and compliance documentation for building control, insurers and landlords. We provide a complete documentation package on every job.'),
        (I_SHIELD, 'RECI Registered Contractors',    'Only RECI registered and Safe Electric approved electricians are authorised to certify commercial electrical installations in Ireland. Our team is fully registered and carries out all work to current ETCI standards.'),
        (I_LAYERS, 'Project-Managed Delivery',       'Commercial projects require co-ordination with other trades, strict programme management and clear communication. We work directly with your main contractor or project manager to keep the electrical scope on schedule and within budget.'),
    ),
    'hiw_service': 'Commercial Electrical Installation',
    'related_intro': 'Other commercial electrical services from Cork Solar &amp; Electrical.',
    'related_keys': ['office-retail-fitouts', 'electrical-maintenance-contracts', 'periodic-electrical-inspections'],
    'quote_h2': 'Get a Free Commercial Installation Quote Today',
    'quote_body': "Fill in the form and we'll be in touch to discuss your project requirements and arrange a free site visit \u2014 no call-out fee, no obligation.",
    'form_aria': 'Commercial electrical installation quote request form',
},

# ── 2. Office & Retail Fit-Outs ──────────────────────────────────────────────
{
    'filename': 'office-retail-fitouts.html',
    'title': 'Office &amp; Retail Electrical Fit-Outs Cork',
    'meta_desc': 'Complete electrical fit-outs for offices and retail spaces across Cork City and County Cork. Lighting, power, data points and consumer units. RECI registered. Free quotes. Call 085 216 8789.',
    'og_desc': 'Office and retail electrical fit-outs in Cork. Lighting, power, data and consumer units by RECI registered electricians. Free no-obligation quotes.',
    'schema_type': 'Office and Retail Electrical Fit-Outs',
    'schema_name': 'Office and Retail Electrical Fit-Outs Cork',
    'schema_desc': 'Complete electrical fit-outs for offices and retail spaces across Cork City and County Cork, including lighting, power, data points and consumer units, by RECI registered electricians.',
    'hero_aria': 'Office and retail fit-out hero',
    'breadcrumb': 'Office &amp; Retail Fit-Outs',
    'h1': 'Office &amp; Retail Electrical <span>Fit-Outs Cork</span>',
    'hero_sub': 'Complete electrical fit-outs for offices and retail spaces — lighting, power, data points and consumer units across Cork City and County Cork.',
    'intro_img': 'assets/csae-com-office-fitout.jpg.png',
    'intro_img_alt': 'Electrical fit-out in a Cork office or retail unit',
    'intro_label': 'Commercial Fit-Outs',
    'intro_h2': 'Office &amp; Retail Electrical Fit-Outs in Cork',
    'paras': [
        'Cork Solar &amp; Electrical carry out complete electrical fit-outs for offices, retail units, showrooms and commercial premises across Cork City and County Cork. We manage the full electrical scope of your fit-out — from lighting design and installation to power distribution, data cabling, consumer units and emergency lighting — delivering a compliant, finished result ready for occupation.',
        'We work closely with fit-out contractors, shopfitters and interior designers across Cork, co-ordinating our works within the broader programme and delivering to agreed milestones. Our electricians work efficiently to minimise disruption and keep the project on schedule — whether it is a single retail unit or a multi-floor office.',
        'All fit-out electrical work is carried out to current ETCI wiring regulations, with a full Electrical Installation Completion Certificate provided on handover. Contact us for a free, no-obligation quote on your fit-out project.',
    ],
    'checks': [
        'Full electrical fit-out service from first fix to final fix',
        'Lighting, power distribution and data point installation',
        'Consumer unit and distribution board supply and installation',
        'Compliant with all current Irish wiring regulations',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Why It Matters', 'What Makes a Successful Office or Retail Fit-Out',
        'A well-executed electrical fit-out underpins every other aspect of your workspace. Here is what to expect from a specialist commercial electrician.',
        (I_LAYERS, 'Single-Contractor Convenience', 'By using one electrical contractor for your entire fit-out — lighting, power, data and emergency — you avoid interface issues between trades and have a single point of contact for all electrical queries and sign-off documentation.'),
        (I_ZAP,    'Energy-Efficient by Design',    'We specify LED lighting, daylight sensors and energy-efficient distribution from the outset. A well-designed commercial lighting scheme reduces your operational energy costs from day one and improves the working environment for staff and customers.'),
        (I_DOC,    'Handover-Ready Documentation',  'We provide a complete documentation pack on handover, including test certificates, as-installed drawings and compliance records — everything your landlord, insurer and building control authority will require on occupation.'),
    ),
    'hiw_service': 'Office &amp; Retail Fit-Out',
    'related_intro': 'Other commercial electrical services that complement an office or retail fit-out.',
    'related_keys': ['commercial-electrical-installation', 'data-network-cabling', 'led-lighting-upgrades'],
    'quote_h2': 'Get a Free Fit-Out Electrical Quote Today',
    'quote_body': "Fill in the form and we'll be in touch to discuss your fit-out requirements and arrange a free site visit \u2014 no call-out fee, no obligation.",
    'form_aria': 'Office and retail fit-out quote request form',
},

# ── 3. Emergency Lighting ─────────────────────────────────────────────────────
{
    'filename': 'emergency-lighting.html',
    'title': 'Emergency Lighting Installation Cork',
    'meta_desc': 'Supply, installation and testing of emergency lighting systems for commercial premises across Cork City and County Cork. Compliant with Irish Fire Services regulations. Free quotes. Call 085 216 8789.',
    'og_desc': 'Emergency lighting installation in Cork. Compliant systems for commercial premises. Scheduled testing and certification. RECI registered electricians. Free no-obligation quotes.',
    'schema_type': 'Emergency Lighting Installation',
    'schema_name': 'Emergency Lighting Installation Cork',
    'schema_desc': 'Supply, installation and testing of emergency lighting systems for commercial premises across Cork City and County Cork, fully compliant with Irish Fire Services and Building Regulations.',
    'hero_aria': 'Emergency lighting installation hero',
    'breadcrumb': 'Emergency Lighting',
    'h1': 'Emergency Lighting <span>Installation Cork</span>',
    'hero_sub': 'Supply, installation and testing of emergency lighting systems for commercial premises across Cork City and County Cork.',
    'intro_img': 'assets/csae-com-emergency-lighting.jpg.png',
    'intro_img_alt': 'Emergency lighting installation in a Cork commercial premises',
    'intro_label': 'Life Safety Systems',
    'intro_h2': 'Emergency Lighting Installation in Cork',
    'paras': [
        'Cork Solar &amp; Electrical supply, install and test emergency lighting systems for commercial premises across Cork City and County Cork. Emergency and exit lighting is a legal requirement under the Irish Fire Services Act and Building Regulations for all commercial buildings — workplaces, retail units, hospitality premises, schools and healthcare facilities.',
        'We design and install systems to IS 3217 and EN 1838 standards, covering maintained and non-maintained emergency luminaires, exit signs and central battery systems. All installations are fully tested and commissioned, with a detailed test log and compliance certificate issued at handover.',
        'We also offer scheduled six-monthly and annual testing and certification services, ensuring your emergency lighting remains compliant and your business avoids enforcement action from the Fire Authority. Contact us today for a free assessment and quote.',
    ],
    'checks': [
        'Emergency and exit lighting supply and installation',
        'Design to IS 3217 and EN 1838 standards',
        'Full commissioning, testing and compliance certification',
        'Scheduled six-monthly and annual testing contracts available',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Why It Matters', 'Why Compliant Emergency Lighting Is Non-Negotiable',
        'Inadequate or non-compliant emergency lighting is one of the most common reasons commercial premises fail a Fire Authority inspection.',
        (I_ALERT,  'Legal Requirement for All Commercial Premises', 'Under the Irish Fire Services Act and Building Regulations, all commercial buildings must have compliant emergency and exit lighting. Failure to comply can result in prohibition notices and enforcement action from Cork Fire Services.'),
        (I_DOC,    'Regular Testing Is Mandatory',                  'Emergency lighting must be tested monthly (function test), six-monthly (duration test) and annually (full discharge test). We provide scheduled testing contracts and maintain your test log, so your compliance records are always up to date.'),
        (I_SHIELD, 'Protects Occupants in an Emergency',           'In a fire or power failure, occupants need clear, reliable guidance to exit the building safely. A properly designed and maintained emergency lighting system is the single most important life safety measure in your premises.'),
    ),
    'hiw_service': 'Emergency Lighting',
    'related_intro': 'Other commercial electrical services from Cork Solar &amp; Electrical.',
    'related_keys': ['commercial-electrical-installation', 'electrical-maintenance-contracts', 'periodic-electrical-inspections'],
    'quote_h2': 'Get a Free Emergency Lighting Quote Today',
    'quote_body': "Fill in the form and we'll be in touch to discuss your emergency lighting requirements and arrange a free site visit \u2014 no call-out fee, no obligation.",
    'form_aria': 'Emergency lighting quote request form',
},

# ── 4. Electrical Maintenance Contracts ──────────────────────────────────────
{
    'filename': 'electrical-maintenance-contracts.html',
    'title': 'Electrical Maintenance Contracts Cork',
    'meta_desc': 'Tailored electrical maintenance contracts for businesses and commercial properties across Cork City and County Cork. Planned preventative maintenance, priority callout and compliance reporting. Free quotes. Call 085 216 8789.',
    'og_desc': 'Commercial electrical maintenance contracts in Cork. Planned preventative maintenance, priority callout and full compliance reporting for Cork businesses.',
    'schema_type': 'Electrical Maintenance Contracts',
    'schema_name': 'Electrical Maintenance Contracts Cork',
    'schema_desc': 'Tailored electrical maintenance contracts for businesses across Cork City and County Cork, including planned preventative maintenance, priority emergency callout and full compliance reporting.',
    'hero_aria': 'Electrical maintenance contracts hero',
    'breadcrumb': 'Electrical Maintenance Contracts',
    'h1': 'Electrical Maintenance <span>Contracts Cork</span>',
    'hero_sub': 'Tailored planned preventative maintenance contracts for businesses and commercial properties across Cork City and County Cork.',
    'intro_img': 'assets/csae-com-maintenance.jpg.png',
    'intro_img_alt': 'Commercial electrical maintenance in Cork',
    'intro_label': 'Planned Maintenance',
    'intro_h2': 'Electrical Maintenance Contracts in Cork',
    'paras': [
        'Cork Solar &amp; Electrical offer tailored electrical maintenance contracts for businesses, landlords and commercial property owners across Cork City and County Cork. A maintenance contract ensures your electrical systems are regularly inspected, faults are identified before they cause disruption, and your premises remain compliant with all relevant regulations.',
        'Our contracts are flexible and built around your specific requirements — from light-touch quarterly visits for small commercial premises to comprehensive planned preventative maintenance programmes for larger facilities. All contract clients benefit from priority response for emergency callouts, with our team available to attend urgent faults at short notice.',
        'We provide full compliance reporting after each visit, giving you a clear record of all work carried out, any defects identified and their recommended remediation. Contact us today to discuss a contract that suits your business.',
    ],
    'checks': [
        'Tailored planned preventative maintenance programmes',
        'Priority emergency callout for contract clients',
        'Full compliance reporting after every visit',
        'Suitable for all sizes of commercial premises',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Why It Matters', 'Why a Maintenance Contract Makes Business Sense',
        'Reactive maintenance is always more expensive and disruptive than planned prevention. Here is what a maintenance contract delivers for your business.',
        (I_CLOCK,  'Prevent Costly Breakdowns',      'Regular electrical maintenance identifies deteriorating components, loose connections and developing faults before they cause a breakdown. Planned prevention is significantly cheaper than emergency repairs and avoids the loss of trading time that comes with unexpected failures.'),
        (I_DOC,    'Maintain Compliance Records',     'A maintenance contract provides an auditable compliance record — essential for insurance purposes, landlord obligations and any future inspection by the HSA, Fire Authority or building certifier. We provide full written reports after every visit.'),
        (I_SHIELD, 'Priority Callout When You Need It', 'Contract clients go to the front of our callout queue. If an electrical fault threatens your operations, our team will respond at the earliest opportunity — minimising downtime and protecting your revenue.'),
    ),
    'hiw_service': 'Electrical Maintenance',
    'related_intro': 'Other commercial electrical services that complement a maintenance contract.',
    'related_keys': ['periodic-electrical-inspections', 'commercial-fuse-board-upgrades', 'emergency-lighting'],
    'quote_h2': 'Get a Free Maintenance Contract Quote Today',
    'quote_body': "Fill in the form and we'll be in touch to discuss your maintenance requirements and put together a contract tailored to your premises \u2014 no obligation.",
    'form_aria': 'Electrical maintenance contract quote request form',
},

# ── 5. Commercial Fuse Board Upgrades ────────────────────────────────────────
{
    'filename': 'commercial-fuse-board-upgrades.html',
    'title': 'Commercial Fuse Board Upgrades Cork',
    'meta_desc': 'Commercial distribution board upgrades and fault finding for businesses across Cork City and County Cork. Minimise downtime, ensure compliance. RECI registered. Free quotes. Call 085 216 8789.',
    'og_desc': 'Commercial fuse board and distribution board upgrades in Cork. Fault diagnostics and minimal business disruption. RECI registered electricians. Free no-obligation quotes.',
    'schema_type': 'Commercial Fuse Board Upgrades',
    'schema_name': 'Commercial Fuse Board Upgrades Cork',
    'schema_desc': 'Commercial distribution board upgrades and fault diagnostics for businesses across Cork City and County Cork, carried out by RECI registered, Safe Electric approved electricians with minimal disruption.',
    'hero_aria': 'Commercial fuse board upgrade hero',
    'breadcrumb': 'Commercial Fuse Board Upgrades',
    'h1': 'Commercial Fuse Board <span>Upgrades Cork</span>',
    'hero_sub': 'Distribution board upgrades and fault diagnostics for commercial premises across Cork City and County Cork — minimal downtime, full compliance.',
    'intro_img': 'assets/csae-com-fuse-board.jpg.png',
    'intro_img_alt': 'Commercial distribution board upgrade in Cork',
    'intro_label': 'Distribution Board Upgrades',
    'intro_h2': 'Commercial Fuse Board Upgrades in Cork',
    'paras': [
        'Cork Solar &amp; Electrical upgrade commercial distribution boards and fuse boards for businesses across Cork City and County Cork. An outdated or overloaded distribution board is a safety risk, a compliance issue and a common source of operational disruption — affecting lighting, equipment and essential business systems.',
        'We carry out the full upgrade process: isolating supply, removing the old board, installing a new distribution board with correct MCB and RCD protection for all circuits, testing all circuits to ETCI standards and issuing a full Electrical Installation Completion Certificate. We work outside business hours where necessary to minimise disruption to your operations.',
        'We also carry out advanced fault diagnostics for commercial premises experiencing recurring tripping, unexplained power loss, or electrical faults that have not been resolved by previous contractors. Contact us for a free assessment and written quote.',
    ],
    'checks': [
        'Commercial distribution board supply and installation',
        'MCB and RCD protection to current ETCI standards',
        'Advanced fault diagnostics for recurring electrical issues',
        'Work available outside business hours to minimise disruption',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Why It Matters', 'When to Upgrade Your Commercial Distribution Board',
        'Commercial premises place far greater electrical demand on distribution boards than homes. Here are the most common triggers for a commercial board upgrade.',
        (I_ALERT,  'Overcrowded or Overloaded Boards',  'Adding new equipment, circuits or tenants to a commercial building without upgrading the distribution board is a common cause of recurring tripping and electrical faults. An upgrade creates the capacity your business actually needs.'),
        (I_DOC,    'Compliance for Insurance &amp; Leases', 'Commercial landlords, insurers and building certifiers increasingly require evidence of compliant electrical infrastructure. A board upgrade with a Completion Certificate resolves outstanding defects and demonstrates a commitment to electrical safety.'),
        (I_CLOCK,  'Minimise Operational Downtime',     'We plan distribution board upgrades to minimise the impact on your business — agreeing programme, isolating sections progressively where possible, and carrying out work outside trading hours when required. Your operations stay running.'),
    ),
    'hiw_service': 'Commercial Board Upgrade',
    'related_intro': 'Other commercial electrical services from Cork Solar &amp; Electrical.',
    'related_keys': ['electrical-maintenance-contracts', 'periodic-electrical-inspections', 'commercial-electrical-installation'],
    'quote_h2': 'Get a Free Distribution Board Upgrade Quote',
    'quote_body': "Fill in the form and we'll be in touch to discuss your distribution board requirements and arrange a free on-site assessment \u2014 no call-out fee, no obligation.",
    'form_aria': 'Commercial fuse board upgrade quote request form',
},

# ── 6. LED Lighting Upgrades ──────────────────────────────────────────────────
{
    'filename': 'led-lighting-upgrades.html',
    'title': 'LED Lighting Upgrades Cork',
    'meta_desc': 'LED lighting upgrades for commercial premises across Cork City and County Cork. Reduce energy costs and improve workplace lighting quality. RECI registered. Free quotes. Call 085 216 8789.',
    'og_desc': 'Commercial LED lighting upgrades in Cork. Reduce energy bills and improve lighting quality for offices, warehouses and retail spaces. Free no-obligation quotes.',
    'schema_type': 'LED Lighting Upgrades',
    'schema_name': 'LED Lighting Upgrades Cork',
    'schema_desc': 'LED and energy-efficient lighting upgrades for commercial premises across Cork City and County Cork, reducing energy costs and improving workplace lighting quality, by RECI registered electricians.',
    'hero_aria': 'LED lighting upgrade hero',
    'breadcrumb': 'LED Lighting Upgrades',
    'h1': 'LED Lighting Upgrades <span>Cork</span>',
    'hero_sub': 'Energy-efficient LED lighting upgrades for commercial premises across Cork City and County Cork — lower energy bills, better light quality.',
    'intro_img': 'assets/csae-com-led-upgrades.jpg.png',
    'intro_img_alt': 'LED lighting upgrade in a Cork commercial premises',
    'intro_label': 'Energy-Efficient Lighting',
    'intro_h2': 'LED Lighting Upgrades for Commercial Premises in Cork',
    'paras': [
        'Cork Solar &amp; Electrical carry out LED lighting upgrades for commercial premises across Cork City and County Cork. Switching from fluorescent, halogen or older metal halide fittings to modern LED delivers immediate, measurable reductions in your electricity bills — typically 50\u201380% less energy for the same or better light output.',
        'We survey your existing lighting, specify appropriate LED replacements for each area and application, install all new fittings, dispose of old fittings responsibly and issue compliance certification. We supply high-quality commercial LED fittings with long warranties and excellent lumen output — not budget consumer-grade products.',
        'LED upgrades also reduce your maintenance burden significantly. Commercial LED fittings have rated lifespans of 50,000 hours or more, eliminating the time and cost of frequent lamp replacements. Contact us for a free lighting survey and quote.',
    ],
    'checks': [
        'Full LED lighting survey and specification',
        'Supply and installation of commercial-grade LED fittings',
        'Typical energy saving of 50\u201380% versus existing systems',
        'Responsible disposal of old fluorescent and halogen fittings',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Why It Matters', 'Why LED Upgrades Deliver Real Commercial Value',
        'An LED upgrade is one of the fastest-payback capital investments available to a commercial business. Here is why it makes sense.',
        (I_CHART,  'Immediate Energy Cost Savings',   'Modern LED fittings use 50\u201380% less electricity than fluorescent or halogen equivalents. For a commercial premises with lighting running eight or more hours a day, the electricity cost saving alone typically pays back the installation cost within two to three years.'),
        (I_CLOCK,  'Dramatically Reduced Maintenance', 'Commercial LED fittings have rated lifespans of 50,000 hours or more. This eliminates the frequent lamp replacement costs and disruption associated with fluorescent and metal halide systems, and frees up your maintenance budget for higher-value tasks.'),
        (I_ZAP,    'Better Light Quality for Staff',  'Modern LED lighting provides consistent, high-CRI light that reduces eye strain, improves colour rendering and creates a more comfortable working environment. Better lighting quality has a demonstrable positive effect on staff productivity and wellbeing.'),
    ),
    'hiw_service': 'LED Lighting Upgrade',
    'related_intro': 'Other commercial electrical services that complement an LED lighting upgrade.',
    'related_keys': ['office-retail-fitouts', 'energy-efficiency-auditing', 'electrical-maintenance-contracts'],
    'quote_h2': 'Get a Free LED Lighting Upgrade Quote Today',
    'quote_body': "Fill in the form and we'll arrange a free lighting survey and provide a clear, written quote with projected energy savings \u2014 no call-out fee, no obligation.",
    'form_aria': 'LED lighting upgrade quote request form',
},

# ── 7. Data & Network Cabling ─────────────────────────────────────────────────
{
    'filename': 'data-network-cabling.html',
    'title': 'Data &amp; Network Cabling Cork',
    'meta_desc': 'Structured data and network cabling for offices and commercial premises across Cork City and County Cork. Server room installations, patch panels and cable management. Free quotes. Call 085 216 8789.',
    'og_desc': 'Data and network cabling in Cork. Structured cabling, server room installations and patch panels for offices and commercial premises. Free no-obligation quotes.',
    'schema_type': 'Data and Network Cabling',
    'schema_name': 'Data and Network Cabling Cork',
    'schema_desc': 'Structured data and network cabling installations for offices and commercial premises across Cork City and County Cork, including server room installations, patch panels and cable management.',
    'hero_aria': 'Data and network cabling hero',
    'breadcrumb': 'Data &amp; Network Cabling',
    'h1': 'Data &amp; Network Cabling <span>Cork</span>',
    'hero_sub': 'Structured data and network cabling for offices and commercial premises across Cork City and County Cork — organised, reliable and future-ready.',
    'intro_img': 'assets/csae-com-data-cabling.jpg.png',
    'intro_img_alt': 'Data and network cabling installation in a Cork office',
    'intro_label': 'Structured Cabling',
    'intro_h2': 'Data &amp; Network Cabling in Cork',
    'paras': [
        'Cork Solar &amp; Electrical install structured data and network cabling for offices, commercial premises and server rooms across Cork City and County Cork. A properly designed and installed cabling infrastructure is the foundation of your business network — reliable, organised and capable of supporting your current and future requirements.',
        'We install Cat5e, Cat6 and Cat6a cabling systems, terminating to RJ45 outlets, patch panels and switches in a clean, labelled and documented installation. We also handle server room fit-outs, cabinet installation, patch panel organisation and trunking and containment throughout your premises.',
        'Whether you are fitting out a new office, adding network points to an existing building or reorganising a chaotic server room, we provide a tidy, professional result with full documentation. Contact us for a free site visit and quote.',
    ],
    'checks': [
        'Cat5e, Cat6 and Cat6a structured cabling installation',
        'RJ45 outlets, patch panels and cabinet installation',
        'Server room fit-outs and cable management',
        'Full labelling and as-installed documentation',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Why It Matters', 'Why Structured Cabling Infrastructure Matters',
        'Ad-hoc network cabling is one of the most common sources of IT unreliability in commercial buildings. Here is why a structured approach pays off.',
        (I_LAYERS, 'Organised &amp; Documented',       'A structured cabling installation is labelled, documented and logical — making it straightforward to diagnose faults, add new points or reconfigure your network without disrupting the rest of the office. Unstructured cabling quickly becomes a source of cost and frustration.'),
        (I_SHIELD, 'Reliable Performance',             'Correctly installed Cat6 or Cat6a cabling, with properly terminated connections and managed bend radii, delivers consistent gigabit performance without the packet loss and interference that poorly installed cabling introduces. Your network is only as reliable as its physical layer.'),
        (I_ZAP,    'Future-Ready Infrastructure',      'Installing a higher category cable now costs very little more than a lower category — but gives you the headroom to support faster network speeds, Power over Ethernet (PoE) devices and future technology without rewiring. Get it right once.'),
    ),
    'hiw_service': 'Data &amp; Network Cabling',
    'related_intro': 'Other commercial electrical services that complement a data cabling installation.',
    'related_keys': ['office-retail-fitouts', 'commercial-electrical-installation', 'led-lighting-upgrades'],
    'quote_h2': 'Get a Free Data Cabling Quote Today',
    'quote_body': "Fill in the form and we'll arrange a free site visit to discuss your network cabling requirements and provide a clear, written quote \u2014 no obligation.",
    'form_aria': 'Data and network cabling quote request form',
},

# ── 8. Periodic Electrical Inspections ───────────────────────────────────────
{
    'filename': 'periodic-electrical-inspections.html',
    'title': 'Periodic Electrical Inspections Cork',
    'meta_desc': 'Commercial periodic electrical inspection and testing across Cork City and County Cork. Safety compliance certification issued. RECI registered, Safe Electric approved. Free quotes. Call 085 216 8789.',
    'og_desc': 'Commercial periodic electrical inspections in Cork. Full testing and compliance certification for businesses and commercial properties. RECI registered electricians.',
    'schema_type': 'Periodic Electrical Inspections',
    'schema_name': 'Periodic Electrical Inspections Cork',
    'schema_desc': 'Commercial periodic electrical inspection and testing for properties across Cork City and County Cork, with compliance certification issued, by RECI registered, Safe Electric approved electricians.',
    'hero_aria': 'Periodic electrical inspection hero',
    'breadcrumb': 'Periodic Electrical Inspections',
    'h1': 'Periodic Electrical <span>Inspections Cork</span>',
    'hero_sub': 'Commercial periodic electrical inspection and testing with full compliance certification — for businesses and property owners across Cork City and County Cork.',
    'intro_img': 'assets/csae-com-periodic-inspection.jpg.png',
    'intro_img_alt': 'Commercial electrical inspection being carried out in Cork',
    'intro_label': 'Compliance Inspection',
    'intro_h2': 'Periodic Electrical Inspections in Cork',
    'paras': [
        'Cork Solar &amp; Electrical carry out commercial periodic electrical inspections for businesses, landlords and commercial property owners across Cork City and County Cork. A Periodic Inspection Report (PIR) provides a complete assessment of the condition and compliance of your electrical installation, identifying any defects, deterioration or non-compliance with current ETCI standards.',
        'Our RECI registered electricians carry out a full visual inspection and live circuit testing of all distribution boards, circuits, protective devices, earthing and bonding. We issue a detailed written report with all observations categorised by urgency, and provide a compliance certificate where the installation is found to be satisfactory.',
        'Commercial premises should be inspected at a maximum five-year interval, or more frequently for high-use or harsh environments. Inspections are also required on change of occupancy, following electrical incidents or at the request of insurers and lenders. Contact us today for a free quote.',
    ],
    'checks': [
        'Full periodic inspection and circuit testing',
        'Detailed written report with categorised observations',
        'Compliance certification issued for satisfactory installations',
        'RECI registered and Safe Electric approved inspectors',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Why It Matters', 'Who Needs a Commercial Periodic Electrical Inspection?',
        'Periodic inspections are required by law, by insurers and by landlords for most commercial properties. Here is what you need to know.',
        (I_DOC,    'Required by Law for Many Premises',    'The Health and Safety Authority (HSA) requires employers to maintain electrical systems in a safe condition. For many types of commercial premises, periodic inspection and testing is the primary means of demonstrating this — and of identifying faults before they cause injury or fire.'),
        (I_SHIELD, 'Essential for Insurance &amp; Leases', 'Most commercial property insurers require evidence of a current periodic inspection report. Landlords are also increasingly making PIR completion a condition of lease renewal. A current certificate removes a common compliance risk for your business.'),
        (I_CHECK,  'Identify Faults Before They Cost More', 'Periodic inspection identifies deteriorating cables, overloaded circuits, missing earth connections and non-compliant wiring before they cause breakdowns, fires or enforcement action. The cost of an inspection is a fraction of the cost of a major fault.'),
    ),
    'hiw_service': 'Electrical Inspection',
    'related_intro': 'Other commercial electrical services from Cork Solar &amp; Electrical.',
    'related_keys': ['electrical-maintenance-contracts', 'commercial-fuse-board-upgrades', 'emergency-lighting'],
    'quote_h2': 'Book a Commercial Electrical Inspection Today',
    'quote_body': "Fill in the form and we'll get back to you to arrange a convenient time to carry out your inspection and issue a full written report \u2014 no call-out fee, no obligation.",
    'form_aria': 'Periodic electrical inspection quote request form',
},

# ── 9. Energy Efficiency Auditing ────────────────────────────────────────────
{
    'filename': 'energy-efficiency-auditing.html',
    'title': 'Energy Efficiency Auditing Cork',
    'meta_desc': 'Electrical energy efficiency audits for commercial premises across Cork City and County Cork. Identify energy-saving opportunities and reduce operational costs. Free quotes. Call 085 216 8789.',
    'og_desc': 'Commercial energy efficiency auditing in Cork. Identify electricity cost savings and practical improvements for your business premises. Free no-obligation quotes.',
    'schema_type': 'Energy Efficiency Auditing',
    'schema_name': 'Energy Efficiency Auditing Cork',
    'schema_desc': 'Electrical energy efficiency audits for commercial premises across Cork City and County Cork, identifying energy-saving opportunities and reducing operational electricity costs.',
    'hero_aria': 'Energy efficiency auditing hero',
    'breadcrumb': 'Energy Efficiency Auditing',
    'h1': 'Energy Efficiency <span>Auditing Cork</span>',
    'hero_sub': 'Electrical energy efficiency audits for commercial premises across Cork City and County Cork — identify saving opportunities and reduce your electricity costs.',
    'intro_img': 'assets/csae-com-energy-audit.jpg.png',
    'intro_img_alt': 'Energy efficiency audit being carried out at a Cork business',
    'intro_label': 'Energy Assessment',
    'intro_h2': 'Energy Efficiency Auditing in Cork',
    'paras': [
        'Cork Solar &amp; Electrical carry out electrical energy efficiency audits for commercial premises across Cork City and County Cork. With electricity costs continuing to rise, a structured energy audit identifies where your business is consuming more electricity than necessary and provides a clear, prioritised plan for reducing your energy bills.',
        'Our audits cover lighting systems, distribution and power factor correction, motor and HVAC loads, standby consumption and metering. We assess your current usage against best-practice benchmarks and provide practical, costed recommendations — from LED lighting upgrades and power factor correction to sub-metering and load scheduling.',
        'We work with businesses of all sizes, from single commercial units to multi-site operations. Our recommendations are practical, deliverable and focused on the fastest return on investment. Contact us to arrange a free initial conversation about your energy costs.',
    ],
    'checks': [
        'Full electrical energy usage assessment',
        'Lighting, power, HVAC and standby load review',
        'Prioritised, costed improvement recommendations',
        'LED, power factor and sub-metering options covered',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Why It Matters', 'What an Energy Efficiency Audit Delivers for Your Business',
        'Many businesses are spending significantly more on electricity than they need to. An audit identifies exactly where — and by how much.',
        (I_CHART,  'Identify Your Biggest Savings',    'An energy audit goes beyond looking at your electricity bill. We measure actual loads, identify inefficient equipment and poor usage patterns, and show you exactly where your money is going — so you can target the improvements that will make the biggest difference to your costs.'),
        (I_ZAP,    'Practical, Costed Recommendations', 'We do not produce theoretical reports. Every recommendation is practical, costed and includes an estimated payback period. You can prioritise the improvements that deliver the fastest return and implement them at a pace that suits your budget and operations.'),
        (I_DOC,    'Support for SEAI Grants',          'Some energy efficiency improvements are eligible for SEAI business energy grants. As SEAI approved contractors, we can advise on which measures qualify, assist with grant applications and carry out the required works to grant specification.'),
    ),
    'hiw_service': 'Energy Efficiency Audit',
    'related_intro': 'Other commercial electrical services that follow naturally from an energy audit.',
    'related_keys': ['led-lighting-upgrades', 'commercial-fuse-board-upgrades', 'electrical-maintenance-contracts'],
    'quote_h2': 'Get a Free Energy Efficiency Audit Quote Today',
    'quote_body': "Fill in the form and we'll be in touch to discuss your energy audit requirements and how we can help reduce your electricity costs \u2014 no call-out fee, no obligation.",
    'form_aria': 'Energy efficiency audit quote request form',
},

# ── 10. Factory & Plant Wiring ────────────────────────────────────────────────
{
    'filename': 'factory-plant-wiring.html',
    'title': 'Factory &amp; Plant Wiring Cork',
    'meta_desc': 'Heavy-duty electrical wiring for factories, warehouses and industrial facilities across Cork City and County Cork. Three-phase power, machinery connections and system expansions. Free quotes. Call 085 216 8789.',
    'og_desc': 'Factory and industrial plant wiring in Cork. Three-phase power, machinery connections and system expansions for industrial facilities. RECI registered electricians. Free no-obligation quotes.',
    'schema_type': 'Factory and Plant Wiring',
    'schema_name': 'Factory and Plant Wiring Cork',
    'schema_desc': 'Heavy-duty electrical wiring for factories, warehouses and industrial facilities across Cork City and County Cork, including three-phase power and machinery connections, by RECI registered electricians.',
    'hero_aria': 'Factory and plant wiring hero',
    'breadcrumb': 'Factory &amp; Plant Wiring',
    'h1': 'Factory &amp; Plant Wiring <span>Cork</span>',
    'hero_sub': 'Heavy-duty industrial electrical wiring for factories, warehouses and plant facilities across Cork City and County Cork.',
    'intro_img': 'assets/csae-com-factory-wiring.jpg.png',
    'intro_img_alt': 'Industrial electrical wiring in a Cork factory or plant',
    'intro_label': 'Industrial Wiring',
    'intro_h2': 'Factory &amp; Plant Wiring in Cork',
    'paras': [
        'Cork Solar &amp; Electrical carry out heavy-duty electrical wiring for factories, warehouses, production facilities and industrial plants across Cork City and County Cork. From new installations and three-phase power supply to machinery connections, system expansions and motor control panel wiring, our qualified electricians have the experience and equipment to handle demanding industrial electrical projects.',
        'Industrial electrical work requires an understanding of the specific demands of production environments — high-current circuits, motor starting and protection, three-phase distribution, power factor, isolation requirements and compliance with both ETCI wiring regulations and relevant machinery safety standards.',
        'We work directly with factory owners, operations managers and main contractors to plan and deliver electrical works that minimise disruption to production schedules. All work is fully tested, certified and documented. Contact us for a free site visit and quotation.',
    ],
    'checks': [
        'Industrial and factory electrical installation and expansion',
        'Three-phase power supply and distribution',
        'Machinery connections and motor control wiring',
        'Compliant with ETCI regulations and safety standards',
        'Covering Cork City and all of County Cork',
    ],
    'reasons': (
        'Why It Matters', 'Why Industrial Electrical Work Demands Specialist Experience',
        'Factory and plant environments place demands on electrical systems that go well beyond standard commercial work. Here is what experience delivers.',
        (I_ZAP,    'Three-Phase Experience',              'Industrial machinery typically requires three-phase power, high-current circuits and specific motor protection devices. Getting these wrong causes equipment damage, production loss and safety incidents. Our electricians are experienced in three-phase industrial environments.'),
        (I_SHIELD, 'Production-Aware Working',            'We understand that electrical works in a live factory must be planned carefully to avoid unplanned production downtime. We agree an isolation and programme plan with your team before any work begins, and carry out planned outages at times that minimise impact on output.'),
        (I_DOC,    'Full Compliance Documentation',       'Industrial electrical installations must be fully tested, certified and documented — for insurance purposes, HSA compliance and machinery CE marking requirements. We provide complete documentation, including test certificates and as-installed drawings, on every project.'),
    ),
    'hiw_service': 'Factory &amp; Plant Wiring',
    'related_intro': 'Other commercial electrical services from Cork Solar &amp; Electrical.',
    'related_keys': ['commercial-electrical-installation', 'electrical-maintenance-contracts', 'periodic-electrical-inspections'],
    'quote_h2': 'Get a Free Factory Wiring Quote Today',
    'quote_body': "Fill in the form and we'll arrange a free site visit to discuss your industrial electrical requirements and provide a clear, written quotation \u2014 no call-out fee, no obligation.",
    'form_aria': 'Factory and plant wiring quote request form',
},

]

# ── Generate ──────────────────────────────────────────────────────────────────
print(f'Generating {len(PAGES)} commercial sub-service pages...')
for page in PAGES:
    try:
        generate(page)
    except Exception as e:
        print(f'  ERROR on {page["filename"]}: {e}')
print('Done.')
