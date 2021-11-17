import unittest
import config
from flask_migrate import upgrade, downgrade

class BaseTest(unittest.TestCase):
    def setUp(self, ) -> None:
        with config.app.app_context():
            config.app.config.update(SQLALCHEMY_DATABASE_URI=config.DATABASE_TEST_URI)
            config.app.config['TESTING'] = True
            upgrade() # apply migrations and create fresh tables

    def tearDown(self) -> None:
        with config.app.app_context():
            downgrade() # clear all data and destroy tables