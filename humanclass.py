class Human:
    def __init__(self, eyes, hair_color, legs, gender, height):
        self.eyes = eyes
        self.hair_color = hair_color
        self.legs = legs
        self.gender = gender
        self.height = height

    def walking(self):
        print("I am walking")

    def speaking(self):
        print("I am talking")

    def breathing(self):
        print("I am breathing")


# Example usage
person = Human(2, "Black", 2, "Male", "5.9ft")
person.walking()
person.speaking()
person.breathing()
print(person.eyes)
print(person.hair_color)
print(person.legs)
print(person.gender)
print(person.height)