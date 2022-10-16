# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10

# Install pip requirements
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt
COPY . .

# Workspace
WORKDIR /app
COPY . /app

CMD ["python", "main.py"]