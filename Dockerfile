FROM python:3.8

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY ./ ./

# Default port used by Dash to serve the application, see app.run_server() in app.py
EXPOSE 8050

CMD ["python", "./src/app.py"]