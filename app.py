# importing required libraries
from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import LabelEncoder
import joblib

# creating the app
app = Flask(__name__)

# rendering the home page
@app.route('/')
def home():
    return render_template('index.html')

# rendering the result page
@app.route('/test', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        # accepting the inputs from the webpage and storing them inside a dictionary to be converted into a dataframe 
        data = {
                'Airline':[request.form['Airline']],
                'Source':[request.form['Source']],
                'Destination':[request.form['Destination']],
                'Total_Stops':[int(request.form['Total_Stops'])],
                'Additional_Info':[request.form['Additional_Info']],
                'Date':[int(request.form['Date_of_Journey'].split('-')[-1])],
                'Month':[int(request.form['Date_of_Journey'].split('-')[1])],
                'Arrival Hour':[int(request.form['Arrival_Time'].split(':')[0])],
                'Arrival Minute':[int(request.form['Arrival_Time'].split(':')[1])],
                'Departure Hour':[int(request.form['dep_time'].split(':')[0])],
                'Departure Minute':[int(request.form['dep_time'].split(':')[1])]
                }
        
        # calculating the duration of the flight in terms of minutes. 
        day_of_arrival= int(request.form['Date_of_Arrival'].split('-')[-1])
        departure_hour= int(data["Departure Hour"][0])
        arrival_hour= int(data['Arrival Hour'][0])
        day_of_departure= int(data['Date'][-1])
        deparure_minute= int(data['Departure Minute'][0])
        arrival_minute= int(data['Arrival Minute'][0])
    
        dur = (((24-departure_hour) + ((day_of_arrival-day_of_departure-1)*24) + arrival_hour)*60) - deparure_minute + arrival_minute

        # adding the duration to the dictionary
        data.update({'Duration Min': dur})
        
        # converting the dictionary into a dataframe
        input_df = pd.DataFrame(data)
        
        # loading the joblib file
        file = joblib.load('flight price prediction model.joblib')
        
        # extracting the necessary elements to perform data preprocessing
        model = file['model']
        scaler=file['scaler']
        numerical_cols=file['numerical columns']
        categorical_cols= file['categorical columns']
        encoders= file.get('encoders')

        # performing label encoding to all the categorical columns
        for col in categorical_cols:
            input_df[col] = encoders[col].transform(input_df[col])
        
        # performing data preprocessing
        input_df = scaler.transform(input_df)
        input_df = pd.DataFrame(input_df)
        input_df.columns = data.keys()
        
        # using the model to predict the flight ticket price
        prediction = model.predict(input_df)
        
        # rendering the webpage to show the predicted answer
        return render_template('test.html', prediction=float(prediction[0]))


if __name__=='__main__':
    app.run()


