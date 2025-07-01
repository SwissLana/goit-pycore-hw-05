def caching_fibonacci(): # Функція для створення кешованої версії обчислення чисел Фібоначчі
    cache = {}  # Створення порожнього кешу

    def fibonacci(n): # Функція для обчислення чисел Фібоначчі з кешуванням
        # Базові випадки
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        # Якщо результат уже в кеші — повернути його
        if n in cache:
            return cache[n]
        # Інакше — обчислити рекурсивно, зберегти у кеші і повернути
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci

# Приклад використання
# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію для обчислення чисел Фібоначчі
print(fib(10))  # Виведе: 55
print(fib(15))  # Виведе: 610
print(fib(20))  # Виведе: 6765
print(fib(30))  # Виведе: 832040
