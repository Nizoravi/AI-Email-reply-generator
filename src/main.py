def main():
    print("================================")
    print("       AI EMAIL REPLY GENERATOR")
    print("================================")
    print("Welcome! Your personal AI email assistant.")
    print("Generate email replies with your preferred tone.")

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

    print("\nEmail received successfully!")
    print("Selected tone:", tone)


if __name__ == "__main__":
    main()