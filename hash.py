import hashlib
import time

# Пример транзакций
transactions = [
    "Alice -> Bob: 10 BTC",
    "Bob -> Charlie: 5 BTC",
    "Charlie -> Dave: 2 BTC"
]

# Функция для хеширования блока
def hash_block(header):
    return hashlib.sha256(header.encode()).hexdigest()

# Функция для создания нового блока
def create_block(previous_hash, transactions, nonce):
    block_header = f"{previous_hash}|{str(transactions)}|{nonce}"
    return block_header

# Функция для майнинга блока
def mine_block(previous_hash, transactions, difficulty):
    nonce = 0
    start_time = time.time()
    while True:
        block_header = create_block(previous_hash, transactions, nonce)
        block_hash = hash_block(block_header)
        if block_hash.startswith('0' * difficulty):
            end_time = time.time()
            print(f"Блок найден с хешем: {block_hash}")
            print(f"Nonce: {nonce}")
            print(f"Время майнинга: {end_time - start_time} секунд")
            return block_hash, nonce
        nonce += 1

# Предыдущий хеш (для примера используем строку "0000000000000000")
previous_hash = "0000000000000000"

# Сложность (количество нулей, с которых должен начинаться хеш)
difficulty = 4

# Запуск майнинга
new_block_hash, nonce = mine_block(previous_hash, transactions, difficulty)

# Вывод результатов
print(f"Новый блок добавлен с хешем: {new_block_hash}")
print(f"Nonce: {nonce}")
