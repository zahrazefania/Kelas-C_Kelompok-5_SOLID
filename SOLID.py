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

#Dikerjakan Nadia Indah Santika (K3525084)
