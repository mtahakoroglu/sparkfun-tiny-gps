import cv2
import numpy as np

img1 = cv2.imread("IMG-20250506.jpg")
img2 = cv2.imread("gps data 06-May-2025 14-15-37.png")
(h1,w1,c) = img1.shape
(h2,w2,c) = img2.shape
print("img1 shape: ", img1.shape)
print("img2 shape: ", img2.shape)

if (w1 != w2):
    if (w1>w2):
        s = w2/w1
        img1 = cv2.resize(img1, (w2, int(s*img1.shape[0])), interpolation=cv2.INTER_AREA)
    elif (w2 > w1):
        s = w1/w2
        img2 = cv2.resize(img2, (w1, int(s*img2.shape[0])), interpolation=cv2.INTER_AREA)

print("img1 shape: ", img1.shape)
print("img2 shape: ", img2.shape)

# write text on images
# img1 = cv2.putText(img1,"(a)",(75,150), 0, 4, (255,255,255), 12, lineType=cv2.INTER_AREA)
# img2 = cv2.putText(img2,"(b)",(75,150), 0, 4, (255,255,255), 12, lineType=cv2.INTER_AREA)

# Get the exact target width after resizing
target_width = min(img1.shape[1], img2.shape[1])

# Create combined image with the precise dimensions
img = np.zeros((img1.shape[0]+img2.shape[0], target_width, c), np.uint8)
img[0:img1.shape[0],:,:] = img1[:,:target_width,:]
img[img1.shape[0]:img1.shape[0]+img2.shape[0],:,:] = img2[:,:target_width,:]

# resize image for display and then save & display image
s = 0.2
rimg = cv2.resize(img, (int(s*img.shape[1]), int(s*img.shape[0])), interpolation=cv2.INTER_AREA)
cv2.imwrite("2025_05_06_gps_experiment.jpg", img, [cv2.IMWRITE_JPEG_QUALITY,60])
cv2.imshow("GPS experiment", rimg)
cv2.waitKey(0)