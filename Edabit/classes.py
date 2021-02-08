class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def compare_age(self, other):
        if self.age < other.age:
            return "{} is older than me.".format(other.name)
        if self.age == other.age:
            return "{} is the same age as me.".format(other.name)
        return "{} is younger than me.".format(other.name)


import math


class Rectangle:

    def __init__(self, sideA=0, sideB=0):
        self.sideA = sideA
        self.sideB = sideB

    def getArea(self):
        return self.sideA * self.sideB

    def getPerimeter(self):
        return 2 * (self.sideA + self.sideB)


class Circle:
    def __init__(self, radius):
        self.r = radius

    def getArea(self):
        return math.pi * (self.r)**2

    def getPerimeter(self):
        return 2 * math.pi * self.r


class Calculator:
    def add(self, p1, p2):
        return p1 + p2

    def multiply(self, p1, p2):
        return p1 * p2

    def subtract(self, p1, p2):
        return p1 - p2

    def divide(self, p1, p2):
        return p1 / p2


class player():
    def __init__(self, name, age, height, weight):
        # complete function
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def get_age(self):
        return "{} is age {}".format(self.name, self.age)

    def get_height(self):
        return "{} is {}cm".format(self.name, self.height)

    def get_weight(self):
        return "{} weighs {}kg".format(self.name, self.weight)


class Employee:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.email = "{}.{}@company.com".format(
            firstname.lower(), lastname.lower())
        self.fullname = "{} {}".format(firstname, lastname)


class ones_threes_nines:
    def __init__(self, num):
        self.ones = int(num // 1)
        self.threes = int(num // 3)
        self.nines = int(num // 9)


class User:
    user_count = 0

    def __init__(self, name):
        User.user_count = User.user_count + 1
        self.username = name


class Composer:
    count = 0

    def __init__(self, name, dob, country):
        Composer.count = Composer.count + 1
        self.name = name
        self.dob = dob
        self.country = country


class Name:

    def __init__(self, fname, lname):
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()
        self.fullname = "{} {}".format(self.fname, self.lname)
        self.initials = "{}.{}".format(self.fname[0], self.lname[0])


u1 = User("johnsmith10")
u2 = User("marysue1989")
u3 = User("milan_rodrick")
print(User.user_count)
print(u2.username)
print(u3.username)
