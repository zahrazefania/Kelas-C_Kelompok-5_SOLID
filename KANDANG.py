<<<<<<< HEAD
from BINATANG import Burung, Ikan
class Kandang:
    
    def _init_(self, nama_kandang):
        self.nama_kandang = nama_kandang
        self.hewan_list = []
    
    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)
    
class BersihkanKandang:

    def bersihkan(self, kandang: Kandang):
=======
from BINATANG import Burung, Ikan
class Kandang:
    
    def _init_(self, nama_kandang):
        self.nama_kandang = nama_kandang
        self.hewan_list = []
    
    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)
    
class BersihkanKandang:

    def bersihkan(self, kandang: Kandang):
>>>>>>> 48796186f61536183bc3c56ace24a6a714bc1064
        print(f"{kandang.nama_kandang} Telah dibersihkan.")