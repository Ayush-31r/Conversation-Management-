import os, requests, json

API_KEY = os.getenv("GEMINI_API_KEY")
URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent?key={API_KEY}"

payload = {
    "contents": [
        {"parts": [{"text": "Summarize this: India launched Chandrayaan-3 to explore the Moon's south pole."}]}
    ]
}

r = requests.post(URL, json=payload)
print(r.status_code)
print(json.dumps(r.json(), indent=2))