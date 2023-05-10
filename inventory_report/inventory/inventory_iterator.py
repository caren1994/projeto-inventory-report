from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.current = 0
        self.data = data

    def __next__(self):
        try:
            current = self.data[self.current]
            if current:
                self.current += 1
                return current
        except Exception:
            raise StopIteration
