from abc import ABC, abstractmethod

class Hewan:
    def __init__(self, nama, jenis):
        self.nama= nama
        self.jenis= jenis
        
    @abstractmethod
    def makan(self):
        pass
    
class HewanTerbang(Hewan, ABC):
    def terbang(self):
        pass