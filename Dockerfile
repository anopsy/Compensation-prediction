
FROM python:3.10


WORKDIR /app
RUN pip install --upgrade pip setuptools

COPY . /app

RUN pip install --no-cache-dir -r requirements.txt


COPY rbf_model.joblib /app/
COPY scaler.joblib /app/


CMD ["streamlit", "run", "comp_app.py"]
