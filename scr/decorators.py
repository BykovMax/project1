import functools
from typing import Optional, Callable, Iterator

def log(filename: Optional[str] = None):
    """
    Декоратор логирует результат выполнения функции.
    Если аргумент filename передан, то записываются логи в файл, если нет — выводится в консоль.
    При успехе: 'The function_name ok.'
    При ошибке: 'The function_name function returned an error.
                 Error: <тип ошибки>.
                 Inputs: <args>, <kwargs>'
    """

    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            log_line = ""
            is_generator = False

            try:
                result = func(*args, **kwargs)

                if isinstance(result, Iterator):
                    is_generator = True

                    def generator_wrapper():
                        try:
                            for value in result:
                                yield value
                            log_line_local = f"The {func.__name__} ok\n"
                        except Exception as e:
                            log_line_local = (
                                f"The {func.__name__} function returned an error.\n"
                                f"Error: {type(e).__name__}.\n"
                                f"Inputs: {args}, {kwargs}\n"
                            )
                            raise
                        finally:
                            if filename:
                                with open(filename, "a", encoding="utf-8") as f:
                                    f.write(log_line_local + "\n")
                            else:
                                print(log_line_local)

                    return generator_wrapper()
                else:
                    log_line = f"The {func.__name__} ok\n"
                    return result

            except Exception as e:
                log_line = (
                    f"The {func.__name__} function returned an error.\n"
                    f"Error: {type(e).__name__}.\n"
                    f"Inputs: {args}, {kwargs}\n"
                )
                raise

            finally:
                if not is_generator:
                    if filename:
                        with open(filename, "a", encoding="utf-8") as f:
                            f.write(log_line + "\n")
                    else:
                        print(log_line)

        return wrapper

    return decorator
