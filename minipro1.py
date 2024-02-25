import os
os.system("cls")

class Instrumen:
    def __init__(self, nama, merek, kategori, harga, stok):
        self.nama = nama
        self.merek = merek
        self.kategori = kategori
        self.harga = harga
        self.stok = stok

    def display_info(self):
        print(f"{self.nama} ({self.merek}) ({self.kategori}) - ${self.harga:.2f}, stok: {self.stok}")

class MusicShop:
    def __init__(self, nama, default_data=None):
        self.nama = nama
        self.inventory = []
        
        if default_data:
            for data in default_data:
                self.create_instrumen(*data, print_message=False) 

    def add_instrumen(self, instrumen):
        self.inventory.append(instrumen)

    def display_inventory(self):
        print(f"\nInventory of {self.nama}:")
        for instrumen in self.inventory:
            instrumen.display_info()

    def find_instrumen(self, instrumen_nama):
        for instrumen in self.inventory:
            if instrumen.nama.lower() == instrumen_nama.lower():
                return instrumen
        return None

    def create_instrumen(self, nama, merek, kategori, harga, stok, print_message=True):
        new_instrumen = Instrumen(nama, merek, kategori, harga, stok)
        self.add_instrumen(new_instrumen)
        if print_message:
            print(f"\nInstrument '{nama}' telah ditambahkan!.")

    def update_instrumen(self, instrumen_nama, new_harga, new_stok):
        instrumen = self.find_instrumen(instrumen_nama)
        if instrumen:
            instrumen.harga = new_harga
            instrumen.stok = new_stok
            print(f"\ninstrumen '{instrumen_nama}' telah di Update.")
        else:
            print(f"\ninstrumen '{instrumen_nama}' Tidak ada")

    def delete_instrumen(self, instrumen_nama):
        instrumen = self.find_instrumen(instrumen_nama)
        if instrumen:
            self.inventory.remove(instrumen)
            print(f"\ninstrumen '{instrumen_nama}' telah dihapus.")
        else:
            print(f"\ninstrumen '{instrumen_nama}' tidak ada.")


def main():
    default_instruments = [
        ("Guitar", "Fender", "String", 500.0, 10),
        ("Keyboard", "Yamaha", "Piano", 800.0, 5),
    ]

    music_shop = MusicShop("Melody Music", default_data=default_instruments)


    while True:
        print("\nPilihan:")
        print("1. Lihat Penyimpanan")
        print("2. Tambah Instrumen")
        print("3. Update Instrumen")
        print("4. Hapus Instrumen")
        print("0. Exit")

        choice = input("Masukkan Pilihan: ")

        if choice == "1":
            os.system("cls")
            music_shop.display_inventory()
        elif choice == "2":
            os.system("cls")
            nama = input("Masukkan nama instrumen: ")
            merek = input("Masukkan merek instrumen: ")
            kategori = input("Masukkan kategori instrumen: ")
            harga = float(input("Masukkan harga instrumen: "))
            stok = int(input("Masukkan instrumen stok: "))
            music_shop.create_instrumen(nama, merek, kategori, harga, stok)
        elif choice == "3":
            os.system("cls")
            instrumen_nama = input("Masukkan nama instrumen yang akan diupdate: ")
            new_harga = float(input("Masukkan harga baru: "))
            new_stok = int(input("Masukkan stok baru: "))
            music_shop.update_instrumen(instrumen_nama, new_harga, new_stok)
        elif choice == "4":
            os.system("cls")
            instrumen_nama = input("Masukkan nama instrumen yang akan dihapus: ")
            music_shop.delete_instrumen(instrumen_nama)
        elif choice == "0":
            os.system("cls")
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
