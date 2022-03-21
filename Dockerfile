FROM alpine:3.14



RUN apk add --no-cache python3-dev \
    && apk add py3-pip 


WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

CMD ["python3", "src/app.py"] 

