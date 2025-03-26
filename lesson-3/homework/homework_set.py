#i have used global variable 
print("\n=== Set Tasks ===")
sample_set = {1, 3, 2, 3, 4, -1, 5, 2}

# 1
def union_sets(set1, set2):
    return set1 | set2
print("1. Union:", union_sets({1, 2}, {2, 3}))  # Combines them, no duplicates be {1, 2, 3}.

# 2
def intersection_sets(set1, set2):
    return set1 & set2
print("2. Intersection:", intersection_sets({1, 2}, {2, 3}))  # Just the stuff they {2}.

# 3
def difference_sets(set1, set2):
    return set1 - set2
print("3. Difference:", difference_sets({1, 2}, {2, 3}))  # What’s in the first but not the second? Just {1}.

# 4
def check_subset(set1, set2):
    return set1 <= set2
print("4. Is {1, 2} subset of {1, 2, 3}?", check_subset({1, 2}, {1, 2, 3}))  # Does it fit inside? Yep, True!

# 5. Check Element
def check_element_set(st, elem):
    return elem in st
print("5. Is 4 in set?", check_element_set(sample_set, 4))  # Is 4 part of the gang? Sure is!

# 6
def set_length(st):
    return len(st)
print("6. Length:", set_length(sample_set))  # How many unique items? Should be 6.

# 7. Converting
def list_to_set(lst):
    return set(lst)
print("7. List to set:", list_to_set([1, 2, 2, 3]))  # Turns a list into a set, drops duplicates—nice!

# 8
def remove_element_set(st, elem):
    new_set = st.copy()
    new_set.discard(elem)
    return new_set
print("8. Remove 3:", remove_element_set(sample_set, 3))  # Takes out 3, leaves the rest behind.

# 9. Clearing 
def clear_set(st):
    return set()
print("9. Cleared:", clear_set(sample_set))  # Wipes it clean—nothing left!

# 10. Check if emty
def is_set_empty(st):
    return len(st) == 0
print("10. Is empty?", is_set_empty(sample_set))  # Any stuff in there? Nope, it’s got things—False.

# 11.
def symmetric_difference(set1, set2):
    return set1 ^ set2
print("11. Symmetric diff:", symmetric_difference({1, 2}, {2, 3}))  # Stuff in one or the other, but not both—{1, 3}.

# 12.
def add_element_set(st, elem):
    new_set = st.copy()
    new_set.add(elem)
    return new_set
print("12. Add 6:", add_element_set(sample_set, 6))  # Tosses 6 !

# 13. Poping
def pop_element_set(st):
    new_set = st.copy()
    elem = new_set.pop()
    return elem, new_set
elem, new_set = pop_element_set(sample_set)
print("13. Popped:", elem, new_set)  # Grabs something random and shows what’s left.

# 14. Find Max
def find_max_set(st):
    return max(st) if st else None
print("14. Max:", find_max_set(sample_set))  # What’s the biggest in the set? Should be 5.

# 15. Find Min
def find_min_set(st):
    return min(st) if st else None
print("15. Min:", find_min_set(sample_set))  # Smallest one? That’s -1.

# 16. Filter Even Numbers
def filter_even_numbers_set(st):
    return {x for x in st if x % 2 == 0}
print("16. Even numbers:", filter_even_numbers_set(sample_set))  # Picks out the even ones—{2, 4}.

# 17. Filter Odd Numbers
def filter_odd_numbers_set(st):
    return {x for x in st if x % 2 != 0}
print("17. Odd numbers:", filter_odd_numbers_set(sample_set))  # Grabs the oddballs—{1, 3, 5, -1}.

# 18
def create_range_set(start, end):
    return set(range(start, end + 1))
print("18. Range 1-3:", create_range_set(1, 3))  # Makes a set from 1 to 3—easy peasy.

# 19
def merge_and_deduplicate(lst1, lst2):
    return set(lst1 + lst2)
print("19. Merge & dedup:", merge_and_deduplicate([1, 2, 2], [2, 3]))  # Combines lists, keeps it unique—{1, 2, 3}.

# 20
def check_disjoint_sets(set1, set2):
    return set1.isdisjoint(set2)
print("20. Are disjoint?", check_disjoint_sets({1, 2}, {3, 4}))  # Do they shar? Nope, True!

# 21. Remove Duplicates from a List
def remove_duplicates_list(lst):
    return list(set(lst))
print("21. Dedup list:", remove_duplicates_list([1, 2, 2, 3]))  # Cleans up  the extras.

# 22
def count_unique_elements(lst):
    return len(set(lst))
print("22. Unique count:", count_unique_elements([1, 2, 2, 3]))  # How many different items? 3!

# 23
import random
def generate_random_set(size, min_val, max_val):
    return set(random.randint(min_val, max_val) for _ in range(size))
print("23. Random set:", generate_random_set(3, 1, 5))  # Throws together some random numberss!