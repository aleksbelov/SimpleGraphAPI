FROM python:3.8
WORKDIR /app
COPY main.py requirements.txt ./
RUN pip install -r requirements.txt
CMD uvicorn main:app