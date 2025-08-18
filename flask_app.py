# app.py
from flask import Flask, render_template, request
from model import regressor_model

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def house_view():
    if request.method == 'GET':
        return render_template("house.html")
    elif request.method == 'POST':
        sqft = float(request.form["sqft"])
        bedroom = float(request.form["bedroom"])
        age = float(request.form["age"])
        op_array = regressor_model.predict([[sqft, bedroom, age]])
        y_pred = round(op_array[0], 2)
        return render_template("result.html", predicted_price=y_pred)


if __name__ == '__main__':
    app.run(debug=True)