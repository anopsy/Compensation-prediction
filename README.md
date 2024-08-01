## Compensation Prediction for Engineering Roles
![image](https://github.com/user-attachments/assets/aa1a72be-488b-46f8-842d-aeba8db7ed5f)



After analyzing the data from the [Juniors vs ChatGPT study](https://github.com/anopsy/Juniors_vs_ChatGPT), I decided to use the compensation estimation data to build an app that predicts compensation for various engineering roles. 
After cleaning, I built a baseline model and later experimented with different regression models. After hyperparameters tuning I decided to go for the SVC model with rbf kernel. 
The model was developed using data provided by [SourceStack](https://sourcestack.co/).

### Running the App in a Docker Container
To run the Streamlit app in a Docker container, follow these steps:

1. Clone this repository and open in VS Code.
2. Install and configure Docker for your operating system. Make sure Docker is running.
3. Open a terminal or command prompt in the directory of the repo and run the following command: 
```
docker build -t compensation-app .
```
4. After the image is built, run a container from the image with the following command: 
```
docker run -p 8501:8501 compensation-app
```
5. You can now view your Streamlit app in your browser: http://0.0.0.0:8501

### Running the App locally
To run the Streamlit app locally, follow these steps:

1. Clone this repository and open in VS Code.
2. Install the required libraries listed in `requirements.txt` using 
```
pip install -r requirements.txt
```
3. Open a terminal or command prompt in the directory of the repo and run the following command: 
```
streamlit run ./comp_app.py
```
4. You can now view the Compensation App in your browser by following one of the links from your terminal

### Next steps
I would like to fine-tune the model for Data Science jobs specifically.
