FROM python:3.10-alpine


COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ARG email_env="email@domain.com"
ARG password_env="password"
ENV email=${email_env}
ENV password=${password_env}
ENV FLASK_APP="app"

CMD [ "python3", "-m" , "flask", "run" ]