from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
frutas = []
registros = []

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cursos.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = b'\xa7\xbb\xec\xa2\xc1\xa3\x0c\x1at\xf6d\xc4R\x8fk\xef'
db = SQLAlchemy(app)


class Cursos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50))
    descricao = db.Column(db.String(100))
    carga_horaria = db.Column(db.Integer)

    def __init__(self, nome, descricao, carga_horaria):
        self.nome = nome
        self.descricao = descricao
        self.carga_horaria = carga_horaria


@app.route("/cursos")
def lista_cursos():
    return render_template("cursos.html", cursos=Cursos.query.all())


@app.route("/cria_curso", methods=["GET", "POST"])
def cria_curso():
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    carga_horaria = request.form.get('carga_horaria')

    if request.method == "POST":
        if not nome or not descricao or not carga_horaria:
            flash('Preencha todos os campos do formulário', 'error')
        else:
            curso = Cursos(nome, descricao, carga_horaria)
            db.session.add(curso)
            db.session.commit()
            return redirect(url_for('lista_cursos'))
    return render_template("novo_curso.html")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
    return render_template("frutas.html", frutas=frutas)


@app.route("/alunos", methods=["GET", "POST"])
def alunos():
    existe = False
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            for registro in registros:
                if request.form.get("aluno") == registro["aluno"]:
                    existe = True
            if not existe:
                registros.append({"aluno": request.form.get("aluno"),
                                  "nota": request.form.get("nota")})
    return render_template("alunos.html", registros=registros, existe=existe)


@app.route('/<int:id>/atualiza_curso', methods=["GET", "POST"])
def atualiza_curso(id):
    curso = Cursos.query.filter_by(id=id).first()
    if request.method == "POST":
        nome = request.form['nome']
        descricao = request.form['descricao']
        carga_horaria = request.form['carga_horaria']

        Cursos.query.filter_by(id=id).update({"nome": nome,
                                              "descricao": descricao,
                                              "carga_horaria": carga_horaria})
        db.session.commit()
        return redirect(url_for('lista_cursos'))
    return render_template("atualiza_curso.html", curso=curso)


@app.route('/<int:id>/remove_curso')
def remove_curso(id):
    curso = Cursos.query.filter_by(id=id).first()
    db.session.delete(curso)
    db.session.commit()
    return redirect(url_for('lista_cursos'))


if __name__ == "__main__""":
    db.create_all()
    app.run(debug=True)
