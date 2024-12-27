def hitung_tinggi_badan_balita(jenis_kelamin, umur):
    if not (0 <= umur <= 5):
        return "Umur harus antara 1 hingga 5 tahun."
    
    # Data rata-rata tinggi badan berdasarkan WHO (dalam cm)
    tinggi_laki_laki = {
        0: 49.9, 1: 54.7, 2: 58.4, 3: 61.4, 4: 63.9, 5: 65.9, 6: 67.6,
        12: 76.1, 24: 87.8, 36: 95.2, 48: 102.3, 60: 109.2
    }
    
    tinggi_perempuan = {
        0: 49.1, 1: 53.7, 2: 57.1, 3: 59.8, 4: 62.1, 5: 64.0, 6: 65.7,
        12: 74.0, 24: 86.4, 36: 94.1, 48: 101.0, 60: 107.4
    }
    
    # Pilih data sesuai jenis kelamin
    if jenis_kelamin.lower() == "laki-laki":
        data_tinggi = tinggi_laki_laki
    elif jenis_kelamin.lower() == "perempuan":
        data_tinggi = tinggi_perempuan
    else:
        return "Jenis kelamin tidak valid. Gunakan 'laki-laki' atau 'perempuan'."
    
    # Jika umur ada di data, langsung kembalikan tinggi
    if umur in data_tinggi:
        return data_tinggi[umur]
    
    # Jika umur tidak ada, lakukan interpolasi linear
    umur_sebelum = max(k for k in data_tinggi.keys() if k < umur)
    umur_setelah = min(k for k in data_tinggi.keys() if k > umur)
    
    tinggi_sebelum = data_tinggi[umur_sebelum]
    tinggi_setelah = data_tinggi[umur_setelah]
    
    # Rumus interpolasi linear
    tinggi_estimasi = tinggi_sebelum + (tinggi_setelah - tinggi_sebelum) * (
        (umur - umur_sebelum) / (umur_setelah - umur_sebelum)
    )
    
    return round(tinggi_estimasi, 2)



# Program utama
def main():
    print("Program Menghitung Estimasi Tinggi Badan Balita")
    jenis_kelamin = input("Masukkan jenis kelamin (laki-laki/perempuan): ").strip()
    try:
        umur = int(input("Masukkan umur balita dalam tahun (1-5): ").strip())
    except ValueError:
        print("Umur harus berupa angka.")
        return
    
    hasil = hitung_tinggi_badan_balita(jenis_kelamin, umur)
    if isinstance(hasil, str):
        print("Error:", hasil)
    else:
        print(f"Tinggi badan estimasi untuk balita {jenis_kelamin} umur {umur} tahum adalah {hasil} cm.")


if __name__ == "__main__":
    main()