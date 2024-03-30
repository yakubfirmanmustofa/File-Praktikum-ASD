def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# for number in range(2, 1001):
#     if is_prime(number):
#         print(number)

# A = [ [2,3], [5,7] ]
# A[0][1]
# 3
# A[1][1]
# 7

# B = [ [0 for j in range(3)] for i in range(3) ]
# B
# [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# [x**2 for x in range(0,7)]
# [0, 1, 4, 9, 16, 25, 36]
# [(x,x**2) for x in range(7)]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25), (6, 36)]
# [x**2 for x in range(15) if x%2==0]
# [0, 4, 16, 36, 64, 100, 144, 196]
# [3 for i in range(5)]
# [3, 3, 3, 3, 3]