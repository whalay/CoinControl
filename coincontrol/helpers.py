import requests
import os
import uuid

"""
Helper functions are stored here

"""

def get_google_provider_cfg():
    try:
        response = requests.get(os.environ.get("GOOGLE_DISCOVERY_URL")).json()
    except Exception as e:
        return e
    return response


def generate_uuid() -> str:
    return str(uuid.uuid4())

