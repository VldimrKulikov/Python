from datetime import datetime


def count_of_slave_lang(s):
    a = 0
    for i in range(0, len(s)):
        if "а" <= s[i] <= "я":
            a += 1
    return a


def latin_palindrom(s):
    for i in range(0, len(s)):
        if not ("a" <= s[i] <= "z" and s[len(s) - i - 1] == s[i]):
            return "Не является латинским полиндромом"
    return "Число является латинским полиндромом"


def search_date_of_text(s):
    s =s.split()
    for i in range(len(s)):
        try:
            day, month, year = s[i].split('.')
            print(day, month, year)
        except Exception as e:
            pass
    print(s)


str = input("Enter a text: ")
print(count_of_slave_lang(str))
str = input("Enter a text: ")
print(latin_palindrom(str))
str = input("Enter a text: ")
print(search_date_of_text(str))
