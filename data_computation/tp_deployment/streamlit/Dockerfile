FROM python:3.8

COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

COPY APP.md /app/
COPY app.py /app/
COPY .streamlit /app/

EXPOSE 8501
WORKDIR /app

CMD ["streamlit", "run", "app.py", "--server.enableWebsocketCompression=false", "--server.enableXsrfProtection=false", " --server.enableCORS=false"]
