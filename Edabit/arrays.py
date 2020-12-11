import uuid


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


def say_what(obj):
    return " ".join([v for k, v in obj.items()]) + " {}".format(obj[2])


def inclusive_list(start_num, end_num):
    return list(range(start_num, end_num + 1, 1))


def total_amount_adjectives(obj):
    return len(obj.items())


def tuck_in(lst1, lst2):
    return [lst1[0]] + lst2 + [lst1[1]]
    # probably better:
    # return lst1[:1] + lst2 + lst1[-1:]


def war_of_numbers(lst):
    evens = [x for x in lst if x % 2 == 0]
    odds = [x for x in lst if x % 2 != 0]
    return abs(sum(evens) - sum(odds))


def matrix(x, y, z):
    return [[z] * y] * x


def flatten_the_curve(lst):
    return [round(sum(lst) / len(lst), 1) if len(lst) > 0 else None] * len(lst)


def find_nemo(sentence):
    words = sentence.split(" ")
    index = words.index("Nemo") + 1 if "Nemo" in words else 0
    return "I found Nemo at {}!".format(index) if index else "I can't find Nemo :("


def number_split(n):
    a, b = int(n/2), n - int(n/2)
    return [min(a, b), max(a, b)]
    # better
    # return [n//2, n - n//2]


def parse_list(lst):
    return [str(x) for x in lst]


def find_factors(n):
    return [x for x in range(1, n+1) if n % x == 0]


def one_list(lst):
    return [x for b in lst for x in b]
    # return [value for ele in lst for value in ele]


def index_filter(indexes, string):
    return "".join([string[x] for x in indexes]).lower()


def spin_around(lst):
    lefts = sum([90 for x in lst if x == 'left'])
    rights = sum([90 for x in lst if x == 'right'])
    return int((max(lefts, rights) - min(lefts, rights)) / 360)


def first_and_last(s):
    return ["".join(sorted(list(s))), "".join(sorted(list(s), reverse=True))]


def sum_of_two(a, b, v):
    for x in a:
        for y in b:
            if x + y == v:
                return True

    return False
    # return any(i+j == v for i in a for j in b)


def get_xp(d):
    tot = 0
    tot += d['Very Easy'] * 5
    tot += d['Easy'] * 10
    tot += d['Medium'] * 20
    tot += d['Hard'] * 40
    tot += d['Very Hard'] * 80

    return str(tot) + "XP"


def get_only_evens(nums):
    return [x for i, x in enumerate(nums) if x % 2 == 0 and i % 2 == 0]


def upward_trend(lst):
    for i, x in enumerate(lst):
        if isinstance(x, str):
            return "Strings not permitted!"
        if i > 0 and lst[i-1] >= x:
            return False
    return True
    # def upward_trend(lst):
    # try:
    # 	return sorted(lst) == lst
    # except:
    # 	return "Strings not permitted!"


def count_towers(towers):
    return len([x for x in towers[len(towers) - 1][0].split(" ") if x == "##"])
    # return towers[-1][0].count('##')


def sum_two_smallest_nums(lst):
    return sum(sorted([x for x in lst if x >= 0])[0:2])


def sum_neg(lst):
    if len(lst) == 0:
        return []
    count_of_pos = len([x for x in lst if x > 0])
    sum_negs = sum([x for x in lst if x < 0])
    return [count_of_pos, sum_negs]


def hacker_speak(txt):
    return txt.replace('a', '4').replace('e', '3').replace('i', '1').replace('o', '0').replace('s', '5')
    # return txt.translate(str.maketrans('aeios', '43105'))


def numbers_sum(lst):
    return sum([x for x in lst if type(x) is int])


def maurice_wins(m_snails, s_snails):
    results = [m_snails[0] > s_snails[2], m_snails[1]
               > s_snails[0], m_snails[2] > s_snails[1]]
    return len([x for x in results if x]) >= 2


def cumulative_sum(lst):
    return [sum(lst[:i+1]) for i, x in enumerate(lst)]


def flip_end_chars(txt):
    if type(txt) is not str or len(txt) < 2:
        return "Incompatible."
    if txt[len(txt)-1] == txt[0]:
        return "Two's a pair."
    return txt[len(txt)-1] + txt[1:len(txt)-1] + txt[0]


def char_index(word, char):
    indx = [i for i, x in enumerate(word) if x == char]
    return [min(indx), max(indx)] if indx else None


def format_phone_number(lst):
    chars = [str(x) for x in lst]
    return "(" + "".join(chars[0:3]) + ") " + "".join(chars[3:6]) + "-" + "".join(chars[6:])
    # def format_phone_number(lst):
    #   return '({}{}{}) {}{}{}-{}{}{}{}'.format(*lst)


def is_good_match(lst):
    if len(lst) % 2 != 0:
        return "bad match"
    return [sum([x, lst[i-1]]) for i, x in enumerate(lst) if i % 2 != 0]


def cms_selector(lst, txt):
    return sorted([x for x in lst if txt in x])


def partially_hide(phrase):
    return " ".join([word[0] + "-" * (len(word[1:-1])) + word[-1] for word in phrase.split(" ")])


def how_many_missing(lst):
    return len(list(range(min(lst), max(lst)+1))) - len(lst)


def fifty_thirty_twenty(ati):
    r = {}
    r['Needs'] = ati * .5
    r['Wants'] = ati * .3
    r['Savings'] = ati * .2
    return r
    # Prefer:
    # return {
    # 	'Needs'  : 0.5 * ati,
    # 	'Wants'  : 0.3 * ati,
    # 	'Savings': 0.2 * ati,
    # }


def partition(txt, n):
    r = []
    while len(txt) > 0:
        r.append(txt[:n])
        txt = txt[n:]
    return r
    # one liner
    # return [txt[i:i+n] for i in range(0, len(txt), n)]


def unique_lst(lst):
    return list(dict.fromkeys([x for x in lst if x > 0]))
    # return sorted(set(x for x in lst if x>0), key=lst.index)


def lonely_integer(lst):
    for x in lst:
        if -x not in lst:
            return x
    # very clever:
    # return sum(set(lst))


def age_difference(ages):
    sort_ages = sorted(ages)
    diff = sort_ages[-1] - sort_ages[-2]
    if diff == 0:
        return "No age difference between spouses."
    if diff == 1:
        return "1 year"
    return "{} years".format(diff)


def superheroes(heroes):
    return sorted([x for x in heroes if x[-3:] == 'man' and x[-5:].lower() != 'woman'])


def puzzle_pieces(a1, a2):
    if len(a1) != len(a2):
        return False
    return len(set([x[0] + x[1] for x in list(zip(a1, a2))])) == 1


def is_special_array(lst):
    even_id = [x for i, x in enumerate(lst) if i % 2 == 0]
    odd_ids = [x for i, x in enumerate(lst) if i % 2 != 0]
    all_evs_are_ev = all([True if x % 2 == 0 else False for x in even_id])
    all_odd_are_od = all([True if x % 2 != 0 else False for x in odd_ids])
    return all_evs_are_ev and all_odd_are_od
    # better
    # return all(lst[i]%2==i%2 for i in range(len(lst)))


def ranged_reversal(lst, start, finish):
    return lst[:start] + lst[start:finish+1][::-1] + lst[finish+1:]


print(ranged_reversal([1, 2, 3, 4, 5, 6], 1, 3))
print(ranged_reversal([1, 2, 3, 4, 5, 6], 0, 4))
print(ranged_reversal([9, 8, 7, 4], 0, 0))
