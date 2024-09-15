from flask import Flask, request, render_template
import pickle
import numpy as np
app = Flask(__name__)
with open('loan_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)
@app.route('/')
def home():
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    age = float(request.form['age'])
    income = float(request.form['income'])
    loan_amount = float(request.form['loan_amount'])
    credit_score = float(request.form['credit_score'])

    features = np.array([[age, income, loan_amount, credit_score]])
    prediction = model.predict(features)

    result = 'Approved' if prediction[0] == 1 else 'Denied'
    return render_template('result.html', result=result)
if __name__ == '__main__':
    app.run(debug=True)
