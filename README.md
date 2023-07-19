# Telegram Bot with Docker Compose

This project sets up a Telegram bot using Docker Compose for easy development and deployment. The bot is built with Python and utilizes the `python-telegram-bot` library to interact with the Telegram API.

## File Directory

The project directory structure looks like this:

```
telegram-bot/
  ├── bot_telegram.py
  ├── docker-entrypoint.sh
  ├── Dockerfile
  ├── requirements.txt
  └── docker-compose.yml
```

- `bot_telegram.py`: The main Python script that contains the code for the Telegram bot. This script interacts with the `python-telegram-bot` library to handle incoming messages and perform actions.

- `docker-entrypoint.sh`: The shell script used as the entrypoint for the Docker container. It contains commands to install dependencies, run the bot, and perform any setup required.

- `Dockerfile`: The Dockerfile that defines the Docker image for the Telegram bot. It installs the required Python packages and sets up the environment for running the bot.

- `requirements.txt`: A text file listing the Python dependencies required for the bot. The `python-telegram-bot` library is specified here.

- `docker-compose.yml`: The Docker Compose file that orchestrates the setup for the Telegram bot. It defines the services, volumes, and environment variables needed to run the bot.

## Setup and Usage

Follow these steps to set up and run the Telegram bot:

1. Ensure you have Docker and Docker Compose installed on your system.

2. Clone this repository to your local machine:

   ```
   git clone <repository_url>
   cd telegram-bot
   ```

3. Make sure to edit the `bot_telegram.py` file with your specific bot logic and Telegram API token.

4. Run the Telegram bot using Docker Compose:

   ```
   docker-compose up -d
   ```

   This command will build the Docker image, start the bot container, and run it in detached mode (background).

5. To see the logs of the bot container, use:

   ```
   docker-compose logs -f
   ```

   The `-f` flag allows you to follow the log output in real-time.

6. To stop and remove the bot container, use:

   ```
   docker-compose down
   ```

## Development and Deployment

This setup allows for easy development and deployment of the Telegram bot:

- During development, you can modify the `bot_telegram.py` file on your host machine, and the changes will be immediately reflected in the running bot container without the need to rebuild the Docker image.

- For deployment, the entire Telegram bot, along with its dependencies, can be easily deployed to any server or cloud platform using Docker Compose.
