import pytest

from scr.decorators import log
from scr.generators import card_number_generator

# ===========================
# ====== Тесты для log ======
# ===========================


# ====== ОБЫЧНАЯ ФУНКЦИЯ ДЛЯ ТЕСТА УСПЕХА ======
@log()
def add(a, b):
    return a + b


def test_regular_function_success(capsys):
    result = add(2, 3)
    captured = capsys.readouterr()

    assert result == 5
    assert "The add works\n" in captured.out


# ====== ОБЫЧНАЯ ФУНКЦИЯ ДЛЯ ТЕСТА ОШИБКИ ======
@log()
def divide(a, b):
    return a / b


def test_regular_function_error(capsys):
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "The divide function returned an error." in captured.out
    assert "ZeroDivisionError" in captured.out


# ====== ГЕНЕРАТОР ДЛЯ УСПЕШНОГО ТЕСТА ======
@log()
def wrapped_generator(start, end):
    return card_number_generator(start, end)


def test_generator_success(capsys):
    result = list(wrapped_generator(1234567890123456, 1234567890123456))
    captured = capsys.readouterr()

    assert result == ["1234 5678 9012 3456"]
    assert "The wrapped_generator works" in captured.out


# ====== ГЕНЕРАТОР С ОШИБКОЙ ======
@log()
def wrapped_generator_error(start, end):
    return card_number_generator(start, end)


def test_generator_error(capsys):
    with pytest.raises(ValueError):
        list(wrapped_generator_error(5, 4))

    captured = capsys.readouterr()
    assert "The wrapped_generator_error function returned an error." in captured.out
    assert "ValueError" in captured.out


# ====== ТЕСТЫ С ФАЙЛОМ ======
@pytest.fixture
def temp_log_file(tmp_path):
    return tmp_path / "log.txt"


def test_log_to_file_success(temp_log_file):
    @log(filename=temp_log_file)
    def add_numbers(x, y):
        return x + y

    result = add_numbers(10, 20)

    with open(temp_log_file, encoding="utf-8") as f:
        log_output = f.read()

    assert result == 30
    assert "The add_numbers works\n" in log_output


def test_log_to_file_generator_error(temp_log_file):
    @log(filename=temp_log_file)
    def wrapped(start, end):
        return card_number_generator(start, end)

    with pytest.raises(ValueError):
        list(wrapped(100, 10))  # Ошибка: start > end

    with open(temp_log_file, encoding="utf-8") as f:
        log_output = f.read()

    assert "function returned an error" in log_output
    assert "ValueError" in log_output
