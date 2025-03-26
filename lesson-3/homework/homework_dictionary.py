#global makes progress

print("\n=== Dictionary Tasks ===")
sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2}

# 1
def get_value(dct, key):
    return dct.get(key)
print("1. Value of 'a':", get_value(sample_dict, 'a'))
# Hey this grab value for 'a' so easy! It use .get() which don’t yell if key gone, just chill with None. Here 'a' got 1 so we see that, nice huh!

# 2
def check_key(dct, key):
    return key in dct
print("2. Has 'b'?", check_key(sample_dict, 'b'))
# This like peekin if 'b' in there, yeah? Use 'in' and it say True if 'b' hangin out. Got 'b' with 2 so True pop up, sweet!

# 3
def count_keys(dct):
    return len(dct)
print("3. Key count:", count_keys(sample_dict))
# Countin keys real quick here! Len() tell how many pair we got, and with 'a', 'b', 'c', 'd' that four, so 4 it is—boom!

# 4
def get_all_keys(dct):
    return list(dct.keys())
print("4. Keys:", get_all_keys(sample_dict))
# Pullin all key out in list, fun stuff! .keys() show em and list() make it real nice. We got 'a', 'b', 'c', 'd' so that what we see—cool!

# 5
def get_all_values(dct):
    return list(dct.values())
print("5. Values:", get_all_values(sample_dict))
# Now we snatch all value, not k\

# 6
def merge_dicts(dct1, dct2):
    return {**dct1, **dct2}
print("6. Merge:", merge_dicts({'x': 1}, {'y': 2}))
# Smashin two dict together, whoa! That ** thing mix em up goo

# 7
def remove_key(dct, key):
    new_dict = dct.copy()
    new_dict.pop(key, None)
    return new_dict
print("7. Remove 'b':", remove_key(sample_dict, 'b'))
# Kickin 'b' outta here! Copy first so o None if it miss!

# 8
def clear_dict(dct):
    return {}
print("8. Cleared:", clear_dict(sample_dict))
# Wipin dict clean, like new! Don’t even toucom sample_dict, see them curly brace—empty!

# 9
def is_dict_empty(dct):
    return len(dct) == 0
print("9. Is empty?", is_dict_empty(sample_dict))
# Checkin if dict got nothin! Len() say 0 if em full, yo!

# 10
def get_key_value_pair(dct, key):
    return (key, dct[key]) if key in dct else None
print("10. Pair 'a':", get_key_value_pair(sample_dict, 'a'))
# Grabbin key and value together, cute tu

# 11
def update_value(dct, key, value):
    new_dict = dct.copy()
    new_dict[key] = value
    return new_dict
print("11. Update 'a' to 5:", update_value(sample_dict, 'a', 5))
# Changin 'a' value to 5, fun! Copy dict so we don’t mess original, then slap 5 in 'a'. Was 1, now 5, x!

# 12
def count_value_occurrences(dct, value):
    return list(dct.values()).count(value)
print("12. Count of 2:", count_value_occurrences(sample_dict, 2))
# Countin how many 2 we got in value! Make list .count() say 2 twice—for 'b' and 'd', so 2 it t!

# 13
def invert_dict(dct):
    return {v: k for k, v in dct.items()}  # Assumes unique values
print("13. Inverted:", invert_dict({'a': 1, 'b': 2}))
# Flippin dict upside downe simple one here,wild!

# 14
def find_keys_with_value(dct, value):
    return [k for k, v in dct.items() if v == value]
print("14. Keys with 2:", find_keys_with_value(sample_dict, 2))
# Huntin key that got 2, yep key. 'b' and 'd' both 2, so ['b', 'd']—found em!

# 15
def dict_from_lists(keys, values):
    return dict(zip(keys, values))
print("15. From lists:", dict_from_lists(['x', 'y'], [1, 2]))
# Makin dict from two list, d it. We get {'x': 1, 'y': 2}—like magic trick!

# 16
def has_nested_dict(dct):
    return any(isinstance(v, dict) for v in dct.values())
print("16. Has nested?", has_nested_dict({'a': 1, 'b': {'x': 2}}))
# Lookin if any value a dict True. Here 'b' got {'x': 2}, so True—nested party!

# 17
def get_nested_value(dct, outer_key, inner_key):
    return dct.get(outer_key, {}).get(inner_key)
print("17. Nested 'b'->'x':", get_nested_value({'b': {'x': 2}}, 'b', 'x'))
# Diggin deep for nested value, whoa! Get 'b'iss, no crash, but we hit gold here!

# 18
from collections import defaultdict
def create_default_dict(default_value):
    return defaultdict(lambda: default_value)
d = create_default_dict(0)
d['a'] = 1
print("18. Default (0):", d['b'])
# Makin dict that give 0 if key gone, cool! Dot there so 0—smooth!

# 19
def count_unique_values(dct):
    return len(set(dct.values()))
print("19. Unique values:", count_unique_values(sample_dict))
# Countin different value, yeah! Set make dict got 3 unique—quick look!

# 20
def sort_by_key(dct):
    return dict(sorted(dct.items()))
print("20. Sort by key:", sort_by_key(sample_dict))
# Sortin key all nice! Sorted() line em  back together. Look clean now, huh!

# 21
def sort_by_value(dct):
    return dict(sorted(dct.items(), key=lambda x: x[1]))
print("21. Sort by value:", sort_by_value(sample_dict))
# Sortin by value this time Two !

# 22
def filter_by_value(dct, condition):
    return {k: v for k, v in dct.items() if condition(v)}
print("22. Values > 1:", filter_by_value(sample_dict, lambda x: x > 1))
# Keepin only big value Check each pair, if value over 1, Bigger  win!

# 23
def common_keys(dct1, dct2):
    return bool(set(dct1.keys()) & set(dct2.keys()))
print("23. Common keys?", common_keys({'a': 1}, {'a': 2, 'b': 3}))
# Seein if key match up so True. No match be False—quick check!

# 24
def dict_from_tuple(tup):
    return dict(tup)
print("24. From tuple:", dict_from_tuple((('a', 1), ('b', 2))))
# Turn tuple  ! Each pair in tuple like. Simple 

# 25
def first_key_value_pair(dct):
    return next(iter(dct.items())) if dct else None
print("25. First pair:", first_key_value_pair(sample_dict))
# Grabbin first pair, 'a': 1 in sample_dict—so ('a', 1). First come, first serve!