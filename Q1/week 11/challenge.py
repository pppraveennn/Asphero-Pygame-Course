class Phone:
    def __init__(self, color, brand, year, battery, storage):
        self.color = color
        self.brand = brand
        self.year = year
        self.battery = battery
        self.storage = storage
    def text(self, msg):
        print(msg)
        self.battery += -1
    def takePhoto(self):
        print("photo taken")
        self.battery += -1
        self.storage += -1