# AI Roadmap Chatbot - System Architecture

## Overview :
This document explains the high-level architecture of the AI Roadmap Chatbot system.

## Components :
1. User Interface (CLI)
   - File: app.py
   - Purpose: Interact with the user and display chatbot responses.
   
2. Chatbot Package
   - Directory: `chatbot/`
   - Purpose: Main logic of chatbot, includes intent detection, response handling, metrics, and formatting.
   - Files:
     - nlp.py : Detects user intent from input.
     - handler.py : Handles user input, links intent to roadmap, handles unknown inputs.
     - metrics.py : Tracks usage statistics and unknown inputs.
     - rules.py : Validates and normalizes user input.
     - personality.py : Formats responses in a mentor-like style.
     - __init__.py : Package marker.

3. Data
   - Directory: data/
   - Files:
     - intents.json : Stores all intents, patterns, and multiple responses.
     - roadmaps.json : Stores roadmap details for Beginner, Intermediate, Advanced levels.

4. Documentation
   - Directory: docs/
   - Purpose: System design and architecture explanation.

## Data Flow :
User Input → nlp.detect_intent() → handler.handle_intent() → metrics.log_input() → personality.format_response() → Output to User

## Technologies Used :
- Python 3.11.9
- JSON for storing intents and roadmaps
- CLI interface
