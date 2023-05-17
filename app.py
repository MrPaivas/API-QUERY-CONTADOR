from models import db, ApoioMulti, Biblioteca, Clinica, Comercial, Cordenacao, Psicologia, SecAcad, Secretaria
from dotenv import load_dotenv
from flask import Flask, jsonify
import os


load_dotenv()
host = os.getenv("DB_HOST")
usuario = os.getenv("DB_USER")
passwd = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+mysqlconnector://{usuario}:{passwd}@{host}/{database}"
db.init_app(app)


@app.route('/apoio_multi', methods=['GET'])
def apoio_multi():
    """Faz uma busca ao banco de dados"""
    dados = ApoioMulti.query.all()
    resultados = []
    for dado in dados:
        resultado = {
            'idapoio_multi': dado.idapoio_multi,
            'data': dado.data,
            'contador': dado.contador
        }
        resultados.append(resultado)

    return jsonify(resultados)


@app.route('/biblioteca', methods=['GET'])
def biblioteca():
    """Faz uma busca ao banco de dados"""
    dados = Biblioteca.query.all()
    resultados = []
    for dado in dados:
        resultado = {
            'idbiblioteca': dado.idbiblioteca,
            'data': dado.data,
            'contador': dado.contador
        }
        resultados.append(resultado)

    return jsonify(resultados)


@app.route('/clinica', methods=['GET'])
def clinica():
    """Faz uma busca ao banco de dados"""
    dados = Clinica.query.all()
    resultados = []
    for dado in dados:
        resultado = {
            'idclinia': dado.idclinia,
            'data': dado.data,
            'contador': dado.contador
        }
        resultados.append(resultado)

    return jsonify(resultados)


@app.route('/comercial', methods=['GET'])
def comercial():
    """Faz uma busca ao banco de dados"""
    dados = Comercial.query.all()
    resultados = []
    for dado in dados:
        resultado = {
            'idcomercial': dado.idcomercial,
            'data': dado.data,
            'contador': dado.contador
        }
        resultados.append(resultado)

    return jsonify(resultados)


@app.route('/cordenacao', methods=['GET'])
def cordenacao():
    """Faz uma busca ao banco de dados"""
    dados = Cordenacao.query.all()
    resultados = []
    for dado in dados:
        resultado = {
            'idcordenacao': dado.idcordenacao,
            'data': dado.data,
            'contador': dado.contador
        }
        resultados.append(resultado)

    return jsonify(resultados)


@app.route('/psicologia', methods=['GET'])
def psicologia():
    """Faz uma busca ao banco de dados"""
    dados = Psicologia.query.all()
    resultados = []
    for dado in dados:
        resultado = {
            'idpsicologia': dado.idpsicologia,
            'data': dado.data,
            'contador': dado.contador
        }
        resultados.append(resultado)

    return jsonify(resultados)


@app.route('/sec_acad', methods=['GET'])
def sec_acad():
    """Faz uma busca ao banco de dados"""
    dados = SecAcad.query.all()
    resultados = []
    for dado in dados:
        resultado = {
            'idsec_acad': dado.idsec_acad,
            'data': dado.data,
            'contador': dado.contador
        }
        resultados.append(resultado)

    return jsonify(resultados)


@app.route('/secretaria', methods=['GET'])
def secretaria():
    """Faz uma busca ao banco de dados"""
    dados = Secretaria.query.all()
    resultados = []
    for dado in dados:
        resultado = {
            'idsecretaria': dado.idsecretaria,
            'data': dado.data,
            'contador': dado.contador
        }
        resultados.append(resultado)

    return jsonify(resultados)


if __name__ == '__main__':
    app.run(debug=True, host='10.151.22.123', port=5000)
