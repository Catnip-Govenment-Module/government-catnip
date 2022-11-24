FROM python:3.9

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

# Export the container port for outsider to connect.
EXPOSE 80

CMD ["python", "app/main.py"]