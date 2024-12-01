from flask import Flask, render_template, request
from Py.passwords import generar_password as generate_pwd

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/generar_password', methods=['GET', 'POST'])
def generar_password():
    if request.method == 'POST':
        app_name = request.form.get('app_name')
        password = generate_pwd()
        print(f"Password generada: {password}")  # Para debug
        return render_template('password.html', password=password, app_name=app_name)
    return render_template('password.html')

if __name__ == '__main__':
    app.run(debug=True)
