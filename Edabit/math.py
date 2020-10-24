def calc_age(age):
    return age * 365


def circuit_power(voltage, current):
    return voltage * current


def list_less_than_100(lst):
    return sum(lst) < 100


def area_shape(base, height, shape):
    if shape == "triangle":
        return 0.5 * base * height
    return base * height


def absolute(n):
    if n < 0:
        return n - n * 2
    return n
# better
# def absolute(n):
    # return -n if n < 0 else n


print(absolute(-5))
print(absolute(-5.25))
print(absolute(250))
