FROM python:3.11-alpine
WORKDIR /code
ADD . /code
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
CMD ["python3", "main.py", "logger_config.ini"]