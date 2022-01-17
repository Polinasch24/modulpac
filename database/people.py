documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]



def get_employees():
   number = input('Введите номер документа:')
   for num_doc in documents:
      if num_doc.get("number") == number:
         return num_doc.get("name")
   return"Такого документа не существует"
print(get_employees())