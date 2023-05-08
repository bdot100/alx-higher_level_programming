#!/usr/bin/python3
"""sends a POST request to the passed URL
    with the email as a parameter, and displays
    the body of the response (decoded in utf-8)
Usage: ./2-post_email.py <URL> <EMAIL>
"""
import sys
import urllib.request
import urllib.parse


if __name__ == "__main__":
    url, email = sys.argv[1], sys.argv[2]
    value = {"email": email}
    send_data = urllib.parse.urlencode(value).encode("ascii")

    req = urllib.request.Request(url, send_data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf-8"))
