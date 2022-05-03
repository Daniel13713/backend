# syntax=docker/dockerfile:1

FROM python:3.9.12

WORKDIR /app_workspace

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

ENV FLASK_APP=main.py
ENV FLASK_DEBUG=1
ENV FLASK_ENV=development

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
