class Bottle:
    # constructor to construct object with given values
    # assigning local variable to self so we can use in 
    # all the methods created inside class
    def __init__(self,id,brand,capacity,color):
        self.id=id
        self.brand=brand
        self.capacity=capacity
        self.color=color
        print(f"Bottle created with Id {self.id}")
        
    # all methods and constructors of class can use by all objects
    def display(self):
        print(f"------------------------Id: {self.id}------------------------")
        print(f"Bottle brand {self.brand}, Color: {self.color}")
        print(f"Capacity: {self.capacity} ltr")
        
        
bottle1= Bottle(1,"Tupperware",2,"Red") 
bottle2= Bottle(2,"Trueware",1,"blue") 
bottle3= Bottle(3,"Tupperware",1,"pink")  

bottle1.display()
bottle2.display()
bottle3.display()