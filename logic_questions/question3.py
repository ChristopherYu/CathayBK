test_data = 10


def get_sequence(num):
    if num == 0:
        return 0
    nums = range(1, num + 1)
    original = {key: 0 for key in nums}
    start = 1
    while len(original) > 1:
        for key in sorted(list(original.keys())):
            original[key] = start
            start += 1
        original = {key: value for key, value in original.items() if value % 3 != 0}
    return list(original.keys())[0]


print(get_sequence(test_data))
