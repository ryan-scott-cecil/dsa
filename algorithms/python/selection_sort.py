def selection_sort(nums):
    for i in range(0, len(nums)):
        smallest_idx = i
        for j in range(smallest_idx, len(nums)):
            if nums[j] < nums[smallest_idx]:
                smallest_idx = j
        nums[i], nums[smallest_idx] = nums[smallest_idx], nums[i]
    return nums
