from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')
    

@app.route('/suma', methods=['GET', 'POST'])
def suma():
    resultado = None
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        resultado = int(num1) + int(num2)
    return render_template('suma.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
