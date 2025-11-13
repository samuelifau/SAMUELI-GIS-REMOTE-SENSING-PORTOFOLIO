<p align="center">
  <img src="https://img.shields.io/badge/Remote%20Sensing-NDVI-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge">
  <img src="https://img.shields.io/badge/Rasterio-GeoTIFF-orange?style=for-the-badge">
</p>

# 🌿 **VegetationMapping — NDVI Calculation Project** 🌿
### *GIS & Remote Sensing Mini Project using Python (Rasterio, NumPy, Matplotlib)*

---
<img width="1052" height="770" alt="image" src="https://github.com/user-attachments/assets/67ffc002-7791-486f-b70c-c4203b5e6e0f" />

📌 Project Summary

This project is a simple demonstration of calculating NDVI (Normalized Difference Vegetation Index) using a small EuroSAT/Sentinel-2 sample image.
The output includes an NDVI GeoTIFF raster and a colorized NDVI map.

The main goals of this project:

Learn basic raster processing in Remote Sensing

Generate NDVI from Red (B04) and NIR (B08) bands

Build a clean GIS/Remote Sensing portfolio project for recruiters

The repository uses lightweight sample data, making it safe for GitHub uploads.

🚀 Key Features

Read satellite raster data (TIFF)

NDVI computation using:

𝑁
𝐷
𝑉
𝐼
=
𝑁
𝐼
𝑅
−
𝑅
𝐸
𝐷
𝑁
𝐼
𝑅
+
𝑅
𝐸
𝐷
NDVI=
NIR+RED
NIR−RED
	​


Save NDVI result as GeoTIFF

Generate NDVI visualization with Matplotlib

Modular, clean, and extendable project structure

📁 Folder Structure
VegetationMapping/
│
├── data/
│   └── sample_eurosat.tif        # Sample TIFF for NDVI
│
├── scripts/
│   └── ndvi_calculation.py       # Main NDVI script
│
├── output/
│   ├── ndvi_result.tif           # NDVI raster output
│   └── ndvi_map.png              # NDVI visualization
│
├── docs/
│   └── images/
│       └── ndvi_preview.png      # NDVI preview image
│
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git ignore rules
├── LICENSE                       # MIT License
└── README.md                     # Documentation

🧪 NDVI Example Output
File	Description
output/ndvi_result.tif	NDVI GeoTIFF raster
output/ndvi_map.png	Colorized NDVI visualization
🛠 Technologies Used
Library	Purpose
Rasterio	Read/write raster data
NumPy	NDVI computation
Matplotlib	Visualization
Python 3.x	Main language
📥 Dataset Sources

EuroSAT Dataset
🔗 https://github.com/phelber/eurosat

Sentinel-2 Data (ESA)
🔗 https://earth.esa.int/eogateway/missions/sentinel-2

Only a small sample TIFF is included to keep the repo lightweight.

🧩 Installation & Usage
1️⃣ Clone This Repository
git clone https://github.com/samuelifau/SAMUELI-GIS-REMOTE-SENSING-PORTOFOLIO.git
cd VegetationMapping

2️⃣ Create a Virtual Environment
python -m venv venv

3️⃣ Activate Virtual Environment (Windows)
.\venv\Scripts\activate

4️⃣ Install Dependencies
pip install -r requirements.txt

5️⃣ Run NDVI Script
python scripts/ndvi_calculation.py


Generated outputs:

output/ndvi_result.tif
output/ndvi_map.png

🧾 How the Script Works
with rasterio.open(DATA_FP) as src:
    img = src.read()
    red = img[2].astype(float)
    nir = img[3].astype(float)

    ndvi = (nir - red) / (nir + red + 1e-10)


The script:

Reads the TIFF

Extracts Red & NIR bands

Computes NDVI

Saves GeoTIFF & image visualization

🎯 Project Purpose

This project is part of the GIS & Remote Sensing Portfolio Series, demonstrating:

Raster data understanding

Satellite image processing (Sentinel-2 / EuroSAT)

Python environment management

NDVI map generation

Professional repository structure

Suitable for:

✔ GIS students
✔ Remote Sensing job applicants
✔ Geospatial data analysts

📜 License

This project is licensed under the MIT License.
Free to use for learning and research.

🙋 About Me

Samueli Fau
GIS & Remote Sensing Enthusiast

📧 Email: samuelifau@student.untan.ac.id

🌐 GitHub: https://github.com/samuelifau

If you find this project useful, please ⭐ the repository!

⭐ Thank You for Visiting This Project!

⭐ Terima kasih sudah melihat project ini!


