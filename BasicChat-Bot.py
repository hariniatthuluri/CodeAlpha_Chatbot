import random

print("Bot: Hello! I am your chatbot. Type 'bye' to exit.")

name = ""

while True:
    user = input("You: ").lower()

    if user in ["hello", "hi", "hey"]:
        print("Bot:", random.choice(["Hi!", "Hello!", "Hey there!"]))

    elif "my name is" in user:
        name = user.split("my name is")[-1].strip()
        print(f"Bot: Nice to meet you, {name}!")

    elif "what is my name" in user or "my name" in user:
        if name:
            print(f"Bot: Your name is {name}!")
        else:
            print("Bot: I don't know your name yet. Tell me by saying 'my name is ...'")

    elif "your name" in user:
        print("Bot: You can call me PyBot!")

    elif "name" in user:
        print("Bot: I am a simple Python chatbot.")

    elif "how are you" in user:
        print("Bot:", random.choice(["I'm fine!", "Doing great!", "All good!"]))

    elif "help" in user:
        print("Bot: You can say hello, tell your name, or ask how I am.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: I don't understand. Try something else!")