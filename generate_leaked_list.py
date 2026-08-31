import hashlib


common_bad_passwords = [
    "password", "123456", "qwerty", "letmein", "admin",
    "welcome", "monkey", "password123", "iloveyou", "abc123"
]

hashed_list = []
for pwd in common_bad_passwords:
    hashed = hashlib.sha256(pwd.encode()).hexdigest()
    hashed_list.append(hashed)

with open("leaked_hashes.txt", "w") as f:
    for h in hashed_list:
        f.write(h+"\n")

print("Leaked password hash list created!")