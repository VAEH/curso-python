import openpyxl

wb = openpyxl.load_workbook('CT01 Categorizacion 2021.xlsx')

#print(wb.sheetnames)

sheet = wb['Categoría con historicos']
print(sheet['A15'].value)