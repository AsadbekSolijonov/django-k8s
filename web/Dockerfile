FROM python:3.11.4-slim

COPY . /app

WORKDIR /app

RUN python3 -m venv venv

RUN /opt/venv/bin/pip install --upgrade pip

RUN /opt/venv/bin/pip install -r requirements.txt

RUN chmod +x entrypoint.sh

CMD [ "/app/entrypoint.sh" ]

