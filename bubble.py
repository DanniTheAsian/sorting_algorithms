import random
import time
class Bubble:
    def __init__(self, size=10, min_val:int = 1, max_val: int=10, data: list = None):

        if data is not None:
            self.data = list(data)
        elif size is not None:
            self.data = [random.randint(min_val, max_val) for _ in range(size)]
        else: raise ValueError('ERROR')

    def is_sorted(self) -> bool:
        return all(self.data[i] <= self.data[i + 1] for i in range(len(self.data)-1))

    def sort(self):
        n = len(self.data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if self.data[j] > self.data[j+1]:
                    self.data[j], self.data[j+1] = self.data[j+1], self.data[j]

    def bubblesort(self):
        start_time = time.time()
        while not self.is_sorted():
            self.sort()

        end_time = time.time()
        elapsed = end_time - start_time

        print(f"Sorteret: {self.data}")
        print(f"Tid brugt: {elapsed:.6f} sekunder")

        return self.data

    def __str__(self):
        return f'{self.data}'
