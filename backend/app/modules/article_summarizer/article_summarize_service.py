import requests
import os
from dotenv import load_dotenv
import traceback

load_dotenv()

RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST")
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")


def article_summarize(article_url: str):
    try:
        if not article_url:
            return 1

        if not RAPIDAPI_HOST or not RAPIDAPI_KEY:
            raise ValueError("Missing RapidAPI credentials in environment variables.")

        # RapidAPI request setup
        url = f"https://{RAPIDAPI_HOST}/summarize"
        headers = {
            "X-RapidAPI-Key": RAPIDAPI_KEY,
            "X-RapidAPI-Host": RAPIDAPI_HOST,
        }
        params = {"url": article_url, "length": 3}

        # Make the API call
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            return {
                "error": f"RapidAPI returned an error: {response.status_code}",
                "details": response.text,
            }
    except Exception as e:
        traceback_str = traceback.format_exc()
        print(traceback_str)
        line_no = traceback.extract_tb(e.__traceback__)[-1][1]
        print(f"Exception occurred on line {line_no}")
        return str(e)
