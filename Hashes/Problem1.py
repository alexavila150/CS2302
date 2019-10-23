def two_sum(nums, target):
    nums_needed = set()
    for num in nums:
        nums_needed.add(num - target)

    for num in nums:
        if num in nums_needed:
            return [num, target - num]

print(two_sum([2, 7, 11, 15], 9))