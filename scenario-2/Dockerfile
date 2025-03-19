FROM python:3.9-alpine

WORKDIR /app

COPY script.py /app/

RUN pip install boto3

CMD ["python", "/app/script.py"]
