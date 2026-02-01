# class animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} makes a sound."

# class fourlegged(animal):
#     def walk(self):
#         return f"{self.name} walks on four legs."

# class dog(fourlegged):
#     def bark(self):
#         return f"{self.name} barks."

# my_dog = fourlegged("Buddy")
# my_dog2 = dog("Max")

# print(my_dog.speak())
# print(my_dog.walk())

# print(my_dog2.speak())
# print(my_dog2.bark())

class papa:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, I am {self.name}.")


class son(papa):

    def greet(self):
        print(f"Hi, I am the son. My parent is Below")
        super().greet()
    
class daughter(papa):
    def greet(self):
        print(f"Hi, I am the daughter. My parent is Below")
        super().greet()
    
class incest(son, daughter):
    def greet(self):
        print(f"Hi, I am the incest child. My parents are Below")
        super().greet()

child = incest("Yogesh")