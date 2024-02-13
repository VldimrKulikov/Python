def search_max_num_of_text(s):
    s = s.split()
    set_num = set()
    for i in range(len(s)):
            if s[i].isdigit():
                set_num.add(s[i])
    print(max(set_num))


str = input("Enter a text: ")
search_max_num_of_text(str)