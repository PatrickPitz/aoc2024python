import re
from util.aoc_loader import AocLoader

def sum_multiples(data):
    pattern  = re.compile(r'mul\((\d+),(\d+)\)')
    matches = pattern.findall(data)
    return sum([int(match[0]) * int(match[1]) for match in matches])

def sum_multiples_part2(data):
    pattern_mul = re.compile(r'mul\((\d+),(\d+)\)')
    pattern_do = re.compile(r'do\(\)')
    pattern_dont = re.compile(r"don't\(\)")

    enabled = True
    total_sum = 0
    pos = 0

    while pos < len(data):
        do_match = pattern_do.match(data, pos)
        dont_match = pattern_dont.match(data, pos)
        mul_match = pattern_mul.match(data, pos)

        if do_match:
            enabled = True
            pos += do_match.end() - do_match.start()
        elif dont_match:
            enabled = False
            pos += dont_match.end() - dont_match.start()
        elif mul_match:
            if enabled:
                x, y = map(int, mul_match.groups())
                total_sum += x * y
            pos += mul_match.end() - mul_match.start()
        else:
            pos += 1
    return total_sum



aoc = AocLoader(3)
aoc_data = aoc.load_data()

sum_multiples(aoc_data)
print(sum_multiples(aoc_data))
print(sum_multiples_part2(aoc_data))