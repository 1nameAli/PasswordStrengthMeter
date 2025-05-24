import re
import random
import string
import streamlit as st

# Streamlit page configuration
st.set_page_config(page_title="Password Strength Meter", layout="centered")

# Title
st.title("🔐 Password Strength Meter")

# --- Password Strength Checker ---
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number.")

    if re.search(r"[!@#$%^&*()_+=\-{}[\]:;\"'<>,.?/\\|]", password):
        score += 1
    else:
        feedback.append("❌ Add at least one special character.")

    if score == 4:
        return "✅ Strong", "green", feedback
    elif score == 3:
        return "⚠️ Moderate", "orange", feedback
    else:
        return "❌ Weak", "red", feedback

# --- Password Generator ---
def generate_strong_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()_+"
    return ''.join(random.choice(chars) for _ in range(length))

# --- UI Input ---
password = st.text_input("Enter your password:", type="password")

# --- Check Password Button ---
if st.button("Check Strength"):
    if password:
        strength, color, suggestions = check_password_strength(password)
        st.markdown(f"<h4 style='color:{color}'>{strength} Password</h4>", unsafe_allow_html=True)
        if suggestions:
            for tip in suggestions:
                st.info(tip)
    else:
        st.warning("Please enter a password.")

# --- Generate Password ---
st.markdown("---")
if st.button("Generate Strong Password"):
    strong_pass = generate_strong_password()
    st.text_input("Generated Password:", value=strong_pass, key="generated_pass", help="You can copy this manually.")
    st.success("Password generated! Click the field above to copy it.")
