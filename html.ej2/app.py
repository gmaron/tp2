# Lugar para poder los imports de python
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# app.route define la ruta donde se debe acceder
@app.route('/')
def hello_world():
    return render_template('form.html')

@app.route('/form')
def action_form(nom=None):
    return render_template('response.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=1111)

    