FROM python:3.8.5-buster
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 5000
COPY src/ .
CMD [ "python", "./infer.py" ]