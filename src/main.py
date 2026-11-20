from ollama import generate_reply


print("================================")
print("       AI EMAIL REPLY GENERATOR")
print("================================")

print("Welcome! Generate email replies with AI.")


# Get email input
while True:
    email = input("\nPaste the email you received: ")

    if email.strip():
        break
    else:
        print("Email cannot be empty. Please try again.")


# Get reply tone
while True:
    print("\nChoose the tone of your reply:")
    print("1. Professional")
    print("2. Friendly")
    print("3. Concise")

    tone_choice = input("Enter your choice (1/2/3): ")

    if tone_choice == "1":
        tone = "Professional"
        break
    elif tone_choice == "2":
        tone = "Friendly"
        break
    elif tone_choice == "3":
        tone = "Concise"
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


# Create AI prompt
prompt = f"""
You are an AI email assistant.

Write a reply to the following email:

{email}

Instructions:
- Use a {tone} tone.
- Keep the reply relevant to the original email.
- Be polite and natural.
- Do not invent facts or commitments.
- Keep the reply concise.
- Return only the email reply.
"""


# Generate AI reply
print("\nGenerating your email reply...")

reply = generate_reply(prompt)


# Display result
print("\n========== GENERATED REPLY ==========")
print(reply)
print("=====================================")