import typing
from functools import wraps


def log(filename=None):
    """Декоратор, который будет автоматически логировать начало и конец выполнения функции, а также ее результаты
    или возникшие ошибки. Декоратор должен принимать необязательный аргумент filename, который определяет,
    куда будут записываться логи (в файл или в консоль):"""

    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"Функция {func.__name__} запущена\n")
                else:
                    print(f"Функция {func.__name__} запущена")

                result = func(*args, **kwargs)

                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"Функция {func.__name__} отработана. Результат: {result}\n")
                else:
                    print(f"Функция {func.__name__} отработана")

                return f"Результат: {result}"
            except Exception as e:
                if filename:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(
                            f"Ошибка в функции {func.__name__}: {type(e).__name__}, входные параметры {args} {kwargs}\n"
                        )
                else:
                    print(f"Ошибка в функции {func.__name__}: {type(e).__name__}, входные параметры {args} {kwargs}")

        return wrapper

    return my_decorator


@log(filename=None)
def my_function(x: int | float, y: int | float) -> int | float:
    """Функция принимает числа типа int и float и возвращает сумму чисел"""

    return x + y
if __name__ == "__main__":
    print(my_function(1, 3))
