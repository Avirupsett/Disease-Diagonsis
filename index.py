import pandas as pd
from flask import Flask, jsonify, request
from joblib import load

model=load("Prediction_Deases_final_1.joblib")

app=Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def home():
    return "<h2>Flask Vercel</h2>"

@app.route('/predict', methods=['POST'])
def predict():
    # get data
    data = request.get_json(force=True)

    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'results': int(result[0])}

    # return data
    return jsonify(results=output)
    

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0",port= 5000)