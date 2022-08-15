from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def lista():
    frutas = ['Morango', 'Uva', 'Laranja', 'Mamão', 'Pera', 'Maça', 'Abacaxi', 'Melão']
    return render_template('lista.html', frutas=frutas)


@app.route('/dicionario')
def dicionario():
    alunos = {'Fulano': 5.0, 'Ciclano': 6.0, 'Beltrano': 7.0, 'Aluno': 8.5}
    return render_template('dicionario.html', alunos=alunos)


if __name__ == '__main__':
    app.run(debug=True)
