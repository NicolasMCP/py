import html
from flask import Flask, render_template, request, redirect
from busque_letras import busque_letras

app = Flask(__name__)


@app.route('/')
def hello() -> '302':
    return redirect('/entrada')


@app.route('/busca', methods=['POST'])
def busca():
    frase = request.form['frase']
    letras = request.form['letras']
    resultados = busque_letras(frase, letras)
    subtitulo = 'Aqui estão seus resultados:'
    titulo = 'Resultados'
    return render_template('resultados.html',
                           frase=frase,
                           letras=letras,
                           subtitulo=subtitulo,
                           titulo=titulo,
                           resultados=resultados)


@app.route('/entrada')
def entrada() -> 'html':
    return render_template('entrada.html',
                           subtitulo="Bem vindo ao 'busca_letras' na web")


if __name__ == "__main__":
    app.run(debug=True)
