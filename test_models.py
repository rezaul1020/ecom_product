#Test Model 
"""
Test Cases TestProductModel
"""
import json
from random import randrange
from unittest import TestCase
from models import db
from models.product import Product, DataValidationError

PRODUCT_DATA = {}

class TestProductModel(TestCase):
    """Test Product Model"""

    @classmethod
    def setUpClass(cls):
        """ Load data needed by tests """
        db.create_all()  # make our sqlalchemy tables
        global PRODUCT_DATA
        with open('tests/fixtures/product_data.json') as json_data:
            PRODUCT_DATA = json.load(json_data)

    @classmethod
    def tearDownClass(cls):
        """Disconnext from database"""
        db.session.close()

    def setUp(self):
        """Truncate the tables"""
        self.rand = randrange(0, len(PRODUCT_DATA))
        db.session.query(Product).delete()
        db.session.commit()

    def tearDown(self):
        """Remove the session"""
        db.session.remove()

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_create_all_products(self):
        """ Test creating multiple Products """
        for data in PRODUCT_DATA:
            product = Product(**data)
            product.create()
        self.assertEqual(len(Product.all()), len(PRODUCT_DATA))

    def test_create_an_product(self):
        """ Test Product creation using known data """
        data = PRODUCT_DATA[self.rand] # get a random account
        product = Product(**data)
        product.create()
        self.assertEqual(len(Product.all()), 1)

    def test_repr(self):
        """Test the representation of an product"""
        product = Product()
        product.name = "Foo"
        self.assertEqual(str(account), "<Account 'Foo'>")

    def test_to_dict(self):
        """ Test product to dict """
        data = PRODUCT_DATA[self.rand] # get a random account
        product = Product(**data)
        result = product.to_dict()
        self.assertEqual(product.id, result["id"])
        self.assertEqual(product.name, result["name"])
        self.assertEqual(product.price, result["price"])
        self.assertEqual(product.category, result["category"])
        self.assertEqual(product.available, result["available"])

    def test_from_dict(self):
        """ Test product from dict """
        data = PRODUCT_DATA[self.rand] # get a random account
        product = Product()
        product.from_dict(data)
        self.assertEqual(product.id, result["id"])
        self.assertEqual(product.name, result["name"])
        self.assertEqual(product.price, result["price"])
        self.assertEqual(product.category, result["category"])
        self.assertEqual(product.available, result["available"])

    def test_update_an_account(self):
        """ Test Product update using known data """
        data = PRODUCT_DATA[self.rand] # get a random account
        product = Product(**data)
        product.create()
        self.assertIsNotNone(product.id)
        account.name = "Rumpelstiltskin"
        account.update()
        found = Product.find(product.id)
        self.assertEqual(found.name, product.name)

    def test_invalid_id_on_update(self):
        """ Test invalid ID update """
        data = PRODUCT_DATA[self.rand] # get a random account
        product = Product(**data)
        product.id = None
        self.assertRaises(DataValidationError, product.update)

    def test_delete_an_account(self):
        """ Test Product delete using known data """
        data = PRODUCT_DATA[self.rand] # get a random account
        product = Product(**data)
        product.create()
        self.assertEqual(len(Product.all()), 1)
        product.delete()
        self.assertEqual(len(Product.all()), 0)

