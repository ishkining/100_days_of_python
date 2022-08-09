from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/guess/<name>')
def predict_by_name(name):
    params = {
        'name': name,
    }
    age_response = requests.get('https://api.agify.io', params=params)
    gender_response = requests.get('https://api.genderize.io', params=params)
    print(age_response.json()['age'])
    return render_template('guesser.html', name=name.title(), age=age_response.json()['age'],
                           gender=gender_response.json()['gender'])


if __name__ == '__main__':
    app.run(debug=True)