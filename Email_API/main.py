import requests
from send_email import send_email

topic = "apple"
api_key = "bfd5bf377c5f4f92b137814564f34662"
url = "https://newsapi.org/v2/everything?" \
      f"q={topic}&" \
      "from=2023-04-07&to=2023-04-07&" \
      "sortBy=popularity&" \
      "apiKey=bfd5bf377c5f4f92b137814564f34662&" \
      "language=en&" \
      "sortby=relevancy"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Acces the article titles and description
body = ""
for article in content["articles"][:20]:
    body = "Subject: Today's News" \
           + "\n" +body + article["title"] + "\n" \
           + article["description"] + "\n" \
           + article["url"] + 2*"\n"

# Send email
body = body.encode("utf-8")
send_email(message=body)