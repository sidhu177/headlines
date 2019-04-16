import feedparser
from flask import Flask
from flask import render_template
from flask import request
import json
from urllib.request import urlopen
import urllib
import urllib.parse
import urllib.request
import datetime
from flask import make_response 

app = Flask(__name__)

RSS_Feed = {'cbc':"https://www.cbc.ca/cmlink/rss-topstories",
             'ctv':"https://www.ctvnews.ca/rss/ctvnews-ca-top-stories-public-rss-1.822009"}

weather_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=cb932829eacb6a0e9ee4f38bfbf112ed"

default = {'city':'Toronto,Canada'}

def get_value_with_fallback(key):
    if request.args.get(key):
        return request.args.get(key)
    if request.cookies.get(key):
        return request.cookies.get(key)
    return default[key]

@app.route("/")
def home():
    publication = get_value_with_fallback("publication")
    articles = get_news(publication)

    city = get_value_with_fallback("city")
    weather = get_weather(city)

    response = make_response(render_template("home.html", articles=articles, weather=weather))
    expires = datetime.datetime.now() + datetime.timedelta(days=365)
    response.set_cookie("publication",publication, expires=expires)
    response.set_cookie("city",city,expires=expires)
    return response 

def get_news(publication):
    feed = feedparser.parse(RSS_Feed[publication.lower()])
    return feed['entries']

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
