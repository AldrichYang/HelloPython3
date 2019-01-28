import xlrd
loc = ("/Users/user/Desktop/N3.1.xlsx")
wb = xlrd.open_workbook(loc)
sheet_1 =wb.sheet_by_index(0)
col_a_row_6 = sheet_1.cell_value(0,2)
for i in range(sheet_1.ncols): 
    for j in range(sheet_1.nrows):
        print(sheet_1.cell_value(j, i)) 