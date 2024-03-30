def binSe(kumpulan,target):
    low = 0
    high = len(kumpulan) - 1
    index = -1
    while (low <= high) and (index == -1):
        mid = (high + low) // 2
        if kumpulan[mid] == target:
            index = mid
            return index
        else:
            if target < kumpulan[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return False

    # A = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]