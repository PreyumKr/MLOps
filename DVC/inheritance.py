class Animal:
    def __init__(self):
        self.name = "Buddy"

    def speak(self):
        return f"{self.name} makes a sound."
    
class Dog(Animal):
    # If No init was defined here, it would inherit Animal's init
    def __init__(self):
        # Inherit Main Class Constructor
        super().__init__()
        # Add extra attributes
        self.breed = "Golden Retriever"

    def speak(self):
        return f"{self.name} barks."
    
dog = Dog()
print(dog.speak())