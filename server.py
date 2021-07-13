from flask import Flask, render_template, request, redirect, session
import random


app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'

@app.route('/')
def index():
    if 'winning_number' not in session:
        session['winning_number'] = random.randint(1, 11)
        session['game_status'] = 'no_guess'
    
    print(session['winning_number'])

    return render_template('index.html')

@app.route('/guess_a_number', methods=['POST'])
def guess_a_number():

    # hasn't guessed yet => 'no_guess'
    # guess is too high -> 'too_high'
    # guess is too low -> 'too_low'
    # guess is exact -> 'exact'

    
    
    if session['winning_number'] == int(request.form['number_guess']):
        session['game_status'] = 'exact'

    elif session['winning_number'] < int(request.form['number_guess']):
        session['game_status'] = 'too_high'

    else:
        session['game_status'] = 'too_low'

    return redirect('/')

@app.route('/reset_click', methods=['POST'])
def reset_click():
    session.clear()
    session.modified = True
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)