#class syntax
class Car:
    def __init__(self, make, model, year, miles, price): #always need to have init or Python will run pre-defined init
        #All variables belong to the class always have syntax: "self".[variable name]
        self.make = make 
        self.model = model
        self.year = year
        self.miles = miles
        self.price = price
        
    #user define string function for the class. 
    #For more info: https://www.pythontutorial.net/python-oop/python-__str__/
    def __str__(self):
        # ... This line will cause error until method is implemented
        return('%d %s %s \n Milleage:%s \n Sticker price:$%d'%(self.year, self.make, self.model, self.miles, self.price))
    
cars = [] #a list of car's object
cars.append(Car('Ford', 'Mustang', 2013, 25000, 37999))
cars.append(Car('Nissan', 'Xterra', 2004, 89500, 7500))
cars.append(Car('Nissan', 'Mazda', 2012, 25000, 15750))

for car in cars:# print out car in the list
    print(car)
