import cv2
import numpy as np

img = cv2.imread('collections/image.png')

[x, y, z] = img.shape


eixo_x = y // 2
eixo_y = x // 2
print(eixo_x, eixo_y)



pontos = np.array([[100 + 50, 50], [200 + 50, 50], [250 + 50, 150], [150 + 50, 200], [50 + 50, 150]], np.int32)


cv2.polylines(img, [pontos], isClosed=True, color=(255, 0, 0), thickness=2)
cv2.circle(img, (eixo_x, eixo_y), 100, (150, 255, 220), thickness=3)



cv2.imshow('Imagem com Poligono', img)
cv2.waitKey(0)
cv2.destroyAllWindows()