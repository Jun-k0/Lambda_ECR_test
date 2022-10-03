FROM python:3.7
RUN apt-get update -y
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["main.my_handler"]