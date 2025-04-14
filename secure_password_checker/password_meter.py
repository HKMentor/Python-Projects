import streamlit as st
import random
import string
import re

# Function to calculate password strength
def calculate_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("🔹 Add at least 8 characters.")

    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("🔹 Include at least one uppercase letter.")

    if re.search(r'[0-9]', password):
        score += 1
    else:
        suggestions.append("🔹 Add at least one number.")

    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        suggestions.append("🔹 Add at least one special character (!@#$%^&*).")

    return score, suggestions

# Function to generate strong password
def generate_password():
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(12))

# Streamlit UI starts here
st.markdown("<h1 style='text-align: center; color: #6a1b9a;'>🔐 Password Strength Checker</h1>", unsafe_allow_html=True)

st.markdown("##### Developed with ❤️ by **Hooria Fatima**")
st.markdown("📷 Follow me on Instagram: [@hooria_codehub](https://www.instagram.com/hooria_codehub?igsh=ZWhvMmVucm5ueHBl)")
st.markdown("📷 Check Out My Python Github Code Projects: [HKMentor](https://github.com/HKMentor/Python-Projects)")


password = st.text_input("🔑 Enter your password below:", type="password")

if password:
    st.write("🔍 Checking your password strength...")
    score, suggestions = calculate_strength(password)

    st.markdown(f"### 💪 Password Strength Score: **{score} / 4**")

    if score == 4:
        st.success("✅ Strong Password! Great job 🎉")
    else:
        st.error("❌ Weak Password. Let's improve it together!")
        st.markdown("#### ✨ Suggestions to make it stronger:")
        for suggestion in suggestions:
            st.markdown(f"- {suggestion}")

        st.markdown("#### 💡 Here's a strong password you can use:")
        st.code(generate_password())

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Made with 💜 using Python & Streamlit</p>", unsafe_allow_html=True)
