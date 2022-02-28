# eg.notification

HOW TO RUN Notification Microservice

1. pip install -r requirements.txt
2. cd app
3. export email="YOUR_EMAIL_HERE"
4. export password="YOUR_PASSWORD_HERE"
5. export FLASK_APP="app"
6. flask run

TO Build Docker Image
docker build -t testing --build-arg email_env=YOUR_EMAIL_HERE --build-arg password_env=YOUR_PASSWORD_HERE --no-cache .