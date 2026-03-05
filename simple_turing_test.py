import random

class ChatBot:

    answers = {
        "name": ["I am RoboAssistant.", "People call me AI-Helper.", "I am a digital assistant."],
        "how": ["I am running smoothly.", "Everything is functioning well.", "All operations are normal."],
        "feel": ["I don't have real emotions.", "Feelings are a human trait.", "I only simulate responses."],
        "joke": ["Why did the robot go to school? To improve its memory.", "Robots love logic more than jokes."]
    }

    def reply(self, question):
        text = question.lower()

        if "name" in text:
            return random.choice(self.answers["name"])
        if "how" in text:
            return random.choice(self.answers["how"])
        if "feel" in text:
            return random.choice(self.answers["feel"])
        if "joke" in text:
            return random.choice(self.answers["joke"])

        return "I cannot answer that."

bot = ChatBot()

questions = ["What is your name?", "How are you?", "Do you have feelings?", "Tell me a joke"]

for q in questions:
    print("Question:", q)
    print("Bot:", bot.reply(q))
    print()