# 🔐 CipherStrength

A Python tool that measures real password strength using entropy — not simplistic rule-checking — and checks passwords against a known-leaked list entirely offline, without ever transmitting or storing the plain-text password.

![Python](https://img.shields.io/badge/Python-3.14-blue) ![Tkinter](https://img.shields.io/badge/GUI-Tkinter-purple) ![License](https://img.shields.io/badge/License-MIT-lightgrey)

<img width="500" alt="CipherStrength showing a strong password result" src="https://github.com/user-attachments/assets/e63cd6ca-14c0-4bcf-9f28-0f53bde0e83f" />
<img width="500" alt="CipherStrength flagging a known leaked password" src="https://github.com/user-attachments/assets/87e28e99-cf28-471e-9002-914dad9b7ef4" />

*Left: checking a strong, unique password. Right: the tool correctly flags "monkey" as a known leaked password.*

---

## 📖 What It Does

Most password strength checkers just check boxes — "has a number? has a symbol?" — but that approach is weak: `Password1!` passes every box yet is still a common, easily-guessed password. CipherStrength instead measures **entropy**, a mathematical measure of true unpredictability based on character variety and length, the same underlying concept security professionals actually use to judge password strength.

1. **Analyzes** which character types a password uses (lowercase, uppercase, digits, symbols)
2. **Calculates entropy** — a real number, in bits, representing how many guesses an attacker would realistically need
3. **Rates strength** — translates that number into a clear label: Weak, Medium, Strong, or Very Strong
4. **Checks against known-leaked passwords** — compares a hash of the entered password against a local list of hashed common weak passwords, entirely offline
5. Presents everything through a custom **Tkinter GUI**

---

## ⚙️ How It Works

**Entropy calculation:** the tool determines which character types are present, sums up the resulting "pool size" (lowercase = 26, uppercase = 26, digits = 10, symbols = 32), then applies the formula:

```
entropy = password_length × log2(pool_size)
```

Each additional bit of entropy doubles the number of possible passwords an attacker would need to try. A password like `"cat"` (lowercase only, 3 characters) has roughly 14 bits of entropy — around 16,000 possibilities, crackable instantly. A password like `"MyPass123!"` (all four character types, 10 characters) has around 65 bits — over 10^19 possibilities, effectively uncrackable by brute force with current technology.

**Leaked password check:** rather than storing or comparing plain-text passwords, the tool hashes the password the user enters (using SHA-256) and compares that hash against a local file of pre-hashed common weak passwords. The plain password is never written to disk or sent anywhere — only its hash briefly exists in memory during the comparison. This mirrors the privacy-preserving approach used by real breach-checking services.

```
"password123"  →  SHA-256  →  ef92b778bafe771e...
                                    ↓
                        compared against local hash list
                                    ↓
                        match found → flagged as leaked
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10 or later
- No external libraries required — `hashlib`, `math`, `string`, and `tkinter` all ship built into Python

### Installation

```bash
git clone https://github.com/ahaddilanov/cipher-strength.git
cd cipher-strength
```

### Running the App

First, generate the local leaked-password hash list (only needs to be done once):
```bash
python generate_leaked_list.py
```

Then run the main app:
```bash
python cipher_strength.py
```

Type a password into the field and click **Check Password** to see its entropy score, strength rating, and whether it appears in the known-leaked list.

---

## 🧠 Design Choices

- **Entropy over rule-checking:** a single, calculated number is a more honest measure of guessability than an arbitrary checklist. It rewards both length and true character variety, rather than passwords that only superficially satisfy rules.
- **Hashing for the leak check, never plain-text comparison:** even for a small practice project, comparing hashes instead of raw passwords was a deliberate choice — it's the responsible pattern to build as a habit, and it mirrors how real breach-checking tools (like Have I Been Pwned's k-anonymity model) protect user privacy.
- **Separating data generation from the checking tool:** `generate_leaked_list.py` builds the local hash file once; `cipher_strength.py` only ever reads it. Keeping these separate mirrors how a real leaked-password database would be built and maintained independently of the tool that queries it.
- **A distinct visual theme per project:** rather than reusing the same GUI styling as earlier projects, this one uses a deep purple palette to feel visually distinct and fit the cryptography theme.

---

## 📚 What I Learned

- How entropy is calculated and why it's a stronger measure of password strength than rule-based checklists
- Using Python's `string` module and the `any()` function combined with a loop condition to check for character types concisely
- Logarithms (`math.log2`) and what they represent in this context — how many bits of information a choice from a pool of possibilities carries
- Hashing text strings (not just files) using `.encode()` before passing them to `hashlib`
- Reading a file into a list of lines with `.splitlines()` and checking for membership with `in`
- Building a second custom-themed Tkinter GUI, reinforcing the pattern from an earlier project while adapting the visual design

---

## 🔮 Possible Future Improvements

- [ ] Expand the leaked-password list using a larger, real breach-derived word list (hashed, never stored in plain text)
- [ ] Add a live strength meter that updates as the user types, instead of only on button click
- [ ] Support checking multiple passwords from a file at once
- [ ] Add password generation — suggest a genuinely high-entropy password on request

---

## 📄 License

MIT — free to use, modify, and learn from.

---

*Built as part of a personal cybersecurity portfolio project of mine.
