import re

url = input("What is your twitter account?").strip()

#username = url.removeprefix("https://twitter.com/")

matches = re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)$", url, flags= re.IGNORECASE)

if matches:
    print(f"Username is {matches.group(1)}")

username = re.sub(r"^(http(s)?://)?(www\.)?twitter\.com/","",url)

print(f"username is {username}")
