# class = instructions

class Person:

    def assign_name(self):
        self.name = "Mike Kramer"

    def print_name(self):  # class method ... self = object that gets created as a result of class method aka class function
        print("Mike Kramer")

mike = Person()

mike.assign_name()
mike.print_name()





