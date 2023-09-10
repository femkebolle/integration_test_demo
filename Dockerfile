FROM --platform=linux/amd64 python:3.10

WORKDIR /code

# upgrade pip
RUN pip install --upgrade pip

# Copy and install requirements
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY requirements-dev.txt ./
RUN pip install -r requirements-dev.txt

# Copy code
COPY src/ ./src
COPY tests/ ./tests
