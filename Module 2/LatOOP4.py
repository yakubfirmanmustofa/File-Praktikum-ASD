class Manusia(object):
    keadaan = "lapar"
    def __init__(self,nama):
        self.nama = nama
    def ucapkanSalam(self):
        print("Salaam, namaku", self.nama)
    def makan(self, s):
        print("Saya baru saja makan", s)
        self.keadaan = "kenyang"
    def olahraga(self,k):
        print("Saya baru saja latihan", k)
        self.keadaan = "lapar"
    def mengalikanDenganDua(self,n):
        return n*2

class Mahasiswa(Manusia):
    def __init__(self, nama, NIM, kota, us):
        super().__init__(nama)
        self.NIM = NIM
        self.kotaTinggal = kota
        self.uangSaku = us
        self.listKuliah = [] #tugas 4   
    def __str__(self):
        s = self.nama + ', NIM ' + str(self.NIM) \
            + '. Tinggal di ' + self.kotaTinggal \
            + '. Uang saku Rp ' + str(self.uangSaku) \
            + ' tiap bulannya.'
        return s    
    def ambilNama(self):
        return self.nama
    def ambilNIM(self):
        return self.NIM    
    def ambilUangSaku(self):
        return self.uangSaku    
    def makan(self, s):
        print("Saya baru saja makan", s, "sambil belajar.")
        self.keadaan = 'kenyang'

        # tugas 2.a
    def ambilKotaTinggal(self):
        return self.kotaTinggal

        # tugas 2.b
    def perbaruiKotaTinggal(self, kotaBaru):
        self.kotaTinggal = kotaBaru

        # tugas 2.c
    def ambilUangSakul(self):
        return self.uangSaku
    def tambahUangSaku(self,tambahSaku):
        self.uangSaku += tambahSaku

        # tugas 4
    def ambilKuliah(self, nama_kuliah):
        self.listKuliah.append(nama_kuliah)
        # tugas 5
    def hapusKuliah(self, nama_kuliah):
        if nama_kuliah in self.listKuliah:
            self.listKuliah.remove(nama_kuliah)
        else:
            print("Error: Mata kuliah tidak ditemukan.")
            #yugas 7
class MhsTIF(Mahasiswa):
    def katakanPy(self):
        print("Python is cool.")

        # tugas 3
#def inputMahasiswaBaru():
#         nama = input("Masukkan nama mahasiswa: ")
#         NIM = input("Masukkan NIM mahasiswa: ")
#         kota = input("Masukkan kota tempat tinggal mahasiswa: ")
#         uang_saku = int(input("Masukkan jumlah uang saku mahasiswa: "))
#        
#         return Mahasiswa(nama, NIM, kota, uang_saku)
#mahasiswaBaru = inputMahasiswaBaru()

        
m1 = Mahasiswa("Jamil", 234, "Surakarta", 250000)
m2 = Mahasiswa("Andi",365,"Magelang",275000)
m3 = Mahasiswa("Sri", 676,"Yogyakarta",240000)
# m9 = Mahasiswa("Firman", 36, "surabaya", 250000) #tugas 2
# m7 = Mahasiswa("Yakub", 37, "Tuban", 270000) #tugas 3
# m234 = Mahasiswa("Yusup", 38, "Jakarta", 300000) #tugas 4

# m1.ambilNama()
# m2.ambilNIM()
# m3.ucapkanSalam()
# m3.keadaan
# m3.makan("gado-gado")
# m3.keadaan
# print(m3)

# 2.6
# daftar = [m1, m2, m3]
# for i in daftar: print(i.NIM)
# for i in daftar: print(i)
# daftar[2].ambilNama()

# 2.a 
# m9.ambilKotaTinggal()

# 2.b 
# m9.perbaruiKotaTinggal("Sleman")
# m9.ambilKotaTinggal()

# 2.c 
# m7.ambilUangSaku()
# m7.tambahUangSaku(50000)
# m7.ambilUangSaku()

# 4
# m234.listKuliah
# m234.ambilKuliah("Matematika Diskrit")
# m234.listKuliah
# m234.ambilKuliah("Algoritma dan Struktur Data")
# m234.listKuliah
# m234.hapusKuliah("Matematika Diskrit")
# 5
# m234.listKuliah
