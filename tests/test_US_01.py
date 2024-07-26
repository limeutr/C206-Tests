from inventory.inventory import Inventory
class Test_US_01:
############### Test add camera ######################
    def test_add_camera(self):
        test_inventory = Inventory()
        assert len(test_inventory.cameraList) == 0

        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        
        assert result == True
        assert len(test_inventory.cameraList) == 1

    def test_add_existing_camera(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)
        original_len = len(test_inventory.cameraList)
        
        result = test_inventory.addCamera("C002", "Test camera 2", 10)
        
        assert result == False
        assert len(test_inventory.cameraList) == original_len

    def test_add_camera_missing_description(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)
        original_len = len(test_inventory.cameraList)
        
        result = test_inventory.addCamera("C004", "", 10)
        
        assert result == False
        assert len(test_inventory.cameraList) == original_len

    def test_add_camera_incorrect_zoom(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)
        original_len = len(test_inventory.cameraList)
        
        result = test_inventory.addCamera("C004", "Test camera 4", -1)
        
        assert result == False
        assert len(test_inventory.cameraList) == original_len

    ############### Test add laptop ######################
    def test_add_laptop(self):
        test_inventory = Inventory()
        assert len(test_inventory.laptopList) == 0
        
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        
        assert result == True
        assert len(test_inventory.laptopList) == 1
        
    def test_add_existing_laptop(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        original_len = len(test_inventory.laptopList)
        
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        
        assert result == False
        assert len(test_inventory.laptopList) == original_len
        
    def test_add_laptop_missing_description(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        original_len = len(test_inventory.laptopList)
        
        result = test_inventory.addLaptop("L004", "", "WIN10")
        
        assert result == False
        assert len(test_inventory.laptopList) == original_len
        
    def test_add_laptop_missing_os(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        original_len = len(test_inventory.laptopList)
        
        result = test_inventory.addLaptop("L004", "Test Laptop 4", "")

        assert result == False
        assert len(test_inventory.laptopList) == original_len


    ############### Test view camera ######################
    def test_view_empty_camera_list(self):
        test_inventory = Inventory()

        tested_text = test_inventory.getAvailableCamera()
        
        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "AssetTag", "Description", "Available", "Due Date", "Zoom")
        actual_text += "There is no camera to display."
        assert tested_text == actual_text

    def test_view_camera(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)

        tested_text = test_inventory.getAvailableCamera()

        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "AssetTag", "Description", "Available", "Due Date", "Zoom")
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "C001", "Test camera 1", "Yes", "", 5)
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "C002", "Test camera 2", "Yes", "", 10)
        assert tested_text == actual_text

    def test_view_camera_only_available(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)
        result = test_inventory.addCamera("C003", "Test camera 3", 6)
        test_inventory.cameraList[2].setIsAvailable(False)
        
        tested_text = test_inventory.getAvailableCamera()

        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "AssetTag", "Description", "Available", "Due Date", "Zoom")
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "C001", "Test camera 1", "Yes", "", 5)
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "C002", "Test camera 2", "Yes", "", 10)
        assert tested_text == actual_text

    ############### Test view laptop ######################
    def test_view_empty_laptop_list(self):
        test_inventory = Inventory()

        tested_text = test_inventory.getAvailableLaptop()
        
        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "OS")
        actual_text += "There is no laptop to display."
        assert tested_text == actual_text

    def test_view_laptop(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")

        tested_text = test_inventory.getAvailableLaptop()

        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "OS")
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "L001", "Test Laptop 1", "Yes", "", "WINXP")
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "L002", "Test Laptop 2", "Yes", "", "MACOS")
        assert tested_text == actual_text

    def test_view_laptop_only_available(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        result = test_inventory.addLaptop("L003", "Test Laptop 3", "WINXP")
        test_inventory.laptopList[2].setIsAvailable(False)
        
        tested_text = test_inventory.getAvailableLaptop()

        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "OS")
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "L001", "Test Laptop 1", "Yes", "", "WINXP")
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "L002", "Test Laptop 2", "Yes", "", "MACOS")
        assert tested_text == actual_text

class Test_US_06:
   ############### Test loan camera ######################
    def test_loan_an_available_camera(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)

        tested_camera = test_inventory.cameraList[0]
        result = test_inventory.loanCamera(tested_camera.getAssetTag(), "08-08-2030")
        
        assert result == True
        assert tested_camera.getDueDate() == "08-08-2030"
        assert tested_camera.getIsAvailable() == "No"

    def test_loan_an_unavailable_camera(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)
        tested_camera = test_inventory.cameraList[0]
        result = test_inventory.loanCamera(tested_camera.getAssetTag(), "08-08-2030")
        original_date = tested_camera.getDueDate()
        assert result == True

        result2 = test_inventory.loanCamera(tested_camera.getAssetTag(), "01-01-2050")

        assert result2 == False
        assert tested_camera.getDueDate() == original_date
        assert tested_camera.getIsAvailable() == "No"

    def test_loan_not_exists_camera(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)

        result = test_inventory.loanCamera("CC0016", "08-08-2030")

        assert result == False

    def test_loan_camera_with_missing_details(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)
        tested_camera = test_inventory.cameraList[0]

        result = test_inventory.loanCamera(tested_camera.getAssetTag(), "")

        assert result == False
        assert tested_camera.getDueDate() == ""
        assert tested_camera.getIsAvailable() == "Yes"

    ############### Test loan laptop ######################
    def test_loan_an_available_laptop(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")

        tested_laptop = test_inventory.laptopList[0]
        result = test_inventory.loanLaptop(tested_laptop.getAssetTag(), "08-08-2030")

        assert result == True
        assert tested_laptop.getDueDate() == "08-08-2030"
        assert tested_laptop.getIsAvailable() == "No"

    def test_loan_an_unavailable_laptop(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        tested_laptop = test_inventory.laptopList[0]
        result = test_inventory.loanLaptop(tested_laptop.getAssetTag(), "08-08-2030")
        original_date = tested_laptop.getDueDate()
        assert result == True

        result2 = test_inventory.loanLaptop(tested_laptop.getAssetTag(), "01-01-2050")
        
        assert result2 == False
        assert tested_laptop.getDueDate() == original_date
        assert tested_laptop.getIsAvailable() == "No"

    def test_loan_not_exists_laptop(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")

        result = test_inventory.loanLaptop("CB0016", "08-08-2030")

        assert result == False

    def test_loan_laptop_with_missing_details(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        tested_laptop = test_inventory.laptopList[0]

        result = test_inventory.loanLaptop(tested_laptop.getAssetTag(), "")

        assert result == False
        assert tested_laptop.getDueDate() == ""
        assert tested_laptop.getIsAvailable() == "Yes"


class Test_US_07:
    ############### Test return camera ######################
    def test_return_camera_onLoan(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        tested_camera = test_inventory.cameraList[0]
        result = test_inventory.loanCamera(tested_camera.getAssetTag(), "08-08-2030")
        assert result == True
        assert tested_camera.getDueDate() == "08-08-2030"
        assert tested_camera.getIsAvailable() == "No"

        result2 = test_inventory.returnCamera(tested_camera.getAssetTag())

        assert result2 == True
        assert tested_camera.getDueDate() == ""
        assert tested_camera.getIsAvailable() == "Yes"

    def test_return_camera_not_onLoan(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        tested_camera = test_inventory.cameraList[0]

        result = test_inventory.returnCamera(tested_camera.getAssetTag())

        assert result == False
        assert tested_camera.getDueDate() == ""
        assert tested_camera.getIsAvailable() == "Yes"

    def test_return_camera_not_exists(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        
        result = test_inventory.returnCamera("C003")
        
        assert result == False

    ############### Test return laptop ######################
    def test_return_laptop_onLoan(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        tested_laptop = test_inventory.laptopList[0]
        result = test_inventory.loanLaptop(tested_laptop.getAssetTag(), "08-08-2030")
        assert result == True
        assert tested_laptop.getDueDate() == "08-08-2030"
        assert tested_laptop.getIsAvailable() == "No"

        result2 = test_inventory.returnLaptop(tested_laptop.getAssetTag())
        assert result2 == True
        assert tested_laptop.getDueDate() == ""
        assert tested_laptop.getIsAvailable() == "Yes"


    def test_return_laptop_not_onLoan(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        tested_laptop = test_inventory.laptopList[0]

        result = test_inventory.returnLaptop(tested_laptop.getAssetTag())
        
        assert result == False
        assert tested_laptop.getDueDate() == ""
        assert tested_laptop.getIsAvailable() == "Yes"

    def test_return_laptop_not_exists(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        
        result = test_inventory.returnLaptop("L003")
        
        assert result == False


class Test_Refactor_Codes:
    #################### Test findAsset(assetTag) ######################
    def test_find_existing_camera(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)
        result = test_inventory.addCamera("C003", "Test camera 3", 6)

        return_value = test_inventory.findAsset("C001")

        assert return_value.getAssetTag() == "C001"

    def test_find_non_existing_camera(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)
        result = test_inventory.addCamera("C003", "Test camera 3", 6)

        return_value = test_inventory.findAsset("C004")

        assert return_value == None

    def test_find_existing_laptop(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        result = test_inventory.addLaptop("L003", "Test Laptop 3", "WINXP")
        
        return_value = test_inventory.findAsset("L001")

        assert return_value.getAssetTag() == "L001"

    def test_find_non_existing_laptop(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        result = test_inventory.addLaptop("L003", "Test Laptop 3", "WINXP")
        
        return_value = test_inventory.findAsset("L004")

        assert return_value == None

    ## Test cases for getNotAvailableCamera() and getNotAvailableLaptop() ##
    def test_view_empty_camera_list_for_Not_Available(self):
        test_inventory = Inventory()

        tested_text = test_inventory.getNotAvailableCamera()
        
        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "Zoom")
        actual_text += "There is no camera to display."
        assert tested_text == actual_text

    def test_view_camera_all_available_for_Not_available(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)
        result = test_inventory.addCamera("C003", "Test camera 3", 6)
        
        tested_text = test_inventory.getNotAvailableCamera()

        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "Zoom")
        assert tested_text == actual_text

    def test_view_camera_only_not_available(self):
        test_inventory = Inventory()
        result = test_inventory.addCamera("C001", "Test camera 1", 5)
        result = test_inventory.addCamera("C002", "Test camera 2", 10)
        result = test_inventory.addCamera("C003", "Test camera 3", 6)
        test_inventory.loanLaptop("C002", "01-01-2025")
        test_inventory.loanLaptop("C003", "01-01-2025")
        
        tested_text = test_inventory.getNotAvailableCamera()

        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "Zoom")
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "C002", "Test camera 2", "No", "01-01-2025", 10)
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "C003", "Test camera 3", "No", "01-01-2025", 6)
        assert tested_text == actual_text
        
    def test_view_empty_laptop_list_for_Not_Available(self):
        test_inventory = Inventory()

        tested_text = test_inventory.getNotAvailableLaptop()
        
        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "OS")
        actual_text += "There is no laptop to display."
        assert tested_text == actual_text

    def test_view_laptop_all_available_for_Not_available(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        result = test_inventory.addLaptop("L003", "Test Laptop 3", "WINXP")
        
        tested_text = test_inventory.getNotAvailableLaptop()

        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "OS")
        assert tested_text == actual_text
        
    def test_view_laptop_only_not_available(self):
        test_inventory = Inventory()
        result = test_inventory.addLaptop("L001", "Test Laptop 1", "WINXP")
        result = test_inventory.addLaptop("L002", "Test Laptop 2", "MACOS")
        result = test_inventory.addLaptop("L003", "Test Laptop 3", "WINXP")
        test_inventory.loanLaptop("L002", "01-01-2025")
        test_inventory.loanLaptop("L003", "01-01-2025")
        
        tested_text = test_inventory.getNotAvailableLaptop()

        actual_text = "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format("AssetTag", 
                    "Description", "Available", "Due Date", "OS")
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "L002", "Test Laptop 2", "No", "01-01-2025", "MACOS")
        actual_text += "{:<10}{:<30}{:<10}{:<12}{:<10}\n".format(
            "L003", "Test Laptop 3", "No", "01-01-2025", "WINXP")
        assert tested_text == actual_text


            


