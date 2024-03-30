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

class SiswaSMA(Manusia):
    def __init__(self, nama, sma):
        super().__init__(nama)
        self.sma = sma
    def __str__(self):
        s = self.nama + ', bersekolah di ' + str(self.sma)
        return s    
    def ambilNama(self):
        return self.nama
    def ambilsma(self):
        return self.sma

p1 = Manusia("Fatimah")
p1.ucapkanSalam()

# p2 = Manusia("Budi")
# p2.ucapkanSalam()
# ak = Manusia("Abdul karim")
# ak.ucapkanSalam()
# ak.keadaan
# ak.olahraga("renang")
# ak.keadaan
# ak.makan("bakso")
# ak.keadaan
# ak.mengalikanDenganDua(8)