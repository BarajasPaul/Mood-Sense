#!/bin/python3

from moodsense import app
import unittest


class FlaskApiTest(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.client.testing = True

    def test_flask_work(self):
        response = self.client.options('/')
        self.assertEqual(response.status_code, 200)

    def test_flask_fail(self):
        response = self.client.options('/failed')
        self.assertEqual(response.status_code, 404)


if __name__ == '__main__':
    print("Flask Testing")
    unittest.main()
