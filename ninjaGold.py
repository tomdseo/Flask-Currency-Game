from flask import Flask, render_template, request, redirect, session
import random
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'keep it secret'

@app.route('/')
def show_index():
    if not (session.get('farm') or session.get('cave') or session.get('house') or session.get('casino') or session.get('total')):
        session['history'] = []
        session['total'] = 0
        session['update'] = False
    return render_template("index.html")

@app.route('/process_money', methods=["POST"])
def process_money():
    # PART 1: adding to total
    if request.form['building'] == 'farm':
        randGold = random.randint(10, 20)
        session['total'] += randGold
        print("total", session['total'])
        output = "Earned " + str(randGold) + " gold from the farm!"
        session['history'].append(output)
    if request.form['building'] == 'cave':
        randGold = random.randint(5, 10)
        session['total'] += randGold
        print("total", session['total'])
        output = "Earned " + str(randGold) + " gold from the cave!"
        session['history'].append(output)
    if request.form['building'] == 'house':
        randGold = random.randint(2, 5)
        session['total'] += randGold
        print("total", session['total'])
        output = "Earned " + str(randGold) + " gold from the house!"
        session['history'].append(output)
    if request.form['building'] == 'casino':
        switch = random.randint(0, 1) #0 for subtraction, 1 for addition
        randGold = random.randint(0, 50)
        if switch == 1:
            session['total'] += randGold
            output = "Entered a casino and won " + str(randGold) + "!"
            session['history'].append(output)
        else:
            session['total'] -= randGold
            if session['total'] < 0:
                session['total'] = 0
            output = "Entered a casino and lost " + str(randGold) + " golds... Ouch.."
            session['history'].append(output)
        print("total", session['total'])


    return redirect("/")

@app.route('/restart', methods=["POST"])
def restart():
    session['history'] = []
    session['total'] = 0
    session['update'] = False

    return redirect("/")

if __name__ == '__main__':
    app.run(debug = True)