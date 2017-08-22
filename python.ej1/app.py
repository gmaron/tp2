# Aqui se listan los imports
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

# Define la ruta con la que se ingresara desde el browser
@app.route('/')
def index():
    return render_template('form.html')

# Define la ruta y metodo con el que se debe llegar a este endpoint
@app.route('/form', methods = ['POST'])
def action_form():

    if request.method == 'POST':
        data = request.form
        nombre = data["nombre"]
        return render_template('response.html', nombre=nombre)

if __name__ == "__main__":
    # Define HOST y PUERTO para accerder
    app.run(host='localhost', port=80)