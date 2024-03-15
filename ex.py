from flask import Flask
import xlrd 

app = Flask(__name__)

@app.route('/')
def read():
    workbook=xlrd.open_workbook('demo1.xlsx')
    sheet = workbook.sheet_by_index(0)
    for i in range(sheet.nrows):
        print(i)
        #print(sheet.cell_value(0,i))
    for i in range(sheet.ncols):
        print(i)
        #print(sheet.cell_value(0, i))
    return "success"   

if __name__ == '__main__':
    app.run(debug=True)








# from flask import Flask
# import xlrd as x

# app = Flask(__name__)

# @app.route('/')
# def read():
#     wb = x.open_workbook('demo1.xlsx')
#     sheet = wb.sheet_by_index(0)
#     for i in range(sheet.nrows):
#         print(i)
#         print(sheet.cell_value(0,i))
#     for i in range(sheet.ncols):
#         print(i)
#         print(sheet.cell_value(0, i))
#     return "success"   

# if __name__ == '__main__':
#     app.run(debug=True)





# from flask import Flask
# import os
# import xlrd as x

# app = Flask(__name__)

# @app.route('/')
# def read():
#     loc_file=("<demo1.xlsx>")
#     wb = x.open_workbook(loc_file)
#     sheet = wb.sheet_by_index(0)
#     print(sheet.nrows)
#     print(sheet.ncols)
#     return "success"   

# if __name__ == '__main__':
#     app.run(debug=True)