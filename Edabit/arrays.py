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


print(next_in_line([], 6))
print(next_in_line([5, 6, 7, 8, 9], 1))
