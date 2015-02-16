from tests import BaseTestCase
from app.parser.rss_parser import Parser
import json


class TestDummy(BaseTestCase):
    def setUp(self):
        self.client = self.create_app().test_client()

    def test_root(self):
        response = self.client.get('/dummy')
        self.assertEqual(200, response.status_code)

    def test_test(self):
        response = self.client.get('/dummy/test')
        self.assertEqual(Parser.test_method(), response.data.decode('utf8'))

    def test_json(self):
        response = self.client.get('/dummy/json_test')
        self.assertEqual('{"key": "value"}', response.data.decode('utf8'))

        post_data = {'k': 'v'}
        response = self.client.post('/dummy/json_test', data=json.dumps(post_data))
        self.assertEqual(json.dumps(post_data), response.data.decode('utf8'))