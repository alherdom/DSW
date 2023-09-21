def mult(numbers: str) -> int:
    result = 1
    for number in numbers:
        result *= int(number)
    return result

def max_product(sequence: str, span: int) -> int:
    if span > len(sequence) or span <= 0 or not sequence.isnumeric():
        raise ValueError("Invalid input arguments!")
    return max([mult(sequence[i:i+span]) for i in range(len(sequence) - span + 1)])