from Bio import Entrez

# Установим email для использования Entrez
Entrez.email = "akarpushev@yandex.ru"

# Поиск статей по ключевым словам
query = "origin of biological information in the origin of life"
handle = Entrez.esearch(db="pubmed", term=query, retmax=10)
record = Entrez.read(handle)
handle.close()

# Получение списка идентификаторов статей
id_list = record["IdList"]
print(id_list)
