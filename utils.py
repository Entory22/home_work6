def read_fle(file_name: str) -> str:
    """Прочитать слова"""
    with open(file_name, 'r') as file:
        app = file.read()
    return app


def write_result(data: str, file_name: str) -> str:
    """Запись ответов"""
    with open(file_name, 'a') as file:
        file.write(data)
    return "Запись выполнена"


def read_statistic(file_name: str) -> str:
    """Чтение статистики"""
    with open(file_name, 'r') as file:
        statistic = file.read()
    return statistic


def print_statistic(file_name: str) -> None:
    """Показать статистику"""
    statistic = read_statistic(file_name)
    list_word = statistic.split('\n')

    user = None
    max_score = 0
    for word in list_word[:-1]:
        user_stat = word.split(" - ")
        if int(user_stat[1]) >= max_score:
            max_score = int(user_stat[1])
            user = user_stat[0]

    print(user, max_score)
    print(f"Всего игр: {len(list_word) - 1}")
