from django.test import TestCase
from .models import *


class PosTestClass(TestCase):
    '''
    This is a class that perform unittest on the Post Model.
    '''
    
    def setUp(self):
        self.post = Post(id=1,title='new post',image='images/lagoon.jpeg',description='the best of the best', link='https://link.com/',user_id=3)

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_save_method(self):
        self.post.save_post()
        post = Post.objects.all()
        self.assertTrue(len(post)>0)
    
    def test_delete_method(self):
        self.post.save_post()
        self.post.delete_post()
        post = Post.objects.all()
        self.assertTrue(len(post) is 0)