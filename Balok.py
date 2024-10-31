import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Menghitung luas permukaan dan volume balok
def hitung_balok(panjang, lebar, tinggi):
    luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
    volume = panjang * lebar * tinggi
    return luas_permukaan, volume

panjang = int(input("Masukan Panjang Balok: "))
lebar = int(input("Masukan Lebar Balok: "))
tinggi = int(input("Masukan Tinggi Balok: "))
luas_permukaan, volume = hitung_balok(panjang, lebar, tinggi)

# Visualisasi balok
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

vertices = [
    [0, 0, 0], [panjang, 0, 0], [panjang, lebar, 0], [0, lebar, 0],
    [0, 0, tinggi], [panjang, 0, tinggi], [panjang, lebar, tinggi], [0, lebar, tinggi]
]
edges = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],
    [vertices[4], vertices[5], vertices[6], vertices[7]],
    [vertices[0], vertices[1], vertices[5], vertices[4]],
    [vertices[2], vertices[3], vertices[7], vertices[6]],
    [vertices[1], vertices[2], vertices[6], vertices[5]],
    [vertices[4], vertices[7], vertices[3], vertices[0]]
]

ax.add_collection3d(Poly3DCollection(edges, color="lightblue", edgecolor="blue", linewidths=1, alpha=0.5))

ax.set_xlabel("Panjang (cm)")
ax.set_ylabel("Lebar (cm)")
ax.set_zlabel("Tinggi (cm)")
ax.set_xlim([0, max(panjang, lebar) * 1.2])
ax.set_ylim([0, max(panjang, lebar) * 1.2])
ax.set_zlim([0, tinggi * 1.2])

plt.title(f"Balok (Luas Permukaan: {luas_permukaan} cm², Volume: {volume} cm³)")
plt.show()