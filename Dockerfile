FROM public.ecr.aws/lambda/python:3.7

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN cp main.py /var/task
CMD ["main.my_handler"]