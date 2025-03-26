#in my code i have used global variable to make them all manageable from one variable :)
print("\n=== List Tasks ===")
sample_list = [1, 3, 2, 3, 4, -1, 5, 2]

# 1
def count_occurrences(lst, elem):
    return lst.count(elem)
print("1. Count of 3:", count_occurrences(sample_list, 3))  
# from my calculations my output is  2

# 2
def sum_elements(lst):
    return sum(lst)
print("2. Sum:", sum_elements(sample_list))
# Output will be 19

# 3. how to find max element  have to use max function 
def max_element(lst):
    return max(lst) if lst else None
print("3. Max:", max_element(sample_list))  
# my max will be 5

# 4
def min_element(lst):
    return min(lst) if lst else None
print("4. Min:", min_element(sample_list))  

# 5
def check_element(lst, elem):
    return elem in lst
print("5. Is 4 in list?", check_element(sample_list, 4))  #the result will be  True

# 6
def first_element(lst):
    return lst[0] if lst else None
print("6. First:", first_element(sample_list))  
# as usual my first result : 1

# 7
def last_element(lst):
    return lst[-1] if lst else None
print("7. Last:", last_element(sample_list))  

# 8
def slice_list(lst):
    return lst[:3]
print("8. First 3:", slice_list(sample_list))  
# Output: [1, 3, 2]

# 9
def reverse_list(lst):
    return lst[::-1]
print("9. Reversed:", reverse_list(sample_list))  # Output: [2, 5, -1, 4, 3, 2, 3, 1]

# 10
def sort_list(lst):
    return sorted(lst)
print("10. Sorted:", sort_list(sample_list))  

# 11
def remove_duplicates(lst):
    return list(dict.fromkeys(lst)) 
print("11. Unique:", remove_duplicates(sample_list))  

# 12
def insert_element(lst, elem, index):
    new_lst = lst.copy()
    new_lst.insert(index, elem)
    return new_lst
print("12. Insert 10 at 2:", insert_element(sample_list, 10, 2))  
#my Output will be  [1, 3, 10, 2, 3, 4, -1, 5, 2]

# 13
def index_of_element(lst, elem):
    return lst.index(elem) if elem in lst else -1
print("13. Index of 3:", index_of_element(sample_list, 3))  
# Output: 1

# 14
def is_empty(lst):
    return len(lst) == 0
print("14. Is empty?", is_empty(sample_list)) # Output: False

# 15
def count_even_numbers(lst):
    return sum(1 for x in lst if x % 2 == 0)
print("15. Even count:", count_even_numbers(sample_list))  

# 16
def count_odd_numbers(lst):
    return sum(1 for x in lst if x % 2 != 0)
print("16. Odd count:", count_odd_numbers(sample_list))  # Output: 6

# 17
def concatenate_lists(lst1, lst2):
    return lst1 + lst2
print("17. Concatenate:", concatenate_lists([1, 2], [3, 4]))  # Output: [1, 2, 3, 4]

# 18
def find_sublist(lst, sublst):
    return any(lst[i:i+len(sublst)] == sublst for i in range(len(lst) - len(sublst) + 1))
print("18. Has [3, 2]?", find_sublist(sample_list, [3, 2]))  # Output: True

# 19
def replace_element(lst, old, new):
    new_lst = lst.copy()
    if old in new_lst:
        new_lst[new_lst.index(old)] = new
    return new_lst
print("19. Replace 3 with 7:", replace_element(sample_list, 3, 7))  
# the result : [1, 7, 2, 3, 4, -1, 5, 2]

# 20
def second_largest(lst):
    unique = sorted(set(lst), reverse=True)
    return unique[1] if len(unique) > 1 else None
print("20. Second largest:", second_largest(sample_list))  # solution: 4

# 21
def second_smallest(lst):
    unique = sorted(set(lst))
    return unique[1] if len(unique) > 1 else None
print("21. Second smallest:", second_smallest(sample_list))  # result : 1

# 22. 
def filter_even_numbers(lst):
    return [x for x in lst if x % 2 == 0]
print("22. Even numbers:", filter_even_numbers(sample_list))  # my solution: [2, 4, 2]

# 23.
def filter_odd_numbers(lst):
    return [x for x in lst if x % 2 != 0]
print("23. Odd numbers:", filter_odd_numbers(sample_list))  # Output: [1, 3, 3, -1, 5]

# 24. 
def list_length(lst):
    return len(lst)
print("24. Length:", list_length(sample_list))  # Output: 9

# 25. 
def create_copy(lst):
    return lst.copy()
print("25. Copy:", create_copy(sample_list))  
# my final result wil be when we filter it [1, 3, 2, 3, 4, -1, 5, 2]

# 26. 
def get_middle_element(lst):
    mid = len(lst) // 2
    return lst[mid] if len(lst) % 2 else lst[mid-1:mid+1]
print("26. Middle:", get_middle_element(sample_list))  

# 27.
def max_of_sublist(lst, start, end):
    return max(lst[start:end+1]) if 0 <= start <= end < len(lst) else None
print("27. Max of [1:4]:", max_of_sublist(sample_list, 1, 4))  

# 28. 
def min_of_sublist(lst, start, end):
    return min(lst[start:end+1]) if 0 <= start <= end < len(lst) else None
print("28. Min of [1:4]:", min_of_sublist(sample_list, 1, 4))  
#the min valuesub will be 2 in my case 

# 29
def remove_by_index(lst, index):
    new_lst = lst.copy()
    if 0 <= index < len(lst):
        new_lst.pop(index)
    return new_lst
print("29. Remove at 2:", remove_by_index(sample_list, 2))  

# 30. 
def is_sorted(lst):
    return lst == sorted(lst)
print("30. Is sorted?", is_sorted(sample_list))  

# 31. Repeating 
def repeat_elements(lst, n):
    return [x for x in lst for _ in range(n)]
print("31. Repeat 2x:", repeat_elements([1, 2], 2))  
# in my range of numbers  i have to control which  numbers and how many tmes they should repeat 


# 32
def merge_and_sort(lst1, lst2):
    return sorted(lst1 + lst2)
print("32. Merge & sort:", merge_and_sort([1, 3], [2, 4]))  

# 33
def find_all_indices(lst, elem):
    return [i for i, x in enumerate(lst) if x == elem]
print("33. Indices of 3:", find_all_indices(sample_list, 3))  

# 34
def rotate_list(lst, shifts=1):
    shifts %= len(lst) if lst else 0
    return lst[shifts:] + lst[:shifts] if lst else []
print("34. Rotate by 1:", rotate_list(sample_list))  # the rotation will be overall  [3, 2, 3, 4, -1, 5, 2, 1]

# 35
def create_range_list(start, end):
    return list(range(start, end + 1))
print("35. Range 1-3:", create_range_list(1, 3))  

# 36
def sum_positive_numbers(lst):
    return sum(x for x in lst if x > 0)
print("36. Sum positives:", sum_positive_numbers(sample_list))  # the final answer is  20

# 37.
def sum_negative_numbers(lst):
    return sum(x for x in lst if x < 0)
print("37. Sum negatives:", sum_negative_numbers(sample_list))  
# when we add them up togehter  -1

# 38.
def is_palindrome(lst):
    return lst == lst[::-1]
print("38. Is palindrome?", is_palindrome([1, 2, 2, 1])) 
# depending on my function yes it is 

# 39.
def create_nested_list(lst, size):
    return [lst[i:i+size] for i in range(0, len(lst), size)]
print("39. Nested (size 3):", create_nested_list(sample_list, 3))  

# 40.
def unique_in_order(lst):
    return list(dict.fromkeys(lst))
print("40. Unique ordered:", unique_in_order(sample_list))  

# === TUPLE TASKS ===
print("\n=== Tuple Tasks ===")
sample_tuple = (1, 3, 2, 3, 4, -1, 5, 2)

# 1. Count Occurrences
def count_occurrences_tuple(tup, elem):
    return tup.count(elem)
print("1. Count of 3:", count_occurrences_tuple(sample_tuple, 3))  # Output: 2

# 2. Max Element
def max_element_tuple(tup):
    return max(tup) if tup else None
print("2. Max:", max_element_tuple(sample_tuple))  # Output: 5

# 3. Min Element
def min_element_tuple(tup):
    return min(tup) if tup else None
print("3. Min:", min_element_tuple(sample_tuple))  # Output: -1

# 4. Check Element
def check_element_tuple(tup, elem):
    return elem in tup
print("4. Is 4 in tuple?", check_element_tuple(sample_tuple, 4))  # Output: True

# 5. First Element
def first_element_tuple(tup):
    return tup[0] if tup else None
print("5. First:", first_element_tuple(sample_tuple))  # Output: 1

# 6. Last Element
def last_element_tuple(tup):
    return tup[-1] if tup else None
print("6. Last:", last_element_tuple(sample_tuple))  # Output: 2

# 7. Tuple Length
def tuple_length(tup):
    return len(tup)
print("7. Length:", tuple_length(sample_tuple))  # Output: 8

# 8. Slice Tuple
def slice_tuple(tup):
    return tup[:3]
print("8. First 3:", slice_tuple(sample_tuple))  # Output: (1, 3, 2)

# 9. Concatenate Tuples
def concatenate_tuples(tup1, tup2):
    return tup1 + tup2
print("9. Concatenate:", concatenate_tuples((1, 2), (3, 4)))  # Output: (1, 2, 3, 4)

# 10. Check if Tuple is Empty
def is_tuple_empty(tup):
    return len(tup) == 0
print("10. Is empty?", is_tuple_empty(sample_tuple))  # Output: False

# 11. Get All Indices of Element
def all_indices_tuple(tup, elem):
    return [i for i, x in enumerate(tup) if x == elem]
print("11. Indices of 3:", all_indices_tuple(sample_tuple, 3))  # Output: [1, 3]

# 12. Find Second Largest
def second_largest_tuple(tup):
    unique = sorted(set(tup), reverse=True)
    return unique[1] if len(unique) > 1 else None
print("12. Second largest:", second_largest_tuple(sample_tuple))  # Output: 4

# 13. Find Second Smallest
def second_smallest_tuple(tup):
    unique = sorted(set(tup))
    return unique[1] if len(unique) > 1 else None
print("13. Second smallest:", second_smallest_tuple(sample_tuple))  # Output: 1

# 14. Create a Single Element Tuple
def single_element_tuple(elem):
    return (elem,)
print("14. Single elem:", single_element_tuple(5))  # Output: (5,)

# 15. Convert List to Tuple
def list_to_tuple(lst):
    return tuple(lst)
print("15. List to tuple:", list_to_tuple([1, 2, 3]))  # Output: (1, 2, 3)

# 16. Check if Tuple is Sorted
def is_tuple_sorted(tup):
    return tup == tuple(sorted(tup))
print("16. Is sorted?", is_tuple_sorted(sample_tuple))  # Output: False

# 17. Find Maximum of Subtuple
def max_of_subtuple(tup, start, end):
    return max(tup[start:end+1]) if 0 <= start <= end < len(tup) else None
print("17. Max of [1:4]:", max_of_subtuple(sample_tuple, 1, 4))  # Output: 4

# 18. Find Minimum of Subtuple
def min_of_subtuple(tup, start, end):
    return min(tup[start:end+1]) if 0 <= start <= end < len(tup) else None
print("18. Min of [1:4]:", min_of_subtuple(sample_tuple, 1, 4))  # Output: 2

# 19. Remove Element by Value
def remove_element_tuple(tup, elem):
    return tuple(x for x in tup if x != elem)
print("19. Remove 3:", remove_element_tuple(sample_tuple, 3))  # Output: (1, 2, 4, -1, 5, 2)

# 20. Create Nested Tuple
def create_nested_tuple(tup, size):
    return tuple(tup[i:i+size] for i in range(0, len(tup), size))
print("20. Nested (size 3):", create_nested_tuple(sample_tuple, 3))  # Output: ((1, 3, 2), (3, 4, -1), (5, 2))

# 21. Repeat Elements
def repeat_elements_tuple(tup, n):
    return tuple(x for x in tup for _ in range(n))
print("21. Repeat 2x:", repeat_elements_tuple((1, 2), 2))  # Output: (1, 1, 2, 2)

# 22. Create Range Tuple
def create_range_tuple(start, end):
    return tuple(range(start, end + 1))
print("22. Range 1-3:", create_range_tuple(1, 3))  # Output: (1, 2, 3)

# 23. Reverse Tuple
def reverse_tuple(tup):
    return tup[::-1]
print("23. Reversed:", reverse_tuple(sample_tuple))  # Output: (2, 5, -1, 4, 3, 2, 3, 1)

# 24. Check Palindrome
def is_palindrome_tuple(tup):
    return tup == tup[::-1]
print("24. Is palindrome?", is_palindrome_tuple((1, 2, 2, 1)))  # Output: True

# 25. Get Unique Elements
def unique_elements_tuple(tup):
    return tuple(dict.fromkeys(tup))
print("25. Unique ordered:", unique_elements_tuple(sample_tuple))  # Output: (1, 3, 2, 4, -1, 5)

# === SET TASKS ===
print("\n=== Set Tasks ===")
sample_set = {1, 3, 2, 3, 4, -1, 5, 2}

# 1. Union of Sets
def union_sets(set1, set2):
    return set1 | set2
print("1. Union:", union_sets({1, 2}, {2, 3}))  # Output: {1, 2, 3}

# 2. Intersection of Sets
def intersection_sets(set1, set2):
    return set1 & set2
print("2. Intersection:", intersection_sets({1, 2}, {2, 3}))  # Output: {2}

# 3. Difference of Sets
def difference_sets(set1, set2):
    return set1 - set2
print("3. Difference:", difference_sets({1, 2}, {2, 3}))  # Output: {1}

# 4. Check Subset
def check_subset(set1, set2):
    return set1 <= set2
print("4. Is {1, 2} subset of {1, 2, 3}?", check_subset({1, 2}, {1, 2, 3}))  # Output: True

# 5. Check Element
def check_element_set(st, elem):
    return elem in st
print("5. Is 4 in set?", check_element_set(sample_set, 4))  # Output: True

# 6. Set Length
def set_length(st):
    return len(st)
print("6. Length:", set_length(sample_set))  # Output: 6

# 7. Convert List to Set
def list_to_set(lst):
    return set(lst)
print("7. List to set:", list_to_set([1, 2, 2, 3]))  # Output: {1, 2, 3}

# 8. Remove Element
def remove_element_set(st, elem):
    new_set = st.copy()
    new_set.discard(elem)
    return new_set
print("8. Remove 3:", remove_element_set(sample_set, 3))  # Output: {1, 2, 4, -1, 5}

# 9. Clear Set
def clear_set(st):
    return set()
print("9. Cleared:", clear_set(sample_set))  # Output: set()

# 10. Check if Set is Empty
def is_set_empty(st):
    return len(st) == 0
print("10. Is empty?", is_set_empty(sample_set))  # Output: False

# 11. Symmetric Difference
def symmetric_difference(set1, set2):
    return set1 ^ set2
print("11. Symmetric diff:", symmetric_difference({1, 2}, {2, 3}))  # Output: {1, 3}

# 12. Add Element
def add_element_set(st, elem):
    new_set = st.copy()
    new_set.add(elem)
    return new_set
print("12. Add 6:", add_element_set(sample_set, 6))  # Output: {1, 2, 3, 4, -1, 5, 6}

# 13. Pop Element
def pop_element_set(st):
    new_set = st.copy()
    elem = new_set.pop()
    return elem, new_set
elem, new_set = pop_element_set(sample_set)
print("13. Popped:", elem, new_set)  # Output: (some element), remaining set

# 14. Find Maximum
def find_max_set(st):
    return max(st) if st else None
print("14. Max:", find_max_set(sample_set))  # Output: 5

# 15. Find Minimum
def find_min_set(st):
    return min(st) if st else None
print("15. Min:", find_min_set(sample_set))  # Output: -1

# 16. Filter Even Numbers
def filter_even_numbers_set(st):
    return {x for x in st if x % 2 == 0}
print("16. Even numbers:", filter_even_numbers_set(sample_set))  # Output: {2, 4}

# 17. Filter Odd Numbers
def filter_odd_numbers_set(st):
    return {x for x in st if x % 2 != 0}
print("17. Odd numbers:", filter_odd_numbers_set(sample_set))  # Output: {1, 3, 5, -1}

# 18. Create a Set of a Range
def create_range_set(start, end):
    return set(range(start, end + 1))
print("18. Range 1-3:", create_range_set(1, 3))  # Output: {1, 2, 3}

# 19. Merge and Deduplicate
def merge_and_deduplicate(lst1, lst2):
    return set(lst1 + lst2)
print("19. Merge & dedup:", merge_and_deduplicate([1, 2, 2], [2, 3]))  # Output: {1, 2, 3}

# 20. Check Disjoint Sets
def check_disjoint_sets(set1, set2):
    return set1.isdisjoint(set2)
print("20. Are disjoint?", check_disjoint_sets({1, 2}, {3, 4}))  # Output: True

# 21. Remove Duplicates from a List
def remove_duplicates_list(lst):
    return list(set(lst))
print("21. Dedup list:", remove_duplicates_list([1, 2, 2, 3]))  # Output: [1, 2, 3]

# 22. Count Unique Elements
def count_unique_elements(lst):
    return len(set(lst))
print("22. Unique count:", count_unique_elements([1, 2, 2, 3]))  # Output: 3

# 23. Generate Random Set
import random
def generate_random_set(size, min_val, max_val):
    return set(random.randint(min_val, max_val) for _ in range(size))
print("23. Random set:", generate_random_set(3, 1, 5))  # Output: e.g., {2, 4, 5}

# === DICTIONARY TASKS ===
print("\n=== Dictionary Tasks ===")
sample_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 2}

# 1. Get Value
def get_value(dct, key):
    return dct.get(key)
print("1. Value of 'a':", get_value(sample_dict, 'a'))  # Output: 1

# 2. Check Key
def check_key(dct, key):
    return key in dct
print("2. Has 'b'?", check_key(sample_dict, 'b'))  # Output: True

# 3. Count Keys
def count_keys(dct):
    return len(dct)
print("3. Key count:", count_keys(sample_dict))  # Output: 4

# 4. Get All Keys
def get_all_keys(dct):
    return list(dct.keys())
print("4. Keys:", get_all_keys(sample_dict))  # Output: ['a', 'b', 'c', 'd']

# 5. Get All Values
def get_all_values(dct):
    return list(dct.values())
print("5. Values:", get_all_values(sample_dict))  # Output: [1, 2, 3, 2]

# 6. Merge Dictionaries
def merge_dicts(dct1, dct2):
    return {**dct1, **dct2}
print("6. Merge:", merge_dicts({'x': 1}, {'y': 2}))  # Output: {'x': 1, 'y': 2}

# 7. Remove Key
def remove_key(dct, key):
    new_dict = dct.copy()
    new_dict.pop(key, None)
    return new_dict
print("7. Remove 'b':", remove_key(sample_dict, 'b'))  # Output: {'a': 1, 'c': 3, 'd': 2}

# 8. Clear Dictionary
def clear_dict(dct):
    return {}
print("8. Cleared:", clear_dict(sample_dict))  # Output: {}

# 9. Check if Dictionary is Empty
def is_dict_empty(dct):
    return len(dct) == 0
print("9. Is empty?", is_dict_empty(sample_dict))  # Output: False

# 10. Get Key-Value Pair
def get_key_value_pair(dct, key):
    return (key, dct[key]) if key in dct else None
print("10. Pair 'a':", get_key_value_pair(sample_dict, 'a'))  # Output: ('a', 1)

# 11. Update Value
def update_value(dct, key, value):
    new_dict = dct.copy()
    new_dict[key] = value
    return new_dict
print("11. Update 'a' to 5:", update_value(sample_dict, 'a', 5))  # Output: {'a': 5, 'b': 2, 'c': 3, 'd': 2}

# 12. Count Value Occurrences
def count_value_occurrences(dct, value):
    return list(dct.values()).count(value)
print("12. Count of 2:", count_value_occurrences(sample_dict, 2))  # Output: 2

# 13. Invert Dictionary
def invert_dict(dct):
    return {v: k for k, v in dct.items()}  # Assumes unique values
print("13. Inverted:", invert_dict({'a': 1, 'b': 2}))  # Output: {1: 'a', 2: 'b'}

# 14. Find Keys with Value
def find_keys_with_value(dct, value):
    return [k for k, v in dct.items() if v == value]
print("14. Keys with 2:", find_keys_with_value(sample_dict, 2))  # Output: ['b', 'd']

# 15. Create a Dictionary from Lists
def dict_from_lists(keys, values):
    return dict(zip(keys, values))
print("15. From lists:", dict_from_lists(['x', 'y'], [1, 2]))  # Output: {'x': 1, 'y': 2}

# 16. Check for Nested Dictionaries
def has_nested_dict(dct):
    return any(isinstance(v, dict) for v in dct.values())
print("16. Has nested?", has_nested_dict({'a': 1, 'b': {'x': 2}}))  # Output: True

# 17. Get Nested Value
def get_nested_value(dct, outer_key, inner_key):
    return dct.get(outer_key, {}).get(inner_key)
print("17. Nested 'b'->'x':", get_nested_value({'b': {'x': 2}}, 'b', 'x'))  # Output: 2

# 18. Create Default Dictionary
from collections import defaultdict
def create_default_dict(default_value):
    return defaultdict(lambda: default_value)
d = create_default_dict(0)
d['a'] = 1
print("18. Default (0):", d['b'])  # Output: 0

# 19. Count Unique Values
def count_unique_values(dct):
    return len(set(dct.values()))
print("19. Unique values:", count_unique_values(sample_dict))  # Output: 3

# 20. Sort Dictionary by Key
def sort_by_key(dct):
    return dict(sorted(dct.items()))
print("20. Sort by key:", sort_by_key(sample_dict))  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 2}

# 21. Sort Dictionary by Value
def sort_by_value(dct):
    return dict(sorted(dct.items(), key=lambda x: x[1]))
print("21. Sort by value:", sort_by_value(sample_dict))  # Output: {'a': 1, 'b': 2, 'd': 2, 'c': 3}

# 22. Filter by Value
def filter_by_value(dct, condition):
    return {k: v for k, v in dct.items() if condition(v)}
print("22. Values > 1:", filter_by_value(sample_dict, lambda x: x > 1))  # Output: {'b': 2, 'c': 3, 'd': 2}

# 23. Check for Common Keys
def common_keys(dct1, dct2):
    return bool(set(dct1.keys()) & set(dct2.keys()))
print("23. Common keys?", common_keys({'a': 1}, {'a': 2, 'b': 3}))  # Output: True

# 24. Create Dictionary from Tuple
def dict_from_tuple(tup):
    return dict(tup)
print("24. From tuple:", dict_from_tuple((('a', 1), ('b', 2))))  # Output: {'a': 1, 'b': 2}

# 25. Get the First Key-Value Pair
def first_key_value_pair(dct):
    return next(iter(dct.items())) if dct else None
print("25. First pair:", first_key_value_pair(sample_dict))  # Output: ('a', 1)