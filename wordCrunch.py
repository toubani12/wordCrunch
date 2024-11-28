import os
import tkinter as tk
from tkinter import *
fn=tk()

pathD=os.path.join(os.path.expanduser("~"), "Desktop")
numAlpha="ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
mac=input("enter the mac adress: \n")
while (len(mac)>17 or len(mac)<10  ):
    mac=input("enter the mac adress: \n")
suffix=""
file=open(pathD+'/'+mac+".txt","a")
for i in mac:
    if len(suffix)==10:
        pass
    else:
        if i==":" or i=="-":
            pass
        else:
        
            suffix+=i
suffix=suffix.upper()
for i in numAlpha:
    for j in numAlpha:
        file.write(suffix+i+j+"\n")
file.close()
print("done")
print(file.name)
input("tap enter key to exit")

