FROM python:3.9.13-alpine3.16

WORKDIR /app

COPY . /app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh
CMD ./entrypoint.sh

# CMD python main.py