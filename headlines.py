import feedparser
from flask import Flask
from flask import render_template
from flask import request
import json
from urllib.request import urlopen
import urllib
import urllib.parse
import urllib.request

app = Flask(__name__)

RSS_Feed = {'cbc':"https://www.cbc.ca/cmlink/rss-topstories",
             'ctv':"https://www.ctvnews.ca/rss/ctvnews-ca-top-stories-public-rss-1.822009"}

weather_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=cb932829eacb6a0e9ee4f38bfbf112ed"

DEFAULTS = {'city':'Toronto,Canada'}

@app.route("/")
def get_news():
    query = request.args.get("publication")
    if not query or query.lower() not in RSS_Feed:
        publication = "cbc"
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_Feed[publication])
    city = request.args.get('city')
    if not city: 
        city = DEFAULTS['city']
    weather = get_weather(city)
    return render_template("home.html", articles=feed['entries'],weather=weather )

def get_weather(query):
    query = urllib.parse.quote(query)
    url = weather_url.format(query)
    data = urllib.request.urlopen(url).read()
    parsed = json.loads(data)
    weather = None
    if parsed.get('weather'):
        weather = {'description':parsed['weather'][0]['description'],
                   'temperature':parsed['main']['temp'],
                   'city':parsed['name'],
                   'country':parsed['sys']['country']
                   }
    return weather

if __name__=='__main__':
    app.run(port=5000)
