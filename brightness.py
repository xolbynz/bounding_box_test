import cv2 
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


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


def brightness(src):
    val=50
    array=np.full(src.shape,(val,val,val),dtype=np.uint8)
    img_add=cv2.add(src,array)
    img_sub=cv2.subtract(src,array)
    img_add2=cv2.add(img_add,array)
    img_sub2=cv2.subtract(img_sub,array)
    return src,img_add,img_add2,img_sub,img_sub2

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
    cv2.imshow('dd',dst0)
    cv2.waitKey(0)
    return dst0

bringtness0,bringtness1,bringtness2,bringtness3,bringtness4=brightness(img0)
bringtness5,bringtness6,bringtness7,bringtness8,bringtness9=brightness(img1)
bringtness10,bringtness11,bringtness12,bringtness13,bringtness14=brightness(img2)
bringtness15,bringtness16,bringtness17,bringtness18,bringtness19=brightness(img3)
bringtness20,bringtness21,bringtness22,bringtness23,bringtness24=brightness(img4)
bringtness25,bringtness26,bringtness27,bringtness28,bringtness29=brightness(img5)



bringtness0=boundingbox(bringtness0,df0)
bringtness1=boundingbox(bringtness1,df0)
bringtness2=boundingbox(bringtness2,df0)
bringtness3=boundingbox(bringtness3,df0)
bringtness4=boundingbox(bringtness4,df0)

bringtness5=boundingbox(bringtness5,df1)
bringtness6=boundingbox(bringtness6,df1)
bringtness7=boundingbox(bringtness7,df1)
bringtness8=boundingbox(bringtness8,df1)
bringtness9=boundingbox(bringtness9,df1)

bringtness10=boundingbox(bringtness10,df2)
bringtness11=boundingbox(bringtness11,df2)
bringtness12=boundingbox(bringtness12,df2)
bringtness13=boundingbox(bringtness13,df2)
bringtness14=boundingbox(bringtness14,df2)

bringtness15=boundingbox(bringtness15,df3)
bringtness16=boundingbox(bringtness16,df3)
bringtness17=boundingbox(bringtness17,df3)
bringtness18=boundingbox(bringtness18,df3)
bringtness19=boundingbox(bringtness19,df3)

bringtness20=boundingbox(bringtness20,df4)
bringtness21=boundingbox(bringtness21,df4)
bringtness22=boundingbox(bringtness22,df4)
bringtness23=boundingbox(bringtness23,df4)
bringtness24=boundingbox(bringtness24,df4)

bringtness25=boundingbox(bringtness25,df5)
bringtness26=boundingbox(bringtness26,df5)
bringtness27=boundingbox(bringtness27,df5)
bringtness28=boundingbox(bringtness28,df5)
bringtness29=boundingbox(bringtness29,df5)


cv2.destroyAllWindows()