import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Fungsi untuk menghitung luas dan keliling persegi
def hitung_persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2*(panjang + lebar)
    return luas, keliling

# Panjang sisi persegi panjang
panjang = int(input("Masukan angka pertama disini: "))
lebar = int(input("Masukan angka kedua disini: "))

# Menghitung luas dan keliling
luas, keliling = hitung_persegi_panjang(panjang, lebar)

# Menampilkan persegi dengan matplotlib
fig, ax = plt.subplots()
persegi = patches.Rectangle((0, 0), panjang, lebar, linewidth=2, edgecolor='blue', facecolor='lightblue')
ax.add_patch(persegi)

# Menambahkan teks untuk sisi, luas, dan keliling
ax.text(panjang / 2, lebar + 0.5, f'Panjang = {panjang}, Lebar = {lebar}', ha='center', fontsize=12)
ax.text(panjang / 2, -1, f'Luas = {luas}', ha='center', fontsize=12)
ax.text(panjang / 2, -2, f'Keliling = {keliling}', ha='center', fontsize=12)

# Pengaturan tampilan plot
plt.xlim(-2, panjang + 2)
plt.ylim(-3, lebar + 2)
ax.set_aspect('equal')
plt.gca().set_axis_off()
plt.title("Visualisasi Persegi panjang")

# Menampilkan plot
plt.show()