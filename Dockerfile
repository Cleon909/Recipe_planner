FROM python:3.10
copy . .
RUN pip install -r requirements.txt
ENTRYPOINT ["python3", "app.py"]