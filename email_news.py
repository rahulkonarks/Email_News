import requests as rq
from send_email import send_email

topic = "tesla"
with open('/home/konarkguatam/API_KEY.txt', 'r') as file:
    api_key = file.read().strip('\n')
    url = f"https://newsapi.org/v2/everything?" \
          f"q={topic}" \
          f"&from=2022-11-14" \
          f"&sortBy=publishedAt" \
          f"&apiKey={api_key}" \
          f"&language=en"

request = rq.get(url)
content = request.json()

body = ""

for article in content['articles'][:20]:
    if article['title'] is not None:
        body = "Subject: Today's news" + '\n'\
               + body + article['title'] + '\n'\
               + article['description'] + '\n'\
               + article['url'] + 2 * '\n'

body = body.encode('utf-8')
send_email(message=body)
