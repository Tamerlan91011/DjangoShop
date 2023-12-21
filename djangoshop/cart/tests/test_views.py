from django.test import TestCase, Client

from shop.models import Category
from cart.forms import CartAddProductForm

class RunServerTestCase(TestCase):    
    def setUp(self):
        self.client = Client()
        
    def test_webpage_accessibility(self):
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, 200)
    
    def test_correct_form(self):
        form = CartAddProductForm(data={'quantity':1,'update':False})
        self.assertTrue(form.is_valid())
    
    def test_incorrect_form(self):
        # Так как поле "Кол-во" не может быть больше 20, то все, что выше этого числа, считается некорректным вводом
        form = CartAddProductForm(data={'quantity':21,'update':False})
        self.assertFalse(form.is_valid())