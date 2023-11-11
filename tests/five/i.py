def binnary_search(num, lst):
    result = None
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == num:
            result = mid
            high = mid - 1
        elif lst[mid] > num:
            high = mid - 1
        else:
            low = mid + 1
    return result
