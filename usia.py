import streamlit as st
from datetime import datetime, timedelta

def hitung_usia(tanggal_lahir, tanggal_opsi=None):
    # Jika tanggal_opsi tidak diberikan, gunakan tanggal hari ini
    if tanggal_opsi is None:
        tanggal_opsi = datetime.now().date()
    
    # Validasi input tanggal
    if tanggal_lahir > tanggal_opsi:
        raise ValueError("Tanggal lahir tidak boleh lebih besar dari tanggal perhitungan")
    
    # Konversi ke datetime
    tanggal_lahir_dt = datetime.combine(tanggal_lahir, datetime.min.time())
    tanggal_opsi_dt = datetime.combine(tanggal_opsi, datetime.min.time())

    # Hitung usia
    delta = tanggal_opsi_dt - tanggal_lahir_dt
    
    # Hitung tahun, bulan, hari dengan metode yang lebih presisi
    tahun = tanggal_opsi_dt.year - tanggal_lahir_dt.year
    bulan = tanggal_opsi_dt.month - tanggal_lahir_dt.month
    hari = tanggal_opsi_dt.day - tanggal_lahir_dt.day

    # Penyesuaian bulan dan hari
    if hari < 0:
        bulan -= 1
        # Dapatkan jumlah hari di bulan sebelumnya
        hari += (tanggal_opsi_dt.replace(day=1) - timedelta(days=1)).day

    if bulan < 0:
        tahun -= 1
        bulan += 12

    return tahun, bulan, hari, delta.days

# Contoh penggunaan
def main():
    try:
        # Input tanggal lahir
        tanggal_lahir_input = input("Masukkan tanggal lahir balita (format: YYYY-MM-DD): ").strip()
        tanggal_lahir = datetime.strptime(tanggal_lahir_input, "%Y-%m-%d").date()
        
        # Input tanggal opsi (opsional)
        tanggal_opsi_input = input("Masukkan tanggal perhitungan (format: YYYY-MM-DD) atau tekan Enter untuk hari ini: ").strip()
        if tanggal_opsi_input:
            tanggal_opsi = datetime.strptime(tanggal_opsi_input, "%Y-%m-%d").date()
        else:
            tanggal_opsi = datetime.now().date()
        
        # Hitung usia
        tahun, bulan, hari, total_hari = hitung_usia(tanggal_lahir, tanggal_opsi)
        
        # Cetak hasil
        print(f"Usia balita adalah {tahun} tahun, {bulan} bulan, dan {hari} hari.")
        print(f"Total hari: {total_hari} hari")
    
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# Jalankan fungsi main jika script dieksekusi langsung
if __name__ == "__main__":
    main()
