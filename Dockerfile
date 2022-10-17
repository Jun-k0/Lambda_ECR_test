FROM public.ecr.aws/lambda/python:3.6

COPY . /app
WORKDIR /app
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN cp main.py habit.py /var/task
CMD ["main.my_handler"]