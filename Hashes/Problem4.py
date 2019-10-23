def single_number(nums):
    nums_appeared_odd_time = set()
    for num in nums:
        if num in nums_appeared_odd_time:
            nums_appeared_odd_time.remove(num)
        else:
            nums_appeared_odd_time.add(num)

    for num in nums:
        if num in nums_appeared_odd_time:
            return num

print(single_number([4,1,2,1,2]))
