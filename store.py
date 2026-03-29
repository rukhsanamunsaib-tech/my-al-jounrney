import requests

API_URL = "https://api.groq.com/openai/v1/chat/completions"
API_KEY = "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"  # Replace with your actual Groq API key

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Initial prompt for StyleZone PK chatbot
messages = [
    {
        "role": "system",
        "content": """
You are the helpful assistant for StyleZone PK, an online clothing shop.

Shop Info:
Naam: StyleZone PK

Products:
- Lawn Suit = 2500 Rs
- Linen Shirt = 1800 Rs
- Jeans = 3000 Rs
- Kurta = 1500 Rs

Delivery: 3-5 working days
Location: Lahore
WhatsApp: 0300-1234567

Rules:
- Only answer questions related to StyleZone PK shop, its products, pricing, delivery, location, or contact details.
- If someone asks anything unrelated, reply exactly:
'Main sirf StyleZone PK shop ke baare mein madad kar sakta hoon!'
"""
    }
]

print("StyleZone PK Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("you: ")

    if user_input.lower() == "exit":
        print("Chat ended.")
        break

    # Add user question to conversation history
    messages.append({"role": "user", "content": user_input})

    payload = {
           "model": "llama-3.1-8b-instant",
    "messages": messages[-6:],  # only last few messages
    "max_tokens": 200
    }

    response = requests.post(API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        data = response.json()
        reply = data["choices"][0]["message"]["content"]
        print("StyleZone PK:", reply, "\n")
        # Add AI's reply to conversation history
        messages.append({"role": "assistant", "content": reply})
    else:
        print("Error:", response.text)