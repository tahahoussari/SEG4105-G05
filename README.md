# Telegram Bot Setup Guide

Set up a simple Telegram bot that sends "Good morning." messages and responds to the `/chatid` command.

## Prerequisites

- **Python 3.7+** installed.

## Setup Instructions

### 1. Clone the repo `main.py`


### 2. Install Dependencies

Run:

```bash
pip install python-telegram-bot==20.3 apscheduler pytz python-dotenv
```

### 3. Create `.env` File

In the same directory as `main.py`, create a `.env` file:

```
BOT_TOKEN=YOUR_BOT_TOKEN_HERE
CHAT_ID=YOUR_CHAT_ID_HERE
```

- **BOT_TOKEN:** Ask Demian for this.
- **CHAT_ID:** Ask Demian for this.

### 4. Get Your Chat ID

- Run the bot:

  ```bash
  python main.py
  ```

- Send `/chatid` to your bot on Telegram.
- The bot will reply with the `CHAT_ID`.
- Update your `.env` file with this `CHAT_ID`.

## Running the Bot

With the `.env` file set, run:

```bash
python main.py
```

The bot will:

- Send "Good morning." daily at 7 AM Eastern Time.
- Respond to `/chatid` by providing the chat ID.

## Customization

- **Change Message:** Edit the text in `scheduled_morning_message`.
- **Change Time:** Modify `hour` and `minute` in the scheduler:

  ```python
  scheduler.add_job(scheduled_morning_message, 'cron', hour=NEW_HOUR, minute=NEW_MINUTE)
  ```

- **Change Time Zone:** Update the timezone:

  ```python
  scheduler = AsyncIOScheduler(timezone=pytz.timezone('Your/Timezone'))
  ```

## Notes

- **Security:** Do not share your `.env` file or bot token.
- **Dependencies:** Ensure all packages are installed as specified.# SEG4105-G05
