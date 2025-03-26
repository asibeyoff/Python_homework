# global variablleeeee 
print("\n=== Tuple Tasks ===")
sample_tuple = (1, 3, 2, 3, 4, -1, 5, 2)

# 1. Count Occurrences
def count_occurrences_tuple(tup, elem):
    return tup.count(elem)
print("1. Count of 3:", count_occurrences_tuple(sample_tuple, 3))  # Hey, this counts how many 3s are in there—should be 2!

# 2. Max Element
def max_element_tuple(tup):
    return max(tup) if tup else None
print("2. Max:", max_element_tuple(sample_tuple))  # This finds the biggest number, so we’ll get 5 here.

# 3. Min Element
def min_element_tuple(tup):
    return min(tup) if tup else None
print("3. Min:", min_element_tuple(sample_tuple))  # Looks for the smallest one—expecting -1.

# 4. Check Element
def check_element_tuple(tup, elem):
    return elem in tup
print("4. Is 4 in tuple?", check_element_tuple(sample_tuple, 4))  # Just checking if 4 is hanging out in the tuple—yep, it’s there!

# 5. First Element
def first_element_tuple(tup):
    return tup[0] if tup else None
print("5. First:", first_element_tuple(sample_tuple))  # Grabs the first thing in the tuple, which is 1.

# 6. Last Element
def last_element_tuple(tup):
    return tup[-1] if tup else None
print("6. Last:", last_element_tuple(sample_tuple))  # Snags the last item—should be 2.

# 7. Tuple Length
def tuple_length(tup):
    return len(tup)
print("7. Length:", tuple_length(sample_tuple))  # How many items are in this tuple? Looks like 8.

# 8. Slice Tuple
def slice_tuple(tup):
    return tup[:3]
print("8. First 3:", slice_tuple(sample_tuple))  # Chops off the first three items—gives us (1, 3, 2).

# 9. Concatenate Tuples
def concatenate_tuples(tup1, tup2):
    return tup1 + tup2
print("9. Concatenate:", concatenate_tuples((1, 2), (3, 4)))  # Sticks two tuples together—ends up with (1, 2, 3, 4).

# 10. Check if Tuple is Empty
def is_tuple_empty(tup):
    return len(tup) == 0
print("10. Is empty?", is_tuple_empty(sample_tuple))  # Is there nothing in here? Nope, it’s got stuff—False.

# 11. Get All Indices of Element
def all_indices_tuple(tup, elem):
    return [i for i, x in enumerate(tup) if x == elem]
print("11. Indices of 3:", all_indices_tuple(sample_tuple, 3))  # Finds all the spots where 3 shows up—should be 1 and 3.

# 12. Find Second Largest
def second_largest_tuple(tup):
    unique = sorted(set(tup), reverse=True)
    return unique[1] if len(unique) > 1 else None
print("12. Second largest:", second_largest_tuple(sample_tuple))  # Gets the second biggest number—looks like 4.

# 13. Find Second Smallest
def second_smallest_tuple(tup):
    unique = sorted(set(tup))
    return unique[1] if len(unique) > 1 else None
print("13. Second smallest:", second_smallest_tuple(sample_tuple))  # Finds the second smallest—should be 1.

# 14. Create a Single Element Tuple
def single_element_tuple(elem):
    return (elem,)
print("14. Single elem:", single_element_tuple(5))  # Makes a tuple with just one thing—here’s (5,).

# 15. Convert List to Tuple
def list_to_tuple(lst):
    return tuple(lst)
print("15. List to tuple:", list_to_tuple([1, 2, 3]))  # Turns a list into a tuple—gives us (1, 2, 3).

# 16. Check if Tuple is Sorted
def is_tuple_sorted(tup):
    return tup == tuple(sorted(tup))
print("16. Is sorted?", is_tuple_sorted(sample_tuple))  # Checks if it’s in order—nah, it’s not, so False.

# 17. Find Maximum of Subtuple
def max_of_subtuple(tup, start, end):
    return max(tup[start:end+1]) if 0 <= start <= end < len(tup) else None
print("17. Max of [1:4]:", max_of_subtuple(sample_tuple, 1, 4))  # What’s the biggest in this chunk? Should be 4.

# 18. Find Minimum of Subtuple
def min_of_subtuple(tup, start, end):
    return min(tup[start:end+1]) if 0 <= start <= end < len(tup) else None
print("18. Min of [1:4]:", min_of_subtuple(sample_tuple, 1, 4))  # Smallest in this slice—looks like 2.

# 19. Remove Element by Value
def remove_element_tuple(tup, elem):
    return tuple(x for x in tup if x != elem)
print("19. Remove 3:", remove_element_tuple(sample_tuple, 3))  # Kicks out all the 3s—leaves us with (1, 2, 4, -1, 5, 2).

# 20. Create Nested Tuple
def create_nested_tuple(tup, size):
    return tuple(tup[i:i+size] for i in range(0, len(tup), size))
print("20. Nested (size 3):", create_nested_tuple(sample_tuple, 3))  # Splits it into groups of 3—pretty cool, right?

# 21. Repeat Elements
def repeat_elements_tuple(tup, n):
    return tuple(x for x in tup for _ in range(n))
print("21. Repeat 2x:", repeat_elements_tuple((1, 2), 2))  # Doubles up each item—gives us (1, 1, 2, 2).

# 22. Create Range Tuple
def create_range_tuple(start, end):
    return tuple(range(start, end + 1))
print("22. Range 1-3:", create_range_tuple(1, 3))  # Makes a tuple from 1 to 3—simple as that!

# 23. Reverse Tuple
def reverse_tuple(tup):
    return tup[::-1]
print("23. Reversed:", reverse_tuple(sample_tuple))  # Flips it backwards—starts with 2, ends with 1.

# 24. Check Palindrome
def is_palindrome_tuple(tup):
    return tup == tup[::-1]
print("24. Is palindrome?", is_palindrome_tuple((1, 2, 2, 1)))  # Same forwards and back? Yep, it’s True!

# 25. Get Unique Elements
def unique_elements_tuple(tup):
    return tuple(dict.fromkeys(tup))
print("25. Unique ordered:", unique_elements_tuple(sample_tuple))  # Keeps only one of each, in order—nice and tidy.

