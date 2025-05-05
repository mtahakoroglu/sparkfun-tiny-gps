import cv2
import numpy as np

img1 = cv2.imread("enes-muratcan-stadium-walk.jpg")
img2 = cv2.imread("muratcan-enes-stadyum.png")
(h1,w1,c) = img1.shape
(h2,w2,c) = img2.shape
if (w1 != w2):
    if (w1>w2):
        s = w2/w1
        img1 = cv2.resize(img1, (int(s*img1.shape[1]),int(s*img1.shape[0])), interpolation=cv2.INTER_AREA)
    elif (w2 > w1):
        s = w1/w2
        img2 = cv2.resize(img2, (int(s*img2.shape[1]),int(s*img2.shape[0])), interpolation=cv2.INTER_AREA)
# write text on images
# img1 = cv2.putText(img1,"(a)",(75,150), 0, 4, (255,255,255), 12, lineType=cv2.INTER_AREA)
# img2 = cv2.putText(img2,"(b)",(75,150), 0, 4, (255,255,255), 12, lineType=cv2.INTER_AREA)
# merge images via numpy
img = np.zeros((img1.shape[0]+img2.shape[0],min(w1,w2),c), np.uint8)
img[0:img1.shape[0],:,:] = img1
img[img1.shape[0]:img1.shape[0]+img2.shape[0],:,:] = img2
# resize image for display and then save & display image
s = 0.2
rimg = cv2.resize(img, (int(s*img.shape[1]),int(s*img.shape[0])), interpolation=cv2.INTER_AREA)
cv2.imwrite("enes-muratcan-stadyum-rapor.jpg", img, [cv2.IMWRITE_JPEG_QUALITY,50])
cv2.imshow("Ens Muratcan Stadium Walk", rimg)
cv2.waitKey(0)