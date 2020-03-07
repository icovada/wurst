FROM python:3.8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /code
RUN pip install --upgrade pip
ADD requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . /code/

COPY entrypoint.sh /usr/src/app/entrypoint.sh
