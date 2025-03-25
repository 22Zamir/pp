import datetime
import random
from flask import Flask

app = Flask(__name__)


@app.route('/hello_world')
def test_function():
    return 'Привет мир!'
    pass


@app.route('/cars')
def cars_function():
    cars = ['Chevrolet', 'Renault', 'Ford', 'Lada']
    return f'{cars}'
    pass


@app.route('/cats')
def cats_function():
    cats = ['корниш-рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин.']
    return f'{random.choice(cats)}'
    pass


@app.route('/get_time/now')
def get_time_function():
    now = datetime.datetime.now().utcnow()
    return f'{now}'
    pass


@app.route('/get_time/future')
def get_time_future_function():
    current_time_after_hour = (datetime.datetime.now() + datetime.timedelta(hours=1)).time()
    return f'{current_time_after_hour}'
    pass


@app.route('/get_random_word')
def get_random_word_function():
    with open('war_and_peace.txt', 'r') as f:
        a = f.read()
    print((random.choice(a.translate({ord(i): None for i in '.,!&:;«»„“'}).split())))




@app.route('/counter')
def counter_function():
    global counte_num
    counte_num += 1
    return f'{counte_num}'
    pass

counte_num = 0

if __name__ == '__main__':
    app.run(debug=True)
