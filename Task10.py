stroke = input("Enter str: ")
str_list = [stroke]
while stroke != "0":
    stroke = input("Enter str: ")
    str_list.append(stroke)

str_list.sort(key=lambda l: len(l.split()))
print(str_list)
