# Flask library
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
    url_for)

import pandas as pd
import pymysql
import operator

import taxpackage.salary as tx


# Flask setup
app = Flask(__name__)  # create the flask app


@app.route("/")
def home():
    return render_template("salary.html")


@app.route("/salary", methods=["GET", "POST"])
def salary():

    if request.method == 'POST':  # this block is only entered when the form is submitted
        income = float(request.form["incomeInput"])
        print(request.form["incomeInput"])
        tax = float(tx.tax_salary(income))
        percent = "%.2f" % round((tax/income), 2)
        return render_template("salary_return.html", tax=tax, income=income, percent=percent)

    return render_template("salary.html")


@app.route("/bonus", methods=["GET", "POST"])
def bonus():

    if request.method == 'POST':  # this block is only entered when the form is submitted
        income = float(request.form["incomeInput"])
        bonus = float(request.form["lumpsumInput"])
        rate = tx.tax_bonus(income, bonus)
        tax = bonus*(rate/100)
        return render_template("bonus_return.html", income=income, bonus=bonus, rate=rate, tax=tax)

    return render_template("bonus.html")


if __name__ == "__main__":
    # run app in debug mode in port 5000
    app.run(debug=True, host='0.0.0.0', port=8070)
