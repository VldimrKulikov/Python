import re


def search_min_raz_in_text(s):
    s = s.split()
    set_num = set()
    for i in range(len(s)):
        if re.match("^\d+?\.\d+?$", s[i]):
            set_num.add(float(s[i]))
    print(min(set_num))


stroke = input("Enter a text: ")
search_min_raz_in_text(stroke)
