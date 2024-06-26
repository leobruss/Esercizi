class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()
        if exc_type is not None:
            print(f"An error occurred: {exc_value}")
        return True  # This will suppress the exception if one occurred

# Esempio di utilizzo del context manager
with FileManager('example.txt', 'w') as f:
    f.write('Hello, world!')
    