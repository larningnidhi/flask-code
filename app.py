from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/demo')
def demo():
    return "demo function"

@app.route('/', methods=['GET', 'POST'])
def template_file():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        city = request.form.get('city')
        date = request.form['date']
        age = request.form['age']
        gender = request.form['gender']
        
        if gender == 'female':
            title = 'Ms ' + fname
        elif gender == 'male':
            title = 'Mr. ' + fname
        else:
            title = ''
        
        file = request.files['file']
        print(file)
        
        return render_template('p2.html', n=fname, l=lname, e=email, c=city, d=date, a=age, g=title, file=file)
    
    else:
        cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
        return render_template('p1.html', cities=cities)

if __name__ == '__main__':  
    app.run(debug=True)

   