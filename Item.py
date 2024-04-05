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
