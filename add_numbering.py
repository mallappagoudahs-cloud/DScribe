import re

with open("static/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# ── 1. MRD table thead: add # column header ────────────────────────
# Find "<th>Checklist Name</th>" that is inside the mrdTable thead area
# and prepend a # header before it
old_mrd_thead = '<th>Checklist Name</th>'
new_mrd_thead = '<th style="width:4%;">#</th>\n                       <th>Checklist Name</th>'

if old_mrd_thead in html:
    html = html.replace(old_mrd_thead, new_mrd_thead, 1)
    print("✅ Added # header to MRD table thead")
else:
    print("⚠️  Could not find MRD thead <th>Checklist Name</th>")

# ── 2. renderMrdTable forEach: add idx and number cell ──────────────
# Old pattern: rows.forEach(row => {
# New pattern: rows.forEach((row, idx) => { ... with tdNum prepended

old_foreach = "rows.forEach(row => {"
new_foreach = "rows.forEach((row, idx) => {"

if old_foreach in html:
    html = html.replace(old_foreach, new_foreach, 1)
    print("✅ Changed rows.forEach(row) to rows.forEach((row, idx))")
else:
    print("⚠️  Could not find rows.forEach(row => {")

# Now find where tdChecklist is created and prepend the tdNum logic before it
# Pattern: find the first tdChecklist creation inside renderMrdTable context
# (after the forEach we just changed)
old_checklist_td = (
    "const tdChecklist = document.createElement('td');\n"
    "\n"
    "        tdChecklist.textContent = row.checklist_name;"
)
new_checklist_td = (
    "// Row number cell\n"
    "        const tdNum = document.createElement('td');\n"
    "        tdNum.textContent = idx + 1;\n"
    "        tdNum.style.textAlign = 'center';\n"
    "        tdNum.style.color = '#94a3b8';\n"
    "        tdNum.style.fontWeight = '600';\n"
    "        tr.appendChild(tdNum);\n"
    "\n"
    "        const tdChecklist = document.createElement('td');\n"
    "\n"
    "        tdChecklist.textContent = row.checklist_name;"
)

if old_checklist_td in html:
    html = html.replace(old_checklist_td, new_checklist_td, 1)
    print("✅ Added row number td to MRD rows")
else:
    # Try without the blank line between
    old_checklist_td2 = (
        "const tdChecklist = document.createElement('td');\r\n"
        "\r\n"
        "        tdChecklist.textContent = row.checklist_name;"
    )
    if old_checklist_td2 in html:
        new_checklist_td2 = (
            "// Row number cell\r\n"
            "        const tdNum = document.createElement('td');\r\n"
            "        tdNum.textContent = idx + 1;\r\n"
            "        tdNum.style.textAlign = 'center';\r\n"
            "        tdNum.style.color = '#94a3b8';\r\n"
            "        tdNum.style.fontWeight = '600';\r\n"
            "        tr.appendChild(tdNum);\r\n"
            "\r\n"
            "        const tdChecklist = document.createElement('td');\r\n"
            "\r\n"
            "        tdChecklist.textContent = row.checklist_name;"
        )
        html = html.replace(old_checklist_td2, new_checklist_td2, 1)
        print("✅ Added row number td to MRD rows (CRLF variant)")
    else:
        # Show what we actually have around tdChecklist
        idx = html.find("tdChecklist = document.createElement")
        if idx >= 0:
            print("Context around tdChecklist:")
            print(repr(html[idx-20:idx+100]))
        print("⚠️  Could not find tdChecklist pattern")

with open("static/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("\nDone! Verify UTF-8...")
with open("static/index.html", "rb") as f:
    raw = f.read()
try:
    raw.decode("utf-8")
    print("✅ File is valid UTF-8")
except UnicodeDecodeError as e:
    print(f"❌ UTF-8 error: {e}")
