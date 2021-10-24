from django.test import TestCase
from forms import ProductForm

# Create your tests here.
# test-driven development
"""
Components including:

a. parameters
1. bar_name, bar_rating, bar_occupancy, bar_capacity should not be empty
2. bar_rating should range from 0.0 to 5.0
3. bar_capacity and bar_occupancy should > 0
4. bar_occupancy should < bar_capacity

b. functions
1. list
2. search
3. to_filter
4. sort
5. bar_filter
6. details

c. logic
1. login --> show list
2. show list --> search
3. show list --> sort
4. show list --> filter
5. search --> sort
6. search --> filter
7. sort --> search
8. sort --> filter
9. filter --> sort
10. filter --> search

d. system
1. database capacity
2. response time
"""
class SimpleTest(TestCase):
    def test_basic_addition(self):
        # Tests that 1 + 1 always equals 2.

        self.assertEqual(1 + 1, 2)


class ProductTest(TestCase):
    def setUp(self):
        self.product = {
            'bar_name': 'bar_name',
            'bar_rating': 1.0,
            'bar_occupancy': 1,
            'bar_capacity': 1
        }
        f = ProductForm(self.product)
        f.save()

    #### bar_name, bar_rating, bar_occupancy, bar_capacity should not be empty
    def test_attrs_cannot_empty(self):
        f = ProductForm({})
        self.assertFalse(f.is_valid())
        self.assertTrue(f['bar_name'].errors)
        self.assertTrue(f['bar_rating'].errors)
        self.assertTrue(f['bar_occupancy'].errors)
        self.assertTrue(f['bar_capacity'].errors)

    #### bar_capacity should be positve
    def test_capacity_positive(self):
        f = ProductForm(self.product)
        self.assertTrue(f.is_valid())
        self.product['bar_capacity'] = 0
        f = ProductForm(self.product)
        self.assertFalse(f.is_valid())
        self.product['bar_capacity'] = - 1
        f = ProductForm(self.product)
        self.assertFalse(f.is_valid())
        self.product['bar_capacity'] = 1

    #### bar_occupancy should be positve
    def test_occupancy_positive(self):
        f = ProductForm(self.product)
        self.assertTrue(f.is_valid())
        self.product['bar_occupancy'] = 0
        f = ProductForm(self.product)
        self.assertFalse(f.is_valid())
        self.product['bar_occupancy'] = - 1
        f = ProductForm(self.product)
        self.assertFalse(f.is_valid())
        self.product['bar_occupancy'] = 1

        

