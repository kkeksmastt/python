text = input('Введите текст или набор слов ')
text.split()
num_of_word = 1
for i in text.split():
    print(f'Слово №{num_of_word} {i[:10:]}')
    num_of_word += 1
