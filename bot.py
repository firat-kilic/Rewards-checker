import asyncio
from web3 import Web3
from telegram.ext import Application

# Define the Telegram bot token, chat ID, your wallet address, and the API URL for Arbitrum mainnet.
TELEGRAM_TOKEN = "YourTelegramToken"
TELEGRAM_CHAT_ID = "YourChatId"
MY_WALLET_ADDRESS = "YourSentryWalletAddress"
ARB_API_URL = "YourBlockchainApiURL"

# Initialize a Web3 instance with the HTTP provider for the Arbitrum mainnet.
w3 = Web3(Web3.HTTPProvider(ARB_API_URL))

# Create a Telegram bot application with the specified token.
application = Application.builder().token(TELEGRAM_TOKEN).build()

async def check_wallet_transactions():
    # Get the initial transaction count for your wallet.
    initial_txn_count = w3.eth.get_transaction_count(MY_WALLET_ADDRESS)
    print(f"Initial Transaction Count: {initial_txn_count}")


    # Continuously check for new transactions.
    while True:
        current_txn_count = w3.eth.get_transaction_count(MY_WALLET_ADDRESS)
        # If a new transaction is found, send a message via Telegram.
        if current_txn_count > initial_txn_count:
            message = f"You got rewards from your XAI node !"
            await application.bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
            initial_txn_count = current_txn_count

        # Wait for a specified duration before checking again (~1h for each challenge).
        await asyncio.sleep(3670)

def main():
    # Run the wallet transaction check in an asynchronous event loop.
    asyncio.get_event_loop().create_task(check_wallet_transactions())
    # Start the Telegram bot.
    application.run_polling()

if __name__ == '__main__':
    main()
