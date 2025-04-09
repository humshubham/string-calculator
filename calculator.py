def add(numbers: str) -> int:
    if numbers == "":
        return 0

    delimiter = ","
    if numbers.startswith("//"):
        delimiter_line, numbers = numbers.split("\n", 1)
        delimiter = delimiter_line[2:]

    numbers = numbers.replace("\n", delimiter)
    parts = numbers.split(delimiter)
    nums = [int(p) for p in parts]
    
    negative_nums = [str(n) for n in nums if n < 0]
    if negative_nums:
        raise Exception(f"negative numbers not allowed {'/'.join(negative_nums)}")

    return sum(nums)