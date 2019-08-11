#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2

BRc=[]
BRcc=[]
Ecc={}

# get elements coordinates inside canvas 
def find_elements(img_path):
    global BRc,BRcc
    src=cv2.imread(img_path)
    gray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
    dst=cv2.threshold(gray,250,255,cv2.THRESH_BINARY)[1]
    if int(cv2.__version__[0]) == 3:
       cnts=cv2.findContours(dst,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[1] 
    elif int(cv2.__version__[0]) == 4:
         cnts=cv2.findContours(dst.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)[0]
    for cnt in cnts:
        [x,y,w,h]=cv2.boundingRect(cnt)
        M=cv2.moments(cnt)
        if M["m00"]==0:
           continue
        if h < 18:
           continue
        if (x+w/2,y+h/2) in BRcc:
           continue  
        if 500 < w < 100:
           continue 
        BRc.append((x,y,w,h))  
        BRcc.append((x+w/2,y+h/2))  
    BRc=sorted(BRc,key=lambda x:x[1]) 
    BRcc=sorted(BRcc,key=lambda x:x[1]) 
    for i in range(len(BRcc)):
        x=BRc[i][0]
        y=BRc[i][1]
        w=BRc[i][2]
        h=BRc[i][3]  
        xc=BRcc[i][0]
        yc=BRcc[i][1]
        if i==11:
           cv2.rectangle(src,(x,y),(x+w,y+h),(0,0,255),2)
        cv2.circle(src,(xc,yc),5,(20,255,0),-1)
        cv2.putText(src,str(i+1),(xc-5,yc-12),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),2,cv2.LINE_AA)
        Ecc.update({"elem"+str(i+1):BRcc[i]})
    #cv2.imshow('canvas',src) 
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    return Ecc
if __name__=="__main__":
   find_elements(path)       