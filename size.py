import cv2 
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


## 이미지 기하변형 3단계 (https://opencv-python.readthedocs.io/en/latest/doc/10.imageTransformation/imageTransformation.html)
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

    dst0 = cv2.resize(img, dsize=(640, 360), interpolation=cv2.INTER_AREA)
    h, w, c = dst0.shape
    h_전,w_전,c_전=img.shape
    w_비율=w/w_전
    h_비율=h/h_전
    for X in range (0,len(df)):
        label=df[0][X] 
        x1=round(float(df[4][X])*w_비율) 
        y1=round(float(df[5][X])*h_비율)
        x2=round(float(df[6][X])*w_비율)
        y2=round(float(df[7][X])*h_비율)
        dst0=cv2.rectangle(dst0,(x1,y1),(x2,y2),(0,255,0),1)
        dst0=cv2.putText(dst0, label, (x1-10,y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 1)
    return dst0




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