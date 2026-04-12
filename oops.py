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

  

philpes:Microwave = Microwave("Philips", 1000)
print(philpes)  


whirpool:Microwave = Microwave("Whirlpool", 1200)
print(whirpool)         

smeg:Microwave = Microwave("Smeg", 800)
print(smeg)

 