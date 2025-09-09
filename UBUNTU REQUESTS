import os
import requests
from urllib.parse import urlparse
import uuid

# Community: Program connects to the wider web by fetching from URLs.
# Respect: Handles errors gracefully without crashing.
# Sharing: Organizes fetched images into a directory for easy sharing.
# Practicality: Provides a reusable tool for saving images locally.

def fetch_image():
    # Prompt user for image URL
    url = input("Enter the URL of an image: ").strip()

    # Create directory if it doesn't exist
    save_dir = "Fetched_Images"
    os.makedirs(save_dir, exist_ok=True)

    try:
        # Attempt to download the image
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise error for bad HTTP status codes

        # Try to extract a filename from the URL
        parsed_url = urlparse(url)
        filename = os.path.basename(parsed_url.path)

        # If URL doesn’t end with a file name, generate one
        if not filename:
            filename = f"image_{uuid.uuid4().hex}.jpg"

        # Full path for saving the image
        file_path = os.path.join(save_dir, filename)

        # Save image in binary mode
        with open(file_path, "wb") as f:
            f.write(response.content)

        print(f"Image successfully saved to {file_path}")

    except requests.exceptions.MissingSchema:
        print("Invalid URL format. Please include http:// or https://")
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("Connection error. Please check your internet.")
    except requests.exceptions.Timeout:
        print("Request timed out. Try again later.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    fetch_image()
