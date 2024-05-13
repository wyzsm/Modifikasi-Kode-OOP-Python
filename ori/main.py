from abc import ABC, abstractmethod


# SUPERCLASS
class Alutsista:
    @abstractmethod
    def info(self):
        pass  # ABSTRACT METHOD

    def latihan(self):
        pass  # ABSTRACT METHOD


# SUBCLASS ALUTSISTA (TANK)
class Tank(Alutsista):
    def __init__(self):  # CONSTRUCTOR
        super().__init__()
        self._nama_tank = input("\nMasukkan nama tank : ")  # ENCAP / AccMod
        self._jenis_tank = input("Masukkan jenis tank: ")

    def info(self):
        print(f"\nNama Tank  : {self._nama_tank}")
        print(f"Jenis Tank : {self._jenis_tank}")

    def latihan(self):
        print(f"\n{self._nama_tank}: Berjalan di medan...")


# SUBCLASS ALUTSISTA (KAPAL PERANG)
class Kapal_Perang(Alutsista):
    def __init__(self):  # CONSTRUCTOR
        super().__init__()
        self._nama_kapal = input("\nMasukkan nama kapal perang : ")  # ENCAP / AccMod
        self._jenis_kapal = input("Masukkan jenis kapal perang: ")

    def info(self):
        print(f"\nNama Kapal  : {self._nama_kapal}")
        print(f"Jenis Kapal : {self._jenis_kapal}")

    def latihan(self):
        print(f"{self._nama_kapal}: Berlayar di perairan...")


# SUBCLASS ALUTSISTA (PESAWAT TEMPUR)
class Pesawat_Tempur(Alutsista):
    def __init__(self):  # CONSTRUCTOR
        super().__init__()
        self._nama_pesawat = input("\nMasukkan nama pesawat tempur: ")  # ENCAP / AccMod
        self._jenis_pesawat = input("Masukkan jenis pesawat tempur: ")

    def info(self):
        print(f"\nNama Pesawat  : {self._nama_pesawat}")
        print(f"Jenis Pesawat : {self._jenis_pesawat}")

    def latihan(self):
        print(f"{self._nama_pesawat}: Terbang di langit...")


tank_1 = Tank()
kapal_1 = Kapal_Perang()
pesawat_1 = Pesawat_Tempur()

for Alutsista in [tank_1, kapal_1, pesawat_1]:  # POLYMORPHISM
    Alutsista.latihan()
