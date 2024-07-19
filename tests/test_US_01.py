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