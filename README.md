# Telco-Churn-Prediction-Deployment

*This readme is specifically to provide quick instruction on how to run and use the model deployment, not the analysis of the data itself

In this case i use Jupyter and VSCode which has different packages installed, thus to run all the code properly, the following packages must be installed:
In Jupyter, i use:
- numpy (pip install numpy)
- pandas (pip install pandas)
- matplotlib (pip install matplotlib)
- seaborn (pip install seaborn)
- scikit-learn (pip install -U scikit-learn)
- pickle (pip install pickle-mixin)

In VSCode:
- flask (pip install flask)
- pandas
- numpy
- pickle
- flasgger (pip install flasgger)

1. The first step is to import all of the packages, get the csv file ready and read through jupyter

![image](https://user-images.githubusercontent.com/78836385/126109566-c1f928b3-1cd0-439b-96e2-121e559c040c.png)


2. Then, run all of the Telco_Churn file (In my case i use jupyter), or you can just run the code from Machine Learning section and further until you successfully run the code to export the model

![image](https://user-images.githubusercontent.com/78836385/125919382-34abbcd3-5d69-43a3-989d-c87cc47d2f39.png)


3. After that we will be using VSCode from now on (you can use other source-code editor), first thing we will import all of the packages as seen in the image below

![image](https://user-images.githubusercontent.com/78836385/126111265-93aabe42-a074-49f0-b2d1-7555d92da7be.png)


4. To successfully run the app these two codes must be executed to indicate the start and end of the flask app code

![image](https://user-images.githubusercontent.com/78836385/126112045-a9682004-15e9-470d-9df2-9bb0a467765e.png)
![image](https://user-images.githubusercontent.com/78836385/126112097-958bf709-62bf-440e-9b6e-4238f0eeabf5.png)


5. Load the model from the jupyter file that you have exported and then assign it to variable, in this case i assigned it to model_telco
![image](https://user-images.githubusercontent.com/78836385/126112685-b12a830d-86df-4d34-bf1b-f7d69e033440.png)

6. Create a route for your flask app, the default route should be http://127.0.0.1:5000/ and it will your homepage, in this case the homepage should look like this

![image](https://user-images.githubusercontent.com/78836385/126113424-bdb31172-969e-4528-b04b-5041a812444f.png)


7. To start create function for prediction in the flaskapp, we need to create separate route for it as we use a customized template for flask (swagger)

![image](https://user-images.githubusercontent.com/78836385/126114774-8fe33741-c9a4-473e-a15c-01e8e7a06f47.png)


8. Then below is the parameters (features) that will be shown in the UI, the parameters represent the features we have in our data, so in this case we have a total of 19 parameters.

- The 'name' represent the variable name of the feature
- 'in' is the type of variables, because it is a query parameters we will write query in all of the parameters
- 'required' is whether data is mandatory to fill, because we need all of the features, we put all 'required' to be true

![image](https://user-images.githubusercontent.com/78836385/125920557-ab3fae9f-690d-4614-bf70-260cc49c90c2.png)

9. After you run the code you will get message on the terminal like this

![image](https://user-images.githubusercontent.com/78836385/125921643-c2eed22f-1257-4edd-bf93-cbb7dc2ed470.png)

10. Run wherever your local host it and then add /apidocs
or, click : http://127.0.0.1:5000/apidocs/

11. On your browser you it should direct you to flasggr UI, then input any data (As this is an early build, the value of the data must be exactly the same as the telco_churn original value)

![image](https://user-images.githubusercontent.com/78836385/125922092-da9e89e3-42e6-4c28-b575-07413d3e1159.png)

12. After clicking execute your response/answer wether the customer will churn or not located in the response body

![image](https://user-images.githubusercontent.com/78836385/125922483-faa5ba6e-53c1-443e-8ad6-87701ab3e72c.png)

