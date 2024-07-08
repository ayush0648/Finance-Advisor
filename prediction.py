import pandas as pd
import joblib

# Load the pre-trained model
model = joblib.load('credit_card_spending_model.pkl')

# Define function to predict expense
def predict_expense(city, card_type, exp_type):
    # Prepare input data
    data = {
        'City': [city],
        'Card Type': [card_type],
        'Exp Type': [exp_type]
    }
    df = pd.DataFrame(data)
    
    # Predict expense
    prediction = model.predict(df)[0]
    
    # Format the output
    result = f"For a user in {city} with a {card_type} card, the suggested amount to spend on {exp_type} is ₹{prediction:.2f}."
    
    return result

# Example usage
city = "Greater Mumbai"
card_type = "Silver"
exp_type = "Bills"

predicted_output = predict_expense(city, card_type, exp_type)
print(predicted_output)