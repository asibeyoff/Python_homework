def uncommon(list1, list2):
    count1 = {}
    count2 = {}
    
    for num in list1:
        count1[num] = count1.get(num, 0) + 1
    for num in list2:
        count2[num] = count2.get(num, 0) + 1
    
    result = []
    for num in count1:
        diff = count1.get(num, 0) - count2.get(num, 0)
        if diff > 0:
            result.extend([num] * diff)
    for num in count2:
        diff = count2.get(num, 0) - count1.get(num, 0)
        if diff > 0:
            result.extend([num] * diff)
    
    return result

print(uncommon([1, 1, 2], [2, 3, 4]))
print(uncommon([1, 2, 3], [4, 5, 6]))
print(uncommon([1, 1, 2, 3, 4, 2], [1, 3, 4, 5]))
# Simple and handles duplicates 
# use sets for unique elements, but  preserves multiplicity.