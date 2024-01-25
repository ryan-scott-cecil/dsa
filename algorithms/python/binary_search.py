def binary_search(data, search):
    left = 0
    right = len(data) - 1
    while left <= right:
        middle = (left + right) // 2
        if data[middle] < search:
            left = middle + 1
        elif data[middle] > search:
            right = middle -1
        else:
            return data[middle]
        