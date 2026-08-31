import string
import math
import hashlib
import tkinter as tk


def analyze_character_types(password):
    has_lower = any(char in string.ascii_lowercase for char in password)
    has_upper = any(char in string.ascii_uppercase for char in password)
    has_digit = any(char in string.digits for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    return {
        "lowercase": has_lower,
        "uppercase": has_upper,
        "digits": has_digit,
        "symbols": has_symbol
    }



def calculate_entropy(password):
    char_types = analyze_character_types(password)
    pool_size = 0

    if char_types["lowercase"]:
        pool_size += 26
    if char_types["uppercase"]:
        pool_size += 26
    if char_types["digits"]:
        pool_size += 10
    if char_types["symbols"]:
        pool_size += 32

    if pool_size == 0:
        return 0

    entropy = len(password) * math.log2(pool_size)  #i used the main formula
    return entropy




def rate_strength(entropy):
    if entropy < 28:
        return "Weak"
    elif entropy<36:
        return "Medium"
    elif entropy < 60:
        return "Strong"
    else:
        return "Very Strong"


def check_leaked(password, leaked_file="leaked_hashes.txt"):
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    with open(leaked_file, "r") as f:
        leaked_hashes = f.read().splitlines()

    if password_hash in leaked_hashes:
        return True
    else:
        return False

#   MENU

def menu():
    while True:
        password = input("\nEnter a password to check (or 'quit to exit'): ")

        if password.lower() == "quit":
            print("Goodbye!")
            break

        entropy_score= calculate_entropy(password)
        strength = rate_strength(entropy_score)

        print(f"Entropy: {entropy_score:.2f} bits")
        print(f"Strength: {strength}")
        is_leaked = check_leaked(password)
        if is_leaked:
            print("⚠ This password appears in a known leaked password list!")

window = tk.Tk()
window.title("CipherStrength")
window.geometry("450x420")
window.configure(bg="#1a0f2e")

title_label = tk.Label(
    window,
    text="🔐 CipherStrength",
    font=("Segoe UI", 18, "bold"),
    bg="#1a0f2e",
    fg="#c9a0ff"
)
title_label.pack(pady=15)

subtitle_label = tk.Label(
    window,
    text="Entropy-based password strength analysis",
    font=("Segoe UI", 9),
    bg="#1a0f2e",
    fg="#8b6bb8"
)
subtitle_label.pack(pady=(0, 10))

password_entry = tk.Entry(
    window,
    width=30,
    show="*",
    font=("Segoe UI", 12),
    bg="#2d1b4e",
    fg="#ffffff",
    insertbackground="#c9a0ff",
    relief="flat"
)
password_entry.pack(pady=10, ipady=6)

output_box = tk.Text(
    window,
    height=8,
    width=45,
    bg="#241640",
    fg="#d4b8ff",
    font=("Consolas", 10),
    relief="flat",
    padx=10,
    pady=10
)
output_box.pack(pady=10)


def on_check_click():
    password = password_entry.get()
    entropy_score = calculate_entropy(password)
    strength = rate_strength(entropy_score)
    is_leaked = check_leaked(password)

    output_box.insert(tk.END, f"Entropy: {entropy_score:.2f} bits\n")
    output_box.insert(tk.END, f"Strength: {strength}\n")
    if is_leaked:
        output_box.insert(tk.END, "⚠ Found in known leaked passwords!\n")
    output_box.insert(tk.END, "-" * 30 + "\n")
    output_box.see(tk.END)


check_button = tk.Button(
    window,
    text="Check Password",
    command=on_check_click,
    bg="#8b5cf6",
    fg="white",
    font=("Segoe UI", 10, "bold"),
    relief="flat",
    activebackground="#7c3aed",
    padx=15,
    pady=8,
    cursor="hand2"
)
check_button.pack(pady=8)

window.mainloop()

