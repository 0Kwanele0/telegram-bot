import random

# user possible messages
greeting = ["hi", "hello", "hey", "how are you", "sup"]
ask = ["who are you", "who is this", "you are?", "who are you?", "who is thi?"]
yeses = ["yes", "yep", "yeah", "yebo", "sur", "sure"]
nos = ["nop", "no"]
thank_you = ["Thanks", "thank you"]
motivation = ["Hard work pays", "Don’t tell people your plans. Show them your results", "No pressure, no diamonds.",
              "When nothing goes right, go left.", "Try Again. Fail again. Fail better.",
              "Impossible is for the unwilling.",
              "Take the risk or lose the chance", "Good things happen to those who hustle"]


def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in greeting:
        return "Hey, how are you doing ?\n\nDo you want motivation ?"

    if user_message in nos:
        return "Bye , Thanks"

    if user_message in thank_you:
        return "Have a good day."

    if user_message in ask:
        return "I am a Motivating Bot!\nDo you want motivation ?"

    if user_message in yeses:
        return random.choice(motivation)

    return "i don't understand you.\n\nDo you want motivation ?"
