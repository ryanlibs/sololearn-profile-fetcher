import sys
import json
import requests
import time

def fetch_guid(profile_id):
    url = f"https://www.sololearn.com/en/profile/{profile_id}"
    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
        "Upgrade-Insecure-Requests": "1"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response_text = response.text
        guid_start = response_text.find('"guid":"') + len('"guid":"')
        guid_end = response_text.find('"', guid_start)
        return response_text[guid_start:guid_end]
    else:
        return None

def fetch_bearer_token(guid, retries=10, delay=1):
    url = "https://www.sololearn.com/user/publicToken"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0",
        "Origin": "https://www.sololearn.com",
        "Referer": "https://www.sololearn.com/",
    }
    payload = {
        "subject": guid,
        # "checkboxCaptcha": "false",
        # "captchaToken": "03A..." # if you want to bypass captcha you can add this line

    }

    for attempt in range(retries): # try to fetch the token for a number of times to bypass the captcha not always 100% working though
        try:
            response = requests.post(url, headers=headers, json=payload)
            if response.status_code == 200:
                data = response.json()
                token = data.get("accessToken")
                if token:
                    return token  # Return the token if successfully fetched
            time.sleep(delay)
        except Exception as e:
            pass  # suppresses the error and continues the loop

    return None  # return none if the token is not found after all attempts


def fetch_profile_info(bearer_token, profile_id):
    url = f"https://api2.sololearn.com/v2/userinfo/v3/profile/{profile_id}"
    headers = {
        "Authorization": f"Bearer {bearer_token}",
        "Content-Type": "application/json",
        "Accept": "application/json",
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == "__main__":
    profile_id = sys.argv[1]
    guid = fetch_guid(profile_id)
    if guid:
        bearer_token = fetch_bearer_token(guid)
        if bearer_token:
            profile_info = fetch_profile_info(bearer_token, profile_id)
            if profile_info:
                print(json.dumps(profile_info))
            else:
                print(json.dumps({"error": "Failed to fetch profile information"}))
        else:
            print(json.dumps({"error": "Failed to fetch Bearer token"}))
    else:
        print(json.dumps({"error": "Failed to fetch GUID"}))
