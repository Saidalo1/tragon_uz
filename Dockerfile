# Base Python Alpine image
FROM python:3.9-alpine

# Install dependencies and tools
RUN apk add --no-cache build-base

# Create working directory inside the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project code into the container
COPY . .

# Run migrations
CMD python manage.py makemigrations
CMD python manage.py migrate

# Expose the port on which Django will run
EXPOSE 8000

# Run Django server
CMD python manage.py runserver 0.0.0.0:8000
