class Car:
    def __init__(self, make, model, year ,color):
        self.make =make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print(f"The {self.make} {self.model} is driving.")
  
    def get_info(self):
        return f"{self.make} {self.model}"

volvo: Car = Car("Volvo", "XC90")
volvo.drive()     
volvo.get_info()



bmw: Car = Car("BMW", "X5")
bmw.drive()




mercedes: Car = Car("Mercedes", "C-Class")
mercedes.drive()
