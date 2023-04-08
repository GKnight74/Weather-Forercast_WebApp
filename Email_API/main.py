import requests
from send_email import send_email

api_key = "bfd5bf377c5f4f92b137814564f34662"
url = "https://newsapi.org/v2/everything?q=apple&from=2023-04-07&" \
      "to=2023-04-07&sortBy=popularity&" \
      "apiKey=bfd5bf377c5f4f92b137814564f34662"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Acces the article titles and description
body = ""
for article in content["articles"]:
    body = body + article["title"] + "\n" + article["description"] + 2*"\n"

# Send email
body = body.encode("utf-8")
send_email(message=body)