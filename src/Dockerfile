# Base Image, we are using the official Python 3.10.10-slim-buster image from Docker Hub
FROM python:3.10.10-slim-buster

# Working Directory
WORKDIR /usr/tfd/src

# Set Environment Variables

# :Prevents Python from writing pyc files to disc, which is the default behavior
ENV PYTHONDONTWRITEBYTECODE 1
# :Prevents Python from buffering stdout and stderr, which is the default behavior
ENV PYTHONUNBUFFERED 1

# Install System Dependencies
RUN apt update \
    && apt -y install netcat gcc \
    && apt clean

# Install Python Dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .

# Cache Python Packages to the Docker Host:
# using the BuildKit: an optin image building engine which offers substantial improvements over the traditional process.
# new caching mechanism that can cache these dependencies download, instead of downloading them each time.
RUN --mount=type=cache,target=/root/.cache \
    pip install -r requirements.txt

# Add app, copy all files from src to the working directory
COPY . .

# Run uvicorn server, with the reload flag to enable hot reloading
CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8008"]