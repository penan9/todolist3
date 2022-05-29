FROM python:3.9.13-slim
FROM gcc:12.1.0

RUN mkdir -p /home/todo

WORKDIR /home/todo

COPY requirements.txt .

RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5001

ENTRYPOINT [ "python3" ]

CMD ["app.py" ]