FROM python:3.10-slim-buster

COPY . .
RUN pip3 install -r requirements.txt

CMD ["python", "app.py"]