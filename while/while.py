# class Car:
#     def __init__(self,model,year):
#         self.model = model
#         self.year = year

#     def __str__(self):
#         return f"my car is  {self.model} year: {self.year}"

# car = Car("Bmw","1998")

# print(car)


# class Car:
#     def __init__(self,name,year):
#         self.name = name
#         self.year = year

#     def __str__(self):
#         return f"{self.name} {self.year}"

# cars = Car("bmw","1999")
# print(cars)

# def add(x,y):
#     return x + y
# print(add(2,3))

# add = lambda x,y:x + y
# print(add(2,3))

# def add(number):
#     return len(str(number))

# numbers = [1, 123, 45, 6789, 12]
# numbers.sort(key=add)
# print(numbers)


city = ["Moscow: -5", "Baku: +3", "Spb: -7","Amsterdam: 1"]

city.sort(key=lambda temperature : int(temperature.split(":")[1].strip()))
print(city)
