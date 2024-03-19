FROM python:3.11
WORKDIR /code
ADD . /code
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]