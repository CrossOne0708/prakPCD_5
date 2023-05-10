# Mengimport library
import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load gambar
img = cv2.imread("bolehhh.jpg")

# Mendapatkan / define resolusi dan tipe gambar
img_height = img.shape[0]
img_width = img.shape[1]
img_channel = img.shape[2]
img_type = img.dtype

# ------------------------------------------------
# Percobaan Pertama (membuat brightness untuk gambar grayscale)
# Membuat variabel img_brightness untuk menampung

img_brightness = np.zeros(img.shape, dtype=np.uint8)


# Membuat fungsi penambahan brightness dengan nilai yang menjadi parameter
def brighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray += nilai
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_brightness[y][x] = (gray, gray, gray)


# Menampilkan gambar dengan parameter -100
brighter(-100)
cv2.imshow("Brightness -100", img_brightness)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Menampilkan gambar dengan parameter +25
brighter(25)
cv2.imshow("Brightness -100", img_brightness)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------------------------------------------
# Percobaan Kedua (membuat brightness untuk gambar RGB)

img_rgbbright = np.zeros(img.shape, dtype=np.uint8)


def rgbbrighter(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            # Channel Red
            red = img[y][x][0]
            red += nilai
            if red > 255:
                red = 255
            if red < 0:
                red = 0
            # Channel Green
            green = img[y][x][1]
            green += nilai
            if green > 255:
                green = 255
            if green < 0:
                green = 0
            # Channel Blue
            blue = img[y][x][2]
            blue += nilai
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0
            # Penjumlahan brightness
            img_rgbbright[y][x] = (red, green, blue)


# Menampilkan gambar dengan parameter -100
rgbbrighter(-100)
cv2.imshow("Brightness -100", img_rgbbright)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Menampilkan gambar dengan parameter +100
rgbbrighter(100)
cv2.imshow("Brightness +100", img_rgbbright)
cv2.waitKey(0)
cv2.destroyAllWindows()

# ------------------------------------------------
# Percobaan Ketiga (membuat contrast untuk gambar grayscale)

img_contrast = np.zeros(img.shape, dtype=np.uint8)


def contrast(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray += nilai
            if gray > 255:
                gray = 255
            if gray < 0:
                gray = 0
            img_contrast[y][x] = (gray, gray, gray)


# Menampilkan gambar dengan parameter +2
contrast(2)
cv2.imshow("Contrast +2", img_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Menampilkan gambar dengan parameter +10
contrast(10)
cv2.imshow("Contrast +10", img_contrast)
cv2.waitKey(0)
cv2.destroyAllWindows()
# ------------------------------------------------
# Percobaan Keempat (membuat contrast untuk gambar RGB)

img_rgbcontrast = np.zeros(img.shape, dtype=np.uint8)


def rgbcontrast(nilai):
    for y in range(0, img_height):
        for x in range(0, img_width):
            # Channel Red
            red = img[y][x][0]
            red += nilai
            if red > 255:
                red = 255
            if red < 0:
                red = 0
            # Channel Green
            green = img[y][x][1]
            green += nilai
            if green > 255:
                green = 255
            if green < 0:
                green = 0
            # Channel Blue
            blue = img[y][x][2]
            blue += nilai
            if blue > 255:
                blue = 255
            if blue < 0:
                blue = 0
            # Penjumlahan brightness
            img_rgbcontrast[y][x] = (red, green, blue)


fig, axes = plt.subplots(1, 2, figsize=(8, 5))
ax = axes.ravel()

# Menampilkan gambar dengan parameter +2
rgbcontrast(2)
ax[0].imshow(img_rgbcontrast)
ax[0].set_title("Contrast +2")

# Menampilkan gambar dengan parameter +10
rgbcontrast(10)
ax[1].imshow(img_rgbcontrast)
ax[1].set_title("Contrast +10")

fig.tight_layout()
plt.show()

# ------------------------------------------------
# Percobaan Kelima (membuat auto_contrast untuk gambar RGB)

# Membuat variabel contrast autolevel
img_autocontrast = np.zeros(img.shape, dtype=np.uint8)


def autocontrast():
    xmax = 255
    xmin = 0
    d = 0

    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            if gray < xmax:
                xmax = gray
            if gray > xmin:
                xmin = gray

    d = xmin - xmax
    for y in range(0, img_height):
        for x in range(0, img_width):
            red = img[y][x][0]
            green = img[y][x][1]
            blue = img[y][x][2]
            gray = (int(red) + int(green) + int(blue)) / 3
            gray = int(float(255 / d) * (gray - xmax))
            img_autocontrast[y][x] = (gray, gray, gray)


autocontrast()
cv2.imshow("Autolevel Contrast", img_autocontrast)
cv2.waitKey(0)
cv2.destroyAllWindows()
