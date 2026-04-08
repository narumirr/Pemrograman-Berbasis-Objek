# Modul gadget.py berisi kelas dan fungsi terkait penjualan HP

class Handphone:
    def __init__(self, merk, model, harga):
        # Inisialisasi atribut objek HP [cite: 156, 189]
        self.merk = merk
        self.model = model
        self.harga = harga
        self.stok = 10  # Stok default

    def tampilkan_info(self):
        # Menampilkan detail spesifikasi dan harga [cite: 162, 189]
        print(f"HP: {self.merk} {self.model}")
        print(f"Harga: Rp {self.harga}")
        print(f"Stok Tersedia: {self.stok}")

    def kurangi_stok(self, jumlah):
        # Logika untuk mengurangi stok saat terjual
        if self.stok >= jumlah:
            self.stok -= jumlah
            return True
        else:
            print(f"Maaf, stok {self.model} tidak mencukupi.")
            return False

def hitung_total_bayar(harga, jumlah):
    # Fungsi dengan return value untuk menghitung total belanja [cite: 85, 111]
    return harga * jumlah