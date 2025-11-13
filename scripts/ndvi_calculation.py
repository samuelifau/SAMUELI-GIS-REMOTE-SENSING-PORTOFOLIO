MODE = "single_file"   # atau "two_files" jika kamu punya dua file
SINGLE_FP = "data/sample_eurosat.tif"
RED_BAND = 4   # ubah ke 3/4/8 sesuai output check_tif.py
NIR_BAND = 8   # ubah sesuai

# scripts/ndvi_calculation.py
import os
import numpy as np
import rasterio
import matplotlib.pyplot as plt

# ======= CONFIG =======
# Jika kamu memiliki 2 file terpisah gunakan mode "two_files":
#   - data/sentinel2_B04.tif  (red)
#   - data/sentinel2_B08.tif  (nir)
# Jika kamu hanya punya satu multiband file (sample_eurosat.tif), gunakan mode "single_file".
MODE = "single_file"   # "single_file" atau "two_files"

# path untuk single-file (multiband)
SINGLE_FP = "data/sample_eurosat.tif"

# paths untuk two-files mode
RED_FP  = "data/sentinel2_B04.tif"
NIR_FP  = "data/sentinel2_B08.tif"

# Jika single_file: atur index band (1-based index)
# Contoh: jika band 4 = NIR dan band 3 = RED: set RED_BAND=3, NIR_BAND=4
RED_BAND = 3
NIR_BAND = 4

OUTPUT_TIF = "output/ndvi_result.tif"
OUTPUT_PNG = "output/ndvi_map.png"
# ======================

def calc_ndvi_from_arrays(red_arr, nir_arr):
    # convert to float and compute NDVI
    red = red_arr.astype('float32')
    nir = nir_arr.astype('float32')
    ndvi = (nir - red) / (nir + red + 1e-10)
    return ndvi

def main():
    os.makedirs("output", exist_ok=True)

    if MODE == "two_files":
        # open two single-band files
        with rasterio.open(RED_FP) as rsrc, rasterio.open(NIR_FP) as nsrc:
            red = rsrc.read(1)
            nir = nsrc.read(1)
            profile = nsrc.profile.copy()
            profile.update(count=1, dtype=rasterio.float32)
    else:
        # single multiband file
        with rasterio.open(SINGLE_FP) as src:
            # read specified bands (1-based)
            red = src.read(RED_BAND)
            nir = src.read(NIR_BAND)
            profile = src.profile.copy()
            profile.update(count=1, dtype=rasterio.float32)

    ndvi = calc_ndvi_from_arrays(red, nir)

    # Save NDVI GeoTIFF
    with rasterio.open(OUTPUT_TIF, 'w', **profile) as dst:
        dst.write(ndvi.astype(rasterio.float32), 1)

    # Save simple PNG image for quick preview
    plt.figure(figsize=(8,8))
    plt.imshow(ndvi, cmap='RdYlGn', vmin=-1, vmax=1)
    plt.title("NDVI")
    plt.colorbar(label="NDVI")
    plt.axis('off')
    plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight')
    plt.close()

    print("Saved NDVI GeoTIFF:", os.path.abspath(OUTPUT_TIF))
    print("Saved PNG preview:", os.path.abspath(OUTPUT_PNG))

if __name__ == "__main__":
    main()
