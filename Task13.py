def mid_ascii_of_str(s):
    result = 0
    for i in range(len(s)):
        result += ord(s[i])
    return result / len(s)


def max_ascii_of_troika(s):
    sub_res = []
    for i in range(len(s)-3):
        sub_res.append(mid_ascii_of_str(s[i:i+3]))
    return max(sub_res)


stroke = input("Enter str: ")
str_list = [stroke]
while stroke != "0":
    stroke = input("Enter str: ")
    str_list.append(stroke)
str_list.remove('0')
str_list.sort(key=lambda l: (mid_ascii_of_str(l) - max_ascii_of_troika(l)) ** 2, reverse=False)

print(str_list)
for i in range(len(str_list)):
    print((mid_ascii_of_str(str_list[i]) - max_ascii_of_troika(str_list[i])) ** 2)
