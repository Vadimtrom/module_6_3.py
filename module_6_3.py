import random
class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]
    def __init__(self, speed):
        self.speed = speed

    def move(self, dx, dy, dz):
        self._cords[0] += dx * self.speed
        self._cords[1] += dy * self.speed
        self._cords[2] += dz * self.speed
        if self._cords[2] <= 0:
            print("It's too deep, i can't dive :(")
            self._cords[2] = 0

    def get_cords(self):
        print(f'Координаты:\n'
              f'X: {self._cords[0]} \n'
              f'Y: {self._cords[1]} \n'
              f'Z: {self._cords[2]}')

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:
            print('Sorry, i`m peaceful :)')
        else:
            print('Be careful, i`m attacking you O_O')

    def speak(self):
        print(self.sound)

class Bird(Animal):
    beak = True

    def lay_eggs(self):
        egg = random.randint(1, 4)
        print(f'Here are(is) {egg} eggs for you')

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3
    def __init__(self, speed):
        super().__init__(speed)

    def dive_in(self, dz):
        self._cords[2] -= int((self.speed * abs(dz))/2)

class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"


db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()