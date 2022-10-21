FROM python:3.10

RUN mkdir /app

COPY app.py /app
COPY requirements.txt /app
COPY model /app/model
COPY preprocesing /app/preprocesing
COPY predict /app/predict

WORKDIR /app

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0"]

