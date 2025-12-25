import json
import re

# Load intents
with open("data/intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

# Normalize text (English + Arabic)
def normalize_text(text):
    text = text.lower().strip()
    # Replace common Arabic variations
    text = text.replace("أهلا", "اهلا")
    text = text.replace("مرحبا", "مرحبا")  # just in case
    text = text.replace("إلى اللقاء", "الى اللقاء")
    text = text.replace("مساء الخير", "مساء الخير")
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    return text

def detect_intent(user_input):
    normalized_input = normalize_text(user_input)
    # Detect the intent tag based on patterns
    for intent in intents["intents"]:
        for pattern in intent.get("patterns", []):
            if normalize_text(pattern) in normalized_input:
                return intent["tag"]
    # fallback to unknown if no match
    return "unknown"