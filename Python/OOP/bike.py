class Bike(object):
    def __init__(self,price,max_speed,miles):
        self.price = price
        self.max_speed = max_speed
        self.miles = miles
    def ride(self):
        self.miles += 10
        print "riding"
        return self
    def displayinfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self

    def reverse(self):
        print 'reversing'
        self.miles -= 5
        return self

x = Bike(300, 20,200)
x.ride().displayinfo().reverse().displayinfo()


