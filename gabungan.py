import streamlit as st
from datetime import datetime, timedelta

def hitung_bbi_balita(usia, satuan='tahun'):
    # Konversi ke tahun jika input dalam bulan
    if satuan == 'bulan':
        usia_tahun = usia / 12
    else:
        usia_tahun = usia
    
    # Perhitungan BBI berdasarkan usia
    if usia_tahun <= 1:
        # Untuk balita di bawah 1 tahun
        usia_bulan = usia_tahun * 12
        bbi = (usia_bulan / 2) + 4
    else:
        # Untuk balita di atas 1 tahun
        bbi = (usia_tahun * 2) + 8
    
    return round(bbi, 2)

def hitung_tinggi_badan_balita(jenis_kelamin, umur):    
    # Data rata-rata tinggi badan berdasarkan WHO (dalam cm)
    tinggi_laki_laki = {
        0: "Umur harus antara 1 hingga 5 tahun.", 1: 54.7, 2: 58.4, 3: 61.4, 4: 63.9, 5: 65.9
    }
    
    tinggi_perempuan = {
        0: "Umur harus antara 1 hingga 5 tahun.", 1: 53.7, 2: 57.1, 3: 59.8, 4: 62.1, 5: 64.0
    }
    
    # Pilih data sesuai jenis kelamin
    if jenis_kelamin.lower() == "laki-laki":
        data_tinggi = tinggi_laki_laki
    elif jenis_kelamin.lower() == "perempuan":
        data_tinggi = tinggi_perempuan
    else:
        return "Jenis kelamin tidak valid. Gunakan 'laki-laki' atau 'perempuan'."
    
    return data_tinggi.get(umur, None)

def main():
    # Set page configuration
    st.set_page_config(page_title="Posyandu Balita", page_icon=":baby:", layout="wide")

     # CSS untuk styling
    st.markdown("""
        <style>
        .header {
            text-align: center;
            color: #4CAF50;
            font-size: 2.5em;
            margin-bottom: 20px;
        }
        .subheader {
            color: #2196F3;
        }
        .info {
            background-color: #f9f9f9;
            padding: 10px;
            border-radius: 5px;
        }
        .button {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
        }
        .button:hover {
            background-color: #45a049;
        }
        </style>
    """, unsafe_allow_html=True)

    # Judul
    st.title("📊 Informasi Kesehatan Balita Posyandu")

    # Sidebar menu
    menu = st.sidebar.selectbox("Pilih Menu", 
        ["","Usia Balita", "Berat Badan Ideal", "Tinggi Badan Balita"], 
        index=0
    )
    try:
        st.image("img/gbmr.balita.jpg")
    except FileNotFoundError:
        st.warning("Gambar tidak ditemukan")

    st.markdown("Aplikasi ini dirancang untuk membantu Anda memantau perkembangan si kecil. Untuk mendapatkan hasil yang akurat, pastikan data yang Anda masukkan sudah benar.")
    st.info("Adapun data sesuai masukan WHO bahwa Usia balita 1-5 tahun")

    # Konten berdasarkan menu
    if menu == "Usia Balita":
        hitung_usia()
    elif menu == "Berat Badan Ideal":
        hitung_bb()
    elif menu == "Tinggi Badan Balita":
        hitung_tinggi_badan_balita_ui()

def hitung_usia():
    st.subheader("🎂 Kalkulator Usia Balita")
    
    # Kolom input
    col1, col2 = st.columns(2)
    
    with col1:
        # Input tanggal lahir
        tanggal_lahir = st.date_input("Tanggal Lahir Balita")
    
    with col2:
        # Input tanggal perhitungan (default hari ini)
        tanggal_opsi = st.date_input("Tanggal Perhitungan", value=datetime.now().date())
    
    # Tombol hitung
    if st.button("Hitung Usia"):
        # Validasi input tanggal
        if tanggal_lahir > tanggal_opsi:
            st.error("Tanggal lahir tidak boleh lebih besar dari tanggal perhitungan")
            return
        
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

        # Tampilkan hasil
        st.success(f"Usia balita adalah {tahun} tahun, {bulan} bulan, dan {hari} hari.")
        st.info(f"Total hari: {delta.days} hari")

def hitung_bb():
    st.subheader("⚖️ Berat Badan Ideal Balita")
    
    # Buat fungsi kolom input
    col1, col2 = st.columns(2)
    
    with col1:
        # Pilih satuan usia
        satuan = st.selectbox("Satuan Usia", ["tahun", "bulan"])
        # # Input usia balita
        # usia = st.slider("Masukkan Usia Balita", min_value=1, max_value=5, step=1)
    
    with col2:
        if satuan == "tahun":
            usia = st.slider("Masukkan usia balita (dalam tahun):", min_value=1, max_value=5)
        elif satuan == "bulan":
            usia = st.slider("Masukkan usia balita (dalam bulan):", min_value=1, max_value=12)
    
    # Tombol hitung
    if st.button("Hitung Berat Badan Ideal"):
        try:
            # # validasi usia yang dimasukan
            # if satuan == 'tahun' and (usia >= 5 and usia <= 1):
            #     st.error("Usia balita harus berada dalam rentang 1 tahun hingga 5 tahun. Silakan periksa kembali input Anda.")
            #     return
            # if satuan == 'bulan' and usia >= 12:
            #     st.error("Usia balita harus berada dalam rentang 1 bulan hingga 12 bulan. Silakan periksa kembali input Anda.")
            #     return
            # Hitung BBI
            bbi = hitung_bbi_balita(usia, satuan)
            
            # Tampilkan hasil
            st.success(f"Berat Badan Ideal ({usia}) balita: {bbi} kg")
            
            if usia < 1 or satuan == 'bulan':
                st.info("Rumus: BBI = (usia dalam bulan / 2) + 4")
            else:
                st.info("Rumus: BBI = (usia dalam tahun x 2) + 8")
        
        except Exception as e:
            st.error(f"Terjadi kesalahan: {e}")

def hitung_tinggi_badan_balita_ui():
    st.subheader("📏 Estimasi Tinggi Badan Balita")
    
    # Kolom input
    col1, col2 = st.columns(2)
    
    with col1:
        # Input jenis kelamin
        jenis_kelamin = st.selectbox("Jenis Kelamin", ["laki-laki", "perempuan"])
    
    with col2:
        # Input umur
        umur = st.number_input("Umur (tahun)", min_value=0, max_value=5, step=1)
    
    # Tombol hitung
    if st.button("Hitung Tinggi Badan"):
        # Hitung tinggi badan
        hasil = hitung_tinggi_badan_balita(jenis_kelamin, umur)
        
        if isinstance(hasil, float):
            st.success(f"Estimasi tinggi badan balita {jenis_kelamin} umur {umur} tahun: {hasil} cm")
        else:
            st.error(hasil)

if __name__ == "__main__":
    main()