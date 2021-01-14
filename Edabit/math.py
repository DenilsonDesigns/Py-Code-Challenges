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


def back_to_home(directions):
    coords = [0, 0]
    for direct in [x for x in directions]:
        if direct == 'N':
            coords[0] += 1
        elif direct == 'S':
            coords[0] -= 1
        elif direct == 'W':
            coords[1] += 1
        else:
            coords[1] -= 1
    return coords == [0, 0]
# slick daddy solution:
# def back_to_home(d):
# 	return d.count('N') == d.count('S') and d.count('E') == d.count('W')


def weight_allowed(car, p, max_weight):
    return (sum(p) + car) * .453592 < max_weight


def smash_factor(bs, cs):
    return round(bs / cs, 2)


def calc_kinetic_energy(m, v):
    return round(.5 * (m * v ** 2))


# print(height(2))
# print(height(5))
# print(height(8.7))
