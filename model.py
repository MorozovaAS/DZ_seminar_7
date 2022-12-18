def mode_selection(example):
    if "=" in example:
        mode = '2'
    elif "x" in example:
        mode = '3'
    elif "h" in example:
        mode = '4'
    else:
        mode = '1'
    return mode

import sympy

def execute_expr(expr: str) -> str:         
    """"Принимает на вход строку-пример.
    Возвращает результат примера."""
    try:
        result = str(sympy.expand(expr))
    except ValueError:
        result = 'Введите пример корректно'       
    return result
   

def solve_eq(expr: str) -> str:                    
    """Принимает на вход уравнение в виде строки.
    Возвращает список корней уравнения в строку с разделителем"""
    try:
        expr = expr[:expr.find('=')]
        result = str(sympy.solve(expr))        
    except ValueError:
        result = 'Введите пример корректно'       
    return result
    

def simpify_pol(expr: str) -> str:          
    """"Упрощает введенный многочлен"""
    try:
        result = str(sympy.expand(expr))        
    except ValueError:
        result = 'Введите пример корректно'       
    return result



