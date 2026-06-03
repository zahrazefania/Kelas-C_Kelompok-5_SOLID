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
>>>>>>> 21d9f53c5715b2e29743e953d94dbe360e4087f9
        print(f"{kandang.nama_kandang} Telah dibersihkan.")