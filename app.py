import streamlit as st
import pickle

model = pickle.load(open('model.pkl','rb'))
st.title("House Price Prediction")

area = st.number_input("Area")
bedrooms = st.number_input("Bedrooms")
bathrooms = st.number_input("Bathrooms")
stories = st.number_input("Stories")
parking = st.number_input("Parking")

if st.button("Predict"):
    prediction =  model.predict(
        [[area,bedrooms,bathrooms,stories,parking]]
    )

    st.write(
        f"Predicted Price: {prediction[0]}"
    )