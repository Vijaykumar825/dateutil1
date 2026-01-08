FROM python:3.10-slim

WORKDIR /app

# Copy repository contents
COPY . .

# Install dependencies and the package in development mode
RUN pip install --no-cache-dir -e . && \
  pip install --no-cache-dir pytest

# Make test script executable
RUN chmod +x challenge/test.sh

CMD ["/bin/bash"]
