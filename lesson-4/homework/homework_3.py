def under(txt):
    result = ''
    for i in range(len(txt)):
        result += txt[i]
        if (i + 1) % 3 == 0:
            if i != len(txt) - 1:
                result += '_'
    return result

print(under('hello'))
print(under('assalom'))
print(under('abcabcdabcdeabcdefabcdefg'))
#Adds an underscore after every third character, skips the end.