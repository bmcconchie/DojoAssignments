class Fighter(object):
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
    def hit(self, otherFighter):
        otherFighter.health -= self.attack
        print '{} attacked {} for {} damage.'.format(self.name,otherFighter.name, self.attack)

        print '{} is at {} health.'.format(otherFighter.name, otherFighter.health)
        return self



ray = Fighter('ray', 9000, 3)
choi = Fighter('choi', 9000, 1)
ray.hit(choi)
choi.hit(ray)

    
