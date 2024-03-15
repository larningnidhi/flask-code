from flask import Flask, render_template, request
import xlsxwriter
import xlrd
import os

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def template_file():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        city = request.form['city']
        date = request.form['date']
        age = request.form['age']
        gender = request.form['gender']

        workbook = xlsxwriter.Workbook('pro1.xlsx')
        worksheet = workbook.add_worksheet()
        
        filename = 'pro1.xlsx'
        name='Sheet1'
        if os.path.isfile(filename):
            print(filename)
            if name in workbook.sheetnames:
                print(name)
                last_row=worksheet.max_row+1
                data_value=[fname, lname, email, city, date, age, gender]
                print(data_value)
                for col, value in enumerate(data_value):
                    worksheet.cell(row=last_row,column=col+1, value=value) 
                workbook.close()   
            else:
                return "Sheet1 not found in existing workbook"
        else:
            return "Success: Data saved to Excel file!"
    else:
        cities = ["gandhinagar", "Ahemdabad", "Gota", "bopal", "puna"]
        return render_template('p1.html', cities=cities)
    

if __name__ == '__main__':  
    app.run(debug=True)

