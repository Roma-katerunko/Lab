import sys
import os

def hide_output(func):
    def wrapper(*args, **kwargs):
        old_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')  # приховуємо вивід

        try:
            return func(*args, **kwargs)
        finally:
            sys.stdout.close()
            sys.stdout = old_stdout  # повертаємо вивід
    return wrapper
