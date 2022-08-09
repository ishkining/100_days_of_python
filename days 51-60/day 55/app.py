from random import randint

from flask import Flask

random_number = 0
app = Flask(__name__)


@app.route("/")
def hello_world():
    global random_number
    random_number = randint(1, 9)
    return "<h1>Guess the number(❁´◡`❁)</h1>" \
           "<img src='https://media.giphy.com/media/l2SpYSNrKPONySXYY/giphy.gif'>"


@app.route("/<number>")
def number_checker(number):
    if int(number) > random_number:
        return "<h1>Too high(┬┬﹏┬┬)</h1>" \
                "<img src='https://media.giphy.com/media/wHB67Zkr63UP7RWJsj/giphy.gif'>"
    elif int(number) < random_number:
        return "<h1>Too low ಠ_ಠ</h1>" \
               "<img src='https://media.giphy.com/media/sqajHVw58WRLW/giphy.gif'>"
    else:
        return "<h1>You are right ╰(*°▽°*)╯</h1>" \
               "<img src='https://giphy.com/clips/justin-right-youre-goddamn-j81bDtL9zhu7uFzMfc'>"


if __name__ == '__main__':
    app.run(debug=True)

