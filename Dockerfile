FROM ubuntu:20.04

RUN apt-get update
RUN apt-get -y install libgl1-mesa-glx

FROM public.ecr.aws/lambda/python:3.9

COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip
#RUN pip3 install wheel


RUN pip3 install opencv-contrib-python
RUN pip3 install tensorflow>=1.7
RUN pip3 install fer

RUN pip3 install -r requirements.txt
RUN cp main.py /var/task
CMD ["main.my_handler"]