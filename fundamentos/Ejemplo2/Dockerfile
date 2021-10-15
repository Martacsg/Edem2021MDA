FROM python:3.9.7
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY main.py main.py
EXPOSE 5000

CMD ["python","main.py"]

