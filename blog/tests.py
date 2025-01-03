from django.test import TestCase, Client
from django.urls import reverse


class SimpleViewTests(TestCase):
    def setUp(self):
        self.client = Client()

    def test_hello_world(self):
        # 測試 hello_world 視圖
        response = self.client.get(reverse('hello'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Hello, World!")

    def test_greet_user(self):
        # 測試 greet_user 視圖
        response = self.client.get(reverse('greet', args=['Tom']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content.decode(), "Hello, Tom!")
