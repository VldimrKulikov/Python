stroke = input("Enter str: ")
str_list = [stroke]
while stroke != "0":
    stroke = input("Enter str: ")
    str_list.append(stroke)

str_list.sort(key=len, reverse=True)
print(str_list)