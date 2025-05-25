import functools

from typing import Optional, Callable

def log(filename: Optional[str] = None):
    """
    Декоратор логирует результат выполнения функции.
    При успехе: 'function_name ok'
    При ошибке: 'function_name error: <тип ошибки>. Inputs: <args>, <kwargs>'
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log_line = ""
            try:
                result = func(*args, **kwargs)
                log_line = f"{func.__name__} ok"
                return result
            except Exception as e:
                log_line = (
                    f"{func.__name__} error: {type(e).__name__}."
                    f"Inputs: {args}, {kwargs}"
                )
                raise
            finally:
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(log_line + "\n")
                else:
                    print(log_line)

        return wrapper

    return decorator


if __name__ == "__main__":
    @log(filename="mylog.txt")
    def my_function(x, y):
        return x / y


    my_function(1, 0)