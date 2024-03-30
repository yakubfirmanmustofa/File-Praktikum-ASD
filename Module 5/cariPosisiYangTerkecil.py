def cariPosisiYangTerkecil(A,dariSini,sampaiSini):
    posisiYangTerkecil = dariSini
    for i in range(dariSini+1, sampaiSini):
        if A[i] < A[posisiYangTerkecil]:
            posisiYangTerkecil = i
    return posisiYangTerkecil

# A = [18, 13, 44, 25, 66, 107, 78, 89]
# j = cariPosisiYangTerkecil(A, 2, len(A))