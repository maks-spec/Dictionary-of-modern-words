import time
print("Словарь современных слов.")
time.sleep(1)
while (True):
    meme_dict = {
                "КРИНЖ": "Что-то очень странное или стыдное",
                "ЛОЛ": "Что-то очень смешное",
                "РОФЛ": "шутка",
                "ЩИЩ": "одобрение или восторг",
                "КРИПОВЫЙ": "страшный , пугающий",
                "АГРИТЬСЯ": "злиться , негодовать",
                "ВАЙБ": "что-то приятное"
                }
    
    word = input("Введите непонятное слово (большими буквами!): ")
    
    if word in meme_dict.keys():
        print(meme_dict[word])
    else:
        print("Слово не существует повторите попытку.")
    time.sleep(2)
