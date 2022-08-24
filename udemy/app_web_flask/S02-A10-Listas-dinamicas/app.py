from flask import Flask, render_template, request

app = Flask(__name__)
frutas = []


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        if request.form.get('fruta'):
            frutas.append(request.form.get('fruta'))
    return render_template('lista_dinamica.html', frutas=frutas)


if __name__ == '__main__':
    app.run(debug=True)
