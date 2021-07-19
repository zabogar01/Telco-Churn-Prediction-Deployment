# Telco-Churn-Prediction-Deployment

*This readme is specifically to provide quick instruction on how to run and use the model deployment, not the analysis of the data itself

In this case i use Jupyter and VSCode which has different packages installed, thus to run all the code properly, the following packages must be installed:
In Jupyter, i use:
- numpy (pip install numpy)
- pandas (pip install pandas)
- matplotlib (pip install matplotlib)
- seaborn (pip install seaborn)
- scikit-learn (pip install -U scikit-learn)


1. The first step is to run all of the Telco_Churn file (In my case i use jupyter), or you can just run the code from Machine Learning section and further until you successfully run the code to export the model

![image](https://user-images.githubusercontent.com/78836385/125919382-34abbcd3-5d69-43a3-989d-c87cc47d2f39.png)

2. After that open appflasggr file, we will use flask specifically flasgger to create the UI, load the model using the exported model name (in this case model_telco.pkl)

![image](https://user-images.githubusercontent.com/78836385/125919893-b3b0b78c-b32a-403f-ba50-2344a9c8d2e9.png)

3. Input your data feature in parameters which located in predict_churn() function (not the value)

![image](https://user-images.githubusercontent.com/78836385/125920557-ab3fae9f-690d-4614-bf70-260cc49c90c2.png)

4. After you run the code you will get message on the terminal like this

![image](https://user-images.githubusercontent.com/78836385/125921643-c2eed22f-1257-4edd-bf93-cbb7dc2ed470.png)

5. Run wherever your local host it and then add /apidocs
example: http://127.0.0.1:5000/apidocs/

6. On your browser you it should direct you to flasggr UI, then input any data (As this is an early build, the value of the data must be exactly the same as the telco_churn original value)

![image](https://user-images.githubusercontent.com/78836385/125922092-da9e89e3-42e6-4c28-b575-07413d3e1159.png)

7. After clicking execute your response/answer wether the customer will churn or not located in the response body

![image](https://user-images.githubusercontent.com/78836385/125922483-faa5ba6e-53c1-443e-8ad6-87701ab3e72c.png)

