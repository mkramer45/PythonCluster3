class Person:
    def __init__(self, name, hair_color, height):
        self.name = name
        self.hair_color = hair_color
        self.height = height

    def print_name(self, another_value):
        print(self.name + another_value)

    def print_height(self):
        print(self.height)

    def print_hair_color(self):
        print(self.hair_color)

class Employee(Person):
    def __init__(self, name: object, hair_color: object, height: object, employee_id: object) -> object:
        Person.__init__(self, name, hair_color, height)
        self.employee_id = employee_id

    def print_employee_id(self):
        print(self.employee_id)

    def print_employee_hair(self):
        print(self.hair_color)


mike_the_employee = Employee("Mike Kramer", "brown", "6'2''", "a123")
mike_the_employee.print_employee_id()
mike_the_employee.print_employee_hair()

