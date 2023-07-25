class Engine:
    
     def start(self):
          print("starting...")
     
     def prepearing(self):
          print("prepearing...")
     

class Car:
     def __init__(self, name):
          self.name = name
          self.engine = Engine()

     def drive(self):
          print(f"The Car of {self.name}")
          self.engine.prepearing()
          self.engine.start()
         

car_1 = Car("Tosho")
car_1.drive()
