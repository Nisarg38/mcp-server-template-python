FROM python:3.10-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY pyproject.toml ./
RUN pip install --no-cache-dir build && \
    pip install --no-cache-dir -e .

# Copy the rest of the code
COPY . .

# Environment variables
ENV PYTHONUNBUFFERED=1
ENV DEBUG=false

# Expose port for HTTP transport (optional)
EXPOSE 8080

# Command to run the server
CMD ["mcp-server-template", "--port", "8080"] 