import cv2
import numpy as np

img1 = cv2.imread("matlab-app-sensors.jpg")
img2 = cv2.imread("matlab-app-sensors-1.jpg")
img3 = cv2.imread("matlab-app-sensors-2.jpg")
(h,w,c) = img1.shape
# write text on images
img1 = cv2.putText(img1,"(a)",(475,110), 0, 3, (0,255,255), 9, lineType=cv2.INTER_AREA)
img2 = cv2.putText(img2,"(b)",(475,110), 0, 3, (0,255,255), 9, lineType=cv2.INTER_AREA)
img3 = cv2.putText(img3,"(c)",(475,110), 0, 3, (0,255,255), 9, lineType=cv2.INTER_AREA)
# merge images via numpy
img = np.zeros((h,3*w,c), np.uint8)
img[:,0:w,:] = img1
img[:,w:2*w,:] = img2
img[:,2*w:3*w,:] = img3
# resize image for display and then save & display image
s = 0.2
rimg = cv2.resize(img, (int(s*3*w),int(s*h)), interpolation=cv2.INTER_AREA)
cv2.imwrite("play-store-matlab-app-sensors.jpg", img, [cv2.IMWRITE_JPEG_QUALITY,30])
cv2.imshow("Google Play Store MATLAB app sensors screenshots", rimg)
cv2.waitKey(0)