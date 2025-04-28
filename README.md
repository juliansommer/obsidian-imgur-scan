# Obsidian Imgur Scan

Scan an Obsidian notebook for Imgur URLs, and find which Imgur URLs aren't used in the notebook

## Setup

Follow these steps to run the project locally.

**Prerequisites**

Make sure the following are installed.

- [Git](https://git-scm.com)
- [Python](https://www.python.org)

**Cloning the Repository**

```bash
git clone https://github.com/juliansommer/obsidian-imgur-scan.git
cd obsidian-imgur-scan
```

**Creating a Virtual Environment**

On Windows
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

On MacOS/Linux
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Installing Dependencies**

```bash
pip install -r requirements.txt
```

**Set up `.env` file**

```bash
cp .env.example .env
```

Then fill in the `IMGUR_CLIENT_ID` with your Imgur client ID. You can get one by creating an app on [Imgur](https://api.imgur.com/oauth2/addclient). Make sure to select "OAuth 2 authorization without a callback URL" as the authorization type.
