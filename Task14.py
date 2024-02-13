from collections import Counter
from itertools import count


def count_chars_in_list(list):
    count = 0
    for i in range(len(list)):
        for j in range(len(list[i])):
            count += 1
    return count


def frequency_in_str(s, c):
    count = 0
    for i in range(len(s)):
        if s[i] == c:
            count += 1
    return count / len(s)


def sup_find_simv(list):
    charfrequency = {}
    for string in list:
        for char in string:
            if char in charfrequency:
                charfrequency[char] += 1
            else:
                charfrequency[char] = 1
    rt = max(charfrequency, key=charfrequency.get)
    return rt, charfrequency[rt]


stroke = input("Enter str: ")
str_list = [stroke]
while stroke != "0":
    stroke = input("Enter str: ")
    str_list.append(stroke)
str_list.remove('0')
a, c = sup_find_simv(str_list)
b = count_chars_in_list(str_list)
str_list.sort(key=lambda l: (c/b - frequency_in_str(l,a)) ** 2, reverse=False)
print(str_list)