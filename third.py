class Car:  
   def start(self, a, b=None):
        if b is not None:
            print (a + b)
        else:
            print (a)



car_a = Car()  
car_a.start(10)

car_a.start(10, 20)


class Vehicle:  
    def print_details(self):
        print("Это родительский метод из класса Vehicle")
 
# создание класса, который наследует Vehicle
class Car1(Vehicle):  
    def print_details(self):
        print("Это дочерний метод из класса Car")
 
# создание класса Cycle, который наследует Vehicle
class Cycle(Vehicle):  
    def print_details(self):
        print("Это дочерний метод из класса Cycle")


car_a = Vehicle()  
car_a. print_details()
 
car_b = Car1()  
car_b.print_details()
 
car_c = Cycle()  
car_c.print_details()