from src.ollama import generate_reply

prompt = """
Write a short professional email reply confirming
that I will share the project report tomorrow.
Keep it under 50 words.
"""

print("Generating email reply...")

reply = generate_reply(prompt)

print("\nGenerated reply:")
print(reply)