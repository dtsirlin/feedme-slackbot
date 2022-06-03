class SelectionMessage():

    def __init__(self, selectedLocation):
        self.name = selectedLocation['name']
        self.address = selectedLocation['address']
        self.menuLink = selectedLocation['menuLink']
        self.instagram = selectedLocation['instagram']
        self.contactEmail = selectedLocation['contactEmail']
        self.contactNumber = selectedLocation['contactNumber']
        self.category = selectedLocation['category']
