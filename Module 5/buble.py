def bubbleSort(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-i-1):
            if A[j] > A[j+i]:
                swap(A,j,j+i)

# L = [10, 51, 22, 18, 4, 31, 13, 5, 23, 64, 29]