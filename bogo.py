"""
Docstring
"""
import random

class Bogo:
    """
    Docstring
    """
    def __init__(self, size, min_val: int = 1, max_val: int = 10):
        """
        Docstring
        """
        self.data = [random.randint(min_val, max_val) for _ in range(size)]
        self.attempts = 0

    def is_sorted(self) -> bool:
        """
        Docstring
        """
        return all(self.data[i] <= self.data[i + 1] for i in range(len(self.data)-1))

    def shuffle(self):
        """
        Docstring
        """
        random.shuffle(self.data)
        self.attempts += 1

    def bogosort(self, max_attempt: int = 100000)-> list:
        """
        Docstring
        """
        print(f'starter med {self.data}')
        while not self.is_sorted():
            if self.attempts >= max_attempt:
                print(f"Gav op: {self.attempts} forsøg")
                return None
            self.shuffle()
        print(f'sorteret efter {self.attempts} forsøg {self}')
        return self.data

    def __str__(self):
        """
        Docstring
        """
        return f'{self.data} (Forsøg: {self.attempts})'
