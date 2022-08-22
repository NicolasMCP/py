from flask import Flask, render_template, request
app = Flask(__name__)
frutas = []
registros = []


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('fruta'):
            frutas.append(request.form.get('fruta'))
    return render_template('lista_dinamica.html', frutas=frutas)


@app.route('/alunos', methods=['GET', 'POST'])
def alunos():
    if request.method == 'POST':
        if request.form.get('aluno') and request.form.get('nota'):
            registros.append({'aluno': request.form.get('aluno'),
                              'nota': request.form.get('nota')
                              })
    return render_template('alunos.html', registros=registros)


if __name__ == '__main__':
    app.run(debug=True)
