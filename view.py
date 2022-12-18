def choose() -> str:
    example = input('Для просмотра истории введите "h", для решения задачи введите пример: \n')
    return example


def show_history(history: str):
    """Выводит истроию оперций"""
    print(f'История решения задач:\n{history}')

def show_res(result):
    print(f'Ответ: {result}')

