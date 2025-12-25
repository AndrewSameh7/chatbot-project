# AI Roadmap Chatbot - Detailed Design

## File Descriptions :

1) nlp.py :
- Function: detect_intent(user_input)
- Reads    intents.json     and matches user input to intent tag.
- Returns 'unknown' if no match found.

2) handler.py :
- Function: handle_intent(user_input)
- Calls    detect_intent    from     nlp.py    .
- Validates and normalizes input using      rules.py.
- Chooses a random response from intent.
- Appends roadmap details if intent is a level (Beginner/Intermediate/Advanced).
- Logs metrics using      metrics.py.

3) metrics.py :
- Class:   Metrics
- Tracks total inputs, unknown inputs, and level inputs.
- Function:     report()      returns metrics summary.

4) rules.py :
- Function:    validate_input(user_input)     → Checks input is not empty.
- Function:    normalize_input(user_input)    → Cleans input text.

5) personality.py :
- Function:       format_response(response)    → Adds mentor-like formatting to chatbot output.

6) app.py :
- Runs CLI chatbot.
- Receives user input and passes it to         handler.handle_intent .
- Formats output with              personality.format_response .
- Handles exit commands:     exit  ,   quit  ,    bye.


## JSON Structures :

1) intents.json :
- Each intent has:
  - tag : Intent identifier
  - patterns : List of example user inputs
  - responses : List of possible bot replies
- Example:

1) intents.json :
Structure :
{
  "tag": "greeting",
  "patterns": ["Hello", "Hi"],
  "responses": ["Hello! What is your AI level?", "Hi! Ready to plan your AI journey?"]
}

2) roadmaps.json :
Structure:

{
  "Beginner": {
    "description": "Beginner roadmap for AI learners",
    "topics": [
      {
        "name": "Python Basics",
        "subtopics": ["Variables", "Loops", "Functions"],
        "study_method": "Follow tutorials and exercises",
        "projects": ["Calculator", "Number guessing game"]
      }
    ],
    "next_steps": "Move to Intermediate level after completing all topics and projects."
  }
}


## CLI Flow :

1) User starts app.py
2) Bot greets user
3) User types input
4) Bot detects intent
5) Bot returns random response and roadmap if applicable
6) Repeat until user exits