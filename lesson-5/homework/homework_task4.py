universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(university_list):
    students = [uni[1] for uni in university_list]
    tuition = [uni[2] for uni in university_list]
    return students, tuition

def mean(numbers):
    return sum(numbers) / len(numbers)

def median(numbers):
    sorted_nums = sorted(numbers)
    length = len(sorted_nums)
    if length % 2 == 0:
        return (sorted_nums[length//2 - 1] + sorted_nums[length//2]) / 2
    return sorted_nums[length//2]

students, tuition = enrollment_stats(universities)
total_students = sum(students)
total_tuition = sum(tuition)
student_mean = mean(students)
student_median = median(students)
tuition_mean = mean(tuition)
tuition_median = median(tuition)

print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print()
print(f"Student mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,}")
print()
print(f"Tuition mean: $ {tuition_mean:,.2f}")
print(f"Tuition median: $ {tuition_median:,}")
print("******************************")

# Calculates and displays university enrollment and tuition statistics