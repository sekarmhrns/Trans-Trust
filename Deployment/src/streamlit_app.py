import streamlit as st
import eda, predict

# ===========================
# PAGE CONFIGURATION
# ===========================
st.set_page_config(
    page_title='TransTrust: Traffic & Delay Prediction',
    layout='centered'
)

# ===========================
# SIDEBAR
# ===========================
with st.sidebar:
    st.write("# Page Navigation")
    option = st.selectbox("Select Page", ["EDA", "Model"])

    st.write("---")
    st.write("### About")
    st.write("""
    **TransTrust** Adalah merupakan model predictor yang:
    - Mendeteksi kendaraan dari gambar tampak atas menggunakan **YOLOv8**
    - Menghitung **Indeks Kemacetan Lalu Lintas**
    - Memprediksi **waktu keterlambatan transportasi umum**
    """)

# ===========================
# PAGE ROUTING
# ===========================
if option == "EDA":
    eda.run()
else:
    predict.run()
