import requests

api_key = "bfd5bf377c5f4f92b137814564f34662"
url = "https://newsapi.org/v2/everything?q=apple&from=2023-04-07&" \
      "to=2023-04-07&sortBy=popularity&" \
      "apiKey=bfd5bf377c5f4f92b137814564f34662"

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

# Acces the article titles and description
for article in content["articles"]:
    print(article["title"])