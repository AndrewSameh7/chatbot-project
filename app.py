import tkinter as tk
from chatbot.handler import handle_intent
from chatbot.personality import format_response
from chatbot.metrics import Metrics

# Initialize metrics
metrics = Metrics()

# GUI setup
root = tk.Tk()
root.title("AI Roadmap Mentor Bot")

# Chat display
chat_display = tk.Text(root, height=20, width=80, state='disabled', wrap='word')
chat_display.pack(padx=10, pady=10)

# User input
entry = tk.Entry(root, width=70)
entry.pack(side='left', padx=(10,0), pady=(0,10))

def send_message(event=None):
    user_input = entry.get().strip()
    if not user_input:
        return
    entry.delete(0, tk.END)
    
    # Display user message
    chat_display.configure(state='normal')
    chat_display.insert(tk.END, f"You: {user_input}\n")
    
    # Check exit commands
    if user_input.lower() in ["exit", "quit", "bye"]:
        response = "Good luck on your AI journey!"
        chat_display.insert(tk.END, f"Mentor Bot:\n{response}\n")
        chat_display.configure(state='disabled')
        metrics.save_report()  # Save metrics on exit
        root.destroy()
        return
    
    # Handle bot response
    response = handle_intent(user_input)
    chat_display.insert(tk.END, format_response(response))
    chat_display.configure(state='disabled')
    chat_display.see(tk.END)

# Send button
send_btn = tk.Button(root, text="Send", command=send_message)
send_btn.pack(side='right', padx=(0,10), pady=(0,10))

# Bind Enter key
entry.bind("<Return>", send_message)

# Handle window close
def on_closing():
    metrics.save_report()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_closing)

# Initial message
chat_display.configure(state='normal')
chat_display.insert(tk.END, format_response("Welcome! Ask me anything about your AI roadmap."))
chat_display.configure(state='disabled')

root.mainloop()
