import view
import model
import logger

def run_calc():
    expr = view.choose()
    mode = model.mode_selection(expr)
    if mode == '1':
        result = model.execute_expr(expr)
        view.show_res(result)
        logger.log_exec(expr, result)
    elif mode == '2':
        result = model.solve_eq(expr)
        view.show_res(result)
        logger.log_exec(expr, result)
    elif mode == '3':
        result = model.simpify_pol(expr)
        view.show_res(result)
        logger.log_exec(expr, result)
    elif mode == '4':
        history = logger.get_history()
        view.show_history(history)
    
    

