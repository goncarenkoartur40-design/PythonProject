import functools
import time

def timeit(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()

        result = func(*args, **kwargs)

        elapsed = time.perf_counter() - start
        print(f'{func.__name__} zajął {elapsed:.4f}s')

        return result

    return wrapper


@timeit
def fetch_users():
    print("Pobieram użytkowników...")

fetch_users()
fetch_users()2("imie")