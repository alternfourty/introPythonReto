""" def log_uuid(function):
    def internal():
        uid = function()
        print(uid)
        return uid
    return internal """

class Item:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        self.id = self.generate_unique_id()
    def generate_unique_id(self):
        import uuid
        return str(uuid.uuid4())
    def __str__(self):
        return f"\n========= \nItem: {self.name}\nDescription: {self.description}\nPrice: ${self.price}\nID: {self.id}\n=========\n"

# new_item = Item("Keyboard","Simple TKL keyboard",10000)
# print(new_item.id + new_item.name + new_item.description + str(new_item.price))