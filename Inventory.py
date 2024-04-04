from Item import Item

class Inventory:
    def __init__(self):
        self.items = []
        
    def add_item(self, name, description, price):
        found_item = None
        index = self.get_index(self.items,"name",name)
        if index == None:     
            item = Item(name,description,price)
            self.items.append(item)
            print(f"\nThe Item '{item.name}' was created succesfully.\nItem unique ID: {item.id}\n")
        else:
            found_item = self.items[index]
            print(f"\nThere is already an item with exact name '{name}' \n Name: {found_item.name} \n price: $ {found_item.price} \n Description: {found_item.description} \n ID: {found_item.id}")
                 
    def update_item(self, item_name, new_item_name = None, new_description = None, new_price = None):
        index = self.get_index(self.items,"name",item_name)
        nameflag = None
        try:
            found_item = self.items[index]
            if new_item_name == None or new_item_name == "":
                nameflag = 1
                pass
            else:
                found_item.name = new_item_name
            if new_description == None or new_description == "":
                pass
            else:
                found_item.description = new_description
            if new_price == None or new_price == "":
                pass
            else:
                found_item.price = new_price
            self.items.pop(index)
            self.items.insert(index,found_item)
            if nameflag == 1:
                print(f"\nSuccesfully updated item {new_item_name}\n")
            else:
                print(f"\nSuccesfully updated item {item_name}\n")
            return None                           
        except TypeError:
            print(f"\n === item {item_name} not found ===\n")
            
    def remove_item(self, item_name):
        index = self.get_index(self.items,"name",item_name)
        try:
            self.items.pop(index)
            print(f"\nSuccesfully removed item {item_name}\n")
            return None                           
        except TypeError:
            print(f"\n === item {item_name} not found ===\n")
            
    def display_inventory(self):
        for item in self.items:
            print(item)

    def get_index(self,list,attribute,value):
        for i, obj in enumerate(list):
            try:
                if getattr(obj, attribute) == value:
                    return i
            except AttributeError:
                    pass
        return None