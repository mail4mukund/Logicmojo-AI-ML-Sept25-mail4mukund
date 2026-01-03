class Car:
    # def __init__(): # Not allowed as it will not take self parameter
    #     pass
    def __init__(self, name, model, color,year=2025):
        self.name = name
        self.model = model
        self.color = color
        self.year = year
    def start(self):
        print(f'{self.name} is starting')
    def stop(self):
        print(f'{self.name} is stopping')
    def getDetails(self):
        print(f'Car name is {self.name}, model is {self.model}, Year is {self.year} and color is {self.color}')

objCar1 = Car('BMW', 'X5', 'Black')
objCar2 = Car('Audi', 'Q7', 'White') 

objCar1.start()
objCar1.getDetails()    
objCar1.stop()  
objCar2.start()
objCar2.getDetails()
objCar2.stop()

# objCar3=Car() # This will give error as __init__ is expecting 3 parameters
# #objCar3
# objCar3 = Car() # TypeError: __init__() missing 3 required positional arguments: 'name', 'model', and 'color'

