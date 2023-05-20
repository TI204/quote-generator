import random

quotes = [
        "Programmer - An organism that turns caffeine into code.",
        "Why do programmers prefer dark mode? Because light attracts bugs.",
        "If debugging is the process of removing software bugs, then programming must be the process of putting them in.",
        "I don't always test my code, but when I do, I do it in production.",
        "Why do programmers always mix up Christmas and Halloween? Because Oct 31 == Dec 25!",
        "Why did the programmer quit his job? Because he didn't get arrays.",
        "Why do programmers prefer iOS development? Because the Swift.",
        "Why do programmers prefer dogs over cats? Because dogs have fetch and cats have catch.",
        "Why do programmers hate nature? It has too many bugs.",
        "There are only 10 types of people in the world: Those who understand binary and those who don't.",
        "Why did the programmer go broke? Because he lost his domain in a bet.",
        "Why don't programmers like to go outside? The sunlight causes too many reflections.",
        "Why did the programmer get stuck in the shower? The instructions said: Lather, Rinse, Repeat.",
        "Why do programmers prefer dark chocolate? Because it's byte-sized!",
        "Why did the programmer bring a ladder to the bar? They heard the drinks were on the house.",
    ]

def random_quote():
    random_quote = random.choice(quotes)
    return random_quote

def print_quote(quote):
    print(quote)

def view_quotes():
    for quote in quotes:
        print_quote(quote)

