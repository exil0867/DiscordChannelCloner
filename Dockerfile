FROM python:3.11-bookworm

RUN mkdir /config

VOLUME /config

ADD app.py .

RUN curl -sSL https://install.python-poetry.org | python3 -

RUN poetry install

CMD ["python", "./app.py"]
