from models.modules import *

class User:
    
    def __init__(self, username, password, email, name, l_name, dni, address, contact):
        self.id = Modules.auto_key(__class__)
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.l_name = l_name
        self.dni = dni
        self.address = address
        self.contact = contact
        self.pay_methods = []


    @classmethod
    def check_user(cls, username):
        users = Json.json2list(cls)
        for user in users:
            if user.get('username').lower() == username.lower():
                return True
        return False

    @classmethod
    def add_user(cls, username, obj):
        if not cls.check_user(username):
            Json.write_json(cls, obj)

    @classmethod
    def check_credentials(cls, username, password):
        users = Json.json2list(cls)
        for user in users:
            if user.get('username').lower() == username.lower() and user.get('password') == password:
                return True
        return False