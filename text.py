from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
def template_file():
     cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
     print(cities)

     
     return render_template('p1.html',cities=cities)

@app.route('/',methods=['GET','POST'])
def getvalue():
    fname=request.form['fname']
    print(fname)
    lname=request.form['lname']
    email=request.form['email']
    city=request.form['city']
    date=request.form['date']
    age=request.form['age']
    gender= request.form['gender']
    if gender == 'female':
        title = 'Ms ' + fname
    elif gender == 'male':
        title = 'Mr.'+ fname
    else:
        title = ''

    file = request.files['file']
    print(file)

    return render_template('p2.html',n=fname,l=lname, e=email,c=city, d=date,a=age,g=title, file=file)


if __name__ == '__main__':  
   app.run(debug=True)