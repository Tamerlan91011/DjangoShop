from django.test import TestCase
from shop.models import Product, Category


from decimal import Decimal


class ProductTestCase(TestCase):
    def setUp(self):
        category = Category.objects.get_or_create(name="Category")[0]
        
        Product.objects.create(category=category, 
                               name="Product 1", 
                               slug="Product", 
                               description="Description", 
                               price=1, 
                               stock=10,
                               available=True)
        

    def test_correctness_types(self):
        self.assertIsInstance(Product.objects.get(category=1).category, Category)
        self.assertIsInstance(Product.objects.get(name="Product 1").name, str)
        self.assertIsInstance(Product.objects.get(slug="Product").slug, str)
        self.assertIsInstance(Product.objects.get(description="Description").description, str)
        self.assertIsInstance(Product.objects.get(price=1).price, Decimal)
        self.assertIsInstance(Product.objects.get(stock=10).stock, int)
        self.assertIsInstance(Product.objects.get(available=True).available, bool)
    
    def test_correctness_data(self):
        self.assertTrue(Product.objects.get(category=1).category == Category.objects.get_or_create(name="Category")[0])
        self.assertTrue(Product.objects.get(name="Product 1").name == "Product 1")
        self.assertTrue(Product.objects.get(slug="Product").slug == "Product")
        self.assertTrue(Product.objects.get(description="Description").description == "Description")
        self.assertTrue(Product.objects.get(price=1).price == Decimal(1))
        self.assertTrue(Product.objects.get(stock=10).stock == 10)
        self.assertTrue(Product.objects.get(available=True).available == True)
    
    
class CategoryTestCase(TestCase):
    def setUp(self):        
        Category.objects.create(name="Category 1", 
                               slug="Category")
        

    def test_correctness_types(self):
        self.assertIsInstance(Category.objects.get(name="Category 1").name, str)
        self.assertIsInstance(Category.objects.get(slug="Category").slug, str)
    
    def test_correctness_data(self):
        self.assertTrue(Category.objects.get(name="Category 1").name == "Category 1")
        self.assertTrue(Category.objects.get(slug="Category").slug == "Category")