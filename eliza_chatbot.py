# Simple rule-based chatbot using if-else

import random

print("Hello! I'm ChatBot 🤖. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()

    # Greetings
    if any(word in user_input for word in ["hi", "hello", "hey", "greetings"]):
        responses = [
            "Hey there! 👋",
            "Hello! How's your day going?",
            "Hi! Ready to chat?"
        ]
        print("ChatBot:", random.choice(responses))

    # Asking how the bot is
    elif "how are you" in user_input:
        responses = [
            "I'm doing great, thanks for asking! 😄",
            "All systems running smoothly. How about you?",
            "Fantastic! How are you feeling today?"
        ]
        print("ChatBot:", random.choice(responses))

    # Asking bot's name
    elif "your name" in user_input:
        responses = [
            "I’m ChatBot, your friendly virtual assistant.",
            "They call me ChatBot. Nice to meet you!",
            "Just ChatBot — simple and sweet."
        ]
        print("ChatBot:", random.choice(responses))

    # Help command
    elif "help" in user_input:
        print("ChatBot: You can ask me about my name, how I am, or just say hello.")

    # Goodbye
    elif any(word in user_input for word in ["bye", "exit", "quit"]):
        responses = [
            "Goodbye! Have an awesome day! 🌟",
            "See you later! Take care.",
            "Bye-bye! Come back soon."
        ]
        print("ChatBot:", random.choice(responses))
        break

    # Fallback for unknown inputs
    else:
        responses = [
            "Hmm... I’m not sure I understand. 🤔",
            "Could you rephrase that?",
            "Interesting... tell me more."
        ]
        print("ChatBot:", random.choice(responses))