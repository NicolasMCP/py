from flask import Flask, render_template, request
app = Flask(__name__)
registros = []


@app.route('/', methods=['GET', 'POST'])
@app.route('/alunos', methods=['GET', 'POST'])
def alunos():
    # alunos = {'Fulano': 5.0, 'Ciclano': 7.0, 'Beltrano': 6.0, 'Aluno': 8.5}
    if request.method == 'POST':
        if request.form.get('aluno') and request.form.get('nota'):
            registros.append({'aluno': request.form.get('aluno'),
                              'nota': request.form.get('nota')})
    return render_template('alunos.html', registros=registros)


if __name__ == '__main__':
    app.run(debug=True)
