import string
import math


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

menu()