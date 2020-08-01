FROM python:3
ADD app-tracker/app-tracker-server.py /
ADD apps.json /
RUN pip install flask
RUN pip install -U flask-cors
CMD ["python", "./app-tracker-server.py"]