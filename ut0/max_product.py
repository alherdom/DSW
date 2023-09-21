def mult(numbers: str) -> int:
    result = 1
    for number in numbers:
        result *= int(number)
    return result

def max_product(sequence: str, span: int) -> int:
    if span > len(sequence) or span <= 0 or not sequence.isnumeric():
        raise ValueError("Invalid input arguments!")
    return max([mult(sequence[i:i+span]) for i, char in enumerate(sequence) if i <= len(sequence) -span])
    
    # Sin comprensión y usando 'break':
    # parts_sequence = []
    # for i, char in enumerate(sequence):
    #     parts_sequence.append(mult(sequence[i:i+span]))
    #     if i == len(sequence) - span:
    #         break
    # return max(parts_sequence)