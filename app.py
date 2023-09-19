from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])

def calcular():
    try:
        n1 = float(request.form['n1'])
        n2 = float(request.form['n2'])
        opp = request.form['opp']

        if opp == 'Suma':
            R = n1 + n2
        elif opp == 'Resta':
            R = n1 - n2
        elif opp == 'Multiplicación':
            R = n1*n2
        elif opp == 'Division':
            R = n1/n2
        elif opp == 'Raiz':
            R = n1**(1/n2)
        elif opp == 'Potencia':
            R = n1**n2
        else:
            R = 'ERROR, NO VALIDO'
        return render_template('resultado.html', R=R)
    except ZeroDivisionError:
        return render_template('resultado.html', R='No se puede dividir por cero')

if __name__ == '__main__':
    app.run(debug=True)