# Lugar para poder los imports de python
import mysql.connector
from flask import Flask
from flask import render_template
from flask import request
import os

app = Flask(__name__)

# app.route define la ruta donde se debe acceder

@app.route('/')
def hello_world():
    user = os.environ['TP_SQL_USER']
    password=os.environ['TP_SQL_PASS']
    database=os.environ['TP_DATABASE']
    cnx = mysql.connector.connect(user=user, password=password,
                              host='127.0.0.1',
                              database=database)

    cursor = cnx.cursor()
    cursor.execute ("show databases;")
    row = cursor.fetchall()
    print("aviable databases:", row)
    cursor.close()
    cnx.close()
    return render_template('form.html')

@app.route('/form')
def action_form(nom=None):
    nom = request.args["nombre"]
    return render_template('response.html', name=nom)

hello_world()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=1111)