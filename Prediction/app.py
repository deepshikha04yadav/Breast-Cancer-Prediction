from flask import Flask, request, render_template
import pickle
import numpy as np
app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

    fields = [
    'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean',
    'smoothness_mean', 'compactness_mean', 'concavity_mean', 'concave_point_mean',
    'symmetry_mean', 'fractal_dimension_mean',
    'radius_se', 'texture_se', 'perimeter_se', 'area_se', 'smoothness_se',
    'compactness_se', 'concavity_se', 'concave_point_se', 'symmetry_se', 'fractal_dimension_se',
    'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst', 'smoothness_worst',
    'compactness_worst', 'concavity_worst', 'concave_point_worst', 'symmetry_worst', 'fractal_dimension_worst'
]


@app.route('/')
def home():
    return render_template('index.html', fields=fields)  # Your HTML form

@app.route('/prediction', methods=['POST'])
def predict():
    try:
        # Extract all 30 features from form
        features = [
            float(request.form.get(field))
            for field in fields
        ]

        # Convert to NumPy array and predict
        prediction = model.predict([features])[0]
        result = "Malignant" if prediction == 0 else "Benign"

        return f"<h2>Prediction Result: {result}</h2>"

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
