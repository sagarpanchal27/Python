
class Dog:
    def __init__(self, name, day, month, year, sound):
        self.name = name
        self.day = day
        self.month = month
        self.year = year
        self.sound = sound

    def speak(self):
        return self.sound

    def birthDate(self):
        return "{}-{}-{}".format(self.day, self.month, self.year)

    def changeBark(self, sound):
        self.sound = sound

    def speak(self):
        return self.sound

if __name__ == '__main__':
    boyDog = Dog("Mesa", 5, 15, 2004, "WOOOF")
    girlDog = Dog("Sequoia", 5, 6, 2004, "barkbark")
    print(boyDog.speak())
    print(girlDog.speak())
    print(boyDog.birthDate())
    print(girlDog.birthDate())
    boyDog.changeBark("woofywoofy")
    print(boyDog.speak())
