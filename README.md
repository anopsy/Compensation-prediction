##Compensation Prediction
After performing the [ Juniors vs ChatGPT Data Analysis](https://github.com/anopsy/Juniors_vs_ChatGPT)
I decided I want to use the data that contain compensation estimation to build an app predicting compensation for a given engineering role.

##Run the app in a Docker container
To run the Streamlit app in a Docker container, follow these steps:


1. Install and configure Docker for your operating system. Make sure Docker is running.
2. Open a terminal or command prompt in the directory of the repo and run the following command: docker build -t compensation-app .
3. After the image is built, run a container from the image with the following command: docker run -p 8501:8501 compensation-app
4. You can now view your Streamlit app in your browser: http://0.0.0.0:8501
