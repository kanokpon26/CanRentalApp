class CarItem:
    def __init__(self, image, carId, carType, price, availability):
        self.image = image
        self.carId = carId
        self.carType = carType
        self.price = price
        self.availability = availability
    
    def getImage(self):
        return self.image

    def setImage(self, image):
        self.image = image

    def getCarId(self):
        return self.carId

    def setCarId(self, carId):
        self.carId = carId

    def getCarType(self):
        return self.carType

    def setcarType(self, carType):
        self.carType = carType

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getAvailability(self):
        return self.availability

    def setAvailability(self, availability):
        self.availability = availability
    
    def __str__(self):
        return f'Car: {self.carId, self.carType} Price: {self.price} Availability: {self.availability}'



    
    