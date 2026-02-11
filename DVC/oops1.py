# Creating a class

class employee:
    # constructor
    def __init__(self):
        self.id = 123
        self.salary = 50000 
        self.designation = "SDE"
    
    def travel(self, destination):
        print("Employee is traveling to", destination)



# Creating an object or instance of class employee
sam = employee()

print(sam.salary)
sam.travel("Chennai")