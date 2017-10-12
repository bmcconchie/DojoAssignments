class Car(object):
    def __init__(self,price,speed,fuel,mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12 
    
    def display_all(self):
        print self.price
        print self.speed
        print self.fuel
        print self.mileage
        print self.tax
        return self

car1 =Car(2000, '35mph','full','15mph')
car1.display_all()



        

       