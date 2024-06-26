import time
from contextlib import contextmanager

@contextmanager
def timer():
    start_time = time.time()
    try:
        yield
    finally:
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"time elapsed: {elapsed_time:.5f}")

# Esempio d'uso:
with timer():
    time.sleep(1)
