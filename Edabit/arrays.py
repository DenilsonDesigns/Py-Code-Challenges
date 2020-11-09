def cpp_txt(lst):
    return "".join(lst)[:-1]


def second_largest(lst):
    return sorted(lst)[-2]


def get_filename(path):
    return path.split("/")[-1]


def find_none(lst):
    return lst.index(None) if None in lst else -1


def check_equals(lst1, lst2):
    return lst1[::] == lst2[::]


def list_between(num1, num2, lst):
    return [x for x in lst if num1 < x < num2]


def list_to_string(lst):
    return "".join(str(x) for x in lst)


def sum_found_indexes(lst, n):
    return sum([i for i, x in enumerate(lst) if x == n])


def filter_state_names(lst, cat):
    if cat == "abb":
        return [x for x in lst if len(x) == 2]
    else:
        return [x for x in lst if len(x) > 2]


def all_truthy(*args):
    return all(args)


def cap_me(lst):
    return [x.title() for x in lst]


def test_fairness(agatha, bertha):
    return sum([x[0] * x[1] for x in agatha]) == sum([x[0] * x[1] for x in bertha])

# using nested list comprehension


def count_characters(lst):
    return sum([len(y) for x in lst for y in x])
# or just:
# def count_characters(lst):
# 	return len("".join(lst))


def add_indexes(lst):
    return [i + el for i, el in enumerate(lst)]


def unique_sort(lst):
    return sorted(set(lst))


def letter_counter(lst, letter):
    return sum([1 for x in lst for y in x if y == letter])
# more concise
# def letter_counter(lst, letter):
# 	return str(lst).count(letter)


def filter_list(lst):
    return [x for x in lst if not isinstance(x, str)]


def index_multiplier(lst):
    return sum([i * el for i, el in enumerate(lst)])


def find_even_nums(num):
    return [x for x in range(1, num + 1) if x % 2 == 0]
# slightly more pythonic
# def find_even_nums(num):
# 	return [ x for x in range(2,num+1,2)]


def get_budgets(lst):
    return sum([x['budget'] for x in lst])


def correct_stream(user, correct):
    return [1 if a == b else -1 for a, b in list(zip(user, correct))]


def find_bob(names):
    return names.index("Bob") if "Bob" in names else -1


def is_subset(lst1, lst2):
    return all(elem in lst2 for elem in lst1)


def get_student_names(students):
    # either way werks
    # return sorted([v for k, v in students.items()])
    return sorted([x for x in students.values()])


def find_odd(lst):
    return [x for x in lst if lst.count(x) % 2 != 0][0]


def society_name(friends):
    return "".join([x[0] for x in sorted(friends)])


def convert_cartesian(x, y):
    return [[i, j] for i, j in zip(x, y)]


def next_in_line(lst, num):
    if len(lst) > 0:
        return lst[1:] + [num]
    return "No list has been selected"
# better
# def next_in_line(lst, num):
# 	return lst[1:] + [num] if lst else "No list has been selected"


def simon_says(lst1, lst2):
    return lst1[:len(lst2)-1] == lst2[1:]


def move_to_end(lst, el):
    return [x for x in lst if x != el] + [x for x in lst if x == el]
# using sorting
# def move_to_end(lst, el):
# 	return sorted(lst, key=lambda x: x is el)


def probability(lst, n):
    return round(len([x for x in lst if x >= n]) / len(lst) * 100, 1)


def amplify(num):
    return [x if x % 4 != 0 else x*10 for x in range(1, num + 1)]


def sort_by_length(lst):
    return sorted(lst, key=len)


def marathon_distance(d):
    return sum([abs(x) for x in d]) == 25


def mapping(letters):
    return {x: x.upper() for x in letters}


def return_only_integer(lst):
    return [x for x in lst if type(x) is int]


def clone(lst):
    lst.append(lst[:])
    return lst


def remove_enemies(names, enemies):
    return [x for x in names if x not in enemies]


def sum_of_evens(lst):
    return sum([x for b in lst for x in b if x % 2 == 0])


def remove_smallest(lst):
    if lst:
        lst.remove(min(lst))
    return lst


def nth_smallest(lst, n):
    return sorted(lst)[n-1] if len(lst) > n - 1 else None


def magnitude(list):
    return sum([x**2 for x in list]) ** (0.5)


def odd_or_even(word):
    return True if len(word) % 2 == 0 else False


def integer_boolean(n):
    return [True if x == '1' else False for x in list(n)]
# more cleverer way
# def integer_boolean(n):
# 	return [i == '1' for i in str(n)]


def jazzify(lst):
    return [x + "7" if x[len(x)-1] != "7" else x for x in lst]
    # return [x[:len(x)] + "7" for x in lst]


def get_discounts(nums, d):
    percent = int(d[:- 1]) / 100
    return [x * percent for x in nums]


def cube_squareroot(num):
    return num**(3/2)


def list_operation(x, y, n):
    return [x for x in range(x, y) if x % n == 0]


def trace(lst):
    sum = 0
    ind = 0
    for arr in lst:
        sum += arr[ind]
        ind += 1
    return sum
# genius solution
# def trace(arr):
# 	return sum(arr[i][i] for i in range(len(arr)))


def to_list(num):
    return [int(x) for x in list(str(num))]


def to_number(lst):
    return int("".join([str(x) for x in lst]))


def prep_region_ids(region_str=""):
    if len(list(region_str)) == 0:
        return False
    return tuple([x.strip() for x in region_str.split(',')])


def calc_diff(obj, limit):
    return sum([v for k, v in obj.items()]) - limit
# cleaner
# def calc_diff(m, n):
#   return sum(m.values()) - n


def greet_people(names):
    return "".join(["Hello " + x + ", " for x in names])[:-2]


def factor_chain(lst):
    for i, el in enumerate(lst):
        if i < len(lst)-1:
            if lst[i + 1] % el != 0:
                return False
    return True
# my fav solution
# def factor_chain(lst):
# 	return all(lst[i] % lst[i-1] == 0 for i in range(1, len(lst)))


def last(a, n):
    if n == 0:
        return []
    if n > len(a):
        return "invalid"
    return a[len(a) - n:]

# better
# def last(a, n):
#   return 'invalid' if n>len(a) else a[len(a)-n:]


def chatroom_status(users):
    if len(users) == 0:
        return "no one online"
    if len(users) == 1:
        return "{} online".format(users[0])
    if len(users) == 2:
        return "{} and {} online".format(users[0], users[1])
    return "{}, {} and {} more online".format(users[0], users[1], len(users)-2)


def total_volume(*boxes):
    return sum([x[0] * x[1] * x[2] for x in boxes])

# better
# def total_volume(*boxes):
# 	return sum([x*y*z for x,y,z in boxes])


print(total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]))
print(total_volume([2, 2, 2], [2, 1, 1]))
print(total_volume([1, 1, 1]))
