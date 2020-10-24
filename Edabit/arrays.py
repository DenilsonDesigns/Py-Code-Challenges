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


# def test_fairness(agatha, bertha):
#     return [[j[0] * j[1] in j] for x in agatha]


print(test_fairness([[1, 5], [6, 3], [1, 1]], [[7, 1], [2, 2], [1, 1]]))
print(test_fairness([[2, 2], [2, 2], [2, 2], [2, 2]], [[4, 4]]))
