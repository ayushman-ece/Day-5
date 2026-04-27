class Employee:
    companyName = "Apple" #class
    def __init__(self, name): #class
        self.name = name
        self.raise_amount = 0.02
    def showDetails(self):
        print(f"The name of the Employee is {self.name} and the raise amont in {self.companyName} is {self.raise_amount}") 

emp1 = Employee("Harry")
emp1.raise_amount = 0.3 # Instace
emp1.companyName = "Apple India" #Instance
emp1.showDetails()

emp2 = Employee("Rohan")
emp2.showDetails()
