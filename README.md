Financial Telegram Bot
Overview
This project is a Telegram bot designed to manage and track financial transactions. It integrates with an underlying SQL database to store transactional data and utilizes the power of OpenAI's language model for natural language processing capabilities.

Features
Expense Tracking: Users can send their expenses to the bot, which will then save them in the database.
Transaction Retrieval: Users can request to view all transactions stored in the database.
Natural Language Interaction: The bot employs OpenAI's language model to interpret user messages and respond accordingly.
Prerequisites
Before running the project, ensure you have the following dependencies installed:

Python 3.x
PostgreSQL database
Telegram API token
OpenAI API key and organization ID
Setup
Clone the repository to your local machine.
Install the required Python packages by running:
Copy code
pip install -r requirements.txt
Set up your PostgreSQL database and configure the .env file with your database credentials, Telegram API token, and OpenAI API key and organization ID.
Project Structure
.env: Configuration file for storing environment variables.
base.py: Module describing the database structure. Defines SQLAlchemy models and methods for database interaction.
gpt.py: Module integrating the language model with the bot's functionality. Establishes connections to the database and sets up the language model.
main.py: Entry point for the Telegram bot logic. Defines message handlers and invokes methods from other modules based on user interactions.
Usage
Run the main.py file to start the Telegram bot:
css
Copy code
python main.py
Interact with the bot via Telegram. Use commands like /start and /help to get started, and send messages to input expenses or request transaction information.
Contributing
Contributions are welcome! If you encounter any bugs or have suggestions for improvements, feel free to open an issue or submit a pull request.

License
This project is licensed under the MIT License.