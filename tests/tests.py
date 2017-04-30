import unittest

from pyramid.paster import get_appsettings
settings = get_appsettings('test.ini', name='main')


class FunctionalTests(unittest.TestCase):
    def setUp(self):
        from todo import main
        app = main({}, **settings)
        from webtest import TestApp
        self.testapp = TestApp(app)

    def test_root(self):
        res = self.testapp.get('/')
        self.assertTrue(b'Hello World' in res.body)
