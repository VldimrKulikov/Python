# This is a sample Python script.

def sum_of_prime_divisors(n):
    result = 0
    for i in range(1, n):
        if n % i == 0 and simpleDiv(i) == 1:
            result += i
    return result


def simpleDiv(k):
    count = 0
    for i in range(2, k - 1):
        while count == 0:
            if k % i == 0:
                return 0
    return 1


def count_of_num_before_3(x):
    a = x
    count = 0
    while a != 0:
        if (a / 10) % 2 != 0 and a % 10 > 3:
            count += 1
        a //= 10
    return count


def sum_of_num(x):
    sum_digits = 0
    for digit in str(x):
        sum_digits += int(digit)
    return sum_digits


def multiple_of_div_after_mainSum(x):
    result = 1
    for i in range(1, x):
        if x % i == 0 and sum_of_num(i) < sum_of_num(x):
            result *= i
    return result


number = int(input("Enter a number: "))
print("Сумма простых делителей числа ", number, "равна ", sum_of_prime_divisors(number))
number = int(input("Enter a number: "))
print("Количество нечетных цифр числа, больших 3 ", number, "равна ", count_of_num_before_3(number))
number = int(input("Enter a number: "))
print("Произведение делителей числа, сумма цифр которых меньше, чем сумма цифр самого числа", number, "равна ", multiple_of_div_after_mainSum(number))
