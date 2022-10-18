FROM python:3.10

# Workspace
WORKDIR /services/backend

# Install pip requirements
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt
COPY . .

COPY . /app

CMD ["python", "./app/main.py"]