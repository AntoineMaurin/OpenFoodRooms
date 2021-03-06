import sys

from database.database_request import DatabaseRequest
from models.product import Product

sys.path.append("..")

"""This class is used to make category objects from the categories in the
database, it mainly has a list attribute self.products which contains the
products of a category, and a class method to get them all from the database"""


class Category:
    def __init__(self, id, name):
        self.name = name
        self.id = id
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    @classmethod
    def get_all(cls):
        cls.db_rq = DatabaseRequest()
        categories = []
        for elt in cls.db_rq.get_categories():
            id = elt[0]
            name = elt[1]
            category = Category(id, name)
            categories.append(category)
        return categories

    def get_products(self):
        self.db_rq = DatabaseRequest()
        products = []
        for elt in self.db_rq.get_products_from_category(self):
            product_name = elt[1]
            product_description = elt[2]
            product_nutriscore = elt[3]
            product_store = elt[4]
            product_url = elt[5]
            product = Product(product_name, product_description,
                              product_nutriscore, product_store,
                              product_url, self)
            product.id = elt[0]
            products.append(product)
        return products
