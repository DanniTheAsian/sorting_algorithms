"""
Docstring
"""
import random
from bubble import Bubble
from merge import Merge
from bogo import Bogo

def main():
    """
    Docstring
    """
    numbers = [random.randint(1, 9) for _ in range(30)]
    print(f"Tilfældigt genereret liste: {numbers}\n")

    print("=== BOGOSORT ===")
    bogosort = Bogo(data=list(numbers))
    bogo_sorted_list = bogosort.bogosort()
    print(f"Bogosort – sorteret liste: {bogo_sorted_list}\n")

    print("=== BUBBLESORT ===")
    bubblesort = Bubble(data=list(numbers))
    bubble_sorted_list = bubblesort.bubblesort()
    print(f"Bubblesort – sorteret liste: {bubble_sorted_list}\n")

    print("=== MERGESORT ===")
    mergesort = Merge(data=list(numbers))
    merge_sorted_list = mergesort.mergesort()
    print(f"Mergesort – sorteret liste: {merge_sorted_list}\n")
if __name__ == '__main__':
    main()
