import cv2
import numpy as np

#读入图片
img=cv2.imread('cat.jpg')

#创建/复制图像
emptyImage=np.zeros(img.shape,np.uint8)
emptyImage2=img.copy()
emptyImage3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#在窗口中显示图像
cv2.imshow('image',img)
cv2.imshow('EmptyImage',emptyImage3)
cv2.imshow('EmptyImage2',emptyImage2)
# 第三个参数表示图像质量
cv2.imwrite("cat2.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 5])
cv2.imwrite("cat3.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 100])
cv2.imwrite("cat.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
#压缩级别越高，尺寸越小
cv2.imwrite("cat2.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 9])

img=cv2.imread('F:\\W\\cos\\1.jpg')
cv2.imshow('cosplay',img)

cv2.waitKey(0)
cv2.destroyAllWindows()