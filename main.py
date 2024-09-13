from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)


stations = pd.read_csv('data_small/stations.txt', skiprows = 17)
stations = stations[['STAID', 'STANAME                                 ']]
@app.route('/')
def home():
    return render_template('home.html', data=stations.to_html())
# we import render_template and put in tutorial.html in a folder
# folder is called templates
# idea of this to allow website parameter/home to take to home page


@app.route('/api/v1/<station>/<date>')
#<> denote that user can enter value for those
def about(station,date):
    filename = "data_small/TG_STAID" + str(station).zfill(6) +".txt"
    # example for str(99).zefill(6)= 000099, 6 digits
    df = pd.read_csv(filename, skiprows=20, parse_dates=['    DATE'])
    temperature = df.loc[df['    DATE'] ==date]['   TG'].squeeze()/10
    return {'station' :station,
        'date': date,
        'temperature' : temperature}


if __name__ =='__main__':
# this is a condition where we only run our website
# when this script is executed directly
# common practice
    app.run(debug=True)
#debug = true to allow debugging
# if we specify the port like app.run(debug=True, port=5001)
# as default is 5000, if we run 2 apps it will say port is occupied


