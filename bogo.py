"""
Docstring
"""
import random
import time

class Bogo:
    """
    Docstring
    """
    def __init__(self, size=10, min_val: int = 1, max_val: int = 10, data: list = None):
        """
        Docstring
        """
        
        if data is not None:
            self.data = list(data)
        elif size is not None:
            self.data = [random.randint(min_val, max_val) for _ in range(size)] 
        else:
            raise ValueError("ERROR")
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

    def bogosort(self, max_attempt: int = 20000000)-> list:
        """
        Docstring
        """
        start_time = time.time()  # start tid

        while not self.is_sorted():
            if self.attempts >= max_attempt:
                print(f"Gav op efter {self.attempts} forsøg")
                return None
            self.shuffle()

        end_time = time.time()  # slut tid
        elapsed = end_time - start_time

        print(f"Sorteret: {self.attempts} forsøg: {self}")
        print(f"Tid brugt: {elapsed:.6f} sekunder")

        return self.data

    def __str__(self):
        """
        Docstring
        """
        return f'{self.data} (Forsøg: {self.attempts})'
