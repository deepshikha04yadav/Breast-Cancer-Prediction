# Breast-Cancer-Prediction

This project is a web application built using Flask that predicts whether a tumor is malignant or benign based on various features from a breast cancer dataset. The prediction is made using a trained machine learning model.

Features
Input 30 features related to tumor cell characteristics.

Predicts if the tumor is malignant or benign.

Simple, user-friendly web interface built using HTML and Flask.

Backend model built using Scikit-learn and saved as a .pkl file.

Directory Structure
bash
Copy
Edit
Prediction/
├── model.pkl              # Trained machine learning model (pickled)
├── app.py                  # Flask backend application
├── templates/
│   └── index.html          # Frontend HTML form
├── Cancer Prediction.ipynb # Jupyter Notebook (training and EDA)
Requirements
Python 3.10+

Flask

scikit-learn

numpy

pandas

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/your-username/breast-cancer-predictor.git
cd breast-cancer-predictor
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the Flask app:

bash
Copy
Edit
python pre.py
Open your browser and go to:

cpp
Copy
Edit
http://127.0.0.1:5000
How it Works
The app takes 30 numerical inputs from a form (based on breast cancer cell features).

These inputs are passed to a trained machine learning model (like RandomForest or DecisionTree).

The model returns a prediction: Malignant or Benign.

Note
This is a development server. For production, consider using a production-ready WSGI server like Gunicorn or uWSGI.

License
MIT License
