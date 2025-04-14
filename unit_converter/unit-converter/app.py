import streamlit as st

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(page_title="Hooria's Unit Converter", page_icon="📏", layout="centered")

# -------------------------
# Function to Convert Units
# -------------------------
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meters_kilometers": 0.001,
        "kilometers_meters": 1000,
        "grams_kilograms": 0.001,
        "kilograms_grams": 1000
    }
    
    key = f"{unit_from}_{unit_to}"
    if key in conversions:
        return value * conversions[key]
    else:
        return "❌ Conversion not supported"

# -------------------------
# UI Design
# -------------------------
st.markdown("<h1 style='text-align: center; color: teal;'>🔁 Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Made with ❤️ by <strong>Hooria Khan</strong></p>", unsafe_allow_html=True)
st.markdown("---")

st.subheader("🔢 Enter a value to convert:")

value = st.number_input("Value:", min_value=0.0, format="%.2f")

col1, col2 = st.columns(2)
with col1:
    unit_from = st.selectbox("Convert from:", ["meters", "kilometers", "grams", "kilograms"])
with col2:
    unit_to = st.selectbox("Convert to:", ["meters", "kilometers", "grams", "kilograms"])

# -------------------------
# Conversion Button
# -------------------------
if st.button("🚀 Convert Now"):
    result = convert_units(value, unit_from, unit_to)
    if isinstance(result, float):
        st.success(f"✅ Converted value: **{result:.4f} {unit_to}**")
    else:
        st.error(result)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 12px;'>© 2025 Hooria's App | Built using Streamlit</p>", unsafe_allow_html=True)
