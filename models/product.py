from models.modules import *

class Product:

    def __init__(self, name, category, supplier, price):
        self.id = Modules.auto_key(__class__)
        self.name = name
        self.category = category
        self.supplier = supplier
        self.price = price

    @classmethod
    def check_product(cls, product):
        products = Json.json2list(cls)
        for prod in products:
            if prod.get('name').lower() == product.lower():
                return True
        return False
    
    @classmethod
    def add_product(cls, product, obj):
        if not cls.check_product(product):
            Json.write_json(cls, obj)