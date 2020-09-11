import cv2 
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


##주어진 이미지와 라벨 파일을 활용하여 이미지 위에 bounding box를 표시해 보시기 바랍니다.
img0=cv2.imread('000000.png')
df0=pd.read_csv('000000.txt',sep=' ',header=None)


img1=cv2.imread('000001.png')
df1=pd.read_csv('000001.txt',sep=' ',header=None)

img2=cv2.imread('000002.png')
df2=pd.read_csv('000002.txt',sep=' ',header=None)

img3=cv2.imread('000003.png')
df3=pd.read_csv('000003.txt',sep=' ',header=None)

img4=cv2.imread('000004.png')
df4=pd.read_csv('000004.txt',sep=' ',header=None)

img5=cv2.imread('000005.png')
df5=pd.read_csv('000005.txt',sep=' ',header=None)


def boundingbox(img,df):
    for X in range (0,len(df)):
        label=df[0][X] 
        x1=round(float(df[4][X])) 
        y1=round(float(df[5][X]))
        x2=round(float(df[6][X]))
        y2=round(float(df[7][X]))
        img2=cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),1)
        img2=cv2.putText(img, label, (x1-10,y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
    return img2

img0=boundingbox(img0,df0)
img1=boundingbox(img1,df1)
img2=boundingbox(img2,df2)
img3=boundingbox(img3,df3)
img4=boundingbox(img4,df4)
img5=boundingbox(img5,df5)

cv2.imshow('img',img0)
cv2.waitKey(0)

cv2.imshow('img',img1)
cv2.waitKey(0)

cv2.imshow('img',img2)
cv2.waitKey(0)

cv2.imshow('img',img3)
cv2.waitKey(0)

cv2.imshow('img',img4)
cv2.waitKey(0)
cv2.imshow('img',img5)
cv2.waitKey(0)
cv2.destroyAllWindows()