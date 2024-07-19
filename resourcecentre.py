from inventory.inventory import Inventory
class ResourceCenter:
    def __init__(self):
        ## Prepare the data (Inventory list)
        self.inventory = Inventory()

    def display_menu(self):
        choice = -1
        while not 1 <= choice <= 5:
            print("\n==============================================")
            print('RESOURCE CENTRE SYSTEM: by Intan')
            print("1. Add item")
            print("2. Display Inventory")
            print("3. Loan item")
            print("4. Return item")
            print("5. Quit")
            choice = int(input("Enter your choice >"))
            if not 1 <= choice <= 5:
                print("Invalid choice, please enter again.\n")
        return choice

    def main(self):
        # Refactor (A): Extract constants for choice integers
        # Refactor (A): Extract constants for option integers

        #### Menu driven application ####
        # Display menu and obtain menu choices
        choice = self.display_menu()

        while choice != 5:

            if choice == 1:
                # Refactor (B): use printHeader(mesage)
                print("")
                print("==============================================")
                print("Add an item")
                print("==============================================")
                
                # Refactor (B): Extract duplicate codes to selectItemType(),
                # return the option selected.
                # Advance refactoring: error chekcing in selectItemType().
                print("\nItem types:")
                print("1. Digital Camera")
                print("2. Laptop")
                option = int(input("Enter option to select item type >"))

                if option == 1:
                    assetTag = input("Enter asset tag >")
                    description = input("Enter description >")
                    opticalZoom = input("Enter optical zoom >")
                    result = self.inventory.add_digital_camera(assetTag, description, opticalZoom)
                    if result:
                        print("Digital Camera added successfully.")
                    else:
                        print("Error adding digital camera.")
            
                elif option == 2:
                    assetTag = input("Enter asset tag >")
                    description = input("Enter descrition >")
                    os = input("Enter os >")
                    result = self.inventory.addLaptop(assetTag, description, os)
                    if result:
                        print("Laptop added.")
                    else:
                        print("Error adding laptop.") 
                else:
                    print("Invalid item type.")


            elif choice == 2:
                # Refactor (B): use printHeader(mesage)
                print("")
                print("==============================================")
                print("Display all items")
                print("==============================================")


                # TO-DO: Write the code to display all digital camera or laptop.
                print(self.inventory.getAvailableCamera())
                print(self.inventory.getAvailableLaptop())

            elif choice == 3:
                # Refactor (B): use printHeader(mesage)
                print("")
                print("==============================================")
                print("Loan an item")
                print("==============================================")
                
                # Refactor (B): use selectItemType()
                print("\nItem types:")
                print("1. Digital Camera")
                print("2. Laptop")
                option = int(input("Enter option to select item type >"))

                if option == 1:
                    assetTag = input("Enter asset tag of the camera > ")
                    studentName = input("Enter student's name > ")
                    dueDate = input("Enter due date (YYYY-MM-DD) > ")

                    result = self.inventory.loanItem(assetTag, 'camera', studentName, dueDate)
                    if result:
                        print("Camera loaned successfully.")
                    else:
                        print("Error loaning camera or item not available.")
                
                elif option == 2:
                    assetTag = input("Enter asset tag of the laptop > ")
                    studentName = input("Enter student's name > ")
                    dueDate = input("Enter due date (YYYY-MM-DD) > ")

                    result = self.inventory.loanItem(assetTag, 'laptop', studentName, dueDate)
                    if result:
                        print("Laptop loaned successfully.")
                    else:
                        print("Error loaning laptop or item not available.")
                
                else:
                    print("Invalid item type.")
                
            elif choice == 4:
                # Refactor (B): use printHeader(mesage)
                print("")
                print("==============================================")
                print("Return an item")
                print("==============================================")
                
                # Refactor (B): use selectItemType()
                print("\nItem types:")
                print("1. Digital Camera")
                print("2. Laptop")
                option = int(input("Enter option to select item type >"))

                if option == 1:
                    assetTag = input("Enter asset tag of the camera > ")

                    result = self.inventory.returnItem(assetTag, 'camera')
                    if result:
                        print("Camera returned successfully.")
                    else:
                        print("Error returning camera or item not found.")
                
                elif option == 2:
                    assetTag = input("Enter asset tag of the laptop > ")

                    result = self.inventory.returnItem(assetTag, 'laptop')
                    if result:
                        print("Laptop returned successfully.")
                    else:
                        print("Error returning laptop or item not found.")
                
                else:
                    print("Invalid item type.")
            
            choice = self.display_menu()

        print("Good bye.")

if __name__ == "__main__":
    app = ResourceCenter()
    app.main()