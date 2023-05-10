# Mengimport library
import matplotlib.pyplot as plt
import cv2
from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray
from skimage.util import invert
import numpy as np

# PERCOBAAN 1 : CROP IMAGE
# Load gambar dari local drive
huh = cv2.imread("huh.jpg")
kucing = cv2.imread("kucing.jpg")

# Cropping gambar
huhCropped = huh.copy()
huhCropped = huhCropped[150:680, 150:680]

kucingCropped = kucing.copy()
kucingCropped = kucingCropped[150:800, 150:800]

# Membuat figure subplot
fig, axes = plt.subplots(2, 2, figsize=(8, 8))
ax = axes.ravel()

# Plot gambar pertama dengan cv2.imshow
ax[0].imshow(cv2.cvtColor(huh, cv2.COLOR_BGR2RGB))
ax[0].set_title("Citra Input 1")

# Plot gambar kedua dengan cv2.imshow
ax[1].imshow(cv2.cvtColor(kucing, cv2.COLOR_BGR2RGB))
ax[1].set_title("Citra Input 2")

# Plot gambar ketiga dengan cv2.imshow
huhCropped_resized = cv2.resize(cv2.cvtColor(huhCropped, cv2.COLOR_BGR2RGB), (320, 320))
ax[2].imshow(huhCropped_resized)
ax[2].set_title("Citra Output 1")

# Plot gambar keempat dengan cv2.imshow
kucingCropped_resized = cv2.resize(
    cv2.cvtColor(kucingCropped, cv2.COLOR_BGR2RGB), (800, 800)
)
ax[3].imshow(kucingCropped_resized)
ax[3].set_title("Citra Output 2")

fig.tight_layout()
plt.show()

# ------------------------------------------------
# PERCOBAAN 2 : CITRA NEGATIVE
inv = invert(huhCropped)
print("Shape Input : ", huhCropped.shape)
print("Shape Output : ", inv.shape)

fig, axes = plt.subplots(2, 2, figsize=(8, 8))
ax = axes.ravel()

# Plot Gambar Input dengan cv2.imshow
ax[0].imshow(cv2.cvtColor(huh, cv2.COLOR_BGR2RGB))
ax[0].set_title("Citra Input")

# Plot Histogram Input
ax[1].hist(huhCropped.ravel(), bins=256)
ax[1].set_title("Histogram Input")

# Plot Gambar Output Negatif
ax[2].imshow(inv)
ax[2].set_title("Citra Output (Inverted Image)")

# Plot Histogram Output Negatif
ax[3].hist(inv.ravel(), bins=256)
ax[3].set_title("Histogram Output")

fig.tight_layout()
plt.show()

# ------------------------------------------------
# PERCOBAAN 3 : INCREASE BRIGHTNESS
copyKucing = kucingCropped.copy().astype(float)

# m1, n1 = copyKucing.shape[:2]  # hanya memuat satu nilai tuple

# Menambahkan variabel brightness
brightness = 100
kucing_bright = np.clip(copyKucing + brightness, 0, 255).astype(dtype=np.uint8)

# for baris in range(0, m1 - 1):
#     for kolom in range(0, n1 - 1):
#         a1 = baris
#         b1 = kolom
#         kucing_bright[a1, b1] = copyKucing[baris, kolom] + 100

fig, axes = plt.subplots(2, 2, figsize=(8, 8))
ax = axes.ravel()

# Plot Gambar Input dengan cv2.imshow
ax[0].imshow(cv2.cvtColor(kucing, cv2.COLOR_BGR2RGB))
ax[0].set_title("Citra Input 2")

ax[1].hist(kucingCropped.ravel(), bins=256)
ax[1].set_title("Histogram Input")

ax[2].imshow(cv2.cvtColor(kucing_bright, cv2.COLOR_BGR2RGB))
ax[2].set_title("Citra Output (Brightness +100)")

ax[3].hist(kucing_bright.ravel(), bins=256)
ax[3].set_title("Histogram Output")

fig.tight_layout()
plt.show()

brightness = 50
kucing_bright = np.clip(copyKucing + brightness, 0, 255).astype(dtype=np.uint8)

fig, axes = plt.subplots(2, 2, figsize=(8, 8))
ax = axes.ravel()

# Plot Gambar Input dengan cv2.imshow
ax[0].imshow(cv2.cvtColor(kucing, cv2.COLOR_BGR2RGB))
ax[0].set_title("Citra Input 2")

ax[1].hist(kucingCropped.ravel(), bins=256)
ax[1].set_title("Histogram Input")

ax[2].imshow(cv2.cvtColor(kucing_bright, cv2.COLOR_BGR2RGB))
ax[2].set_title("Citra Output (Brightness +50)")

ax[3].hist(kucing_bright.ravel(), bins=256)
ax[3].set_title("Histogram Output")

fig.tight_layout()
plt.show()
