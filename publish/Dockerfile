FROM python:3.6

RUN pip install paho-mqtt==1.4.0

COPY . .

CMD ["python", "publish_topic.py"]