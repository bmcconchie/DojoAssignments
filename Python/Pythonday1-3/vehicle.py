class Vehicle(object):
    def __init__(self,color,typeof,speed,noise):
        self.color = color
        self.typeof = typeof
        self.speed = speed
        self.noise = noise

    def honk(self):
        print 'ahahahaha'
        return self

    
veh1 = Vehicle('white','truck',60,'loud')

print veh1.color, veh1.typeof, veh1.speed, veh1.noise, veh1.honk()



