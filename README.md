# Finance-Advisor
Finance Advisor is an 
application that provides users with a suggested amount they should spend on various expenses based on their city, card type, and expense type. The application leverages a machine learning model trained on a dataset of recorded expenditures to make predictions.

**Features**

- Predicts the suggested spending amount based on user input
- Uses a neural network model for predictions
- Flask-based API for easy interaction with the model

**Installation**

**Prerequisites**

- Python 3.7 or higher
- Python package installer

**Clone the Repository**

git clone https://github.com/ayush0648/finance-advisor.git
cd finance-advisor

**Install Required Libraries**

pip install -r requirements.txt

**Usage**
**Start the Flask Application**

python finance_advisor.py

**Predictions**

Use a curl command on your powershell command line. Here's an example you can copy and paste:
Invoke-WebRequest -Uri "http://127.0.0.1:5000/predict" `
    -Method POST `
    -ContentType "application/json" `
    -Body '{"City": "Greater Mumbai", "Card Type": "Gold", "Exp Type": "Grocery"}'

**Model Details**

The machine learning model is a simple neural network implemented in PyTorch. The model takes categorical features (City, Card Type, Exp Type) as input and predicts the suggested amount for spending.

**Limitations**

The model can only predict with locations and card types provided in the dataset. More input on the dataset is required.

**Dataset Used:** https://www.kaggle.com/datasets/thedevastator/analyzing-credit-card-spending-habits-in-india?resource=download
