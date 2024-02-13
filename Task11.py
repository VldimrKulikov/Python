def glas(s):
    count = 0
    for i in range(len(s)):
        if s[i] in vowels:
            count += 1
    return count


def soglas(s):
    count = 0
    for i in range(len(s)):
        if s[i] in sowels:
            count += 1
    return count


stroke = input("Enter str: ")
str_list = [stroke]
vowels = {'a', 'e', 'i', 'o', 'u'}
sowels = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
while stroke != "0":
    stroke = input("Enter str: ")
    str_list.append(stroke)

str_list.sort(key=lambda l: soglas(l)-glas(l))
str_list.remove('0')
print(str_list)
