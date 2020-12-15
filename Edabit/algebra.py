import math


def calculator(txt):
    return eval(txt)


def how_many_stickers(n):
    return n ** 2 * 6


def imposter_formula(i, p):
    return "{}%".format(round(i/p*100))


def calculate(num1, num2, op):
    return eval("{} {} {}".format(num1, op, num2))


def num_layers(n):
    return str(0.0005 * 2**n) + "m"


def compound_interest(p, t, r, n):
    return p * ((1 + (r/n)) ** (n * t))
    # return round(p * (1 + (r / n))**(n * t), 2)


def abcmath(a, b, c):
    total = a
    for _ in enumerate(range(0, b)):
        total = total * 2
    return total % c == 0
    # return not a*2**b%c


def is_automorphic(n):
    return int(repr(n ** 2)[-len(str(n)):]) == n


def count(deck):
    return sum([1 if x in [2, 3, 4, 5, 6] else 0 if x in [7, 8, 9] else -1 for x in deck])


def total_distance(height, length, tower):
    return round(tower / height * (height + length), 1)


def color_invert(rgb):
    return tuple(255 - c for c in rgb)


def get_distance(a, b):
    return round(math.sqrt((a['x'] - b['x'])**2 + (a['y'] - b['y'])**2), 3)


def adjacent_product(lst):
    return max(a*b for a, b in zip(lst, lst[1:]))


print(adjacent_product([3, 6, -2, -5, 7, 3]))
print(adjacent_product([5, 6, -4, 2, 3, 2, -23]))
print(adjacent_product([0, -1, 1, 24, 1, -4, 8, 10]))
