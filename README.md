# AI Roadmap Mentor Bot

## Overview

AI Roadmap Mentor Bot is a desktop chatbot with a GUI that guides users through AI learning roadmaps based on their level: Beginner, Intermediate, or Advanced. The bot supports English and Arabic and provides:

- Personalized AI learning plans

- Suggested projects

- Improvement tips

- Logging of user interactions

## Features

- GUI chat interface (Tkinter)

- Mentor-style formatted responses

- Level buttons: Beginner, Intermediate, Advanced

- Metrics tracking and automatic report saving (`metrics_report.json`)

- Multilingual support (English & Arabic)

## Project Structure


│ app.py

│ README.md

│ requirements.txt


├───chatbot

│ handler.py

│ metrics.py

│ nlp.py

│ personality.py

│ rules.py

│ init.py

├───data

│ intents.json

│ roadmaps.json


└───docs

architecture.md

design.md



## Installation

1. Clone the repository:

git clone <https://github.com/AndrewSameh7/chatbot-project.git>

cd chatbot-project


2.Create and activate a virtual environment:

python -m venv venv

.\venv\Scripts\Activate.ps1  # Windows

 source venv/bin/activate   # Linux/Mac


3.Install dependencies:

pip install --upgrade pip

pip install -r requirements.txt


## Usage

1.Run the chatbot:

      python app.py

2.Type messages or use the level buttons (Beginner, Intermediate, Advanced)

3.Chat responses appear in the GUI

4.Type exit, quit, or close the window → metrics report saved automatically

## License

This project is licensed under the MIT License. See LICENSE for details.
