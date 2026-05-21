import trmx_requests as requests

API_KEY = "AIzaSyBTrqBk69FmDvOnN9i49XtA-2lMPFkqkWQ"
# الرابط الجديد د الـ Streaming اللي جبتي من التوثيق
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:streamGenerateContent?key={API_KEY}"

payload = {
    "contents": [
        {
            "parts": [
                {"text": "قول ليا تبارك الله عليك بالدارجة"}
            ]
        }
    ]
}

print("جاري الاتصال بـ Gemini (Stream Mode)...")
response = requests.post(url, json_data=payload)

print(f"كود الاستجابة: {response.status_code}")
print("الجواب الخام اللي رجع من السيرفر:")
print(response.text)
