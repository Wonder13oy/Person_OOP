class Person:

    def __init__(self, name, age, gender, *interests):
        self.name = name
        self.age = age
        self.gender = gender
        self.interests = interests

    def greeting(self):
        greet = f'Hi, my name is {self.name} and I am {self.age} years old. My interests are {self.interests[0]}'

        for x in self.interests[1:]:
            greet += f', {x}'

        return greet
