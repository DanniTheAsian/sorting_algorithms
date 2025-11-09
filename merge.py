import random
import time

class Merge:
    def __init__(self, size = 10, min_val: int =1, max_val: int= 10, data: list = None):
        if data is not None:
            self.data = list(data)
        elif size is not None:
            self.data = [random.randint(min_val, max_val) for _ in range(size)]
        else: raise ValueError('ERROR')

    def is_sorted(self) -> bool:
        return all(
            self.data[i] <= self.data[i + 1]
            for i in range(len(self.data)-1))

    def sort(self, arr):
        if len(arr) <=1:
            return arr
        
        mid = len(arr) // 2
        left = self.sort(arr[:mid])
        right = self.sort(arr[mid:])

        return self.merge(left,right)

    def merge(self, left, right):
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])

        return merged
    
    def mergesort(self):
        start_time = time.time()
        self.data = self.sort(self.data)
        end_time = time.time()

        elapsed = end_time - start_time

        print(f"Slutter med: {self.data}")
        print(f"Tid brugt: {elapsed:.6f} sekunder")

        return self.data

    def __str__(self):
        return f"{self.data}"
            


