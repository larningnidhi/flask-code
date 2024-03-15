from flask import Flask, render_template, request
import xlsxwriter

app = Flask(__name__)

@app.route('/insert_data', methods=['POST'])
def insert_data():
    # Retrieve data from the request
    item = request.form.get('item')

    # Create the Excel file and write data
    workbook = xlsxwriter.Workbook('pro1.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write('A1', item)
    workbook.close()

    return 'Data inserted successfully into Excel file!'

if __name__ == '__main__':  
    app.run(debug=True)
