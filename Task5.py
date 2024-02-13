def search_date_of_text(s):
    s = s.split()
    mon_set = {"января", "февраля", "марта", "апреля", "мая", "июня", "июля", "августа", "сентября", "октября", "ноября", "декабря"}
    for i in range(len(s)-2):
        try:
            if 1 <= int(s[i]) <= 31 and s[i+1] in mon_set and 2 <= int(s[i+2]) <= 9999:
             print(s[i], s[i+1], s[i+2])
        except Exception as e:
            pass


str = input("Enter a text: ")
search_date_of_text(str)
