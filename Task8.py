def max_count_repeat_num(s):
    count = 0
    c_set = set()
    for i in range(len(s)-1):
        if s[i] == s[i+1] and s[i].isdigit():
            count += 1
        else:
            c_set.add(count+1)
            count = 0
    print(c_set)


stroke = input("Enter a text: ")
max_count_repeat_num(stroke)