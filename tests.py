from app import app
import unittest
import requests


class TestFlask(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()

    def test_index_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"<title>Currency Converter</title>", response.data)

    def test_index_post(self):
        response = self.app.post(
            '/', data={'convert-from': 'USD', 'convert-to': 'EUR', 'convert-amount': 100}, follow_redirects=True)
        data = round((requests.get(
            f'https://api.exchangerate.host/convert?from=USD&to=EUR&amount=100').json())['result'], 2)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            f'<p class="success">100 USD converts to {data} EUR</p>'.encode(), response.data)
        response = self.app.post(
            '/', data={'convert-from': 'AED', 'convert-to': 'MRO', 'convert-amount': 100}, follow_redirects=True)
        self.assertIn(
            f'<p class="error">Cannot convert AED to MRO</p>'.encode(), response.data)
        # codes = (requests.get(
        #     'https://api.exchangerate.host/symbols').json())['symbols'].keys()
        # # inc = 0
        # # for a in codes:
        # #     for b in codes:
        # #         print(f'{inc/(len(codes)**2)}%')
        # #         inc += 1
        # #         response = self.app.post(
        # #             '/', data={'convert-from': a, 'convert-to': b, 'convert-amount': 100})


if __name__ == '__main__':
    unittest.main()
