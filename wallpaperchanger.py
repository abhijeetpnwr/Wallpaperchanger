#Writtern by Abhijeet

import os
from random import randint

wallpaperdir="/home/abhijeet/MEGA/wallpapers/"

totalwallpapers = 0

wallpaperlist=[]

for file in os.listdir(wallpaperdir):
    if file.endswith(".jpg"):
	totalwallpapers=totalwallpapers+1
	wallpaperlist.append(wallpaperdir+file)
	
wallpaperno=randint(0,totalwallpapers)

toset = wallpaperlist[wallpaperno]

print toset

command = "gsettings set org.gnome.desktop.background picture-uri "+toset

os.system(command)
