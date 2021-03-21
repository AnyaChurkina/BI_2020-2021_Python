from PIL import Image, ImageEnhance, ImageFilter
import matplotlib.pyplot as plt
import cv2
import numpy as np


path = 'Planets.jpg'  # path to image

# Task 1. Editing images

# Filtering with PIL
PIL_image = Image.open(path)
# PIL_image.show()

# Filter 1: Change brightness
img1 = ImageEnhance.Brightness(PIL_image).enhance(0.5)
# img1.show()
img1.save("Brightness_planets.png")

# Filter 2: Change contrast
img2 = ImageEnhance.Contrast(PIL_image).enhance(1.2)
# img2.show()
img2.save("Contrast_planets.png")

# Filter 3: Detail planet
img3 = PIL_image.filter(ImageFilter.DETAIL)
# img3.show()
img3.save("Detail_planets.png")

# Filter 4: Cropped image
left = 240
top = 100
right = 1200
bottom = 550
img4 = PIL_image.crop((left, top, right, bottom))
# img4.show()
img4.save("Cropped_planets.png")

# Filtering with plt
# Filter 5: bone cmap
plt.figure(figsize=(16, 9))
plt_planets = plt.imread(path)
plt.imshow(plt_planets[:, :, 1], cmap="bone")
plt.axis("off")
# plt.show()
plt.savefig('Bone_planets.png')

# Filter 6: hot cmap
plt.figure(figsize=(16, 9))
plt.imshow(plt_planets[:, :, 1], cmap="hot")
plt.axis("off")
# plt.show()
plt.savefig('Hot_planets.png')

# Filtering with OpenCV
# Filter 7: Add the Gaussian noise to the image
CV_image = cv2.imread(path)
gauss = np.random.normal(0, 1, CV_image.size)
gauss = gauss.reshape(plt_planets.shape[0], plt_planets.shape[1],
                      plt_planets.shape[2]).astype('uint8')
img_gauss = cv2.add(plt_planets, gauss)
# cv2.imshow('Gauss_planets', img_gauss)
# cv2.waitKey(0)
cv2.imwrite('Gauss_planets.png', img_gauss)

# Filter 8: Black/white image
bw = cv2.cvtColor(CV_image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('bw', bw)
# cv2.waitKey(0)
cv2.imwrite('Bw_planets.png', bw)

# Filter 9: Planets in galaxy
galaxy = Image.open("galaxy.jpg")  # path to background image
planets = Image.open(path)
galaxy = galaxy.resize(planets.size)

glx = np.asarray(galaxy)
plnts = np.asarray(planets)

img = np.where(plnts > [0.9, 0.9, 0.9], plnts, glx)
plt.figure(figsize=(16, 9))
plt.axis("off")
plt.imshow(img)
# plt.show()
plt.savefig('Planets_in_galaxy.png')

# Filter 10: Milky way planets
planets = planets.convert('L')
im_rgba = galaxy.copy()
im_rgba.putalpha(planets)
# im_rgba.show()
im_rgba.save("Milky_way_planets.png")

# Task 2. Finding circles
gray_image = cv2.cvtColor(CV_image, cv2.COLOR_BGR2GRAY)
blur_image = cv2.medianBlur(gray_image, 11)
thresh_image = cv2.threshold(blur_image, 0, 255, cv2.THRESH_BINARY +
                             cv2.THRESH_OTSU)[1]

kernel = np.ones((5, 5), np.uint8)
opening = cv2.morphologyEx(thresh_image, cv2.MORPH_OPEN, kernel,
                           iterations=1)

contours = cv2.findContours(opening, cv2.RETR_EXTERNAL,
                            cv2.CHAIN_APPROX_SIMPLE)
contours = contours[0] if len(contours) == 2 else contours[1]

for cnt in contours:
    peri = cv2.arcLength(cnt, True)
    approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)
    area = cv2.contourArea(cnt)
    if len(approx) > 5 and 1000 < area < 1000000:
        ((x, y), r) = cv2.minEnclosingCircle(cnt)
        cv2.circle(CV_image, (int(x), int(y)), int(r), (255, 255, 0), 4)

# cv2.imshow('image', CV_image)
# cv2.waitKey()
cv2.imwrite('Find_circles.png', CV_image)
