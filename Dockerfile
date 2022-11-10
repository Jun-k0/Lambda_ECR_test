FROM public.ecr.aws/lambda/python:3.8

COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip
#RUN pip3 install wheel
RUN pip3 install opencv-contrib-python==3.4.8.29
RUN pip3 install tensorflow>=1.7
RUN pip3 install fer

RUN pip3 install -r requirements.txt
RUN cp main.py /var/task
CMD ["main.my_handler"]