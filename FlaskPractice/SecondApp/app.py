from flask import Flask, render_template, request
from Logic.intermedio.passwords import generar_password as generate_pwd

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/generar_password', methods = ['GET', 'POST'])
def generar_password():
    if request.method == 'POST':
        generate_pwd()
    return render_template('generar_password.html')

if __name__ == '__main__':
    app.run(debug=True)
