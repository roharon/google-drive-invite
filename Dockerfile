FROM python:3.10-slim-buster

COPY . .
RUN pip install -r requirements.txt
RUN pip install gunicorn

CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]

