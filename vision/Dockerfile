# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10

# Workspace
WORKDIR /services/vision

# Install pip requirements
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt
COPY . .

COPY . /app

CMD ["python", "./app/main.py"]