class item():
    def __init__(self, assertTag, description):
        self.assertTag = assertTag
        self.description = description
        self._dueDate = ""
        self._isAvailable = True

    def getAssetTag(self):
        return self.assertTag
    
    def getDescription(self):
        return self.description
    
    def getDueDate(self):
        return self._dueDate
    
    def getIsAvailable(self):
        if self._isAvailable:
            return "Yes"
        else:
            return "No"
        
    def setDueDate(self, dueDate):
        self._dueDate = dueDate

    def setIsAvailable(self, isAvailable):
        self._isAvailable = isAvailable

    def __str__(self):
        return "{:<10}{:<30}{:<10}{:<12}".format(
            self.assertTag, self.description, 
            self.getIsAvailable(), self.getDueDate())