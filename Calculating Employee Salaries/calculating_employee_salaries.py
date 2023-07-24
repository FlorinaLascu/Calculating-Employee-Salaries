import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from flask import Flask, request, jsonify
from flask import render_template

app = Flask(__name__, template_folder='templates')

df = pd.read_csv("salaries_dataset.csv", sep=";")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    experience_level = float(data['experience_level'])

    # Transform the input data
    polynomial_regression = PolynomialFeatures(degree=4)
    x_polynomial = polynomial_regression.fit_transform([[experience_level]])

    # Create the feature matrix X
    X = df.drop('salary', axis=1)  # Exclude the target variable
    X = polynomial_regression.transform(X)

    # Fit the LinearRegression model
    reg = LinearRegression()
    reg.fit(X, df['salary'])

    # Make the prediction
    predicted_salary = reg.predict(x_polynomial)

    response = {'salary': float(predicted_salary[0])}
    return jsonify(response)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5003)

