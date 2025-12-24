FROM python:3.12-slim

ENV PYTHONUNBUFFERED=1
WORKDIR /app

# System dependencies needed for mysqlclient and Pillow
RUN apt-get update \
    && apt-get install -y \
        gcc \
        pkg-config \
        default-libmysqlclient-dev \
        python3-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app/

# Expose Django port
EXPOSE 8000
