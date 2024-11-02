import numpy as np
import matplotlib.pyplot as plt

n = 8
tile_size = 10
chessboard_pattern = np.zeros((n, n), dtype=int)
chessboard_pattern[1::2, ::2] = 1
chessboard_pattern[::2, 1::2] = 1
chessboard_image = np.kron(chessboard_pattern, np.ones((tile_size, tile_size)))
plt.imshow(chessboard_image, cmap='gray', interpolation='nearest')
plt.axis('on')
plt.show()