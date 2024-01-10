from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


def run_server():
    app.run(debug=True,port=6908)


if __name__ == "__main__":
    run_server()
