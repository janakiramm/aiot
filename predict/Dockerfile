FROM python:3.8.5-buster
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
CMD [ "python", "./predict.py" ]