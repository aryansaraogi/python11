class Car:
    def __init__(self, make, model):
        self.make =make
        self.model = model
    
    def drive(self):
        print("The {self.make} {self.model} is driving.")
    


volvo: Car = Car("Volvo", "XC90")
volvo.drive()
    