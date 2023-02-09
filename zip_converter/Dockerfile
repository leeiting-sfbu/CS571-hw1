FROM python:latest

WORKDIR /code

COPY requirements.txt zip_converter.py /code/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["python", "zip_converter.py"]