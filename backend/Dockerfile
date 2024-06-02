FROM python:3.11-alpine
RUN apk update && \
    apk add --no-cache ruby ruby-dev
WORKDIR /
RUN gem install vinbot
WORKDIR /code
ADD . /code
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
CMD ["python3", "main.py", "logger_config.ini"]