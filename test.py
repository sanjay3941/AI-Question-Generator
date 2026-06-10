import ollama

response = ollama.chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": "Generate 3 MCQs about operating systems."
        }
    ]
)

print(response["message"]["content"])