Alien Project Bot 🚀👽
================================

Welcome to the **Alien Project Bot**! This is a fun, interactive Telegram bot that provides various alien-themed functionalities, including diplomatic tips, UFO sightings, ISS (International Space Station) information, and a Klingon translator. You can also explore some out-of-this-world data and have a bit of fun with quirky commands!

Features ✨
----------

1.  **Start**: Initialize the bot and view available options.
2.  **Diplomatic Tips**: Receive a random alien diplomatic tip.
3.  **UFO Data**: Get random UFO sighting data.
4.  **Klingon Translator**: Translate text into mock Klingon (reverse the text as a fun twist).
5.  **ISS Info**: Get the current position of the International Space Station (ISS).
6.  **Exit**: End the conversation and exit the bot.

Installation 🛠️
----------------

1.  Clone this repository:

bash

Copy

`git clone https://github.com/amirdhs/Alien-with-TelegramBot.git
cd hackathon-alien-project`

1.  Install the required dependencies:

bash

Copy

`pip install python-telegram-bot requests`

1.  Replace the placeholder **BOT_TOKEN** in the script with your own Telegram Bot Token (obtained from BotFather).
2.  Run the bot:

bash

Copy

`python bot.py`

Usage 💬
--------

Once the bot is up and running, you can interact with it on Telegram. Here are the available commands:

-   **/start**: Start the bot and view the available options.
-   **Enter a number (1-5)**: Choose an option to explore specific features.
-   **Text for Klingon Translation**: Input text, and the bot will return the translated text in mock Klingon (by reversing the text).

Code Structure 📂
-----------------

-   **Main Bot Logic**: Defined in the `main()` function where we set up the bot and conversation handler.
-   **States**: The bot uses a conversation handler with two states:
    -   `CHOOSING`: Displays the menu and handles numeric selections.
    -   `TRANSLATING`: Handles the Klingon translation functionality.
-   **Diplomatic Tips**: The bot returns random diplomatic tips using a predefined list.
-   **UFO Data**: Provides mock UFO sighting data for fun.
-   **ISS Info**: Retrieves live data on the ISS position using an external API.

Example Interactions 💥
-----------------------

-   **Start Command**:
    -   The bot will ask you to choose from a list of options.
-   **Diplomatic Tip Command**:
    -   Bot responds with a random diplomatic tip.
-   **UFO Data Command**:
    -   Bot sends a random UFO sighting report.
-   **Klingon Translator**:
    -   The bot translates text by reversing it for fun.
-   **ISS Info**:
    -   Get live ISS position data.
