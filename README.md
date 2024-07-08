# Finance-Advisor

This project implements a financial advisory system that predicts suggested amounts for expenses based on user inputs using machine learning. It includes two main components: a model training script and a web-based interface to interact with the trained model.

**Features**

- Model Training: Trains a machine learning model on historical credit card spending data to predict suggested expense amounts based on city, card type, and expense type.
- Persistence: Uses joblib to save and load the trained model for efficient prediction.

**Installation**

**Prerequisites**

- Python 3.7 or higher
- Python package installer

**Clone the Repository**

git clone https://github.com/ayush0648/Finance-Advisor.git
cd Finance-Advisor

**Install Required Libraries**

pip install -r requirements.txt

**Usage**

**Train the Model**

python model.py

**Run the Prediction file**

python prediction.py

You can change the parameters in the given code to get an output based on your needs.


**Limitations**

The model can only predict with locations and card types provided in the dataset. More input on the dataset is required.

**Dataset Used:** https://www.kaggle.com/datasets/thedevastator/analyzing-credit-card-spending-habits-in-india?resource=download
