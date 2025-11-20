import streamlit as st
import pandas as pd
import pickle
from datetime import datetime
from ultralytics import YOLO
from PIL import Image
import numpy as np
import requests
from io import BytesIO
import os
import cv2

# ============================================================
# YOLO VEHICLE DETECTION SECTION (TOP)
# ============================================================

os.environ["ULTRALYTICS_CACHE_DIR"] = "/tmp"
os.environ["HF_HOME"] = "/tmp"
os.environ["TRANSFORMERS_CACHE"] = "/tmp"
os.environ["TORCH_HOME"] = "/tmp"

@st.cache_resource
def load_yolo_model():
    model = YOLO("src/best.onnx")
    return model

def predict_count(model, img, conf=0.4):
    results = model(img, conf=conf, verbose=False)
    boxes = results[0].boxes
    count = len(boxes)
    return count

def traffic_congestion_index(vehicle_count, lane_count, lane_capacity=10):
    if lane_count == 0:
        return 99
    D = vehicle_count / (lane_count * lane_capacity)
    TCI = 20 + 80 * (D / (1 + D))
    TCI = max(1, min(99, TCI))
    return round(TCI, 1)

def yolo_section():
    st.title("🚘 YOLOv8 Vehicle Counter via URL")

    model = load_yolo_model()

    confidence = st.slider('Confidence:', 0.0, 1.0, 0.4, 0.05)
    laneCount = st.slider('Jumlah Lajur:', 1, 5, 3, 1)
    url_input = st.text_input("Masukkan URL gambar kendaraan (jpg/jpeg/png):")

    if url_input:
        try:
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url_input, headers=headers, timeout=10)
            response.raise_for_status()

            img = Image.open(BytesIO(response.content)).convert("RGB")

            st.image(img, caption='Gambar dari URL', use_column_width=True)
            st.success("✅ Gambar berhasil diambil dari URL")

            if st.button("Predict"):
                count = predict_count(model, img, confidence)
                results = model.predict(source=img, imgsz=640, conf=confidence)
                result_image = results[0].plot(line_width=2)
                result_image = cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB)

                st.image(result_image, caption='Hasil Deteksi YOLO', use_column_width=True)
                st.write(f"## 🚗 Jumlah Kendaraan Terdeteksi: **{count}**")

                tci_value = traffic_congestion_index(count, laneCount)
                st.write(f"## 🚦 Traffic Congestion Index: **{tci_value}**")

                # 🔥 Store the TCI in Streamlit session_state
                st.session_state["traffic_index_from_yolo"] = tci_value
                st.success("📊 Nilai Traffic Congestion Index telah dikirim ke model regresi.")

        except Exception as e:
            st.error(f"Gagal memproses gambar: {e}")
    else:
        st.info("Silakan masukkan link gambar kendaraan untuk diprediksi.")
        st.info("Contoh link: https://awsimages.detik.net.id/visual/2022/04/26/sejumlah-kendaraan-berjalan-perlahan-saat-terjebak-macet-di-tol-dalam-kota-jakarta-selasa-2642022-cnbc-indonesiaandrean-kristi-3_169.jpeg?w=650o")


# ============================================================
#  REGRESSION MODEL SECTION (BOTTOM)
# ============================================================

@st.cache_resource
def load_regression_model():
    with open("src/model_akhir.pkl", "rb") as file:
        model_rf = pickle.load(file)
    return model_rf

def regression_section():
    st.title("🧠 Prediksi Keterlambatan Kedatangan")
    st.write("Masukkan detail perjalanan untuk memprediksi keterlambatan kedatangan (dalam menit).")

    # 🔥 Use YOLO’s traffic index if available
    default_tci = st.session_state.get("traffic_index_from_yolo", 68)

    with st.form("prediction_form"):
        col1, col2 = st.columns(2)

        with col1:
            transport_type = st.selectbox("Jenis Transportasi", ["Bus", "Train", "Tram"])
            origin_station = st.text_input("Stasiun Asal", "Station_12")
            destination_station = st.text_input("Stasiun Tujuan", "Station_30")
            actual_departure_delay_min = st.number_input("Keterlambatan Keberangkatan (menit)", min_value=0, value=8)
            temperature_C = st.number_input("Suhu (°C)", value=29.3)
            humidity_percent = st.number_input("Kelembaban (%)", value=76)
            event_attendance_est = st.number_input("Perkiraan Kehadiran Acara", value=250)

        with col2:
            # Auto-filled slider value from YOLO prediction
            traffic_congestion_index = st.slider("Traffic Congestion Index (1–99)", 1, 99, int(default_tci))
            holiday = st.selectbox("Hari Libur?", [0, 1])
            weekday = st.selectbox("Hari Kerja?", [0, 1])
            season = st.selectbox("Musim", ["Dry", "Wet"])
            datetime_input = st.text_input("Tanggal & Waktu (YYYY-MM-DD HH:MM:SS)", "2025-10-08 08:00:00")
            scheduled_duration_min = st.number_input("Durasi Terjadwal (menit)", min_value=0, value=50)

        submitted = st.form_submit_button("Prediksi")

    if submitted:
        try:
            datetime_value = pd.Timestamp(datetime_input)
        except Exception:
            st.error("⚠️ Format tanggal & waktu tidak valid. Gunakan format YYYY-MM-DD HH:MM:SS.")
            return

        data_input = pd.DataFrame([{
            'transport_type': transport_type,
            'origin_station': origin_station,
            'destination_station': destination_station,
            'actual_departure_delay_min': actual_departure_delay_min,
            'temperature_C': temperature_C,
            'humidity_percent': humidity_percent,
            'event_attendance_est': event_attendance_est,
            'traffic_congestion_index': traffic_congestion_index,
            'holiday': holiday,
            'weekday': weekday,
            'season': season,
            'datetime': datetime_value,
            'scheduled_duration_min': scheduled_duration_min
        }])

        # Match training categories
        data_input["transport_type"] = pd.Categorical(data_input["transport_type"], categories=["Bus", "Train", "Tram"])
        data_input["season"] = pd.Categorical(data_input["season"], categories=["Dry", "Wet"])
        data_input["holiday"] = pd.Categorical(data_input["holiday"], categories=[0, 1])
        data_input["weekday"] = pd.Categorical(data_input["weekday"], categories=[0, 1])
        data_input["origin_station"] = data_input["origin_station"].astype("category")
        data_input["destination_station"] = data_input["destination_station"].astype("category")

        model_rf = load_regression_model()

        try:
            prediction = model_rf.predict(data_input)
            st.success(f"🎯 **Perkiraan Keterlambatan Kedatangan:** {round(prediction[0], 2)} menit")
        except Exception as e:
            st.error(f"❌ Terjadi kesalahan saat prediksi: {e}")

# ============================================================
# MAIN APP
# ============================================================

def run():
    yolo_section()
    st.divider()
    regression_section()

if __name__ == "__main__":
    run()
