from django.test import TestCase
from .models import Post

# Create your tests here.
class HomePageViewTest(TestCase):
    def test_home_page_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Test', body='Test body.')

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEqual(expected_object_name, 'Test')