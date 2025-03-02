import streamlit as st

# Page config with title and icon
st.set_page_config(page_title="Unit Converter", page_icon="🌍", layout="centered")

# Sidebar for category selection
st.sidebar.title("⚙️ Settings")
category = st.sidebar.selectbox("Choose a category", ["Length", "Weight", "Time"])

# Title & Description
st.markdown(
    """
    <h1 style='text-align: center;'>🌍 Unit Converter</h1>
    <h3 style='text-align: center; color: grey;'>Convert Length, Weight, and Time Instantly</h3>
    <p style='text-align: center;'>Select a category, enter a value, and see the conversion in real-time!</p>
    """, unsafe_allow_html=True
)

# Define conversion function
def Convert(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.20462
        elif unit == "Pounds to Kilograms":
            return value / 2.20462
    elif category == "Time":
        if unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Seconds to Minutes":
            return value / 60
    return None

# Conversion unit selection
col1, col2 = st.columns([1, 1])
with col1:
    if category == "Length":
        unit = st.selectbox("🔗 Choose a unit", ["Kilometers to Miles", "Miles to Kilometers"])
    elif category == "Weight":
        unit = st.selectbox("⚖️ Choose a unit", ["Kilograms to Pounds", "Pounds to Kilograms"])
    elif category == "Time":
        unit = st.selectbox("⏳ Choose a unit", ["Minutes to Seconds", "Seconds to Minutes"])

# Input field for value
with col2:
    value = st.number_input("📥 Enter value", min_value=0.0, format="%.2f")

# Perform conversion and display result in real-time
if value:
    result = Convert(category, value, unit)
    if result is not None:
        st.markdown(
            f"""
            <div style='text-align: center; font-size: 24px; padding: 15px; border-radius: 10px; 
            background-color: #4CAF50; color: white; font-weight: bold;'>
            ✅ Converted Value: {result:.2f}
            </div>
            """, unsafe_allow_html=True
        )
    else:
        st.error("⚠️ Invalid conversion selected!")

# Footer
st.markdown("<br><hr><p style='text-align: center;'>Built with ❤️ using Streamlit</p>", unsafe_allow_html=True)
