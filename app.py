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
            v1=int(v1)
        except ValueError:
            return "Valores errados"

        try:
            v2 =int(v2)
        except ValueError:
            return "Valores errados"
        
        match operacao:
            case "soma":
                return str(soma(v1, v2))
            case "subtracao":
                return str(subtracao(v1, v2))
            case "divisao":
                return str(divisao(v1, v2))
            case "multiplicacao":
                return str(multiplicacao(v1, v2))
        return str("algo deu errado")


    


    
        
