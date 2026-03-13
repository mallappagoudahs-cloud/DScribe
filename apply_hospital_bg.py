"""
UI update: apply hospital images to the background of the page.
- body: hospital_hero.png as a fixed full-page background (behind the dark overlay)
- hero section img: swap to hospital_hero.png, increase opacity slightly
- pills_card.png: used as subtle background on the results card section
- hospital_side.png: added as a right-side decorative panel in the hero
"""

with open("static/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# ── 1. Body: add hospital image as full-page fixed background ────────
old_body = """\
    body {

      font-family: 'Inter', sans-serif;

      margin: 0;

      padding: 0;

      background: var(--bg-gradient);

      color: var(--text-main);

      min-height: 100vh;

      backdrop-filter: blur(20px);

    }"""

new_body = """\
    body {

      font-family: 'Inter', sans-serif;

      margin: 0;

      padding: 0;

      background: var(--bg-gradient);

      color: var(--text-main);

      min-height: 100vh;

    }

    /* Full-page hospital background image */
    body::before {
      content: '';
      position: fixed;
      inset: 0;
      background: url('/static/hospital_hero.png') center/cover no-repeat;
      opacity: 0.10;
      z-index: -1;
      pointer-events: none;
    }"""

if old_body in html:
    html = html.replace(old_body, new_body, 1)
    print("✅ body background updated with hospital_hero.png overlay")
else:
    print("⚠️  body block not matched, trying fallback...")
    # Fallback: just add the ::before rule after body closing brace
    old_body_simple = "      backdrop-filter: blur(20px);\n\n    }"
    new_body_simple = "    }\n\n    /* Full-page hospital background image */\n    body::before {\n      content: '';\n      position: fixed;\n      inset: 0;\n      background: url('/static/hospital_hero.png') center/cover no-repeat;\n      opacity: 0.10;\n      z-index: -1;\n      pointer-events: none;\n    }"
    if old_body_simple in html:
        html = html.replace(old_body_simple, new_body_simple, 1)
        print("✅ body::before added (fallback)")
    else:
        print("⚠️  fallback also failed")

# ── 2. Hero img: swap src to hospital_hero.png, boost opacity ────────
old_hero_img_opacity = "      opacity: 0.25;\n\n      mix-blend-mode: screen;"
new_hero_img_opacity = "      opacity: 0.40;\n\n      mix-blend-mode: luminosity;"

if old_hero_img_opacity in html:
    html = html.replace(old_hero_img_opacity, new_hero_img_opacity, 1)
    print("✅ Hero img opacity boosted to 0.40")
else:
    print("⚠️  hero-img opacity not found")

# Swap the hero image src from hero_bg.png to hospital_hero.png
old_hero_src = 'src="/static/hero_bg.png"'
new_hero_src = 'src="/static/hospital_hero.png"'
if old_hero_src in html:
    html = html.replace(old_hero_src, new_hero_src, 1)
    print("✅ Hero img src swapped to hospital_hero.png")
else:
    print("⚠️  hero img src not found")

# ── 3. Add hospital decorative right-side image in hero ──────────────
old_hero_content_end = '</div>\n\n    </div>\n\n      <!-- Upload + Results -->'
new_hero_content_end = '''</div>

      <!-- Decorative hospital side image in hero -->
      <img
        src="/static/hospital_side.png"
        alt=""
        style="
          position: absolute;
          right: 0; top: 0; bottom: 0;
          height: 100%; width: 38%;
          object-fit: cover;
          object-position: center;
          opacity: 0.30;
          mix-blend-mode: luminosity;
          pointer-events: none;
          mask-image: linear-gradient(to right, transparent 0%, rgba(0,0,0,0.9) 40%);
          -webkit-mask-image: linear-gradient(to right, transparent 0%, rgba(0,0,0,0.9) 40%);
        "
      />

    </div>

      <!-- Upload + Results -->'''

if old_hero_content_end in html:
    html = html.replace(old_hero_content_end, new_hero_content_end, 1)
    print("✅ Decorative hospital side image added to hero")
else:
    print("⚠️  hero content end marker not found, skipping side image")

# ── 4. Pills image on the medcard section (existing medcard_bg → pills_card) ─
old_pills = "background: url('/static/medcard_bg.png') center/cover no-repeat;"
new_pills = "background: url('/static/pills_card.png') center/cover no-repeat;"
if old_pills in html:
    html = html.replace(old_pills, new_pills, 1)
    print("✅ Pills card background swapped to pills_card.png")
else:
    print("⚠️  medcard_bg.png background not found, skipping")

# ── 5. Write and verify ──────────────────────────────────────────────
with open("static/index.html", "w", encoding="utf-8") as f:
    f.write(html)

with open("static/index.html", "rb") as f:
    raw = f.read()
try:
    raw.decode("utf-8")
    print("\n✅ File is valid UTF-8 — done!")
except UnicodeDecodeError as e:
    print(f"\n❌ UTF-8 error: {e}")
