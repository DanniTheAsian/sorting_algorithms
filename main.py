"""
Docstring
"""
from bogo import Bogo

def main():
    """
    Docstring
    """
    sort = Bogo(size=10, min_val=1, max_val=10)
    sorted_list = sort.bogosort()
    print(f"sorteret list: {sorted_list}")

if __name__ == '__main__':
    main()
