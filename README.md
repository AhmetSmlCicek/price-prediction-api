# Description 

Here you can find the deployment of machine learning model built for real estate price prediction in Belgium.

Deployment is carried out through FASTAPI, Docker and Render. 

When a user provides required information -can be found in FASTAPI documentation- the user will receive a price prediction.

My api is accesible at https://ml-fastapi.onrender.com. When you go to this URL, you will see the Alive message.


# Installation 

To have a working api for use of prediction model, you need to firts log into Render.

You can log in with your Github account.

Once you logged in, you need to export all files in this repo into Render.

Render then asks you to follow steps -very easy and clear - to deploy the model and api.

When the deployment is over -you will see "live" words on Render dashboard- the URL of your api is ready to use.


# Usage

To test and see how the model works, you can use Postman.

Postman allows you to test the API and see the result that the prediction model gives.

There are 2 routes available at the URL : / (general route) and /predict

General route returns Alive message indicating that the server works.

At /predict route, two commands exists : GET and POST.

With GET command, the user will be able to see how real estate info should be provided (must-have features etc ).

With POST command, the real estate info is provided and in return, the user will received price prediction based on his query.   


