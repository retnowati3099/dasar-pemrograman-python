# class Car:
#     def __init__(self):
#         self.make = ""
#         self.model = ""
#         self.year = 0

#     def description(self):
#         return f"{self.year} {self.make} {self.model}"


# car1 = Car()
# car1.make = "Toyota"
# car1.model = "Corolla"
# car1.year = 2020
# print(car1.description())


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"


car1 = Car("Toyota", "Corolla", "2020")
print(car1.description())

"""
Create a class Car with attributes make, model, and year. Define an instance method description that returns a string in the format "year make model"
"""
