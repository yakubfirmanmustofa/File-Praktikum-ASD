def awal(array, n) :
    low = 0
    high = len(array) - 1
    while (low <= high) :
        mid = int (low + (high-low)/2)
        if (array[mid] == n) :
            if (mid-1 >= 0 and array[mid-1] == n) :
                high = mid-1
                continue
            return mid
        elif (array[mid] < n) :
            low = mid + 1
        else :
            high = mid - 1
    return -1
def akhir(array, n) :
    low = 0
    high = len(array)-1
    while (low <= high) :
        mid = int(low + (high-low)/2)
        if (array[mid] == n) :
            if (mid+1 < len(array) and array[mid+1]== n) :
                low = mid + 1
                continue
            return mid
        elif (array[mid] < n) :
            low = mid + 1
        else :
            high = mid - 1
    return -1
array = [2,3,5,6,6,6,5,8,9,9,10,11,12,13,13,14]
def binSe(array,target):
    awal_index = awal(array, target)
    akhir_index = akhir(array, target)
    hasil = []
    for x in range(awal_index,akhir_index+1):
        hasil.append(x)
    return hasil
print(binSe(array,6))
