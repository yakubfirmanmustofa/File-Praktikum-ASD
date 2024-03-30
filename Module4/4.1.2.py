class MhsTIF:
    def __init__(self, nama, nim, kotaTinggal, saku):
        self.nama = nama
        self.nim = nim
        self.kotaTinggal = kotaTinggal
        self.saku = saku
    

c0 = MhsTIF("Ika", 10, "Sukoharjo", 240000)
c1 = MhsTIF('Budi', 51, 'Sragen', 230000)
c2 = MhsTIF('Ahmad', 2, 'Surakarta', 250000)
c3 = MhsTIF('Candra', 18, 'surakarta', 235000)
c4 = MhsTIF('Eka', 4, 'Boyolali', 240000)
c5 = MhsTIF('Fandi', 31, 'Salatiga', 250000)
c6 = MhsTIF('Deni', 13, 'Klaten', 245000)
c7 = MhsTIF('Galuh', 5, 'Wonogirii', 245000)
c8 = MhsTIF('Janto', 23, 'Klaten', 240000)
c9 = MhsTIF('Hasan', 64, 'Karanganyar', 270000)
c10 = MhsTIF('Khalid', 29, 'Purwodadi', 265000)

Daftar = [c0, c1, c2, c3, c4, c5, c6, c7, c8, c9, c10]

target = "Klaten"
for i in Daftar:
    if i.kotaTinggal == target:
        print(i.nama + " tinggal di" + target)

def cariTerkecil(kumpulan):
    n = len(kumpulan)
    terkecil = kumpulan[0].saku
    for i in range(1, n):
        if kumpulan[i].saku < terkecil:
            terkecil = kumpulan[i].saku
    return terkecil

def cariTerbesar(kumpulan):
    n = len(kumpulan)
    terbesar = kumpulan[0].saku
    for i in range(1, n):
        if kumpulan[i].saku > terbesar:
            terbesar = kumpulan[i].saku
    return terbesar


