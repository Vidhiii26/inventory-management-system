# Lightweight Python image (Updated to 3.13)
FROM python:3.13-slim

# Working directory set karein
WORKDIR /app

# Requirements copy karein aur install karein
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Baaki saara backend code copy karein
COPY . .

# Port expose karein
EXPOSE 8000

# Server run karne ki command
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]