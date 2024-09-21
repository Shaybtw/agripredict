import streamlit as st

# Set the title and some page configurations
st.set_page_config(page_title="AgriPredict: Crop Prediction tool", page_icon="🌾")

# Title
st.title("🌾 AgriPredict: Crop Prediction Tool")

# Create a sidebar for better organization
st.sidebar.header("Input Parameters")

# Crop Type Selection
crop_type = st.sidebar.selectbox("Select Crop Type:", ["Wheat", "Maize", "Rice\Paddy", "Potatos", "Sorghum","Cassava","Sweet Potato","Plantains","Yams"])

# Pesticide Quantity Input
pesticide_tonnes = st.sidebar.number_input("Enter Pesticide Quantity (in tonnes):", min_value=0.0)

# Average Rainfall Input
avg_rainfall = st.sidebar.number_input("Enter Average Rainfall (in mm):", min_value=0.0)

# Average Temperature Input
avg_temperature = st.sidebar.number_input("Enter Average Temperature (in °C):", min_value=-50.0, max_value=50.0)

# Prediction Button
if st.sidebar.button("Predict"):
    # Placeholder for prediction logic
    st.markdown("### Prediction Results")
    st.write(f"**Crop Type:** {crop_type}")
    st.write(f"**Pesticide Quantity:** {pesticide_tonnes} tonnes")
    st.write(f"**Average Rainfall:** {avg_rainfall} mm")
    st.write(f"**Average Temperature:** {avg_temperature} °C")
    
    st.write("#  Predicted Yield: 3000 kg/ha")  # Placeholder for prediction output
    # Suggestion for the user according to the kind of crop that he is growing.
if (crop_type == "Wheat"):
    st.markdown(f"The Ideal condition for the wheat crop is:")
    st.markdown(f"Ideal Pesticide Quantity: 1.0 - 2.0 tonns")
    st.markdown(f"Ideal Rainfall: 400-600mm")
    st.markdown(f"IdeaL temperature: 15 - 25 °C")
elif(crop_type == "Maize"):
    st.markdown(f"The Ideal condition for the Maize crop is:")
    st.markdown(f"Ideal Pesticide Quantity:1.5 - 2.5 tonns")
    st.markdown(f"Ideal Rainfall: 500-800mm ")
    st.markdown(f"IdeaL temperature: 20 - 30 °C")
elif(crop_type == "Rice\Paddy"):
    st.markdown(f"The Ideal condition for Rice/Paddy crop is")
    st.markdown(f"Ideal Pesticide Quantity: 1.0 - 2.0 tonnes")
    st.markdown(f"Ideal Rainfall: 1000 - 2000 mm ")
    st.markdown(f"IdeaL temperature: 20 - 35 °C")
elif(crop_type == "Potatos"):
    st.markdown(f"The Ideal condition for Potatos are:")
    st.markdown(f"Ideal Pesticide Quantity: 1.0 - 1.5 tonnes")
    st.markdown(f"Ideal Rainfall: 600 - 800 mm")
    st.markdown(f"IdeaL temperature: 15 - 20 °C")
elif(crop_type == "Plantains"):
    st.markdown(f"The Ideal condition for Plantains is:")
    st.markdown(f"Ideal Pesticide Quantity:1.2 - 1.7 tonnes ")
    st.markdown(f"Ideal Rainfall: 300-500mm ")
    st.markdown(f"IdeaL temperature: 25-35°C")
elif(crop_type == "Cassava"):
    st.markdown(f"The Ideal condition for Cassava is")
    st.markdown(f"Ideal Pesticide Quantity: 1.0-1.5 tonnes")
    st.markdown(f"Ideal Rainfall:800-1200mm ")
    st.markdown(f"IdeaL temperature: 25-35°C")
elif(crop_type == "Sweer Potato"):
    st.markdown(f"The Ideal condition for sweet potatos is")
    st.markdown(f"Ideal Pesticide Quantity: 0.5-1.0")
    st.markdown(f"Ideal Rainfall:500-700mm")
    st.markdown(f"IdeaL temperature:20-30°C")
elif(crop_type == "Sorghum"):
    st.markdown(f"The Ideal condition for is this ")
    st.markdown(f"Ideal Pesticide Quantity: 0.5 - 1.0 tonnes ")
    st.markdown(f"Ideal Rainfall: 400 - 600 mm")
    st.markdown(f"IdeaL temperature: 20 - 30 °C")
elif(crop_type == "Yams"):
    st.markdown(f"The Ideal condition for Yams are")
    st.markdown(f"Ideal Pesticide Quantity: 0.2-0.5 tonnes")
    st.markdown(f"Ideal Rainfall: 300-500mm")
    st.markdown(f"IdeaL temperature: 20-25°C")
else:
    st.markup(".")
st.markdown("---")
st.markdown("### About AgriPredict")
st.write(
    "AgriPredict is a prediction tool designed to help farmers determine the best crop "
    "to plant based on the given parameters. Use it to make informed decisions for better yields!"
)

# Add some colorful styling
st.markdown(
    """
    <style>
    .stButton {
        background-color: #4CAF50;  /* Green */
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
    }
    .stButton:hover {
        background-color: #45a049;  /* Darker green */
    }
    </style>
    """,
    unsafe_allow_html=True
)

 