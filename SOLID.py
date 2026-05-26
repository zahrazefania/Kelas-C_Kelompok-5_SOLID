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
    
    def __init__(self, nama_kandang):
        self.nama_kandang = nama_kandang
        self.hewan_list = []
    
    def tambah_hewan(self, hewan):
        self.hewan_list.append(hewan)
    
class BersihkanKandang:

    def bersihkan(self):
        print("Kandang dibersihkan.")

#Dikerjakan Aurrea Daffa Putri Febriana (K3525021)
class KebunBinatang:
    def __init__(self):
        self.daftar_kandang = []

    def tambah_kandang(self, kandang: Kandang):
        self.daftar_kandang.append(kandang)

    def rawat_semua_hewan(self):
        for kandang in self.daftar_kandang:
            for hewan in kandang.hewan_list:
                hewan.makan()
            if isinstance(hewan, HewanTerbang):
                hewan.terbang()

burung = Burung("Boni", "Omnivora")
ikan= Ikan("Goldie", "Herbivora")

kandang_burung = Kandang("Kandang Burung")
kandang_burung.tambah_hewan(burung)

kandang_aquarium = Kandang("Aquarium Utama")
kandang_aquarium.tambah_hewan(ikan)
