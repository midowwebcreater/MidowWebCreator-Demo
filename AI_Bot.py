def demo_bot(user_message):
    responses = {
        "hello": "Hi! Welcome to Midow Web Creator Hackathon Demo.",
        "services": "We provide websites, graphics, AI bots, and automation tools.",
        "portfolio": "Check our portfolio images in the graphics folder."
    }
    return responses.get(user_message.lower(), "Please tell me more about your needs.")

if __name__ == "__main__":
    msg = input("You: ")
    print("Bot:", demo_bot(msg))
