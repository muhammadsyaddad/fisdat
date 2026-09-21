import numpy as np
import pandas as pd

# Soal 1: CsCl (10 Puncak Pertama)
DATASET_SOAL_1 = {
    "material": "CsCl",
    "lambda": 1.5405,  # CuKa1
    "data_puncak_1": [
        {"2theta": 21.550, "h": 1, "k": 0, "l": 0},
        {"2theta": 30.622, "h": 1, "k": 1, "l": 0},
        {"2theta": 37.766, "h": 1, "k": 1, "l": 1},
        {"2theta": 43.869, "h": 2, "k": 0, "l": 0},
        {"2theta": 49.380, "h": 2, "k": 1, "l": 0},
        {"2theta": 54.473, "h": 2, "k": 1, "l": 1},
        {"2theta": 63.829, "h": 2, "k": 2, "l": 0},
        {"2theta": 68.193, "h": 3, "k": 0, "l": 0},
        {"2theta": 72.411, "h": 3, "k": 1, "l": 0},
        {"2theta": 76.584, "h": 3, "k": 1, "l": 1},
    ],
}

# Soal 2: Al3Ti5O2 (12 Puncak - Semua Data)
DATASET_SOAL_2 = {
    "material": "Al3Ti5O2",
    "lambda": 1.5418,  # CuKa
    "data_puncak_2": [
        {"2theta": 22.451, "h": 1, "k": 1, "l": 1},
        {"2theta": 29.086, "h": 2, "k": 1, "l": 0},
        {"2theta": 39.344, "h": 3, "k": 0, "l": 0},
        {"2theta": 41.418, "h": 3, "k": 1, "l": 0},
        {"2theta": 43.508, "h": 3, "k": 1, "l": 1},
        {"2theta": 49.481, "h": 3, "k": 2, "l": 1},
        {"2theta": 56.451, "h": 3, "k": 3, "l": 0},
        {"2theta": 59.949, "h": 4, "k": 2, "l": 0},
        {"2theta": 61.579, "h": 4, "k": 2, "l": 1},
        {"2theta": 63.211, "h": 3, "k": 3, "l": 2},
        {"2theta": 67.865, "h": 4, "k": 3, "l": 0},
        {"2theta": 69.410, "h": 5, "k": 1, "l": 0},
    ],
}

# Soal 3: Ba0.5Sr0.5TiO3 (15 Puncak Pertama)
DATASET_SOAL_3 = {
    "material": "Ba0.5Sr0.5TiO3",
    "lambda": 1.5405981,  # CuKa1
    "data_puncak_3": [
        {"2theta": 22.494, "h": 1, "k": 0, "l": 0},
        {"2theta": 32.032, "h": 1, "k": 1, "l": 0},
        {"2theta": 39.498, "h": 1, "k": 1, "l": 1},
        {"2theta": 45.944, "h": 2, "k": 0, "l": 0},
        {"2theta": 51.755, "h": 2, "k": 1, "l": 0},
        {"2theta": 57.114, "h": 2, "k": 1, "l": 1},
        {"2theta": 67.011, "h": 2, "k": 2, "l": 0},
        {"2theta": 71.674, "h": 3, "k": 0, "l": 0},
        {"2theta": 76.225, "h": 3, "k": 1, "l": 0},
        {"2theta": 80.679, "h": 3, "k": 1, "l": 1},
        {"2theta": 85.052, "h": 2, "k": 2, "l": 2},
        {"2theta": 89.459, "h": 3, "k": 2, "l": 0},
        {"2theta": 93.808, "h": 3, "k": 2, "l": 1},
        {"2theta": 102.63, "h": 4, "k": 0, "l": 0},
        {"2theta": 107.13, "h": 4, "k": 1, "l": 0},
    ],
}

data_puncak_1 = DATASET_SOAL_1["data_puncak_1"]
data_puncak_2 = DATASET_SOAL_2["data_puncak_2"]
data_puncak_3 = DATASET_SOAL_3["data_puncak_3"]



def calculate_lattice_parameters(data_puncak: list, wavelength: float) -> pd.DataFrame:
    """Menghitung nilai d-spacing dan parameter kisi a untuk kisi kubus."""
    df = pd.DataFrame(data_puncak)

    theta_rad = np.radians(df["2theta"] / 2.0)

    # sum of squares: h^2 + k^2 + l^2
    h2_k2_l2 = df["h"] ** 2 + df["k"] ** 2 + df["l"] ** 2

    #  Bragg: d = lambda / (2 * sin(theta))
    df["d (Å)"] = wavelength / (2.0 * np.sin(theta_rad))

    # kisi kubus: a = d * sqrt(h^2 + k^2 + l^2)
    df["a (Å)"] = df["d (Å)"] * np.sqrt(h2_k2_l2)

    return df


def display_results(material_name: str, df_result: pd.DataFrame) -> None:
    """Menampilkan tabel hasil dan nilai statistik ke konsol."""
    a_mean = df_result["a (Å)"].mean()
    a_std = df_result["a (Å)"].std()

    print(f"\n{'=' * 65}")
    print(f"ANALISIS KISI STRUKTUR KUBUS: {material_name}")
    print(f"{'=' * 65}")

    # Formating
    formatted_df = df_result.copy()
    formatted_df["2theta"] = formatted_df["2theta"].apply(lambda x: f"{x:.3f}°")
    formatted_df["d (Å)"] = formatted_df["d (Å)"].apply(lambda x: f"{x:.4f}")
    formatted_df["a (Å)"] = formatted_df["a (Å)"].apply(lambda x: f"{x:.4f}")

    print(
        formatted_df[["2theta", "h", "k", "l", "d (Å)", "a (Å)"]].to_string(index=False)
    )
    print(f"{'-' * 65}")
    print(f"Parameter Kisi Rata-Rata (a) : {a_mean:.4f} Å")
    print(f"Standar Deviasi              : {a_std:.2e} Å")
    print(f"{'=' * 65}\n")


def process_dataset(dataset_dict: dict, dataset_key: str) -> pd.DataFrame:
    """Mengemas tahapan kalkulasi dan output display."""
    df_result = calculate_lattice_parameters(
        data_puncak=dataset_dict[dataset_key], wavelength=dataset_dict["lambda"]
    )
    display_results(dataset_dict["material"], df_result)
    return df_result


def export_to_markdown(material_name: str, df_result: pd.DataFrame) -> str:
    """Menghasilkan teks berformat Markdown rapi lengkap dengan tabel."""
    a_mean = df_result["a (Å)"].mean()
    a_std = df_result["a (Å)"].std()

    # Salin dan format angka agar desimalnya seragam
    df_md = df_result.copy()
    df_md["2theta"] = df_md["2theta"].apply(lambda x: f"{x:.3f}°")
    df_md["d (Å)"] = df_md["d (Å)"].apply(lambda x: f"{x:.4f}")
    df_md["a (Å)"] = df_md["a (Å)"].apply(lambda x: f"{x:.4f}")

    # Konversi tabel pandas ke Markdown table
    tabel_md = df_md[["2theta", "h", "k", "l", "d (Å)", "a (Å)"]].to_markdown(
        index=False
    )

    konten = f"""## Analisis Struktur Kisi: {material_name}

{tabel_md}

* **Nilai Parameter Kisi Rata-Rata ($a$):** **{a_mean:.4f} Å**
* **Standar Deviasi:** {a_std:.2e} Å

---
"""
    return konten


def main():
    daftar_tugas = [
        (DATASET_SOAL_1, "data_puncak_1"),
        (DATASET_SOAL_2, "data_puncak_2"),
        (DATASET_SOAL_3, "data_puncak_3"),
    ]

    laporan_md = "# Laporan Analisis Parameter Kisi XRD (Struktur Kubus)\n\n"

    for data_soal, key_puncak in daftar_tugas:
        df_hasil = calculate_lattice_parameters(
            data_puncak=data_soal[key_puncak], wavelength=data_soal["lambda"]
        )

        display_results(data_soal["material"], df_hasil)

        laporan_md += export_to_markdown(data_soal["material"], df_hasil)

    nama_file = "laporan_analisis_kisi.md"
    with open(nama_file, "w", encoding="utf-8") as file:
        file.write(laporan_md)

    print(f"Laporan berhasil disimpan ke file: {nama_file}")


if __name__ == "__main__":
    main()
