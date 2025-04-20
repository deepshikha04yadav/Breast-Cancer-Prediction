# Breast-Cancer-Prediction

This project is a web application built using Flask that predicts whether a tumor is malignant or benign based on various features from a breast cancer dataset. The prediction is made using a trained machine learning model.

# Features
* Input 30 features related to tumor cell characteristics.
* Predicts if the tumor is malignant or benign.
* Simple, user-friendly web interface built using HTML and Flask.

Backend model built using Scikit-learn and saved as a .pkl file.

# Directory Structure

![image](https://github.com/user-attachments/assets/96ea97e8-8664-4e48-8ed5-2aa43ad88b42)



# Requirements
* Python 3.10+
* Flask

* scikit-learn

* numpy

* pandas

# Installation
1. Clone the repository:
   * git clone https://github.com/your-username/breast-cancer-predictor.git
   * cd breast-cancer-predictor

2. Install dependencies:
   * pip install -r requirements.txt

4. Run the Flask app:
   * python app.py

5. Open your browser and go to:
   * http://127.0.0.1:5000
# How it Works
* The app takes 30 numerical inputs from a form (based on breast cancer cell features).

* These inputs are passed to a trained machine learning model (like RandomForest or DecisionTree).

* The model returns a prediction: Malignant or Benign.

# Features Used
  * The model uses 30 diagnostic features including:

Mean, standard error, and worst-case values of:
radius, texture, perimeter, area, smoothness, compactness, concavity, concave points, symmetry, and fractal dimension.

# Warning
  * This is a development server.
  
  * Do NOT use in production without using a WSGI server (e.g., Gunicorn) and proper security measures.
  
  * The model may not generalize well for clinical use without further validation.

# Acknowledgements
  * Dataset: data.csv
  
  * Libraries: scikit-learn, Flask, pandas, Jupyter

