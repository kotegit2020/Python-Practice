"""
f = open("testdoc.txt" ,"a")
f.write("this file has an extra record now")
#print(f.read())
f.close()

f=open("testdoc.txt")
print(f.read())
f.close()
"""
import xlrd
import xlwt


#loc = r"C:\Users\KOTI\Desktop\Python Practice\testsheet.xlsx"
wb = xlrd.open_workbook('testsheet.xlsx')
sheet = wb.sheet_by_index(0)
print(sheet.cell_value(1,1))
data = [sheet.cell_value(0, col) for col in range(sheet.ncols)]

workbook = xlwt.Workbook()
sheet = workbook.add_sheet('test')

for index, value in enumerate(data):
    sheet.write(0, index, value)

workbook.save('output.xls')

