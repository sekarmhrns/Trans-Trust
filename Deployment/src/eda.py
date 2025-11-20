#imports
import streamlit as st
import pandas as pd
from PIL import Image

def run():
    # Judul
    st.title("TransTrust: Prediksi Keterlambatan Perjalanan, Pantau Kemacetan Secara Real-Time")

    # Load Gambar
    gambar_header = Image.open('src/TransNusa.jpg')
    st.image(gambar_header)

    st.write('# Latar Belakang')
    st.write('''Kemacetan dan keterlambatan transportasi umum membuat waktu tempuh tidak pasti, agenda harian terganggu, dan produktivitas pengguna menurun. 

Kerugian akibat kemacetan lalu lintas di DKI Jakarta bisa mencapai angka Rp.8,3 triliun, yang terdiri dari kerugian biaya operasi kendaraan Rp. 3 triliun, kerugian waktu
Rp. 2,5 triliun, serta kerugian dampak kesehatan Rp. 2,8 triliun(Sidjabat, 2015).

Kondisi ini kerap dipicu oleh berbagai macam faktor yang menambah kepadatan. Di sisi operator, keterlambatan berulang mengacaukan penjadwalan armada dan menurunkan kualitas layanan.

''')

    # Load dataset
    st.write("# Dataset 1")
    st.write('''Dataset ini berisi informasi tentang berbagai penundaan transportasi umum, termasuk waktu penundaan, durasi, dan Situasi. 
             Data yang dipakai dari Kaggle bisa ditemukan [disini](https://www.kaggle.com/datasets/khushikyad001/public-transport-delays-with-weather-and-events).''')
    
    url = "src/public_transport_delays.csv"  
    df = pd.read_csv(url)
    st.dataframe(df)

    st.write("# Dataset 2")
    st.write(''' Dataset ini berisi adalah kumpulan 626 gambar yang dikurasi dan dirancang untuk melatih dan mengevaluasi model deteksi objek berbasis YOLO.
             Setiap gambar memberikan perspektif atas-bawah dari berbagai kendaraan termasuk mobil, truk, dan bus. 
             sehingga ideal untuk penelitian dan pengembangan dalam pemantauan lalu lintas, mengemudi otonom, dan perencanaan kota.
             Data yang dipakai dari Kaggle bisa ditemukan [disini](https://www.kaggle.com/datasets/farzadnekouei/top-view-vehicle-detection-image-dataset).''')

    gambar_header2 = Image.open('src/car.jpg')
    st.image(gambar_header2)

    # =====================
    # On-time Vs Delayed
    # =====================
    st.write("## Distribusi Data On-time dan Delay")

    gambar_header3 = Image.open('src/1.jpg')
    st.image(gambar_header3)

    st.write('''
    **Insights**: Berdasarkan 2000 perjalanan yang dianalisa dalam dataset, keterlambatan terjadi pada 1499 perjalanan. 
             Sekitar ~75% dari total perjalanan mengalami keterlambatan, angka ini sangat tinggi. 
Dampak keterlambatan ini seringnya bisa mengakibatkan over-capacity atau kepadatan pada transportasi umum lain, 
             karena pengguna cenderung akan mengganti moda transportasi [tirto.id](https://tirto.id/kepadatan-krl-keterlambatan-transjakarta-warnai-hut-ke-80-tni-hiZM)''') 

    # =====================
    # Distribusi Jam Delay Kedatangan
    # =====================
    st.write("## Distribusi Jam Delay Kedatangan")

    gambar_header4 = Image.open('src/2.jpg')
    st.image(gambar_header4)

    st.write('''
    **Insights**: Sebaran keterlambatan terutama di rentang 5–15 menit dengan puncak sekitar 9–13 menit, disertai sedikit nilai ≤0 menit (indikasi berangkat tepat/lebih awal) dan ekor kanan hingga ~19 menit untuk kasus terlambat berat; 
             variabilitas yang lebar ini menandakan faktor konteks (jam sibuk, weekday/weekend) sangat berpengaruh.''')
    
    # =====================
    # Jam Keterlambatan Terbanyak
    # =====================
    st.write("## Jam Keterlambatan Terbanyak")

    gambar_header5 = Image.open('src/3.jpg')
    st.image(gambar_header5)

    st.write('''
    **Insights**: Keterlambatan yang cukup tinggi kerap terjadi di jam 09.00-10.00 pagi dan jam 13.00-14.00 siang. 
             Hal ini perlu diperhatikan karena berdasarkan data Ditlantas, 54% kemacetan di Jakarta terjadi pada jam sibuk, yakni pukul 06.00-10.00 dan 15.00-20.00(BBC,2022). 
             Keterlambatan pada jam tersebut bisa sangat berdampak dan merugikan untuk pengguna transportasi umum khususnya kelas pekerja.''')

    # =====================
    # Distribusi Jumlah Kendaraan Per Gambar
    # =====================
    st.write("## Distribusi Jumlah Kendaraan Per Gambar")

    gambar_header6 = Image.open('src/4.jpg')
    st.image(gambar_header6)

    st.write('''
    **Insights**: Sebagian besar gambar dalam dataset berisi sedikit kendaraan, terutama di kisaran 1–5 kendaraan per gambar. 
             Frekuensi kemudian menurun seiring bertambahnya jumlah kendaraan, dan hanya sedikit gambar yang memiliki lebih dari 25 kendaraan. 
             Pola ini menunjukkan bahwa mayoritas data menggambarkan kondisi lalu lintas yang relatif lancar, sementara kondisi padat hanya muncul pada sebagian kecil gambar''')
    
    # =====================
    # Heatmap lokasi kendaraan dalam Frame
    # =====================
    st.write("## Heatmap lokasi kendaraan dalam Frame")

    gambar_header7 = Image.open('src/5.jpg')
    st.image(gambar_header7)

    st.write('''
    **Insights**: Sebaran kendaraan pada frame menunjukkan konsentrasi tertinggi ada di area tengah frame, ditunjukkan oleh warna kuning-putih. 
             Area tersebut merepresentasikan jalur utama jalan tempat kendaraan paling sering muncul. 
             Sementara itu, area pinggir frame dengan warna merah gelap-hitam mempresentasikan bahwa kendaraan jarang muncul di area tersebut. ''')

if __name__ == "__main__":
    run()