from django.test import TestCase

# Create your tests here.
from django.contrib.auth.models import User
from ..models import Post

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        u = User.objects.create(first_name='Big', last_name='Bob')
        for x in range(20):
            Post.objects.create(title=f'My first post {x}',
            slug=f'my-first-post-{x}',
            author=u,
            content=f'My first post content {x}')

    def test_urls(self):
        '''
        Comprobar que el listado de posts devuelve 20 posts
        '''
        # página principal
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # admin
        response = self.client.get('/admin/')
        self.assertEqual(response.status_code, 302)
        # primer posts
        p = Post.objects.first()
        response = self.client.get(f'/{p.slug}/')
        self.assertEqual(response.status_code, 200)
