def mid_ascii_of_str(s):
    result = 0;
    for i in range(len(s)):
        result += ord(s[i])
    return result / len(s)


stroke = input("Enter str: ")
str_list = [stroke]
firstStr = stroke
while stroke != "0":
    stroke = input("Enter str: ")
    str_list.append(stroke)

str_list.sort(key=lambda l: (mid_ascii_of_str(l) - mid_ascii_of_str(firstStr) ** 2), reverse=False)
str_list.remove('0')
print(str_list)
for i in range(len(str_list)):
    print((mid_ascii_of_str(str_list[i]) - mid_ascii_of_str(firstStr)) ** 2)
