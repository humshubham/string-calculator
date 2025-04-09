def add(numbers: str) -> int:
    if numbers == "":
        return 0

    delimiter = ","
    if numbers.startswith("//"):
        delimiter_line, numbers = numbers.split("\n", 1)
        delimiter = delimiter_line[2:]

    numbers = numbers.replace("\n", delimiter)
    parts = numbers.split(delimiter)
    return sum(int(p) for p in parts)