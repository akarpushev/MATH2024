def is_prime(n):
    """Проверяет, является ли число n простым."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for divisor in range(3, max_divisor, 2):
        if n % divisor == 0:
            return False
    return True

def nth_prime(n):
    """Возвращает n-е простое число."""
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prime(num):
            count += 1
    return num

n = 91
print(f"{n}-е простое число: {nth_prime(n)}")
