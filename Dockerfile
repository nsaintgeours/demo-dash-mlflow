FROM python:3.8

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY ./ ./

EXPOSE 8050

CMD ["python", "./src/app.py"]