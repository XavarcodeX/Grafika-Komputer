import matplotlib.pyplot as plt
import numpy as np

def plot_circle_with_main_points(xp, yp, r):
    # Titik-titik utama (8 titik di oktan utama)
    main_points = [
        (xp, yp + r),   # Atas
        (xp, yp - r),   # Bawah
        (xp + r, yp),   # Kanan
        (xp - r, yp),   # Kiri
        (xp + int(r / np.sqrt(2)), yp + int(r / np.sqrt(2))),  # 45° Kuadran I
        (xp - int(r / np.sqrt(2)), yp + int(r / np.sqrt(2))),  # 135° Kuadran II
        (xp + int(r / np.sqrt(2)), yp - int(r / np.sqrt(2))),  # 315° Kuadran IV
        (xp - int(r / np.sqrt(2)), yp - int(r / np.sqrt(2)))   # 225° Kuadran III
    ]

    # Buat grafik
    plt.figure(figsize=(6, 6))
    plt.axis("equal")  # Menjaga proporsi lingkaran
    plt.grid(True)

    # Plot 8 titik utama dengan warna biru
    x_main, y_main = zip(*main_points)
    plt.scatter(x_main, y_main, color='blue', s=50,)

    # Hubungkan titik-titik utama dengan garis lingkaran ideal
    circle_x = [xp + r * np.cos(angle) for angle in np.linspace(0, 2 * np.pi, 100)]
    circle_y = [yp + r * np.sin(angle) for angle in np.linspace(0, 2 * np.pi, 100)]
    plt.plot(circle_x, circle_y, 'g-', linewidth=1.5,)

    # Tambahkan anotasi pada 8 titik utama
    for i, (x, y) in enumerate(main_points):
        plt.text(x, y, f"({x},{y})", fontsize=9, color='blue', ha='right')

    # Tambahkan judul dan legenda
    plt.title(f"Lingkaran Midpoint (Pusat: ({xp}, {yp}), Radius: {r})")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.legend()
    plt.show()

    # Cetak titik-titik utama
    print("8 Titik Utama:")
    for point in main_points:
        print(point)

# Input dari pengguna
xp = float(input("Masukkan koordinat x pusat lingkaran (xp): "))
yp = float(input("Masukkan koordinat y pusat lingkaran (yp): "))
r = float(input("Masukkan jari-jari lingkaran (r): "))

# Jalankan fungsi untuk menggambar lingkaran
plot_circle_with_main_points(xp, yp, r)
