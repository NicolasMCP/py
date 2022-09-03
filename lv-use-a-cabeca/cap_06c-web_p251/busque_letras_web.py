import html
from flask import Flask, render_template, request
from busque_letras import busque_letras

app = Flask(__name__)


def log_request(req: 'request', res: str) -> None:
    with open('busque_letras.log', 'a') as log:
        print(str(req.form)[20:-2], req.remote_addr, res, file=log, sep=' | ', end='<br>')


@app.route('/busca', methods=['POST'])
def busca():
    frase = request.form['frase']
    letras = request.form['letras']
    resultados = busque_letras(frase, letras)
    subtitulo = 'Aqui estão seus resultados:'
    titulo = 'Resultados'
    log_request(request, resultados)
    return render_template('resultados.html',
                           frase=frase,
                           letras=letras,
                           subtitulo=subtitulo,
                           titulo=titulo,
                           resultados=resultados)


@app.route('/')
@app.route('/entrada')
def entrada() -> 'html':
    return render_template('entrada.html',
                           subtitulo="Bem vindo ao 'busca_letras' na web")


@app.route('/verlog')
def ver_log() -> str:
    with open('busque_letras.log') as log:
        conteudo = log.read()
        return conteudo


if __name__ == "__main__":
    app.run(debug=True)
