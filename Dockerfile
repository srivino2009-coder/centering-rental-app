FROM python:3.11-slim

WORKDIR /app

COPY . .

EXPOSE 4000

CMD ["python", "demo_server.py"]
