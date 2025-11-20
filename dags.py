"""
==========================================
Final Project 

Program Ini dibuat untuk melakukan ETL pada dataset guna menghasilkan wawasan
untuk membantu bisnis mengoptimalkan operasi, meningkatkan kepuasan pelanggan, dan mendorong pertumbuhan.

==========================================
"""

import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from airflow import DAG
from elasticsearch import Elasticsearch
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator

"""
import untuk menjalankan DAG:

- pandas untuk menangani dataframes
- datetime untuk menangani tanggal dan waktu
- sqlalchemy untuk menghubungkan ke PostgreSQL
- airflow untuk membuat DAG
- elasticsearch untuk menghubungkan ke Elasticsearch
- airflow.decorators untuk membuat tugas
- airflow.operators.empty untuk membuat tugas kosong

"""



default_args = {
    'owner': 'vitto',
    'start_date': datetime(2025, 5, 10)
}

"""
- owner : pemilik DAG
- start_date : tanggal mulai DAG dijalankan

"""

with DAG(
    'PublicTransportDataset',
    description='ETL Public Transport Delays dataset: PostgreSQL -> Preprocessing -> Elasticsearch',
    schedule_interval='10-30/10 9 * * SAT',
    default_args=default_args,
    catchup=False
) as dag:
    """
    -DagID: identifier unik untuk DAG, diatur ke 'PublicTransportDataset'
    -description: deskripsi tujuan DAG. 
    -Schedule Interval: berjalan setiap 10 menit antara 09:10 dan 09:30 setiap hari Sabtu.
    -Catchup: False untuk tidak melakukan backfilling pada run sebelumnya.

    """

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')
    """

    start dan end adalah tugas kosong yang berfungsi sebagai penanda untuk awal dan akhir DAG.

    """

    @task()
    def fetch_from_postgres():
        database = "airflow"
        username = "airflow"
        password = "airflow"
        host = "postgres"

        postgres_url = f"postgresql+psycopg2://{username}:{password}@{host}/{database}"
        engine = create_engine(postgres_url)
        conn = engine.connect()

        # Load data CSV ke postgres
        df = pd.read_csv(
            '/opt/airflow/data/public_transport_delays.csv',
            encoding='latin1'
        )

        # bersihkan nama kolom
        df.columns = [c.strip().replace(" ", "_").lower() for c in df.columns]

        # masukkan ke tabel postgres
        df.to_sql('table_finalproject', conn, index=False, if_exists='replace')

        print("Success getting data from Postgres")
        return True

    @task()
    def data_preprocessing():
        df = pd.read_csv(
            '/opt/airflow/data/public_transport_delays.csv',
            encoding='latin1'
        )

        # bersihkan nama kolom
        df.columns = [c.strip().replace(" ", "_").lower() for c in df.columns]

        # Tangani nilai numerik yang hilang
        df.fillna(df.mean(numeric_only=True), inplace=True)

        # jatuhkan baris duplikat
        df.drop_duplicates(inplace=True)

        # jadikan kolom date ke format DATE
        df['date'] = pd.to_datetime(df['date'], errors='coerce').dt.date

        # jadikan time relasi kolom ke format TIME
        time_cols = ['time', 'scheduled_departure', 'scheduled_arrival']
        for col in time_cols:
            df[col] = pd.to_datetime(df[col], format='%H:%M:%S', errors='coerce').dt.time

        # Save data yang sudah dibersihkan ke CSV baru
        df.to_csv('/opt/airflow/data/public_transport_delays_cleaned.csv', index=False)
        print(" Success data preprocessing")
        return True

    @task()
    def post_to_elasticsearch():
        es = Elasticsearch("http://elasticsearch:9200")
        df = pd.read_csv('/opt/airflow/data/public_transport_delays_cleaned.csv')

        for i, row in df.iterrows():
            doc = row.to_dict()
            es.index(index="public_transport_data", id=i+1, body=doc)

        print(" Success Loading to Elasticsearch")
        return True

    # DAG order
    start >> fetch_from_postgres() >> data_preprocessing() >> post_to_elasticsearch() >> end
    """
    Dag ordernya, dari start to finish.
    """
