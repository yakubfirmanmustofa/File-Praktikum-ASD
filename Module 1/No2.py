def gambarlahPersegiEmpat(panjang, lebar):
    for i in range(lebar):
        if i == 0 or i == lebar - 1:
            print('@' * panjang)
        else:
            print('@' + ' ' * (panjang - 2) + '@')