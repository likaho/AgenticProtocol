# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.10-slim
# Install CA certificates
RUN apt-get update && apt-get install -y ca-certificates && apt-get install -y curl && apt-get clean

# Disable SSL verification
# ENV REQUESTS_CA_BUNDLE=""
USER root
WORKDIR /app
# Install pip requirements
COPY requirements.txt .
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade certifi
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org --upgrade pyopenssl
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt
COPY . .

EXPOSE 5000

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
# CMD ["python3", "app.py"]
# Set environment variables
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the Flask app
CMD ["flask", "run"]