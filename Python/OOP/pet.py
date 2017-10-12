# pet1 = {'name': 'frankie', 'age': 6,'fur': 'golden'}
# print pet1
# pet2 = {'name': 'sunny', 'age': 12,'fur': 'yellow'}


class Pet(object):
    def __init__(self, name, age, fur):
        self.name = name
        self.age = age
        self.fur = fur
        self.legs = 4
        
    def speak(self):
        print 'grrrrrrrrrrrrr'
        return self
    def move(self):
        print "I'm moving"
        print " Im done moving"
        return self
pet1 = Pet('tina',0.1,'grey')

print pet1.name, pet1.age, pet1.fur, pet1.legs
pet1.speak().move().speak().move()
pet1.legs = 3
print pet1.legs



