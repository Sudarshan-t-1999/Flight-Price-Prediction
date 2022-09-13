# Flight Ticket Price Prediction
![Capture](https://user-images.githubusercontent.com/76962685/189926442-c383f809-ff15-4fa1-8814-dd7a7fa28fb8.JPG)

The objective of this project is to predict the price of a flight ticket based on different options by training a machine learning model on the available data, it is used to predict a range for the price of the ticket which can be help while making the decision to book ticket.

The backend of this project is made using the **Flask** library of python and the frontend with **HTML**.

## How to run this project in local machine?
* First, download the contents of this repository to your local machine. You can do this by cloning the repository using the `git clone <repository url>` in Command Prompt(if you do not have git installed, download and install it from the git website) or click on the code button and then on 'Download ZIP' button and extract the files.
* Make sure you have installed python in your machine. If not, download and install it from the official python website.
* If not installed, open command prompt or powershell and install `virtualenv` python library using the command `pip install virtualenv` and then create a virtual environment using the command `virtualenv <environment name>` to run the program in. 
* After creating the virtual environment, change the directory to the root folder of the virtual environment using the `cd` command, then activate the environment using `Scritps\activate` command. You can confirm the activation, when the name of the environment appears within paranthesis before every command like `(environment name) C:/path to the environment`.
* Then copy the downloaded files inside the virtual environment directory.
* Then install the dependencies listed in the requirements.txt file on the virtual environment using the command `pip install -r requirements.txt`.
* To run the file type, `python app.py`. This will start the application, to use the application you can either copy the ip address appearing next to `* Running on` and paste it on a browser search bar or open a browser and type `localhost:5000` in the search bar.
* This will load a page identical to the one shown in the image above.

## How to use the app?
* Select the name of the Airline from the dropox.
* Select the Date of Departure and Date of Arrival respectively 
* Select the Source and Destination cities from their respective dropboxes.
* Select the Number of Stops from the dropbox. 
* Select the Additional Information from the dropbox, if there aren't any leave it as the default which is `No Info`.
* Select the Departure and Arrival Time.
* Select whether it is a One-Way or with Return ticket.
* Click on the Submit button.
* This will display the result, which is the range for the ticket price in the format `The price for the flight is around Rs. <lower limit> to Rs. <upper limit>.`. 

## Credits
* This project was made by referencing and applying the concepts learnt from [this vedio](https://www.youtube.com/watch?v=v5dqavbyE-I&list=PLZoTAELRMXVPzj1D0i_6ajJ6gyD22b3jh&index=4) on [Krish Naik's](https://github.com/krishnaik06) [YouTube channel](https://www.youtube.com/user/krishnaik06)
* The dataset used in this project is available at https://github.com/krishnaik06/5-Days-Live-EDA-and-Feature-Engineering/tree/main/Flight%20Prediction
