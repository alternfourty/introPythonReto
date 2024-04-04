from Inventory import Inventory

def execute():
    version = "0.0.1"
    run = True
    inventory = Inventory()
    while(run == True):
        print(f"Welcome to ItemStorage v.{version}\nIMPORTANT: Data is NOT PERSISTANT in this version\nPlease choose operation number to execute: \n")
        print("1. Store a New item\n2. Update an existing item\n3. Remove an item\n4. Display the Inventory\n5. Exit Program")  
        option = input("\nEnter the operation number: ")
        match option:
            case "1":
                print("\nYou selected 1. Store a New item")
                item_name = input("\nEnter the name of the new item to store:")
                item_description = input("\nPlease enter the item Description:")
                item_price = input("\nPlease enter the item Price:")
                inventory.add_item(item_name, item_description, item_price)
            case "2":
                print("\nYou selected 2. Update an existing item")
                item_name = input("\nEnter the Name of the item to update: ")
                new_item_name = input("\nEnter the new name for the item (Enter without typing for keeping the original): ")
                new_description = input("\nEnter the new description for the item (Enter without typing for keeping the original): ")
                new_price = input("\nEnter the new price for the item (Enter without typing for keeping the original): ")
                inventory.update_item(item_name, new_item_name, new_description, new_price)
            case "3":
                print("\nYou selected 3. Remove an Item")
                item_name = input("\nEnter the item name to remove (CANNOT BE UNDONE - TO CANCEL ENTER WITHOUT TYPING): ")
                inventory.remove_item(item_name)
            case "4":
                print("\nYou selected 4. Display the Inventory")
                inventory.display_inventory()
            case "5":
                print("\nYou selected 5. Exit Program")
                print("Thanks for Using ItemStorage")
                run = False
            case _:
                print("\nPlease enter a valid number to execute an action")
    return None