def merge_sort(nums):
    if len(nums) < 2:
        return nums
    left_half = nums[0: len(nums)//2]
    right_half = nums[len(nums)//2:]
    return merge(merge_sort(left_half), merge_sort(right_half))

def merge(first, second):
    i, j, merged = 0, 0, []
    while i < len(first) and j < len(second):
        if first[i] >= second[j]:
            merged.append(first[i])
            i += 1
        else:
            merged.append(second[j])
            j += 1
    while i < len(first):
        merged.append(first[i])
        i += 1
    while j < len(second):
        merged.append(second[j])
        j += 1
    return merged