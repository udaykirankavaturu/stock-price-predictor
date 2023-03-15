FROM python:3.9-slim-buster
WORKDIR /app
COPY . /app
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 5000
CMD python3 app.py