from contextlib import contextmanager

@contextmanager
def file_manager(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

# Esempio di utilizzo del context manager
with file_manager('example.txt', 'w') as f:
    f.write('Hello, World!')