FROM public.ecr.aws/lambda/python:3.7

COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt --target /app
CMD ["main.my_handler"]