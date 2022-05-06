FROM python:3.10
copy . .
RUN pip3 install -r requirements.txt
run python create.py
ENTRYPOINT ["python3", "app.py"]