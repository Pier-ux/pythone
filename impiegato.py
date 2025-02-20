
class Employee:
    def __init__(self, name, surname, salary):
        self._name = name
        self._surname = surname
        self._salary = salary
    def __repr__(self):
        return self._name + " " + self._surname + " " + str(self._salary)
class Manager(Employee):
    def __init__(self, name, surname, salary, department):
        super().__init__(name, surname, salary)
        self._department = department
    def __repr__(self):
        return self._name + " " + self._surname + " " + str(self._salary) + " " + self._department
    

x = Employee("Pierangelo" , "Quarato", 3000)
y = Manager("Grent" , "Sota", 2500 , "IT")
print(x)
print(y)
