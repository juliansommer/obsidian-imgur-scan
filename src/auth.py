import os

import pyimgur
from dotenv import load_dotenv


def get_imgur_auth() -> pyimgur.Imgur:
    """
    Get Imgur object with access token and refresh token.
    This will allow you to make authenticated requests to the Imgur API.
    This function will open a browser window for you to authorize the app.
    """
    # load environment variables from .env file
    load_dotenv()
    CLIENT_ID = os.getenv("IMGUR_CLIENT_ID")
    CLIENT_SECRET = os.getenv("IMGUR_CLIENT_SECRET")
    im = pyimgur.Imgur(CLIENT_ID, CLIENT_SECRET)

    # get authorization url
    # this will open a browser window for you to authorize the app
    auth_url = im.authorization_url("pin")
    print("Go to the following url to authenticate with Imgur:")
    print(auth_url)

    pin = input("What is the pin? ")
    access_token, refresh_token = im.exchange_pin(pin)

    # return imgur object with access token and refresh token
    # this will allow you to make authenticated requests to the imgur api
    im = pyimgur.Imgur(
        CLIENT_ID,
        CLIENT_SECRET,
        access_token,
        refresh_token,
    )
    return im
