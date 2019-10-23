def repeated_number(nums):
    nums_in_list = set()
    for num in nums:
        if num in nums_in_list:
            return num
        nums_in_list.add(num)
    return False

print(repeated_number([3, 4, 6, 1, 10, 10, -1]))