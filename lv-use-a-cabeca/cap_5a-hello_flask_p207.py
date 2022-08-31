from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello() -> str:
    return 'Olá mundo do Flask!'


if __name__ == "__main__":
    app.run(debug=True)
