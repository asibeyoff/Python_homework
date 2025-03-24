# 1. 
name = input("Enter your name: ")
birthday = int(input("Enter your year of birth: "))
current = 2025
age = current - birthday
print(f"Hello {name}, you are {age} years old.")

# 2
txt = 'LMaasleitbtui'

names = ['Tesla', 'BMW', 'Audi']
for car in names:
    if car.lower() in txt.lower():
        print(car)


# 3
user = input("Enter a string: ")
print("Length of the string:", len(user))
print("Uppercase:", user.upper())
print("Lowercase:", user.lower())

# 4
palindrome_check = input("Enter a string to check for palindrome: ")
if palindrome_check == palindrome_check[::-1]:
    print("It's a palindrome!")
else:
    print("Not a palindrome.")

# 5
def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char in vowels:
            vowel_count += 1
        elif 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            consonant_count += 1

    return vowel_count, consonant_count

user_input = input("Enter a string: ")
vowels, consonants = count_vowels_consonants(user_input)
print("Vowels:", vowels)
print("Consonants:", consonants)


# 6
main_string = input("Enter the main string: ")
sub_string = input("Enter the sub to check: ")
print("Sub found:", sub_string in main_string)

# 7
sentence = input("Enter a sentence: ")
old= input("Word to replace: ")
new = input("Replace with: ")
print("Updated sentence:", sentence.replace(old, new))

# 8
string_input = input("Enter a string: ")
print("First character:", string_input[0])
print("Last character:", string_input[-1])

# 9
reverse_input = input("Enter a string to reverse: ")
print("Reversed string:", reverse_input[::-1])

# 10
word_count_sentence = input("Enter a sentence: ")
print("Number of words:", len(word_count_sentence.split()))

# 11
digit_check_string = input("Enter a string: ")
print("Contains digits:", any(char.isdigit() for char in digit_check_string))

# 12
words = input("Enter words separated by spaces: ").split()
separator = input("Enter a separator: ")
print("Joined string:", separator.join(words))

# 13
space_string = input("Enter a string with spaces: ")
print("String without spaces:", space_string.replace(" ", ""))

# 14
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
print("Strings are equal:", str1 == str2)

# 15
acronym_input = input("Enter a sentence for acronym: ")
acronym = ''.join(word[0].upper() for word in acronym_input.split())
print("Acronym:", acronym)

# 16
char_string = input("Enter a string: ")
char_to_remove = input("Character to remove: ")
print("Updated string:", char_string.replace(char_to_remove, ""))

# 17
symbol_string = input("Enter a string: ")
symbol = input("Enter a symbol: ")
for vowel in vowels:
    symbol_string = symbol_string.replace(vowel, symbol)
print("Updated string:", symbol_string)

# 18
check_string = input("Enter a string: ")
start_word = input("Enter the starting word: ")
end_word = input("Enter the ending word: ")
print("Starts with:", check_string.startswith(start_word))
print("Ends with:", check_string.endswith(end_word))
