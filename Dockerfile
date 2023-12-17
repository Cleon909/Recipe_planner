FROM python:3.10
COPY . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]