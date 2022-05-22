FROM python:3
ADD app.py /

RUN pip install -U discord.py-self python-dotenv
CMD ['python', './app.py']
