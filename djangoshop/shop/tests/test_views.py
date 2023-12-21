from django.test import TestCase, Client

from shop.models import Category, Product

class RunServerTestCase(TestCase):    
    def setUp(self):
        self.client = Client()
        
        self.category = Category.objects.create(name="Category", 
                               slug="category")
        
        self.product = Product.objects.create(category=self.category, 
                               name="Product 1", 
                               slug="Product", 
                               description="Description", 
                               price=1, 
                               stock=10,
                               available=True)


    def test_webpage_accessibility(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test_category_accessibility(self):
        response = self.client.get('/category/')
        self.assertEqual(response.status_code, 200)
        
    def test_category_accessibility(self):
        response = self.client.get(f'/{self.product.category.pk}/{self.product.slug}/')
        self.assertEqual(response.status_code, 200)
    