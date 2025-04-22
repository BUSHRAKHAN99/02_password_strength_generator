import streamlit as st
import re
import random
import string
import math
import pyperclip  # Clipboard support

# --- CONFIGURATION ---
st.set_page_config(page_title="🔐 Secure Password Tool", layout="centered")
st.title("🔐 Ultimate Password Checker & Generator")

# Blacklist common passwords
blacklist = [
    "password", "123456", "password123", "qwerty", "letmein", "admin", "welcome", "iloveyou", "123456789", "abc123"
]

# Check password entropy
def estimate_entropy(password):
    charset = 0
    if re.search(r"[a-z]", password): charset += 26
    if re.search(r"[A-Z]", password): charset += 26
    if re.search(r"\d", password): charset += 10
    if re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?/~\\-]", password): charset += 32
    entropy = len(password) * math.log2(charset) if charset else 0
    return entropy

# Password strength scoring
def check_password_strength(password, custom_rules=None):
    score = 0
    feedback = []

    if password.lower() in blacklist:
        feedback.append("❌ This password is commonly used. Please choose a more unique one.")
        return 0, feedback, 0

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0–9).")

    if re.search(r"[!@#$%^&*()_+{}\[\]:;<>,.?/~\\-]", password):
        score += 2
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    if custom_rules:
        for rule in custom_rules:
            if not re.search(rule['pattern'], password):
                feedback.append(f"❌ {rule['message']}")
            else:
                score += 1

    entropy = estimate_entropy(password)
    return score, feedback, entropy

# Password Generator
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()"
    return ''.join(random.choice(chars) for _ in range(length))

# --- PASSWORD CHECKER UI ---
password = st.text_input("🔍 Enter your password to check:", type="password")

# Custom Rule Example (emoji rule)
with st.expander("⚙️ Advanced Rules"):
    use_custom_rule = st.checkbox("Require at least one emoji (😎, 🔥, ❤️, etc.)")
    custom_rules = []
    if use_custom_rule:
        custom_rules.append({
            "pattern": r"[😎🔥❤️💯✨🎉]",
            "message": "Include at least one emoji (😎, 🔥, ❤️, etc.)"
        })

if password:
    score, feedback, entropy = check_password_strength(password, custom_rules)

    # Strength Bar
    st.subheader("🧠 Password Strength")
    st.progress(min(score / 7, 1.0))  # 7 is max score with custom rules

    # Score Feedback
    if score >= 6:
        st.success("✅ Very Strong Password!")
    elif 4 <= score < 6:
        st.warning("⚠️ Decent Password - could be stronger.")
    else:
        st.error("❌ Weak Password - improve using the tips below.")

    for f in feedback:
        st.write(f)

    st.caption(f"🔐 Entropy Estimate: **{entropy:.2f} bits**")

st.markdown("---")

# --- PASSWORD GENERATOR UI ---
st.subheader("🔑 Password Generator")

col1, col2 = st.columns([3, 1])
with col1:
    length = st.slider("Password length", 8, 32, 12)
with col2:
    if st.button("Generate Password"):
        new_pass = generate_password(length)
        st.session_state["generated_password"] = new_pass

# Display Generated Password
if "generated_password" in st.session_state:
    gen_pw = st.session_state["generated_password"]
    st.text_input("Generated Password", value=gen_pw, type="password")

    col3, col4 = st.columns([1, 1])
    with col3:
        if st.button("👁️ Show Password"):
            st.code(gen_pw)
    with col4:
        if st.button("📋 Copy to Clipboard"):
            pyperclip.copy(gen_pw)
            st.success("Copied!")

# Optional placeholder for breach checking
st.markdown("---")
st.info("🔎 Want to check if your password was leaked in a data breach? Try using the [HaveIBeenPwned API](https://haveibeenpwned.com/API/v3).")
