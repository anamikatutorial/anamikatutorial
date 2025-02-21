from flask import Flask, render_template, request
import pickle
import pandas as pd
import numpy as np

# Load the Random Forest Classifier model
filename = 'pickle.pkl'
model = pickle.load(open(filename, 'rb'))

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/symptoms')
def symptoms():
    return render_template('symptoms.html')
@app.route('/diet')
def diet():
    return render_template('diet.html')    

@app.route('/index')
def index():
    return render_template('index.html')



@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Extracting the form data and validating
            Age = request.form.get('Age')
            Gender = request.form.get('Gender')
            Heartrate = request.form.get('Heartrate')
            SystolicBP = request.form.get('SystolicBP')
            DiastolicBP = request.form.get('DiastolicBP')
            Bloodsugar = request.form.get('Bloodsugar')
            CKMB = request.form.get('CKMB')
            Troponin = request.form.get('Troponin')

            # Ensure all required values are provided
            if not Age or not Gender or not Heartrate or not SystolicBP or not DiastolicBP or not Bloodsugar or not CKMB or not Troponin:
                return render_template('index.html', error="Please fill in all fields.")

            # Convert numerical values to appropriate types (handling None/empty values)
            Age = int(Age) if Age else 0
            Heartrate = float(Heartrate) if Heartrate else 0.0
            SystolicBP = int(SystolicBP) if SystolicBP else 0
            DiastolicBP = int(DiastolicBP) if DiastolicBP else 0
            Bloodsugar = float(Bloodsugar) if Bloodsugar else 0.0
            CKMB = int(CKMB) if CKMB else 0.0
            Troponin = int(Troponin) if Troponin else 0.0

            # Convert categorical data like 'Gender' into numerical representation if necessary
            # Assuming Gender is either 'Male' or 'Female', you may need to map this
            Gender = 1 if Gender == 'Male' else 0  # For example, map 'Male' to 1 and 'Female' to 0

            # Prepare the data for prediction
            data = np.array([[Age, Gender, Heartrate, SystolicBP, DiastolicBP, Bloodsugar, CKMB, Troponin]])

            # Make the prediction
            my_prediction = model.predict(data)
            
            # Returning the prediction result
            return render_template('show.html',Age=Age, Gender=Gender, Heartrate=Heartrate, 
                               SystolicBP=SystolicBP, DiastolicBP=DiastolicBP, Bloodsugar=Bloodsugar, 
                               CKMB=CKMB, Troponin=Troponin, prediction=my_prediction[0])

        except Exception as e:
            return render_template('index.html', error=f"An error occurred: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
