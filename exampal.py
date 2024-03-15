from flask import Flask
import xlsxwriter
import xlrd

app = Flask(__name__)

@app.route('/')
def demo():
    workbook = xlsxwriter.Workbook('demo1.xlsx')
    worksheet = workbook.add_worksheet()
    data = {'nidhi',  23,  'ahemdabad'} 
    row = 0
    col = 0
    for col, value in enumerate(data):
        worksheet.write(row, col, value)
    workbook.close()
    return " success"



if __name__ == '__main__':
    app.run(debug=True)