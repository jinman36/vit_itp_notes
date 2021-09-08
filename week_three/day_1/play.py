import openpyxl

#Assign your .xlsx file to a variable
filename = "/mnt/c/Users/Jeffe/source/codefellows/vetsInTech/vit_itp_notes/week_three/day_1/lecture.xlsx"
wb = openpyxl.load_workbook(filename)

print(type(wb))