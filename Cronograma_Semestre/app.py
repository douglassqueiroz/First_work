from flask import Flask, render_template


meu_app = Flask(__name__)

@meu_app.route('/first_page')
def principal():
    return render_template('first_page.html')
    
@meu_app.route('/second_page')    
def second_page():
    return render_template('second_page.html')