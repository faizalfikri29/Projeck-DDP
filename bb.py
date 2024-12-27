# Fungsi untuk menghitung Berat Badan Ideal (BBI) Balita
def hitung_bbi_balita(usia, satuan='tahun'):
    # Konversi ke tahun jika input dalam bulan
    if satuan == 'bulan':
        usia_tahun = usia / 12
    else:
        usia_tahun = usia
    
    # Perhitungan BBI berdasarkan usia
    if usia_tahun < 1:
        # Untuk balita di bawah 1 tahun
        # BBI = (usia dalam bulan / 2) + 4
        usia_bulan = usia_tahun * 12
        bbi = (usia_bulan / 2) + 4
    else:
        # Untuk balita di atas 1 tahun
        # BBI = (usia dalam tahun x 2) + 8
        bbi = (usia_tahun * 2) + 8
    
    return round(bbi, 2)

# Contoh penggunaan
def main():
    while True:
        try:
            # Input usia
            usia = float(input("Masukkan usia balita: "))
            
            # Pilih satuan
            satuan = input("Satuan usia (tahun/bulan): ").lower()
            
            # Validasi satuan
            if satuan not in ['tahun', 'bulan']:
                print("Masukkan satuan yang valid (tahun/bulan)")
                continue
            
            # Hitung BBI
            bbi = hitung_bbi_balita(usia, satuan)
            
            # Tampilkan hasil
            print(f"Berat Badan Ideal (BBI) balita: {bbi} kg")
            
            # Tanya apakah ingin menghitung lagi
            lanjut = input("Ingin menghitung lagi? (ya/tidak): ").lower()
            if lanjut != 'ya':
                break
        
        except ValueError:
            print("Masukkan usia dengan angka yang valid")

# Jalankan program
if __name__ == "__main__":
    main()