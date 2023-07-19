# Use the official Python image as the base image
FROM python:3.10.6-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container
COPY requirements.txt .

# Install the required Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the bot_telegram.py file into the container
COPY bot_telegram.py .
COPY db.py .
COPY files.db .
COPY .env .

# Run the commands using subprocess in the container
RUN apt-get update && apt-get install -yqq dos2unix
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN dos2unix /docker-entrypoint.sh && chmod +x /docker-entrypoint.sh
ENTRYPOINT ["/docker-entrypoint.sh"]
