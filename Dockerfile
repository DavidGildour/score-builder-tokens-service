FROM python:3.6-alpine

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 5001

ENTRYPOINT ["python3"]

CMD ["run.py", "docker"]