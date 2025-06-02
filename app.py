import pandas as pd
import pickle as pk
import streamlit as st

# Load the model
try:
    with open('model.pkl', 'rb') as file:
        model = pk.load(file)
    
except Exception as e:
    st.error(f"Error loading model: {e}")
    model = None

# Streamlit app header
st.header('CAR PRICE PREDICTION ANALYSIS')

# Input fields for the user
name = st.selectbox('Select Car Brand',['Maruti', 'Skoda', 'Honda', 'Hyundai', 'Toyota', 'Ford', 'Renault',
       'Mahindra', 'Tata', 'Chevrolet', 'Datsun', 'Jeep', 'Mercedes-Benz',
       'Mitsubishi', 'Audi', 'Volkswagen', 'BMW', 'Nissan', 'Lexus',
       'Jaguar', 'Land', 'MG', 'Volvo', 'Daewoo', 'Kia', 'Fiat', 'Force',
       'Ambassador', 'Ashok', 'Isuzu', 'Opel'])  # Example brands
year = st.slider('Car Manufactured Year', 1994, 2024)
km_driven = st.slider('No Of Kms Driven', 11, 200000)
fuel = st.selectbox('Fuel Type', ['Petrol', 'Diesel','LPG', 'CNG'])
seller_type = st.selectbox('Seller Type', ['Individual', 'Dealer','Trustmark Dealer'])
transmission = st.selectbox('Transmission Type', ['Manual', 'Automatic'])
owner = st.selectbox('Owner Type', ['First Owner', 'Second Owner', 'Third Owner',
       'Fourth & Above Owner', 'Test Drive Car'])
mileage = st.slider('Car Mileage (kmpl)', 10, 40)
engine = st.slider('Engine capacity (cc)', 700, 5000)
max_power = st.slider('Max Power (bhp)', 0, 200)
seats = st.slider('No Of Seats', 2, 10)

# Prediction button
if st.button("Predict"):
    if model is not None:
        # Prepare input data with the correct number of features
        input_data_model = pd.DataFrame([[year, km_driven, mileage, engine, max_power, seats]], 
                                        columns=['year', 'km_driven', 'mileage', 'engine', 'max_power', 'seats'])

        # Check the model has the predict function
        if hasattr(model, 'predict'):
            try:
                # Predict car price
                car_price = model.predict(input_data_model)
                st.success(f"The Car Price Is Going To Be ₹{car_price[0]:,.2f}")
            except Exception as e:
                st.error(f"Prediction error: {e}")
        else:
            st.error("The model does not support prediction.")
    else:
        st.error("Model is not loaded.")


        







    
    