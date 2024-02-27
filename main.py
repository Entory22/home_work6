from random import shuffle
from utils import read_fle, write_result, print_statistic

FILE_RESULT = 'result.txt'
FILE_WORD = 'file.txt'

file_data = read_fle(FILE_WORD)
list_file = file_data.split('\n')

total_score = 0
user_name = input("Введите Ваше имя: ")

for word in list_file:
    hidden_word = [letter for letter in word]
    shuffle(hidden_word)
    shuffle_letter = ''.join(hidden_word)

    print(shuffle_letter)
    user_answer = input('Ваш ответ: ')

    if user_answer in word:
        print("Верно")
        total_score += 10
    else:
        print(f"Неверно, верный ответ {word}")

result = f"{user_name} - {str(total_score)}\n"

write_result(result, FILE_RESULT)
print_statistic(FILE_RESULT)
