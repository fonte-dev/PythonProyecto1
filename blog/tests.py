from django.test import TestCase
from django.urls import reverse_lazy
from blog.views import PostCreateView
from .models import Post, User


class PostTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345")
        self.post = Post.objects.create(titulo="Python", autor=self.user)


class PostCreateViewTests(TestCase):
    def test_success_url(self):
        url = reverse_lazy("blog:post_list")
        self.assertEqual(PostCreateView.success_url, url)
