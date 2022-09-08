FROM python:3.10.7
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_ENV="docker"
EXPOSE 8000
WORKDIR /app/server
ENTRYPOINT ["./local.sh"]