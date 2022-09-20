#Code by GVV Sharma (works on termux)
#February 16, 2022
#License
#https://www.gnu.org/licenses/gpl-3.0.en.html
#To solve a system of linear equations 


#Python libraries for math and graphics
import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

import sys                                          #for path to external scripts
sys.path.insert(0,'/home/user/Documents/CoordGeo')         #path to my scripts

#local imports
from line.funcs import *
from triangle.funcs import *
#from conics.funcs import circ_gen

#if using termux
#iimport subprocess
#import shlex
#end if

#Input parameters
#Input parameters
A = np.array(([0,0]))
e_1 = np.array(([1,0]))
k=4
B =k*e_1
r =6
theta = np.arccos(k/r)
C = r*np.array(([np.cos(theta),np.sin(theta)]))
D = np.array(([k-r*(np.cos(theta)),r*np.sin(theta)]))

#Generating all line
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_AD = line_gen(A,D)
x_AC = line_gen(A,C)
x_DB = line_gen(D,B)


#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_AC[0,:],x_AC[1,:],label='$AC$')
plt.plot(x_DB[0,:],x_DB[1,:],label='$DB$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')

#Labeling the coordinates
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.03), D[1] * (1 - 0.1) , 'D')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
plt.savefig('/home/user/Documents/Assignments/assg_4/fig.png')
#subprocess.run(shlex.split("termux-open /sdcard/ramesh/maths/fig.pdf"))
#else
plt.show()
