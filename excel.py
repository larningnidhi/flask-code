from flask import Flask, render_template, request
import xlsxwriter
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
           
        workbook = xlsxwriter.Workbook('data.xlsx')
        worksheet = workbook.add_worksheet()

        headers = ['First Name', 'Last Name', 'Email', 'City', 'Date', 'Age', 'Gender']
        for col, header in enumerate(headers):
            worksheet.write(0, col, header)
        
        row_counter=1
        data_values = [fname, lname, email, city, date, age, gender]
        for col, value in enumerate(data_values):
             print(col)
             print(value)
             worksheet.write(row_counter, col, value)
        row_counter +=1

        workbook.close()

        return "Success: Data saved to Excel file!"      
    else:
        cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
        return render_template('p1.html', cities=cities)

if __name__ == '__main__':  
    app.run(debug=True)
