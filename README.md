🔐 Ultimate Password Checker & Generator
This is a secure and interactive web tool built with Streamlit to help users:

✅ Check the strength of their passwords using entropy-based scoring and custom rules.

🔑 Generate strong, secure passwords with customizable length.

⚙️ Add advanced custom rules (like emojis) to enforce password policies.

📋 Copy generated passwords securely to the clipboard.

🔍 Learn about password security and avoid common pitfalls.

🚀 Features
Password Strength Checker
Evaluates passwords against multiple criteria:

Length

Uppercase & lowercase mix

Numeric and special characters

Blacklisted (commonly used) passwords

Custom rules (e.g., emojis)

Entropy estimation (bit strength)

Password Generator
Quickly generate strong passwords with adjustable length (8–32 characters).

Clipboard Copy & Reveal Password
Securely copy the password to clipboard or reveal it for manual use.

Modular & Extensible
Easily add custom validation rules and extend password policies.

🧠 Password Scoring System

Criteria	Score
Length ≥ 12	+2
Length 8–11	+1
Upper & Lowercase mix	+1
Contains at least one digit (0–9)	+1
Contains special characters	+2
Passes custom rule (e.g., emoji)	+1
Maximum Score: 7

🛠️ Tech Stack
Streamlit – UI and interactive widgets

Python – Core logic

Regex – Pattern matching for validation

Pyperclip – Copy-to-clipboard support

Math – Entropy estimation

