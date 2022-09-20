#!/bin/bash


#Download python and latex templates

#svn co https://github.com/gadepall/training/trunk/math  /sdcard/Download/math

#Test Latex Installation
#Uncomment only the following lines and comment the above line

#cd /sdcard/Download/math 
cd /home/user/Documents/Assignments/assg_4
#pio run
 
texfot pdflatex Assg_4.tex
termux-open Assg_4.pdf


#Test Python Installation
#Uncomment only the following line
python3 rectangle.py

