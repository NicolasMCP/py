from typing import List
from flask import Flask, render_template, request
app = Flask(__name__)
frutas = []
registros: List = []


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form.get("fruta"):
            frutas.append(request.form.get("fruta"))
    return render_template("frutas.html", frutas=frutas)


@app.route("/alunos", methods=["GET", "POST"])
def alunos():
    if request.method == "POST":
        if request.form.get("aluno") and request.form.get("nota"):
            existe = False
            for registro in registros:
                if request.form.get("aluno") == registro["aluno"]:
                    existe = True
            if not existe:
                registros.append({"aluno": request.form.get("aluno"),
                                  "nota": request.form.get("nota")})
    return render_template("alunos.html", registros=registros)


if __name__ == "__main__""":
    app.run(debug=True)
