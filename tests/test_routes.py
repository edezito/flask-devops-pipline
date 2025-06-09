import unittest
from app import create_app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.client = create_app().test_client()

    def test_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_auth_sem_token(self):
        response = self.client.get('/protegido')
        self.assertEqual(response.status_code, 401)

    def test_auth_com_token(self):
        response = self.client.get('/protegido', headers={'Authorization': 'Bearer meu-token'})
        self.assertEqual(response.status_code, 200)
