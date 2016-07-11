#Writing this script to schedule wallppaer cahnge

Motive of the script if to  automatically update after some time , so I will not be bored with my desktop.

#Cron Entry:
*/1 * * * *  export DISPLAY=:0.0 && /usr/bin/python /home/abhijeet/projects/wallpaperchanger/wallpaperchanger.py 
