def log_exec(expr: str, result: str):
    """Записывает в файл результат вычислений
    в виде |задача -> ответ|"""
    try:
        with open('History.txt', 'a', encoding='utf-8') as hisrory:
            hisrory.write(f'{expr} = {result}\n')
    except FileNotFoundError:
        with open('History.txt', 'w', encoding='utf-8') as hisrory:
            hisrory.write(f'{expr} = {result}\n')



def get_history() -> str:
    """"Возвращает содержимое файла с результатами вычислений"""
    with open('History.txt', 'r', encoding='utf-8') as hisrory:
        return hisrory.read()
