import re
from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    """
    Генерує всі дійсні числа з тексту як float.
    """
    # Шукаємо числа з пробілами з обох боків або на початку/кінці рядка
    # якщо дійсні числа у тексті записані без помилок, чітко відокремлені пробілами з обох боків
    
    pattern = r'(?<=\s)\d+\.\d+(?=\s)|^\d+\.\d+(?=\s)|(?<=\s)\d+\.\d+$'
    
    # або pattern = r'\d+\.\d+'
    # працює навіть, якщо числа у тексті записані з помилками
    # та не відокремлені чітко пробілами з обох боків
    
    for match in re.finditer(pattern, text):
        yield float(match.group())


def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    """
    Підсумовує всі дійсні числа, які повертає генератор.
    """
    return sum(func(text))

# Приклад використання
text = (
        "Загальний дохід працівника складається з декількох частин: 1000.05 як "
        "основний дохід, доповнений додатковими надходженнями 27.40 і 324.00 доларів."
    )
total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income:.2f}")

# Виведе: Загальний дохід: 1351.45  # (1000.05 + 27.40 + 324.00 = 1351.45)
