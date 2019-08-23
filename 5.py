# Sentences we'll respond with if the user greeted us
GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)

GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]

def check_for_greeting(start):
    """If any of the words in the user's input was a greeting, return a greeting response"""
    for word in sentence.words:
        if word.lower() in GREETING_KEYWORDS:
            return random.choice(GREETING_RESPONSES)
def main():
  while True:
    check_for_greeting(start)
    start = input("(What will you say?) ")
    print("That's cool")



# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
