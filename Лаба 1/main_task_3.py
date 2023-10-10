# TODO Найдите количество книг, которое можно разместить на дискете
amount_of_pages = 100
lines = 50
symbols = 25

one_symbol = 4

one_book = (amount_of_pages * lines * symbols * one_symbol) #Байты

disk = 1.44 # Мегабайты

books = int((disk * 2**20)//one_book)

print("Количество книг, помещающихся на дискету:", books)
