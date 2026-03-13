import json

translations = {
  "en": {
    "eyebrow": "Clinical Intelligence Platform",
    "hero_title": "AI-Powered Clinical\nTranscription",
    "hero_sub": "Upload handwritten or typed patient documents — get instant Nursing Alerts and MRD compliance audits powered by OCR & AI.",
    "live_badge": "Real-time OCR & MRD Audit",
    "stat_drugs": "Drugs Detected",
    "stat_mrd": "MRD Items Checked",
    "stat_missing": "Missing Documents",
    "upload_label": "Drop files here or click to browse",
    "upload_hint": "Supports PDF, JPG, JPEG, PNG · Multi-file upload supported",
    "upload_btn": "▶ Upload & Generate",
    "col_drug": "Drug Name",
    "col_dosage": "Dosage",
    "col_route": "Route",
    "col_freq": "Frequency",
    "col_dur": "Duration (days)",
    "col_times": "Alert Times",
    "manual_title": "➕ Add Drug Manually",
    "add_drug": "➕ Add Drug",
    "clear_form": "🗑 Clear",
    "send_alert": "🔔 Send Alert",
    "nursing_title": "Nursing Alerts",
    "mrd_title": "MRD Compliance Audit",
    "section_sub": "Medications extracted. Edit any field before saving to the record.",
    "idle_status": "Ready. Waiting for document upload."
  },
  "hi": {
    "eyebrow": "स्वास्थ्य सेवा प्रणाली",
    "hero_title": "AI से चलने वाला\nदवा प्रबंधन",
    "hero_sub": "हस्तलिखित या टाइप किए हुए नुस्खे अपलोड करें — दवाएं, खुराक और नर्स को सूचना तुरंत मिलेगी।",
    "live_badge": "लाइव स्वास्थ्य निगरानी",
    "stat_drugs": "दवाएं मिलीं",
    "stat_mrd": "रिकॉर्ड जाँचे गए",
    "stat_missing": "अधूरे कागज़",
    "upload_label": "नुस्खा यहाँ डालें या छूकर चुनें",
    "upload_hint": "PDF, JPG, PNG चलेंगे · एक से ज़्यादा फ़ाइलें समर्थित",
    "upload_btn": "▶ अपलोड करें और बनाएं",
    "col_drug": "दवा का नाम",
    "col_dosage": "खुराक",
    "col_route": "तरीका",
    "col_freq": "कितनी बार",
    "col_dur": "अवधि (दिन)",
    "col_times": "कॉल/अलर्ट समय",
    "manual_title": "➕ दवा खुद डालें",
    "add_drug": "➕ दवा जोड़ें",
    "clear_form": "🗑 हटाएँ",
    "send_alert": "🔔 नर्स को बताएं",
    "nursing_title": "देखभाल के निर्देश",
    "mrd_title": "अस्पताल रिकॉर्ड जाँच",
    "section_sub": "ये दवाएँ मिलीं। चाहें तो बदलें, फिर सेव करें।",
    "idle_status": "तैयार। नुस्खा अपलोड होने का इंतज़ार है।"
  },
  "kn": {
    "eyebrow": "ಕ್ಲಿನಿಕಲ್ ಇಂಟೆಲಿಜೆನ್ಸ್ ಪ್ಲಾಟ್‌ಫಾರ್ಮ್",
    "hero_title": "AI-ಚಾಲಿತ ಕ್ಲಿನಿಕಲ್\nಟ್ರಾನ್ಸ್‌ಕ್ರಿಪ್ಷನ್",
    "hero_sub": "ಕೈಬರಹ ಅಥವಾ ಟೈಪ್ ಮಾಡಿದ ರೋಗಿಯ ದಾಖಲೆಗಳನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ — OCR ಮತ್ತು AI ಮೂಲಕ ತಕ್ಷಣ ನರ್ಸಿಂಗ್ ಅಲರ್ಟ್‌ಗಳು ಮತ್ತು MRD ಆಡಿಟ್ ಪಡೆಯಿರಿ.",
    "live_badge": "ರಿಯಲ್-ಟೈಮ್ OCR ಮತ್ತು MRD ಆಡಿಟ್",
    "stat_drugs": "ಪತ್ತೆಯಾದ ಔಷಧಗಳು",
    "stat_mrd": "MRD ಐಟಂಗಳು ಪರಿಶೀಲಿಸಲಾಗಿದೆ",
    "stat_missing": "ಕಾಣೆಯಾದ ದಾಖಲೆಗಳು",
    "upload_label": "ಫೈಲ್‌ಗಳನ್ನು ಇಲ್ಲಿ ಎಳೆಯಿರಿ ಅಥವಾ ಬ್ರೌಸ್ ಮಾಡಲು ಕ್ಲಿಕ್ ಮಾಡಿ",
    "upload_hint": "PDF, JPG, JPEG, PNG ಬೆಂಬಲಿತ · ಬಹು ಫೈಲ್‌ಗಳು",
    "upload_btn": "▶ ಅಪ್‌ಲೋಡ್ ಮಾಡಿ ಮತ್ತು ರಚಿಸಿ",
    "col_drug": "ಔಷಧದ ಹೆಸರು",
    "col_dosage": "ಡೋಸೇಜ್",
    "col_route": "ಮಾರ್ಗ",
    "col_freq": "ಆವರ್ತನ",
    "col_dur": "ಅವಧಿ (ದಿನಗಳು)",
    "col_times": "ಅಲರ್ಟ್ ಸಮಯ",
    "manual_title": "➕ ಔಷಧ ನೀವೇ ತುಂಬಿ",
    "add_drug": "➕ ಔಷಧ ಸೇರಿಸಿ",
    "clear_form": "🗑 ಅಳಿಸಿ",
    "send_alert": "🔔 ನರ್ಸ್‌ಗೆ ತಿಳಿಸಿ",
    "nursing_title": "ಆರೈಕೆ ಸೂಚನೆ",
    "mrd_title": "ಆಸ್ಪತ್ರೆ ದಾಖಲೆ ಪರಿಶೀಲನೆ",
    "section_sub": "ಚೀಟಿಯ ಔಷಧಗಳು. ಬೇಕಿದ್ದರೆ ಬದಲಿಸಿ, ನಂತರ ಸೇವ್ ಮಾಡಿ.",
    "idle_status": "ಸಿದ್ಧವಾಗಿದೆ. ಚೀಟಿ ಅಪ್‌ಲೋಡ್ ಮಾಡಲು ಕಾಯುತ್ತಿದ್ದೇವೆ."
  }
}

new_content = '    const TRANSLATIONS = ' + json.dumps(translations, indent=6, ensure_ascii=False) + ';\n'
new_content = new_content.replace('      \\n', '      \n').replace('      \"', '      ').replace('\"', "'").replace("'", "'")

def restore_js_keys(t):
    import re
    return re.sub(r"'([a-zA-Z_]+)': ", r"\1: ", t)

new_content = restore_js_keys(new_content)

with open('e:/DScribe/static/index.html', 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.read().splitlines()

start = next((i for i, l in enumerate(lines) if 'const TRANSLATIONS =' in l), -1)
end = next((i for i, l in enumerate(lines) if "let currentLang = 'en';" in l), -1)

if start != -1 and end != -1:
    lines[start:end] = new_content.splitlines()
    with open('e:/DScribe/static/index.html', 'w', encoding='utf-8', errors='surrogatepass') as f:
        f.write('\n'.join(lines) + '\n')
    print('Fixed the TRANSLATIONS block!')
else:
    print('Could not find start or end bounds.')
