class MhsTIF(object):
    def __init__(self,nama,nim,kota,us):
        self.nama = nama 
        self.nim = nim
        self.kotaTinggal = kota
        self.uangSaku = us
    def __str__(self):
        s = self.nama +"," + str(self.nim) \
         + ',' + self.kotaTinggal \
         + ',' + str(self.uangSaku)
        return s

c0 = MhsTIF('Ika',10,'Sukoharjo',240000)
c1 = MhsTIF('Budi',51,'Sragen',230000)
c2 = MhsTIF('Ahmad',2,'Surakarta',250000)
c3 = MhsTIF('Chandra',18,'Surakarta',235000)
c4 = MhsTIF('Eka',4,'Boyolali',240000)
c5 = MhsTIF('Fandi',31,'Salatiga',250000)
c6 = MhsTIF('Deni',13,'Klaten',245000)
c7 = MhsTIF('Galuh',5,'Wonogiri',245000)
c8 = MhsTIF('Janto',23,'Klaten',245000)
c9 = MhsTIF('Hasan',64,'Karanganyar',270000)
c10 = MhsTIF('Khalid',29,'Purwodadi',265000)

Daftar = [c0,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10]

# No1
def asal(kumpulan, x):
    i = []
    for j in kumpulan:
        if j.kotaTinggal == x:
            a = kumpulan.index(j)
            i.append(a)
    return i
# No2
def uangSakuKcl(kumpulan):
    terkecil = kumpulan[0].uangSaku
    for i in kumpulan:
        if i.uangSaku < terkecil:
            terkecil = i.uangSaku
            return terkecil
# No3
def cariTerkecil(kumpulan):
    terkecil = kumpulan[0].uangSaku
    hasil = kumpulan[0]
    for mhs in kumpulan:
        if mhs.uangSaku < terkecil:
            terkecil = mhs.uangSaku
            hasil = mhs
    print(hasil.nama, hasil.uangSaku)

# No4
def kurang250(kumpulan):
    for i in kumpulan:
        if i.uangSaku < 250000:
            print (i)

