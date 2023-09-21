import streamlit as st
from Chronic_disease_prediction import DiseasePrediction  # Replace 'your_module' with the actual module name

dp = DiseasePrediction(model_name='decision_tree')  # Initialize the DiseasePrediction class with the desired model name

st.title("Disease Prediction App")

# Create input widgets
symptoms = st.text_area("Enter symptoms (comma-separated):")
model_choice = st.selectbox("Select a model:", ["decision_tree", "random_forest", "mnb"])  # List available models

if st.button("Predict"):
    # Use the DiseasePrediction instance to make predictions
    result = dp.make_prediction(saved_model_name=model_choice, test_data=symptoms)

    # Display the prediction result
    st.write("Predicted Disease:", result)
