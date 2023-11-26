from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'This is not the first Flask project'


if __name__ == '__main__':
    app.run()
