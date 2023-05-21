# -*- coding: utf-8 -*-

import cv2
import numpy as np
# kütüphaneler

cap = cv2.VideoCapture(r'C:\Users\Selin\Desktop\python\wastes.mp4')
# yerel videonun aktarılması

while(True):
    
 ret, frame = cap.read()
 # video okuma
 
 if ret == False:
    break 
# video kontrol    


# TESPİTLER 

 #Plastik

 hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
 # hsv dönüşümü

 low_blue = np.array([94,160,2])
 upper_blue = np.array([126,255,255])
 # maskeleme için alt üst sınırlar

 blue_mask = cv2.inRange(hsv,low_blue,upper_blue)
 # maskeleme

 median = cv2.medianBlur(blue_mask, 5)
 # gürültü giderme

 cnts,hierarchy = cv2.findContours(median, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
 for cnt in cnts:
     x,y,w,h = cv2.boundingRect(cnt)
     area = cv2.contourArea(cnt) 
     if(150 < area < 2000):
        cv2.putText(frame, 'plastik',(x+20,y+20),cv2.FONT_HERSHEY_PLAIN,1.5,(0,255,0),2)
 # plastik tespiti     
             
 #Kağıt
 
 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
 # griye dönüştürme

 median2 = cv2.medianBlur(gray,5)
 # gürültü giderme

 ret,thresh = cv2.threshold(median2,180,255,cv2.THRESH_BINARY)
 # filtreleme

 median2 = cv2.medianBlur(thresh,5)
 # gürültü giderme

 kernel = np.ones((5,5),np.uint8)
 # filtre için kernel oluşturma

 closing = cv2.morphologyEx(median2, cv2.MORPH_CLOSE, kernel)
 # kapatma filtresi

 cnts,hierarchy = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
 for cnt in cnts:
     x,y,w,h = cv2.boundingRect(cnt)
     area = cv2.contourArea(cnt)
     if(area>2500):
        cv2.putText(frame, 'kagit',(x+30,y+30),cv2.FONT_HERSHEY_PLAIN,1.5,(255,0,0),2)
 # kağıt tespiti
       
 #Cam

 median3 = cv2.medianBlur(frame,5)
 # gürültü giderme
 
 hsv = cv2.cvtColor(median3, cv2.COLOR_BGR2HSV)
 # hsv dönüşümü
 
 low_green = np.array([40,80,80])
 upper_green = np.array([80,255,255])
 # maskeleme için alt üst sınırlar

 green_mask = cv2.inRange(hsv,low_green,upper_green)
 # maskeleme
    
 median4 = cv2.medianBlur(green_mask,5)
 # gürültü giderme

 kernel = np.ones((5,5),np.uint8)
 # filtre için kernel oluşturma

 closing = cv2.morphologyEx(median4, cv2.MORPH_CLOSE, kernel)
 # kapatma filtresi

 cnts,hierarchy = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
 for cnt in cnts:
     x,y,w,h= cv2.boundingRect(cnt)
     area = cv2.contourArea(cnt)
     if(area>1500):
        cv2.putText(frame, 'cam',(x,y+60),cv2.FONT_HERSHEY_PLAIN,1.5,(0,0,255),2)
 # cam tespiti      
        
 cv2.imshow('frame',frame)
 # sonuç gösterimi

 k = cv2.waitKey(1)
 if k%256 == 27:
    break


cap.release()
# videoyu serbest bırakma

cv2.destroyAllWindows()
# açık pencere kapatma
    
    
    