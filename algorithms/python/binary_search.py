def binary_search(data, search):
    left = 0
    right = len(data) - 1
    while left <= right:
        middle = (left + right) // 2
        if data[middle] == search:
            return data[middle]        
        if data[middle] < search:
            left = middle + 1
        if data[middle] > search:
            right = middle - 1
    return None
        