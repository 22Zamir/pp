import datetime

from flask import Flask

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    year = int(date[:4])
    month = int(date[4:6])
    day = int(date[6:8])
    if check_date(year, month, day):
        storage.setdefault(year, {}).setdefault(month, 0)
        storage[year][month] += number
        return f'Данные записаны! {storage}'
    else:
        return 'Введенная дата некорректна, испрравьте!'


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    sum_expense = 0
    try:
        for expense in storage[year].values():
            sum_expense += expense
        return f'Расходы за {year} год составиои: {sum_expense} руб.'
    except KeyError:
        return f'У меня пока нет данных по {year} году'


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    try:
        if year in storage and month in storage[year]:
            return f'Расходы за {year} год и {month}\nМесяц составили: {storage[year][month]}'
        else:
            return f'У меня пока нет данных по {year} году и {month} месяцу'
    except KeyError:
        return f'У меня пока нет данных по {year} году'


def check_date(year, month, day):
    """"ПРОВЕРКА ДАТЫ НА ВАЛИДНОСТЬ"""
    try:
        datetime.datetime(year, month, day)
        correct_date = True
    except ValueError:
        correct_date = False
    return correct_date


if __name__ == "__main__":
    app.run(debug=True)
