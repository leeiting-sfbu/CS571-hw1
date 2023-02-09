FROM python:latest

WORKDIR /code

COPY requirements.txt city_converter.py /code/

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

CMD ["python", "city_converter.py"]