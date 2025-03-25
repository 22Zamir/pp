

import requests

from hw3.finance import app, storage
import unittest


class TestFinanceApp(unittest.TestCase):
    def setUp(self):
        storage.clear()
        storage[2022] = {1: 100, 2: 200}
        storage[2023] = {1: 300, 2: 400}

    def test_add_endpoint(self):
        response = requests.get('http://127.0.0.1:5000/add/20220101/500')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Данные записаны!', response.text)

    def test_calculate_year_endpoint(self):
        response = requests.get('http://127.0.0.1:5000/calculate/2022')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Расходы за 2022 год составиои:', response.text)

    def test_calculate_moth_endpoint(self):
        response = requests.get('http://127.0.0.1:5000/calculate/2022/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Расходы за 2022 год и 1', response.text)

    def test_add_endpoint_invalid_date(self):
        response = requests.get('http://127.0.0.1:5000/add/20221332/500')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Введенная дата некорректна, испрравьте!',response.text)

    def test_calculate_endpoint_emtu_storage(self):
        storage.clear()
        storage.clear()
        response = requests.get('http://127.0.0.1:5000/calculate/2022')
        self.assertEqual(response.status_code, 200)
        self.assertIn('У меня пока нет данных по 2022 году', response.text)

        # response = requests.get('http://127.0.0.1:5000/calculate/2022/1')
        # self.assertEqual(response.status_code, 200)
        # self.assertIn('У меня пока нет данных по 2022 году и 1 месяцу', response.text)


if __name__ == '__main__':
    app.run(debug=True)
    unittest.main()
        