FROM python:3.11

RUN pip install flask[async]==2.3.2

RUN pip install aiogram==2.25.1

WORKDIR ./workdir

COPY ./ ./

CMD ["python3", "app.py"]

EXPOSE 5002