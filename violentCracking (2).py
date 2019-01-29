#[xa,ya]
#[xb,yb]
#[xc,yc]

#[m,n]

#da,db,dc
#f1,f2,f3

#F[m,n]=f1+f2+f3


##Open the D01.xlsx##################################


import xlrd
import xlwt
from datetime import date,datetime

import numpy as np

import math

max_num = 0.0


workbook = xlrd.open_workbook(r"C:\2019IMMC\IMMC2019-ProblemD\D01.xlsx")
sheet1_name = workbook.sheet_names()[0]

sheet1 = workbook.sheet_by_index(0)
sheet1 = workbook.sheet_by_name('Sheet1')

######################################################

#Right side & Left side of the equation
right_list = []
left_list = []

#make the list of the right side
for r in range(2,12):
    rows = sheet1.row_values(r)
    for c in range(2,7):
        left_list.append(round(rows[c],3))

#make the list of the right side
#enumeration for Xanypoint
for x_a in range(0,100):
    
    #enumeration for Yanypoint
    for y_a in range(0,100):

        #enumeration for xA
        for xa in range(0,5):

            #enumeration for yA
            for ya in range(0,10):

               #enumeration for xB 
                for xb in range(0,5):

                    #enumeration for yB
                    for yb in range(0,10):

                        #enumeration for xC
                        for xc in range(0,5):

                            #enumeration for yC
                            for yc in range(0,10):
                            
                                #Calculate the distance between that anypoint and A,B,C
                                da = math.sqrt(math.pow((xa-x_a),2)+math.pow((ya-y_a),2))
                                db = math.sqrt(math.pow((xb-x_a),2)+math.pow((yb-y_a),2))
                                dc = math.sqrt(math.pow((xc-x_a),2)+math.pow((yc-y_a),2))

                                if x_a == xa and y_a == ya:
                                    da = 1
                                if x_a == xb and y_a == yb:
                                    db = 1
                                if x_a == xc and y_a == yc:
                                    dc = 1

                                #The Pollution Value in a particular distance(da/db/dc) between A/B/C and that anypoint
                                #a/b/c means a coefficient for the unknown equation
                                #fa = a/math.pow(da)
                                #fb = b/math.pow(db)
                                #fc = c/math.pow(dc)

                                right_list.append([round(1/math.pow(da,2),3),round(1/math.pow(db,2),3),round(1/math.pow(dc,2),3)])
                                
#solute
from numpy.linalg import lstsq
right = np.mat(right_list)
left = np.mat(left_list).T
result = lstsq(right,left)
print(result)
