from flask import Flask, request, render_template
from calculadora import *


def create_app(config):
    app = Flask(__name__)

    app.secret_key = config.SECRET
    app.config.from_object(config)
    app.config.from_pyfile('config.py')

    config.APP = app

    @app.route('/')
    def index():
        return render_template('html.html')

    @app.route('/calculaform', methods=['POST', 'GET'])
    def calculaform():
        v1 = request.form['v1']
        v2 = request.form['v2']
        operacao = request.form['operacao']

        try:
            v1 = float(v1)
        except ValueError:
            return "Valores errados"

        try:
            v2 = float(v2)
        except ValueError:
            return "Valores errados"

        # para pythons mais recentes (3.10 por exemplo)
        match operacao:
            case "soma":
                return str(soma(v1, v2))
            case "subtracao":
                return str(subtracao(v1, v2))
            case "divisao":
                return str(divisao(v1, v2))
            case "multiplicacao":
                return str(multiplicacao(v1, v2))
            case "potencicacao":
                return str(potencicacao(v1, v2))
            case "raiz quadrada":
                return str(raiz_quadrada(v1, v2))
            case "logaritimo":
                return str(logaritimo(v1, v2))
        return str("algo deu errado")

        # ajuste para rodar em python mais antigos
        '''
        if operacao == "soma":
            return str(soma(v1, v2))
        elif operacao == "subtracao":
            return str(subtracao(v1, v2))
        elif operacao == "divisao":
            return str(divisao(v1, v2))
        elif operacao == "multiplicacao":
            return str(multiplicacao(v1, v2))
        else: return str("algo deu errado")
        '''
