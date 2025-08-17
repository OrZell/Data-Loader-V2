FROM python:slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY services ./services
ENV PYTHONPATH=/app
EXPOSE 8000
CMD ["uvicorn", "services.data_loader.app:app", "--host", "0.0.0.0", "--port", "8000"]