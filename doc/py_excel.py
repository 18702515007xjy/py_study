# -*- coding: UTF-8 -*- 

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

# ----------- Usage----------
# 1.读取excel文件
# workbook = xlrd.open_workbook('file.xls')

# 2.获取excel中表单数量
# workbook.nsheets

# 3.获取excel中的一个表单
# workbook.sheets()[i]
# workbook.sheet_by_index(i)
# workbook.sheet_by_name(u'Sheet1')

# 4.获取行数
# sheet.nrows

# 5.获取列数
# sheet.ncols

# 6.获取整行数据
# sheet.row(i)

# 7.获取整列数据
# sheet.col(i)

# 8.获取单元格数据
# sheet.cell(i, j).value

import xlrd

workbook = xlrd.open_workbook("excel_1.xlsx")

# print "There are {} sheets in the workbook".format(workbook.nsheets)
print ("There are "+str(workbook.nsheets)+" sheets in the workbook")

# 简单上手 - 遍历表中数据
# for booksheet in workbook.sheets():
#     for col in xrange(booksheet.ncols):
#         for row in xrange(booksheet.nrows):
#             value = booksheet.cell(row, col).value
#             print(value)


# 更进一步 - 按需求组合数据

writeData = '''--[[

        @author:xujinyun
        @qq: 136761906

--]]\n\n'''

fileOutput = open('excel_1.lua','w')
for booksheet in workbook.sheets():
    writeData = writeData + booksheet.name + ' = {\n'
    for col in xrange(booksheet.ncols):
        for row in xrange(booksheet.nrows):
            value = booksheet.cell(row, col).value
            if row == 0 :
                # writeData = writeData + '\t' + '["' + value + '"]' + ' = ' + '{' 
                writeData = writeData + '\t' + value + ' = ' + '{'  
            else :
                writeData = writeData + '"' + str(booksheet.cell(row, col).value) + '", '
        else :
            writeData = writeData + '},\n'
    else :
        writeData = writeData + '}\n\n'
else :
    fileOutput.write(writeData)

fileOutput.close()