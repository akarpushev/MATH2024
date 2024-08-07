def is_prime(n):
    """Проверяет, является ли число n простым."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    print(max_divisor)
    for divisor in range(3, max_divisor, 2):
        print(divisor, n / divisor)
        if n % divisor == 0:
            #return False
            return print(f"{number} не является простым числом.")
    #return True
    return print(f"{number} является простым числом.")


number = 299
# if is_prime(number):
#     print(f"{number} является простым числом.")
# else:
#     print(f"{number} не является простым числом.")
is_prime(number)