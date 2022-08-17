FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN python3 -m pip install --upgrade pip
RUN pip3 install -r requirements.txt
COPY . .
#RUN python3 manage.py collectstatic
EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "webserver.wsgi:application"]