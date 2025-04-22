# 🔐 Ultimate Password Checker & Generator

This is a secure and interactive web tool built with **Streamlit** to help users:
- ✅ Check the strength of their passwords using entropy-based scoring and custom rules.
- 🔑 Generate strong, secure passwords with customizable length.
- ⚙️ Add advanced custom rules (like emojis) to enforce password policies.
- 📋 Copy generated passwords securely to the clipboard.
- 🔍 Learn about password security and avoid common pitfalls.

---

## 🚀 Features

- **Password Strength Checker**  
  Evaluates passwords against multiple criteria:
  - Length
  - Uppercase & lowercase mix
  - Numeric and special characters
  - Blacklisted (commonly used) passwords
  - Custom rules (e.g., emojis)
  - Entropy estimation (bit strength)

- **Password Generator**  
  Quickly generate strong passwords with adjustable length (8–32 characters).

- **Clipboard Copy & Reveal Password**  
  Securely copy the password to clipboard or reveal it for manual use.

- **Modular & Extensible**  
  Easily add custom validation rules and extend password policies.

---

## 🧠 Password Scoring System

| Criteria                              | Score |
|---------------------------------------|-------|
| Length ≥ 12                           | +2    |
| Length 8–11                           | +1    |
| Upper & Lowercase mix                | +1    |
| Contains at least one digit (0–9)    | +1    |
| Contains special characters          | +2    |
| Passes custom rule (e.g., emoji)     | +1    |

**Maximum Score**: 7

---

## 🛠️ Tech Stack

- **[Streamlit](https://streamlit.io/)** – UI and interactive widgets
- **Python** – Core logic
- **Regex** – Pattern matching for validation
- **Pyperclip** – Copy-to-clipboard support
- **Math** – Entropy estimation

---

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/password-checker-generator.git
cd password-checker-generator
```

### 2. Create a Virtual Environment (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
streamlit run app.py
```

---

## 📋 Requirements

Make sure you have these installed:

- Python 3.7+
- `streamlit`
- `pyperclip`

Create a `requirements.txt` with:
```txt
streamlit
pyperclip
```

---

## 📎 Screenshots

> _(You can add your screenshots here for visual demonstration)_

---

## 🔐 Security Note

This tool runs locally and does **not** store or transmit any passwords. For breach checking, consider using official APIs like [HaveIBeenPwned](https://haveibeenpwned.com/API/v3) separately and responsibly.

---

## 💡 Future Ideas

- Integrate real-time breach checking via HaveIBeenPwned API
- Option to save passwords to encrypted local storage
- Dark mode toggle
- Support for passphrases

---

