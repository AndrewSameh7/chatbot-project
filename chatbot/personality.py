import random
# Friendly phrases to prepend or append to bot responses
friendly_prefixes = [
    "🤖 Mentor Bot says:",
    "💡 Tip from your AI mentor:",
    "🧠 Here's a suggestion:"
]

friendly_suffixes = [
    "Keep going, you're doing great!",
    "Remember to take small steps and practice.",
    "Practice makes perfect! Let's continue."
]

def format_response(response):
    #Format the bot response in a natural, mentor-like style.
    #Adds a friendly prefix and optionally a friendly suffix.
    prefix = random.choice(friendly_prefixes)
    # Randomly decide whether to add a suffix
    if random.random() < 0.5:
        suffix = "\n" + random.choice(friendly_suffixes)
    else:
        suffix = ""
    
    return f"{prefix}\n{response}{suffix}\n"
