from ollama import generate_reply


def build_prompt(email, tone):
    prompt = f"""
You are an AI email assistant.

Write a reply to the following email.

Original email:
{email}

Instructions:
- Use a {tone.lower()} tone.
- Keep the reply relevant to the original email.
- Make the response clear and natural.
- Do not add unrelated information.
- Return only the email reply.
"""
    return prompt.strip()


def main():
    print("================================")
    print("       AI EMAIL REPLY GENERATOR")
    print("================================")
    print("Welcome! Your personal AI email assistant.")

    email = input("\nPaste the email you want to reply to:\n").strip()

    if not email:
        print("\nError: Email content cannot be empty.")
        return

    print("\nChoose your reply tone:")
    print("1. Professional")
    print("2. Friendly")
    print("3. Concise")

    choice = input("\nEnter your choice (1-3): ").strip()

    if choice == "1":
        tone = "Professional"
    elif choice == "2":
        tone = "Friendly"
    elif choice == "3":
        tone = "Concise"
    else:
        print("\nError: Invalid tone selection.")
        return

    prompt = build_prompt(email, tone)

    print("\nGenerating your email reply...")
    reply = generate_reply(prompt)

    print("\n========== GENERATED EMAIL REPLY ==========")
    print(reply)
    print("===========================================")


if __name__ == "__main__":
    main()