def cleanup_decorator(func):
    def wrapper(numbers):
        if numbers == "":
            return 0

        delimiter = ","
        if numbers.startswith("//"):
            delimiter_line, numbers = numbers.split("\n", 1)
            delimiter = delimiter_line[2:]

        numbers = numbers.replace("\n", delimiter)
        parts = ["sum"] if delimiter!="*" else ["product"]

        parts.extend(numbers.split(delimiter))
        
        return func(parts)
    return wrapper

@cleanup_decorator
def calc(numbers: list) -> int:

    operation, *nums = numbers
    nums = list(map(int, nums))
    
    negative_nums = [str(n) for n in nums if n < 0]
    if negative_nums:
        raise Exception(f"negative numbers not allowed {'/'.join(negative_nums)}")
    
    if operation=="product":
        
        from functools import reduce
        from operator import mul
        ans = reduce(mul, nums, 1)
        return ans

    return sum(nums)