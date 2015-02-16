from app.parser.rss_parser import Parser
from tests import BaseTestCase


class TestParser(BaseTestCase):
    def test_method(self):
        self.assertEqual("hello", Parser.test_method())