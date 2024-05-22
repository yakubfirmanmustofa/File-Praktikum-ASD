class MhsTIF(object):
    def __init__(self,nama,nim,kota,us):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us
m1 = MhsTIF('Yakub',105,'Surabaya',250000)
m2 = MhsTIF('Firman',101,'Surakarta',255000)
m3 = MhsTIF('Mustofa',103,'Tuban',350000)
m4 = MhsTIF('Muhammad',102,'Jakarta',275000)
m5 = MhsTIF('Al-Fatih',104,'Yogyakarta',300000)
Daftar = [m1,m2,m3,m4,m5]
def swap(a,b,c):
    tmp = a[b]
    a[b] = a[c]
    a[c] = tmp
def urutkanNIM(mhstif):
    n = len(mhstif)
    for i in range(n-1):
        for j in range(n-i-1):
            if mhstif[j].nim > mhstif[j+1].nim:
                swap(mhstif,j,j+1)
def cetak(mhstif):
    for i in mhstif:
        print( i.nim, i.nama, i.kotaTinggal)

    print('\n--- Oleh L200220036 ---')
