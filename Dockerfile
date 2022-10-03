FROM ubuntu:latest
RUN apt-get update -y
RUN apt-get install -y python-pip
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "main.py"]