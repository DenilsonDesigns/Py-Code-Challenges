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


def binary_to_decimal(lst):
    return int("".join([str(x) for x in lst]), 2)


def outlier_number(lst):
    evens = [x for x in lst if x % 2 == 0]
    odds = [x for x in lst if x % 2 != 0]
    if len(evens) == 1:
        return evens[0]
    return odds[0]


def rotate_max_number(num):
    el = sorted([str(x) for x in str(num)], reverse=True)
    return int("".join(el))


def leap_year(year):
    if (year % 4) == 0:
        if (year % 100) == 0:
            if (year % 400) == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def average_index(letters):
    return round(sum([ord(x) - 96 for x in letters]) / len(letters), 2)


def opposite_house(house, n):
    odds = [x for x in range(0, (n * 2)) if x % 2 != 0]
    evens = sorted([x for x in range(1, (n * 2) + 1) if x %
                    2 == 0], reverse=True)
    if house % 2 == 0:
        return odds[evens.index(house)]
    return evens[odds.index(house)]
# better
# def opposite_house(house, n):
# 	return (n*2)-house+1


print(opposite_house(1, 3))
print(opposite_house(2, 3))
print(opposite_house(7, 11))
