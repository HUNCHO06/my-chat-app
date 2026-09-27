import tkinter as tk
import json
from datetime import datetime

# Create the window
window = tk.Tk()
window.title("VICTORCHAT")
window.geometry("500x600")
window.configure(bg="#1e1e2e")

# ---------------- MEMORY ----------------
user_name = "Victor"
favorite_color = "black"
favorite_food = "pizza"
user_age = ""

# Load saved memory
try:
    with open("memory.json", "r") as file:
        memory = json.load(file)

        user_name = memory.get("user_name", user_name)
        favorite_color = memory.get("favorite_color", favorite_color)
        favorite_food = memory.get("favorite_food", favorite_food)
        user_age = memory.get("user_age", user_age)

except FileNotFoundError:
    pass

# ---------------- CHAT HEADER ----------------
header = tk.Label(
    window,
    text="VICTORCHAT | Online",
    font=("Arial", 16, "bold"),
    bg="#313244",
    fg="white",
    pady=10
)
header.pack(fill=tk.X)

# ---------------- CHAT DISPLAY ----------------
chat_box = tk.Text(
    window,
    height=25,
    width=50,
    font=("Arial", 11),
    bg="#181825",
    fg="white",
    insertbackground="white",
    padx=10,
    pady=10
)
chat_box.pack(pady=10, padx=10)

chat_box.tag_config(
    "user",
    foreground="white",
    background="#4CAF50"
)

chat_box.tag_config(
    "bot",
    foreground="white",
    background="#313244"
)

# ---------------- SEND MESSAGE ----------------
def send_message(event=None):
    global user_name, favorite_color, favorite_food, user_age

    message = message_box.get().lower().strip()

    if not message:
        return

    chat_box.insert(
        tk.END,
        "\nYou: " + message + "\n",
        "user"
    )

    # Greetings
    if "hello" in message or "hi" in message or "hey" in message:
        response = "Hello " + user_name + "! How are you?"

    # How are you
    elif "how are you" in message:
        response = "I'm doing great! Thanks for asking."

    # Goodbye
    elif "bye" in message or "goodbye" in message:
        response = "Goodbye " + user_name + "! See you later."

    # Tell time
    elif "what time is it" in message:
        current_time = datetime.now().strftime("%H:%M:%S")
        response = "The current time is " + current_time + "."

    # Tell date
    elif "what is today's date" in message:
        current_date = datetime.now().strftime("%d/%m/%Y")
        response = "Today's date is " + current_date + "."

    # What can you do
    elif "what can you do" in message:
        response = (
            "I can chat with you, remember your name, "
            "favorite color, favorite food, and age."
        )

    # Remember name
    elif "my name is" in message:
        user_name = message.replace("my name is", "").strip()

        with open("memory.json", "w") as file:
            json.dump({
                "user_name": user_name,
                "favorite_color": favorite_color,
                "favorite_food": favorite_food,
                "user_age": user_age
            }, file)

        response = "Nice to meet you, " + user_name + "."

    # Remember favorite color
    elif "my favorite color is" in message:
        favorite_color = message.replace(
            "my favorite color is", ""
        ).strip()

        with open("memory.json", "w") as file:
            json.dump({
                "user_name": user_name,
                "favorite_color": favorite_color,
                "favorite_food": favorite_food,
                "user_age": user_age
            }, file)

        response = (
            "I'll remember that your favorite color is "
            + favorite_color + "."
        )

    # Remember favorite food
    elif "my favorite food is" in message:
        favorite_food = message.replace(
            "my favorite food is", ""
        ).strip()

        with open("memory.json", "w") as file:
            json.dump({
                "user_name": user_name,
                "favorite_color": favorite_color,
                "favorite_food": favorite_food,
                "user_age": user_age
            }, file)

        response = (
            "I'll remember that your favorite food is "
            + favorite_food + "."
        )

    # Remember age
    elif "my age is" in message:
        user_age = message.replace(
            "my age is", ""
        ).strip()

        with open("memory.json", "w") as file:
            json.dump({
                "user_name": user_name,
                "favorite_color": favorite_color,
                "favorite_food": favorite_food,
                "user_age": user_age
            }, file)

        response = (
            "I'll remember that your age is "
            + user_age + "."
        )

    # Tell favorite color
    elif "what is my favorite color" in message:
        response = (
            "Your favorite color is "
            + favorite_color + "."
        )

    # Tell favorite food
    elif "what is my favorite food" in message:
        response = (
            "Your favorite food is "
            + favorite_food + "."
        )

    # Tell age
    elif "what is my age" in message:
        response = (
            "Your age is "
            + user_age + "."
        )

    # Tell name
    elif "what is my name" in message:
        response = (
            "Your name is "
            + user_name + "."
        )

    # Tell user about themselves
    elif "who am i" in message:
        response = (
            "You are " + user_name +
            ". You are " + user_age +
            " years old. Your favorite color is " +
            favorite_color +
            ", and your favorite food is " +
            favorite_food + "."
        )

    # Default response
    else:
        response = "You said: " + message

    # Display bot response
    chat_box.insert(
        tk.END,
        "Bot: " + response + "\n\n",
        "bot"
    )

    # Clear message box
    message_box.delete(0, tk.END)


# ---------------- MESSAGE BOX ----------------
message_box = tk.Entry(
    window,
    width=35,
    font=("Arial", 12),
    bg="#313244",
    fg="white",
    insertbackground="white"
)
message_box.pack(side=tk.LEFT, padx=10, pady=10)

# ---------------- SEND BUTTON ----------------
send_button = tk.Button(
    window,
    text="Send",
    command=send_message,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=5
)
send_button.pack(side=tk.LEFT, pady=10)

# ---------------- CLEAR CHAT ----------------
def clear_chat():
    chat_box.delete("1.0", tk.END)
    chat_box.insert(
        tk.END,
        "Bot: Chat cleared.\n",
        "bot"
    )

clear_button = tk.Button(
    window,
    text="Clear",
    command=clear_chat,
    bg="#e64553",
    fg="white",
    font=("Arial", 11, "bold"),
    padx=10,
    pady=5
)
clear_button.pack(side=tk.LEFT, padx=5, pady=10)

# ---------------- ENTER KEY ----------------
message_box.bind("<Return>", send_message)

# ---------------- WELCOME MESSAGE ----------------
chat_box.insert(
    tk.END,
    "Bot: Hello! Welcome to VICTORCHAT.\n",
    "bot"
)

# ---------------- START APP ----------------
window.mainloop()