# class Hamburger(object):
#     def __init__(self,bread,cheese):
#         self.bread = bread
#         self.cheese = cheese

#     ham1 =Hamburger('onion', 'chedder')
#     ham2 =Hamburger('plain', 'american')

# class is a blueprint for creating an object
# objects are instances created from a blueprint

class Ninja(Turtle):
    def __init__(self,weapon,color,hasShell=True):
        super(Ninja,self).__init__(color,hasShell)
        self.weapon = weapon
        self.color = color

class Turtle(object):
    def __init__(self,skin_color,hasShell):
        self.skin_color = skin_color
        self.hasShell = hasShell

newNinja = Ninja("sai","blue")