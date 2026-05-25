from abc import ABC, abstractmethod

#Dikerjakan Zahra Zefania (K3525078)
class Hewan(ABC):
    def __init__(self, nama, jenis):
        self.nama= nama
        self.jenis= jenis
        
    @abstractmethod
    def makan(self):
        pass
        
class HewanTerbang(Hewan):
    @abstractmethod
    def terbang(self):
        pass
        
#Dikerjakan Udzma Fithratun Nufuus (K3525076)
class Burung(HewanTerbang):
    
    def makan(self):
        print(f"{self.nama} sedang makan biji-bijian.")
        
    def terbang(self):
        print(f"{self.nama} sedang terbang di udara.")

class Ikan(Hewan):
    def makan(self):
        print(f"{self.nama} sedang makan pelet ikan.")
        
#Dikerjakan Nadia Indah Santika (K3525084)
class Kandang:
    
    def __init__(self):
    self.hewan_list = []
    
    def tambah_hewan(self, hewan):
    self.hewan_list.append(hewan)
    
class BersihkanKandang:

    def bersihkan(self):
        print("Kandang dibersihkan.")
