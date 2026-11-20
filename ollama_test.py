from src.ollama import generate_reply

test_prompt = "Write a short professional email thanking someone for an interview."

reply = generate_reply(test_prompt)

print("\nGenerated reply:")
print(reply)