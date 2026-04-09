class Microwave:

     plant:str
     turned_on:bool = False
     size:int     


     def __init__(self,brand:str,Power:int,):
        self.brand = brand
        self.Power = Power
        self.turned_on = False  
        self.plant = "Kitchen"
        self.size = 20

  

bosch:Microwave = Microwave("Bosch", 1000)
print(bosch)

perfect:Microwave = Microwave("Perfect", 1200)
print(perfect)  


smeg:Microwave = Microwave("Smeg", 800)
print(smeg)

 