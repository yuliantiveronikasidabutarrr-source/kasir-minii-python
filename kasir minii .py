print("=== Kasir Mini ===")
jumlah_kategori = int(input("Jumlah Kategori: "))
barang = {}        # Menyimpan data (kategori → list barang)
total = 0
for k in range(jumlah_kategori):
    kategori = input(f" Nama kategori ke-{k+1}: ")
    jumlah_barang = int(input(f"Jumlah barang dalam {kategori}: "))

    barang[kategori] = []  # siapkan list

    for i in range(jumlah_barang):
        print(f" Barang ke-{i+1} di {kategori}:")
        nama = input("    Nama barang : ")
        harga = int(input("    Harga       : "))

        barang[kategori].append((nama, harga))
        total += harga

# --- Hitung Diskon ---
diskon = 0
if total >= 500000:
    diskon = total * 0.10

total_akhir = total - diskon

# --- Cetak Struk ---
print("======================= STRUK PEMBELIAN ======================")
print("--------------------------------------------------------------")
for kategori, daftar in barang.items():
    print(f" Kategori: {kategori}")
    for nama, harga in daftar:
        print(f" {nama:<20} Rp {harga}")

print(f"Total Belanja          : Rp {total}")
print(f"Diskon (10%)           : Rp {diskon}")
print(f"Total yang Dibayar     : Rp {total_akhir}")
print("==============================================================")
print("Terima kasih telah berbelanja!")