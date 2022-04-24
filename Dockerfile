FROM python:3.10-alpine

COPY /requirements.txt .

RUN pip install -r requirements.txt

COPY /app .

ENV FLASK_APP="app"

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run" ]
