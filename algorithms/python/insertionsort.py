def insertion_sort(nums):
    for i in range(0, len(nums)):
        j = 1
        while j > 0 and nums[j-1] > nums[j]:
            nums[j-1], nums[j] = nums[j], nums[j-1]
            j -= 1
    return nums
