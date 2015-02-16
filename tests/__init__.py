from flask.ext.testing import TestCase

from app import create_app
from app.config import TestConfig


class BaseTestCase(TestCase):
    """Base TestClass for your application."""

    def create_app(self):
        """Create and return a testing flask app."""

        app = create_app(TestConfig)
        return app

    def setUp(self):
        pass

    def tearDown(self):
        pass