from util.aoc_loader import AocLoader

def check_safety(nums):
    for i, _ in enumerate(nums[:-1]):
        if not(1 <= nums[i + 1] - nums[i] <= 3):
            return False
    return True

def check_safety_part2(nums):
    unsafe_count = 0
    for i, _ in enumerate(nums[:-1]):
        if not(1 <= nums[i + 1] - nums[i] <= 3):
            unsafe_count += 1
        if unsafe_count > 1:
            return False
    return True

def count_safe_sequences(data, check_func):
    safe_count = 0
    for line in data.splitlines():
        numbers = list(map(int, line.split()))
        if ((numbers[0] < numbers[1] and check_func(numbers))
                or (numbers[0] > numbers[1] and check_func(numbers[::-1]))):
            safe_count += 1
    return safe_count

aoc = AocLoader(2)
aoc_data = aoc.load_data()

print(count_safe_sequences(aoc_data, check_safety))
print(count_safe_sequences(aoc_data, check_safety_part2))