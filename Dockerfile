FROM python:3.11-slim-bookworm

RUN mkdir /config

VOLUME /config

ADD app.py .

ADD pyproject.toml .

ADD poetry.lock .

RUN curl -sSL https://install.python-poetry.org | python3 -

RUN /root/.local/bin/poetry install

CMD ["/root/.local/bin/poetry", "run", "python", "/app.py"]