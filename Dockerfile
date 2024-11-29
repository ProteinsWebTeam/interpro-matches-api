FROM python:3.12-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir .

EXPOSE 8000

CMD ["uvicorn", "matchesapi:app", "--host", "0.0.0.0", "--port", "8000"]
