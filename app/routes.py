from app import app
from flask import render_template

@app.route('/')
@app.route('/index')


def index():
    nomeCompleto = "renatomtoscano"
    dados = {
        "profissão": "Não sei",
        "idade":"34"
    }
    return render_template('index.html', nome = nomeCompleto, date=dados["profissão"], paragrafo=dados)
   
@app.route('/contato')
def contato():
    return render_template('contato.html')
