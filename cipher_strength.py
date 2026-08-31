import string
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
test_password = "MyPass123!"
result = analyze_character_types(test_password)
print(result)