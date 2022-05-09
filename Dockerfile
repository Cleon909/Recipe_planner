FROM python:3.10
copy . .
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]