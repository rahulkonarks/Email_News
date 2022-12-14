import requests as rq

with open('/home/konarkguatam/API_KEY.txt', 'r') as file:
    api_key = file.read().strip('\n')
    url = f"https://newsapi.org/v2/everything?" \
          f"q=tesla" \
          f"&from=2022-11-14" \
          f"&sortBy=publishedAt" \
          f"&apiKey={api_key}" \
          f"&language=en"

request = rq.get(url)
content = request.json()

body = ""

