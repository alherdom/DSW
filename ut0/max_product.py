import sys

def mult(numbers: list[int]) -> int:
    result = 1
    for number in numbers:
        result *= number
    return result

def max_product(sequence: str, span: int) -> int:
    if span > len(sequence) or span <= 0 or not sequence.isnumeric():
        raise ValueError("Invalid input arguments!")
    
    