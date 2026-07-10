import time
import functools

def time_it(func):
    """Функция-декоратор для фиксации времени выпоолнения кода"""
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        
        result = await func(*args, **kwargs)
        
        end_time = time.perf_counter()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {execution_time:.4f} сек.")
        
        return result
    return wrapper
