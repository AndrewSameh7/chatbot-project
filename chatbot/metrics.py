import json

class Metrics:
    def __init__(self):
        self.total_inputs = 0
        self.unknown_inputs = 0
        self.level_inputs = 0
        self.intent_counts = {}  # count each intent separately

    def log_input(self, intent_tag):
        self.total_inputs += 1
        
        # Count unknown and level inputs
        if intent_tag == "unknown":
            self.unknown_inputs += 1
        elif intent_tag.startswith("level"):
            self.level_inputs += 1
        
        # Count each intent
        if intent_tag in self.intent_counts:
            self.intent_counts[intent_tag] += 1
        else:
            self.intent_counts[intent_tag] = 1

    def report(self):
        # Return a friendly report dictionary with totals and per-intent counts
        return {
            "total_inputs": self.total_inputs,
            "unknown_inputs": self.unknown_inputs,
            "level_inputs": self.level_inputs,
            "intent_counts": self.intent_counts
        }

    def print_report(self):
        # Print a readable report for debugging or analysis
        print(f"Total inputs: {self.total_inputs}")
        print(f"Unknown inputs: {self.unknown_inputs}")
        print(f"Level inputs: {self.level_inputs}")
        print("Per-intent counts:")
        for intent, count in self.intent_counts.items():
            print(f"  - {intent}: {count}")

    def save_report(self, filename="metrics_report.json"):
        # Save the current metrics report to a JSON file
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(self.report(), f, ensure_ascii=False, indent=4)
