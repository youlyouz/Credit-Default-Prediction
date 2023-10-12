from flask import Flask, request, render_template
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')
import pandas as pd

model = pickle.load(open('pipeline.pkl', 'rb'))

cols = ['loan_amnt' , 'int_rate' , 'grade' , 'revol_bal' , 'out_prncp' , 'total_rec_int' , 'total_rec_late_fee' , 'recoveries' , 'last_pymnt_amnt']

app = Flask(__name__)

# Define a route for the home page
@app.route('/', methods=['GET', 'POST'])
def index():

    output = None

    if request.method == 'POST':
        # Get the values submitted in the form
        loan_amnt = float(request.form['loan_amnt'])
        int_rate = float(request.form['int_rate'])
        grade = request.form['grade']
        revol_bal = float(request.form['revol_bal'])
        out_prncp = float(request.form['out_prncp'])
        total_rec_int = float(request.form['total_rec_int'])
        total_rec_late_fee = float(request.form['total_rec_late_fee'])
        recoveries = float(request.form['recoveries'])
        last_pymnt_amnt = float(request.form['last_pymnt_amnt'])

        
        
        x = [[loan_amnt , int_rate , grade , revol_bal ,out_prncp ,total_rec_int , total_rec_late_fee , recoveries , last_pymnt_amnt]]

        x=pd.DataFrame(x , columns = cols)

        output = str(round(100*model.predict_proba(x)[0][1] , 2)) + ' %'

    return render_template('index.html', output=output)

if __name__ == '__main__':
    app.run(debug=True)
