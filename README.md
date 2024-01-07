# Rewards-checker

This project contains a Python script to monitor transactions on your Sentry wallet and notify you via Telegram once rewards from node are granted.

## Prerequisites

- A Telegram account to interact with BotFather and create a bot.
- An account on [Alchemy](https://www.alchemy.com/) for accessing the Arbitrum network.

## Setup

### Step 1: Set Up the Telegram Bot

1. **Create a new Telegram bot:**
   - Send a message to [@BotFather](https://t.me/botfather) on Telegram.
   - Use the `/newbot` command and follow the instructions to create your bot.
   - At the end, BotFather will give you an API token for your bot.

2. **Retrieve the Chat ID using a Web Service:**
   - There are several web services that can help you find your Telegram chat ID. One option is to use `https://api.telegram.org/bot<YourBOTToken>/getUpdates`.
   - Replace `<YourBOTToken>` with your actual bot token.
   - Send a message to your bot in Telegram.
   - Open the above URL in your web browser. You'll get a JSON response where you can find your chat ID under `message.chat.id`.

### Step 2: Create an API on Alchemy for the Arbitrum Network

- Sign up or log in to [Alchemy](https://www.alchemy.com/).
- Create a new app, and when selecting the network, choose 'Arbitrum'.
- Copy the provided API URL which will be used to interact with the Arbitrum network.

### Step 3: Configure the Script

- Open `bot.py` and replace the values of `TELEGRAM_TOKEN`, `TELEGRAM_CHAT_ID`, `MY_WALLET_ADDRESS`, and `ARB_API_URL` with your own information.

### Step 4: Install Required Packages

- Ensure you have a `requirements.txt` file in your project directory with all the necessary packages.
- Install the required packages by running:
  pip install -r requirements.txt

### Step 5: Creating and Managing a Screen Session

To ensure that the script continues to run in the background, particularly useful on a remote server, you can utilize `screen`:

1. **Create a New Screen Session:**
   - Start a new session by running:
     screen -S bot
   - This command creates a new screen session named 'bot'.

2. **Run the Script:**
   - Within the screen session, start the script by executing:
     python3 bot.py. Note that the script checks transactions approximately each hour, so run it right before a challenge for the first time.

3. **Detach from the Screen Session:**
   - To detach and leave the script running in the background, press `Ctrl-A` followed by `D`.
   - This key combination detaches you from the screen session but keeps it running.

4. **Reattach to the Screen Session:**
   - If you need to check the script's output or interact with it, reattach to the session using:
     screen -r bot
   - This command reconnects you to the 'bot' screen session.

By using `screen`, your script will continue to monitor your wallet address on the Arbitrum network and send notifications via Telegram for any new transactions, even after you've logged out or closed the terminal.
