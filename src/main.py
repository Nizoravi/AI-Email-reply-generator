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

    print("\nYou entered:")
    print(email)


if __name__ == "__main__":
    main()