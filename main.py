from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
# we import render_template and put in tutorial.html in a folder
# folder is called templates
# idea of this to allow website parameter/home to take to home page


@app.route('/api/v1/<station>/<date>')
#<> denote that user can enter value for those
def about(station,date):
    temperature = 23
    return {'station' :station,
        'date': date,
        'temperature' : temperature}


if __name__ =='__main__':
# this is a condition where we only run our website
# when this script is executed directly
# common practice
    app.run(debug=True)#debug = true to allow debugging

