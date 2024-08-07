import hashlib


# Функция для вычисления SHA-256 хэша строки
def calculate_sha256_hash(input_string):
    # Преобразуем строку в байтовый объект, так как хэш-функции работают с байтами
    byte_string = input_string.encode('utf-8')
    print(byte_string)

    # Создаем объект хэша для SHA-256
    sha256_hash = hashlib.sha256()
    print(sha256_hash)

    # Обновляем объект хэша байтами строки
    sha256_hash.update(byte_string)
    print(sha256_hash)

    # Получаем и возвращаем SHA-256 хэш в виде шестнадцатеричной строки
    return sha256_hash.hexdigest()


# Пример использования функции
input_string = "Hello, World!"
sha256_hash = calculate_sha256_hash(input_string)
print(f'SHA-256 хэш строки "{input_string}": {sha256_hash}')
