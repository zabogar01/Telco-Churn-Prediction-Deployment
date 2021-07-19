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

3. After that open appflasggr.py file (in my case im using VSCode), we will use flask API specifically flasgger to create the UI, load the model using the exported model name (in this case model_telco.pkl)

![image](https://user-images.githubusercontent.com/78836385/125919893-b3b0b78c-b32a-403f-ba50-2344a9c8d2e9.png)

4. Input your data feature in parameters which located in predict_churn() function (not the value)

![image](https://user-images.githubusercontent.com/78836385/125920557-ab3fae9f-690d-4614-bf70-260cc49c90c2.png)

5. After you run the code you will get message on the terminal like this

![image](https://user-images.githubusercontent.com/78836385/125921643-c2eed22f-1257-4edd-bf93-cbb7dc2ed470.png)

6. Run wherever your local host it and then add /apidocs
or, click : http://127.0.0.1:5000/apidocs/

7. On your browser you it should direct you to flasggr UI, then input any data (As this is an early build, the value of the data must be exactly the same as the telco_churn original value)

![image](https://user-images.githubusercontent.com/78836385/125922092-da9e89e3-42e6-4c28-b575-07413d3e1159.png)

8. After clicking execute your response/answer wether the customer will churn or not located in the response body

![image](https://user-images.githubusercontent.com/78836385/125922483-faa5ba6e-53c1-443e-8ad6-87701ab3e72c.png)

