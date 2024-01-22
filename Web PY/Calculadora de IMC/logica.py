from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Obter os dados do formulário
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])

        # Calcular o IMC
        imc = peso / (altura ** 2)

        # Interpretar o resultado do IMC
        resultado = interpretar_imc(imc)

        # Renderizar o template com os resultados
        return render_template('resultado_imc.html', imc=imc, resultado=resultado)

    # Renderizar o formulário inicial
    return render_template('index.html')

def interpretar_imc(imc):
    if imc < 18.5:
        return 'Abaixo do peso'
    elif 18.5 <= imc < 24.9:
        return 'Peso normal'
    elif 25 <= imc < 29.9:
        return 'Sobrepeso'
    elif 30 <= imc < 34.9:
        return 'Obesidade grau 1'
    elif 35 <= imc < 39.9:
        return 'Obesidade grau 2'
    else:
        return 'Obesidade grau 3'

if __name__ == '__main__':
    app.run(debug=True)
