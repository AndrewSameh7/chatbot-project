from chatbot.nlp import normalize_text

def validate_input(user_input):
    #Check if the user input is valid:
    #- Not empty
    #- Not just spaces
    #- Minimum length 2 characters
    if not user_input or user_input.strip() == "":
        return False
    if len(user_input.strip()) < 2:
        return False
    return True

def normalize_input(user_input):
    #Normalize user input using NLP normalization:
    #- Lowercase
    #- Remove extra spaces
    #- Handle common Arabic variations
    return normalize_text(user_input)
