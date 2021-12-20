import xlrd

loc=("")

wb=xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

p1=sheet.cell(2,0).value
print(p1)

print(sheet.nrows)
print(sheet.ncols)

for i in range(sheet.nrows)
    p2 - sheet.cell(i, 0).value
    print(p2)