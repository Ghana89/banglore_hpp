from flask import Flask , render_template , request
import pandas as pd
from utils import prediction

app = Flask(__name__)
data = pd.read_csv('Bengaluru_House_Data.csv')

@app.route('/')
def index():
    location = data['location'].unique()
    area = data['area_type'].unique()
    return render_template('index.html' , locations = location ,areas = area )

@app.route("/pred" ,methods = ['POST', 'GET'])
def pred():
    data = request.form
    obj = prediction(data)
    result = obj.uer_predict()
    

    return render_template('index.html' , result_app = result)

if __name__ == '__main__':
    app.run(debug=True)