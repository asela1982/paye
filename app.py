# Flask library
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect,
url_for)

import taxpackage.salary as tx
import taxpackage


# Flask setup
app = Flask(__name__) # create the flask app


@app.route("/")
def home():
    return render_template("salary.html")


@app.route("/salary", methods=["GET", "POST"])
def salary():

    if request.method == 'POST': #this block is only entered when the form is submitted
        income = int(request.form["incomeInput"])
        tax = int(tx.tax_salary(income))
        percent = "%.2f" % round((tax/income),2)
        return render_template("salary_return.html",tax = tax, income = income, percent= percent)

    return render_template("salary.html")


@app.route("/bonus", methods=["GET", "POST"])
def bonus():

    if request.method == 'POST': #this block is only entered when the form is submitted
        income = int(request.form["incomeInput"])
        bonus = int(request.form["lumpsumInput"])
        rate = int(tx.tax_bonus(income,bonus))
        return render_template("bonus_return.html",rate = rate)

    return render_template("bonus.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080) #run app in debug mode in port 5000