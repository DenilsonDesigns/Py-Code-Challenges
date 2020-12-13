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


print(is_automorphic(36))
print(is_automorphic(5))
print(is_automorphic(25))
