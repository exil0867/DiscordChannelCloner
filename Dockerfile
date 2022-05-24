FROM python:3

RUN mkdir /config

VOLUME /config

ADD app.py .

RUN pip install --upgrade pip

RUN pip install -U discord.py-self python-dotenv

CMD ["python", "./app.py"]