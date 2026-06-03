from abc import ABC, abstractmethod

class Hewan(ABC):
    def __init__(self, nama, jenis):
        self_nama=nama
        self_jenis=jenis
        
    @abstractmethod    
    def makan(self):
        pass
    
class HewanTerbang(ABC):
    @abstractmethod
    def terbang(self):
        pass