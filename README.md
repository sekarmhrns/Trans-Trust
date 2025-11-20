<h1 align="center">TransTrust:
Predicts trip delays,
Monitors traffic congestion
</h1>

<p align="center">
  <a href="https://huggingface.co/spaces/VagueV12/TransTrust">
    <img alt="Deploy on Hugging Face" src="https://img.shields.io/badge/Deploy-HuggingFace-blue?logo=huggingface">
  </a>
</p>


## Initiative

<div align="justify">

Trusted-Transports adalah platform transportasi cerdas yang dapat diandalkan untuk memprediksi keterlambatan transum dan memantau kemacetan lalu lintas secara real-time untuk mengoptimalkan perencanaan mobilitas publik. Dengan menggabungkan model prediksi keterlambatan berbasis machine learning dan sistem computer vision yang menganalisis rekaman jalan secara langsung, platform ini membantu penumpang maupun pengelola transportasi dalam mengambil keputusan perjalanan yang cerdas dan berbasis data untuk kebutuhan sehari-hari.

## Background

<div align="justify">

Kemacetan dan keterlambatan transportasi umum menyebabkan waktu tempuh tidak pasti, aktivitas terganggu, dan produktivitas menurun. Masalah ini sering dipicu oleh cuaca, jam sibuk, pola hari, serta kegiatan besar yang meningkatkan kepadatan lalu lintas.

Menurut Sidjabat (2015), akar kemacetan di kota besar seperti Jakarta berasal dari pertumbuhan kendaraan pribadi yang jauh melampaui kapasitas jalan dan rendahnya kualitas angkutan umum. Data menunjukkan panjang jalan hanya bertambah sekitar 1% per tahun, sementara jumlah kendaraan meningkat hingga 11%, dengan 98% di antaranya kendaraan pribadi. Kondisi ini memperparah kemacetan dan menurunkan efisiensi sistem transportasi.

Dampaknya tidak hanya pada waktu perjalanan, tetapi juga ekonomi — kerugian akibat kemacetan di Jakarta diperkirakan mencapai Rp8,3 triliun per tahun. Karena itu, dibutuhkan solusi berbasis teknologi seperti prediksi keterlambatan dan pemantauan lalu lintas real-time untuk mendukung mobilitas publik yang lebih efisien dan adaptif terhadap kondisi jalan.

## Problem statement

<div align="justify">

Proyek ini hadir untuk menjawab dua kebutuhan utama: (1) memberikan prediksi keterlambatan—apakah sebuah perjalanan berpotensi terlambat dan berapa menit perkiraan keterlambatannya—serta (2) menyediakan wawasan kondisi lalu lintas secara kontekstual (dipengaruhi cuaca, hari, dan event). Dengan memanfaatkan data historis perjalanan, informasi cuaca, kalender acara, serta sinyal operasional, platform ini membantu pengguna merencanakan keberangkatan dengan lebih akurat, sekaligus memberi operator dasar pengambilan keputusan yang lebih baik untuk penjadwalan dan mitigasi kemacetan.

## Objective

<div align="justify">

- Tujuan utama proyek Trusted-Transports adalah membangun sistem transportasi cerdas yang mampu:

   - Memprediksi keterlambatan perjalanan secara akurat menggunakan model machine learning    berbasis data historis, kondisi cuaca, pola waktu (jam sibuk, weekday/weekend), dan event publik.

  - Menganalisis kondisi lalu lintas secara real-time melalui computer vision untuk mendeteksi tingkat kemacetan, kepadatan kendaraan, serta anomali di jalan.

  - Menyediakan insight visual interaktif bagi pengguna dan operator transportasi untuk mendukung pengambilan keputusan yang cepat dan berbasis data.

  - Mengoptimalkan perencanaan rute dan jadwal transportasi, sehingga meningkatkan ketepatan waktu perjalanan dan efisiensi operasional armada.

- Dengan demikian, proyek ini bertujuan untuk menciptakan ekosistem mobilitas yang lebih terencana, efisien, dan responsif terhadap dinamika lalu lintas perkotaan.

## Dataset

<div align="justify">

- **Sumber:** [Top-View Vehicle Detection Image Dataset for YOLOv8](https://www.kaggle.com/datasets/farzadnekouei/top-view-vehicle-detection-image-dataset)  
- **Sumber:** [📊 Public Transport Delays with Weather & Events](https://www.kaggle.com/datasets/khushikyad001/public-transport-delays-with-weather-and-events)
  **Penggunaan dalam proyek ini:** Kami mengunduh pada bagian train/ dan valid/ dari dataset dan menggunakannya sebagai data utama untuk proses pelatihan dan validasi model. **raw_data** (≈ **2k**).

- **Classes:**  
  `Deteksi`


## Referensi

<div align="justify">

Cut Azka, N., & Rahman, F. (2023). Implementasi sistem transportasi cerdas di Indonesia. Prosiding Seminar Nasional Teknologi Terapan, 2(1), 15–22.
https://www.researchgate.net/publication/388919496_Implementasi_Sistem_Transportasi_Cerdas

Gaikindo. (2022, September 14). Sistem lalu lintas cerdas pendukung konektivitas transportasi. Gaikindo News.
https://www.gaikindo.or.id/sistem-lalulintas-cerdas-pendukung-konektivitas-transportasi/

Rachman, D., & Pratama, B. (2020). Analisis risiko dan ketidakpastian pada prediksi arus lalu lintas menggunakan data historis. Jurnal Teknik dan Aplikasi Transportasi, 8(1), 45–53.
https://ejurnalmalahayati.ac.id/index.php/teknologi/article/download/16581/pdf

Sidjabat, S. (2015). Revitalisasi Angkutan Umum untuk Mengurangi Kemacetan Jakarta.
Jurnal Manajemen Bisnis Transportasi dan Logistik, 1(2), 309–330.
Jakarta: STMT Trisakti.
