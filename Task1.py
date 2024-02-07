# This is a sample Python script.

def sum_of_prime_divisors(n):
    result = 0
    for i in range(1, n):
        if n % i == 0 and simpleDiv(i) == 1:
            result += i
    return result


def simpleDiv(k):
    count = 0
    for i in range(2, k-1):
        while count == 0:
            if k % i == 0:
                return 0
    return 1


number = int(input("Enter a number: "))
print("Сумма простых делителей числа ", number, "равна ", sum_of_prime_divisors(number))
