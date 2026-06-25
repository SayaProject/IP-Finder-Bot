

#  IP Finder Bot for Telegram 

.

## Sample Output
![IP Finder Bot Sample](https://files.catbox.moe/7m08g5.png)

## ✨ Features
- **IP Address Lookup**: Enter an IP address to get detailed information 🔎.
- **IPv4 and IPv6 Support**: Handles both IPv4 and IPv6 address formats 🔄.
- **Geographical Information**: Provides details like country 🏳️, city 🏙, region, and postal code 📬.
- **ISP Information**: Retrieves the Internet Service Provider associated with the IP 🌐.
- **Interactive Map**: Shares a static map pinpointing the IP address location 🗺, generated using the [LocationIQ Maps API](https://docs.locationiq.com/docs/maps).
- **Inline Query Support**: Use the bot in any conversation through inline queries 🔍.
- **Privacy Focused**: Does not store user queries 🛡.

## 🗺 Utilizing LocationIQ Maps API for Map Images
The bot generates map images for IP locations using the LocationIQ Maps API:

### 🚀 Getting Started with LocationIQ Maps API
1. Obtain an API key by signing up for a free LocationIQ account 🔑.
2. Use the Static Map service by constructing a URL with the location's latitude and longitude, and your API key 📍.

### 📌 Example API Request
```
https://maps.locationiq.com/v3/staticmap?key=YOUR_LOCATIONIQ_API_KEY&center=LATITUDE,LONGITUDE&zoom=16&size=600x600&markers=icon:large-blue-cutout|LATITUDE,LONGITUDE
```
*Replace `YOUR_LOCATIONIQ_API_KEY`, `LATITUDE`, and `LONGITUDE` with your LocationIQ API key and the geographical coordinates.*

## 🚀 Deployment

Set Environmentals variable before deploy. -  [Instructions](#-installation-steps)

[![Deploy with heroku](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)
[![Deploy to Netlify](https://www.netlify.com/img/deploy/button.svg)
[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy)

## ⚙️ Installation

To use this bot, you need to have Python installed on your machine along with some specific libraries. Follow the steps below to set up and run the bot:

### 📋 Prerequisites
- Python 3.6 or newer 🐍
- A Telegram Bot Token 🤖 (obtained from [BotFather](https://t.me/botfather))
- An IPinfo API token 🔑 (obtain from [IPinfo](https://ipinfo.io/))

### 📚 Required Libraries
- `pyrogram` - A modern, elegant, and asynchronous Telegram MTProto API framework 🚀.
- `ipinfo` - For fetching IP details 🌍.
- `requests` - For making HTTP requests 🌐.

### 🔧 Installation Steps
1. Clone this repository or download the script 📁.
2. Install the required Python libraries using pip:
    ```
    pip install pyrogram ipinfo requests
    ```
3. Create a `config.py` file in the same directory as the script with the following content, replacing `YOUR_API_ID`, `YOUR_API_HASH`, `YOUR_BOT_TOKEN`, and `YOUR_IPINFO_ACCESS_TOKEN` with your actual details:
    ```python
    class con:
        API_ID = 'YOUR_API_ID'  # Your API ID (as a string) 🆔
        API_HASH = 'YOUR_API_HASH'  # Your API Hash (as a string) 🔐
        BOT_TOKEN = 'YOUR_BOT_TOKEN'  # Your Bot Token (as a string) 🤖
        IP_API = 'YOUR_IPINFO_ACCESS_TOKEN'  # Your IPinfo Access Token (as a string) 🔑
    ```
4. Run the bot 🏃‍♂️:
    ```
    python main.py
    ```

---
## 📖 How to use bOT
- **Start the Bot**: Send `/start` to see the welcome message 🚀.
- **Find IP Information**: Send any IP address 📧.
- **Inline Query**: Type `@YourBotUsername IP_ADDRESS` in any chat 🔍.

## 🚀 Original Bot
Access the original bot [here](https://t.me/IPfinderobo_bot).

---

