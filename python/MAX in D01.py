import xlrd
import xlwt
from datetime import date,datetime

max_num = 0.0


workbook = xlrd.open_workbook(r"C:\2019IMMC\IMMC2019-ProblemD\D01.xlsx")
sheet1_name = workbook.sheet_names()[0]

sheet1 = workbook.sheet_by_index(0)
sheet1 = workbook.sheet_by_name('Sheet1')

for r in range(2,102):
    rows = sheet1.row_values(r)
    for c in range(2,102):
        temp = rows[c]

        if temp>max_num:
            max_num = temp

print max_num
