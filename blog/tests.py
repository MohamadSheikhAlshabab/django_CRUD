from django.test import TestCase
from django.urls import reverse
from .models import Post
from django.contrib.auth import get_user_model

# Create your tests here.

class PostTests(TestCase):

    def  setup(self):
        self.user = get_user_model().objects.create_user(
            username = "Amjad",
            email = "amjad@gmail.com",
            password = "1234+4321"
        )

        self.post = Post.objects.create(
            title = "test post",
            author = self.user,
            body = "for testing purpose",
        )

    def test_home_page_status_code(self):
        expected = 200
        url = reverse('home')
        response = self.client.get(url)
        actual = response.status_code 
        self.assertEquals(expected,actual)
        
    def test_home_page_template(self):
        url = reverse('home')
        response = self.client.get(url)
        actual = 'home.html'
        self.assertTemplateUsed(response, actual)

    def test_Model_str(self):
        post = Post('python','mais','python language')
        actual = post.title
        expected = str(post)
        self.assertEqual(expected, actual)
    

    def test_update_page_view(self):
        expected = 200
        url = reverse('update_view',args="1"),{
            "title" : "hello",
        }
        response = self.client.post(url)
        actual = 404
        self.assertEqual(response.status_code,actual)
        # self.assertContains(response,"hello")
        
    def test_details_page_view(self):
        expected = 404
        url = reverse('Blog_details',args="1")
        response = self.client.get(url)
        actual = response.status_code 
        self.assertEqual(expected,actual)
        
    def test_delete_page_view(self):
        url = reverse('delete_view',args="1")
        response = self.client.get(url)
        expected = 404
        self.assertEquals(response.status_code, expected)