FROM python:3.11
WORKDIR /root
RUN rm -f /root/.my.cnf

RUN apt-get update && apt-get install -y mariadb-client
COPY . .
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["python3", "main.py"]
