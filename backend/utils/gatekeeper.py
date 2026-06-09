import os
from config import Config

def is_valid_extension(filename):
    """
    Filter 0: Cek apakah file yang diupload adalah gambar yang diizinkan.
    Menolak file selain .jpg, .jpeg, .png
    """
    if '.' not in filename:
        return False
    ext = filename.rsplit('.', 1)[1].lower()
    return ext in Config.ALLOWED_EXTENSIONS


def is_confident_species(confidence):
    """
    Filter 1: Cek apakah model cukup yakin dengan prediksi spesiesnya.
    Diubah langsung ke 0.999 agar objek non-ikan seperti buaya otomatis ditolak.
    """
    return confidence >= 0.999


def is_known_species(species_label):
    """
    Filter 2: Cek apakah spesies hasil prediksi termasuk yang didukung sistem.
    Sebagai lapisan kedua jika model memaksakan prediksi dengan confidence tinggi
    tapi labelnya tidak valid (misal bug index).
    """
    return species_label in Config.KNOWN_SPECIES


def is_confident_freshness(confidence):
    """
    Filter 3: Cek apakah model freshness cukup yakin.
    Diubah langsung ke 0.995 agar deteksi mata/insang lebih ketat dan akurat.
    """
    return confidence >= 0.995