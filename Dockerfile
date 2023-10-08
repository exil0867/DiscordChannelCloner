FROM python:3.11-slim-bookworm

RUN mkdir /config

VOLUME /config

ADD app.py .

ADD pyproject.toml .

ADD poetry.lock .

ADD install-deps.sh /tmp

RUN bash /tmp/install-deps.sh

CMD ["/root/.local/bin/poetry", "run", "python", "/app.py"]
