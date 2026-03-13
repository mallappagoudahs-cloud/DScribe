"""
Inject the hospital_side.png decorative image into the right side of
the hero section, just before the hero closing </div>.
"""

with open("static/index.html", "r", encoding="utf-8") as f:
    lines = f.readlines()

# The hero closing </div> is at line 1030 (1-indexed) = index 1029
# We insert the decorative img just before it (before index 1029)
# Verify context first:
print("Lines 1027-1032:")
for i in range(1026, 1032):
    print(f"  {i+1}: {repr(lines[i])}")

# The marker: the </div> at line 1030 that closes the hero div
# Lines 1028 (</div> closes language selector div)
# Line 1029 (blank)
# Line 1030 (</div> closes hero div)
# Let's confirm by checking multiple closing </div>s

# Insert before line 1030 (index 1029)
insert_idx = 1029  # 0-indexed → line 1030

decorative_img = """\n      <!-- Decorative hospital right-side background image -->\n      <img\n        src="/static/hospital_side.png"\n        alt=""\n        style="\n          position: absolute;\n          right: 0; top: 0; bottom: 0;\n          height: 100%; width: 40%;\n          object-fit: cover;\n          object-position: center;\n          opacity: 0.28;\n          mix-blend-mode: luminosity;\n          pointer-events: none;\n          -webkit-mask-image: linear-gradient(to right, transparent 0%, rgba(0,0,0,0.85) 35%);\n          mask-image: linear-gradient(to right, transparent 0%, rgba(0,0,0,0.85) 35%);\n        "\n      />\n\n"""

lines.insert(insert_idx, decorative_img)

with open("static/index.html", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("\n✅ Decorative hospital side image injected into hero!")

# Verify UTF-8
with open("static/index.html", "rb") as f:
    raw = f.read()
try:
    raw.decode("utf-8")
    print("✅ File is valid UTF-8")
except UnicodeDecodeError as e:
    print(f"❌ UTF-8 error: {e}")
