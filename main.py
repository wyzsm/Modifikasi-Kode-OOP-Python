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
    def __init__(self, nama_tank, jenis_tank):  # CONSTRUCTOR
        self._nama_tank = nama_tank  # ENCAP / AccMod
        self._jenis_tank = jenis_tank

    def info(self):
        print(f"\nNama Tank  : {self._nama_tank}")
        print(f"Jenis Tank : {self._jenis_tank}")

    def latihan(self):
        print(f"\n{self._nama_tank}: Berjalan di medan...")


# SUBCLASS ALUTSISTA (KAPAL PERANG)
class Kapal_Perang(Alutsista):
    def __init__(self, nama_kapal, jenis_kapal):  # CONSTRUCTOR
        self._nama_kapal = nama_kapal  # ENCAP / AccMod
        self._jenis_kapal = jenis_kapal

    def info(self):
        print(f"\nNama Kapal  : {self._nama_kapal}")
        print(f"Jenis Kapal : {self._jenis_kapal}")

    def latihan(self):
        print(f"{self._nama_kapal}: Berlayar di perairan...")


# SUBCLASS ALUTSISTA (PESAWAT TEMPUR)
class Pesawat_Tempur(Alutsista):
    def __init__(self, nama_pesawat, jenis_pesawat):  # CONSTRUCTOR
        self._nama_pesawat = nama_pesawat  # ENCAP / AccMod
        self._jenis_pesawat = jenis_pesawat

    def info(self):
        print(f"\nNama Pesawat  : {self._nama_pesawat}")
        print(f"Jenis Pesawat : {self._jenis_pesawat}")

    def latihan(self):
        print(f"{self._nama_pesawat}: Terbang di langit...")


def buat_alutsista():
    print("\nPilih jenis alutsista yang ingin dibuat:")
    print("1. Tank")
    print("2. Kapal Perang")
    print("3. Pesawat Tempur")
    pilihan = input("Masukkan nomor pilihan (1/2/3): ")

    if pilihan == "1":
        nama_tank = input("\nMasukkan nama tank  : ")
        jenis_tank = input("Masukkan jenis tank : ")
        alutsista_baru = Tank(nama_tank, jenis_tank)
        return alutsista_baru
    elif pilihan == "2":
        nama_kapal = input("\nMasukkan nama kapal perang  : ")
        jenis_kapal = input("Masukkan jenis kapal perang : ")
        alutsista_baru = Kapal_Perang(nama_kapal, jenis_kapal)
        return alutsista_baru
    elif pilihan == "3":
        nama_pesawat = input("\nMasukkan nama pesawat tempur  : ")
        jenis_pesawat = input("Masukkan jenis pesawat tempur : ")
        alutsista_baru = Pesawat_Tempur(nama_pesawat, jenis_pesawat)
        return alutsista_baru
    else:
        print("Pilihan tidak valid.")
        return None


def main():
    daftar_alutsista = []

    while True:
        print("\nSelamat Datang. Ada yang bisa dibantu?")
        print(
            "1. Buat Alutsista\n2. Lihat Informasi Alutsista\n3. Latih Alutsista\n4. Keluar"
        )
        pilihan = input("Pilihan (1/2/3/4): ")

        if pilihan == "1":
            alutsista_baru = buat_alutsista()
            if alutsista_baru:
                daftar_alutsista.append(alutsista_baru)
        elif pilihan == "2":
            if daftar_alutsista:
                for alutsista in daftar_alutsista:  # POLYMORPHISM
                    alutsista.info()
            else:
                print("Belum ada alutsista yang dibuat.")
        elif pilihan == "3":
            if daftar_alutsista:
                for alutsista in daftar_alutsista:  # POLYMORPHISM
                    alutsista.latihan()
            else:
                print("Belum ada alutsista yang dibuat.")
        elif pilihan == "4":
            print("Terima kasih. Sampai jumpa!")
            break
        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
