from flask import Flask, redirect, request, render_template, jsonify
import pandas as pandas
import json, pickle, sklearn, numpy
from bson import json_util

# Model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/assessment', methods=["GET", "POST"])
def grade():
    print(request.method)
    print(request.get_json())

    if request.method == "GET":
        return render_template('assessment.html')

    else:
        print(request.get_json())
        content = request.get_json()
        print(type(content))

        with open(f'random_forest_model.pkl', 'rb') as f:
            model = pickle.load(f)

        with open(f'scaler.pkl', 'rb') as scale:
            scaler = pickle.load(scale)

        #set up user input
        inputs = [[content['loanAmount'], content['income'], content['FICO'], content['yearsOfEmployement'], content[
            home'], 0, content['appType]]]
        inputs_scaled = scaler.transform(inputs)

        # run prediction
        predictions = model.predict(inputs_scaled)[0]

        # print the response
        return f"{predictions}"

@app.route("/repayment")
def repay():
    return render_template("repayment.html")

@app.route("/grade")
def page():
    return render_template("grade_data.html")

if __name__ == "__main__":
    app.run(debug=True)
