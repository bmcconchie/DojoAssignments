
import copy

class User(object):
    def __init__(self,first_name,last_name,age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Usersdb(object):
    def __init__(self):
        self.contents = []
        self.nextid = 0

    def create(self,first_name,last_name,age):
        user = User(first_name,last_name,age)
        user.id = self.nextid 
        self.nextid +=1
        self.contents.append(user)
        return (self)
    def all(self):
        return self.contents[:]
    def get(self,id):
        for user in self.contents:
            if user.id == id:
                return copy.deepcopy(user)

        return None


users = Usersdb()
users.create('dave', 'johnstone', 34)
print users.get(0).first_name
print users.get(0).last_name
print users.get(0).age
print users.nextid
        
dave = users.get(0)
print dave.first_name
        
        
        




