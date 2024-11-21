from flask import Flask, render_template, request, redirect, url_for, flash

from atm_machine.machine import ATM
app = Flask(__name__)

app.secret_key = "atm_project_secret_key"

atm = ATM(pin="1234", balance=1000)

@app.route("/")
def home():
    return render_template("home.html")  
@app.route("/menu")
def menu():
    return render_template("menu.html", balance=atm.balance)  

@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if request.method == "POST":
        amount = float(request.form["amount"])
        message = atm.deposit(amount)
        flash(message)
        return redirect(url_for("menu"))  
    return render_template("deposit.html")

@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if request.method == "POST":
        amount = float(request.form["amount"])
        message = atm.withdraw(amount)
        flash(message)
        return redirect(url_for("menu")) 
    return render_template("withdraw.html")

@app.route("/balance")
def balance():
    balance = atm.check_balance()
    return render_template("balance.html", balance=balance)

if __name__ == "__main__":
    app.run(debug=True)
