import json

from django.test import TestCase

# Create your tests here.

# blog/tests.py
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Post
from django.urls import reverse


class PostModelTests(TestCase):
    """測試 Post 模型的基本功能"""
    def setUp(self):
        # 創建測試用戶
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # 創建測試文章
        self.post = Post.objects.create(
            title='Test Title',
            content='Test Content',
            author=self.user,
        )

    def test_post_creation(self):
        """check the post creation"""
        self.assertEqual(self.post.title, 'Test Title')
        self.assertEqual(self.post.content, 'Test Content')
        self.assertEqual(self.post.author, self.user)
        self.assertIsNone(self.post.published_date)

    def test_publish_method(self):
        """測試發布方法"""
        self.post.publish()
        self.assertIsNotNone(self.post.published_date)
        self.assertTrue(isinstance(self.post.published_date, timezone.datetime))

    def test_str_representation(self):
        """測試字符串表示"""
        self.assertEqual(str(self.post), 'Test Title')

    def tearDown(self):
        # 清理測試數據
        self.user.delete()


class PostViewTests(TestCase):
    def setUp(self):
        """設置測試環境"""
        self.client = Client()

        # 創建測試用戶
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # 創建測試1筆文章
        self.post = Post.objects.create(
            title='Test Title',
            content='Test Content',
            author=self.user,
        )

        # 準備API URL
        self.list_url = reverse('post_list')
        self.detail_url = reverse('post_detail', args=[self.post.id])

        # 準備POST要寫入的數據
        self.post_data ={
            'title': 'New Title',
            'content': 'New Content',
        }

    def test_get_post_list(self):
        """測試獲取文章列表"""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(len(data['posts']), 1)
        self.assertEqual(data['posts'][0]['title'], 'Test Title')

    def test_get_post_detail(self):
        """測試獲取文章詳情"""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, 200)

        data = response.json()
        self.assertEqual(data['title'], 'Test Title')

    def test_create_post(self):
        """測試創建文章"""
        # 先確保登入成功
        login_success = self.client.login(username='testuser', password='testpass123')
        self.assertTrue(login_success)  # 驗證登入是否成功

        response = self.client.post(
            self.list_url,
            data=json.dumps(self.post_data),
            content_type='application/json'
        )

        self.assertEqual(response.status_code, 201)

    def tearDown(self):
        # 清理測試數據
        self.user.delete()