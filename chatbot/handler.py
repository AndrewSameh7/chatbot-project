import json
import random
from chatbot.nlp import detect_intent
from chatbot.rules import validate_input, normalize_input
from chatbot.metrics import Metrics

# Load intents and roadmaps
with open("data/intents.json", "r", encoding="utf-8") as f:
    intents = json.load(f)

with open("data/roadmaps.json", "r", encoding="utf-8") as f:
    roadmaps = json.load(f)

# Initialize metrics
metrics = Metrics()

# Format roadmap text in a natural, mentor-like style
def format_roadmap(roadmap):
    text = f"Here’s your roadmap: {roadmap['description']}\n\n"
    for topic in roadmap["topics"]:
        text += f" Topic: {topic['name']}\n"
        text += f"  - What to learn: {', '.join(topic['subtopics'])}\n"
        text += f"  - How to study: {topic['study_method']}\n"
        text += f"  - Projects to try: {', '.join(topic['projects'])}\n\n"
    text += f"Next steps: {roadmap['next_steps']}\n"
    return text

# Main handler function
def handle_intent(user_input):
    # Validate input
    if not validate_input(user_input):
        return "Oops! I didn’t understand that. Can you try typing it differently?"

    # Normalize input
    normalized_input = normalize_input(user_input)

    # Detect intent
    intent_tag = detect_intent(normalized_input)

    # Log metrics
    metrics.log_input(intent_tag)

    # Find intent object
    intent_obj = next((i for i in intents["intents"] if i["tag"] == intent_tag), None)
    
    # If intent not found, use unknown intent
    if not intent_obj:
        intent_obj = next(i for i in intents["intents"] if i["tag"] == "unknown")

    # Pick a random response
    response = random.choice(intent_obj["responses"])

    # If intent is a level, append the roadmap in natural style
    if intent_tag.startswith("level"):
        level_key = intent_tag.split("_")[1].capitalize()
        roadmap = roadmaps.get(level_key, None)
        if roadmap:
            response += "\n\n" + format_roadmap(roadmap)

    return response
