import os
import requests

DATA_URL = "https://opendata-cosagis.opendata.arcgis.com/api/download/v1/items/754d5490121e44b8b6f3712934b24839/csv?layers=0"
OUTPUT_FILE = "311_All_Service_Calls.csv"

def download_data():
    if os.path.exists(OUTPUT_FILE):
        print(f"'{OUTPUT_FILE}' already exists. Skipping download.")
        return

    print(f"Downloading San Antonio 311 dataset from Open Data SA...")
    response = requests.get(DATA_URL, stream=True)
    response.raise_for_status()

    with open(OUTPUT_FILE, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    print(f"Download complete: {OUTPUT_FILE} ({os.path.getsize(OUTPUT_FILE) / (1024 * 1024):.2f} MB)")

if __name__ == "__main__":
    download_data()
