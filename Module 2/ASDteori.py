# def faktorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * faktorial(n-1)

# a = faktorial(999)
# print(a)

class JajarGenjang(object):
    """ data dan proses terhadap jajar genjang dengan alas a dan tinggi t
    """

    def __init__(self, alas, tinggi):
        """ mengisi property yang tidak punya nilai default """
        self.alas = alas
        self.tinggi = tinggi
        

    def luas(self):
        """ mengembalikan luas jajar genjang ini """
        return self.alas * self.tinggi


# membuat object  instance untuk alas=3 dan tinggi=5
jajar_genjang = JajarGenjang(3,5)
# menampilkan alas jajar genjang
print("Alas jajar genjang: ", jajar_genjang.alas)
# menampilkan luas jajar genjang
print("Luas jajar genjang: ", jajar_genjang.luas())
