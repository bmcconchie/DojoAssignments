class Dog(object):
    def __init__(self,name,owner):
        self.name = name
        self.owner = owner

    def speak(self,otherDog):
        print '{} barked at {}'.format(self.name, otherDog.name)
        # print 'growl'
        return self




d1 =Dog('thor', 'Brian')
d2 =Dog('fuu','Danny')

d2.speak(d1)

    # def lick(self):
    #     print 'licking your face'
    #     return self

# pet1 = Dog('thor','Brian')
# print pet1.name, pet1.owner
# print pet1.speak(), pet1.lick()

        
        
