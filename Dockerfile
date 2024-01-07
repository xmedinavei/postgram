FROM python:3.11-alpine
ENV PYTHONUNBUFFERED=1
WORKDIR /postgram_app
COPY ./requirements.txt /postgram_app
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt --no-cache-dir